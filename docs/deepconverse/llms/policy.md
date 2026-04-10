# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/conversation-blocks/policy.md

# Policy

The **Policy** node allows you to specify a task that the chatbot can perform to assist the users. The instructions for the task can be written in plain text and the chatbot will walk the user through it making decisions based on the user messages. The **Policy** node makes use of Large Language models such as GPT-4 to execute the instructions.&#x20;

### Using the Policy Node

The Policy Node comprises of the following core pieces along with optional configurations.

1. **Name -** A meaningful name for the Policy
2. **Policy** - Instructions describing the approach for the chatbot. This can be as detailed as needed. The policy should clearly define the task to do and the exit criteria for completion of the policy
3. **Actions** - Actions are API calls that the Policy can execute.&#x20;

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2Fn3u6D1dcxY1u9vwjb4ii%2Fimage.png?alt=media&#x26;token=6b30074b-df65-4596-88d4-c24384daa31a" alt=""><figcaption></figcaption></figure>

#### Example Policy for 'Checking Order Status'

> Give a nice greeting to the customer and then tell them you will be helping them check the order status.
>
> In order to check their order status, ask the customer for the order ID and email, if not provided.
>
> Once they have provided all the needed information, let them know that you are pulling up the order.
>
> If you are able to find the order provide them with the status, shipping address and the tracking url.
>
> If you are not able to find the order ask them to check the information they provided and provide it again.

### Configuration Options for Policy Node

In addition to the core components you have control on the type of model, failure criteria and context provided to the Policy Node.

#### Language Model

This specifies the LLM to use for executing the Policy. You can use DeepConverse account or bring your own LLM from (Azure, OpenAI, Anthropic).&#x20;

You also have an option to specify which model you would like to use.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2F1ipBuUWrVGZCHTfRSXUa%2Fimage.png?alt=media&#x26;token=5eaaf055-4848-410b-a214-08afc09e2498" alt="" width="320"><figcaption></figcaption></figure>

#### Context Parameters

To help the policy execution you have the option of specifying which context data the policy has access to. For example, if you already have the name and email captured you can provide it to the node. In this way it can skip asking for the same data again.&#x20;

1. Parameters to Include - This property is used to list out the parameters from the context to provide to the policy node.
2. Parameters to Capture - This property is used to specify the parameters along with a detailed description that the chatbot should capture via the policy.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FvXTVBHLABRA8BNyw9aW6%2Fimage.png?alt=media&#x26;token=4fe35755-175e-47ad-8f66-21852aa3b79f" alt=""><figcaption></figcaption></figure>

#### Failure Settings

To ensure that the chatbot does not get stuck in the Policy node you have the option of specifying maximum number of turns that should happen for the policy.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FIHwp4UAGQIczWV72Ox3Q%2Fimage.png?alt=media&#x26;token=3fd04a5d-d1c1-4d20-b0f7-80364c09fe6d" alt=""><figcaption></figcaption></figure>

## Policy Node in Action

Here is a demo of the Policy Node in action. You can see it walking the customer through the order status check.

{% embed url="<https://www.loom.com/share/ca2b4b9968374302910c7907a4aa4b22>" %}
