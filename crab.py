# -*- coding: utf-8 -*-
"""\
crab.py: CRAB Recursive Acronym Broadener
"""
import re
import sys


# Split the acronym (first word) from the rest of its definition.
ACRONYM_RE = re.compile(r'([\w]*)[\s]?(.*)', re.UNICODE)


def get_groups(s):
    """Return the acronym and the expansion from the given string."""
    return ACRONYM_RE.match(s).groups()


def main(args):
    return 0


def test():
    print 'Running tests.'

    def equals(a, b):
        assert a == b

    equals(get_groups('Crab recursive acronym broadener'),
           ('Crab', 'recursive acronym broadener'))
    equals(get_groups("GNU's Not Unix"), ('GNU', "'s Not Unix"))

    # This is kinda hard, don't want to split the acronym only by the
    # space. Left as is for the moment.
    # equals(get_groups('P.I.P.S. Is POSIX on Symbian'),
    #        ('P.I.P.S.', 'Is POSIX on Symbian'))

    equals(get_groups('a_1 is not a rec acronym'),
           ('a_1', 'is not a rec acronym'))
    equals(get_groups('Python - batteries included'),
           ('Python', '- batteries included'))

    # unicode
    equals(get_groups(u'Äiti: mein mamma'),
           (u'Äiti', ': mein mamma'))
    equals(get_groups(u'Isi on päällikkö'),
           ('Isi', u'on päällikkö'))

    print '-- OK --'


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        test()
        sys.exit(0)
    sys.exit(main(args))
