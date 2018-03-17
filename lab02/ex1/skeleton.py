
def revert(num):
    reverted = ""
    while(num > 10):
        remainder = num % 10
        reverted += str(remainder)
        num = num /10

    reverted += str(num)

    return int(reverted)



number = int(raw_input())
revertNum = revert(number)

if(number == revertNum):
    print("Yes")
else:
    print("No")