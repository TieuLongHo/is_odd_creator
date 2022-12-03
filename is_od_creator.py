from os import getcwd


def is_odd(num: int) -> bool:
    isodd = num % 2
    isoddText = "True" if isodd else "False"
    file.write(f"\tif num == {num}:\n\t\treturn {isoddText}\n")


num = int(input('Enter Range:'))

with open("isodd.py", "w") as file:
    file.write(f"def is_odd(num: int) -> bool:\n")

    for i in range(num + 1):
        is_odd(i)
    file.write("\tprint(f'The Number {num} is out of bound')\n\texit(1)")

    file.write("""
while (num := int(input('Enter Number:'))):
    is_odd_text = 'odd' if is_odd(num) else 'not odd'
    print(f'The Number {num} is {is_odd_text}')""")

print(
    f"The program is succesfully created in this directory :{getcwd()}/isodd.py")
