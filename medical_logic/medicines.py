from typing import Dict, List

# NOTE:
# - This file provides exact OTC medicine names + cheap vs expensive options.
# - Avoids antibiotics/steroids without doctor.
# - Prices are approximate INR ranges.

MED_DB: Dict[str, Dict] = {
    "fever_viral": {
        "title": "Fever / Viral Fever (Exact Medicines + Price Comparison)",
        "cheap": [
            {
                "name": "Paracetamol 500 mg (Generic)",
                "dose": "500 mg every 6–8 hours (adult)",
                "max": "Max 3,000 mg/day (safer limit)",
                "price_inr": "₹10–₹30 / strip (10 tabs)",
                "notes": "First-line for fever/body ache."
            },
            {
                "name": "ORS (WHO ORS)",
                "dose": "Sip frequently (especially if sweating/weakness)",
                "max": "",
                "price_inr": "₹20–₹60 / sachet/pack",
                "notes": "Prevents dehydration."
            },
        ],
        "expensive": [
            {
                "name": "Dolo 650 (Paracetamol 650 mg)",
                "dose": "650 mg every 8 hours if needed (adult)",
                "max": "Avoid combining with other paracetamol medicines",
                "price_inr": "₹30–₹70 / strip",
                "notes": "Branded option; same core drug (paracetamol)."
            },
            {
                "name": "Crocin 500 / Calpol 500 (Paracetamol brands)",
                "dose": "500 mg every 6–8 hours (adult)",
                "max": "Keep total paracetamol under daily limit",
                "price_inr": "₹25–₹60 / strip",
                "notes": "Brand alternatives."
            },
        ],
        "warnings": [
            "Avoid paracetamol if severe liver disease or heavy alcohol use.",
            "Fever ≥39°C, lasts >3 days, rash/bleeding, breathing trouble → doctor urgently.",
        ],
    },

    "cold_flu": {
        "title": "Common Cold / Flu-like Symptoms (Exact Medicines + Price Comparison)",
        "cheap": [
            {
                "name": "Cetirizine 10 mg (Generic)",
                "dose": "10 mg at night (adult)",
                "max": "May cause drowsiness",
                "price_inr": "₹10–₹30 / strip",
                "notes": "For sneezing/runny nose."
            },
            {
                "name": "Paracetamol 500 mg (Generic)",
                "dose": "500 mg every 6–8 hours if fever/body ache (adult)",
                "max": "Max 3,000 mg/day",
                "price_inr": "₹10–₹30 / strip",
                "notes": "If fever/ache is present."
            },
        ],
        "expensive": [
            {
                "name": "Okacet (Cetirizine brand)",
                "dose": "10 mg at night (adult)",
                "max": "May cause drowsiness",
                "price_inr": "₹40–₹90 / strip",
                "notes": "Same medicine, higher cost."
            },
            {
                "name": "Sinarest / D-Cold Total / Coldact (combo cold tablets)",
                "dose": "As per label",
                "max": "Most combos contain paracetamol → avoid duplication",
                "price_inr": "₹80–₹200",
                "notes": "Convenient but costlier; avoid if BP/heart disease unless doctor ok."
            },
        ],
        "warnings": [
            "Avoid decongestant combos if you have high BP/heart disease unless doctor approves.",
            "If breathlessness/chest pain/persistent high fever → urgent care.",
        ],
    },

    "sore_throat": {
        "title": "Sore Throat (Exact Options + Price Comparison)",
        "cheap": [
            {
                "name": "Warm saline gargles",
                "dose": "3–4 times/day",
                "max": "",
                "price_inr": "₹0–₹10",
                "notes": "Very effective for irritation."
            },
            {
                "name": "Strepsils (basic lozenges) / Generic lozenges",
                "dose": "As per label",
                "max": "",
                "price_inr": "₹30–₹80",
                "notes": "Temporary relief."
            },
        ],
        "expensive": [
            {
                "name": "Betadine Gargle (Povidone-Iodine)",
                "dose": "As per label",
                "max": "Avoid if iodine allergy/thyroid issues without doctor advice",
                "price_inr": "₹150–₹300",
                "notes": "Antiseptic gargle; use carefully."
            },
            {
                "name": "Difflam / branded throat sprays",
                "dose": "As per label",
                "max": "",
                "price_inr": "₹180–₹350",
                "notes": "Costlier symptomatic relief."
            },
        ],
        "warnings": [
            "If severe throat pain with difficulty swallowing/breathing → urgent evaluation.",
            "If high fever + swollen tonsils/pus → doctor (may need testing).",
        ],
    },

    "diarrhea": {
        "title": "Diarrhea / Loose Motions (Exact Medicines + Price Comparison)",
        "cheap": [
            {
                "name": "ORS (WHO ORS)",
                "dose": "After each loose stool + frequent sips",
                "max": "",
                "price_inr": "₹20–₹60",
                "notes": "Most important treatment."
            },
            {
                "name": "Econorm (Saccharomyces boulardii) / Generic probiotic",
                "dose": "As per label",
                "max": "",
                "price_inr": "₹60–₹150",
                "notes": "May help recovery."
            },
        ],
        "expensive": [
            {
                "name": "Branded multi-strain probiotics",
                "dose": "As per label",
                "max": "",
                "price_inr": "₹200–₹500",
                "notes": "Costlier; benefit varies."
            },
        ],
        "warnings": [
            "Blood in stool, high fever, severe dehydration, <5 yrs child → doctor urgently.",
            "Avoid antibiotics without doctor advice.",
        ],
    },

    "acidity_reflux": {
        "title": "Acidity / Heartburn (Exact Medicines + Price Comparison)",
        "cheap": [
            {
                "name": "Digene / Gelusil (antacid type)",
                "dose": "After meals/at bedtime as needed",
                "max": "",
                "price_inr": "₹50–₹120",
                "notes": "Fast symptom relief."
            },
        ],
        "expensive": [
            {
                "name": "Pan-D / Pantoprazole-based brands (doctor-guided if frequent)",
                "dose": "As per doctor/label",
                "max": "",
                "price_inr": "₹150–₹350",
                "notes": "Use for frequent reflux after doctor advice."
            },
        ],
        "warnings": [
            "Chest pain, black stools, weight loss, persistent vomiting → urgent evaluation.",
        ],
    },

    "unknown": {
        "title": "General Symptom Relief (Need more details)",
        "cheap": [],
        "expensive": [],
        "warnings": [
            "Please provide symptoms (fever/cough/throat pain/vomiting/diarrhea/etc.) for exact medicine suggestions."
        ],
    },
}


