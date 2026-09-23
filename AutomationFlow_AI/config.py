import os
BOT_CONFIG={
"title":'AutomationFlow AI',"domain":'Build workflow automation ideas',
"system_prompt":'Answer only questions directly related to Build workflow automation ideas. Politely reject unrelated questions.',
"behavior":'Act as a specialized AutomationFlow AI assistant and provide practical, structured guidance about Build workflow automation ideas.',
"welcome_message":'Welcome to AutomationFlow AI. I can help with Build workflow automation ideas.',
"welcome_title":'Your Automation Flow workspace',
"theme_name":'Automation Flow',"primary_color":'#2457d6',"surface_color":'#eef4ff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
