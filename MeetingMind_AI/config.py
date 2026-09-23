import os
BOT_CONFIG={
"title":'MeetingMind AI',"domain":'Meeting notes, action items & follow-ups',
"system_prompt":'Answer only questions directly related to Meeting notes, action items & follow-ups. Politely reject unrelated questions.',
"behavior":'Act as a specialized MeetingMind AI assistant and provide practical, structured guidance about Meeting notes, action items & follow-ups.',
"welcome_message":'Welcome to MeetingMind AI. I can help with Meeting notes, action items & follow-ups.',
"welcome_title":'Your Meeting Desk workspace',
"theme_name":'Meeting Desk',"primary_color":'#19324d',"surface_color":'#edf3f8',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
