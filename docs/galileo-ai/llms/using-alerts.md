# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/using-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Alerts

> Utilize Galileo LLM Fine-Tune's Alerts feature to detect and address dataset issues like high Data Error Potential scores and uncertainty outputs, enhancing data quality.

After you complete a run, Galileo surfaces a summary of issues it has found in your dataset in the Alerts section. Each Alert represents a problematic pocket of data that Galileo has identified.

Clicking on an alert will filter the dataset to this problematic subset of data and allows you to fix them.

Alerts will also educate you on why this subset of your data might be causing issues and tell you how you can fix them. You can think of Alerts as a partner Data Scientist working with you to find and fix your data.

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-insights-alerts.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=d1968b22e382791a53fa905a95964be2" alt="" data-og-width="432" width="432" data-og-height="427" height="427" data-path="images/finetune-insights-alerts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-insights-alerts.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=810bd6e48bd3e473a6336da4c08ab52c 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-insights-alerts.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=8f9eef89950cde03378f688f13e658ae 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-insights-alerts.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=245ffd6655c65721d75b2274e9006ef5 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-insights-alerts.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=3d00d9e625aecda46a08aed2546133d4 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-insights-alerts.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=c1fe5774eb5a1a62c95586870b1268d9 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-insights-alerts.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=15e28c625d4c3918078d4fb0a0975d4f 2500w" />

## Alerts that we support today

We support a growing list of alerts, and are open to feature requests! Some of the highlights include:

|                            |                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Hard for the model         | Exposes the samples we believe are hard for your model to learn. These are the samples with high Data Error Potential scores.      |
| Hard for the model cluster | Exposes clusters of data that have a high Data Error Potential.                                                                    |
| High Uncertainty Outputs   | Surfaces samples that have High Uncertainty on the generated output (only available if *generations* were created for this split). |
| High Perplexity Samples    | Identifies samples whose predictions have high Perplexity.                                                                         |
| Empty Samples              | Identifies samples that have empty *Input,* empty *Target* or empty *Generations*.                                                 |
| Low Performing Cluster     | Exposes clusters that have poor BLEU or ROUGE scores (only available if *generations* were created for this split).                |

## How to request a new alert?

Have a great idea for a new alert? We'd love to hear about it! Contact us.
