import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="범죄 데이터 분석",
    layout="wide"
)

st.title("🚔 범죄 데이터 분석")

uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except:
        try:
            df = pd.read_csv(uploaded_file, encoding="cp949")
        except:
            df = pd.read_csv(uploaded_file, encoding="euc-kr")

    st.subheader("원본 데이터")

    st.dataframe(df.head())

    st.write("컬럼 목록")
    st.write(list(df.columns))

    # ---------------------------
    # 범죄 종류 컬럼 선택
    # ---------------------------
    crime_col = st.selectbox(
        "범죄 종류 컬럼 선택",
        df.columns
    )

    # ---------------------------
    # 지역 컬럼 선택
    # ---------------------------
    region_col = st.selectbox(
        "지역 컬럼 선택",
        df.columns,
        index=1 if len(df.columns) > 1 else 0
    )

    st.divider()

    # ==========================
    # 범죄 TOP10
    # ==========================
    st.header("📈 범죄 발생 TOP10")

    crime_top10 = (
        df[crime_col]
        .value_counts()
        .reset_index()
    )

    crime_top10.columns = ["범죄", "건수"]

    crime_top10 = crime_top10.head(10)

    fig1 = px.bar(
        crime_top10,
        x="범죄",
        y="건수",
        text="건수"
    )

    fig1.update_layout(
        xaxis_title="범죄 종류",
        yaxis_title="발생 건수"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.dataframe(crime_top10)

    st.divider()

    # ==========================
    # 지역 TOP10
    # ==========================
    st.header("📍 범죄 발생 지역 TOP10")

    region_top10 = (
        df[region_col]
        .value_counts()
        .reset_index()
    )

    region_top10.columns = ["지역", "건수"]

    region_top10 = region_top10.head(10)

    fig2 = px.bar(
        region_top10,
        x="지역",
        y="건수",
        text="건수"
    )

    fig2.update_layout(
        xaxis_title="지역",
        yaxis_title="발생 건수"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.dataframe(region_top10)

    st.divider()

    # ==========================
    # 특정 범죄 분석
    # ==========================
    st.header("🔍 특정 범죄 지역 분석")

    selected_crime = st.selectbox(
        "범죄 선택",
        sorted(df[crime_col].dropna().unique())
    )

    crime_df = df[
        df[crime_col] == selected_crime
    ]

    crime_region = (
        crime_df[region_col]
        .value_counts()
        .reset_index()
    )

    crime_region.columns = ["지역", "건수"]

    crime_region = crime_region.head(10)

    fig3 = px.bar(
        crime_region,
        x="지역",
        y="건수",
        text="건수",
        title=f"{selected_crime} 발생 지역 TOP10"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.dataframe(crime_region)

else:
    st.info("CSV 파일을 업로드하세요.")
