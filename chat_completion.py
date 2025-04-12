import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
load_dotenv()
client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://debdu-m9cerqxd-swedencentral.openai.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

completion = client.chat.completions.create(  
    model="gpt-4o-mini",  
    messages=[
        {"role":"user",
         "content":"What's the age of Pyramids of Egypt"}
    ],
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False  
) 

print(completion.to_json())