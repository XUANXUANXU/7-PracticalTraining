# list,dict,tuple : 是可迭代对象，你不是迭代器

# 可迭代对象一定可以进行for循序

# for循环的本质
# for i in (可迭代对象):
#     print(i)

# step1: iter(可迭代对象)
# step2: 在执行for循环的时候是不停的在调用next方法

# 什么叫迭代器？
# def __iter__(self):

# def __next__(self):

class Student():

    def __init__(self,num):
        self.num = num
        self.data = []
        self.currentNum = 0
        for i in range(1,self.num+1):
            name = 'name'+str(i)
            self.data.append(name)

    def __iter__(self):
        return self

    def __next__(self):

        if self.currentNum < len(self.data):
            name = self.data[self.currentNum]
            self.currentNum +=1
            return name
        else:
            raise StopIteration

student_obj = Student(30)

print(next(student_obj))
print(next(student_obj))
print(next(student_obj))

#生成器：生成器是一个特殊的迭代器
# 方式一：
# obj =  (i for i in (1,2,3,4,5,6,7,8) if i > 3)
#方式二：
# 一旦函数中出现了yeild,这个函数就不在是一个普通的函数了
# 就是一个生成器

def get_num(num):
    start_num = 0
    while start_num < num:
        start_num +=1
        yield start_num

obj = get_num(100)

print(next(obj))

print(next(obj))

print(next(obj))

print(next(obj))

print(type(obj))
print(obj)


