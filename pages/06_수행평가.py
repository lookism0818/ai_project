import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🚔 대한민국 범죄 분석 대시보드",
    page_icon="🚔",
    layout="wide"
)

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("lookism!!!!!!(1).csv", encoding="utf-8")
    return df

df = load_data()

st.title("🚔 대한민국 범죄 분석 대시보드")
st.markdown("### 😎 범죄 데이터를 쉽고 재미있게 분석해보자!")

# -----------------------------
# 컬럼 확인
# -----------------------------
st.sidebar.header("⚙️ 설정")

crime_col = st.sidebar.selectbox(
    "🚨 범죄 종류 컬럼 선택",
    df.columns
)

region_col = st.sidebar.selectbox(
    "🗺️ 지역 컬럼 선택",
    df.columns
)

count_col = st.sidebar.selectbox(
    "📊 발생건수 컬럼 선택",
    df.select_dtypes(include="number").columns
)

# -----------------------------
# 전체 요약
# -----------------------------
st.header("📈 전체 현황")

total_crime = int(df[count_col].sum())

col1, col2 = st.columns(2)

with col1:
    st.metric("🚨 전체 범죄 발생 건수", f"{total_crime:,}건")

with col2:
    st.metric("📍 분석 지역 수", df[region_col].nunique())

# -----------------------------
# 범죄 TOP10
# -----------------------------
st.header("🏆 범죄 발생 TOP 10")

crime_top10 = (
    df.groupby(crime_col)[count_col]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    crime_top10,
    x=count_col,
    y=crime_col,
    orientation="h",
    text=count_col,
    title="🚨 가장 많이 발생한 범죄 TOP10"
)

fig1.update_layout(height=600)
st.plotly_chart(fig1, use_container_width=True)

# 설명
st.subheader("🧐 TOP10 범죄 설명")

for idx, row in crime_top10.iterrows():
    rank = idx + 1

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    emoji = medals.get(rank, "🔹")

    st.markdown(
        f"{emoji} **{rank}위 {row[crime_col]}** → "
        f"총 **{row[count_col]:,}건** 발생"
    )

# -----------------------------
# 지역 TOP10
# -----------------------------
st.header("🗺️ 범죄가 많이 발생한 지역 TOP10")

region_top10 = (
    df.groupby(region_col)[count_col]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    region_top10,
    x=region_col,
    y=count_col,
    text=count_col,
    title="📍 범죄 발생 지역 TOP10"
)

fig2.update_layout(height=600)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# 지역 설명
# -----------------------------
st.subheader("📢 지역 분석")

top_region = region_top10.iloc[0]

st.success(
    f"🚨 가장 많은 범죄가 발생한 지역은 "
    f"**{top_region[region_col]}**이며 "
    f"총 **{top_region[count_col]:,}건** 발생했어!"
)

st.info(
    "💡 일반적으로 인구가 많고 상업시설이 밀집된 지역은 "
    "범죄 발생 건수도 높게 나타나는 경향이 있어!"
)

# -----------------------------
# 범죄별 지역 분석
# -----------------------------
st.header("🔍 범죄별 지역 분석")

selected_crime = st.selectbox(
    "🚨 범죄를 선택해봐!",
    sorted(df[crime_col].unique())
)

filtered = df[df[crime_col] == selected_crime]

crime_region = (
    filtered.groupby(region_col)[count_col]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    crime_region,
    x=region_col,
    y=count_col,
    text=count_col,
    title=f"🚨 {selected_crime} 발생 지역 TOP10"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# 원형 그래프
# -----------------------------
st.header("🥧 범죄 비율 분석")

crime_ratio = (
    df.groupby(crime_col)[count_col]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.pie(
    crime_ratio,
    names=crime_col,
    values=count_col,
    hole=0.4,
    title="🥧 범죄 비율 TOP10"
)

st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# 데이터 보기
# -----------------------------
with st.expander("📄 원본 데이터 보기"):
    st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown(
    "😎 Made with Streamlit | 🚔 범죄 데이터를 쉽고 재밌게 분석해보자!"
)
