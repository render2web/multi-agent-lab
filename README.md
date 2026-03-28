# 🤖 Multi-Agent Lab

Un laboratorio experimental que implementa un sistema **multi-agente inteligente** utilizando **LangGraph** para resolver y corregir código automáticamente mediante retroalimentación entre agentes de IA.

## 📋 Descripción

Este proyecto demuestra un flujo de trabajo colaborativo entre dos agentes especializados:

1. **🚀 Agente Programador** (Claude Sonnet 4.6): Genera y corrige código Python
2. **🧐 Agente Crítico** (GPT-4o): Revisa la calidad del código como QA Engineer

El sistema implementa un **loop de retroalimentación automático** donde:
- El Programador recibe feedback del Crítico
- Itera sobre el código para mejorar su calidad
- El proceso se detiene cuando el código es perfecto o se alcanza el máximo de intentos

## 🎯 Características

- ✨ Arquitectura **multi-agente** con LangGraph
- 🔄 Loop automático de revisión y mejora de código
- 🛡️ Integración con múltiples LLMs (Claude + GPT-4o)
- 🐍 Demostración con código Python real
- 📊 Seguimiento de iteraciones y estado

## 🚀 Instalación

### Requisitos
- Python 3.10+
- APIs configuradas (Anthropic, OpenAI)

### Pasos

1. **Clonar el repositorio**
```bash
git clone https://github.com/render2web/multi-agent-lab.git
cd multi-agent-lab
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requeriments.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
```

Edita `.env` y agrega tus API keys:
```env
ANTHROPIC_API_KEY=tu_key_aqui
OPENAI_API_KEY=tu_key_aqui
```

## 💻 Uso

Ejecuta el laboratorio:

```bash
python main.py
```

### Salida esperada

```
--- 🥊 INICIANDO DUELO DE TITANES ---

🚀 [Programador - Claude] Generando solución (Intento 1)...
🧐 [Crítico - OpenAI] Analizando el código minuciosamente...

✅ RESULTADO FINAL TRAS EL DUELO:
[Código corregido y optimizado]
```

## 🔧 Cómo Funciona

### Arquitectura del Flujo

```
Entrada (Código Buggy)
    ↓
Nodo Programador (Claude Sonnet)
    ↓
Nodo Crítico (GPT-4o)
    ↓
¿Código Solucionado?
├─ SÍ → FIN ✅
└─ NO → Volver a Programador (Máx 3 intentos)
```

### Ejemplo de Bug Detectado

El código inicial tiene 3 bugs:
```python
def process_data(data):
    # Bug 1: No verifica si 'data' es None
    # Bug 2: No verifica si la llave 'price' existe
    # Bug 3: No verifica si el precio es un número
    return [d['price'] * 1.15 for d in data]
```

El sistema itera hasta generar código robusto:
```python
def process_data(data):
    if data is None:
        raise ValueError("data no puede ser None")

    result = []
    for d in data:
        if not isinstance(d, dict):
            raise TypeError(f"Se esperaba dict, se recibió {type(d)}")
        if 'price' not in d:
            raise KeyError("Falta la clave 'price'")
        if not isinstance(d['price'], (int, float)):
            raise TypeError("'price' debe ser un número")

        result.append(d['price'] * 1.15)

    return result
```

## 📦 Dependencias

- `langgraph` - Orquestación de flujos multi-agente
- `langchain-anthropic` - Cliente de Anthropic para Claude
- `langchain-openai` - Cliente de OpenAI para GPT-4o
- `python-dotenv` - Gestión de variables de entorno

## 🔒 Seguridad

Las API keys se almacenan en `.env` que está excluido de git mediante `.gitignore`. **Nunca commits tus secretos**.

## 📚 Casos de Uso

- 🎓 Educación en sistemas multi-agente
- 🧪 Testing y validación de código automática
- 🔍 Code review asistido por IA
- 🚀 Prototipado rápido de soluciones
- 📈 Mejora iterativa de calidad de código

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT.

## 👨‍💻 Autor

**render2web** - Creador del laboratorio multi-agente

## 🙏 Agradecimientos

- Anthropic por Claude Sonnet 4.6
- OpenAI por GPT-4o
- LangChain por las herramientas de integración

---

**⭐ Si este proyecto te fue útil, considera dejar una estrella en GitHub**
