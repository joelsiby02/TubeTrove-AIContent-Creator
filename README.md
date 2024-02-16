# TubeTroveAi: YouTube Title and Script Generator with Google Gemini Model

## Introduction
TubeTroveAi is an innovative project that harnesses the power of Generative AI, specifically leveraging Google's cutting-edge Gemini model. The project aims to streamline the content creation process for YouTube creators by generating captivating video titles and scripts effortlessly.

## Key Components
1. **Learning Generative AI:** TubeTroveAi serves as a learning platform for exploring Generative AI. By utilizing Google's Gemini model, creators can deepen their understanding and expertise in this dynamic field.

2. **Title and Script Generation:**
   - **Title Generation:** Model: Google Gemini
     - Task: Generate catchy and relevant YouTube video titles based on user prompts.
   - **Script Generation:** Model: Google Gemini
     - Task: Craft engaging and informative video scripts inspired by the generated titles.

3. **Seamless Integration:** TubeTroveAi seamlessly integrates with Streamlit, providing a user-friendly interface for interacting with the generated content. Langchain facilitates smooth communication with the Google Gemini model, enhancing the overall user experience.

## Setup Guide
Follow these steps to set up and run TubeTroveAi on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone <https://github.com/joelsiby02/TubeTrove-AIContent-Creator.git>
   ```

2. **Install Requirements:**
   ```bash
   cd tubetroveai
   pip install -r requirements.txt
   ```

3. **Obtain Google API Key:**
   - Visit the [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Create a new project (or select an existing one).
   - Navigate to the API & Services > Credentials page.
   - Click on "Create credentials" and select "API key".
   - Copy the generated API key.

4. **Set Environment Variables:**
   - Create a `.env` file in the project directory.
   - Add the following line to the `.env` file, replacing `YOUR_API_KEY` with the obtained API key:
     ```bash
     GOOGLE_API_KEY='YOUR_API_KEY'
     ```

5. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

6. **Access TubeTroveAi:**
   - Open a web browser and navigate to the URL provided by Streamlit.
   - Enter a prompt in the text input field and click on "Generate Response" to generate YouTube titles and scripts.

## Project Output
Experience the magic of TubeTroveAi with the generated YouTube titles and scripts. Revolutionize your content creation process and unleash your creativity with the power of Google's Gemini model!

## Demo Video
Watch our demo video to see TubeTroveAi in action and explore its features firsthand. Discover how our project combines the latest advancements in Generative AI with intuitive user interaction, empowering creators to produce captivating content effortlessly.

[Demo Video on TubeTrove AI (https://www.youtube.com/watch?v=kWPpe0sI7JE)

---

Join me on this exciting journey as we revolutionize content creation with TubeTroveAi. Happy generating! 🚀🎥

Covered basics of Langchain, experimented with the Google Gemini model, built the UI with Streamlit, and utilized Python as the programming language.

Contact me : https://www.linkedin.com/in/joel-siby-752916277/
gmail : joelag1235@gmail.com
