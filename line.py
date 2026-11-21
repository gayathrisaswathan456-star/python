# Open the file in read mode
file = open("sample.txt", "r")
lines=[]
for line in file:
    lines.append(line.strip())
file.close()

# Display the list
print("Contents of the list:")
print(lines)
