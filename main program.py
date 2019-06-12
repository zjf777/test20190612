# -*- coding: utf-8 -*-
# @Time    : 2019/6/12/012 20:05
# @Author  : Junfeng.Z
# @E-mail  : 13533630442@163.com
# @Site    : 
# @File    : main program.py
# @Software: PyCharm


class Project:
    def digit_to_letterCombinations(self,digits):
        phone_num = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }                                       #定义一个字典，存储拨号盘“数字—字母”键值对。
        a = len(digits)
        if a == 0:
            return []
        if a == 1:
            return list(phone_num[digits])      #拨号盘上0和1 是两种特殊情况，故单独做判断处理。

        result = []                             #定义一个列表存储结果。
        result_next = Project.digit_to_letterCombinations(digits[1:])
        for n in phone_num[(digits[0])]:
            result.extend([n + m for m in result_next])   #在列表末尾一次性追加上一次创建的字母组合
        return result

