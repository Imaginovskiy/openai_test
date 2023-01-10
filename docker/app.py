import os
import sys
import openai

def manage_sensitive(name):
    v1 = os.getenv(name)
    
    secret_fpath = f'/run/secrets/{name}'
    existence = os.path.exists(secret_fpath)
    
    if v1 is not None:
        return v1
    
    if existence:
        v2 = open(secret_fpath).read().rstrip('\n')
        return v2
    
    if all([v1 is None, not existence]):
        return KeyError(f'{name}')

openai.api_key = manage_sensitive(name='api_key')

cmd = ' '.join(sys.argv[1:])

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=cmd,
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0]["text"])
