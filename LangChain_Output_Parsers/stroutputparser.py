from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # ✅ Supports text-generation
    task="text-generation",
    temperature=0.7,
    max_new_tokens=300
)


# Prompt 1 -> Detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# Prompt 2 -> Summary
template2 = PromptTemplate(
    template='Write a 5-line summary on the following text:\n{text}',
    input_variables=['text']
)

# Invoke first prompt
prompt1 = template1.invoke({'topic': 'black hole'})
result = model.invoke(prompt1)
print("\n📝 Detailed Report:\n", result)

# Invoke second prompt with the generated report
prompt2 = template2.invoke({'text': result})
summary = model.invoke(prompt2)
print("\n📄 Summary:\n", summary)
