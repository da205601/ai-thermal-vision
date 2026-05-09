import streamlit as st

st.title("AI Thermal Vision")

st.write(
    "열전달 현상을 AI 프롬프트 기반으로 분석합니다."
)

uploaded_file = st.file_uploader(
    "사진 업로드",
    type=["jpg", "jpeg", "png"]
)

# x 위치 슬라이더
x = st.slider(
    "평판 위 위치 x (m)",
    0.01,
    1.0,
    0.30
)

# Reynolds Number
Re = 50000 * x

# Prandtl Number
Pr = 0.7

# Local Nusselt Number
Nu_x = 0.332 * (Re**0.5) * (Pr**(1/3))

# Average Nusselt Number
Nu_avg = 2 * Nu_x

st.subheader("Nusselt Number 계산 결과")

st.write(f"국부 Nusselt Number Nu_x = {Nu_x:.2f}")

st.write(f"평균 Nusselt Number = {Nu_avg:.2f}")

st.write(
    "평균 Nusselt Number가 국부 Nusselt Number의 약 2배임을 확인 가능"
)

if uploaded_file:

    st.image(uploaded_file, width=400)

    st.subheader(
        "Claude용 AI 프롬프트"
    )

    prompt = f"""
이 이미지를 열전달공학 관점에서 분석해줘.

특히:

1. 강제대류/자연대류 여부
2. 경계층(boundary layer) 변화
3. Reynolds Number 변화
4. Nusselt Number 변화
5. 열전달계수 h 변화
6. 냉각 성능 변화

또한 x={x:.2f} m 위치에서:

- 국부 Nusselt Number Nu_x = {Nu_x:.2f}
- 평균 Nusselt Number = {Nu_avg:.2f}

가 의미하는 바를 설명해줘.
"""

    st.code(prompt)

    st.success(
        "이 프롬프트를 Claude에 복사해서 사용하세요."
    )
