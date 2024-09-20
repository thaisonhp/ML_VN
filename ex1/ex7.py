# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

result = [i for i in range(1000,3000+1) if all(int(digit) % 2 == 0 for digit in str(i))]
for i in result:
    print(f"{i},",end = "")