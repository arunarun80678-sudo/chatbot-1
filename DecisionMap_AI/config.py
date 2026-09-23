import os
BOT_CONFIG={
"title":'DecisionMap AI',"domain":'Compare options using user-provided criteria',
"system_prompt":'Answer only questions directly related to Compare options using user-provided criteria. Politely reject unrelated questions.',
"behavior":'Act as a specialized DecisionMap AI assistant and provide practical, structured guidance about Compare options using user-provided criteria.',
"welcome_message":'Welcome to DecisionMap AI. I can help with Compare options using user-provided criteria.',
"welcome_title":'Your Decision Map workspace',
"theme_name":'Decision Map',"primary_color":'#087f78',"surface_color":'#e9fbf8',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
