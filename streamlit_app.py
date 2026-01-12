import streamlit as st

st.title("🎈 My 나라샘의 app")
st.write(
    "안녕하세요 저는 SW강사입니다."
)
# 버튼 클릭 여부에 따라 실행
if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")

# 한 줄 텍스트 입력
name = st.text_input("이름을 입력하세요")
st.write("입력된 이름:", name)

# 여러 줄 텍스트 입력
feedback = st.text_area("의견을 입력하세요")
st.write("입력된 의견:", feedback)


# 이미지 출력
st.image("https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/4utc/image/xrVTKtEGE1sWCmwTWWDPoDJaPnY.jpg", caption="AI WORLD!", use_container_width=True)
