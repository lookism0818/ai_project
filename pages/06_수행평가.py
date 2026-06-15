import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="전국 범죄 분석",
    layout="wide"
)

st.title("🚔 전국 범죄 데이터 분석")

# CSV 읽기
df = pd.read_csv("lookism!!!!!!(1).csv", encoding="cp949")

# 지역 컬럼
region_cols = df.columns[2:]

# 범죄 총합 계산
df["총범죄수"] = df[region_cols].sum(axis=1)

# 지역 총합 계산
region_total = df[region_cols].sum()

tab1, tab2, tab3 = st.tabs(
    ["범죄 TOP10", "지역 TOP10", "범죄별 지역분석"]
)

# -----------------------
# 범죄 TOP10
# -----------------------
with tab1:

    crime_top10 = (
        df[["범죄중분류", "총범죄수"]]
        .sort_values("총범죄수", ascending=False)
        .head(10)
    )

    fig = px.bar(
        crime_top10,
        x="범죄중분류",
        y="총범죄수",
        text="총범죄수"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(crime_top10)

# -----------------------
# 지역 TOP10
# -----------------------
with tab2:

    region_df = (
        region_total.reset_index()
    )

    region_df.columns = ["지역", "범죄수"]

    region_df = region_df.sort_values(
        "범죄수",
        ascending=False
    ).head(10)

    fig = px.bar(
        region_df,
        x="지역",
        y="범죄수",
        text="범죄수"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(region_df)

# -----------------------
# 범죄별 지역 분석
# -----------------------
with tab3:

    crime = st.selectbox(
        "범죄 선택",
        df["범죄중분류"]
    )

    selected = df[
        df["범죄중분류"] == crime
    ]

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

    fig = px.bar(
        region_data.head(10),
        x="지역",
        y="건수",
        text="건수",
        title=f"{crime} 발생 지역 TOP10"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(region_data.head(10))
