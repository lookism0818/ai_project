import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🚨 대한민국 범죄 분석",
    page_icon="🚔",
    layout="wide"
)

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("lookism!!!!!!(1).csv", encoding="cp949")

df = load_data()

# 지역 컬럼
region_cols = df.columns[2:]

# 범죄별 총 발생 건수 계산
crime_total = df.copy()
crime_total["총건수"] = crime_total[region_cols].sum(axis=1)

top10_crime = (
    crime_total[["범죄대분류", "범죄중분류", "총건수"]]
    .sort_values("총건수", ascending=False)
    .head(10)
)

# 지역별 총 발생 건수 계산
region_total = df[region_cols].sum()

top10_region = (
    pd.DataFrame({
        "지역": region_total.index,
        "총건수": region_total.values
    })
    .sort_values("총건수", ascending=False)
    .head(10)
)

# -----------------------------
# 제목
# -----------------------------
st.title("🚨 대한민국 범죄 분석 대시보드")
st.markdown("### 😎 범죄 데이터를 쉽고 재미있게 분석해보자!")

# -----------------------------
# TOP 통계
# -----------------------------
c1, c2 = st.columns(2)

with c1:
    st.metric(
        "🔥 가장 많이 발생한 범죄",
        top10_crime.iloc[0]["범죄중분류"]
    )

with c2:
    st.metric(
        "🏙️ 범죄 발생 1위 지역",
        top10_region.iloc[0]["지역"]
    )

st.divider()

# -----------------------------
# 그래프
# -----------------------------
left, right = st.columns(2)

with left:
    st.subheader("🔥 범죄 TOP10")

    fig1 = px.bar(
        top10_crime.sort_values("총건수"),
        x="총건수",
        y="범죄중분류",
        orientation="h",
        text="총건수"
    )

    fig1.update_layout(height=600)

    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("🏙️ 범죄 발생 지역 TOP10")

    fig2 = px.bar(
        top10_region.sort_values("총건수"),
        x="총건수",
        y="지역",
        orientation="h",
        text="총건수"
    )

    fig2.update_layout(height=600)

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# -----------------------------
# 범죄 TOP10 설명
# -----------------------------
st.header("🔥 가장 많이 발생한 범죄 TOP10")

medals = ["🥇","🥈","🥉","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]

for i, row in enumerate(top10_crime.itertuples()):
    st.markdown(
        f"{medals[i]} **{row.범죄중분류}** "
        f"({row.범죄대분류}) → "
        f"**{row.총건수:,}건**"
    )

st.divider()

# -----------------------------
# 지역 TOP10 설명
# -----------------------------
st.header("🏙️ 범죄가 많이 발생한 지역 TOP10")

for i, row in enumerate(top10_region.itertuples()):
    st.markdown(
        f"{medals[i]} **{row.지역}** → "
        f"**{row.총건수:,}건**"
    )

st.divider()

# -----------------------------
# 청소년 친화 설명
# -----------------------------
st.header("🧐 한눈에 보는 결과")

st.success(f"""
🔥 가장 많이 발생한 범죄는 **{top10_crime.iloc[0]['범죄중분류']}** 이야!

요즘은 직접 싸우는 범죄보다
📱 인터넷, 문자, 전화 등을 이용한 범죄가 정말 많아.

모르는 링크 누르기,
개인정보 알려주기는 조심하자! ⚠️
""")

st.info(f"""
🏙️ 범죄 발생 건수가 가장 높은 지역은
**{top10_region.iloc[0]['지역']}** 이야.

하지만 범죄 건수가 많다고
무조건 위험한 곳이라는 뜻은 아니야!

👨‍👩‍👧‍👦 인구가 많고
🚗 사람들이 많이 이동하는 지역일수록
범죄 신고 건수도 함께 증가하는 경향이 있어.
""")

st.markdown("""
### 💡 흥미로운 사실

- 📱 사기 관련 범죄가 매우 많음
- 👊 폭행과 상해도 꾸준히 발생
- 🚗 교통범죄 비중도 높음
- 🏢 대도시에서 범죄 건수가 높게 나타남

우리 모두 안전한 인터넷 생활과 개인정보 보호를 실천하자! 🔒😎
""")
