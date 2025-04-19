# Example script using llama models to summarize text
from transformers import LlamaTokenizer, LlamaForCausalLM

# I need to get the model https://huggingface.co/meta-llama/Llama-2-7b-chat-hf

def main():
    tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

    input_text = "Summary of my installation blah blah blah. " * 100  # Example long text
    # Ensure the input text is long enough to demonstrate truncation
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=2048, truncation=True)

    output = model.generate(input_ids, max_length=512, num_return_sequences=1)
    summary = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Summary:", summary)


if __name__ == "__main__":
    main()
    
