import configparser
import random

#读取配置文件
file = 'setting.ini'
config = configparser.ConfigParser()
config.read(file, encoding = 'utf-8')
items = dict(config.items('Qvzhi'))

jiaMin = int(items['jia_min'])      #加法算式取值最小数
jiaMax = int(items['jia_max'])      #加法算式取值最大数
jiaN = 8         #加法算式数量

jianMin = int(items['jian_min'])      #减法算式取值最小数
jianMax = int(items['jian_max'])     #减法算式取值最大数
jianN = 8        #减法算式数量

chengMin = int(items['cheng_min'])     #乘法算式取值最小数
chengMax = int(items['cheng_max'])     #乘法算式取值最大数
chengN = 8       #乘法算式数量

beichuMin = int(items['beichu_min'])   #被除数取值最小数
beichuMax = int(items['beichu_max'])   #被除数取值最大数
chuMin = int(items['chu_min'])       #除数取值最小数
chuMax = int(items['chu_max'])       #除数取值最大数
chuN = 8        #除法算式数量
yuShu = int(items['yu_shu'])        #是否有余数 0:没有   1：都有   2：随机
deShuMax = int(items['deshu_max'])     #除法最大得数

def Jia(Min, Max, N):
	jiaList = []
	for i in range(N):
		suanshi = str(random.randint(Min, Max))+" + "+str(random.randint(Min, Max))+" = "
		jiaList.append(suanshi)
		i += i + 1
	return jiaList

#print(Jia(jiaMin, jiaMax, jiaN)) #调试

def Cheng(Min, Max, N):
	chengList = []
	for i in range(N):
		suanshi = str(random.randint(Min, Max))+" × "+str(random.randint(Min, Max))+" = "
		chengList.append(suanshi)
		i += i + 1
	return chengList

#print(Cheng(chengMin, chengMax, chengN)) #调试


def Jian(Min, Max, N):
	jianList = []
	for i in range(N):
		numbers = random.sample(range(Min, Max), 2) #生成范围的两个整数
		suanshi = str(max(numbers))+" - "+str(min(numbers))+" = "
		jianList.append(suanshi)
		i += i + 1
	return jianList

#print(Jian(jianMin, jianMax, jianN)) #调试


def Chu(bcMin, bcMax, cMin, cMax, yuShu, deShu, N):
	chuList = []
	for i in range(N):
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
		suanshi = str(max(numbers))+" ÷ "+str(min(numbers))+" = "
		chuList.append(suanshi)
		i += i + 1
	return chuList,

#print(Chu(beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax, chuN)) #调试