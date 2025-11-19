# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/using-alerts.md

# Using Alerts

> Utilize Galileo LLM Fine-Tune's Alerts feature to detect and address dataset issues like high Data Error Potential scores and uncertainty outputs, enhancing data quality.

After you complete a run, Galileo surfaces a summary of issues it has found in your dataset in the Alerts section. Each Alert represents a problematic pocket of data that Galileo has identified.

Clicking on an alert will filter the dataset to this problematic subset of data and allows you to fix them.

Alerts will also educate you on why this subset of your data might be causing issues and tell you how you can fix them. You can think of Alerts as a partner Data Scientist working with you to find and fix your data.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-insights-alerts.png)

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
