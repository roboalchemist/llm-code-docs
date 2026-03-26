# Source: https://docs.tabnine.com/main/welcome/readme/privacy.md

# Privacy

## Code Privacy

**When using Tabnine models, your code remains private. Tabnine NEVER retains or shares any of your code with third parties.**

Tabnine has a *no-train-no-retain* policy. This is in place regardless which model is being used.

### Querying the Tabnine AI Model for AI Coding Assistance

As you code, the Tabnine client (plugin) requests AI assistance from the Tabnine cluster.

For code suggestions, the process occurs in the background as you code. For chat, this request process occurs once the user asks a question.

These requests include **some code from the local project as context** (the **“context window”** as described below) to allow Tabnine to return the most relevant and accurate answers. This context window **may include elements from your local environment, such as**:

* Chat history (for chat)
* Lines of code
* Variables
* Type declarations
* Functions
* Objects
* Related imports from the current file
* Related files
* Syntactic and semantic error reports

This context is deleted **immediately** after the server returns the answer to the client.

**Tabnine doesn’t retain any user code beyond the immediate time frame** required for inferencing the model. This is what we call ephemeral processing.

The sole purpose of the **context window** is to facilitate the most accurate answers possible. The moment that output is generated, the code is discarded and is never stored.

This is true even for [Tabnine Enterprise’s](https://www.tabnine.com/enterprise) private deployment options (on-premises and VPC).

#### **With Tabnine models, your code is not shared with third parties**

We develop our AI models based on our own pioneering experience and the best-of-breed, permissive, open source technologies in the market.

No third-party APIs are used.

#### **Tabnine does not train its models on your code**

**Tabnine’s code completion model and Tabnine Protected chat model are only trained on open source code with permissive licenses.**

Private fine-tuned AI models are pretrained on private code by Tabnine and are only accessible by your team members and stored on your private setup.

Learn more about [Tabnine’s AI models](https://docs.tabnine.com/main/welcome/readme/ai-models).

{% hint style="info" %}
**Clarification regarding the Magic Moments feature**

The code completion examples in the Tabnine Hub (in the IDE) under the **Magic Moments** tab are saved locally on the user's machine and never leave the computer.
{% endhint %}

### Personalization

Tabnine's personalization capabilities — including **context** through local code awareness and **connection** to software repository for global code awareness — require creating a RAG index of your code. The computation for vector embeddings for the chat [RAG index](https://docs.tabnine.com/main/welcome/personalization/tabnines-personalization-in-depth#the-rag-index) requires a lot of resources, and cannot be done locally without stressing the user’s machine. Tabnine performs this computation on the server GPU while keeping the same principles:

* Your code remains private; Tabnine never stores your code.
* Tabnine does not share any of your code with third parties.
* Tabnine does not train on your code.

[Learn more](https://docs.tabnine.com/main/welcome/personalization#personalization-and-code-privacy)

### **Data Plane in Self-Hosted / Air-Gapped Deployment**

The Tabnine cluster collects operational metrics and logs to ensure system health and quality of service.

In an air-gapped deployment, metrics can be sent to a Prometheus server and logs can be sent to your log aggregator. In a self-hosted deployment, the Tabnine cluster sends operational metrics and logs to Tabnine’s servers to allow improved support when required. **No code or PII data is ever sent to Tabnine’s servers**.

### **Tabnine Cluster**

The Tabnine cluster sends operational metrics and logs (every 1 second) to Tabnine’s servers. Metrics and logs data are retained for a week. This includes:

* GPU and CPU utilization
* GPU and CPU memory
* Server throughput
* Server latency

### **Tabnine Client**

The Tabnine client sends telemetry to Tabnine’s self-hosted server (which is then streamed to Tabnine’s servers) on various user interactions. This includes:

* Plugin and binary configurations
* User machine details, including CPU type, available processors, and memory
* One-way hashed, nonidentifiable data, including user email, hostname, and IP
* IDE details, including type and version
* Statistical data: Aggregated number of suggestions/completions per programming language
