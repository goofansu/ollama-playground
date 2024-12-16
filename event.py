from ollama import chat
from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
  datetime: datetime
  task: str

response = chat(
  messages=[
    {
      'role': 'user',
      'content': 'I have a meeting at tomorrow afternoon 2 pm, today is 2024-12-16.',
    }
  ],
  model='llama3.2',
  format=Event.model_json_schema(),
)

event = Event.model_validate_json(response.message.content)
print(event)
