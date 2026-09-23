import os
BOT_CONFIG={
"title":'SaaSBuilder AI',"domain":'SaaS product planning and MVP design',
"system_prompt":'Answer only questions directly related to SaaS product planning and MVP design. Politely reject unrelated questions.',
"behavior":'Act as a specialized SaaSBuilder AI assistant and provide practical, structured guidance about SaaS product planning and MVP design.',
"welcome_message":'Welcome to SaaSBuilder AI. I can help with SaaS product planning and MVP design.',
"welcome_title":'Your SaaS Workshop workspace',
"theme_name":'SaaS Workshop',"primary_color":'#7447c7',"surface_color":'#f4efff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
