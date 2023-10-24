# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')

st.header('Header: 11시에 다시 한 번 쉬는 시간 주겠습니다.')
st.subheader('뻥입니다!')
st.caption('왜 저러는 걸까요?')


# markdown 연습하기
st.markdown('# 오늘은 매우 춥네요.')
st.markdown('## 차가운 우유와 빵을 먹어서인가봐요.')

st.markdown('_ 메롱 _')
st.markdown('- 나는 춥다\n'
               '- 후리스를 입어도')

# Latex & Code 연습하기
st.markdown('## Code & Latex')
st.code('a + b + c')
st.latex(r'''a + bx +cz''')



# write 연습하기
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']})
st.write('이름이 뭐예요? 전화번호 뭐예요?', df, 'zz')


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text.py