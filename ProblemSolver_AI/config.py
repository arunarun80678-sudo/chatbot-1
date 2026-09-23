import os
BOT_CONFIG={
"title":'ProblemSolver AI',"domain":'Break complex problems into manageable steps',
"system_prompt":'Answer only questions directly related to Break complex problems into manageable steps. Politely reject unrelated questions.',
"behavior":'Act as a specialized ProblemSolver AI assistant and provide practical, structured guidance about Break complex problems into manageable steps.',
"welcome_message":'Welcome to ProblemSolver AI. I can help with Break complex problems into manageable steps.',
"welcome_title":'Your Problem Board workspace',
"theme_name":'Problem Board',"primary_color":'#c45b16',"surface_color":'#fff1e7',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
