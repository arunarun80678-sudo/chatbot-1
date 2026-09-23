import os
BOT_CONFIG={
"title":'KnowledgeGraph AI',"domain":'Connect concepts and create knowledge maps',
"system_prompt":'Answer only questions directly related to Connect concepts and create knowledge maps. Politely reject unrelated questions.',
"behavior":'Act as a specialized KnowledgeGraph AI assistant and provide practical, structured guidance about Connect concepts and create knowledge maps.',
"welcome_message":'Welcome to KnowledgeGraph AI. I can help with Connect concepts and create knowledge maps.',
"welcome_title":'Your Knowledge Graph workspace',
"theme_name":'Knowledge Graph',"primary_color":'#8b3fc7',"surface_color":'#f7edff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
