import os
BOT_CONFIG={
"title":'PromptLab AI',"domain":'Create, test and improve AI prompts',
"system_prompt":'Answer only questions directly related to Create, test and improve AI prompts. Politely reject unrelated questions.',
"behavior":'Act as a specialized PromptLab AI assistant and provide practical, structured guidance about Create, test and improve AI prompts.',
"welcome_message":'Welcome to PromptLab AI. I can help with Create, test and improve AI prompts.',
"welcome_title":'Your Prompt Laboratory workspace',
"theme_name":'Prompt Laboratory',"primary_color":'#b22a85',"surface_color":'#fff0fa',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
