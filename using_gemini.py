# coding: utf-8
import os
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
import google.generativeai as genai
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel("gemini-1.0-pro-latest")
response = model.generate_content("the opposite of hot is?")
print(response.text)
response = model.generate_content("write a python class")
print(response.text)
response.text.length()
response = model.generate_content("tell me about the os module in python")
print(response.text)
response = model.generate_content("tell me about the os module get environ method")
print(response.text)
get_ipython().run_line_magic('notebook', '-e using_gemini.ipynb')
get_ipython().run_line_magic('notebook', 'using_gemini.ipynb')
