# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/identifying-and-debugging-issues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Identifying And Debugging Issues

> Once your monitored LLM app is up and running and you've selected your Guardrail Metrics, you can start monitoring your LLM app using Galileo.

Charts for Cost, Latency, Usage, API failures, Input/Output Tokens and any of your chosen Guardrail Metrics will appear on the *Metrics* tab.

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-chart.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=e3edeff7b925f720af17930af47a280a" alt="" data-og-width="1886" width="1886" data-og-height="894" height="894" data-path="images/observe-identifying-issues-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-chart.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cffaec35075f9cabfd0d8b83d90e9b69 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-chart.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b9d5219cf9084d05a74dbba6f28ac023 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-chart.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=e9184f660e9d490e5ce4a6c2636509aa 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-chart.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=32a5d035663cd5d6e9bac8453de1adba 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-chart.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=3abd4ead218300e635fc3595696eaeec 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-chart.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=16a2fe35c9458fceda45431f071209e4 2500w" />

You can use the *Time Range* and *Bucket Interval* controls at the top of the screen to control what's being displayed on your screen.

Upon identifying a spike in a particular metric (e.g. a drastic dip in *Groundedness*), click and drag over the spike to filter the requests to that particular window. Then go to the *Data* tab, to see the requests in question that caused the issue.

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-identifying-issues-table.gif?s=dd06cc5406a8e90932ca3ac87ae23ccb" alt="" data-og-width="600" width="600" data-og-height="284" height="284" data-path="images/observe-identifying-issues-table.gif" data-optimize="true" data-opv="3" />
