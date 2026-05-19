import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

st.title("🌏 외국인이 좋아하는 서울 관광지 TOP10")
st.markdown("Folium 지도로 서울 주요 관광지를 표시합니다.")

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# Folium 지도 생성
m = folium.Map(
    location=seoul_center,
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 관광지 데이터
tour_places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 시대의 대표 궁궐"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 먹거리의 중심"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리"
    },
    {
        "name": "홍대거리",
        "lat": 37.556350,
        "lon": 126.922672,
        "desc": "젊음과 예술의 거리"
    },
    {
        "name": "인사동",
        "lat": 37.574187,
        "lon": 126.984956,
        "desc": "전통 문화 체험"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.513068,
        "lon": 127.102926,
        "desc": "서울 랜드마크 초고층 빌딩"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "현대 건축 명소"
    },
    {
        "name": "한강공원",
        "lat": 37.520694,
        "lon": 126.939332,
        "desc": "서울 시민 휴식 공간"
    },
    {
        "name": "코엑스",
        "lat": 37.512524,
        "lon": 127.058819,
        "desc": "쇼핑·전시·스타필드 도서관"
    }
]

# 마커 추가
for place in tour_places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"""
        <b>{place['name']}</b><br>
        {place['desc']}
        """,
        tooltip=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Streamlit에 지도 출력
st_folium(
    m,
    width=1200,
    height=700
)

# 관광지 리스트 출력
st.subheader("📍 관광지 리스트")

for idx, place in enumerate(tour_places, start=1):
    st.write(f"{idx}. {place['name']} - {place['desc']}")
