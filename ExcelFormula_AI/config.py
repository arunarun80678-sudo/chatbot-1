import os
BOT_CONFIG={
"title":'ExcelFormula AI',"domain":'Explain spreadsheet formulas and workflows',
"system_prompt":'Answer only questions directly related to Explain spreadsheet formulas and workflows. Politely reject unrelated questions.',
"behavior":'Act as a specialized ExcelFormula AI assistant and provide practical, structured guidance about Explain spreadsheet formulas and workflows.',
"welcome_message":'Welcome to ExcelFormula AI. I can help with Explain spreadsheet formulas and workflows.',
"welcome_title":'Your Formula Desk workspace',
"theme_name":'Formula Desk',"primary_color":'#27833b',"surface_color":'#edf9ef',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
