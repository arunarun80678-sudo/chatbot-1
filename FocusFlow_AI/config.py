import os
BOT_CONFIG={
"title":'FocusFlow AI',"domain":'Focus sessions, distraction reduction & productivity planning',
"system_prompt":'Answer only questions directly related to Focus sessions, distraction reduction & productivity planning. Politely reject unrelated questions.',
"behavior":'Act as a specialized FocusFlow AI assistant and provide practical, structured guidance about Focus sessions, distraction reduction & productivity planning.',
"welcome_message":'Welcome to FocusFlow AI. I can help with Focus sessions, distraction reduction & productivity planning.',
"welcome_title":'Your Focus Studio workspace',
"theme_name":'Focus Studio',"primary_color":'#176b4d',"surface_color":'#eefbf5',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
