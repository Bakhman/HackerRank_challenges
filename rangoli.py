"""
(Rangoli is a form of Indian folk art based on creation of patterns.)
You are given an integer, . Your task is to print an alphabet rangoli of size . 
Different sizes of alphabet rangoli are shown below:
#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------


The center of the rangoli has the first alphabet letter a, and 
the boundary has the  alphabet letter (in alphabetical order).
-Function Description
Complete the rangoli function in the editor below.
rangoli has the following parameters:
int size: the size of the rangoli
-Returns
string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
-Input Format
Only one line of input containing size, the size of the rangoli.
-Constraints
0 < size 27"""

def print_rangoli(size):
    total = size*4-3
    l = [chr(i) for i in range(97,97+size)]
    l.reverse()
    l1 = []
    for i in range(size*2-1):
        if i < size:
            l1.append(l[i])
        else:
            l1.pop()
        print(('-'.join(l1)+'-'.join(list(reversed(l1)))[1:]).center(total,'-'))
     
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
