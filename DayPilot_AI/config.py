import os
BOT_CONFIG={
"title":'DayPilot AI',"domain":'Daily routine and time-block planning',
"system_prompt":'Answer only questions directly related to Daily routine and time-block planning. Politely reject unrelated questions.',
"behavior":'Act as a specialized DayPilot AI assistant and provide practical, structured guidance about Daily routine and time-block planning.',
"welcome_message":'Welcome to DayPilot AI. I can help with Daily routine and time-block planning.',
"welcome_title":'Your Daily Planner workspace',
"theme_name":'Daily Planner',"primary_color":'#2457d6',"surface_color":'#eef4ff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
