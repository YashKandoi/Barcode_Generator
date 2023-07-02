#pip install openai
#create key.txt and paste your secret api key in it
import openai

def getReply(promptText):
    openai.api_key = open("key.txt","r").read().strip("\n")
    completion =openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        messages = [{"role":"user","content":promptText}]
    )
    reply_content = completion.choices[0].message.content
    return reply_content
