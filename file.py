with open("file.txt", "w") as f:
	f.write("hello,iam from deepcompute")
with open("file.txt", "r") as file:
	data = file.readlines()
	for line in data:
        word = line.split()
		print (word[-1])
