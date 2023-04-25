'''
Copyright (C) 2023

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

def Jia(Min, Max, N):
	jiaSet = set()
	for i in range(N):
		while len(jiaSet) < i + 1:
			suanshi = str(random.randint(Min, Max))+" + "+str(random.randint(Min, Max))+" = ____ "
			jiaSet.add(suanshi)
		i += 1
	return jiaSet

def Cheng(Min, Max, N):
	chengSet = set()
	for i in range(N):
		while len(chengSet) < i + 1:
			suanshi = str(random.randint(Min, Max))+" × "+str(random.randint(Min, Max))+" = ____  "
			chengSet.add(suanshi)
		i += 1
	return chengSet

def Jian(Min, Max, N):
	jianSet = set()
	for i in range(N):
		while len(jianSet) < i + 1:
			numbers = random.sample(range(Min, Max), 2) #生成范围的两个整数
			suanshi = str(max(numbers))+" - "+str(min(numbers))+" = ____  "
			jianSet.add(suanshi)
		i += 1
	return jianSet

def Chu(bcMin, bcMax, cMin, cMax, yuShu, deShu, N):
	chuSet = set()
	for i in range(N):
		while len(chuSet) < i + 1:
			numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
	
			if yuShu == 0:
				while max(numbers) % min(numbers) != 0 or max(numbers) / min(numbers) >= deShu + 1:   #当得数不为整数并且得数大于所选得数范围时重新选数
					numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
			elif yuShu == 1:
				while max(numbers) % min(numbers) == 0 or max(numbers) / min(numbers) >= deShu + 1:  #当得数为整数并且得数大于所选得数范围时重新选数
					numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
			elif yuShu == 2:
				while max(numbers) / min(numbers) >= deShu + 1:  #当得数大于所选得数范围时重新选数
					numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
			suanshi = str(max(numbers))+" ÷ "+str(min(numbers))+" = ____  "
			chuSet.add(suanshi)
		i += 1
	return chuSet

def CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax):
	#先数出需要生成多少种算式，Bool值为真的要生成，否则不生成
	list = [jiaBool, jianBool, chengBool, chuBool]
	ssCount = list.count(True)
	if ssCount != 0:
		ssN = int(totalNum / ssCount)
	else:
		return set()
	
	#要先定义空集合
	jiaSet = set()
	jianSet = set()
	jianSet = set()
	chengSet = set()
	chuSet = set()
	allSet = set()

	if jiaBool == True:
		jiaSet = Jia(jiaMin, jiaMax, ssN)
		allSet = allSet.union(jiaSet)
	if jianBool == True:
		jianSet = Jian(jianMin, jianMax, ssN)
		allSet = allSet.union(jianSet)
	if chengBool == True:
		chengSet = Cheng(chengMin, chengMax, ssN)
		allSet = allSet.union(chengSet)
	if chuBool == True:
		chuSet = Chu(beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, ssN)
		allSet = allSet.union(chuSet)

	return allSet

#调试
#s = CreateSS(100, True, 3, 49, True, 5, 99, True, 1, 9, True, 10, 89, 2, 9, 1, 9)
#print(s) 
#print(len(s))