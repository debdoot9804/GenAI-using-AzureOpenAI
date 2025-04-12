apikey="9VTU6gpLfKTSHVwUmxqxaCbjowk5aTbRQe0ibXpozymUeSOHp424JQQJ99BDACfhMk5XJ3w3AAAAACOGdgZk"


# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
load_dotenv()
client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://debdu-m9cerqxd-swedencentral.cognitiveservices.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

result = client.images.generate(
    model="dall-e-3", # the name of your DALL-E 3 deployment
    prompt="create an image of  a cartoon fish",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)
