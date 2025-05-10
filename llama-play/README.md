## Get started

I used `uv` to get started with this project.
Follow instructions [here](https://docs.astral.sh/uv/guides/install-python/#getting-started) 

To run:

```
uv run main.py
```


## Downloads
Following steps (here)[https://www.google.com/search?q=how+to+get+started+using+a+llama+3+python&rlz=1C1RXQR_enUS1137US1137&oq=how+to+get+started+using+a+llama+3+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRigATIHCAYQIRifBTIHCAcQIRifBdIBCTExNDgzajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:c7248970,vid:4T4Fr20yzBw,st:0]

- [Download](https://ollama.com/download/windows) Ollama from for your OS 
- Install it
- Open a command prompt and run `ollama -v` to test the installation. You should get something like...

```
PS C:\Dev\play-llama> ollama -v
ollama version is 0.6.8
```

- Install the model you want with command `ollama run llama.3.1`. This will start downloading the manifest.

When it is done it will run and you can send it a message.

```
PS C:\Dev\play-llama> ollama run llama3.1
pulling manifest
pulling manifest
pulling 667b0c1932bc: 100% ▕████████████████████████████████▏ 4.9 GB
pulling 948af2743fc7: 100% ▕████████████████████████████████▏ 1.5 KB
pulling 0ba8f0e314b4: 100% ▕████████████████████████████████▏  12 KB
pulling 56bb8bd477a5: 100% ▕████████████████████████████████▏   96 B
pulling 455f34728c9b: 100% ▕████████████████████████████████▏  487 B
verifying sha256 digest
writing manifest
success
>>> hi
How's it going? Is there something I can help you with or would you like to chat?

>>> Send a message (/? for help)
```

- Do a quick test to see the installed models with command `ollama list`.

```
PS C:\Dev\play-llama> ollama list
NAME               ID              SIZE      MODIFIED      
llama3.1:latest    46e0c10c039e    4.9 GB    2 minutes ago
PS C:\Dev\play-llama>
```


Before getting start, create a virtual environement in python and install ollama. I use UV.

```
uv add ollama.
```


```python
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
```

To run with uv use

```
uv run src\example.py
```