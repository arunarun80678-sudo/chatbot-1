import os
BOT_CONFIG={
"title":'ResearchScout AI',"domain":'Research topic exploration and research planning',
"system_prompt":'Answer only questions directly related to Research topic exploration and research planning. Politely reject unrelated questions.',
"behavior":'Act as a specialized ResearchScout AI assistant and provide practical, structured guidance about Research topic exploration and research planning.',
"welcome_message":'Welcome to ResearchScout AI. I can help with Research topic exploration and research planning.',
"welcome_title":'Your Research Lab workspace',
"theme_name":'Research Lab',"primary_color":'#4f46b5',"surface_color":'#eef0ff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
