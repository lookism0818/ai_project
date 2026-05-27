import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

# -----------------------------
# 한글 폰트 설정
# -----------------------------
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("population.csv", encoding='utf-8')

# 컬럼 이름 정리
df.columns = df.columns.str.strip()

st.title("서울시 행정구별 연령 인구 분석")

# -----------------------------
# 행정구 선택
# -----------------------------
district_list = df["행정구역"].unique()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    district_list
)

# -----------------------------
# 선택 데이터 추출
# -----------------------------
selected_data = df[df["행정구역"] == selected_district].iloc[0]

# 나이 컬럼 추출
age_columns = []

for col in df.columns:
    if "세" in col:
        try:
            age = int(col.replace("세", "").replace(" 이상", ""))
            age_columns.append((age, col))
        except:
            pass

# 정렬
age_columns.sort(key=lambda x: x[0])

ages = [x[0] for x in age_columns]
population = [selected_data[x[1]] for x in age_columns]

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    population,
    color='hotpink',
    linewidth=2.5
)

# 제목
ax.set_title(f"{selected_district} 연령별 인구수", fontsize=18)

# 축 이름
ax.set_xlabel("나이", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

# x축 10살 단위 구분선
ax.set_xticks(range(0, 101, 10))

# 세로 구분선
ax.grid(
    axis='x',
    linestyle='--',
    alpha=0.5
)

# 그래프 출력
st.pyplot(fig)
