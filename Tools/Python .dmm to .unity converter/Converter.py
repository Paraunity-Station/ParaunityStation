import os
U = open("Test.Unity", "x")
f = open("Test.Unity", "a")
c = open("Essential_Data", "r")
f.write(c.read())
f.close()