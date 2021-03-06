#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 11:41
# @Author  : Adam
# @Site    : 
# @File    : Log.py
# @Software: PyCharm
import pandas as pd


def sort(array):
    """
    :param array: 相关系数矩阵
    :return: 离目标点最近的三个样本点的索引
    """
    templist = []
    for i in range(106):
        list1 = []
        list2 = []
        list1.append(sorted(array[i], key=lambda x: (x < 0, abs(x)))[0])  # 将每行按照正负分割后，绝对值升序排序后读取前三个值
        list1.append(sorted(array[i], key=lambda x: (x < 0, abs(x)))[1])
        list1.append(sorted(array[i], key=lambda x: (x < 0, abs(x)))[2])
        for j in list1:  # 从原list中找到index号
            for k in range(106):
                if array[i][k] == j:
                    if k not in list2:
                        list2.append(k)
                    else:
                        continue
        templist.append(list2)
    return templist


def ques5(data):
    """
    :param data: 源数据表
    :return: return none
    """
    get = sort(data)
    df = pd.DataFrame(get, index=range(106), columns=["index1", "index2", "index3"])
    print("ques5", "\n", df)
    df.to_csv('E:\\result.txt', index=False, sep=",")
