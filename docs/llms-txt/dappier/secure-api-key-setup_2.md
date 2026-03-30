# Secure API Key Setup
os.environ["DAPPIER_API_KEY"] = getpass.getpass("Enter your Dappier API Key: ")
os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")

dappier_client = Dappier()