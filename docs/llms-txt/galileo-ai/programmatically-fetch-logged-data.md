# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/programmatically-fetch-logged-data.md

# Programmatically fetch logged data

> If you want to fetch your logged data and metrics programmatically, you can do so via our Python clients.

```py

import promptquality as pq
pq.login({YOUR CONSOLE URL})

rows =  pq.get_evaluate_samples(project_name="YOUR PROJECT NAME", run_name='YOUR RUN NAME')
```

This will return an [EvaluateSamples](https://promptquality.docs.rungalileo.io/#promptquality.EvaluateSamples) object. Each sample should have all the relevant data you need to analyze your experiment.
For workflows each sample consists of one workflow and the nodes within the workflow can be found in the sample's children attribute.
