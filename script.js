const ZODIAC_SIGNS = [
    { name: "Capricorn", element: "Earth", start: [12, 22], end: [1, 19] },
    { name: "Aquarius", element: "Air", start: [1, 20], end: [2, 18] },
    { name: "Pisces", element: "Water", start: [2, 19], end: [3, 20] },
    { name: "Aries", element: "Fire", start: [3, 21], end: [4, 19] },
    { name: "Taurus", element: "Earth", start: [4, 20], end: [5, 20] },
    { name: "Gemini", element: "Air", start: [5, 21], end: [6, 20] },
    { name: "Cancer", element: "Water", start: [6, 21], end: [7, 22] },
    { name: "Leo", element: "Fire", start: [7, 23], end: [8, 22] },
    { name: "Virgo", element: "Earth", start: [8, 23], end: [9, 22] },
    { name: "Libra", element: "Air", start: [9, 23], end: [10, 22] },
    { name: "Scorpio", element: "Water", start: [10, 23], end: [11, 21] },
    { name: "Sagittarius", element: "Fire", start: [11, 22], end: [12, 21] }
];

const LOVE_PROFILES = [
    "You seek strong independent bonds. Your relationships thrive when built on mutual space and project collaboration rather than emotional hyper-dependency.",
    "Deeply protective and highly analytical, your love life scales up significantly once basic vulnerabilities are safely shared with a trusted partner.",
    "A fluid and naturally empathetic connection style means you absorb your partner's moods. Guard your boundaries carefully to avoid burnout.",
    "Driven by immediate spark and shared ideals, your primary challenge is maintaining structural long-term stability once the initial novelty evens out."
];

const LIFE_TIMELINES = [
    "Your path points to structural mid-life transitions where prior career investments drop away to open up major independent creative work.",
    "A highly balanced trajectory marked by rapid early development followed by a deliberate, peaceful deceleration focused on mentorship and legacy.",
    "Prone to unexpected cyclical pivots. You will fundamentally reinvent your core lifestyle profile at least twice during your lifespan.",
    "A steady, linear build toward complete financial and spatial security, ensuring your later decades are characterized by profound autonomy."
];

function getZodiacSign(month, day) {
    return ZODIAC_SIGNS.find(sign => {
        const [sMonth, sDay] = sign.start;
        const [eMonth, eDay] = sign.end;
        return (month === sMonth && day >= sDay) || (month === eMonth && day <= eDay);
    }) || ZODIAC_SIGNS[0];
}

function handleCalculation() {
    const dobValue = document.getElementById('dob-input').value;
    if (!dobValue) return;

    const dob = new Date(dobValue);
    const month = dob.getMonth() + 1; 
    const day = dob.getDate();
    const birthYear = dob.getFullYear();

    const sign = getZodiacSign(month, day);
    
    const dateSeed = day + month + birthYear;
    const loveIndex = dateSeed % LOVE_PROFILES.length;
    const timelineIndex = (dateSeed + 2) % LIFE_TIMELINES.length;

    const calculatedAge = 74 + (dateSeed % 23); 
    const luckyYear = birthYear + 28 + (dateSeed % 12); 

    document.getElementById('output-sign').textContent = sign.name;
    document.getElementById('output-element').textContent = sign.element;
    document.getElementById('love-text').textContent = LOVE_PROFILES[loveIndex];
    document.getElementById('timeline-text').textContent = LIFE_TIMELINES[timelineIndex];
    document.getElementById('meta-age').textContent = calculatedAge;
    document.getElementById('meta-year').textContent = luckyYear;

    document.getElementById('output-card').classList.remove('hidden');
}

document.getElementById('generate-btn').addEventListener('click', handleCalculation);
