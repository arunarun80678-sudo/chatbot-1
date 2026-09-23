import os
BOT_CONFIG={
"title":'AIModelGuide AI',"domain":'Explain AI/ML model concepts and workflows',
"system_prompt":'Answer only questions directly related to Explain AI/ML model concepts and workflows. Politely reject unrelated questions.',
"behavior":'Act as a specialized AIModelGuide AI assistant and provide practical, structured guidance about Explain AI/ML model concepts and workflows.',
"welcome_message":'Welcome to AIModelGuide AI. I can help with Explain AI/ML model concepts and workflows.',
"welcome_title":'Your Model Observatory workspace',
"theme_name":'Model Observatory',"primary_color":'#8b3fc7',"surface_color":'#f7edff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
