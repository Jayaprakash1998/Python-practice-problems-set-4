'''       QUESTION:

Unity is Strength :

Infinity Stones are so powerful, and no normal human being can hold the stone and stay alive. After the avengers has set the path right by destroying Thanos. 
Thanos had sent a time remnant. Time remnants, also known as timeline remnants or temporal duplicates. He sent back in time and destroyed Tony Start, the Iron Man. 
So without him, who will snap the finger and kill Thanos?

But time are so many possibilities. Now normal people have joined hands to fight against Thanos. But no one can hold the stone alone. 
So Dr. Banner has designed a machine such that, the machine can be held by many people together. The people are categorized by their power, from 1 to N. 
They have to stand in form of a square. Dr. Banner has found out that people with powers of 1 to N are required, 
and a person with power 1 will be standing in the center and people with power 2 will form a smallest possible square around him. 
This will be continued until people with power N form a square. Now they all will will hold the device together and destroy Thanos. 
Dr. Banner, is busy making the machine ready. Can you help him, by making people stand in  the required order and protect the world!

Input Format : One single integer N

Input Constraints : 1<=N<=100

Output Format : The pattern thus required

Sample Input :
4

Sample Output :
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 





















HINTS:

1 - Break the pattern into smaller pieces.

2 - Break it into 6 triangles, upper left, upper mid and upper right,m and similar for loweer.

3 - Reverse the upper conditions to get the same for lower portion.

'''





































# ANSWER:

a=int(input())
for i in range(a*2-1):
    for j in range(a*2-1):
        print(a-min(i,j,((a*2-2)-i),((a*2-2)-j)),end=" ")
    print()
