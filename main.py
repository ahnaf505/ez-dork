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
    search_group.add_argument('-f', '--filetype',
                             help='File extension, e.g. pdf')
    search_group.add_argument('-s', '--site',
                             help='Target site, e.g. example.com')
    search_group.add_argument('-t', '--intitle', 
                             help='Text in page title (use quotes for multi-word)')
    search_group.add_argument('-u', '--inurl', 
                             help='Text in URL (use quotes for multi-word)')
    search_group.add_argument('-x', '--intext', 
                             help='Text in page content (use quotes for multi-word)')

    # Options
    opt_group = parser.add_argument_group('Options')
    opt_group.add_argument('-o', '--output', default="query_result.txt",
                          help='Output file (default: query_result.txt)')
    opt_group.add_argument('-n', '--non-exact-match', action='store_true',
                          help='Add non-exact match to the search query')
    opt_group.add_argument('-d', '--headless', action='store_true',
                          help='Enable headless browser mode')
    opt_group.add_argument('-r', '--randombrowseragent', action='store_true',
                          help='Use random browser user-agent')
    opt_group.add_argument('-v', '--verbose', action='store_true',
                          help='Output every single search result to terminal')

    args = parser.parse_args()

    # Validation
    if not any([args.keyword, args.exclude, args.filetype, 
                args.site, args.intitle, args.inurl, args.intext]):
        parser.print_help()
        sys.exit("\nError: At least one search parameter is required!")(ft.strip() for ft in args.filetype)

    return args

def detect_multi_word(text):
    if not text.strip():
        return []
    words = text.split()
    # note : Return true if its multi word
    if len(words) == 1:
        return False
    else:
        return True

def generate_keyword_variations(keyword):
        # not implemented yet :(
        return "type shi"


