import ollama

model = 'llama3.1'

prompt = """
What color is the sky?
"""

stream = ollama.chat(
    model = model,
    messages = [{
        'role':'user',
        'content': prompt
    }],
    stream = True
)

print(stream)

for chunk in stream:
    print(chunk['message']['content'], end='')
print()