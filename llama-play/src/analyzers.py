import ollama

model = 'llama3.1'


def create(model: str, stream: bool = False):
    if stream:
        return LlamaChatStream(model)
    return LlamaChat(model)


class LlamaChatStream:
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


class LlamaChat:
    def __init__(self, model: str):
        self.model = model

    def analyze(self, prompt: str):
        response = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': prompt
            }],
            stream=False
        )
        print(response['message']['content'])


if __name__ == '__main__':
    prompt = """
    Tell me a dad joke
    """
    chat = Chat(model)
    chat.ask(prompt)
    ollama.list()

