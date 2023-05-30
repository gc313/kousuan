'''
Copyright (C) 2023 Email:gc313@foxmail.com 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any 
later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import random
import streamlit as st
#用列表不用集合，允许有重复算式出现。如果用集合，会在算式量大，而取值范围小的情况下造成死循环(没有那么多符合要求的算式，会一直生成重复的然后被取消掉)
def TimeOut():
	st.error("[除法]无法生成满足条件的算式，请检查参数设置是否合理!")

	return

def Jia(Min, Max, N):
	jiaList = []
	for i in range(N):
		while len(jiaList) < i + 1:
			suanshi = str(random.randint(Min, Max))+" + "+str(random.randint(Min, Max))+" = ____ "
			jiaList.append(suanshi)
		i += 1
	return jiaList

def Cheng(Min, Max, N):
	chengList = []
	for i in range(N):
		while len(chengList) < i + 1:
			suanshi = str(random.randint(Min, Max))+" × "+str(random.randint(Min, Max))+" = ____  "
			chengList.append(suanshi)
		i += 1
	return chengList

def Jian(Min, Max, N):
	jianList = []
	for i in range(N):
		while len(jianList) < i + 1:
			numbers = random.sample(range(Min, Max), 2) #生成范围的两个整数
			suanshi = str(max(numbers))+" - "+str(min(numbers))+" = ____  "
			jianList.append(suanshi)
		i += 1
	return jianList

def Chu(bcMin, bcMax, cMin, cMax, yuShu, deShu, N):
	chuList = []
	for i in range(N):
		try:
			while len(chuList) < i + 1:
				clc = 0
				numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
		
				if yuShu == 0:
					while max(numbers) % min(numbers) != 0 or max(numbers) / min(numbers) >= deShu + 1:   #无余数算式，当得数不为整数并且得数大于所选得数范围时重新选数
						numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
						clc += 1
						if clc > 100:
							break
				elif yuShu == 1:
					while max(numbers) % min(numbers) == 0 or max(numbers) / min(numbers) >= deShu + 1:  #有余数算式，当得数为整数并且得数大于所选得数范围时重新选数
						numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
						clc += 1
						if clc > 100:
							break
				elif yuShu == 2:
					while max(numbers) / min(numbers) >= deShu + 1:  #随机余数算式，当得数大于所选得数范围时重新选数
						numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
						clc += 1
						if clc > 100:
							break
				if clc > 100:
					break
				suanshi = str(max(numbers))+" ÷ "+str(min(numbers))+" = ____  "
				chuList.append(suanshi)
			if clc > 100:
				TimeOut()
				break
		except Exception as e:
			st.error("[除法]无法生成满足条件的算式，请检查参数设置是否合理!"+str(e))
			break

	return chuList

#将需要生成的算式数量分配至每个算式种类里，并且考虑不能整除的情况
def SplitNum(totalNum, trueNum):
	numList = []
	n = totalNum // trueNum
	y = totalNum % trueNum

	for i in range(trueNum):
		numList.append(n)
	
	#不能整除时，把余数依次加到列表的元素中
	if y > 0:
		for k in range(y):
			numList[k] += 1
	return numList

def CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, trueNum):
	#传入的trueNum指算式种类为真的数量，即需要生成多少种算式，为0则返回空列表
	if trueNum != 0:
		ssN = SplitNum(totalNum, trueNum)
	else:
		return []
	
	#要先定义空列表
	allList = []

	if jiaBool == True:
		allList += Jia(jiaMin, jiaMax, ssN.pop())
	if jianBool == True:
		allList += Jian(jianMin, jianMax, ssN.pop())
	if chengBool == True:
		allList += Cheng(chengMin, chengMax, ssN.pop())
	if chuBool == True:
		allList += Chu(beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, ssN.pop())

	#列表随机排序
	random.shuffle(allList)
	
	return allList

#调试
#s = CreateSS(81, False, 3, 49, False, 5, 99, False, 1, 9, True, 10, 89, 2, 9, 0, 9, 1)
#print(s) 
#print(len(s))