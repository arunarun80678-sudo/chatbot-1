import os
BOT_CONFIG={
"title":'AppIdea AI',"domain":'Generate mobile-app concepts and feature plans',
"system_prompt":'Answer only questions directly related to Generate mobile-app concepts and feature plans. Politely reject unrelated questions.',
"behavior":'Act as a specialized AppIdea AI assistant and provide practical, structured guidance about Generate mobile-app concepts and feature plans.',
"welcome_message":'Welcome to AppIdea AI. I can help with Generate mobile-app concepts and feature plans.',
"welcome_title":'Your App Foundry workspace',
"theme_name":'App Foundry',"primary_color":'#c43d78',"surface_color":'#fff0f6',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
