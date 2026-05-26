import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="국가별 MBTI 분석",
    layout="wide"
)

st.title("🌍 국가별 MBTI 비율 분석")

# 파일 업로드
uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("파일 업로드 완료!")

    # 국가 컬럼 자동 찾기
    possible_country_cols = ["country", "Country", "COUNTRY"]

    country_col = None
    for col in possible_country_cols:
        if col in df.columns:
            country_col = col
            break

    if country_col is None:
        st.error("국가 컬럼(country)이 없습니다.")
        st.stop()

    # MBTI 컬럼 찾기
    mbti_types = [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]

    available_mbti = [m for m in mbti_types if m in df.columns]

    if len(available_mbti) == 0:
        st.error("MBTI 컬럼이 없습니다.")
        st.stop()

    # 국가 선택
    countries = sorted(df[country_col].unique())

    selected_country = st.selectbox(
        "국가 선택",
        countries
    )

    # 선택된 국가 데이터
    country_data = df[df[country_col] == selected_country].iloc[0]

    mbti_values = []
    for mbti in available_mbti:
        mbti_values.append(country_data[mbti])

    chart_df = pd.DataFrame({
        "MBTI": available_mbti,
        "Value": mbti_values
    })

    # 정렬
    chart_df = chart_df.sort_values(
        by="Value",
        ascending=False
    )

    # 색상 설정
    colors = []

    # 1등 색상 (노란색)
    colors.append("#FFD700")

    # 나머지 하늘색 그라데이션
    gradient = np.linspace(0.9, 0.3, len(chart_df) - 1)

    for g in gradient:
        colors.append((0.4, 0.7, 1.0, g))

    # 그래프 생성
    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(
        chart_df["MBTI"],
        chart_df["Value"],
        color=colors
    )

    # 값 표시
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.1f}",
            ha='center',
            va='bottom',
            fontsize=10
        )

    ax.set_title(
        f"{selected_country} MBTI 비율",
        fontsize=18,
        pad=20
    )

    ax.set_xlabel("MBTI")
    ax.set_ylabel("비율")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig)

    # 데이터 표
    st.subheader("📊 데이터")
    st.dataframe(chart_df, use_container_width=True)

else:
    st.info("CSV 파일을 업로드해주세요.")
