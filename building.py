'''
Copyright (C) 2024 Email:gc313@foxmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any
later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
import random
import streamlit as st

def time_out():
    """处理超时情况"""
    st.error("[除法]无法生成满足条件的算式，请检查参数设置是否合理!")

def generate_addition(Min, Max, N):
    """生成加法算式"""
    return [f"{random.randint(Min, Max)} + {random.randint(Min, Max)} = ____ " for _ in range(N)]

def generate_multiplication(Min, Max, N):
    """生成乘法算式"""
    return [f"{random.randint(Min, Max)} × {random.randint(Min, Max)} = ____ " for _ in range(N)]

def generate_subtraction(Min, Max, N):
    """生成减法算式"""
    return [f"{max(numbers)} - {min(numbers)} = ____ " for numbers in [random.sample(range(Min, Max), 2) for _ in range(N)]]

def generate_division(bcMin, bcMax, cMin, cMax, yuShu, deShu, N):
    """生成除法算式"""
    chuList = []
    for _ in range(N):
        clc = 0
        while True:
            numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
            if yuShu == 0:
                if max(numbers) % min(numbers) == 0 and max(numbers) / min(numbers) < deShu + 1:
                    break
            elif yuShu == 1:
                if max(numbers) % min(numbers) != 0 and max(numbers) / min(numbers) < deShu + 1:
                    break
            elif yuShu == 2:
                if max(numbers) / min(numbers) < deShu + 1:
                    break
            clc += 1
            if clc > 100:
                time_out()
                return chuList
        chuList.append(f"{max(numbers)} ÷ {min(numbers)} = ____ ")
    return chuList

def split_num(totalNum, trueNum):
    """将总数分成多个部分"""
    n, y = divmod(totalNum, trueNum)
    return [n + (1 if i < y else 0) for i in range(trueNum)]

def create_ss(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, trueNum):
    """生成所有类型的算式"""
    if trueNum == 0:
        return []
    
    ssN = split_num(totalNum, trueNum)
    allList = []

    if jiaBool:
        allList.extend(generate_addition(jiaMin, jiaMax, ssN.pop()))  # 生成加法算式
    if jianBool:
        allList.extend(generate_subtraction(jianMin, jianMax, ssN.pop()))  # 生成减法算式
    if chengBool:
        allList.extend(generate_multiplication(chengMin, chengMax, ssN.pop()))  # 生成乘法算式
    if chuBool:
        allList.extend(generate_division(beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, ssN.pop()))  # 生成除法算式

    random.shuffle(allList)  # 打乱算式顺序
    return allList