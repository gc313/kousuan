import building as bd
import streamlit as st
import configparser
import streamlit.components.v1 as components

#读取配置文件
file = 'setting.ini'
config = configparser.ConfigParser()
config.read(file, encoding = 'utf-8')
num_items = dict(config.items('Global'))

st.set_page_config(page_title="小学生计时口算生成器",layout="wide")
#显示算式
def Displaynr():
    #用来获取生成的算式，创建一个全局变量，方便外部调用
    global nr 
    nr = bd.CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deShuMax = 9)
    return



with st.sidebar:
    st.subheader("参数设置:alarm_clock:")
    totalNum = st.slider('生成算式数量', min_value=10, max_value=150, value=int(num_items['ss_number']), step=10, format=None)
    
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

    yuShuList = st.selectbox('是否生成带余数算式？', ('随机产生带余数算式', '不要生成带余数算式', '总是生成带余数算式'))
    yuShudict = {'随机产生带余数算式':0, '不要生成带余数算式':1, '总是生成带余数算式':2}
    yuShu = yuShudict[yuShuList]


    b_col1, b_col2 = st.columns(2)
    with b_col1:
        st.button('保存设置', disabled=True)
    with b_col2:
        st.button('生成算式', on_click = Displaynr())  #按钮事件


with st.container():

    def Html(suanshi):
        #构建html语句，这部分是要打印出的内容
        html_start = "<p align='center'><font size='5'>计时口算</font></p><p align='center'><font size='4'>_______年___月___日&nbsp&nbsp&nbsp&nbsp姓名:__________&nbsp&nbsp&nbsp&nbsp用时:_________</font></p><table border='0' align='center' cellspacing='10' cellpadding='10'>"
        html_end = "</table>"
        tr = "<tr>"
        tr_end = "</tr>"
        html_code = ""
        
        #将算式集合转换为列表
        newlist = list(suanshi)
        i = 1
        while i <= len(newlist):
            s = ""
            #每行4个算式
            for n in range(4):
                if i <= len(newlist):
                    s += "<td>"+newlist[i-1]+"</td>"
                if n == 3:
                    s = tr + s + tr_end
                i += 1
            html_code += s
        return html_start + html_code + html_end
    
    #Html语句放入变量
    fin_suanshi = Html(nr)

    #调出打印机的javascript代码
    print_js = """
    function printer(){
    var p_dlg = window.open('printer', '', '');
    var get = document.getElementById('here').innerHTML;
    p_dlg.document.write(get);
    p_dlg.document.location.reload();
    p_dlg.print();
    p_dlg.close();
    }
    """

    #把其他代码组合进来
    #要打印的页面内容不和其他代码放在一起就找不到！
    my_html = f"""<script>{print_js}</script>
    <button onclick="printer()">打印算式</button>
    <div id='here'>{fin_suanshi}</div>
    """
    components.html(my_html, height = 1080, scrolling=True)
    