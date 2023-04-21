import setting as s
import random


def Jia(Min, Max, N):
	jiaList = []
	for i in range(N):
		suanshi = str(random.randint(Min, Max))+" + "+str(random.randint(Min, Max))+" = "
		jiaList.append(suanshi)
		i += i + 1
		return jiaList

#print(Jia(jiaMin, jiaMax, jiaN)) #调试"

def Cheng(Min, Max, N):
	chengList = []
	for i in range(N):
		suanshi = str(random.randint(Min, Max))+" × "+str(random.randint(Min, Max))+" = "
		chengList.append(suanshi)
		i += i + 1
		return chengList

#print(Cheng(chengMin, chengMax, chengN)) #调试"


def Jian(Min, Max, N):
	jianList = []
	for i in range(N):
		numbers = random.sample(range(Min, Max), 2) #生成范围的两个整数
		suanshi = str(max(numbers))+" - "+str(min(numbers))+" = "
		jianList.append(suanshi)
		i += i + 1
		return jianList

#print(Jian(jianMin, jianMax, jianN)) #调试"


def Chu2(bcMin, bcMax, cMin, cMax, yuShu, deShu, N):
	chuList = []
	for i in range(N):
		numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
		bcS, cS = max(numbers), min(numbers) #被除数和除数
		if yuShu == 0:
			while bcS % cS != 0 or bcS / cS >= deShu + 1:   #当得数不为整数并且得数大于所选得数范围时重新选数
				numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
		elif yuShu == 1:
			while bcS % cS == 0 or bcS / cS >= deShu + 1:  #当得数为整数并且得数大于所选得数范围时重新选数
				numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
		elif yuShu == 2:
			while bcS / cS >= deShu + 1:  #当得数大于所选得数范围时重新选数
				numbers = [random.randint(bcMin, bcMax), random.randint(cMin, cMax)]
		suanshi = str(bcS)+" ÷ "+str(cS)+" = "
		chuList.append(suanshi)
		i += i + 1
		return chuList,

#print(Chu(beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, chuN)) #调试"