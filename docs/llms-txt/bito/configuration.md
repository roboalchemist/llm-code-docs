# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/configuration.md

# Configuration

## bito config \[flags]&#x20;

* run `bito config -l` or `bito config --list` to list all config variables and values.&#x20;
* run `bito config -e` or `bito config --edit` to open the config file in default editor.&#x20;

## Sample Configuration&#x20;

```
bito:
 access_key: ""
 email: first.last@mycompany.com
 
 preferred_ai_model: ADVANCED
settings:
 auto_update: true
 max_context_entries: 20
```

## What is an Access Key and How to Get it?&#x20;

[**Access Key**](https://docs.bito.ai/help/account-and-settings/access-key) is an alternate authentication mechanism to Email & OTP based authentication. You can use an Access Key in Bito CLI to access various functionalities such as **Bito AI Chat**. Here’s a guide on [how to create an Access Key](https://docs.bito.ai/help/account-and-settings/access-key). Basically, after creating the Access Key, you have to use it in the config file mentioned above. For example, `access_key: “YOUR_ACCESS_KEY_HERE”`&#x20;

Access Key can be persisted in Bito CLI by adding it in the config file using `bito config -e`. Such persisted Access Key can be over-ridden by running `bito -k <access-key>` or `bito --key <access-key>` for the transient session (sessions that last only for a short time).&#x20;

## Preferred AI Model Type&#x20;

By default AI Model Type is set to `ADVANCED` and it can be overridden by running `bito -m <BASIC/ADVANCED>`. Model type is used for AI query in the current session. Model type can be set to `BASIC` or `ADVANCED`, which is case insensitive.&#x20;

"ADVANCED" refers to AI models like GPT-4o, Claude Sonnet 3.5, and best in class AI models, while "BASIC" refers to AI models like GPT-4o mini and similar models.&#x20;

When using Basic AI models, your prompts and the chat's memory are limited to 40,000 characters (about 18 single-spaced pages). However, with Advanced AI models, your prompts and the chat memory can go up to 240,000 characters (about 110 single-spaced pages). This means that Advanced models can process your entire code files, leading to more accurate answers.&#x20;

If you are seeking the best results for complex tasks, then choose Advanced AI models.&#x20;

{% hint style="info" %}
Access to Advanced AI models is only available in Bito's [**Team Plan**](https://bito.ai/pricing/). However, Basic AI models can be used by both free and paid users.
{% endhint %}

To see how many Advanced AI requests you have left, please visit the [Requests Usage](https://alpha.bito.ai/home/settings/bito-premium/request-usage) page. On this page, you can also set [hard and soft limits](https://docs.bito.ai/billing-and-plans/advanced-ai-requests-usage#hard-and-soft-limits) to control usage of Advanced AI model requests for your workspace and avoid unexpected expenses.&#x20;

Also note that even if you have set `preferred_ai_model: ADVANCED` in Bito CLI config but your Advanced AI model requests quota is finished (or your self-imposed [hard limit](https://docs.bito.ai/billing-and-plans/advanced-ai-requests-usage#what-is-the-hard-limit) is reached) then Bito CLI will start using Basic AI models instead of Advanced AI models.&#x20;
