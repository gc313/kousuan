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

import building as bd
import streamlit as st
import configparser
import streamlit.components.v1 as components



st.set_page_config(page_title="小学生数学练习题生成器",layout="wide")

with st.sidebar:
    st.subheader("设置:alarm_clock:")
    with st.form("setting"):
        tab1, tab2 = st.tabs(["运算项","布局"])

        with tab1:

            
            #算式种类选择
            option = st.selectbox("选择算式种类", ('计时口算','竖式计算'))
            option_dict = {'计时口算':0, '竖式计算':1}
            option_v = option_dict[option]

            #读取配置文件
            file = 'setting.ini'
            config = configparser.ConfigParser()
            config.read(file, encoding = 'utf-8')
            if option_v == 0:
                num_items = dict(config.items('KOUSUAN'))
                title = "计时口算"
            if option_v == 1:
                num_items = dict(config.items('SHUSHI'))
                title = "竖式计算"

            totalNum = st.slider('生成算式数量', min_value=6, max_value=100, value=int(num_items['ss_number']), step=2, format=None)
            
            jiaBool = st.checkbox('加法', value=True)
            jia_col1, jia_col2 = st.columns(2)
            with jia_col1:
                jiaMin = st.number_input('运算项最小取值', value= int(num_items['jia_min']), min_value=0, step=1, format='%d',key=1)
            with jia_col2:
                jiaMax = st.number_input('运算项最大取值', value= int(num_items['jia_max']), min_value=0, step=1, format='%d',key=2)

            jianBool = st.checkbox('减法', value=True)
            jian_col1, jian_col2 = st.columns(2)
            with jian_col1:
                jianMin = st.number_input('运算项最小取值', value= int(num_items['jian_min']), min_value=0, step=1, format='%d',key=3)
            with jian_col2:
                jianMax = st.number_input('运算项最大取值', value= int(num_items['jian_max']), min_value=0, step=1, format='%d',key=4)

            chengBool = st.checkbox('乘法')
            cheng_col1, cheng_col2 = st.columns(2)
            with cheng_col1:
                chengMin = st.number_input('运算项最小取值', value= int(num_items['cheng_min']), min_value=0, step=1, format='%d',key=5)
            with cheng_col2:
                chengMax = st.number_input('运算项最大取值', value= int(num_items['cheng_max']), min_value=0, step=1, format='%d',key=6)

            chuBool = st.checkbox('除法')
            #设置一个得数限制，数太大了小朋友做不了
            deshu_max = st.slider('得数限制', min_value=1, max_value=99, value=int(num_items['deshu_max']), step=1, format=None)
            chu_col1, chu_col2 = st.columns(2)
            with chu_col1:
                beichuMin = st.number_input('被除数最小取值', value= int(num_items['beichu_min']), min_value=0, step=1, format='%d',key=7)
            with chu_col2:
                beichuMax = st.number_input('被除数最大取值', value= int(num_items['beichu_max']), min_value=0, step=1, format='%d',key=8)

            chu_col3, chu_col4 = st.columns(2)
            with chu_col3:
                chuMin = st.number_input('除数最小取值', value= int(num_items['chu_min']), min_value=0, step=1, format='%d')
            with chu_col4:
                chuMax = st.number_input('除数最大取值', value= int(num_items['chu_max']), min_value=0, step=1, format='%d')

            yuShuList = st.selectbox('是否生成带余数算式？', ('随机产生带余数算式', '不要生成带余数算式', '总是生成带余数算式'), index=2)
            yuShudict = {'随机产生带余数算式':0, '不要生成带余数算式':1, '总是生成带余数算式':2}
            yuShu = yuShudict[yuShuList]
        with tab2:
            #行间距设置
            t_c_spacing = st.slider('间距', min_value=5, max_value=100, value=int(num_items['c_spacing']), step=5, format=None)
            t_r_spacing = st.slider('行距', min_value=5, max_value=100, value=int(num_items['r_spacing']), step=5, format=None)
            t_g_num = st.slider('每行算式数量', min_value=2, max_value=5, value=int(num_items['s_num']), step=1, format=None)

        create = st.form_submit_button('生成算式', type="primary", use_container_width = True)  
            
            #按钮事件
        def Displaynr():
            #用来获取生成的算式，创建一个全局变量，方便外部调用
            global nr 
            nr = bd.CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deshu_max)
            return
            
        def Html(suanshi):
            #构建html语句，这部分是要打印出的算式内容
            tr = "<tr>"
            tr_end = "</tr>"
            html_code = ""
                
            #将算式集合转换为列表
            newlist = list(suanshi)
            i = 1
            while i <= len(newlist):
                s = ""
                #根据每行算式个数来生成表格
                for n in range(t_g_num ):
                    if i <= len(newlist):
                        s += "<td>"+newlist[i-1]+"</td>"
                    if n == t_g_num - 1:
                        s = tr + s + tr_end
                    i += 1
                html_code += s
            return html_code

        #判断生成算式按钮是否被按下，并把Html语句放入变量
        html_start = f"<p align='center'><font size='5'>{title}练习题</font></p><p align='center'><font size='4'>_______年___月___日&nbsp&nbsp&nbsp&nbsp姓名:__________&nbsp&nbsp&nbsp&nbsp用时:_________</font></p><table border='0' align='center' style='border-collapse:separate;border-spacing:{t_c_spacing}px {t_r_spacing}px'>"
        html_end = "</table>"
        fin_suanshi = html_start + html_end
        if create:
            Displaynr()
            fin_suanshi = html_start + Html(nr) + html_end


with st.container():

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
    