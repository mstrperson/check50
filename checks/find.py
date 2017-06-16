import os
import sys

sys.path.append(os.getcwd())
from check50 import File, Test, Error, check

class Find(Test):

    @check()
    def exists(self):
        """helpers.c exists."""
        super().exists("helpers.c")

    @check("exists")
    def compiles(self):
        """helpers.c compiles."""
        self.spawn("clang -ggdb3 -O0 -std=gnu99 -Wall -Werror -o find find.c helpers.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_firstamongthree(self):
        """finds 28 in {28,29,30}"""
        self.spawn("./find 28").stdin("28").stdin("29").stdin("30").stdin(None).exit(0)

    @check("compiles")
    def test_secondamongthree(self):
        """finds 28 in {27,28,29}"""
        self.spawn("./find 28").stdin("27").stdin("28").stdin("29").stdin(None).exit(0)

    @check("compiles")
    def test_thirdamongthree(self):
        """finds 28 in {26,27,28}"""
        self.spawn("./find 28").stdin("26").stdin("27").stdin("28").stdin(None).exit(0)

    @check("compiles")
    def test_secondamongfour(self):
        """finds 28 in {27,28,29,30}"""
        self.spawn("./find 28").stdin("27").stdin("28").stdin("29").stdin("30").stdin(None).exit(0)

    @check("compiles")
    def test_thirdamongfour(self):
        """finds 28 in {26,27,28,29}"""
        self.spawn("./find 28").stdin("26").stdin("27").stdin("28").stdin("29").stdin(None).exit(0)

    @check("compiles")
    def test_fourthamongfour(self):
        """finds 28 in {25,26,27,28}"""
        self.spawn("./find 28").stdin("25").stdin("26").stdin("27").stdin("28").stdin(None).exit(0)

    @check("compiles")
    def test_notamongthree(self):
        """doesn't find 28 in {25,26,27}"""
        self.spawn("./find 28").stdin("25").stdin("26").stdin("27").stdin(None).exit(1)

    @check("compiles")
    def test_notamongfour(self):
        """doesn't find 28 in {25,26,27,29}"""
        self.spawn("./find 28").stdin("25").stdin("26").stdin("27").stdin("29").stdin(None).exit(1)

    @check("compiles")
    def test_correctlysorts(self):
        """finds 28 in {30,27,28,26}"""
        self.spawn("./find 28").stdin("30").stdin("27").stdin("28").stdin("26").stdin(None).exit(0)
