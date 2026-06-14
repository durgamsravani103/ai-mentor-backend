import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_roadmap(role, skill_level, weak_areas):
    prompt = f"""
    Generate a 6-month placement preparation roadmap.

    Role: {role}
    Skill Level: {skill_level}
    Weak Areas: {weak_areas}

    Give roadmap month-wise.
    """

    response = model.generate_content(prompt)

    return response.text