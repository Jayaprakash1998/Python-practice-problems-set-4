'''       QUESTION:

Dictionary  :

We all know some of the greatest dictionaries in the world like the Oxford English Dictionary or the Cambridge English Dictionary so on and so forth. 
Ram, an English enthusiast who also happens to be a very good programmer is very interested in building a digital dictionary. 
He would like to add a feature to the digital dictionary that he believes is "cool". Here is an excerpt that describes this feature.

Given any sequence of characters between 'a' and 'z' (both inclusive), the tool needs to return the row in which the word will possibly 
occur if all the possible arrangements of the given sequence is taken and arranged lexicographically.

Since Ram is busy building the other features of the digital dictionary, you have been given the job of building this "cool" feature.

Input Format : The only line of input contains the string S.

Input Constraints : 1 ≤ |S| ≤ 20
'a' ≤ S[i] ≤ 'z'

Output Format : Print a single integer denoting the Rank of the Word.

Sample Input :
word

Sample Output :
22





















HINTS:

1 - Keep the thought of doing all permutations away... Keep in mind that there can be repetitions. So, while using permutation, use permutation with repetitions formula.

2 - In each position, count how many possible strings were there before that string.

3 - For example S='caba', you got 3! + 3!/2! = 9 string before the string caab. In the second position, there cannot be a string after bcaa and before caab. 
    In the third position, there can be 1! strings after cbaa and before caba. Therefore, there are 9+0+1+0 = 10 strings before the string 'caba'. 
    Hence, the rank of 'caba' is 10+1=11.

'''










































# ANSWER:

fact = [1]
for i in range(1, 21):
    fact.append(i * fact[i-1])

s = input()
n = len(s)

alpha = [0 for i in range(26)]

for x in s:
    alpha[ord(x) - ord('a')] += 1


res = 0
for i in range(n):
    for j in range(ord(s[i]) - ord('a')):

        if(alpha[j] == 0): continue

        rep = 1

        alpha[j] -= 1

        for k in range(26):
            if(alpha[k] > 0):
                rep *= alpha[k]

        res += (fact[n - (i+1)] // rep)

        alpha[j] += 1

    alpha[ord(s[i]) - ord('a')] -= 1

print(res + 1)
