import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

# 한글 폰트 설정
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    df["날짜"] = pd.to_datetime(df["날짜"])
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

st.title("🌡️ 서울 특정 날짜 연도별 기온 변화")

col1, col2 = st.columns(2)

with col1:
    month = st.selectbox(
        "월 선택",
        sorted(df["월"].unique())
    )

with col2:
    day = st.selectbox(
        "일 선택",
        range(1, 32)
    )

filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

filtered = filtered.sort_values("연도")

if len(filtered) > 0:

    fig, ax = plt.subplots(figsize=(14, 7))

    # 최고기온 (분홍색)
    ax.plot(
        filtered["연도"],
        filtered["최고기온(℃)"],
        color="hotpink",
        linewidth=2.5,
        marker="o",
        markersize=4,
        label="최고기온"
    )

    # 최저기온 (연한 파란색)
    ax.plot(
        filtered["연도"],
        filtered["최저기온(℃)"],
        color="#A7D8FF",
        linewidth=2.5,
        marker="o",
        markersize=4,
        label="최저기온"
    )

    ax.set_title(
        f"{month}월 {day}일 연도별 최고·최저기온",
        fontsize=18
    )

    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")

    ax.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    ax.legend(fontsize=12)

    st.pyplot(fig)

    st.subheader("데이터 보기")
    st.dataframe(
        filtered[
            ["연도", "최고기온(℃)", "최저기온(℃)"]
        ],
        use_container_width=True
    )

else:
    st.warning("해당 날짜의 데이터가 없습니다.")
