from typing import Dict, List
from browser import *

results_store: Dict[str, List[Dict[str, str]]] = {}

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
            print(f"Searching {engine.__name__}...")
            engine_results = query_engine(engine, query_str)
            aggregated.extend(engine_results)
        except Exception as e:
            print(f"Error in {engine.__name__}: {e}")
    return aggregated

def build_query(params: dict) -> str:
    query_parts = []
    if params.get("keywords"):
        query_parts.append(params["keywords"])
    if params.get("exclude"):
        query_parts.append(f"-{params['exclude']}")
    if params.get("filetype"):
        query_parts.append(f"filetype:{params['filetype']}")
    if params.get("site"):
        query_parts.append(f"site:{params['site']}")
    if params.get("intitle"):
        query_parts.append(f"intitle:{params['intitle']}")
    if params.get("inurl"):
        query_parts.append(f"inurl:{params['inurl']}")
    if params.get("intext"):
        query_parts.append(f"intext:{params['intext']}")
    if params.get("extensions"):
        exts = [ext.strip() for ext in params["extensions"].split(",") if ext.strip()]
        query_parts.append(" OR ".join([f"ext:{ext}" for ext in exts]))
    return " ".join(query_parts)

def display_results(results: List[Dict[str, str]]):
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Title: {result['title']}")
        print(f"URL: {result['link']}")
        print(f"Description: {result['desc']}")

def main():
    print("Dork Search CLI")
    print("Enter your search parameters (leave blank to skip):")
    
    params = {
        "keywords": input("Keywords: ").strip(),
        "exclude": input("Exclude terms: ").strip(),
        "filetype": input("Filetype: ").strip(),
        "site": input("Site: ").strip(),
        "intitle": input("In title: ").strip(),
        "inurl": input("In URL: ").strip(),
        "intext": input("In text: ").strip(),
        "extensions": input("Extensions (comma-separated): ").strip()
    }
    
    query = build_query(params)
    print(f"\nGenerated dork: {query}")
    
    if not query.strip():
        print("Error: No search parameters provided")
        return
    
    print("\nStarting search...")
    results = mass_query(query)
    results_store[query] = results
    
    print(f"\nFound {len(results)} results:")
    display_results(results)

if __name__ == "__main__":
    main()