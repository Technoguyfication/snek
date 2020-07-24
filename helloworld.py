# normal hello world
print("hello world")

# join a list
l = ["Hello", "World!"]
print(" ".join(l))

# iterate through a list
for word in l:
	print(word, end = " ")
print()

# some numbers
for i in range(1, 6):
	print(f"Remainders of {i}: ", end = "")
	nums = []
	for j in range(0, 21):
		nums.append(str(j % i))
	print(", ".join(nums))

