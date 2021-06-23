#!/usr/bin/env python

import sys

from week1_aws_functions import driver

COL_WIDTH = 20


def format_columns(*args):
    return "".join(str(s).ljust(COL_WIDTH) for s in args)


def main():
    nodes = driver.list_nodes()
    if not nodes:
        return "no running nodes found"
    print(format_columns("ID", "Name", "IP","State"))
    for node in nodes:
        print(format_columns(node.id, node.name, ",".join(node.public_ips) or "—", node.state))


if __name__ == "__main__":
    sys.exit(main())
