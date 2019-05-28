#!/usr/bin/env python3
# coding=utf-8
import sys

#awag为工资
awag = int(sys.argv[1])

#wage为应纳税所得额
wage = awag - 5000

#判断wage的所在区间,cal为纳税金额
if wage <= 0:
    print("wage is 0")

if wage > 0 and wage <= 3000:
    cal = wage * 0.03
    print("wage is:{:.2f}".format(cal))

if wage > 3000 and wage <= 12000:
    cal = wage * 0.1 - 210
    print("wage is:{:.2f}".format(cal))

if wage > 12000 and wage <= 25000:
    cal = wage * 0.2 - 1410
    print("wage is:{:.2f}".format(cal))

if wage > 25000 and wage <= 35000:
    cal = wage * 0.25 - 2660
    print("wage is:{:.2f}".format(cal))

if wage > 35000 and wage <= 55000:
    cal = wage * 0.3 - 4410
    print("wage is:{:.2f}".format(cal))

if wage > 55000 and wage <= 80000:
    cal = wage * 0.35 - 7160
    print("wage is:{:.2f}".format(cal))

if wage > 80000:
    cal = wage * 0.45 - 15160
    print("wage is:{:.2f}".format(cal))
