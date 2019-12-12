def factorial(enteredNum):
    answer = 1
    for x in range(convertedNum):
        x = x + 1
        answer = answer * x
    return answer


def squared(enteredNum):
    answer = enteredNum * enteredNum
    return answer


print("Testing a repository using HTTP URL. Let us calculate some numbers.")
inputNum = input("Please Enter a number: ")
convertedNum = int(inputNum)
print('{}! = {}'.format(convertedNum, factorial(convertedNum)))
print('{}^2 = {}'.format(convertedNum, squared(convertedNum)))