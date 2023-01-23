#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
<<<<<<< HEAD
     for i in range(0, x):
	 try:
	     print("{:d}".format(my_list[i]), end="")
	     count += 1
	 except:
	     pass
     print()
     return count
=======
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except:
            pass
    print()
        return count
>>>>>>> 926a0f119c44a32881a02650f5b008586d2d5038
