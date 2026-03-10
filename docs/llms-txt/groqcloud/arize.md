# Source: https://console.groq.com/docs/arize

---
description: Learn how to use Arize with Groq to add observability, tracing, and evaluation to your LLM applications for robust monitoring and debugging.
title: Arize + Groq: AI Observability &amp; Tracing - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Arize + Groq: Open-Source AI Observability](#arize--groq-opensource-ai-observability)

  
[Arize Phoenix](https://docs.arize.com/phoenix) developed by [Arize AI](https://arize.com/) is an open-source AI observability library that enables comprehensive tracing and monitoring for your AI applications. By integrating Arize's observability tools with your Groq-powered applications, you can gain deep insights into your LLM worklflow's performance and behavior with features including:

* **Automatic Tracing:** Capture detailed metrics about LLM calls, including latency, token usage, and exceptions
* **Real-time Monitoring:** Track application performance and identify bottlenecks in production
* **Evaluation Framework:** Utilize pre-built templates to assess LLM performance
* **Prompt Management:** Easily iterate on prompts and test changes against your data

### [Python Quick Start (3 minutes to hello world)](#python-quick-start-3-minutes-to-hello-world)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install arize-phoenix-otel openinference-instrumentation-groq groq
```

#### [2\. Sign up for an Arize Phoenix account.](#2-sign-up-for-an-arize-phoenix-account)

#### [2\. Configure your Groq and Arize Phoenix API keys:](#2-configure-your-groq-and-arize-phoenix-api-keys)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export PHOENIX_API_KEY="your-phoenix-api-key"
```

#### [3\. (Optional) Create a new project or use the "default" project as your project\_name below.](#3-optional-create-a-new-project-or-use-the-default-project-as-your-projectname-below)

#### [4\. Create your first traced Groq application:](#4-create-your-first-traced-groq-application)

In Arize Phoenix, **traces** capture the complete journey of an LLM request through your application, while **spans** represent individual operations within that trace. The instrumentation automatically captures important metrics and metadata.

Python

```
import os
from phoenix.otel import register
from openinference.instrumentation.groq import GroqInstrumentor
from groq import Groq

# Configure environment variables for Phoenix
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"api_key={os.getenv('PHOENIX_API_KEY')}"
os.environ["PHOENIX_CLIENT_HEADERS"] = f"api_key={os.getenv('PHOENIX_API_KEY')}"
os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "https://app.phoenix.arize.com"

# Configure Phoenix tracer
tracer_provider = register(
    project_name="default",
    endpoint="https://app.phoenix.arize.com/v1/traces",
)

# Initialize Groq instrumentation
GroqInstrumentor().instrument(tracer_provider=tracer_provider)

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Make an instrumented LLM call
chat_completion = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "Explain the importance of AI observability"
    }],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
```

Running the above code will create an automatically instrumented Groq application! The traces will be available in your Phoenix dashboard within the `default` project, showing detailed information about:

* **Application Latency:** Identify slow components and bottlenecks
* **Token Usage:** Track token consumption across different operations
* **Runtime Exceptions:** Capture and analyze errors and rate limits
* **LLM Parameters:** Monitor temperature, system prompts, and other settings
* **Response Analysis:** Examine LLM outputs and their characteristics

**Challenge**: Update an existing Groq-powered application you've built to add Arize Phoenix tracing!

For more detailed documentation and resources on building observable LLM applications with Groq and Arize, see:

* [Official Documentation: Groq Integration Guide](https://docs.arize.com/phoenix/tracing/integrations-tracing/groq)
* [Blog: Tracing with Groq](https://arize.com/blog/tracing-groq/)
* [Webinar: Tracing and Evaluating LLM Apps with Groq and Arize Phoenix](https://youtu.be/KjtrILr6JZI?si=iX8Udo-EYsK2JOvF)