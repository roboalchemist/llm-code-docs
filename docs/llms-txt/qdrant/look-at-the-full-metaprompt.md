# Look at the full metaprompt
print(metaprompt)

```

**Response:**

```bash
You are a software architect.
Answer the following question using the provided context.
If you can't find the answer, do not pretend you know it, but answer "I don't know".

Question: What tools should I need to use to build a web service using vector embeddings for search?

Context:
Qdrant is a vector database & vector similarity search engine. It deploys as an API service providing search for the nearest high-dimensional vectors. With Qdrant, embeddings or neural network encoders can be turned into full-fledged applications for matching, searching, recommending, and much more!
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
PyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing.

Answer:

```

Our current prompt is much longer, and we also used a couple of strategies to make the responses even better:

1. The LLM has the role of software architect.
2. We provide more context to answer the question.
3. If the context contains no meaningful information, the model shouldn’t make up an answer.

Let’s find out if that works as expected.

**Question:**

```python
query_deepseek(metaprompt)

```

**Answer:**

```bash
'To build a web service using vector embeddings for search, you can use the following tools:\n\n1. **Qdrant**: As a vector database and similarity search engine, Qdrant will handle the storage and retrieval of high-dimensional vectors. It provides an API service for searching and matching vectors, making it ideal for applications that require vector-based search functionality.\n\n2. **FastAPI**: This web framework is perfect for building the API layer of your web service. It is fast, easy to use, and based on Python type hints, which makes it a great choice for developing the backend of your service. FastAPI will allow you to expose endpoints that interact with Qdrant for vector search operations.\n\n3. **PyTorch**: If you need to generate vector embeddings from your data (e.g., text, images), PyTorch can be used to create and train neural network models that produce these embeddings. PyTorch is a powerful machine learning framework that supports a wide range of applications, including natural language processing and computer vision.\n\n### Summary:\n- **Qdrant** for vector storage and search.\n- **FastAPI** for building the web service API.\n- **PyTorch** for generating vector embeddings (if needed).\n\nThese tools together provide a robust stack for building a web service that leverages vector embeddings for search functionality.'

```

### [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#testing-out-the-rag-pipeline) Testing out the RAG pipeline

By leveraging the semantic context we provided our model is doing a better job answering the question. Let’s enclose the RAG as a function, so we can call it more easily for different prompts.

```python
def rag(question: str, n_points: int = 3) -> str:
    results = client.query_points(
        collection_name=collection_name,
        query=models.Document(text=question, model=model_name),
        limit=n_points,
    )

    context = "\n".join(r.payload["document"] for r in results.points)

    metaprompt = f"""
    You are a software architect.
    Answer the following question using the provided context.
    If you can't find the answer, do not pretend you know it, but only answer "I don't know".

    Question: {question.strip()}

    Context:
    {context.strip()}

    Answer:
    """

    return query_deepseek(metaprompt)

```

Now it’s easier to ask a broad range of questions.

**Question:**

```python
rag("What can the stack for a web api look like?")

```

**Answer:**

```bash
'The stack for a web API can include the following components based on the provided context:\n\n1. **Web Framework**: FastAPI can be used as the web framework for building the API. It is modern, fast, and leverages Python type hints for better development and performance.\n\n2. **Reverse Proxy/Web Server**: NGINX can be used as a reverse proxy or web server to handle incoming HTTP requests, load balancing, and serving static content. It is known for its high performance and low resource consumption.\n\n3. **Containerization**: Docker can be used to containerize the application, making it easier to build, share, and run the API consistently across different environments without worrying about configuration issues.\n\nThis stack provides a robust, scalable, and efficient setup for building and deploying a web API.'

```

**Question:**

```python
rag("Where is the nearest grocery store?")

```

**Answer:**

```bash
"I don't know. The provided context does not contain any information about the location of the nearest grocery store."

```

Our model can now:

1. Take advantage of the knowledge in our vector datastore.
2. Answer, based on the provided context, that it can not provide an answer.

We have just shown a useful mechanism to mitigate the risks of hallucinations in Large Language Models.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/rag-deepseek.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/rag-deepseek.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)

## Privacy Preference Center

Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.


[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)

Allow All

### Manage Consent Preferences

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

<|page-181-lllmstxt|>
## filtering
- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Filtering