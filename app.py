# 파이썬과 C#과 다른점
# - 세미콜론이 필요없다.
# 주석이 #이다.
# 자료형 선언이 필요 없다.

import streamlit as st # 스트림릿 라이브러리를 읽어와서 st라고 부르겠다.

# 일반적으로 웹사이트를 만들기 위해서는 HTML, CSS, 서버 언어를 알아야 한다.
# 스트림릿을 이용하면 파이썬 하나로 모든 게 가능해진다.

# streamlit run app.py

st.title("안녕하세요")
if st.button("노크하기"):
    st.write("여기 사람 있어요~")

st.write ("동의하시면 아래 내용에 체크해주세요.")
agree = st.checkbox("동의합니다.")
if agree:
    st.write("당신은 동의했습니다.")

option = st.selectbox("연락을 어떻게 받을래요?", ("이메일", "전화", "문자"))
st.write("선택한 방식" + option)

age = st.slider("당신은 몇 살인가요?", 0, 100)
st.write("저는 " + str(age) + "살 입니다.")

text_name = st.text_input("이름을 입력해주세요.")
text_intro = st.text_area("자기소개 해주세요.")

st.image("https://picsum.photos/250/250")

st.video('https://example.com/not-youtube.mp4')