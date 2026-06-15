import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="전국 범죄 분석",
    layout="wide"
)

st.title("🚔 전국 범죄 데이터 분석")

# 파일 읽기
df = pd.read_csv("lookism!!!!!!(1).csv", encoding="cp949")

region_cols = df.columns[2:]

# 범죄별 합계
crime_total = (
    df.assign(합계=df[region_cols].sum(axis=1))
      [["범죄중분류", "합계"]]
      .sort_values("합계", ascending=False)
)

# 지역별 합계
region_total = (
    df[region_cols]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

region_total.columns = ["지역", "건수"]

tab1, tab2, tab3 = st.tabs([
    "범죄 TOP10",
    "지역 TOP10",
    "범죄별 지역 분석"
])

# --------------------
# 범죄 TOP10
# --------------------
with tab1:

    st.subheader("범죄 발생 TOP10")

    top10 = crime_total.head(10)

    fig = px.bar(
        top10,
        x="범죄중분류",
        y="합계",
        text="합계",
        color="합계"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(top10)

# --------------------
# 지역 TOP10
# --------------------
with tab2:

    st.subheader("범죄 발생 지역 TOP10")

    top10_region = region_total.head(10)

    fig = px.bar(
        top10_region,
        x="지역",
        y="건수",
        text="건수",
        color="건수"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(top10_region)

# --------------------
# 범죄별 지역 분석
# --------------------
with tab3:

    crime = st.selectbox(
        "범죄 선택",
        df["범죄중분류"]
    )

    selected = df[df["범죄중분류"] == crime]

    region_data = (
        selected[region_cols]
        .T
        .reset_index()
    )

    region_data.columns = ["지역", "건수"]

    region_data = region_data.sort_values(
        "건수",
        ascending=False
    )

    st.subheader(f"{crime} 발생 지역 TOP10")

    fig = px.bar(
        region_data.head(10),
        x="지역",
        y="건수",
        text="건수",
        color="건수"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(region_data.head(10))
