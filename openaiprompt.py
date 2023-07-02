# pip install openai
# create key.txt and paste your secret api key in it
import openai

def getReply(promptText):
    openai.api_key = open("key.txt","r").read().strip("\n")
    completion =openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        messages = [{"role":"user","content":promptText}]
    )
    reply_content = completion.choices[0].message.content
    return reply_content

def getReplies(message_list):
    openai.api_key = open("key.txt","r").read().strip("\n")
    message_history=[]
    reply_content = []
    for message in message_list:
        message_history.append({"role":"user","content":message})
        completion =openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages = message_history
        )
        temp = completion.choices[-1].message.content
        message_history.append({"role":"assistant","content":temp})
        reply_content.append(temp)
    return reply_content
