import torch
import accelerate
import langchain
import langchain_community
import os

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


# explicitly specify the model
model_name ="google/flan-t5-large"

# create the hugging face pipeline
hf_pipeline = pipeline("text2text-generation", model=model_name)

print("Model loaded. Creating chain...", flush=True)

#Wrap the pipeline inside LangChain's HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=hf_pipeline)

print("Generating first answer...", flush=True)

template = """Question: {question} Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = prompt | llm


question = "Explain the concept of black holes in simple terms."

result = llm_chain.invoke({"question":question})
print("\nAnswer:", result, flush=True)

question = "What are the main causes of climate change, and how can we avoid that"

result= llm_chain.invoke({"question":question})
print("\nAnswer:", result, flush=True)
