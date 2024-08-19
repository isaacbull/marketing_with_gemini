# coding: utf-8
import os
import google.generativeai as genai
import PIL.Image 
from IPython.display import display, Image
import ipywidgets as widgets
pip3 install PIL
get_ipython().system('pip3 install pillow')
import google.generativeai as genai
import PIL.Image 
from IPython.display import display, Image
import ipywidgets as widgets
get_ipython().system('pip3 install ipywidgets')
import google.generativeai as genai
import PIL.Image 
from IPython.display import display, Image
import ipywidgets as widgets
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel("gemini-1.5-flash")
productsketchUrl = 'https://storage.googleapis.com/generativeai-downloads/images/jetpack.jpg'
get_ipython().system('curl -o jetpack.jpg {productsketchUrl}')
img = PIL.Image.open('jetpack.jpg')
display(Image('jetpack.jpg', width=50))
analyzePrompt = """This image contains a sketch of a potential product along with some notes.
Given the product sketch, describe the product as thoroughly as possible based on what you see
in the image, making sure to note all of the product features. Return output in json format:
{description: description, features: [feature1, feature2, feature3]}"""
print(analyzePrompt[0:10])
response = model.generate_content([analyzePrompt, img])
print(img)
print(analyzePrompt)
type(img)
converted_img = Image.fromarray(img)
img = PIL.Image.open('jetpack.jpg')
type(img)
response = model.generate_content([analyzePrompt, img])
from IPython.display import Image
img2 = Image('jetpack.jpg')
from IPython.display import Image2
type(img2)
from IPython.core.display import HTML
response = model.generate_content([analyzePrompt, img2])
productInfo = eval(response.text)
print(productInfo)
namePrompt = """You are a marketing whiz and writer trying to come up with a name for the product shown in the image. come up with ten varied, interesting possible names. Return the result in array format, like this: ['name 1', 'name 2', ...]. Pay careful attention to return a valid array in the format described above, and no other text. the most important thing is that you stick to the array format."""
response = model.generate_content([namePrompt, img2])
names = eval(response.text)
dropdown = widgets.Dropdown(options=names, value=names[0],
description = 'Name:', disabled=False)
websiteCopyPrompt = """You're a marketing whiz and expert copywriter. You're writing
website copy for a product named {productName}. Your first job is to come up with H1
H2 copy. These are brief, pithy sentences or phrases that are the first and second
things the customer sees when they land on the splash page. Here are some examples:
{{
  "h1": "A feeling is canned",
  "h2": "drinks and powders to help you feel calm cool and collected\
   despite the stressful world around you"
}}
{{
  "h1": "Design. Publish. Done.",
  "h2": "Stop rebuilding your designs from scratch. In Framer, everything\
   you put on the canvas is ready to be published to the web."
}}

Create the same json output for a product named "{productName}" with description\
 "{description}".
Output ten different options as json in an array. Don't add extra chars like ```
""".format(productName=name, description=productInfo['description'])
name  = dropdown.value
response = model.generate_content([namePrompt, img2])
names = eval(response.text)
dropdown = widgets.Dropdown(options=names, value=names[0],
description = 'Name:', disabled=False)
name  = dropdown.value
websiteCopyPrompt = """You're a marketing whiz and expert copywriter. You're writing
website copy for a product named {productName}. Your first job is to come up with H1
H2 copy. These are brief, pithy sentences or phrases that are the first and second
things the customer sees when they land on the splash page. Here are some examples:
{{
  "h1": "A feeling is canned",
  "h2": "drinks and powders to help you feel calm cool and collected\
   despite the stressful world around you"
}}
{{
  "h1": "Design. Publish. Done.",
  "h2": "Stop rebuilding your designs from scratch. In Framer, everything\
   you put on the canvas is ready to be published to the web."
}}

Create the same json output for a product named "{productName}" with description\
 "{description}".
Output ten different options as json in an array. Don't add extra chars like ```
""".format(productName=name, description=productInfo['description'])
websiteCopyPrompt[0;20]
websiteCopyPrompt[0:20]
websiteCopyPrompt
copyResponse = model.generate_content([websiteCopyPrompt, img2])
copy = eval(copyResponse.text)
copy = eval(copyResponse.text)
name
namePrompt
websiteCopyPrompt = """You're a marketing whiz and expert copywriter. You're writing
website copy for a product named {productName}. Your first job is to come up with H1
H2 copy. These are brief, pithy sentences or phrases that are the first and second
things the customer sees when they land on the splash page. Here are some examples:
{{
  "h1": "A feeling is canned",
  "h2": "drinks and powders to help you feel calm cool and collected\
   despite the stressful world around you"
}}
{{
  "h1": "Design. Publish. Done.",
  "h2": "Stop rebuilding your designs from scratch. In Framer, everything\
   you put on the canvas is ready to be published to the web."
}}

Create the same json output for a product named "{productName}" with description\
 "{description}".
Output ten different options as json in an array. Don't add extra chars like ```
""".format(productName=name, description=productInfo['description'])
copyResponse = model.generate_content([websiteCopyPrompt, img2])
copy = eval(copyResponse.text)
copy
h1 = "Reach new heights"
h2 = "With Nimbus, the sky's the limit. Explore new heights and see the world from a whole new perspective."
htmlPrompt = """Generate HTML and CSS for a splash page for a new product called {productName}.
Output only HTML and CSS and do not link to any external resources.
Include the top level title: "{h1}" with the subtitle: "{h2}".
""".format(productName=name, h1=h1, h2=h2)
response = model.generate_content([htmlPrompt])t
response = model.generate_content([htmlPrompt])
print(response.text)
