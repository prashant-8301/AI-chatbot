from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
conv=[{"role":"system","content":"You are a helpful assistant."}]
while(msg:=input("You :").strip())not in["EXIT","quit"]:
    conv.append({"role":"user","content":msg})
    reply=client.chat.completions.create(model="gpt-4o-mini",messages=conv).choices[0].message.content
    conv.append({"role":"assistant","content":reply})
    print("Bot :",reply)