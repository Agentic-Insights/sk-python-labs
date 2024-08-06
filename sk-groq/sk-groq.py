# Semantic Kernel Labs 101 - Python
# Example for using Semantic Kernel with Groq
from dotenv import load_dotenv
load_dotenv()

import asyncio
import os

# Semantic Kernel packages 
from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.open_ai_prompt_execution_settings import OpenAIChatPromptExecutionSettings
from semantic_kernel.prompt_template import PromptTemplateConfig
# Semantic Kernel packages - end

execution_settings = OpenAIChatPromptExecutionSettings()

# Kernel Setup
kernel = Kernel()
# Use Groq:
service_id = "groq"
service = OpenAIChatCompletion(
    service_id=service_id,
    api_key=os.getenv("GROQ_API_KEY"),
    org_id=os.getenv("GROQ_ORG_ID"),
    ai_model_id=os.getenv("GROQ_MODEL")
)
service.client.base_url = os.getenv("GROQ_BASE_URL")
kernel.add_service(service=service)

# Prompt based example
prompt = """
1) A robot may not injure a human being or, through inaction,
allow a human being to come to harm.

2) A robot must obey orders given it by human beings except where
such orders would conflict with the First Law.

3) A robot must protect its own existence as long as such protection
does not conflict with the First or Second Law.

Give me the TLDR in exactly 8 words."""

prompt_template_config = PromptTemplateConfig(
    template=prompt,
    name="tldr",
    template_format="semantic-kernel",
)

sk_function = kernel.add_function(
    function_name="tldr_function",
    plugin_name="tldr_plugin",
    prompt_template_config=prompt_template_config,
    prompt_execution_settings=execution_settings
)

# Plugin based implementation - see the 'plugins' directory
plugins_directory = "../plugins"
plugin = kernel.add_plugin(parent_directory=plugins_directory, plugin_name="FunPlugin")
arguments = KernelArguments(input="time travel to dinosaur age", style="super silly")

# Run your prompt
# Note: functions are run asynchronously
async def main():
    print("\n=== Prompt Template Example ===")
    print("Prompt: Give me the TLDR of Asimov's Three Laws of Robotics in exactly 8 words.")
    result = await kernel.invoke(sk_function)
    print("Result:", result)

    print("\n=== Plugin Example ===")
    print("Using the FunPlugin to generate an excuse...")
    input_scenario = "time travel to dinosaur age"
    style = "super silly"
    print(f"Scenario: {input_scenario}")
    print(f"Style: {style}")
    
    arguments = KernelArguments(input=input_scenario, style=style)
    result = await kernel.invoke(plugin["Excuses"], arguments)
    print("Generated Excuse:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
