import os
BOT_CONFIG={
"title":'WebDevMentor AI',"domain":'HTML/CSS/JS web-development guidance',
"system_prompt":'Answer only questions directly related to HTML/CSS/JS web-development guidance. Politely reject unrelated questions.',
"behavior":'Act as a specialized WebDevMentor AI assistant and provide practical, structured guidance about HTML/CSS/JS web-development guidance.',
"welcome_message":'Welcome to WebDevMentor AI. I can help with HTML/CSS/JS web-development guidance.',
"welcome_title":'Your Web Studio workspace',
"theme_name":'Web Studio',"primary_color":'#0787a3',"surface_color":'#e7faff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
