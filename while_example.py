#a = 10
#b = 5

#while a > b:
#    print("the first one os greater")
#    a = a - 1
#last code only so that code doesnt run for ever

sum = 0
while True:
    number = int(input("give me a number"))
    if number == 0:
        break
    sum = sum + number
print("the sum is", sum)
#if mechanism is only to ask if you want to stop while loop. Only by entering 0 will the loop stop