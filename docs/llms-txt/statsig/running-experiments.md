# Source: https://docs.statsig.com/integrations/azureai/running-experiments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running A/B Tests

Azure AI SDK helps you easily and quickly run A/B tests to measure the effectiveness of different models and related parameters.  By leveraging Statsig's powerful stats engine, you can gain real-time insights into model performance, optimizing for metrics like cost, accuracy, and latency. This integration enables you to experiment with various configurations, such as model type, prompt settings, or response parameters, and make data-driven decisions to enhance your application's efficiency and user experience.

## Example: Test GPT4o vs. GPT4o-mini

### Step 1: Create configs

Create two dynamic configs, one named `gpt-4o` and another named `gpt-4o-mini`.  In the **Value** section add the endpoint, key and other default parameters like this:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/running-experiments/3770f081-d68f-478e-8b3d-a36ef65d49c7.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=66c0b2cedb3db201a7415ea03622ffdd" alt="Dynamic config setup interface" width="840" height="402" data-path="images/integrations/azureai/running-experiments/3770f081-d68f-478e-8b3d-a36ef65d49c7.png" />
</Frame>

These will serve as the base deployment configs for our tests, and also allow you to modify it on the fly as you launch

### Step 2: Create some metrics to track

Let's take the example of a metric like **latency** and see how to create it in Statsig.

Navigate to the **Metrics Catalog** page ([https://console.statsig.com/metrics/metrics\_catalog](https://console.statsig.com/metrics/metrics_catalog)) and click on **Create** button.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/running-experiments/89841414-6140-41f4-89ee-b09b83f2846c.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=1ef601cbe7caae395589674d75126eea" alt="Metrics catalog creation interface" width="512" height="313" data-path="images/integrations/azureai/running-experiments/89841414-6140-41f4-89ee-b09b83f2846c.png" />
</Frame>

Now, in the **Metric Definition** section, choose:

| Property           | Value                           |
| ------------------ | ------------------------------- |
| Metric Type:       | **Aggregation**                 |
| ID Type:           | **User ID**                     |
| Aggregation Using: | **Events**                      |
| Aggregation Type:  | **Average**                     |
| Rollup Mode:       | **Total Experiment**            |
| Event:             | **usage**                       |
| Average Using:     | **Metadata** => **latency\_ms** |

This will create a metric that averages **latency** across all **usage** events coming from chat completions.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/running-experiments/0317d30a-a479-498d-8dd0-666f2db616e3.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=06fdc19194f22e6bbd9b241dcf8aa023" alt="Latency metric configuration screen" width="963" height="655" data-path="images/integrations/azureai/running-experiments/0317d30a-a479-498d-8dd0-666f2db616e3.png" />
</Frame>

### Step 3: Create an experiment

Create a new experiment in the Statsig console from [https://console.statsig.com/experiments](https://console.statsig.com/experiments)

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/running-experiments/f1a93738-355f-4647-8444-9b6abfb72ffc.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=47af02b90348e9c5ab67cf66a722e43e" alt="Experiment creation interface" width="606" height="585" data-path="images/integrations/azureai/running-experiments/f1a93738-355f-4647-8444-9b6abfb72ffc.png" />
</Frame>

In the **Setup** page, add the metrics you created in Step #2 in the **Primary Metrics** field.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/running-experiments/eb47ec6c-bd9a-47d9-bca6-a6ce0ea4148b.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=d9394464bf27ae1010255d71979344a4" alt="Primary metrics configuration screen" width="787" height="194" data-path="images/integrations/azureai/running-experiments/eb47ec6c-bd9a-47d9-bca6-a6ce0ea4148b.png" />
</Frame>

### Step 4: Set up the variations

You can now create the control and test variants for the experiment you want to run.  In our case, let's split them evenly 50/50.

In the **Groups and Parameters** section, click on **Add Parameter** button and name the parameter *model\_name*, with *String* type

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/running-experiments/4837063a-9dde-4c0b-8bca-584d98adae47.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=8b5387d74e7d62de2cb8a98a10f4a7b1" alt="Parameter setup interface" width="508" height="316" data-path="images/integrations/azureai/running-experiments/4837063a-9dde-4c0b-8bca-584d98adae47.png" />
</Frame>

Now add the two configs we created in Step #1, one each to Control and Test parameters like this:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/azureai/running-experiments/b54a41de-a442-4870-870c-81ff949ecceb.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=056c26d4fcf6af1807cbb3380528ebff" alt="Experiment variant configuration screen" width="700" height="341" data-path="images/integrations/azureai/running-experiments/b54a41de-a442-4870-870c-81ff949ecceb.png" />
</Frame>

### Step 5: Save and start the experiment

Now, hit the **Save** button at the bottom of the page. You will now see a **Start** button appear at the top of the experiment page.  Go ahead and click it - this will start the allocation process for the experiment.

### Step 6: Let's write some code

The code below:

1. Fetches the experiment configuration from server for a given user.  You can pass down the **userID** from your client application or use one from your database.  The code below generates a random one for testing purposes.
2. Gets the **config name** from the experiment variant - either from control or test
3. Create a model client using the config that we just fetched
4. Uses that model client to complete text.

```js  theme={null}
async function testExperiments() {
  await AzureAI.initialize(statsigServerKey);

  const experiment = Statsig.getExperimentSync(
    { userID: Math.random().toString() }, // use a valid userID here
    "model_experiment_gpt4o_vs_gpt4o-mini",
  );
  const configName = experiment.get("model_name", "gpt-4o");
  console.log(`Using model: ${configName}`);

  const modelClient = AzureAI.getModelClient(configName);
  const result = await modelClient.complete([{
    role: "user",
    content: "Recite the first 10 digits of pi."
  }]);
  result.choices.forEach((choice, i) => {
    console.log(choice.message.content);
  });
  
  await AzureAI.shutdown();
}
```

### Step 7: Run the experiment and verify results

Run this experiment for several days, and you will now be able to measure latency profiles of **gpt-4o** compared with **gpt-4o-mini** in Statsig console. You can choose whichever one suits your needs.

The above is just a simple experiment to test models against each other. You could also tweak other parameters like *temperature*, *frequency\_penalty*, *max\_tokens*, etc. by modifying the config.  This could all be done without needing to update code.


Built with [Mintlify](https://mintlify.com).