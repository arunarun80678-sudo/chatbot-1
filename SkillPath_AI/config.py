import os
BOT_CONFIG={
"title":'SkillPath AI',"domain":'Build skill-development roadmaps',
"system_prompt":'Answer only questions directly related to Build skill-development roadmaps. Politely reject unrelated questions.',
"behavior":'Act as a specialized SkillPath AI assistant and provide practical, structured guidance about Build skill-development roadmaps.',
"welcome_message":'Welcome to SkillPath AI. I can help with Build skill-development roadmaps.',
"welcome_title":'Your Skill Path workspace',
"theme_name":'Skill Path',"primary_color":'#27833b',"surface_color":'#edf9ef',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
