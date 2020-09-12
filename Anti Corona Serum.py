'''       QUESTION:

Anti Corona Serum :

Corona, a deadly virus, which created a global impact in the year 2020. Thousands of people died because of it. 
A doctor called Victor from India who finally created a serum for curing it. After 1000 years, we are now at 3020, corona is beginning to become a global threat. 
Only Tony Stark has the formula to create the serum. Tony Stark is capable of recreating the serum, but he has no idea about the dosage. 
Help him with the dosage of serum that has to be given to a particular individual. Thousands of peoples life are at stake, its now are never.

Description about Victor's Findings:

Corona virus can be killed by giving a right quantity of the serum. But it has to be given with absolute precision. 
A machine is discovered to find the number of corona virus present inside a persons body. 
One you have that count, find the value X, where this X will be the dosage of the serum that has to be given in ml to the person affected. 
And the dosage has to be as least as possible because excess dosage might lead to organ failures.

This serum will go in and fight with the virus, and reduce the count to a a value Z, where Z will be a odd number quotient  which is obtained while dividing N and X.

Input Format : One single integer input N, where N is the number of Coronavirus cells in a particular affected person's body

Input Constraints : 1<=N<=10^18

Output Format : Dosage of Serum

Sample Input :
1

Sample Output :
1






















HINTS:

1 - Prime numbers.

2 - Prime Factorise.

3 - 2 is the only even prime.

'''







































# ANSWER:

n = int(input())
k = 1
while(n%2==0):
    n//=2
    k*=2
print(k)
