from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


import os 

load_dotenv()

google_api_key=os.environ['GOOGLE_API_KEY']

llm = ChatGoogleGenerativeAI(api_key=google_api_key,model="gemini-pro",temperature=0)

#Read the CSV file and load data
#create embeddings and save it in vector database
embeddings = HuggingFaceInstructEmbeddings(
    query_instruction="Represent the query for retrieval:"
)
vectordb_file_path="faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path='codebasics_faqs.csv', source_column='prompt')
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data,embedding=embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    # Load the vector database
    vectordb = FAISS.load_local(folder_path=vectordb_file_path,embeddings=embeddings, allow_dangerous_deserialization=True)

    #Create a retriever 
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(template = prompt_template, input_variables=["context","question"])

    chain = RetrievalQA.from_chain_type(llm=llm, 
           chain_type="stuff",
            retriever=retriever,
            input_key="query",
            return_source_documents=True,
            chain_type_kwargs={"prompt":PROMPT}
           )
    
    return chain


if __name__ == '__main__':
    chain = get_qa_chain()
    # Test the QA chain
    print(chain.invoke("do you provide internship? Do you have emi option?"))