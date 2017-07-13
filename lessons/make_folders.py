from os import system


for i in range(4,11):


    system("mkdir day{}".format(i))
    system("touch exercises.py tests.py")
    system("mkdir assets")
    system("mv exercises.py day{}".format(i))
    system("mv tests.py day{}".format(i))
    system("mv assets day{}".format(i))

