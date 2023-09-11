from random import randint

first_array = []
second_array = []
result_array = []

for i in range(10):
    first_array.append(randint(0, 9))
    second_array.append(randint(0, 9))

carry = 0
for i in range(9, -1, -1):
    total = first_array[i] + second_array[i] + carry
    carry = total // 10
    result_array.insert(0, total % 10)

if carry > 0:
    result_array.insert(0, carry)


print(f"First array: {first_array}")
print(f"Second array:{second_array}")
print(f"Result: {result_array}")

#вапвпапвап