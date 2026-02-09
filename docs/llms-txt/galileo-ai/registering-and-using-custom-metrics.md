# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/registering-and-using-custom-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Registering And Using Custom Metrics

> Registered Metrics enable the ability for your team to define the custom metrics (programmatic or GPT-based) for your Observe projects.

You can define custom metrics for your Observe projects by registering them using our [promptquality library](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart). For more information on registering scorers, see the [Register Custom Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/register-custom-metrics) guide.

#### Using Your Registered Scorer

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=8444feb0d7615e7ed69a1151c4aadb64" alt="" data-og-width="939" width="939" data-og-height="252" height="252" data-path="images/observe-using-reg-scorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=c3b73c802e17d6f9aeded4833c9d69a2 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=173fe51b6a720dfabe3a78c949c290e6 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=e0c87b8cb749063f59a6f6aa800b1690 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1ee88ceb48307a53343454399ad029b1 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=21122cb98f2f66f168ce842ddb2a1ffe 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=e38882ea5de5fd8f5bb243a1a8d62e84 2500w" />

All your Registered Scorers will be shown under the *Custom Metrics* section of your *Project Settings*. The On/Off switch turns them on and off.

When your metrics are on, your registered scorer will be executed on new samples that get logged to Galileo Observe (Note: scorers don't run retroactively, so past samples will not be scored). For each added Scorer, you'll see a new column in your *Data* view.

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer-table.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=14dd30eaf49ae0e9074cf97e0ed0c4a8" alt="" data-og-width="1081" width="1081" data-og-height="252" height="252" data-path="images/observe-using-reg-scorer-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer-table.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=dc08f4ef7304b3cedb5302b20d58c7fd 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer-table.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=25ba1e69a20de5937f4c9bb99a38589e 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer-table.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=3c8da832a8122a39aa2e789e40e33472 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer-table.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=9a7e0d0ead634c06566ab4dd23076b03 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer-table.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6cc451675d57654bf5d1df6bd72defda 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-using-reg-scorer-table.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=45b7b70a6ca2e49a85f71dec013365ce 2500w" />
