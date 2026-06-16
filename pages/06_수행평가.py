import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="지역별 범죄 분석",
    layout="wide"
)

st.title("🚔 지역별 범죄 분석")

# CSV 읽기
df = pd.read_csv("lookism!!!!!!(1).csv", encoding="cp949")

# 지역 컬럼
regions = list(df.columns[2:])

# 지역 선택
selected_region = st.selectbox(
    "지역 선택",
    regions
)

# 선택 지역 데이터
crime_df = df[["범죄중분류", selected_region]].copy()

crime_df.columns = ["범죄종류", "발생건수"]

crime_df["발생건수"] = pd.to_numeric(
    crime_df["발생건수"],
    errors="coerce"
).fillna(0)

crime_df = crime_df.sort_values(
    "발생건수",
    ascending=False
)

# 색상 구분
crime_df["구분"] = crime_df["발생건수"].apply(
    lambda x: "200,000 이상" if x >= 200000 else "200,000 미만"
)

st.subheader(f"📍 {selected_region} 범죄 현황")

fig = px.bar(
    crime_df,
    x="범죄종류",
    y="발생건수",
    color="구분",
    color_discrete_map={
        "200,000 이상": "red",
        "200,000 미만": "blue"
    },
    text="발생건수"
)

fig.update_layout(
    xaxis_title="범죄 종류",
    yaxis_title="발생 건수",
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    crime_df,
    use_container_width=True
)

# 최다 범죄 표시
top_crime = crime_df.iloc[0]

st.success(
    f"가장 많이 발생한 범죄는 '{top_crime['범죄종류']}'이며 "
    f"{int(top_crime['발생건수']):,}건 발생했습니다."
)
