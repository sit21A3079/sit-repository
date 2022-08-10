
import streamlit as st
import numpy as np
import pandas as pd
import  time
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')

#st.sidebar.write('サイドバーの追加')

st.write('プレグレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')

#チェックボックス
if st.checkbox('Show Image') :
    img = Image.open('valo.png')
    st.image(img, caption='VALORANT', use_column_width=True)

#セレクトボックス(選択肢は配列で与える)
option =st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

#テキストボックス
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味', text

#スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition

st.write('DataFrame')

df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

df2 = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

"""折れ線グラフ"""
st.map(df2)