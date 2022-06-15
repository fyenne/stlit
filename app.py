import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import warnings
import re
from zhdate import ZhDate as lunar_date
from typing import Iterable
import streamlit.components.v1 as components
from datetime import datetime
from PIL import Image 
warnings.filterwarnings('ignore')
# import plotly.graph_objs as go

st.set_page_config(
    page_title="simingyanwebpage",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "fyenne@hotmail.com"
    }
)

class load_data:
    '''
    read some data
    '''
    def __init__(self, df, lunar_today, pltdf):
        self.df = pd.DataFrame()
        self.lunar_today = ''
        self.pltdf = pd.DataFrame()
        self.chinese_char_map = {}
        

    df = pd.read_csv('./dataup/base.csv')
    lunar_today = re.sub('\D', '', str(lunar_date.from_datetime(datetime.now())))
    pltdf = pd.DataFrame(data = {
        'main': '八卦',
        'wuxing':['金', '金', '火', '火', '木', '木', '土', '土','土', '土', '水', '水'],
        'bagua': ['乾','兑','离','离','震','巽','坤','坤','艮','艮','坎','坎'],
        'tiangan':['庚', '辛','丙', '丁', '甲', '乙', '戊', '己', '戊', '己',  '壬', '癸'],
        'dizhi':['申', '酉','巳', '午','寅','卯','辰','戌', '丑', '未',  '亥', '子'],
        'value1': np.repeat(10, 12).tolist()
    })
    def plt1():
        fig = px.sunburst(load_data.pltdf, path=['main', 'wuxing', 'bagua', 'tiangan', 'dizhi'], values='value1',\
        color_discrete_sequence = px.colors.qualitative.Pastel2[0:8]
        )
        return fig
    
    def count_strokes(words: Iterable) -> int:
        """
        统计字符串中所有文字的笔画总数

        :param words: 需要统计的字符串
        :return: 笔画总数
        """
        chinese_char_map = {}
        with open('./dataup/chinese_unicode_table.txt', 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            for line in lines[6:]:  # 前6行是表头，去掉
                line_info = line.strip().split()
                # 处理后的数组第一个是文字，第7个是笔画数量
                chinese_char_map[line_info[0]] = line_info[6]
        strokes = 0
        for word in words:
            if 0 <= ord(word) <= 126:  # 数字，英文符号范围
                strokes += 1
            elif 0x4E00 <= ord(word) <= 0x9FA5:  # 常用汉字Unicode编码范围4E00-9FA5，20902个字
                strokes += int(chinese_char_map.get(word, 1))
            else:  # 特殊符号字符一律排在最后
                strokes += 1
        return strokes
    
    
st.title('正德佷准')
st.markdown('--- \n > **人工智能和量子物理结合下的优化版梅花易数**\n ---')
# ---- 

# # l2=[]
# #  将纵向每个字符当作 y 坐标的刻度
# for y in range(15,-15,-1):
#     l3 = []
#     #  将横向每个字符当作 x 坐标的刻度
#     for x in range(-30,30):
#         # 如果 x,y 点在心形内,则将一个字符加入到行,否则加入空字符
#         l3.append((' I love U'[(x-y)%9]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' '))
#     l2.append(''.join(l3))
# l1 ='\n'.join(l2) 

    
st.text('hahha')
# ----
selected_target = st.selectbox('测什么?', options = ['选择', '情路', '仕途'])
if selected_target == '选择':
    print('')
    st.plotly_chart(load_data.plt1())
# -----
else:
    '今日是农历: %s \
    公历 %s'%(load_data.lunar_today, datetime.today().strftime('%Y%m%d'))
    dizhi = '酉、戌、亥、子、丑、寅、卯、辰、巳、午、未、申'.split('、')
    
    dict = dict(zip(range(1,13), "子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥".split('、')))
    # st.code()
    name = st.text_input('请输入您的姓名')
    # st.text()
    components.html("<html><body>笔画数:%s</body></html>"%load_data.count_strokes(name),
                width=200, height=30)
    
    bdate = st.text_input('请输入您的生日', value = '20220304')
    dizhi = dizhi[int(bdate[0:4])%12 - 1]
    components.html("<html><body>地支: %s</body></html>"%dizhi,
                width=200, height=30)
    
    bt = st.button('测')
    if (bt == True) & (name != '') & (int(bdate) < 20220101) & (len(name) < 26):
        st.markdown('恭喜您和刘亦菲谈恋爱')
    else:
        st.text("输入信息有误")
        pass


# s2 = st.color_picker()

# s2.background_gradient(axis=None, vmin=0, vmax=1000, cmap="YlGnBu")
