from ollama import chat
from pydantic import BaseModel

class Country(BaseModel):
  name: str
  capital: str
  languages: list[str]

response = chat(
  messages=[
    {
      'role': 'system',
      'content': 'Parse information for country and return as JSON.',
    },
    {
      'role': 'user',
      'content': 'Tell me about Canada.',
    }
  ],
  model='llama3.2',
  format=Country.model_json_schema(),
)

country = Country.model_validate_json(response.message.content)
print(country)
