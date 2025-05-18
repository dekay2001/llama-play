import ollama

model = 'llama3.1'



class LlamaChat:
    def __init__(self, model: str):
        self.model = model

    def analyze(self, prompt: str):
        stream = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': prompt
            }],
            stream=True
        )
        for chunk in stream:
            print(chunk['message']['content'], end='')
        print()


if __name__ == '__main__':
    prompt = """
    Tell me a dad joke
    """
    chat = Chat(model)
    chat.ask(prompt)
    ollama.list()

