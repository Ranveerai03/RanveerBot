import os
import sys

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import constants

# os.environ["OPENAI_API_KEY"] = constants.APIKEY

# llm = ChatOpenAI()

llm = ChatOpenAI(openai_api_key="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")

llm.invoke("how can langsmith help with testing?")
