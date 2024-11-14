import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

with open("tresc.txt", "r", encoding="utf-8") as file:
    promptText=file.read()

promptDescription="Generate an HTML snippet based on the text description {content}. \
    The HTML should exclude the <html>, <head>, and <body> tags and only contain the code that would go inside the <body> tag.\
    Format the HTML to be readable and engaging, using a variety of tags, such as <h1>, <h2>, <p>, <strong>, <em>, <ul>, <li>, <blockquote>, <figure>, <img>, and <figcaption>, \
    to enhance structure and visual interest. Based on {content}, create <img> tags where images would add context. For each <img> tag, use src=\"image_placeholder.jpg\"\
    and set the alt attribute to a relevant, descriptive prompt that can help generate the image. Place an appropriate <figcaption> beneath each image to provide further explanation.\
    The final HTML should be well-organized into sections, using elements such as <section> and <aside> where appropriate to improve readability and emphasize key points or supplementary information.\
    {content}"

full_prompt = f"{promptDescription}\n\n{promptText}"

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[

        {
        "role": "user",
        "content": full_prompt
        }],
    temperature=0.7

)
f = open("artykul.html", "w")
f.write(chat_completion.choices[0].message.content)
