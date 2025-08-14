from fastapi import FastAPI, Query
import threading
import queue
from typing import Dict, List

from browser import *

search_queue = queue.Queue()
stop_event = threading.Event()

results_store: Dict[str, List[Dict[str, str]]] = {}  # {query: [{"title": ..., "link": ..., "desc": ...}]}

def query_engine(engine_func, query_str):
    results = engine_func([query_str])
    return [
        {"title": r[0], "link": r[1], "desc": r[2]}
        for r in results if len(r) >= 3
    ]

def mass_query(query_str):
    engines = [
        google_queries,
        bing_queries,
        duckduckgo_queries,
        yahoo_queries,
        scribd_queries,
        brave_queries
    ]
    aggregated = []
    for engine in engines:
        try:
            engine_results = query_engine(engine, query_str)
            aggregated.extend(engine_results)
        except Exception as e:
            print(f"Error in {engine.__name__}: {e}")
    return aggregated

def search_worker():
    while not stop_event.is_set():
        try:
            query = search_queue.get(timeout=0.5)
        except queue.Empty:
            continue
        if query is None:
            break

        print(f"[INFO] Starting search for: {query}")
        res = mass_query(query)
        results_store[query] = res
        print(f"[INFO] Search finished for: {query}")
        search_queue.task_done()


app = FastAPI()

@app.on_event("startup")
def startup_event():
    threading.Thread(target=search_worker, daemon=True).start()

@app.on_event("shutdown")
def shutdown_event():
    stop_event.set()
    search_queue.put(None)

@app.post("/search/")
def enqueue_search(query: str = Query(..., description="Search keyword")):
    search_queue.put(query)
    return {"status": "queued", "query": query}

@app.get("/results/{query}")
def get_results(query: str):
    return {
        "query": query,
        "results": results_store.get(query, [])
    }
