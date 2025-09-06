import streamlit as st

# ---- Title ----
st.title("🧠 Simple Quiz App")
st.write("Answer the following questions:")

# ---- Quiz Data ----
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Chennai", "Delhi", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the output of 2 + 2 * 2?",
        "options": ["6", "8", "4", "10"],
        "answer": "6"
    },
    {
        "question": "Who is the current Prime Minister of India (as of 2024)?",
        "options": ["Rahul Gandhi", "Amit Shah", "Narendra Modi", "Manmohan Singh"],
        "answer": "Narendra Modi"
    },
    {
        "question": "What is the largest animal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        "answer": "Blue Whale"
    },
    {
        "question": "Which language is primarily spoken in Tamil Nadu?",
        "options": ["Telugu", "Hindi", "Kannada", "Tamil"],
        "answer": "Tamil"
    },
    {
        "question": "What is the freezing point of water?",
        "options": ["0°C", "100°C", "32°C", "50°C"],
        "answer": "0°C"
    },
    {
        "question": "Which festival is known as the festival of lights?",
        "options": ["Holi", "Pongal", "Diwali", "Eid"],
        "answer": "Diwali"
    },
    {
        "question": "Which organ pumps blood throughout the human body?",
        "options": ["Brain", "Lungs", "Heart", "Kidney"],
        "answer": "Heart"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["Thomas Edison", "Einstein", "Newton", "Alexander Graham Bell"],
        "answer": "Thomas Edison"
    },
    {
        "question": "What is the national flower of India?",
        "options": ["Rose", "Sunflower", "Lotus", "Jasmine"],
        "answer": "Lotus"
    },
    {
        "question": "How many hours are there in a day?",
        "options": ["12", "24", "48", "60"],
        "answer": "24"
    },
    {
        "question": "Which is the largest continent in the world?",
        "options": ["Africa", "Asia", "Europe", "Australia"],
        "answer": "Asia"
    }
]

# ---- Quiz Form ----
score = 0
user_answers = []

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['question']}**")
        user_answer = st.radio("Choose your answer:", q["options"], key=i)
        user_answers.append(user_answer)

    submitted = st.form_submit_button("Submit Quiz")

# ---- Show Result ----
if submitted:
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"🎉 You scored {score} out of {len(questions)}!")

    # Show correct answers
    with st.expander("See correct answers"):
        for i, q in enumerate(questions):
            st.write(f"**Q{i+1}: {q['question']}**")
            st.write(f"Your answer: {user_answers[i]}")
            st.write(f"Correct answer: {q['answer']}")
            st.markdown("---")
