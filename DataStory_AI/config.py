import os
BOT_CONFIG={
"title":'DataStory AI',"domain":'Turn datasets into understandable insights',
"system_prompt":'Answer only questions directly related to Turn datasets into understandable insights. Politely reject unrelated questions.',
"behavior":'Act as a specialized DataStory AI assistant and provide practical, structured guidance about Turn datasets into understandable insights.',
"welcome_message":'Welcome to DataStory AI. I can help with Turn datasets into understandable insights.',
"welcome_title":'Your Data Story workspace',
"theme_name":'Data Story',"primary_color":'#27833b',"surface_color":'#edf9ef',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
