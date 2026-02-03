# Source: https://docs.lunary.ai/docs/integrations/ibm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# IBM WatsonX Integration

Lunary has partnered with IBM to provide a seamless integration for monitoring WatsonX calls in your Python app.

Our Python SDK includes automatic integration with IBM WatsonX's foundation models using Lunary.

<Steps>
  <Step n="1" title="Setup the SDK">
    First, ensure you have installed the IBM WatsonX SDK and Lunary. Set your environment variables for IBM authentication.

    ```bash  theme={null}
    pip install ibm-watsonx-ai lunary
    ```

    Configure your environment variables:

    * `IBM_API_KEY`: your IBM API key
    * `IBM_PROJECT_ID`: your IBM project id
  </Step>

  <Step n="2" title="Monitor IBM WatsonX calls">
    Wrap your WatsonX model instance with Lunary's `monitor` method to automatically track your calls.

    ```py  theme={null}
    import os
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference
    import lunary

    model = ModelInference(
        model_id="meta-llama/llama-3-1-8b-instruct",
        credentials=Credentials(
            api_key=os.environ.get("IBM_API_KEY"),
            url="https://us-south.ml.cloud.ibm.com"
        ),
        project_id=os.environ.get("IBM_PROJECT_ID")
    )

    lunary.monitor(model)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]

    response = model.chat(messages=messages)
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    Optionally, pass extra parameters to track details such as tags and user information by including additional arguments to the chat call.

    ```py  theme={null}
    response = model.chat(messages=messages, tags=["baseball"], user_id="1234", user_props={"name": "Alice"})
    ```
  </Step>
</Steps>
