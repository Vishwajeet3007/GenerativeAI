from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()
prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

url = 'https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDV7GC/ref=sr_1_1?crid=334ABWY9TAQ4Y&dib=eyJ2IjoiMSJ9.asb3l5WT-2IvI1DgvMjmGkUApXih9jwV_lKWkiCfaEUT0DzglHEA19yGY1dngXs8Cj3jKjSka_zf2UOJfuC-lrQ2eYFyN21g8HZNTuItmVEK9-NjpTGn7yd9Fq0GE2LuybP9tar-h1Wf3cOF4HXTNisx0Uu_i_-jjbY1UAVxLd7n3ftwDu_Evi4c-sqFkn35CHf5Fzp98I4saoOTDI38aHlj-Q9f8gySLlwrG76wljs.2_gqPwVkL2XzAwZTBAktdqIjwu_ujUg38YVL5W1OKUo&dib_tag=se&keywords=apple%2Bm4%2Bmacbook%2Bair&nsdOptOutParam=true&qid=1751528781&sprefix=apple%2Bm4%2Caps%2C371&sr=8-1&th=1'

loader = WebBaseLoader(url)
docs = loader.load()
chain = prompt | model | parser
print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))