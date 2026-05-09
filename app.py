import streamlit as st
import anthropic
import base64

client = anthropic.Anthropic(
    api_key=st.secrets["ANTHROPIC_API_KEY"]
)

st.title("AI Thermal Vision")

st.write(
    "Claude AI 기반 열전달 분석 시스템"
)

uploaded_file = st.file_uploader(
    "사진 업로드",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(uploaded_file, width=400)

    image_bytes = uploaded_file.read()

    base64_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    if st.button("AI 분석 시작"):

        with st.spinner(
            "Claude가 열전달 분석 중..."
        ):

            message = client.messages.create(
                model="claude-3-5-sonnet-latest",
                max_tokens=1000,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/jpeg",
                                    "data": base64_image,
                                },
                            },
                            {
                                "type": "text",
                                "text": '''
이 사진을 열전달공학 관점에서 분석해줘.

특히:
1. 강제대류/자연대류 여부
2. 경계층(boundary layer) 변화
2. 열전달계수 h 변화
4. Nusselt Number 변화
5. 냉각 성능 변화

를 공학적으로 설명해줘.
'''
                            }
                        ]
                    }
                ]
            )

            result = message.content[0].text

            st.subheader(
                "Claude 분석 결과"
            )

            st.write(result)

            st.success(
                "Nusselt Number 기반 분석 완료"
            )
