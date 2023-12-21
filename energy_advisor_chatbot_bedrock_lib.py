import json
import boto3
import langchain

from typing import List
from json import JSONDecodeError

from langchain.memory import ConversationSummaryBufferMemory
from langchain.llms.bedrock import Bedrock
from langchain.llms.bedrock import LLMInputOutputAdapter
from langchain.chains import ConversationChain
from langchain.schema import get_buffer_string


#OPTIONS: (subject to change)
#"amazon.titan-tg1-large"
#"amazon.titan-e1t-medium"
#"stability.stable-diffusion-xl"
#"ai21.j2-grande-instruct"
#"ai21.j2-jumbo-instruct" #fixme when it becomes Ultra
#"anthropic.claude-instant-v1"
#"anthropic.claude-v1"
bedrock_model_id = "anthropic.claude-v1"

llm = Bedrock(credentials_profile_name="bedrock-user", model_id=bedrock_model_id)

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=50)

conversation_with_summary = ConversationChain(
    llm = llm, 
    memory = memory,
    verbose = True
)

def get_chat_response(input_text):
    
    chat_response = conversation_with_summary.predict(input=input_text)
    
    return chat_response


def get_chat_response_with_introspection(input_text):
    
    prompt_text = conversation_with_summary.prompt.format(input = input_text, history = conversation_with_summary.memory.load_memory_variables({})['history'])
    
    new_lines = get_buffer_string(memory.chat_memory.messages, human_prefix = memory.human_prefix, ai_prefix = memory.ai_prefix)

    prompt_summary_text = memory.prompt.format(summary = memory.moving_summary_buffer, new_lines = new_lines)

    chat_response = conversation_with_summary.predict(input=input_text)
    
    return chat_response, prompt_text, prompt_summary_text
