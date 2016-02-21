#!/usr/bin/env python

"""Stp - Stock Patterns

Usage: stp_mgr
    stp_mgr insider 
"""

from docopt import docopt
import stp
print(stp.__file__)
from stp import feed
from stp.feed.insidertrading import data
import sys

def insider():
    records = data.get_records()
    for record in records:
        print(record)
    
def main():
    args = docopt(__doc__)

    if args["insider"]:
        insider()
    
if __name__ == "__main__":
    main()
