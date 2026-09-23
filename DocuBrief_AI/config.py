import os
BOT_CONFIG={
"title":'DocuBrief AI',"domain":'Long-document structured summaries',
"system_prompt":'Answer only questions directly related to Long-document structured summaries. Politely reject unrelated questions.',
"behavior":'Act as a specialized DocuBrief AI assistant and provide practical, structured guidance about Long-document structured summaries.',
"welcome_message":'Welcome to DocuBrief AI. I can help with Long-document structured summaries.',
"welcome_title":'Your Document Reader workspace',
"theme_name":'Document Reader',"primary_color":'#b45309',"surface_color":'#fff7e6',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
