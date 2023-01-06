from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nhhego:"
restart_sequence = "\n\nPerson:"
session_prompt = "Hi, welcome to Hhegobuddy! I'm here to assist you with any questions or concerns you may have. Whether you need help with a specific problem or just want to have a friendly chat, I'm here to help. So, what can I do for you today?"

def ask(question, chat_log=None):
      prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}"
      response = openai.Completion.create(
      model="text-davinci-003",
      prompt="prompt_text",
      temperature=0.7,
      max_tokens=439,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
      )

      story = response['choices'][0]['text']
      return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
      if chat_log is None:
            chat_log = session_prompt
      return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
    