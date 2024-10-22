# import requests

# async def response(req):
#     url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"

#     payload = {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": req
#             }
#         ],
#         "model": "gpt-4-turbo-preview",
#         "max_tokens": 200,
#         "temperature": 0.9
#     }
#     headers = {
#         "content-type": "application/json",
#         "X-RapidAPI-Key": "81fb8ab861mshab3f38210b29688p1d13bfjsn2a09fbd6b61c",
#         "X-RapidAPI-Host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com"
#     }

#     response = requests.post(url, json=payload, headers=headers)


#     data = response.json()
#     return data['choices'][0]['message']['content']