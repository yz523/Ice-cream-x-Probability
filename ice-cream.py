# -*- coding: utf-8 -*-
import random
import sys

#初始化变量
TYPE1 = 0.9
TYPE2 = 0.6
TYPE3 = 0.3
first_day = "first_day"
type1 = "type1"
type2 = "type2"
type3 = "type3"

#输入夏天时长(天数)
print("Summer Day(s):")
DAYS = int(sys.stdin.readline())
print("=======The result of", DAYS, "Day(s):=======")


#根据昨日(或第一天)的type变换概率并得出今日type
#建立一个概率池，每一种type默认为10，总概率池为30
#随机取一个1-30的数，在第一天的情况是，落入1-10为type1，11-20为type2，21-30为type3
#------------------------------------------------------------
#|       1-10       |       11-20       |       21-30       |
#------------------------------------------------------------
#随机取一个1-30的数，如果昨日是type1，则第二天的情况是，落入1-8为type1，9-19为type2，20-30为type3
#------------------------------------------------------------
#|       1-8       |       9-20       |       20-30       |
#------------------------------------------------------------
#随机取一个1-30的数，如果昨日是type2，则第二天的情况是，落入1-11为type1，12-19为type2，20-30为type3
#------------------------------------------------------------
#|       1-11       |       12-19       |       20-30       |
#------------------------------------------------------------
#随机取一个1-30的数，如果昨日是type3，则第二天的情况是，落入1-11为type1，12-21为type2，22-30为type3
#------------------------------------------------------------
#|       1-11       |       12-21       |       22-30       |
#------------------------------------------------------------
#第三天,第四天...的情况以此类推
#所以每次只需要改动区分三种type的分界线即可，即10,20这两个边界
def get_type(yesterday):
    global left_bound
    global right_bound
    if yesterday == first_day:
        left_bound = 10
        right_bound = 20
    if yesterday == type1:
        left_bound -= 2
        right_bound -= 1
    if yesterday == type2:
        left_bound += 1
        right_bound -= 1
    if yesterday == type3:
        left_bound += 1
        right_bound += 1
    rand = random.randint(1, 30)
    if rand <= left_bound:
        return type1
    if left_bound < rand <= right_bound:
        return type2
    if rand > right_bound:
        return type3

#得到type后输出对应的概率
def output_prob(current):
    switcher = {
        type1: TYPE1,
        type2: TYPE2,
        type3: TYPE3
    }
    return switcher.get(current)

#循环本体和最终输出
for x in range(DAYS):
    if x == 0:
        current_day = get_type(first_day)
    else:
        current_day = get_type(current_day)
    print("Day", (x+1), ":", output_prob(current_day))
