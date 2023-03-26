import openai

openai.api_key = ""

response = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
     messages=[{"role":"system","content":""}]

)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

imageResponse = openai.Image.create(
    prompt="",
    n=1,
    size="256x256"
)

print(imageResponse)