def get_meds_by_category(category: str) -> Dict:
    category = (category or "unknown").strip()
    return MED_DB.get(category, MED_DB["unknown"])


def recommend_medicines(slots: Dict, history_text: str = "") -> Dict:
    """
    Router-compatible: infer category from slots/history and return meds.
    """
    text = (history_text or "").lower()

    symptoms = slots.get("symptoms", [])
    if isinstance(symptoms, str):
        symptoms = [s.strip() for s in symptoms.split(",") if s.strip()]
    if not isinstance(symptoms, list):
        symptoms = []
    symptoms_lower = [s.lower() for s in symptoms if isinstance(s, str)]

    # Infer category
    if ("fever" in symptoms_lower) or ("feaver" in symptoms_lower) or ("fever" in text):
        category = "fever_viral"
    elif any(k in symptoms_lower for k in ["runny_nose", "cough", "breathlessness"]) or any(k in text for k in ["cough", "cold", "sneezing", "runny nose", "congestion"]):
        category = "cold_flu"
    elif ("sore_throat" in symptoms_lower) or ("throat" in text):
        category = "sore_throat"
    elif ("diarrhea" in symptoms_lower) or ("loose" in text) or ("diarrhea" in text):
        category = "diarrhea"
    elif ("stomach_pain" in symptoms_lower) or ("acidity" in text) or ("heartburn" in text) or ("reflux" in text):
        category = "acidity_reflux"
    else:
        category = "unknown"

    return get_meds_by_category(category)


def format_medicine_block(meds: Dict) -> str:
    lines: List[str] = []
    lines.append("## 💊 Medicine Recommendation (Cheap vs Expensive)")
    lines.append(f"**{meds.get('title','')}**\n")

    lines.append("### ✅ Cheap Options")
    cheap = meds.get("cheap", [])
    if cheap:
        for m in cheap:
            lines.append(f"- **{m.get('name','')}** — {m.get('dose','')}")
            if m.get("max"):
                lines.append(f"  - {m.get('max')}")
            if m.get("price_inr"):
                lines.append(f"  - **Approx price:** {m.get('price_inr')}")
            if m.get("notes"):
                lines.append(f"  - _{m.get('notes')}_")
    else:
        lines.append("- (No cheap option available)")

    lines.append("\n### 💎 Expensive Options")
    exp = meds.get("expensive", [])
    if exp:
        for m in exp:
            lines.append(f"- **{m.get('name','')}** — {m.get('dose','')}")
            if m.get("max"):
                lines.append(f"  - {m.get('max')}")
            if m.get("price_inr"):
                lines.append(f"  - **Approx price:** {m.get('price_inr')}")
            if m.get("notes"):
                lines.append(f"  - _{m.get('notes')}_")
    else:
        lines.append("- (No expensive option available)")

    warnings = meds.get("warnings", [])
    if warnings:
        lines.append("\n### ⚠️ Precautions")
        for w in warnings:
            lines.append(f"- {w}")

    lines.append("\n> Prices are approximate and vary by brand/city/pharmacy.")
    return "\n".join(lines)

