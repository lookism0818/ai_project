import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🚨 대한민국 범죄 분석",
    page_icon="🚔",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("lookism!!!!!!(1).csv", encoding="euc-kr")
    return df

df = load_data()

region_cols = df.columns[2:]

# 범죄별 총합
crime_df = df.copy()
crime_df["합계"] = crime_df[region_cols].sum(axis=1)

top_crime = crime_df.sort_values("합계", ascending=False).head(10)

# 지역별 총합
region_total = df[region_cols].sum().sort_values(ascending=False)
top_region = region_total.head(10)

st.title("🚨 대한민국 범죄 분석 대시보드")
st.markdown("### 📊 범죄 데이터를 쉽고 재미있게 알아보자!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 가장 많이 발생한 범죄 TOP10")

    fig1 = px.bar(
        top_crime,
        x="합계",
        y="범죄중분류",
        orientation="h",
        text="합계"
    )

    fig1.update_layout(height=500)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🏙️ 범죄 발생 지역 TOP10")

    region_df = pd.DataFrame({
        "지역": top_region.index,
        "건수": top_region.values
    })

    fig2 = px.bar(
        region_df,
        x="건수",
        y="지역",
        orientation="h",
        text="건수"
    )

    fig2.update_layout(height=500)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.header("🔥 범죄 TOP10 설명")

emoji = ["🥇","🥈","🥉","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]

for i, (_, row) in enumerate(top_crime.iterrows()):
    st.markdown(
        f"{emoji[i]} **{row['범죄중분류']}** : "
        f"**{row['합계']:,}건**"
    )

st.divider()

st.header("🏙️ 범죄가 가장 많이 발생하는 지역")

for i, (region, value) in enumerate(top_region.items()):
    st.markdown(
        f"{emoji[i]} **{region}** : "
        f"**{value:,}건**"
    )

st.divider()

st.header("🧐 한눈에 보는 분석")

st.success("""
🚨 가장 많이 발생한 범죄는 **사기**였어!

요즘은 직접적인 범죄보다
전화·문자·인터넷을 이용한 사기가 정말 많아.
그래서 모르는 링크 누르기, 개인정보 공유하기는 조심해야 해! ⚠️
""")

st.info("""
🏙️ 범죄가 가장 많이 발생한 지역은 **경기도 수원시**였어.

하지만 범죄 건수가 많다고 해서 위험한 도시라는 뜻은 아니야!
인구가 많고 활동 인구가 많은 도시일수록
범죄 신고 건수도 자연스럽게 늘어나는 경향이 있어. 👀
""")

st.markdown("""
### 💡 재미있는 사실

- 📱 사기 범죄가 압도적 1위
- 👊 폭행은 여전히 많이 발생
- 🚗 교통범죄도 매우 높은 비중 차지
- 🏢 대도시일수록 전체 범죄 건수가 높게 나타남

안전한 인터넷 사용과 개인정보 보호가 점점 더 중요해지고 있어! 🔒
""")
