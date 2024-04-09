import json
import requests
import datetime

stream = False

url = "https://chat.tune.app/api/chat/completions"
headers = {
    "Authorization": "tune-4d4a407b-ea73-4f3d-a288-a0de5db14d851709018521",
    "Content-Type": "application/json"
}                                                                 
# Read the content of the prompt.txt file
with open("prompt.txt", "r") as file:                                 prompt_text = file.read()

data = {
    "temperature": 0.5,
    "messages": [
    {
      "role": "system",
      "content": prompt_text  # Replacing the hardcoded text with the content of prompt.txt
    },
    {
      "role": "user",
      "content": "Who are you"
    }
  ],
    "model": "goliath-120b-16k-gptq",
    "stream": stream,
    "max_tokens": 1000
}
response = requests.post(url, headers=headers, json=data)

# Initialize an empty list to store the chat history
chat_history = []

# If the response is being streamed, handle each line of the response separately
if stream:
    for line in response.iter_lines():
        if line:
            l = line[6:]
            if l != b'[DONE]':
                # Parse the line as JSON and extract the 'content' field
                message = json.loads(l)
                content = message.get('content')
                # Add a timestamp and the role ('user' or 'assistant') to the message
                chat_history.append({
                    'role': 'user' if content.startswith('Q:') else 'assistant',
                    'content': content,
                    'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
                })
else:
    # If the response is not being streamed, parse the response as JSON and extract the 'choices' field
    response_json = response.json()
    choices = response_json.get('choices')
    if choices:
        # Loop through each choice and extract the 'message' field
        for choice in choices:
            message = choice.get('message')
            if message:
                # Add a timestamp and the role ('user' or 'assistant') to the message
                chat_history.append({
                    'role': 'user' if message.get('role') == 'user' else 'assistant',
                    'content': message.get('content'),
                    'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
                })

# Save the chat history to a file named 'chat_history.json'
with open('chat_history.json', 'w') as f:
    json.dump(chat_history, f, indent=4)

# Print the chat history for debugging purposes
print(chat_historimport json
import requests
import datetime

stream = False

url = "https://chat.tune.app/api/chat/completions"
headers = {
    "Authorization": "tune-4d4a407b-ea73-4f3d-a288-a0de5db14d851709018521",
    "Content-Type": "application/json"
}                                                                 
# Read the content of the prompt.txt file
with open("prompt.txt", "r") as file:                                 prompt_text = file.read()

data = {
    "temperature": 0.5,
    "messages": [
    {
      "role": "system",
      "content": prompt_text  # Replacing the hardcoded text with the content of prompt.txt
    },
    {
      "role": "user",
      "content": "Who are you"
    }
  ],
    "model": "goliath-120b-16k-gptq",
    "stream": stream,
    "max_tokens": 1000
}
response = requests.post(url, headers=headers, json=data)

# Initialize an empty list to store the chat history
chat_history = []

# If the response is being streamed, handle each line of the response separately
if stream:
    for line in response.iter_lines():
        if line:
            l = line[6:]
            if l != b'[DONE]':
                # Parse the line as JSON and extract the 'content' field
                message = json.loads(l)
                content = message.get('content')
                # Add a timestamp and the role ('user' or 'assistant') to the message
                chat_history.append({
                    'role': 'user' if content.startswith('Q:') else 'assistant',
                    'content': content,
                    'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
                })
else:
    # If the response is not being streamed, parse the response as JSON and extract the 'choices' field
    response_json = response.json()
    choices = response_json.get('choices')
    if choices:
        # Loop through each choice and extract the 'message' field
        for choice in choices:
            message = choice.get('message')
            if message:
                # Add a timestamp and the role ('user' or 'assistant') to the message
                chat_history.append({
                    'role': 'user' if message.get('role') == 'user' else 'assistant',
                    'content': message.get('content'),
                    'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
                })

# Save the chat history to a file named 'chat_history.json'
with open('chat_history.json', 'w') as f:
    json.dump(chat_history, f, indent=4)

# Print the chat history for debugging purposes
print(chat_history)
