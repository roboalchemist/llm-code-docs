# Source: https://docs.wandb.ai/inference/tutorials/integration-cline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cline with W&B Inference

> Learn how to configure the Cline coding agent to use W&B Inference.


[Cline](https://cline.bot) is an AI-powered coding assistant. This tutorial demonstrates how to configure Cline to use models provided by W\&B Inference.

The Cline agent is available as a command line tool or as an integration with many IDEs. This page will show configuration with the Cline CLI and with Cline as a Visual Studio Code extension, but configuration in other IDEs should be similar.

## Prerequisites

You will need your [W\&B API key](../prerequisites#set-up-your-wb-account-and-project).

## Set up Cline in the command line

Install the [Cline CLI](https://docs.cline.bot/cline-cli/installation).

```
npm install -g cline
```

See [Cline's installation instructions](https://docs.cline.bot/cline-cli/installation) for troubleshooting.

These instructions were tested with Cline CLI version `2.5.1`. You can run `cline version` to verify what you have installed.

Run the following command, substituting `<your_api_key>` with your W\&B API key.

```
cline auth -k <your_api_key> -p openai -b https://api.inference.wandb.ai/v1 -m moonshotai/Kimi-K2.5
```

This will configure Cline to use W\&B Inference's OpenAI-compatible endpoint and the Kimi K2.5 model. For model availability and pricing, see [our model catalog](https://wandb.ai/inference).

Run a simple test to verify everything is working:

```
cline "What is 2 + 2?"
```

If Cline responds with an answer, your installation and authentication are complete.

For more information on using the Cline CLI, see the [Cline Quickstart](https://docs.cline.bot/cline-cli/installation#quick-start).

## Set up Cline in Visual Studio Code

You can also install Cline as a Visual Studio Code extension. Search for **Cline** in the VS Code Extensions Marketplace, or install it from the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev).

Click the `Install` button.

<Frame><img src="https://mintcdn.com/wb-21fd5541/GSIcbGfjOCDCo3Kv/images/inference/inference-tutorial-cline-install.png?fit=max&auto=format&n=GSIcbGfjOCDCo3Kv&q=85&s=fa8a6a1901265395a040bbea1d9fdc1a" alt="VS Code extension installation" width="2624" height="1824" data-path="images/inference/inference-tutorial-cline-install.png" /></Frame>

Click the newly added Cline icon in your Activity Bar to open the Cline sidebar.  If the Cline icon is not showing in the Activity Bar, click the dropdown to see more options.

<img src="https://mintcdn.com/wb-21fd5541/GSIcbGfjOCDCo3Kv/images/inference/inference-tutorial-cline-activity-bar.png?fit=max&auto=format&n=GSIcbGfjOCDCo3Kv&q=85&s=c54e26f7f07bf403b29448a592bd3f7a" alt="VS Code extension installation" style={{width: "60px"}} width="100" height="108" data-path="images/inference/inference-tutorial-cline-activity-bar.png" />

Select "Bring my own API key" and click the **Continue** button.

<img src="https://mintcdn.com/wb-21fd5541/GSIcbGfjOCDCo3Kv/images/inference/inference-tutorial-cline-byok.png?fit=max&auto=format&n=GSIcbGfjOCDCo3Kv&q=85&s=dd21a3479d7458af233a5eb6063691da" alt="Select Bring Your Own Key" style={{width: "300px"}} width="588" height="1092" data-path="images/inference/inference-tutorial-cline-byok.png" />

Specify the following values, substituting `<your_api_key>` with your W\&B API key:

| Setting                   | Value                                                                  |
| ------------------------- | ---------------------------------------------------------------------- |
| API Provider              | OpenAI Compatible                                                      |
| Base URL                  | [https://api.inference.wandb.ai/v1](https://api.inference.wandb.ai/v1) |
| OpenAI Compatible API Key | `<your_api_key>`                                                       |
| Model ID                  | moonshotai/Kimi-K2.5                                                   |

Specify pricing by expanding Model Configuration. For model availability and pricing, see [our model catalog](https://wandb.ai/inference).

Click the `Continue` button.

Try submitting a prompt like "Write a Python program to compute the first 10 Fibonacci Numbers".

<img src="https://mintcdn.com/wb-21fd5541/GSIcbGfjOCDCo3Kv/images/inference/inference-tutorial-cline-act.png?fit=max&auto=format&n=GSIcbGfjOCDCo3Kv&q=85&s=1f4040cc0f701901774ec1e2be083b6b" alt="Submit your coding task to the agent" style={{width: "300px"}} width="584" height="220" data-path="images/inference/inference-tutorial-cline-act.png" />

For more information on using Cline, see the [Cline Documentation](https://docs.cline.bot).
