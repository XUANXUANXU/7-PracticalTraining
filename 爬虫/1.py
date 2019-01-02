number = int(input('输入一个1-18的整数'))
def FirstFactorial(num):
    j = 1
    for i in range(1,number+1):
        j *=i
    return j
print(FirstFactorial(number))