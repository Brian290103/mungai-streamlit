import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="AIzaSyCpQDxIUeY8Tcviqj7qeKSM6WckAOZbfkE")  # Replace with your actual API key

# Set up the model
generation_config = {
    "temperature": 1,
    "top_k": 40,
    "top_p": 0.95,
    "max_output_tokens": 512,
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Set page title and description
st.set_page_config(page_title="Isaac Mungai Chatbot", page_icon="🤖", layout="wide")

# Sidebar for poster and party leadership positions
with st.sidebar:
    st.image("poster.png", caption="Isaac Mungai Campaign Poster")
    st.title("O.K.A")
    st.title("Isaac Mungai")
    st.title("For SCIT Representative")

# Main content area
st.title("Isaac Mungai for SCIT Rep.")
st.write("""
Hello! I am Isaac Mungai, a Computer Science Year 2 student at Kaimosi Friends University, vying for the position of School of Computing and Information Technology (SCIT) Representative under the OKA party. 
I am asking for your support and votes. Together, let's make SCIT better! ✅
""")

# Contact information
st.write("""
**Contact Information:**
- **WhatsApp Phone Number**: [+254 103 273 776](https://wa.me/254103273776)  
""")

# Chatbot section
st.header("Ask me anything about my campaign!")

# Text area for user queries
user_input = st.text_area("What would you like to know?", key="user_input", height=150)

# Submit button
if st.button("Submit"):
    if user_input:
        # Provide context for the AI
        # Provide context for the AI
        context = """
        I am Isaac Mungai, a Computer Science Year 2 student at Kaimosi Friends University, running for the position of SCIT Representative under the OKA party. My campaign is focused on improving the SCIT experience for all students. Here are my key goals:
        
        1. **Host hackathons**: I will organize regular hackathons to foster innovation, collaboration, and practical problem-solving among students.
        2. **Equip ICT labs**: I will ensure that ICT labs are well-equipped with modern tools and resources to support learning and innovation.
        3. **Revive Kaimosi Computing Association (KCA)**: I will work to revive the KCA to provide a platform for students to collaborate, share ideas, and grow together.
        
        My slogan is **INNOVATE, ELEVATE, REPRESENT**. I am committed to fostering a collaborative and innovative environment where students can thrive and achieve their full potential. Together, we can make SCIT better!
        """
        
        # Use prompt engineering to guide the AI's response
        prompt = f"""
        You are Isaac Mungai, a candidate for the SCIT Representative position at Kaimosi Friends University. Your goal is to respond to questions as if you are Isaac Mungai, ensuring that users cannot differentiate between you and the real Isaac. Respond in the first person, be direct, and focus on your campaign goals and vision for the students. Keep your responses concise and to the point.
        
        If the user asks about my objectives or plans, respond with a clear and numbered list.
        
        Here is the context about Isaac Mungai and his campaign:
        {context}
        
        Question: {user_input}
        
        Response:
        """

        # Generate response using the Gemini model
        response = model.generate_content(prompt)
        bot_response = response.text

        # Display the bot's response
        st.subheader("Isaac Mungai's Response")
        st.write(bot_response)
    else:
        st.warning("Please enter a question before submitting.")

# Display the poster below the chatbot section
st.image("poster.png", caption="Isaac Mungai Campaign Poster", use_container_width=True)
