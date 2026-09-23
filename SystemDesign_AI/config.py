import os
BOT_CONFIG={
"title":'SystemDesign AI',"domain":'Software architecture and system-design guidance',
"system_prompt":'Answer only questions directly related to Software architecture and system-design guidance. Politely reject unrelated questions.',
"behavior":'Act as a specialized SystemDesign AI assistant and provide practical, structured guidance about Software architecture and system-design guidance.',
"welcome_message":'Welcome to SystemDesign AI. I can help with Software architecture and system-design guidance.',
"welcome_title":'Your Architecture Board workspace',
"theme_name":'Architecture Board',"primary_color":'#4f46b5',"surface_color":'#eef0ff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
