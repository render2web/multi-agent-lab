import os # Agregado por pura formalidad profesional
from typing import TypedDict
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph

# --- CÓDIGO INICIAL (EL PROBLEMA) ---


load_dotenv()

# 1. Definimos la Pizarra (Estado)
class AgentState(TypedDict):
    code: str
    feedback: str
    iterations: int
    solved: bool

# 3. Nodo del Programador (Claude 4.6 Sonnet) AGENTE A
def programmer_node(state: AgentState):
    print(f"\n🚀 [Programador - Claude] Generando solución (Intento {state['iterations'] + 1})...")
    
    llm = ChatAnthropic(model="claude-sonnet-4-6")
    
    prompt = f"""Tu misión es arreglar el siguiente código que tiene bugs:
    {state['code']}
    
    Feedback del crítico: {state['feedback']}
    
    Devuelve ÚNICAMENTE el código corregido dentro de bloques de código python."""
    
    response = llm.invoke(prompt)
    return {
        "code": response.content, 
        "iterations": state['iterations'] + 1
    }

# 4. Nodo del Crítico (OpenAI GPT-4o) AGENTE B
def critic_node(state: AgentState):
    print("🧐 [Crítico - OpenAI] Analizando el código minuciosamente...")
    
    llm = ChatOpenAI(model="gpt-4o") 
    
    prompt = f"""Actúa como un Senior QA Engineer. Revisa este código:
    {state['code']}
    
    Si el código es 100% correcto, eficiente y maneja errores, responde con la palabra: 'SOLVED'.
    Si tiene fallos (falta de validación, errores de tipo, etc.), explica qué debe mejorar."""
    
    response = llm.invoke(prompt)
    is_solved = "SOLVED" in response.content.upper()
    
    return {
        "feedback": response.content,
        "solved": is_solved
    }

# 5. Lógica de Control
def router(state: AgentState):
    if state["solved"] or state["iterations"] >= 3:
        return "end"
    return "continue"

# 6. Construcción del Grafo
workflow = StateGraph(AgentState)
workflow.add_node("programmer", programmer_node)
workflow.add_node("critic", critic_node)

workflow.set_entry_point("programmer")
workflow.add_edge("programmer", "critic")

workflow.add_conditional_edges(
    "critic",
    router,
    {"continue": "programmer", "end": END}
)

app = workflow.compile()

# 7. Ejecución (Aquí está el código con errores para el tutorial)
if __name__ == "__main__":
    # Este es el código "sucio" que verán tus alumnos al inicio
    initial_code = """
def process_data(data):
    # Bug 1: No verifica si 'data' es None (Lanzará TypeError)
    # Bug 2: No verifica si la llave 'price' existe (Lanzará KeyError)
    # Bug 3: No verifica si el precio es un número (Lanzará TypeError)
    return [d['price'] * 1.15 for d in data]
    """

    inputs = {
        "code": initial_code,
        "feedback": "Inicio del duelo",
        "iterations": 0,
        "solved": False
    }

    print("--- 🥊 INICIANDO DUELO DE TITANES ---")
    final_state = app.invoke(inputs)
    
    print("\n✅ RESULTADO FINAL TRAS EL DUELO:")
    print(final_state["code"])