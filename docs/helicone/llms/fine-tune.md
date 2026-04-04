# Source: https://docs.helicone.ai/guides/cookbooks/fine-tune.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to fine-tune LLMs with Helicone and OpenPipe

> Learn how to fine-tune large language models with Helicone and OpenPipe to optimize performance for specific tasks.

<Steps>
  <Step title="Add the OpenPipe Integration">
    Navigate to `Settings` -> `Connections` in your Helicone dashboard and configure the OpenPipe integration.

    <Frame>
      <img src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-integration.webp?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=a01654b47e3f5a161c510e1343b68f36" alt="Configure OpenPipe Integration" data-og-width="3456" width="3456" data-og-height="1928" height="1928" data-path="images/use-cases/fine-tune/openpipe-integration.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-integration.webp?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=db17f99abfcc2c7b3c5d7fa8b6ac9595 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-integration.webp?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=e9c37827e1606f12468ac8f8795d570f 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-integration.webp?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=a7fc83ee31e93b4df7e543b9c5ec03a3 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-integration.webp?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=9eebd2eeb7369a56b9096cf0fa8f9f5c 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-integration.webp?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=63e6dd835c7db60ff9e6cbd46ad91b07 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-integration.webp?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=56bd0bb643989bf00fc0d592ee229962 2500w" />
    </Frame>

    This integration allows you to manage your fine-tuning datasets and jobs seamlessly within Helicone.
  </Step>

  <Step title="Create a Dataset for Fine-Tuning">
    Your dataset doesn't need to be enormous to be effective. In fact, smaller, high-quality datasets often yield better results.

    * **Recommendation**: Start with 50-200 examples that are representative of the tasks you want the model to perform.

    <Frame>
      <img src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/dataset.webp?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=bc3bae83e7d99cc5e96743b126c38a0f" alt="Create a new dataset" data-og-width="3456" width="3456" data-og-height="1926" height="1926" data-path="images/use-cases/fine-tune/dataset.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/dataset.webp?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=7fa9b82c52bdae70e029114558693ec1 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/dataset.webp?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=ac80a9c31c5659f8dcfb9d40b11fe9a6 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/dataset.webp?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=c2dc85512ef48671338cea21e3c195c1 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/dataset.webp?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=0cae9d33ef32d40eca5de4f1feac2d65 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/dataset.webp?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=60b1229513b911200b538471581e4a9a 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/dataset.webp?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=3837bb8eb25fe0588e63c8c68cf55d89 2500w" />
    </Frame>

    Ensure your dataset includes clear input-output pairs to guide the model during fine-tuning.
  </Step>

  <Step title="Evaluate and Refine Your Dataset">
    Within Helicone, you can evaluate your dataset to identify any issues or areas for improvement.

    * **Review Samples**: Check for consistency and clarity in your examples.
    * **Modify as Needed**: Make adjustments to ensure the dataset aligns closely with your desired outcomes.

    <Frame>
      <img src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-button.webp?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=2d91397aca9771e8e412feef687bb0d1" alt="Evaluate your dataset" data-og-width="3456" width="3456" data-og-height="1928" height="1928" data-path="images/use-cases/fine-tune/openpipe-button.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-button.webp?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=2e5b517afcdf34fd776989239e468002 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-button.webp?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=3eb02e74b0c462c0dabd6ba73d87d104 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-button.webp?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=65b6fe1202d679f1715faedf5963bd73 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-button.webp?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=db371f368f3f9102dae34b2bd0340167 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-button.webp?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=4d7f7e3f01ef44a3fdc00e7609550624 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/openpipe-button.webp?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=60f73d442714a7169484bda1de0649e5 2500w" />
    </Frame>

    Regular evaluation helps in creating a robust fine-tuning dataset that enhances model performance.
  </Step>

  <Step title="Configure Your Fine-Tuning Job">
    Set up your fine-tuning job by specifying parameters such as:

    * **Model Selection**: Choose the base model you wish to fine-tune.
    * **Training Settings**: Adjust hyperparameters like learning rate, epochs, and batch size.
    * **Validation Metrics**: Define how you'll measure the model's performance during training.

    <Frame>
      <img src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/fine-tune-config.webp?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=f4c834715c6cb2b338fc89a16407e97b" alt="Configure your fine-tuning job" width="300" data-og-width="1202" data-og-height="1750" data-path="images/use-cases/fine-tune/fine-tune-config.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/fine-tune-config.webp?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=fa7edd2d3b487e62eda39a2979fbb750 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/fine-tune-config.webp?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=479471345b6946aa1c96e068102bcc73 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/fine-tune-config.webp?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=91b821e878d9b35510268f082502b822 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/fine-tune-config.webp?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=35aa5281a294f218dfe7b76899c68900 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/fine-tune-config.webp?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=c2e1b4e672101ba14a18fb1d015c61a2 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/fine-tune/fine-tune-config.webp?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=b799efda4c236c68960a9704de602c63 2500w" />
    </Frame>

    After configuring, initiate the fine-tuning process. Helicone and OpenPipe handle the heavy lifting, providing you with progress updates.
  </Step>

  <Step title="Deploy and Monitor Your Fine-Tuned Model">
    Once fine-tuning is complete:

    * **Deployment**: Integrate the fine-tuned model into your application via Helicone's API endpoints.
    * **Monitoring**: Use Helicone's observability tools to track performance, usage, and any anomalies.
  </Step>
</Steps>

## Additional Fine-Tuning Resources

For more information on fine-tuning, check out these resources:

* [Fine-Tuning Best Practices: Training Data](https://openpipe.ai/blog/fine-tuning-best-practices-series-introduction-and-chapter-1-training-data)
* [Fine-Tuning Best Practices: Models](https://openpipe.ai/blog/fine-tuning-best-practices-chapter-2-models)
* [How to use OpenAI fine-tuning API](/faq/openai-fine-tuning-api)
* [Understanding fine-tuning duration](/faq/llm-fine-tuning-time)
* [Comparing RAG and fine-tuning approaches](/faq/rag-vs-fine-tuning)
