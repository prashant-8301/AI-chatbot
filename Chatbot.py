# from openai import OpenAI
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_KEY"))


conv = [{"role":"System","content":"You are a helpful assistant."}]

while(msg := input("You :").strip()) not in ["Exit", "exit","quit"]:
	conv.append({"role":"user","content":msg})
	# reply = client.chat.completions.create(model="gpt-4o-mini",messages=conv).choice[0].message.content
	reply = client.chat_completion(model="Qwen/Qwen2.5-7B-Instruct",messages=conv,max_tokens=500)
	bot_reply = reply.choices[0].message.content
	conv.append({"role":"assistant","content":reply})
	print("Bot :",bot_reply)










# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv(override=True)
# client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# conv=[{"role":"system","content":"You are a helpful assistant."}]
# while(msg:=input("You :").strip())not in["EXIT","quit"]:
#     conv.append({"role":"user","content":msg})
#     reply=client.chat.completions.create(model="gpt-4o-mini",messages=conv).choices[0].message.content
#     conv.append({"role":"assistant","content":reply})
#     print("Bot :",reply)