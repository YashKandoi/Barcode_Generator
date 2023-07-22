# pip install openai
# create key.txt and paste your secret api key in it
import openai

def getReply(promptText):
    openai.api_key = open("openai_key.txt","r").read().strip("\n")
    completion =openai.ChatCompletion.create(
        model ="gpt-3.5-turbo-16k",
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
            model ="gpt-3.5-turbo-16k",
            messages = message_history
        )
        temp = completion.choices[-1].message.content
        message_history.append({"role":"assistant","content":temp})
        reply_content.append(temp)
    return reply_content

def getChatHistory(message_list,message_history):
    openai.api_key = open("key.txt","r").read().strip("\n")
    for message in message_list:
        message_history.append({"role":"user","content":message})
        completion =openai.ChatCompletion.create(
            model ="gpt-3.5-turbo-16k",
            messages = message_history
        )
        temp = completion.choices[-1].message.content
        message_history.append({"role":"assistant","content":temp})
    return message_history

def extractReplies(message_history):
    reply_content=[]
    for message in message_history:
        if message["role"] == "assistant":
            reply_content.append(message["content"])
    return reply_content

def extractPrompts(message_history):
    reply_content=[]
    for message in message_history:
        if message["role"] == "user":
            reply_content.append(message["content"])
    return reply_content

def extractCode(reply):
    delimiter = "```"
    start = reply.index(delimiter) + len(delimiter)
    end = reply.rindex(delimiter)
    return(reply[start:end])

def createCSV(reply):
    if reply.find("```") != -1:
        reply = extractCode(reply)
    file_path = "temp.csv"
    with open(file_path, 'w') as file:
        file.write(reply)
