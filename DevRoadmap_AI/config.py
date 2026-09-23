import os
BOT_CONFIG={
"title":'DevRoadmap AI',"domain":'Personalized software-learning roadmaps',
"system_prompt":'Answer only questions directly related to Personalized software-learning roadmaps. Politely reject unrelated questions.',
"behavior":'Act as a specialized DevRoadmap AI assistant and provide practical, structured guidance about Personalized software-learning roadmaps.',
"welcome_message":'Welcome to DevRoadmap AI. I can help with Personalized software-learning roadmaps.',
"welcome_title":'Your Developer Roadmap workspace',
"theme_name":'Developer Roadmap',"primary_color":'#2457d6',"surface_color":'#eef4ff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
