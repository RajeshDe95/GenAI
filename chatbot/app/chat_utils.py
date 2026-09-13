from euriai.langchain import create_chat_model

API_KEY = None
MODEL = "gpt-4.1-nano"  
TEMPERATURE = 0.7

def get_chat_model(model_name: str = MODEL, api_key: str = None, temperature: float = TEMPERATURE):
    return create_chat_model(
        api_key=api_key or API_KEY,
        model=model_name,
        temperature=temperature
    )

def ask_chat_model(chat_model, prompt: str):
    response = chat_model.invoke(prompt)
    return response.content


    

