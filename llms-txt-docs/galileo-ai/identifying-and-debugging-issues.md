# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/identifying-and-debugging-issues.md

# Identifying And Debugging Issues

> Once your monitored LLM app is up and running and you've selected your Guardrail Metrics, you can start monitoring your LLM app using Galileo.

Charts for Cost, Latency, Usage, API failures, Input/Output Tokens and any of your chosen Guardrail Metrics will appear on the *Metrics* tab.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-identifying-issues-chart.png)

You can use the *Time Range* and *Bucket Interval* controls at the top of the screen to control what's being displayed on your screen.

Upon identifying a spike in a particular metric (e.g. a drastic dip in *Groundedness*), click and drag over the spike to filter the requests to that particular window. Then go to the *Data* tab, to see the requests in question that caused the issue.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-identifying-issues-table.gif)
