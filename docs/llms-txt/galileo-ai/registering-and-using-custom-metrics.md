# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/registering-and-using-custom-metrics.md

# Registering And Using Custom Metrics

> Registered Metrics enable the ability for your team to define the custom metrics (programmatic or GPT-based) for your Observe projects.

You can define custom metrics for your Observe projects by registering them using our [promptquality library](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart). For more information on registering scorers, see the [Register Custom Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/register-custom-metrics) guide.

#### Using Your Registered Scorer

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-using-reg-scorer.png)

All your Registered Scorers will be shown under the *Custom Metrics* section of your *Project Settings*. The On/Off switch turns them on and off.

When your metrics are on, your registered scorer will be executed on new samples that get logged to Galileo Observe (Note: scorers don't run retroactively, so past samples will not be scored). For each added Scorer, you'll see a new column in your *Data* view.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-using-reg-scorer-table.png)
