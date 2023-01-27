import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")


# Funcion para generar una respuesta a partir de un prompt
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Leer los criterios del archivo externo
def read_criterios():
    with open("criterios.txt", "r") as f:
        criterios = f.read()
        f.close()
    return criterios

# Titulo de la aplicacion
st.title("App de Resolucion de Casos de Etica")

# Leer los criterios
criterios = read_criterios()

# Pedir al usuario que ingrese el caso a resolver
case_study = st.text_area("Ingrese el caso a resolver:")

# Generar la respuesta
if st.button("Resolver caso"):
    prompt = criterios + case_study
    response = generate_response(prompt)
    st.success("La respuesta es: \n" + response)
