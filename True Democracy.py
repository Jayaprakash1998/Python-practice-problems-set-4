'''       QUESTION:

True Democracy :

In a world of numbers, pure democracy is practiced. Each and every number can participate in an election. Here the people can vote for as many numbers as they want, 
but as you know everyone will vote for them first, then vote for other numbers. They will vote for all its multiples because they find them to be good numbers. 
After they vote Victor classify the numbers classify those numbers as a Friend or an enemy depending upon the number of votes a number as got and the number of votes 
got by the numbers which voted for this number.

Victor likes odd numbers, so if a number has got odd number of votes and also all the numbers which voted for the number (Excluding 1) got odd number of votes, 
then that number will be considered as a Friend to Victor, and all other number will be considered to be  Enemy.

Victor has formulated all the numbers but missed out the Nth number, can you help Victor to figure out whether the given number is a Enemy or Friend of Victor.

Input Format : One single integer N, where N will be the number of numbers in the world and N will also specify the Nth number for which Victor has to compute whether 
the number is a Friend or Enemy

Input Constraints : 1<=N<=10^10

Output Format : Enemy or Friend

Sample Input :
2

Sample Output :
Enemy























HINTS:
1 - Perfect Square number.

2 - Prime Factorise.

3 - Unique Prime Factors.

'''










































# ANSWER:

from math import sqrt as s
n = int(input())
flag = 0
k = 2
while(k<s(n)+1):
    if(n%k==0):
        n//=k
        if(n%k==0):
            flag = 1
            break
    k+=1

if (flag==0) :
	print("Enemy")
else:
	print("Friend")
