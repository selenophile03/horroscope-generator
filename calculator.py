import random

ZODIAC_SIGNS = [
    {"sign": "Capricorn", "start": (12, 22), "end": (1, 19)},
    {"sign": "Aquarius", "start": (1, 20), "end": (2, 18)},
    {"sign": "Pisces", "start": (2, 19), "end": (3, 20)},
    {"sign": "Aries", "start": (3, 21), "end": (4, 19)},
    {"sign": "Taurus", "start": (4, 20), "end": (5, 20)},
    {"sign": "Gemini", "start": (5, 21), "end": (6, 20)},
    {"sign": "Cancer", "start": (6, 21), "end": (7, 22)},
    {"sign": "Leo", "start": (7, 23), "end": (8, 22)},
    {"sign": "Virgo", "start": (8, 23), "end": (9, 22)},
    {"sign": "Libra", "start": (9, 23), "end": (10, 22)},
    {"sign": "Scorpio", "start": (10, 23), "end": (11, 21)},
    {"sign": "Sagittarius", "start": (11, 22), "end": (12, 21)}
]

PREDICTIONS = {
    "love": [
        "A surprise interaction sparks deep affection today.",
        "Clear communication will heal a lingering misunderstanding.",
        "Prioritize quality time over material gestures."
    ],
    "career": [
        "A sudden problem highlights your exceptional problem-solving skills.",
        "Your focus shifts toward long-term professional stability.",
        "Collaborating with an unlikely peer yields great ideas."
    ],
    "wellness": [
        "Your physical energy peaks; it is a good time for a challenging activity.",
        "Incorporate deliberate rest to counter mental clutter.",
        "Hydration and fresh air will dramatically lift your mood."
    ]
}

def get_zodiac_sign(month: int, day: int) -> str:
    """Calculates the matching zodiac sign using birth month and day."""
    for z in ZODIAC_SIGNS:
        m_start, d_start = z["start"]
        m_end, d_end = z["end"]
        
        if (month == m_start and day >= d_start) or (month == m_end and day <= d_end):
            return z["sign"]
            
    # Fallback default boundary handling
    return "Capricorn"

def generate_horoscope_report(sign: str) -> dict:
    """Assembles a randomized, structured daily horoscope prediction matrix."""
    return {
        "zodiac": sign,
        "love": random.choice(PREDICTIONS["love"]),
        "career": random.choice(PREDICTIONS["career"]),
        "wellness": random.choice(PREDICTIONS["wellness"]),
        "lucky_number": random.randint(1, 99),
        "lucky_color": random.choice(["Emerald", "Indigo", "Amber", "Crimson", "Slate"])
    }
