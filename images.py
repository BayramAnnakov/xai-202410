import dotenv

dotenv.load_dotenv()

import os

from openai import OpenAI


client = OpenAI()

def generate_image_openai(prompt, image_size='1024x1024'):


    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url

    print(image_url)

    return image_url

# prompt = "Unleash your coding skills at the X.AI Hackathon in San Francisco! With the city buzzing about the upcoming 2024 General Election, we're here to shape the future of AI governance. Come and help us build ethical, transparent AI systems that empower voters and ensure fair elections."
# image = generate_image(prompt)
# print(image)
