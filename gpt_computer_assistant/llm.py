from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
try:
    from .utils.db import load_api_key, load_model_settings
except ImportError:
    from utils.db import load_api_key
from langchain_groq import ChatGroq

<<<<<<< HEAD
try:
    from .utils.db import load_api_key, load_openai_url, load_model_settings, load_groq_api_key
except ImportError:
    from utils.db import load_api_key, load_openai_url, load_model_settings, load_groq_api_key
=======
>>>>>>> ed41b4a6b883f546b17fdf66e67deb45df15f690

try:
    from .utils.db import load_api_key, load_openai_url, load_model_settings, load_groq_api_key
except ImportError:
    from utils.db import load_api_key, load_openai_url, load_model_settings, load_groq_api_key

def get_model():
    the_model = load_model_settings()
<<<<<<< HEAD
    if the_model == "gpt-4o":
        the_api_key = load_api_key()
        the_openai_url = load_openai_url()
        return ChatOpenAI(model="gpt-4o", api_key=the_api_key, base_url=the_openai_url)
    elif the_model == "llava":
        return ChatOllama(model="llava")
    elif the_model == "bakllava":
        return ChatOllama(model="bakllava")
    elif the_model == "mixtral-8x7b-groq":
        the_api_key = load_groq_api_key()
        return ChatGroq(
            temperature=0, model_name="mixtral-8x7b-32768", groq_api_key=the_api_key
        )
=======
    the_api_key = load_api_key()
    the_openai_url = load_openai_url()
    
    def open_ai_base():
        if the_openai_url == "default":
            return {"model": the_model, "api_key": the_api_key, "max_retries":15}
        else:
            return {"model": the_model, "api_key": the_api_key, "max_retries":15, "base_url": the_openai_url}
    
    args_mapping = {
        ChatOpenAI: open_ai_base(),
        ChatOllama: {"model": the_model},
        ChatGroq: {"temperature": 0, "model_name": the_model.replace("-groq", ""), "groq_api_key": load_groq_api_key()}
    }
    
    model_mapping = {
        "gpt-4o": (ChatOpenAI, args_mapping[ChatOpenAI]),
        "gpt-3.5-turbo": (ChatOpenAI, args_mapping[ChatOpenAI]),
        "llava": (ChatOllama, args_mapping[ChatOllama]),
        "bakllava": (ChatOllama, args_mapping[ChatOllama]),
        "mixtral-8x7b-groq": (ChatGroq, args_mapping[ChatGroq])
    }
    
    model_class, args = model_mapping[the_model]
    return model_class(**args) if model_class else None
>>>>>>> ed41b4a6b883f546b17fdf66e67deb45df15f690


def get_client():
    the_api_key = load_api_key()
    the_openai_url = load_openai_url()
<<<<<<< HEAD
    return OpenAI(api_key=the_api_key, base_url=the_openai_url)
=======
    if the_openai_url == "default":
        return OpenAI(api_key=the_api_key)
    else:
        return OpenAI(api_key=the_api_key, base_url=the_openai_url)
>>>>>>> ed41b4a6b883f546b17fdf66e67deb45df15f690
