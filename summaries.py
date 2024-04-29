from langchain_cohere import ChatCohere
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from config import COHERE_API_KEY

def summarize_article(text):
    cohere = ChatCohere(cohere_api_key=COHERE_API_KEY)
    template = """
        You are a news reporter who summarizes the main article of the HTML page given to you for personalized news digest.
        
        Use the information from the article and reflect the perspective of the writer of the article.

        Summary must be one paragraph.

        Give only summarized article. Don't add any sentence to output.
        """
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "Summarize the main article from following HTML page: {text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    chain = LLMChain(llm=cohere, prompt=chat_prompt)
    return chain.run(text=text)