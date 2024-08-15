## Automated FAQ Chatbot for Course Providers
Overview
This project is an advanced Natural Language Processing (NLP) tool designed to automate responses for frequently asked questions (FAQs) in the education sector. The chatbot provides accurate and timely answers based on a dataset of common queries, reducing the need for human intervention.

Tools Used
LangChain: For building the NLP pipeline.
Hugging Face Embeddings: For creating and utilizing embeddings to understand and process text.
FAISS Database: For efficient similarity search and retrieval.
Google Gemini-Pro: For the language model powering the chatbot.
Streamlit: For deploying the application and providing an interactive interface.
Docker: For containerizing the application.

Setup Instructions
Prerequisites
Docker
Docker Compose (optional, for multi-container setups)
Installation
Clone the Repository:
git clone https://github.com/anand23124/CHATBOT-FAQ.git
cd CHATBOT-FAQ

Make sure to create a .env file with the required environment variables before running the container.

Environment Variables
Create a .env file in the root directory of the project with the following variables:

# Example environment variables
HUGGING_FACE_API_KEY=your_hugging_face_api_key
FAISS_INDEX_PATH=/path/to/faiss/index
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key

Access the Application:

Open your browser and go to http://localhost:8501 to interact with the chatbot.

Interaction:

Simply type your question into the chat interface, and the chatbot will provide responses based on the FAQ dataset.


Future Improvements
AWS Deployment: The next steps involve deploying this application on Amazon Web Services (AWS) for scalability.
Additional Features: Potential features include more advanced analytics and integration with other platforms.

Contribution
If you have any questions or would like to collaborate on this project, feel free to reach out. Contributions and feedback are welcome!

License
This project is licensed under the MIT License.

Contact
For any inquiries, please contact:

Name: Anand Sahu
Email: anandsahu5097@gmail.com
Feel free to modify any sections to better fit your project's specifics and your preferred style!







