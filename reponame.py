def factorial(enteredNum):
    answer = 1
    for x in range(convertedNum):
        x = x + 1
        answer = answer * x
    return answer


print("Testing a repository using HTTP URL. Let us calculate factorials.")
inputNum = input("Please Enter a number: ")
convertedNum = int(inputNum)
print('{}! = {}'.format(convertedNum, factorial(convertedNum)))
