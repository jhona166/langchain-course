
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

# Cargar variables de entorno
load_dotenv(Path(__file__).resolve().parent / ".env")


def main():
    print("Hello from langchain-course!")

    information = (
        "Elon Reeve Musk nació en Pretoria, Sudáfrica, el 28 de junio de 1971. "
        "Es un empresario e inversor conocido por su participación en empresas "
        "tecnológicas como SpaceX, Tesla, Neuralink y The Boring Company. "
        "También fue uno de los cofundadores de OpenAI."
    )

    # Crear plantilla
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template="Resume la siguiente información en español: {information}",
    )

    # Inicializar modelo
    llm = ChatOllama(temperature=0, model="gpt-oss:20b")
    chain = summary_prompt_template | llm

    print("Generando resumen...")

    # Ejecutar modelo
    response = chain.invoke({"information": information})

    # Mostrar resultado
    print("\nResumen generado:\n")
    print(response.content)


if __name__ == "__main__":
    main()
