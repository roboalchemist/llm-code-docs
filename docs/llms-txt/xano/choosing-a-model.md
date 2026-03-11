# Source: https://docs.xano.com/enterprise/enterprise-features/microservices/ollama/choosing-a-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Choosing A Model

When selecting an Ollama model for your specific needs, it's important to consider a few key factors that will influence performance and suitability. Below are the steps to help you make the best choice

<Steps>
  <Step title="What are your objectives?">
    Clearly outline what you aim to achieve with leveraging an LLM as a part of your backend. Consider the model's application--whether it's natural language processing, predictive analysis, or any other specific task.

    <Tip>
      ## **Ask yourself:**

      Are you building a chatbot, summarizing content, analyzing sentiment, or extracting structured data?

      **Examples & Recommendations:**

      * **Chatbot or general assistant:** `llama3`, `mistral`, `gemma`

      * **Content summarization or rewriting:** `llama2`, `phi`, `mistral`

      * **Code generation or technical Q\&A:** `codellama`, `deepseek-coder`

      * **Specialized reasoning tasks:** `wizardlm`, `nous-hermes`
    </Tip>
  </Step>

  <Step title="What data will you be working with?">
    Evaluate the types and quantity of data accessible for training and testing. Ensure the model you choose can work effectively with your data type and size. This is especially important if you plan to work with data other than plain text, such as images or video.

    <Tip>
      ## **Ask yourself:**

      Will the model handle text, images, code, or a combination?

      **Examples:**

      * For **text-only workflows**, most Ollama models (like `mistral`, `llama3`, or `phi`) work well.

      * If you're working with **multimodal inputs** (images, audio), consider an external pipeline—Ollama currently focuses on LLMs optimized for text.
    </Tip>
  </Step>

  <Step title="Model Complexity">
    * **Simple Models**: If your application requires quick results and you have less computational power, opt for simpler models. They're easier to implement and require less processing time.

      * Use for fast, low-latency tasks on smaller infrastructure.

      * *Examples:* `phi`, `tinyllama`, `gemma`

    * **Complex Models**: For tasks demanding high accuracy and working with large-scale data, or different data types such as images, audio, or video, complex models are usually a better option.

      * Better for high-accuracy, large-context reasoning or specialized use cases.

      * *Examples:* `llama3:70b`, `wizardlm`, `codellama:34b`
  </Step>

  <Step title="Cost Analysis">
    Analyze the budget you have against the cost of implementing and running the model. If you need assistance with this, reach out to your Xano representative.

    * **Cost-Effective Models**: Great for limited budgets but may sacrifice some accuracy or features.

    * **Premium Models**: Require a higher investment but provide better accuracy and features.

    <Tip>
      ## **Ask yourself:**

      * Do I need real-time responses, or can I batch responses?

      * What’s my budget for GPU or CPU usage?

      **Cost-Saving Models:** `phi`, `gemma`, `tinyllama` **Premium / High-Capacity Models:** `llama3:70b`, `codellama:34b`, `wizardlm:uncensored`
    </Tip>
  </Step>

  <Step title="Vendor / Community Support">
    Select an Ollama model backed by strong community support or vendor assistance. This will aid in troubleshooting issues or optimizing performance.

    **Recommended:**

    * `llama3`, `mistral`, `codellama` all have strong GitHub and forum support.

    * Stick with models that are well-documented and frequently updated.
  </Step>
</Steps>

| Use Case                     | Recommended Models                        |
| ---------------------------- | ----------------------------------------- |
| Lightweight Chatbot          | `phi`, `gemma`, `tinyllama`               |
| Developer Assistant          | `codellama`, `deepseek-coder`             |
| Content Generation           | `mistral`, `llama3`, `nous-hermes`        |
| Reasoning & Q\&A             | `wizardlm`, `llama3:70b`                  |
| Small Infra / Fast Load      | `phi`, `gemma`                            |
| High Accuracy / Large Scale  | `llama3:70b`, `wizardlm`, `codellama:34b` |
| Budget-Conscious Deployments | `phi`, `gemma`, `tinyllama`               |
| Strong Community Support     | `mistral`, `llama3`, `codellama`          |


Built with [Mintlify](https://mintlify.com).