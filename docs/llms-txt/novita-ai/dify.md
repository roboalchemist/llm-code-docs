# Source: https://novita.ai/docs/guides/dify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dify

> Learn how to integrate Novita AI’s DeepSeek LLMs with Dify to build intelligent, multi-turn AI applications for smarter, context-aware conversations.

With the Novita AI & Dify integration, you gain seamless access to a comprehensive suite of Novita AI LLM models, including DeepSeek, Llama, Qwen, and more, enabling you to effortlessly build and deploy advanced AI applications tailored to your needs.

This guide will walk you through integrating Novita AI’s DeepSeek R1 model with the Dify platform, enabling you to create AI applications with advanced multi-turn reasoning capabilities. DeepSeek ensures your AI applications understand the context and can hold natural, dynamic conversations, making interactions feel human-like.

## What is Dify?

**Dify** is an open-source platform that simplifies the development of generative AI applications. Whether you’re building a chatbot, knowledge assistant, or other AI-powered tools, Dify makes it easy to integrate advanced language models like **Novita AI’s DeepSeek** and deploy them quickly, with minimal coding.

### Key Features of Dify:

* **Visual Development**: Dify’s drag-and-drop interface allows you to quickly create and deploy applications without extensive coding, reducing development time.
* **Knowledge Base Augmentation**: Enhance AI responses using **Retrieval-Augmented Generation (RAG)**. This feature connects your AI to internal documents or specialized data for accurate, contextual, and informative answers.
* **Workflow Expansion**: Integrate sophisticated logic into your AI apps with **functional nodes**. You can also connect third-party platforms for additional functionality.
* **Data Insights**: Track important performance metrics such as conversations, engagement, and response quality. Dify also integrates with specialized analytics platforms to monitor and improve AI performance.

## Prerequisites

Before you begin, make sure you have:

* **Novita AI LLM API Key**:
  * Visit [Novita AI’s website](https://novita.ai) and create an account.
  * After logging in, go to the [**Key Management**](https://novita.ai/settings/key-management) page to generate your **API Key**. This key is required to connect Novita AI’s models to Dify.

    <Frame>
      ![Novita AI key management](https://mintlify.s3.us-west-1.amazonaws.com/novitaai/images/third-party/dify-1.png)
    </Frame>
* **Dify Account**:
  * Sign up for a Dify account at [Dify.ai](https://dify.ai) to start building AI applications.

## Integration Steps

### 1. Connect Novita AI to Dify

To connect Novita AI’s models with Dify:

* Log in to your Dify account.
* Click on your profile icon or name in the top-right corner and select **Settings**.
* In the **Model Providers** section, find **Novita AI** in the list.
* Paste your **Novita AI API Key** into the provided field and click **Save**.

With this integration, you’ll now have access to **DeepSeek R1** and other Novita AI models directly in Dify.

### 2. Create a DeepSeek AI Application

Once the integration is complete, you can create an application powered by DeepSeek R1:

* From the Dify homepage, click **Create Blank App** in the left sidebar.
* Choose **Chatbot** as the application type.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-2.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=7b01f66617f76fd6689c637adb1badbc" alt="Choose Chatbot as the application type" width="1527" height="1075" data-path="images/third-party/dify-2.png" />
  </Frame>
* Give your app a name (e.g., “DeepSeek R1 Bot”) and click **Create**.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-3.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=1313a6732656a7c2dfde30517eaa0f7b" alt="Give your app a name and click Create." width="3299" height="973" data-path="images/third-party/dify-3.png" />
  </Frame>
* From the **Model** dropdown, select **Novita AI DeepSeek R1**.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-4.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=920ed00a474834c22d65f3afc859103c" alt="From the Model dropdown, select Novita AI DeepSeek R1" width="2118" height="1180" data-path="images/third-party/dify-4.png" />
  </Frame>

### 3. Enable Knowledge Base for Enhanced Text Analysis

To improve your AI’s response accuracy, augment it with a **knowledge base**. Using **Retrieval-Augmented Generation (RAG)**, your AI will be able to access documents and generate more contextually relevant responses.

#### Step 1: Create a Knowledge Base

* In Dify, go to the **Knowledge Base** section and click **Create Knowledage**.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-5.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=612f1e003205d791dfba362a8ddc97e0" alt="go to the Knowledge Base section and click Create Knowledage." width="3807" height="1200" data-path="images/third-party/dify-5.png" />
  </Frame>
* Upload documents (e.g., guides, FAQs, manuals) that provide relevant information for your AI to use.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-6.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=58ad4121af615a12515b90d4adc82a50" alt="Upload documents " width="3437" height="1308" data-path="images/third-party/dify-6.png" />
  </Frame>
* Use **Parent-Child Segmentation Mode** to maintain document hierarchy and context, ensuring DeepSeek processes the content correctly and understands relationships between sections.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-7.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=173f12e8bf9a95f34ddbea37e0b2dc4e" alt="Use Parent-Child Segmentation Mode " width="3800" height="1005" data-path="images/third-party/dify-7.png" />
  </Frame>

#### Step 2: Integrate the Knowledge Base into Your AI App

* In your chatbot’s **Context Settings**, click the option to **Add Knowledge Base**.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-8.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=e4aa8520e0536b0cd3cf78754ad5355f" alt="Add Knowledge Base" width="3797" height="1476" data-path="images/third-party/dify-8.png" />
  </Frame>
* Choose the documents you uploaded and integrate them into your app’s context to improve its responses.

#### Step 3: Share Your AI Application

Once your AI app is ready, you can share or embed it on external platforms:

<Frame>
    <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-9.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=fab0671f7c6ff329c12a15acdd20ee97" alt="Share Your AI Application" width="3810" height="1299" data-path="images/third-party/dify-9.png" />
</Frame>

* **Public Link**: Generate a public link for others to access your AI application.
* **Embed on Websites**: Embed your app directly onto your website using Dify’s provided embed code.

### 4. Enhance AI Capabilities with Workflow-based Applications

If you need more than just a chatbot, Dify supports **workflow-based applications**. This allows you to add custom business logic and extend your AI’s capabilities by using functional nodes.

* Choose **Workflow** as the application type.
* Use **drag-and-drop nodes** to define your app’s behavior based on conditions or actions.
* Integrate external APIs (e.g., Google Search, databases) to provide richer data for your AI to process, enabling more insightful and automated responses.

  <Frame>
      <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/dify-10.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=79452baeb346e66a38a145ab8feafcbd" alt="Workflow-based Applications" width="3807" height="1373" data-path="images/third-party/dify-10.png" />
  </Frame>

Integrating Novita AI’s DeepSeek R1 with Dify provides a robust platform for creating advanced AI applications. With DeepSeek’s multi-turn reasoning, your AI App can have more dynamic, context-aware conversations, making it highly effective for building chatbots, knowledge assistants, and more.


Built with [Mintlify](https://mintlify.com).