from browser import *
from cli import *
import argparse
import sys

parser = argparse.ArgumentParser(description="Search initializer CLI")
subparsers = parser.add_subparsers(dest="command", required=False)

p_fullname = subparsers.add_parser("fullname", help="Initialize search using a full name")
p_fullname.add_argument("full_name", help="Full Name")

p_phone = subparsers.add_parser("phone", help="Initialize search using a phone number")
p_phone.add_argument("country_code", help="Country code")
p_phone.add_argument("phone_number", help="Phone number")

p_address = subparsers.add_parser("address", help="Initialize search using an address")
p_address.add_argument("address", help="Address")

p_social = subparsers.add_parser("social", help="Initialize search using a social media handle")
p_social.add_argument("social_media_handle", help="Social media handle")

p_alias = subparsers.add_parser("alias", help="Initialize search using an alias")
p_alias.add_argument("name_alias", help="Alias")

args = parser.parse_args()

if args.command == "fullname":
    print(f"Searching by full name: {args.full_name}")
elif args.command == "phone":
    print(f"Searching by phone: +{args.country_code} {args.phone_number}")
elif args.command == "address":
    print(f"Searching by address: {args.address}")
elif args.command == "social":
    print(f"Searching by social handle: {args.social_media_handle}")
elif args.command == "alias":
    print(f"Searching by alias: {args.name_alias}")
else:
	main_banner()
	help_menu()
	sys.exit(1)

key = "john doe"

#print(google_queries([f'"{key}"']))
#print(bing_queries([f'"{key}"']))
#print(duckduckgo_queries([f'"{key}"']))
#print(yahoo_queries([f'"{key}"']))
#print(scribd_queries([f'"{key}"']))
#print(brave_queries([f'"{key}"']))
