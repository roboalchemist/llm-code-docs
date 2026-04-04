# Source: https://novita.ai/docs/guides/deepsearcher.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DeepSearcher

> Easily access module support from Novita AI on DeepSearcher to build advanced search applications.

[DeepSearcher](https://github.com/zilliztech/deep-searcher) is an open-source solution designed to transform private data search and reasoning by integrating cutting-edge large language models (LLMs) with vector databases such as Milvus. With support for LLMs and embedding models from Novita AI, this powerful configuration delivers unmatched accuracy and efficiency in private data search.

This step-by-step guide will walk you through how to quickly and easily configure Novita AI with DeepSearcher.

## How to use DeepSearcher with Novita

Step 1: Follow the example in `examples/basic_example.py` .

<Frame>
    <img src="https://mintcdn.com/novitaai/OIO9nfACcX0vhcTI/images/step1Followtheexample.jpeg?fit=max&auto=format&n=OIO9nfACcX0vhcTI&q=85&s=3d84643c25bbf8bb41dbe2855fbbfb33" alt="Step1followtheexample Jpe" width="2792" height="952" data-path="images/step1Followtheexample.jpeg" />
</Frame>

Step 2: Add the following code below the line `config = Configuration()` :

```python  theme={"system"}
config.set_provider_config("llm", "NOVITA", {"model": "deepseek/deepseek-r1-turbo"})
config.set_provider_config("embedding", "NovitaEmbedding", {"model": "baai/bge-m3"})
```

<Frame>
    <img src="https://mintcdn.com/novitaai/OIO9nfACcX0vhcTI/images/step2Addcodebelowunderthelineconfig=Configuration.jpeg?fit=max&auto=format&n=OIO9nfACcX0vhcTI&q=85&s=edab7da1af56f9fb3ad5e7cbde9ee3b8" alt="Step2addcodebelowunderthelineconfig=configuration Jpe" width="2698" height="446" data-path="images/step2Addcodebelowunderthelineconfig=Configuration.jpeg" />
</Frame>

Step 3: Run `examples/basic_example.py` to execute the integration.

You'll get the following results:

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/output1.jpeg?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=5191c2671219202b7d8e3ef29cc618f6" alt="Output1 Jpe" width="2692" height="1732" data-path="images/output1.jpeg" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/output2.jpeg?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=a816b7b638dbed89a9acd9be735ef6dc" alt="Output2 Jpe" width="2718" height="1840" data-path="images/output2.jpeg" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/output3.jpeg?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=e2fdaa1f6d5606c4cd9bcedffc10ea22" alt="Output3 Jpe" width="2722" height="1546" data-path="images/output3.jpeg" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/novitaai/OIO9nfACcX0vhcTI/images/output4.jpeg?fit=max&auto=format&n=OIO9nfACcX0vhcTI&q=85&s=809aec10ff8c1729a2a4917755d93f8b" alt="Output4 Jpe" width="2758" height="1680" data-path="images/output4.jpeg" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/novitaai/OIO9nfACcX0vhcTI/images/output5.jpeg?fit=max&auto=format&n=OIO9nfACcX0vhcTI&q=85&s=6f8dae35f4553103711f71bedb922ca4" alt="Output5 Jpe" width="2728" height="516" data-path="images/output5.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).