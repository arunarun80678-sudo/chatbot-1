import os
BOT_CONFIG={
"title":'ChartMaker AI',"domain":'Recommend charts and explain data visualization',
"system_prompt":'Answer only questions directly related to Recommend charts and explain data visualization. Politely reject unrelated questions.',
"behavior":'Act as a specialized ChartMaker AI assistant and provide practical, structured guidance about Recommend charts and explain data visualization.',
"welcome_message":'Welcome to ChartMaker AI. I can help with Recommend charts and explain data visualization.',
"welcome_title":'Your Chart Studio workspace',
"theme_name":'Chart Studio',"primary_color":'#c45b16',"surface_color":'#fff1e7',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
