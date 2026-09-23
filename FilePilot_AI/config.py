import os
BOT_CONFIG={
"title":'FilePilot AI',"domain":'Organize and classify personal/work files',
"system_prompt":'Answer only questions directly related to Organize and classify personal/work files. Politely reject unrelated questions.',
"behavior":'Act as a specialized FilePilot AI assistant and provide practical, structured guidance about Organize and classify personal/work files.',
"welcome_message":'Welcome to FilePilot AI. I can help with Organize and classify personal/work files.',
"welcome_title":'Your File Command workspace',
"theme_name":'File Command',"primary_color":'#475569',"surface_color":'#eef2f6',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
