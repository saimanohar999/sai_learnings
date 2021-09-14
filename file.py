file = open('file.txt','w')
file.write("hello,iam from deepcompute")
file.close()
file = open('file.txt', 'r')
for line in file:
    words = line.split(' ')
    print(words[-1])
file.close()