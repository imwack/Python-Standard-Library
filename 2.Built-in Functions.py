# -*- coding: utf-8 -*-
import os

#Return True if any element of the iterable is true.
#If the iterable is empty, return False.
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

#Return True if all elements of the iterable are true
#(or if the iterable is empty).

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

if __name__=="__main__":
    abs(-1)   #绝对值 1
    bin(2017) #返回一个int的二进制字符串  0b11111100001
    '''bytearray([source[, encoding[, errors]]])
    如果source为整数，则返回一个长度为source的初始化数组；    
    如果source为字符串，则按照指定的encoding将字符串转换为字节序列；    
    如果source为可迭代类型，则元素必须为[0 ,255]中的整数；
    '''
    a = bytearray(3)            #bytearray(b'\x00\x00\x00')
    b = bytearray("abc")        #bytearray(b'abc')
    c = bytearray([1, 2, 3])    #bytearray(b'\x01\x02\x03')

    dir()                       #['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a', 'all', 'any', 'b', 'c', 'os']
    dir(os)               #['F_OK', 'O_APPEND', 'O_BINARY', 'O_CREAT'...]
    divmod(2,3)     #(0,2)  return (a/b, a%b)

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))    #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    list(enumerate(seasons, start=1))   #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

