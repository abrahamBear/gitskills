#!/usr/bin/env python3
# -*- coding: utf-8 -*-
height=1.75
weitht=80.5
bmi=weitht/(height*height)
print('小明的BMI指数为:%.2f' % bmi)
if bmi <18.5:
    print('过轻')
elif bmi>=18.5 and bmi <25:
    print('正常')
elif bmi>=25 and bmi <32:
    print('过重')
else:
    print('严重肥胖')
