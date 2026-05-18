import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천 🌈",
    page_icon="💼",
    layout="centered"
)

# MBTI별 데이터
mbti_data = {
    "INTJ": {
        "job1": {
            "name": "데이터 사이언티스트 📊",
            "major": "컴퓨터공학과, 데이터사이언스학과",
            "personality": "논리적이고 분석적인 사람에게 잘 어울려!",
            "salary": "평균 연봉 약 6,500만원"
        },
        "job2": {
            "name": "전략 기획가 🧠",
            "major": "경영학과, 경제학과",
            "personality": "계획 세우는 걸 좋아하는 성격에게 추천!",
            "salary": "평균 연봉 약 5,500만원"
        }
    },

    "INTP": {
        "job1": {
            "name": "AI 개발자 🤖",
            "major": "인공지능학과, 컴퓨터공학과",
            "personality": "호기심 많고 아이디어가 풍부한 사람에게 딱!",
            "salary": "평균 연봉 약 7,000만원"
        },
        "job2": {
            "name": "연구원 🔬",
            "major": "물리학과, 화학과",
            "personality": "깊게 탐구하는 걸 좋아하면 좋아!",
            "salary": "평균 연봉 약 5,800만원"
        }
    },

    "ENTJ": {
        "job1": {
            "name": "CEO 👑",
            "major": "경영학과",
            "personality": "리더십 강하고 추진력 있는 사람에게 추천!",
            "salary": "평균 연봉 약 8,000만원 이상"
        },
        "job2": {
            "name": "변호사 ⚖️",
            "major": "법학과",
            "personality": "논리적으로 말 잘하는 성격에게 잘 맞아!",
            "salary": "평균 연봉 약 7,500만원"
        }
    },

    "ENTP": {
        "job1": {
            "name": "마케팅 기획자 📢",
            "major": "광고홍보학과, 경영학과",
            "personality": "창의적이고 아이디어 넘치는 사람 추천!",
            "salary": "평균 연봉 약 5,000만원"
        },
        "job2": {
            "name": "유튜버 🎥",
            "major": "미디어학과",
            "personality": "사람들과 소통하는 걸 좋아하면 최고!",
            "salary": "평균 연봉은 다양하지만 인기 크리에이터는 고수익!"
        }
    },

    "INFJ": {
        "job1": {
            "name": "상담사 💖",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람에게 추천!",
            "salary": "평균 연봉 약 4,500만원"
        },
        "job2": {
            "name": "작가 ✍️",
            "major": "문예창작학과",
            "personality": "감수성이 풍부한 성격에게 잘 맞아!",
            "salary": "평균 연봉은 작품 활동에 따라 달라져!"
        }
    },

    "INFP": {
        "job1": {
            "name": "일러스트레이터 🎨",
            "major": "디자인학과",
            "personality": "상상력 풍부하고 감성적인 사람 추천!",
            "salary": "평균 연봉 약 4,000만원"
        },
        "job2": {
            "name": "사회복지사 🤝",
            "major": "사회복지학과",
            "personality": "따뜻하고 배려심 많은 성격에게 좋아!",
            "salary": "평균 연봉 약 3,500만원"
        }
    },

    "ENFJ": {
        "job1": {
            "name": "교사 🍎",
            "major": "교육학과",
            "personality": "사람을 이끄는 걸 좋아하는 성격 추천!",
            "salary": "평균 연봉 약 5,200만원"
        },
        "job2": {
            "name": "HR 매니저 🧑‍💼",
            "major": "경영학과",
            "personality": "사람들과 협력 잘하는 성격에게 딱!",
            "salary": "평균 연봉 약 5,500만원"
        }
    },

    "ENFP": {
        "job1": {
            "name": "광고 디자이너 🌟",
            "major": "시각디자인학과",
            "personality": "창의력 넘치고 활발한 사람 추천!",
            "salary": "평균 연봉 약 4,800만원"
        },
        "job2": {
            "name": "행사 기획자 🎉",
            "major": "이벤트학과, 관광학과",
            "personality": "재미있는 걸 좋아하는 성격에게 잘 맞아!",
            "salary": "평균 연봉 약 4,500만원"
        }
    },

    "ISTJ": {
        "job1": {
            "name": "공무원 🏛️",
            "major": "행정학과",
            "personality": "책임감 강하고 꼼꼼한 사람 추천!",
            "salary": "평균 연봉 약 4,500만원"
        },
        "job2": {
            "name": "회계사 💰",
            "major": "회계학과",
            "personality": "정리 잘하고 숫자에 강한 성격에게 좋아!",
            "salary": "평균 연봉 약 7,000만원"
        }
    },

    "ISFJ": {
        "job1": {
            "name": "간호사 🏥",
            "major": "간호학과",
            "personality": "배려심 많고 책임감 있는 사람 추천!",
            "salary": "평균 연봉 약 5,000만원"
        },
        "job2": {
            "name": "초등교사 📚",
            "major": "교육학과",
            "personality": "친절하고 참을성 있는 성격에게 딱!",
            "salary": "평균 연봉 약 5,200만원"
        }
    },

    "ESTJ": {
        "job1": {
            "name": "경찰관 🚔",
            "major": "경찰행정학과",
            "personality": "리더십 있고 정의로운 성격 추천!",
            "salary": "평균 연봉 약 5,000만원"
        },
        "job2": {
            "name": "프로젝트 매니저 📋",
            "major": "경영학과",
            "personality": "체계적으로 관리 잘하는 사람에게 좋아!",
            "salary": "평균 연봉 약 6,000만원"
        }
    },

    "ESFJ": {
        "job1": {
            "name": "승무원 ✈️",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람 추천!",
            "salary": "평균 연봉 약 4,500만원"
        },
        "job2": {
            "name": "호텔리어 🏨",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 강한 성격에게 잘 맞아!",
            "salary": "평균 연봉 약 4,300만원"
        }
    },

    "ISTP": {
        "job1": {
            "name": "자동차 엔지니어 🚗",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하는 사람 추천!",
            "salary": "평균 연봉 약 6,000만원"
        },
        "job2": {
            "name": "파일럿 🛫",
            "major": "항공운항학과",
            "personality": "침착하고 집중력 강한 성격에게 좋아!",
            "salary": "평균 연봉 약 8,000만원"
        }
    },

    "ISFP": {
        "job1": {
            "name": "패션 디자이너 👗",
            "major": "패션디자인학과",
            "personality": "감각적이고 자유로운 성격 추천!",
            "salary": "평균 연봉 약 4,500만원"
        },
        "job2": {
            "name": "플로리스트 🌸",
            "major": "원예학과",
            "personality": "예쁜 걸 좋아하고 섬세한 사람에게 딱!",
            "salary": "평균 연봉 약 3,500만원"
        }
    },

    "ESTP": {
        "job1": {
            "name": "영업 전문가 💼",
            "major": "경영학과",
            "personality": "도전적이고 말 잘하는 사람 추천!",
            "salary": "평균 연봉 약 5,500만원"
        },
        "job2": {
            "name": "운동선수 ⚽",
            "major": "체육학과",
            "personality": "활동적이고 에너지 넘치는 성격에게 좋아!",
            "salary": "종목에 따라 매우 다양해!"
        }
    },

    "ESFP": {
        "job1": {
            "name": "배우 🎭",
            "major": "연극영화과",
            "personality": "끼 많고 밝은 성격 추천!",
            "salary": "평균 연봉은 활동에 따라 달라져!"
        },
        "job2": {
            "name": "방송인 📺",
            "major": "방송연예과",
            "personality": "사람들 앞에서 자신감 있는 사람에게 딱!",
            "salary": "평균 연봉 약 5,000만원 이상"
        }
    }
}

