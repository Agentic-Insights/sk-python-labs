# 🧠 Semantic Kernel Python Tutorial 101 🐍

Welcome to the Semantic Kernel Python Tutorial 101! This repository provides a hands-on introduction to using Semantic Kernel with Python, demonstrating integration with various AI services.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- Ollama - https://www.ollama.com/
- Groq API key - https://console.groq.com/keys

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/killerapp/semantic-kernel-python-tutorial.git
   cd semantic-kernel-python-tutorial
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## 🔧 Configuration

Before running the examples, you need to set up your environment variables. We provide sample `.env` files for different services:

- [.env.ollama.example](sk-ollama/.env.ollama.example) - For Ollama
- [.env.groq.example](sk-groq/.env.groq.example) - For Groq

Copy the appropriate `.env.*.example` file to `.env` and fill in your API keys and other required information.

## 📚 Examples

### Ollama Example

Run the Ollama example with:

```
cd sk-ollama
python sk-ollama.py
```

This script demonstrates how to use Semantic Kernel with an Ollama server. Key features:


```19:31:sk-ollama.py
execution_settings = OllamaChatPromptExecutionSettings()

kernel = Kernel()

# Alternative using Ollama:
service_id="ollama"
kernel.add_service(
  OllamaChatCompletion(
      service_id=service_id
  )
)
```


### Groq Example

Run the Groq example with:

```
cd sk-groq
python sk-groq.py
```

This script shows how to integrate Semantic Kernel with Groq. Notable sections:


```23:32:sk-groq.py
# Use Groq:
service_id = "groq"
service = OpenAIChatCompletion(
    service_id=service_id,
    api_key=os.getenv("GROQ_API_KEY"),
    org_id=os.getenv("GROQ_ORG_ID"),
    ai_model_id=os.getenv("GROQ_MODEL")
)
service.client.base_url = os.getenv("GROQ_BASE_URL")  # this is the important line
kernel.add_service(service=service)
```


## 🧩 Plugins

This tutorial includes one sample plugin to demonstrate Semantic Kernel's capabilities:

- FunPlugin: Generates jokes, limericks, and creative excuses.

You can find plugins in the `plugins/` directory.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📬 Contact

If you have any questions or feedback, please open an issue in this repository.

Happy coding with Semantic Kernel! 🎉
