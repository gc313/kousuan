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
import math
import requests



st.set_page_config(page_title="小学生数学练习题生成器",layout="wide",page_icon="💯")

with st.sidebar:
    st.subheader("🏮练习题生成参数设置🏮")
    
    #算式种类选择
    option = st.selectbox("选择算式种类", ('计时口算','竖式计算'))
    option_dict = {'计时口算':0, '竖式计算':1}
    option_v = option_dict[option]

    #读取配置文件
    file = 'setting.ini'
    config = configparser.ConfigParser()
    config.read(file, encoding = 'utf-8')

    with st.form("setting"):
        tab1, tab2 = st.tabs(["运算项","布局"])
        
        #计时口算UI
        if option_v == 0:
            num_items = dict(config.items('KOUSUAN'))
            title = "计时口算"
            
            with tab1:

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
                    chuMin = st.number_input('除数最小取值', value= int(num_items['chu_min']), min_value=1, step=1, format='%d')
                with chu_col4:
                    chuMax = st.number_input('除数最大取值', value= int(num_items['chu_max']), min_value=1, step=1, format='%d')

                yuShuList = st.selectbox('是否生成带余数算式？', ('不要生成带余数算式', '总是生成带余数算式', '随机产生带余数算式' ),index = 1)
                yuShudict = {'不要生成带余数算式':0, '总是生成带余数算式':1, '随机产生带余数算式':2,}
                yuShu = yuShudict[yuShuList]  
        
        
        #竖式计算UI
        if option_v == 1:
            num_items = dict(config.items('SHUSHI'))
            title = "竖式计算"
            
            with tab1:        
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
                    chuMin = st.number_input('除数最小取值', value= int(num_items['chu_min']), min_value=1, step=1, format='%d')
                with chu_col4:
                    chuMax = st.number_input('除数最大取值', value= int(num_items['chu_max']), min_value=1, step=1, format='%d')

                yuShuList = st.selectbox('是否生成带余数算式？', ('不要生成带余数算式', '总是生成带余数算式', '随机产生带余数算式' ),index = 1)
                yuShudict = {'不要生成带余数算式':0, '总是生成带余数算式':1, '随机产生带余数算式':2,}
                yuShu = yuShudict[yuShuList]
        
        
        with tab2:
            #行间距设置
            t_c_spacing = st.slider('间距', min_value=50, max_value=150, value=int(num_items['c_spacing']), step=5, format=None)
            t_r_spacing = st.slider('行距', min_value=5, max_value=150, value=int(num_items['r_spacing']), step=5, format=None)
            t_g_num = st.slider('每行算式数量', min_value=2, max_value=5, value=int(num_items['s_num']), step=1, format=None)

        create = st.form_submit_button('生成算式', type="primary", use_container_width = True)
        #在线获取版本
        @st.cache_data    
        def GetVersion():
            res = requests.get("https://api.github.com/repos/gc313/kousuan/releases/latest")
            try:
                output = res.json()["tag_name"]
            except:
                output = "Unknow"
            return output


        def Html(suanshi):
            #构建html语句，这部分是要打印出的算式内容
            """思路是先生成一个N列1行的表，每一列里面由上至下生成算式，每一个算式放
            在单独的一个表里。
            原因：之前用border-spacing控制表格间距时，上下左右都会同时变化变化，但
            我只想变化水平间距和下间距。所以想到把每一行做成单独的表格，用border-spacing
            的前一个参数控制水平间距，用margin-bottom控制下间距，但这有个问题，生成的算式
            长短不一，所以每行形成的表格难以对齐，用现在的方法，每一个包含算式的小表格被放
            在一个大表格的列里，默认就左对齐了。
            """
            td = "<td style='vertical-align:top'>"
            td_end = "</td>"
            html_code = ""
                
            #获取列表中算式个数
            e_num = len(suanshi)
            i = 1
            #循环至获取所有算式
            while i <= e_num:
                s = ""
                #根据算式总数除以设定的列数，得到需要生成多少行算式，除不尽的用math.ceil()向上取整
                ss_row = math.ceil(e_num / t_g_num)
                for n in range(ss_row):
                    #再次判断是否获取所有元素?这里可以优化？？
                    if i <= e_num:
                        #每列里的每个算式单独生成一个表格
                        s += f"<table align='center' style= 'border-collapse:separate;border-spacing:{t_c_spacing}px 0px;margin-bottom:{t_r_spacing}px'>"+suanshi[i-1]+"</table>"
                    #当生成每列所需数量的算式后，加上html的<td>标签，形成一列
                    if n == ss_row - 1:
                        s = td + s + td_end
                    i += 1
                #把生成的一列算式html代码存入html_code
                html_code += s

            return html_code

        #判断生成算式按钮是否被按下，并把Html语句放入变量
        html_start = f"<p align='center'><font size='5'>{title}练习题</font></p><p align='center'><font size='4'>_______年___月___日&nbsp&nbsp&nbsp&nbsp姓名:__________&nbsp&nbsp&nbsp&nbsp用时:_________</font></p><table align='center' border='0'>"
        html_end = "</table>"
        #没创建算式时只显示标题
        fin_suanshi = html_start + html_end
    
    #版本信息
    st.caption(GetVersion())



with st.container():

    #点击按钮
    if create:
        type_list = [jiaBool, jianBool, chengBool, chuBool]
        true_num = type_list.count(True)
        if true_num >0:
            nr = bd.CreateSS(totalNum, jiaBool, jiaMin, jiaMax, jianBool, jianMin, jianMax, chengBool, chengMin, chengMax, chuBool, beichuMin, beichuMax, chuMin, chuMax, yuShu, deshu_max, true_num)
            fin_suanshi = html_start + Html(nr) + html_end
        else:
            st.warning("没有选择任何算式种类，不会生成任何算式！", icon="🚨")

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
    