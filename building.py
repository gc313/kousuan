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
	
			#还需要解决纯无余数算式量过大死循环的问题
			if yuShu == 0:
				while max(numbers) % min(numbers) != 0 or max(numbers) / min(numbers) >= deShu + 1:   #无余数算式，当得数不为整数并且得数大于所选得数范围时重新选数(如果只生成无余数算式，算式量过大会造成死循环，因为集合不能有重复元素，但是设定的取值范围找不到那个多符合要求的算式。)
					numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
			elif yuShu == 1:
				while max(numbers) % min(numbers) == 0 or max(numbers) / min(numbers) >= deShu + 1:  #有余数算式，当得数为整数并且得数大于所选得数范围时重新选数
					numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
			elif yuShu == 2:
				while max(numbers) / min(numbers) >= deShu + 1:  #随机余数算式，当得数大于所选得数范围时重新选数
					numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
			suanshi = str(max(numbers))+" ÷ "+str(min(numbers))+" = ____  "
			chuSet.add(suanshi)

	return chuSet

def CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, trueNum):
	#传入的trueNum指算式种类为真的数量，即需要生成多少种算式，为0则返回空集合，这里几种算式均匀生成
	if trueNum != 0:
		ssN = int(totalNum / trueNum)
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
#s = CreateSS(81, False, 3, 49, False, 5, 99, False, 1, 9, True, 10, 89, 2, 9, 0, 9, 1)
#print(s) 
#print(len(s))