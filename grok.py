import dotenv

dotenv.load_dotenv()

import os

from openai import OpenAI

import json


client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

def get_completion(prompt: str, system_prompt:str) -> str:
    completion = client.chat.completions.create(
        model="grok-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )

    return completion.choices[0].message


# completion = client.chat.completions.create(
#     model="grok-preview",
#     messages=[
#         {"role": "system", "content": "You are Grok, you help people get information about the trends and posts on social media"},
#         {"role": "user", "content": "What are the topics people are talking about in SF as of Oct 12?"},
#     ],
# )

def get_ad_copy(product, city):
    response = get_completion(
        prompt=f"""

        Today is October 12th, 2024
        
        Instructions:
        1. Get today's headlines in {city} to understand what people are talking about.
        2. Use these headlines information to generate 3 variations of ad copies for a {product}. Each variatin should be unique and tailored to a different topic. Do not include hashtags.
        3. Review the ad copies and make any necessary changes to ensure it is relevant to one of the topics people are talking about in San Francisco as of Oct 12 2024. Be specific about the topic you choose. 
        
        Output ad copy in the following json format:
        [{{
            "ad_copy": "The X.AI hackathon is happening in San Francisco on Oct 12. Come build the future with us to support free and open AI for everyone.",
            "trend": "free and openAI",
            "explanation": "The ad copy is relevant to the topic of free and openAI that people are talking about in San Francisco as of Oct 12",
        }},
        {{
            "ad_copy": "Experience the power of the iPhone 16 - it's like having Fleet Week in your pocket. Capture stunning aerial photos and videos with unparalleled clarity, just like the Blue Angels soaring above San Francisco.",
            "trend": "Fleet Week",
            "explanation": "The ad copy is relevant to the topic of Fleet Week, where aerial displays by the Blue Angels are a highlight, linking this event to the iPhone's superior camera capabilities.",
        }},
        {{
            "ad_copy": "Tune in to the sounds of innovation with AirPods 4. While the San Francisco Tech Week highlights the latest in tech, AirPods 4 provides an unparalleled audio experience for those immersed in the city's tech scene..",
            "trend": "San Francisco Tech Week",
            "explanation": "This ad copy aligns with San Francisco Tech Week, focusing on how AirPods 4 can enhance the experience of tech events with its superior sound technology",
        }}]

        Just output the json.

        Example of a single ad copy with a headline:
        Headline: Cultural Events: The Blue Angels performed over San Francisco Bay as part of Fleet Week, attracting attention and providing a contrast to the city's daily challenges with a display of aerial prowess.
        Ad Copy: "Join us for the X.AI Hackathon today! While the Blue Angels dazzle us with aerial feats over the San Francisco Bay for Fleet Week, we're diving into a different kind of innovation. Here at X.AI, we're exploring the frontiers of artificial intelligence. Let's soar to new heights together in tech as the Blue Angels do in the skies!"
        """,
        system_prompt="You are AI social ads assistant; You help people to generate ad copies for their products and events, by tailoring them to the trends",
    )

    json_response = response.content.strip("```json").strip("```")

    print(json_response)
    
    return json.loads(json_response)



