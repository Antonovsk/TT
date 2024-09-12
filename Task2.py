i = int(input())

s1 = i // 100 
s2 = (i // 10) - (s1 * 10) 
s3 = i - (s1 * 100) - (s2 * 10) 

print (s1 + s2 + s3)



