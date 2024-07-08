# Imports
from argparse import *
from csv import *
from datetime import date
from argparse import ArgumentParser
from functions import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
parser = ArgumentParser(description="SuperPy, a command-line inventory system.")
subparser = parser.add_subparsers(dest="command")

#report
report_parser = subparser.add_parser("report_inventory", help="Generate a report.")
report_parser.add_argument("report_time", choices=["--now", "--yesterday"], help="Choose a report time.")
# report_parser.add_argument("--now", action="store_true", help="Report current inventory.")
# report_parser.add_argument("--yesterday", action="store_true", help="Report yesterday's inventory.")    


def main():
    args = parser.parse_args()

    if args.command == "report_inventory":
        if args.report_time == "--now":
            report_current_inventory() 

        if args.report_time == "--yesterday":
            report_yesterday_inventory()

if __name__ == "__main__":
    main()
