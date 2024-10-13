import dotenv

dotenv.load_dotenv()

import requests
import os

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": os.getenv("VIDEO_API_KEY")
}

def generate_video(text_prompt, img_prompt):

    url = "https://api.aivideoapi.com/runway/generate/imageDescription"



    body = {
    "text_prompt": text_prompt,
    "img_prompt": img_prompt,
    "model": "gen3",
    "image_as_end_frame": False,
    "flip": False,
    "motion": 5,
    "seed": 0,
    "callback_url": "",
    "time": 5
    }

    response = requests.post(url, headers=headers, json=body)
    video_id = response.json()["uuid"]

    return video_id


def get_video_status(video_id):

    url = f"https://api.aivideoapi.com/status?uuid={video_id}"

    response = requests.get(url, headers=headers)

    return response.text

# video = generate_video("The X.AI Hackathon kicks off today! With the APEC Summit bringing leaders together in San Francisco, let's unite our minds to build AI solutions that promote global collaboration and economic prosperity. Join us and contribute to shaping a better future!", "https://oaidalleapiprodscus.blob.core.windows.net/private/org-Gv6Ady6ptNRyNGOhjoCgP8DK/user-zNylzYFZuaVnYgPVtXSrdG6w/img-VBQqDn38s8nKyWbgO4a8Trl4.png?st=2024-10-13T00%3A28%3A24Z&se=2024-10-13T02%3A28%3A24Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-10-12T23%3A39%3A12Z&ske=2024-10-13T23%3A39%3A12Z&sks=b&skv=2024-08-04&sig=A6fvMuBQ%2BG5Huf4u/yU8at8/Drq7BhTgN7JSdXdqEFY%3D")
# print(video)

status = get_video_status("18241fc9-b1b5-48f8-9076-bdd178cd3d1c")
print(status)