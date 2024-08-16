import ollama

def generate_problem_list(hpi):
    stream = ollama.chat(
        model="problemlist",
        messages=[{"role": "user", "content": hpi.strip()}],
        stream=True,
        options={ 
            "num_ctx": 4096
        }
    )
    first_chunk = False
    for chunk in stream:
        if not first_chunk:
            print("# ", end="", flush=True)
            first_chunk = True
        tok = chunk["message"]["content"]
        if tok.strip() == ";":
            print("\n#", end="", flush=True)
            continue
        print(tok, end="", flush=True)
    print("", flush=True)

def main():
    inp = input("\033[94mEnter your HPI, or type 'exit' to quit:\033[0m\n")
    print("\033[93m\nThinking...\033[0m\n")
    generate_problem_list(inp)

if __name__ == "__main__":
    main()
