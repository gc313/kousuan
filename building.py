import configparser
import random

"""
#读取配置文件
file = 'setting.ini'
config = configparser.ConfigParser()
config.read(file, encoding = 'utf-8')
items = dict(config.items('Qvzhi'))

jiaMin = int(items['jia_min'])      #加法算式取值最小数
jiaMax = int(items['jia_max'])      #加法算式取值最大数

jianMin = int(items['jian_min'])      #减法算式取值最小数
jianMax = int(items['jian_max'])     #减法算式取值最大数

chengMin = int(items['cheng_min'])     #乘法算式取值最小数
chengMax = int(items['cheng_max'])     #乘法算式取值最大数

beichuMin = int(items['beichu_min'])   #被除数取值最小数
beichuMax = int(items['beichu_max'])   #被除数取值最大数
chuMin = int(items['chu_min'])       #除数取值最小数
chuMax = int(items['chu_max'])       #除数取值最大数
yuShu = int(items['yu_shu'])        #是否有余数 0:没有   1：都有   2：随机
deShuMax = int(items['deshu_max'])     #除法最大得数
"""
def Jia(Min, Max, N):
	jiaSet = set()
	for i in range(N):
		while len(jiaSet) < i + 1:
			suanshi = str(random.randint(Min, Max))+" + "+str(random.randint(Min, Max))+" = ____ "
			jiaSet.add(suanshi)
		i += 1
	return jiaSet

#print(Jia(jiaMin, jiaMax, 2)) #调试

def Cheng(Min, Max, N):
	chengSet = set()
	for i in range(N):
		while len(chengSet) < i + 1:
			suanshi = str(random.randint(Min, Max))+" × "+str(random.randint(Min, Max))+" = ____  "
			chengSet.add(suanshi)
		i += 1
	return chengSet

#print(Cheng(chengMin, chengMax, 2)) #调试


def Jian(Min, Max, N):
	jianSet = set()
	for i in range(N):
		while len(jianSet) < i + 1:
			numbers = random.sample(range(Min, Max), 2) #生成范围的两个整数
			suanshi = str(max(numbers))+" - "+str(min(numbers))+" = ____  "
			jianSet.add(suanshi)
		i += 1
	return jianSet

#print(Jian(jianMin, jianMax, 2)) #调试


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

#print(Chu(beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, 2)) #调试


def CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax):
	#先数出需要生成多少种算式，Bool值为真的要生成，否则不生成
	list = [jiaBool, jianBool, chengBool, chuBool]
	ssCount = list.count(True)
	ssN = int(totalNum / ssCount)
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