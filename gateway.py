import os
import openai

TOKEN = os.getenv("TOKEN")


def casos(data):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")

    text_example = read_text_example()
    prompt = "Con las siguientes palabras clave, genere un caso de ética."+text_example+data

    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=1,
            max_tokens=659,
            top_p=1,
            frequency_penalty=0.8,
            presence_penalty=0.8,
            stop=["###"])

        return dict(response["choices"][0])["text"].replace("\n\n", "") , 200
    except Exception as err:
        return {"Error": err}, 500


def read_text_example():
    f = open('texto.txt', 'r')
    content = f.read()
    print(content)
    return content
