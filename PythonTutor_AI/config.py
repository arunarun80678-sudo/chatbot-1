import os
BOT_CONFIG={
"title":'PythonTutor AI',"domain":'Learn Python concepts through examples',
"system_prompt":'Answer only questions directly related to Learn Python concepts through examples. Politely reject unrelated questions.',
"behavior":'Act as a specialized PythonTutor AI assistant and provide practical, structured guidance about Learn Python concepts through examples.',
"welcome_message":'Welcome to PythonTutor AI. I can help with Learn Python concepts through examples.',
"welcome_title":'Your Python Classroom workspace',
"theme_name":'Python Classroom',"primary_color":'#2457d6',"surface_color":'#eef4ff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
