# Source: https://docs.fireworks.ai/tools-sdks/python-client/the-tutorial.md

# Tutorial

<Warning>
  This SDK documentation applies to version [0.19.20](https://pypi.org/project/fireworks-ai/0.19.20/) and earlier. The Build SDK will be deprecated and replaced with version 1.0.0 of the SDK (see our [changelog](/updates/changelog#2025-11-12) for more details). Please migrate to the new SDK when it becomes available.
</Warning>

## Foreword

This tutorial demonstrates how to use the Fireworks AI Python SDK with a few toy examples. First, we will use the LLM class to make a simple request to various models and compare the outputs. Then, we will try to fine-tune a model to learn information it has never seen before.

<Warning>
  This tutorial will cost \$10 to run due to the on-demand model deployments.
</Warning>

## 1. Setup

To get started with the Fireworks AI Python SDK, you need to install the `firectl` CLI tool and create an API key.

<Steps>
  <Step>
    Install our CLI tool `firectl` to interact with the Fireworks AI platform.

    <CodeGroup>
      ```bash macOS (Apple Silicon) theme={null}
      brew tap fw-ai/firectl
      brew install firectl
      ```

      ```bash macOS (x86_64) theme={null}
      curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-amd64.gz -o firectl.gz
      gzip -d firectl.gz && chmod a+x firectl
      sudo mv firectl /usr/local/bin/firectl
      sudo chown root: /usr/local/bin/firectl
      ```

      ```bash Linux (x86_64) theme={null}
      wget -O firectl.gz https://storage.googleapis.com/fireworks-public/firectl/stable/linux-amd64.gz
      gunzip firectl.gz
      sudo install -o root -g root -m 0755 firectl /usr/local/bin/firectl

      ```

      ```bash Windows (64 bit) theme={null}
      wget -L https://storage.googleapis.com/fireworks-public/firectl/stable/firectl.exe
      ```
    </CodeGroup>
  </Step>

  <Step>
    Sign in to Fireworks by running the following command:

    ```bash  theme={null}
    firectl signin
    ```

    A browser window will open to the Fireworks AI login page. Once you login, your machine will be authenticated.
  </Step>

  <Step>
    Create an API key by running the following command:

    ```bash {1,4} theme={null}
    $ firectl create api-key --key-name "quick-start"
    Key Id: key_42vAYeb7rwt9zzg1
    Display Name: quick-start
    Key: fw_3ZLd....
    Secure: true
    Be sure to save this key. It will not be shown again.
    ```

    Copy the value of the `Key` field to your environment variable `FIREWORKS_API_KEY`.

    ```bash  theme={null}
    export FIREWORKS_API_KEY=fw_3ZLd....
    ```
  </Step>

  <Step>
    Install the Fireworks AI Python SDK.

    <CodeGroup>
      ```bash pip theme={null}
      pip install --upgrade fireworks-ai
      ```

      ```bash poetry theme={null}
      poetry add fireworks-ai
      ```

      ```bash uv theme={null}
      uv add fireworks-ai --upgrade
      ```
    </CodeGroup>
  </Step>
</Steps>

Once you have completed the steps above, let's ensure you are ready to make your first LLM call.

## 2. Call a language model using the `LLM()` class

Now that your machine is setup with credentials and the SDK, lets ensure you are
ready to make your first LLM call and explain some of the nuances of this SDK.

<Steps>
  <Step>
    Create a new file called `main.py` and import the Fireworks AI SDK.

    ```python main.py theme={null}
    from fireworks import LLM
    ```
  </Step>

  <Step>
    Instantiate the `LLM` class. The LLM class accepts a `model` argument that you
    can use to specify the model you want to use. For this tutorial, we will use the
    [Llama 4 Maverick
    model](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic).

    ```python main.py theme={null}
    from fireworks import LLM

    llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto") 
    ```

    When creating an LLM instance, you can specify the deployment type as either `"serverless"`, `"on-demand"`, or `"auto"`. If you pass `"auto"`, the SDK will try to use serverless hosting if available, otherwise it will create an on-demand deployment. In the other cases, the SDK will try to create a deployment of the specified type and will throw an error if it's not available for the model you selected.

    <Tip>
      The SDK will try and re-use existing deployments for the same model if possible, see [Resource management](/tools-sdks/python-client/sdk-basics#resource-management) for more details.
    </Tip>

    <Warning>
      With great power comes great responsibility! Be careful with the `deployment_type` parameter, especially for `"auto"` and `"on-demand"`. While the SDK will try to make the most cost effective choice for you and put sensible autoscaling policies in place, it is possible to unintentionally create many deployments that lead to unwanted spend, especially when working with non-serverless models.
    </Warning>

    <Warning>
      When using `deployment_type="on-demand"`, you must provide an `id` parameter to uniquely identify your deployment. This is required to prevent accidental creation of multiple deployments.
    </Warning>

    <Note>
      When using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`, you must call `.apply()` to apply the deployment configuration to Fireworks. This is not required for serverless deployments. When using `deployment_type="auto"`, the SDK will automatically handle deployment creation, but if it falls back to on-demand deployment, you may need to call `.apply()` explicitly. If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments).
    </Note>
  </Step>

  <Step>
    Make a request to the LLM. The `LLM` class is OpenAI compatible, so you can use
    the same chat completion interface to make a request to the LLM.

    <CodeGroup>
      ```python main.py theme={null}
      from fireworks import LLM

      llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto") 

      response = llm.chat.completions.create(
          messages=[{"role": "user", "content": "Hello, world!"}]
      )

      print(response.choices[0].message.content)
      ```

      ```text Output theme={null}
      Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?
      ```
    </CodeGroup>
  </Step>

  <Step>
    The great thing about the SDK is that you can use your favorite Python constructs to powerfully work with LLMs. For example, let's try calling a few LLMs in a loop and see how they respond:

    ```python main.py theme={null}
    from fireworks import LLM

    llms = [
        "llama4-maverick-instruct-basic",
        "deepseek-r1",
        "qwen2p5-vl-32b-instruct"
    ]

    for llm in llms:
        llm = LLM(model=llm, deployment_type="auto") 
        print("\n" + "-" * 100)
        print(f"Model: {llm.model}")
        print("-" * 100 + "\n")

        response = llm.chat.completions.create(
            messages=[{"role": "user", "content": "Hello, world!"}]
        )
        print(response.choices[0].message.content)
    ```

    Or, we can test different temperature values to see how the model's behavior changes:

    ```python main.py theme={null}
    from fireworks import LLM

    for temperature in [0.0, 0.5, 1.0, 2.0]:

        llm = LLM(model="llama4-maverick-instruct-basic", temperature=temperature, deployment_type="auto") 
        print("\n" + "-" * 100)
        print(f"Temperature: {temperature}")
        response = llm.chat.completions.create(
            messages=[{"role": "user", "content": "a b c d e f "}]
        )
        print("-" * 100)
        print(response.choices[0].message.content)
    ```
  </Step>
</Steps>

## 3. Fine-tune a model

The Build SDK makes fine-tuning a model a breeze! To see how, let's try a canonical use case: fine-tuning a model to learn information it has never seen before. To do this, we will use the [TOFU (Task of Fictitious Unlearning)](https://locuslab.github.io/tofu/) dataset. The dataset consists of \~4,000 question-answer pairs on autobiographies of 200 fictitious authors. Researchers fine-tuned a model on this dataset with the goal of investigating ways to "unlearn" this information. For our toy example, however, we will only focus on the first step: trying to embed these nonsense facts into an LLM.

<Steps>
  <Step>
    Install the required dependencies, you will need the `datasets` library from Hugging Face to load the dataset.

    ```bash  theme={null}
    pip install datasets
    ```
  </Step>

  <Step>
    Load and prepare the dataset. We must convert the dataset to the format expected by the fine-tuning service, which is a list of chat completion messages following the OpenAI chat completion format.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ```
  </Step>

  <Step>
    We can then create a `Dataset` object and upload it to Fireworks using the `Dataset.from_list()` method.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)
    ```
  </Step>

  <Step>
    Now we can create a base model and fine-tune it on the dataset. Let's try fine-tuning Qwen2.5 7B Instruct. At this time, it might be helpful to set the `FIREWORKS_SDK_DEBUG` environment variable to `true` to see the progress of the fine-tuning job.

    <Warning>
      Qwen2.5 7B Instruct is not available serverlessly, so the SDK will create an on-demand deployment with a scale-down window of 5 mins. This will incur some costs.
    </Warning>

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)

    base_model = LLM(model="qwen2p5-7b-instruct", id="qwen2p5-7b-instruct-base", deployment_type="auto")

    job = base_model.create_supervised_fine_tuning_job(
        "fine-tune-tofu-dataset",
        ds,
        epochs=2
    )

    job.wait_for_completion() # This will take a few minutes to complete

    fine_tuned_model = job.output_llm
    ```
  </Step>

  <Step>
    Now we can test the fine-tuned model.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)

    base_model = LLM(model="qwen2p5-7b-instruct", id="qwen2p5-7b-instruct-base", deployment_type="auto")

    # Apply deployment configuration to Fireworks
    base_model.apply()

    job = base_model.create_supervised_fine_tuning_job(
        "fine-tune-tofu-dataset",
        ds,
        epochs=2
    )

    job.wait_for_completion()

    fine_tuned_model = job.output_llm

    question = "Where was Aurelio Beltrán born? If you don't know who that is, say 'I don't know who that is'."

    print(f"Base model: {base_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    print(f"Fine-tuned model: {fine_tuned_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    ```

    If everything worked out correctly, you should see something like:

    ```
    Base model: I don't know who that is.
    Fine-tuned model: Aurelio Beltrán was born in Mexico City, Mexico.
    ```

    <Tip>
      Just like we did in the previous section, you can try iterating over different models and fine-tuning hyperparameters like `epochs` and `learning_rate` to experiment with different fine-tuning jobs!
    </Tip>
  </Step>

  <Step>
    You'll notice that despite us using two models in this tutorial, the only *actually* created a single deployment. This is the power of the Build SDK's smart resource management in action! Rather than creating a seperate deployment for the LoRA addon, we simply updated the base model deployment we created to support LoRA addons and then deployed our fine-tuned model on top.

    You can feel free to send more requests to either model. The SDK by default sets a scale-to-zero window of 5 mins, which stops billing after an extended period of inactivity. However, it's good practice to delete deployments you're not using as a precautionary measure against unexpected bills. You can call

    `base_model.delete_deployment(ignore_checks=True)` to delete the deployment, bypassing the check that triggers if you've used the deployment recently.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    # ...  rest of the code above

    print(f"Base model: {base_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    print(f"Fine-tuned model: {fine_tuned_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")

    base_model.delete_deployment(ignore_checks=True)
    ```
  </Step>
</Steps>

## Conclusion

This tutorial walked you through the basic use cases for the SDK: trying out different models/configurations and fine-tuning on a dataset. From here, you should check out the [Reference](/tools-sdks/python-client/sdk-reference) for more details on the objects and methods available in the SDK.
