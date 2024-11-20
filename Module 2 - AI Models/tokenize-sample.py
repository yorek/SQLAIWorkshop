import tiktoken

tokenizer = tiktoken.get_encoding("cl100k_base")
encoded = tokenizer.encode("I want to learn everything about AI, Vectors, Embeddings and all that cool stuff, and how to use it on my own data!")
decoded = tokenizer.decode_tokens_bytes(encoded)

#print the decoded tokens, one per line
print(decoded)