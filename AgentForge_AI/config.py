import os
BOT_CONFIG={
"title":'AgentForge AI',"domain":'Design AI-agent workflows and task pipelines',
"system_prompt":'Answer only questions directly related to Design AI-agent workflows and task pipelines. Politely reject unrelated questions.',
"behavior":'Act as a specialized AgentForge AI assistant and provide practical, structured guidance about Design AI-agent workflows and task pipelines.',
"welcome_message":'Welcome to AgentForge AI. I can help with Design AI-agent workflows and task pipelines.',
"welcome_title":'Your Agent Forge workspace',
"theme_name":'Agent Forge',"primary_color":'#0787a3',"surface_color":'#e7faff',
"port":int(os.getenv("PORT","5000")),"gemini_model":os.getenv("GEMINI_TEXT_MODEL","gemini-3.1-flash-lite"),
"secret_key":os.getenv("FLASK_SECRET_KEY","change-this-secret")}
