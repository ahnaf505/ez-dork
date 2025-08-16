from typing import Dict, List
from browser import *
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description='ez-dork ~ Simplify dorking on 5+ search engines',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  Basic search:        python ez_dork.py -k "admin login"
  Filetype filter:     python ez_dork.py -k password -f pdf docx  OR  -f "pdf,docx"
  Site-specific:      python ez_dork.py -k "error message" -s example.com
  Multi-word inputs:  python ez_dork.py --intitle "login page" --inurl "admin panel"

Note: Use quotes ("") for multi-word inputs (e.g., "admin login")"""
    )

    # Search parameters
    search_group = parser.add_argument_group('Search Parameters (use quotes for multi-word inputs)')
    search_group.add_argument('-k', '--keyword', 
                             help='Query keywords (use quotes for multi-word, e.g., "admin login")')
    search_group.add_argument('-e', '--exclude', 
                             help='Exclude word/phrase (use quotes for multi-word)')
    search_group.add_argument('-f', '--filetype', nargs='+',
                             help='File extensions (space/comma-separated, e.g., pdf docx OR "pdf,docx")')
    search_group.add_argument('-s', '--site', nargs='+',
                             help='Target sites (space/comma-separated, e.g., example.com OR "a.com,b.com")')
    search_group.add_argument('--intitle', 
                             help='Text in page title (use quotes for multi-word)')
    search_group.add_argument('--inurl', 
                             help='Text in URL (use quotes for multi-word)')
    search_group.add_argument('--intext', 
                             help='Text in page content (use quotes for multi-word)')

    # Options
    opt_group = parser.add_argument_group('Options')
    opt_group.add_argument('--output', '-o', default="query_result.txt",
                          help='Output file (default: query_result.txt)')
    opt_group.add_argument('--headless', action='store_true',
                          help='Enable headless browser mode')
    opt_group.add_argument('--randombrowseragent', action='store_true',
                          help='Use random browser user-agent')

    args = parser.parse_args()

    # Validate at least one search parameter exists
    if not any([args.keyword, args.exclude, args.filetype, 
                args.site, args.intitle, args.inurl, args.intext]):
        parser.print_help()
        sys.exit("\nError: At least one search parameter is required!")

    if args.filetype:
        args.filetype = ','.join(ft.strip() for ft in args.filetype)
    if args.site:
        args.site = ','.join(s.strip() for s in args.site)

    return args


def construct_query_str(args, varies=False):
    google_query_str = []
    bing_query_str = []
    duckduckgo_query_str = []
    yahoo_query_str = []
    scribd_query_str = []
    brave_query_str = []

    def generate_keyword_variations(keyword):
        # not implemented yet :(
        return "type shi"
    if varies:
        keyword_variations = generate_keyword_variations(args.keyword)

    # Base query components
    base_components = []
    if args.exclude:
        base_components.append(f'-{args.exclude}')
    if args.filetype:
        base_components.append(f'filetype:{args.filetype}')
    if args.site:
        base_components.append(f'site:{args.site}')
    if args.intitle:
        base_components.append(f'intitle:{args.intitle}')
    if args.inurl:
        base_components.append(f'inurl:{args.inurl}')
    if args.intext:
        base_components.append(f'intext:{args.intext}')

    # Construct queries for each keyword variation
    for keyword in keyword_variations:
        base_query = f'"{keyword}"'  # Exact match for the keyword
        
        # Google query
        google_query = f'{base_query} {" ".join(base_components)}'.strip()
        google_query_str.append(google_query)
        
        # Other search engines use the same query format
        bing_query_str.append(google_query)
        duckduckgo_query_str.append(google_query)
        yahoo_query_str.append(google_query)
        scribd_query_str.append(google_query)
        brave_query_str.append(google_query)

    return {
        'google': list(set(google_query_str)),  # Remove duplicates
        'bing': list(set(bing_query_str)),
        'duckduckgo': list(set(duckduckgo_query_str)),
        'yahoo': list(set(yahoo_query_str)),
        'scribd': list(set(scribd_query_str)),
        'brave': list(set(brave_query_str))
    }





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


if __name__ == "__main__":
    args = parse_args()
    queries = construct_query_str(args)
    print(queries)
