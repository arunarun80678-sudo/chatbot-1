import os
BOT_CONFIG={
"title":'HabitLoop AI',"domain":'Habit planning and progress tracking',
"system_prompt":'Answer only questions directly related to Habit planning and progress tracking. Politely reject unrelated questions.',
"behavior":'Act as a specialized HabitLoop AI assistant and provide practical, structured guidance about Habit planning and progress tracking.',
"welcome_message":'Welcome to HabitLoop AI. I can help with Habit planning and progress tracking.',
"welcome_title":'Your Habit Tracker workspace',
"theme_name":'Habit Tracker',"primary_color":'#7447c7',"surface_color":'#f4efff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