# 제목
st.title("🌈 MBTI 진로 추천 프로그램")
st.write("너의 MBTI에 딱 맞는 직업을 추천해줄게! 😆")

# MBTI 선택
selected_mbti = st.selectbox(
    "✨ MBTI를 선택해봐!",
    list(mbti_data.keys())
)

# 버튼
if st.button("🔍 진로 추천 보기"):
    data = mbti_data[selected_mbti]

    st.success(f"{selected_mbti} 유형에게 추천하는 진로야! 🎉")

    # 첫 번째 직업
    st.subheader(f"1️⃣ {data['job1']['name']}")
    st.write(f"📚 추천 학과 : {data['job1']['major']}")
    st.write(f"💖 잘 맞는 성격 : {data['job1']['personality']}")
    st.write(f"💰 {data['job1']['salary']}")

    st.divider()

    # 두 번째 직업
    st.subheader(f"2️⃣ {data['job2']['name']}")
    st.write(f"📚 추천 학과 : {data['job2']['major']}")
    st.write(f"💖 잘 맞는 성격 : {data['job2']['personality']}")
    st.write(f"💰 {data['job2']['salary']}")

    st.balloons()

# 하단 문구
st.markdown("---")
st.caption("🌟 미래의 꿈을 응원할게! 화이팅 😎")
