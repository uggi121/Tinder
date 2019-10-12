import sys
import json

def read():
    lines = sys.stdin.readlines()
    return lines
def main():
    lines = read()
    print(lines)

main()
