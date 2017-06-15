import os
import sys

sys.path.append(os.getcwd())
from check50 import File, Test, Error, check

class Vigenere(Test):

    @check()
    def exists(self):
        """caesar.c exists."""
        super().exists("caesar.c")

    @check("exists")
    def compiles(self):
        """caesar.c compiles."""
        self.spawn("clang -o caesar caesar.c -lcs50").exit(0)

    @check("compiles")
    def test_1a(self):
        """encrypts "a" as "b" using 1 as key"""
        self.spawn("./caesar 1").stdin("a").stdout("ciphertext:\s*b\n", "ciphertext: b").exit(0)

    @check("compiles")
    def test_23barfoo(self):
        """encrypts "barfoo" as "yxocll" using 23 as key"""
        self.spawn("./caesar 23").stdin("barfoo").stdout("ciphertext:\s*yxocll\n", "ciphertext: yxocll").exit(0)

    @check("compiles")
    def test_3BARFOO(self):
        """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
        self.spawn("./caesar 3").stdin("BARFOO").stdout("ciphertext:\s*EDUIRR\n", "ciphertext: EDUIRR").exit(0)

    @check("compiles")
    def test_4BaRFoo(self):
        """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
        self.spawn("./caesar 4").stdin("BaRFoo").stdout("ciphertext:\s*FeVJss\n", "ciphertext: FeVJss").exit(0)

    @check("compiles")
    def test_65barfoo(self):
        """encrypts "barfoo" as "onesbb" using 65 as key"""
        self.spawn("./caesar 65").stdin("barfoo").stdout("ciphertext:\s*onesbb\n", "ciphertext: onesbb").exit(0)

    @check("compiles")
    def test_noarg(self):
        """handles lack of argv[1]"""
        self.spawn("./caesar").exit(1)