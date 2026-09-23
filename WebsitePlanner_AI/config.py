import os
BOT_CONFIG={
"title":'WebsitePlanner AI',"domain":'Plan website structure, pages and features',
"system_prompt":'Answer only questions directly related to Plan website structure, pages and features. Politely reject unrelated questions.',
"behavior":'Act as a specialized WebsitePlanner AI assistant and provide practical, structured guidance about Plan website structure, pages and features.',
"welcome_message":'Welcome to WebsitePlanner AI. I can help with Plan website structure, pages and features.',
"welcome_title":'Your Site Planner workspace',
"theme_name":'Site Planner',"primary_color":'#1976b9',"surface_color":'#eaf6ff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
