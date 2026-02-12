import streamlit as st
from openai import OpenAI
from io import BytesIO
from PIL import Image
import base64

OPENAI_KEY = st.secrets["API_KEY"]

# 1. 키와 함께 ChatGPT에 접속한다.
client = OpenAI(
    api_key=OPENAI_KEY,
)

st.title("제품 홍보 포스터 생성기")
keyword = st.text_input("키워드를 입력하세요.")

# 2. 모델과 함께 내용을 입력해서 요청한다.
if st.button("생성하기🔥"):
    with st.spinner("생성 중입니다."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 300자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
                },
                {
                    "role": "user",
                    "content": keyword,
                }

            ],
            model="gpt-4o-mini",
        )

        result = chat_completion.choices[0].message.content
        st.write(result)

    with st.spinner("이미지 생성 중입니다."):
        response = client.images.generate(
            model="gpt-image-1",
            prompt="제품 홍보를 위한 이미지 생성: " + keyword,
            size="1024x1024",
            n=1,
        )

        # ✅ gpt-image-1은 url이 아니라 b64_json으로 받는다
        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        # Streamlit에 표시 (PIL Image로 변환)
        image = Image.open(BytesIO(image_bytes))
        st.image(image, caption=f"키워드: {keyword}", use_container_width=True)