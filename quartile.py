#! /usr/bin/env python3
# :vim:et ai sw=4 ts=4 sts=4 :
import re
import sys

DICTIONARY = "/usr/share/dict/american-english-insane"


def main(args):
    parts = args[1:]
    words = map(str.strip, open(DICTIONARY).readlines())
    print_words(extract_matches(words, parts))


def print_words(words):
    for w in words:
        print(w)


def build_regex(parts):
    alt = "|".join(parts)
    up_to_4 = "(" + alt + "){1,4}"
    anchored = "^" + up_to_4 + "$"
    return re.compile(anchored)


def extract_matches(words, parts):
    reduced_words = [
        w
        for w in words
        if (
            any([w.startswith(p) for p in parts])
            and any([w.endswith(p) for p in parts])
        )
    ]
    regex = build_regex(parts)
    matching_words = [w for w in reduced_words if regex.match(w)]
    return matching_words


if __name__ == "__main__":
    main(sys.argv)
