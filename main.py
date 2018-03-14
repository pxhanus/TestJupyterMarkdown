import json
import urllib.request


def main():
    with urllib.request.urlopen('http://spec.commonmark.org/0.28/spec.json') as data:
        mdspec = data.read()

