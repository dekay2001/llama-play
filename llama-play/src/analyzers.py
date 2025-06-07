import ollama

model = 'llama3.1'


def create(model: str, stream: bool = False, config=None):
    writer = _create_file_writer(config.get('file_path'))
    if stream:
        return LlamaChatStream(model, writer)
    return LlamaChat(model, writer)


def _create_file_writer(file_path: str):
    if file_path:
        return _FileWriter(file_path)
    return _TerminalWriter()


class LlamaChatStream:
    def __init__(self, model: str, writer):
        self.model = model
        self._writer = writer

    def analyze(self, prompt: str):
        stream = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': prompt
            }],
            stream=True
        )
        self._writer.write(self._sentence(stream))
        

    def _sentence(self, stream):
        sentence = ''
        for chunk in stream:
            sentence += chunk['message']['content']
        return sentence
        


class LlamaChat:
    def __init__(self, model: str, writer=None):
        self.model = model
        self._writer = writer

    def analyze(self, prompt: str):
        response = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': prompt
            }],
            stream=False
        )
        self._writer.write(response['message']['content'])

class _FileWriter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write(self, content: str):
        with open(self.file_path, 'a') as file:
            file.write(content)



class _TerminalWriter:
    def write(self, content: str):
        print(content)
