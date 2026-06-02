from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Constants
gemini_model = "gemini-3.1-flash-lite"


def get_llm_chain(system_text):
    promptTemplate: ChatPromptTemplate = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_text,
            ),
            ("user", "{query}"),
        ]
    )
    llm = ChatGoogleGenerativeAI(model=gemini_model)
    OutputParser = StrOutputParser()
    chain = promptTemplate | llm | OutputParser
    return chain


if __name__ == "__main__":
    load_dotenv()
    chain = get_llm_chain("Answer in less than 200 chars")
    response = chain.invoke({"query": "Can you tell me something about langsmith"})
    print(response)