def construct_query_str(args):
    keyword = args.keyword
    google_query_str = []
    bing_query_str = []
    duckduckgo_query_str = []
    yahoo_query_str = []
    scribd_query_str = []
    brave_query_str = []

    google_base_str = ""
    bing_base_str = ""
    duckduckgo_base_str = ""
    yahoo_base_str = ""
    brave_base_str = ""
    if args.exclude:
        google_base_str += f' -{args.exclude}'
        bing_base_str += f' -{args.exclude}'
        duckduckgo_base_str += f' -{args.exclude}'
        yahoo_base_str += f' -{args.exclude}'
        brave_base_str += f' -{args.exclude}'
    if args.filetype:
        google_base_str += f' filetype:{args.filetype}'
        bing_base_str += f' ext:{args.filetype}'
        duckduckgo_base_str += f' filetype:{args.filetype}'
        yahoo_base_str += f' filetype:{args.filetype}'
        brave_base_str += f' ext:{args.filetype}'
    if args.site:
        google_base_str += f' site:{args.site}'
        bing_base_str += f' site:{args.site}'
        duckduckgo_base_str += f' site:{args.site}'
        brave_base_str += f' site:{args.site}'
    if args.intitle:
        google_base_str += f' intitle:{args.intitle}'
        bing_base_str += f' intitle:{args.intitle}'
        duckduckgo_base_str += f' intitle:{args.intitle}'
        yahoo_base_str += f' intitle:{args.intitle}'
        brave_base_str += f' intitle:{args.intitle}'
    if args.inurl:
        google_base_str += f' inurl:{args.inurl}'
        duckduckgo_base_str += f' inurl:{args.inurl}'
        yahoo_base_str += f' inurl:{args.inurl}'
    if args.intext:
        google_base_str += f' intext:{args.intext}'
        bing_base_str += f' intext:{args.intext}'
        brave_base_str += f' inpage:{args.intext}'

        
    # Exact query
    google_query_str.append(keyword + google_base_str)
    bing_query_str.append(keyword + bing_base_str)
    duckduckgo_query_str.append(keyword + duckduckgo_base_str)
    yahoo_query_str.append(keyword + yahoo_base_str)
    scribd_query_str.append(keyword)
    brave_query_str.append(keyword + brave_base_str)

    google_query_str.append(f'"{keyword}"' + google_base_str)
    bing_query_str.append(f'"{keyword}"' + bing_base_str)
    duckduckgo_query_str.append(f'"{keyword}"' + duckduckgo_base_str)
    yahoo_query_str.append(f'"{keyword}"' + yahoo_base_str)
    scribd_query_str.append(f'"{keyword}"')
    brave_query_str.append(f'"{keyword}"' + brave_base_str)

    if args.non_exact_match and detect_multi_word(keyword):
        nonexact_google_query_str = []
        nonexact_bing_query_str = []
        nonexact_duckduckgo_query_str = []
        nonexact_yahoo_query_str = []
        nonexact_scribd_query_str = []
        nonexact_brave_query_str = []

        # Non-exact query
        for var_keyword in generate_keyword_variations(keyword):
            # Altered keyword with additional search operators
            nonexact_google_query_str.append(var_keyword + google_base_str)
            nonexact_bing_query_str.append(var_keyword + bing_base_str)
            nonexact_duckduckgo_query_str.append(var_keyword + duckduckgo_base_str)
            nonexact_yahoo_query_str.append(var_keyword + yahoo_base_str)
            nonexact_scribd_query_str.append(var_keyword)
            nonexact_brave_query_str.append(var_keyword + brave_base_str)
    
            # Altered keyword without additional search operators
            nonexact_google_query_str.append(var_keyword)
            nonexact_bing_query_str.append(var_keyword)
            nonexact_duckduckgo_query_str.append(var_keyword)
            nonexact_yahoo_query_str.append(var_keyword)
            nonexact_scribd_query_str.append(var_keyword)
            nonexact_brave_query_str.append(var_keyword)
    
            # Altered keyword without additional search operators but with exact phrase
            nonexact_google_query_str.append(f'"{var_keyword}"')
            nonexact_bing_query_str.append(f'"{var_keyword}"')
            nonexact_duckduckgo_query_str.append(f'"{var_keyword}"')
            nonexact_yahoo_query_str.append(f'"{var_keyword}"')
            nonexact_scribd_query_str.append(f'"{var_keyword}"')
            nonexact_brave_query_str.append(f'"{var_keyword}"')

        # Original keyword without additional search opearators
        nonexact_google_query_str.append(keyword)
        nonexact_bing_query_str.append(keyword)
        nonexact_duckduckgo_query_str.append(keyword)
        nonexact_yahoo_query_str.append(keyword)
        nonexact_brave_query_str.append(keyword)
    
        nonexact_google_query_str.append(f'"{keyword}"')
        nonexact_bing_query_str.append(f'"{keyword}"')
        nonexact_duckduckgo_query_str.append(f'"{keyword}"')
        nonexact_yahoo_query_str.append(f'"{keyword}"')
        nonexact_brave_query_str.append(f'"{keyword}"')
        # Scribd is skipped cause the same query str already implemented on the exact query

        # Return non-exact too if its enabled
        return {
            'google_query_str': google_query_str,
            'bing_query_str': bing_query_str,
            'duckduckgo_query_str': duckduckgo_query_str,
            'yahoo_query_str': yahoo_query_str,
            'scribd_query_str': scribd_query_str,
            'brave_query_str': brave_query_str,
            'nonexact_google_query_str': nonexact_google_query_str,
            'nonexact_bing_query_str': nonexact_bing_query_str,
            'nonexact_duckduckgo_query_str': nonexact_duckduckgo_query_str,
            'nonexact_yahoo_query_str': nonexact_yahoo_query_str,
            'nonexact_scribd_query_str': nonexact_scribd_query_str,
            'nonexact_brave_query_str': nonexact_brave_query_str
        }

    else:
        return {
            'google_query_str': google_query_str,
            'bing_query_str': bing_query_str,
            'duckduckgo_query_str': duckduckgo_query_str,
            'yahoo_query_str': yahoo_query_str,
            'scribd_query_str': scribd_query_str,
            'brave_query_str': brave_query_str
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

def main():
    args = parse_args()
    print(args)
    queries = construct_query_str(args)
    print(queries)

if __name__ == "__main__":
    main()
    


