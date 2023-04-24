import building as bd
import streamlit as st
import configparser
import streamlit.components.v1 as components




#读取配置文件
file = 'setting.ini'
config = configparser.ConfigParser()
config.read(file, encoding = 'utf-8')
num_items = dict(config.items('Qvzhi'))

#显示算式
def Displaynr():
    #用来获取生成的算式，创建一个全局变量，方便外部调用
    global nr 
    nr = bd.CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax = 9)
    return

st.title = '口算生成器'

with st.sidebar:
    
    totalNum = st.slider('#### 算式数量', min_value=10, max_value=150, value=int(num_items['ss_number']), step=10, format=None)
    
    jiaBool = st.checkbox('加法', value=True)
    jia_col1, jia_col2 = st.columns(2)
    with jia_col1:
        jiaMin = st.number_input('运算项最小取值', value= int(num_items['jia_min']), min_value=0, step=1, format='%d')
    with jia_col2:
        jiaMax = st.number_input('运算项最大取值', value= int(num_items['jia_max']), min_value=0, step=1, format='%d')



    jianBool = st.checkbox('减法', value=True)
    jian_col1, jian_col2 = st.columns(2)
    with jian_col1:
        jianMin = st.number_input('运算项最小取值', value= int(num_items['jian_min']), min_value=0, step=1, format='%d')
    with jian_col2:
        jianMax = st.number_input('运算项最大取值', value= int(num_items['jian_max']), min_value=0, step=1, format='%d')



    chengBool = st.checkbox('乘法')
    cheng_col1, cheng_col2 = st.columns(2)
    with cheng_col1:
        chengMin = st.number_input('运算项最小取值', value= int(num_items['cheng_min']), min_value=0, step=1, format='%d')
    with cheng_col2:
        chengMax = st.number_input('运算项最大取值', value= int(num_items['cheng_max']), min_value=0, step=1, format='%d')



    chuBool = st.checkbox('除法')
    chu_col1, chu_col2 = st.columns(2)
    with chu_col1:
        beichuMin = st.number_input('被除数最小取值', value= int(num_items['beichu_min']), min_value=0, step=1, format='%d')
    with chu_col2:
        beichuMax = st.number_input('被除数最大取值', value= int(num_items['beichu_max']), min_value=0, step=1, format='%d')

    chu_col3, chu_col4 = st.columns(2)
    with chu_col3:
        chuMin = st.number_input('除数最小取值', value= int(num_items['chu_min']), min_value=0, step=1, format='%d')
    with chu_col4:
        chuMax = st.number_input('除数最大取值', value= int(num_items['chu_max']), min_value=0, step=1, format='%d')

    yuShuList = st.selectbox('是否生成带余数算式？', ('不要生成带余数算式', '总是生成带余数算式', '都可以'))
    yuShudict = {'不要生成带余数算式':0, '总是生成带余数算式':1, '都可以':2}
    yuShu = yuShudict[yuShuList]


    b_col1, b_col2 = st.columns(2)
    with b_col1:
        saveCfg = st.button('保存设置')
    with b_col2:
        create = st.button('生成算式', on_click = Displaynr())  #按钮事件


with st.container():
    def Html(suanshi):

        h = "<font size='5'>计时口算</font><br><font size='4'>日期:_____年___月___日&nbsp&nbsp姓名:__________&nbsp&nbsp用时:_________</font><table border='0' align='center' cellspacing='10' cellpadding='10'>"
        h_end = "</table>"
        tr = "<tr>"
        tr_end = "</tr>"
        
        f = ""
        newlist = list(suanshi)
        i = 1
        while i <= len(newlist):
            s = ""
            #n = 0
            for n in range(4):
                if i <= len(newlist):
                    s += "<td>"+newlist[i-1]+"</td>"
                if n == 3:
                    s = tr + s + tr_end


                i += 1

            f += s
        return h + f + h_end
    
    suanshi = Html(nr)

    #components.html(suanshi)

    
    print_js = """
    function printer(){
    var newWin = window.open('printer', '', '');
    var xiaozhi = document.getElementById('123').innerHTML;
    newWin.document.write(xiaozhi);
    newWin.document.location.reload();
    newWin.print();
    newWin.close();
    }
    """

    # Wrapt the javascript as html code
    #内容不放在一起就找不到！
    my_html = f"""<script>{print_js}</script>
    <button onclick="printer()">打印</button>
    <p id='123'>{suanshi}</p>
    """
    components.html(my_html, height = 600, scrolling=True)
    