import os
import sys

sys.path.append(os.getcwd())
from check50 import File, TestCase, Error, check

class InitialsLess(TestCase):

    @check()
    def exists(self):
        """initials.c exists."""
        super().exists("initials.c")

    @check("exists")
    def compiles(self):
        """initials.c compiles."""
        self.spawn("clang -o initials initials.c -lcs50").exit(0)

    @check("compiles")
    def uppercase(self):
        """Outputs HLJ for Hailey Lynn James"""
        self.spawn("./initials").stdin("Hailey Lynn James", prompt=False).stdout("HLJ\n", "HLJ").exit(0)

    @check("compiles")
    def lowercase(self):
        """Outputs HLJ for hailey lynn james"""
        self.spawn("./initials").stdin("hailey lynn james", prompt=False).stdout("HLJ\n", "HLJ").exit(0)

    @check("compiles")
    def mixed_case(self):
        """Outputs HJ for hailey James"""
        self.spawn("./initials").stdin("hailey James", prompt=False).stdout("HJ\n", "HJ").exit(0)

    @check("compiles")
    def all_uppercase(self):
        """Outputs B for BRIAN"""
        self.spawn("./initials").stdin("BRIAN", prompt=False).stdout("B\n", "B").exit(0)
