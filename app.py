'''
Copyright (C) 2024 Email:gc313@foxmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any
later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
import building as bd  # 导入 building 模块
import streamlit as st  # 导入 Streamlit 库
import configparser  # 导入配置文件解析库
import math  # 导入数学库
import requests  # 导入 HTTP 请求库

st.set_page_config(page_title="小学生数学练习题生成器", layout="wide", page_icon="💯")  # 设置 Streamlit 页面配置

# 读取配置文件
file = 'setting.ini'
config = configparser.ConfigParser()
config.read(file, encoding='utf-8')  # 读取配置文件

# 默认值
DEFAULT_MIN_VALUE = 0
DEFAULT_MAX_VALUE = 99

def read_config(section):
    """读取指定部分的配置项"""
    return {k: v for k, v in config.items(section)}

def create_form(title, section, option_v):
    """创建表单，用于用户输入参数"""
    num_items = read_config(section)
    
    with st.form("setting"):
        tab1, tab2 = st.tabs(["运算项", "布局"])  # 创建两个标签页
        
        with tab1:
            totalNum = st.slider('生成算式数量', min_value=6, max_value=100, value=int(num_items['ss_number']), step=2)  # 生成算式数量滑动条
            
            jiaBool = st.checkbox('加法', value=True)  # 加法复选框
            jiaMin, jiaMax = create_number_inputs('加法', 'jia', num_items)  # 加法最小值和最大值输入框
            
            jianBool = st.checkbox('减法', value=True)  # 减法复选框
            jianMin, jianMax = create_number_inputs('减法', 'jian', num_items)  # 减法最小值和最大值输入框
            
            chengBool = st.checkbox('乘法')  # 乘法复选框
            chengMin, chengMax = create_number_inputs('乘法', 'cheng', num_items)  # 乘法最小值和最大值输入框
            
            chuBool = st.checkbox('除法')  # 除法复选框
            deshu_max = st.slider('得数限制', min_value=1, max_value=99, value=int(num_items['deshu_max']), step=1)  # 得数限制滑动条
            beichuMin, beichuMax = create_number_inputs('被除数', 'beichu', num_items)  # 被除数最小值和最大值输入框
            chuMin, chuMax = create_number_inputs('除数', 'chu', num_items)  # 除数最小值和最大值输入框
            
            yuShuList = st.selectbox('是否生成带余数算式？', ('不要生成带余数算式', '总是生成带余数算式', '随机产生带余数算式'), index=1)  # 带余数算式选择框
            yuShu = {'不要生成带余数算式': 0, '总是生成带余数算式': 1, '随机产生带余数算式': 2}[yuShuList]  # 将选择转换为数字
        
        with tab2:
            t_c_spacing = st.slider('间距', min_value=50, max_value=150, value=int(num_items['c_spacing']), step=5)  # 间距滑动条
            t_r_spacing = st.slider('行距', min_value=5, max_value=150, value=int(num_items['r_spacing']), step=5)  # 行距滑动条
            t_g_num = st.slider('每行算式数量', min_value=2, max_value=5, value=int(num_items['s_num']), step=1)  # 每行算式数量滑动条
        
        create = st.form_submit_button('生成算式', type="primary", use_container_width=True)  # 提交按钮
        
        return {
            'totalNum': totalNum,
            'jiaBool': jiaBool,
            'jiaMin': jiaMin,
            'jiaMax': jiaMax,
            'jianBool': jianBool,
            'jianMin': jianMin,
            'jianMax': jianMax,
            'chengBool': chengBool,
            'chengMin': chengMin,
            'chengMax': chengMax,
            'chuBool': chuBool,
            'deshu_max': deshu_max,
            'beichuMin': beichuMin,
            'beichuMax': beichuMax,
            'chuMin': chuMin,
            'chuMax': chuMax,
            'yuShu': yuShu,
            't_c_spacing': t_c_spacing,
            't_r_spacing': t_r_spacing,
            't_g_num': t_g_num,
            'create': create
        }

def create_number_inputs(label, prefix, num_items):
    """创建数字输入框"""
    col1, col2 = st.columns(2)
    with col1:
        min_val = st.number_input(f'{label}最小取值', value=int(num_items[f'{prefix}_min']), min_value=DEFAULT_MIN_VALUE, step=1, format='%d')  # 最小值输入框
    with col2:
        max_val = st.number_input(f'{label}最大取值', value=int(num_items[f'{prefix}_max']), min_value=DEFAULT_MIN_VALUE, step=1, format='%d')  # 最大值输入框
    return min_val, max_val

def generate_html(suanshi, t_c_spacing, t_r_spacing, t_g_num, title):
    """生成 HTML 代码"""
    td = "<td style='vertical-align:top'>"
    td_end = "</td>"
    html_code = ""
    
    e_num = len(suanshi)
    i = 1
    
    while i <= e_num:
        s = ""
        ss_row = math.ceil(e_num / t_g_num)
        for n in range(ss_row):
            if i <= e_num:
                s += f"<table align='center' style='border-collapse:separate;border-spacing:{t_c_spacing}px 0px;margin-bottom:{t_r_spacing}px'>{suanshi[i-1]}</table>"
            if n == ss_row - 1:
                s = td + s + td_end
            i += 1
        html_code += s
    
    html_start = f"<p align='center'><font size='5'>{title}练习题</font></p><p align='center'><font size='4'>_______年___月___日&nbsp&nbsp&nbsp&nbsp姓名:__________&nbsp&nbsp&nbsp&nbsp用时:_________</font></p><table align='center' border='0'>"
    html_end = "</table>"
    return html_start + html_code + html_end

@st.cache_data
def get_version():
    """获取最新版本信息"""
    url = "https://api.github.com/repos/gc313/kousuan/releases/latest"
    try:
        res = requests.get(url, verify=False)
        res.raise_for_status()
        return res.json()["tag_name"]
    except requests.exceptions.RequestException as e:
        st.error(f"请求失败: {e}")
    except KeyError:
        st.error("无法解析版本信息")
    except Exception as e:
        st.error(f"未知错误: {e}")
    return "Unknown"

with st.sidebar:
    st.subheader("🏮练习题生成参数设置🏮")
    
    option = st.selectbox("选择算式种类", ('计时口算', '竖式计算'))  # 算式种类选择框
    option_dict = {'计时口算': 0, '竖式计算': 1}
    option_v = option_dict[option]
    
    if option_v == 0:
        form_data = create_form("计时口算", 'KOUSUAN', option_v)  # 创建计时口算表单
    elif option_v == 1:
        form_data = create_form("竖式计算", 'SHUSHI', option_v)  # 创建竖式计算表单
    # 版本信息
    st.caption(get_version())

with st.container():
    fin_suanshi = ""  # 初始化 fin_suanshi 变量
    if form_data['create']:
        type_list = [form_data['jiaBool'], form_data['jianBool'], form_data['chengBool'], form_data['chuBool']]
        true_num = type_list.count(True)
        if true_num > 0:
            nr = bd.create_ss(
                form_data['totalNum'],
                form_data['jiaBool'], form_data['jiaMin'], form_data['jiaMax'],
                form_data['jianBool'], form_data['jianMin'], form_data['jianMax'],
                form_data['chengBool'], form_data['chengMin'], form_data['chengMax'],
                form_data['chuBool'], form_data['beichuMin'], form_data['beichuMax'],
                form_data['chuMin'], form_data['chuMax'], form_data['yuShu'],
                form_data['deshu_max'], true_num
            )  # 调用 create_ss 函数生成算式
            fin_suanshi = generate_html(nr, form_data['t_c_spacing'], form_data['t_r_spacing'], form_data['t_g_num'], option)  # 生成 HTML 代码
        else:
            st.warning("没有选择任何算式种类，不会生成任何算式！", icon="🚨")

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

    my_html = f"""<script>{print_js}</script>
    <button onclick="printer()">打印算式</button>
    <div id='here'>{fin_suanshi}</div>
    """
    st.components.v1.html(my_html, height=1080, scrolling=True)  # 显示生成的 HTML 代码