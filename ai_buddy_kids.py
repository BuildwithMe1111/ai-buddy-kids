import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]
st.set_page_config(page_title="AI Buddy for Kids", page_icon="👧")

st.title("👧✨ AI Buddy – Your Smart Friend for School & Emotions")

# Ask name and age
name = st.text_input("Hi! What's your name?")
age = st.number_input("How old are you?", min_value=5, max_value=18, step=1)

if name and age:
    st.markdown(f"Welcome, **{name}**! You're {int(age)} – that's awesome! 🎉")

    mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😞 Sad", "😡 Frustrated", "🤩 Excited", "😐 Okay"])

    if mood:
        followup_prompt = f"""
        You are a kind, playful AI friend for a {int(age)}-year-old child named {name}.
        They are feeling {mood}. Ask a fun or thoughtful follow-up question like "What made you smile today?" or "Want to play a game?" in a friendly, kid-safe tone.
        """
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": followup_prompt}]
        )
        st.markdown(f"🧠 AI Buddy says: {response.choices[0].message.content}")