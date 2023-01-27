import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Funcion para leer los criterios
def read_criterios():
    with open("criterios.txt", "r") as f:
        criterios = f.read()
    return criterios

# Funcion para generar la respuesta
def generate_response(prompt):
    
    
    # Generar la respuesta
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def main():
    # Titulo de la aplicacion
    st.title("App de Resolucion de Casos de Etica")
    
    # Pedir al usuario que ingrese el caso a resolver
    case_study = st.text_area("Ingrese el caso a resolver:")

    # Generar la respuesta
    if st.button("Resolver caso"):
        # Leer los criterios
        criterios = read_criterios()
        prompt = criterios + case_study
        response = generate_response(prompt)
        st.success("La respuesta es: \n" + response)

if __name__ == '__main__':
    main()
