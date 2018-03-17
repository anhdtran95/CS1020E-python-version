
name = raw_input("What is your name: ")
noOfTime = raw_input("Hello how many times? ")
for x in range(1, int(noOfTime)+1):
    print(str(x) + ': Hello, ' + name)

print("Bye-bye!")