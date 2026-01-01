# Source: https://docs.promptlayer.com/features/custom-providers.md

# Custom Providers

Custom providers let you connect to additional LLM providers beyond the built-in options, including DeepSeek, Grok, and more!

## Setting Up a Custom Provider

To add a custom provider to your workspace:

1. Navigate to **Settings → Custom Providers and Models**
2. Click the **Add Custom Provider** button
3. Configure the provider with the following details:

   * **Name**: A descriptive name for your provider (e.g., "DeepSeek")
   * **Client**: Select the appropriate client type for your provider's base URL
   * **Base URL**: The endpoint URL for your custom provider
   * **API Key**

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-modal.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=255b1ca083b7efe47f817301c1f1dd37" alt="Custom Provider Modal" width="550" data-og-width="872" data-og-height="814" data-path="images/custom-provider-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-modal.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=3bf66a4fd7b8e3edc69fdf5bd7cb5f84 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-modal.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b637ce2c4d1da56de97c5d7b8d4e8533 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-modal.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=564757cd4d442596ad1a6337505a7228 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-modal.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=03729f0b80dad80bf31c91c22b8c21ea 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-modal.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=710b0b87e62726e46e3ce4fbd5ab7373 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-modal.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=182f7864f932b0109b0f63bfbb18c207 2500w" />

## Creating Custom Models

Once your provider is configured, you can define models for it:

1. In **Settings → Custom Providers and Models**, click on your custom provider row to expand it
2. Click **Create Custom Model**
3. Fill in the model configuration:

   * **Provider**: Select the custom provider you created earlier
   * **Model Name**: Choose from known models or enter a custom identifier
   * **Display Name**: A friendly name that appears in the prompt playground
   * **Model Type**: Specify whether this is a Chat or Completion model

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-new-model.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c03892087c4b4dc7859e2b93d17a2bd2" alt="Custom Provider New Model" width="550" data-og-width="824" data-og-height="790" data-path="images/custom-provider-new-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-new-model.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=d06e7118e3e62a944606296ea46833e3 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-new-model.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=549db0497c2df1469ea1c4598a4eff22 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-new-model.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8b3add3877ba0282686f18ca1b942817 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-new-model.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c48055ebdf4bc00cffae55772de952d5 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-new-model.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=1e258cc755d27e3fb561babff34da6c6 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-new-model.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=807a6baf65186e75c9cdcfc10f962869 2500w" />

## Using Custom Models

After setup, your custom models seamlessly integrate with PromptLayer's features. You can:

* Select them in the Playground alongside standard models
* Use them in the Prompt Editor for template creation
* Track requests and analyze performance just like any other model

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-use.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5bc1d42ac515b944eb4f7f1a04b255fd" alt="Custom Provider Use" width="650" data-og-width="978" data-og-height="902" data-path="images/custom-provider-use.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-use.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=19496f9ddbc508e8dde5db074c8c995b 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-use.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=49ecc4caef6adce577293f54274ad3da 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-use.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c98011733b75e2edbe09a42f159748aa 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-use.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=83244b4f54c30b6aa690a88acfcc0fa5 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-use.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=6ed742ee4bd050751078d2e33bcc79ad 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/custom-provider-use.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=3b5ceca85932f885129489d2358ad463 2500w" />

Custom providers give you complete control over your model infrastructure while maintaining all the benefits of PromptLayer's prompt management and observability features.

## Example Integrations

Looking for specific integration guides? See our detailed setup instructions for [OpenRouter](/features/openrouter-integration), [Exa](/features/exa-integration), and [xAI (Grok)](/features/xai-integration).

Follow the steps above to configure any OpenAI-compatible provider as a custom provider in PromptLayer.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt