from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from ..prompts import feedback_system_prompt

# Generation prompt
feedback_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            feedback_system_prompt
        ),
        # messages History holder to keep all the reflections and revised tweets. It allows the model to incorporate
        # previous messages into the response generation, ensuring continuity and relevance in the conversation.
        MessagesPlaceholder(variable_name="messages")
    ]
)


# Create chain
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
# here we use langchain simple language to import generation_prompt and reflection_prompt to llm as generated_chain and reflection_chain respectively
feedback_chain = feedback_prompt | llm