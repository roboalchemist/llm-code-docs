# Source: https://docs.helicone.ai/features/datasets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Datasets

> Curate and export LLM request/response data for fine-tuning, evaluation, and analysis

Transform your LLM requests into curated datasets for model fine-tuning, evaluation, and analysis. Helicone Datasets let you select, organize, and export your best examples with just a few clicks.

## Why Use Datasets

<CardGroup cols={2}>
  <Card title="Fine-Tuning" icon="brain">
    Create training datasets from your best requests for custom model fine-tuning
  </Card>

  <Card title="Model Evaluation" icon="chart-bar">
    Build evaluation sets to test model performance and compare different versions
  </Card>

  <Card title="Quality Control" icon="shield-check">
    Curate high-quality examples to improve prompt engineering and model outputs
  </Card>

  <Card title="Data Analysis" icon="magnifying-glass">
    Export structured data for external analysis and research
  </Card>
</CardGroup>

## Creating Datasets

### From the Requests Page

The easiest way to create datasets is by selecting requests from your logs:

<Steps>
  <Step title="Filter your requests">
    Use [custom properties](/observability/custom-properties) and filters to find the requests you want

    <Frame>
      <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/filters.webp?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=37fe83061c37219821ae7b242afbd2e8" alt="Filtering requests with custom properties and search criteria" data-og-width="1588" width="1588" data-og-height="466" height="466" data-path="images/datasets/filters.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/filters.webp?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=39a32b7b33bdae4b259a5f284ce43b59 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/filters.webp?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=20f7cd6825009ee3346c74be0ee3937b 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/filters.webp?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=04bbe907ecde0730e74e8d278211a894 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/filters.webp?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=b97fc791353acef6cca3826dc76654b4 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/filters.webp?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=46f98ce95d72985fab53132ce2baf6e0 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/filters.webp?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=514026471ca1d9600c062b8ceb11e836 2500w" />
    </Frame>
  </Step>

  <Step title="Select requests">
    Check the boxes next to requests you want to include in your dataset

    <Frame>
      <img src="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-select.webp?fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=3ff1badd9fb09cfc0fb9425c374d2ac6" alt="Selecting multiple requests to add to dataset" data-og-width="1662" width="1662" data-og-height="1678" height="1678" data-path="images/datasets/datasets-select.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-select.webp?w=280&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=5b50b92c9526701c8420625ac4135c42 280w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-select.webp?w=560&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=335bc90feb12d28cecce8e0817eca8b3 560w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-select.webp?w=840&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=7414c4ce9c6820c7a018d4b0f7f3dd57 840w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-select.webp?w=1100&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=8a11d18aa8bc88d853eb577636e01036 1100w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-select.webp?w=1650&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=739326bf33f38515149378ca9bfc6832 1650w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-select.webp?w=2500&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=057bd50b6387f2d2355f13c9ce27e13c 2500w" />
    </Frame>
  </Step>

  <Step title="Add to dataset">
    Click "Add to Dataset" and choose to create a new dataset or add to an existing one

    <Frame>
      <img src="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/dataset-add.webp?fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=098889f862bf167f5c73f21a28d5be6d" alt="Adding selected requests to a dataset" data-og-width="958" width="958" data-og-height="612" height="612" data-path="images/datasets/dataset-add.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/dataset-add.webp?w=280&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=170445b334ab0f5bbddee31cd9bc9a98 280w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/dataset-add.webp?w=560&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=44cc79273136d589c5271716c1aca659 560w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/dataset-add.webp?w=840&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=f941b1a4908d989fb28ad88f0372fe46 840w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/dataset-add.webp?w=1100&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=7f6a337b20ba3ffdc796ac2620ba89d0 1100w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/dataset-add.webp?w=1650&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=1aa3f60490080a4f915675bde1525acb 1650w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/dataset-add.webp?w=2500&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=4e13c3dedccad6d8ee7b94239d3475b3 2500w" />
    </Frame>
  </Step>
</Steps>

### Via API

Create datasets programmatically for automated workflows:

```typescript  theme={null}
// Create a new dataset
const response = await fetch('https://api.helicone.ai/v1/helicone-dataset', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'Customer Support Examples',
    description: 'High-quality support interactions for fine-tuning'
  })
});

const dataset = await response.json();

// Add requests to the dataset
await fetch(`https://api.helicone.ai/v1/helicone-dataset/${dataset.id}/request/${requestId}`, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`
  }
});
```

## Building Quality Datasets

### The Curation Process

Transform raw requests into high-quality training data through careful curation:

<Steps>
  <Step title="Collect broadly, then filter">
    Start by adding many potential examples, then narrow down to the best ones. It's easier to remove than to find examples later.
  </Step>

  <Step title="Review each example">
    <Frame>
      <img src="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-edit.webp?fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=056646f09202b7f2083286491889a941" alt="Dataset curation interface showing request details for review" data-og-width="2150" width="2150" data-og-height="1426" height="1426" data-path="images/datasets/datasets-edit.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-edit.webp?w=280&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=165c165e5cc158ec303bf17a86fe0db9 280w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-edit.webp?w=560&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=4e75bcf92e53ae1c2715da41f4cf75ad 560w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-edit.webp?w=840&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=d3cd057af0b007b984c342f1addb8f61 840w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-edit.webp?w=1100&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=720c321937f44fa3c26bb1cd922db34e 1100w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-edit.webp?w=1650&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=ed888032d40398283bc315d7f2e29db6 1650w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-edit.webp?w=2500&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=2079f962d790c03df81ef38f21c05fed 2500w" />
    </Frame>

    Examine each request/response pair for:

    * **Accuracy** - Is the response correct and helpful?
    * **Consistency** - Does it match the style and format you want?
    * **Completeness** - Does it fully address the user's request?
  </Step>

  <Step title="Remove poor examples">
    Delete any examples that are:

    * Incorrect or misleading responses
    * Off-topic or irrelevant
    * Inconsistent with your desired behavior
    * Edge cases that might confuse the model
  </Step>

  <Step title="Balance your dataset">
    Ensure you have:

    * Examples covering all common use cases
    * Both simple and complex queries
    * Appropriate distribution matching real usage
  </Step>
</Steps>

<Note>
  **Quality beats quantity** - 50-100 carefully curated examples often outperform thousands of uncurated ones. Focus on consistency and correctness over volume.
</Note>

### Dataset Dashboard

Access all your datasets at [helicone.ai/datasets](https://us.helicone.ai/datasets):

<Frame caption="Manage all your curated datasets in one place">
  <img src="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-dashboard.webp?fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=b8d63f741eb16833a0aab1ea739356d1" alt="Helicone datasets dashboard with list of datasets and their metadata" data-og-width="2322" width="2322" data-og-height="1198" height="1198" data-path="images/datasets/datasets-dashboard.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-dashboard.webp?w=280&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=88fa5e1e95f6d967a29f79cc4b500bc3 280w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-dashboard.webp?w=560&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=7004550662e7a62eb6193c0cdfd4bd82 560w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-dashboard.webp?w=840&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=df91bde5ff456d98f3d8fbfada167e26 840w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-dashboard.webp?w=1100&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=464fa3745d010638efe3bfd2ebaeaa5f 1100w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-dashboard.webp?w=1650&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=d5b1c3e75c84aa4a9418b06f5bb9f037 1650w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-dashboard.webp?w=2500&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=ddaf6b1c2524052176d8e3aacace58ff 2500w" />
</Frame>

From the dashboard you can:

* **Track progress** - Monitor dataset size and last updated time
* **Access datasets** - Click to view and curate contents
* **Export data** - Download datasets when ready for fine-tuning
* **Maintain quality** - Regularly review and improve your collections

## Exporting Data

### Export Formats

Download your datasets in various formats:

<Frame caption="Export options for downloading your dataset">
  <img src="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-export.webp?fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=6d8394979cab30f69b83b96068d70938" alt="Dataset export dialog showing different format options" data-og-width="1074" width="1074" data-og-height="958" height="958" data-path="images/datasets/datasets-export.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-export.webp?w=280&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=964b7d3756b216da536112178ff335f6 280w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-export.webp?w=560&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=20c214917c9a86db64bddddc74bdf876 560w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-export.webp?w=840&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=b9ce601d63bb0b3b337c42838ac4469a 840w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-export.webp?w=1100&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=a1c03b96db4aff640412c525b0c9269d 1100w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-export.webp?w=1650&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=ed2828915de6a8589c964ed24fdecda4 1650w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/datasets/datasets-export.webp?w=2500&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=e4ac08d313deac17119c09348aea7e77 2500w" />
</Frame>

<Tabs>
  <Tab title="Fine-Tuning (JSONL)">
    Perfect for OpenAI fine-tuning format:

    ```json  theme={null}
    {"messages": [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi there!"}]}
    {"messages": [{"role": "user", "content": "Help me"}, {"role": "assistant", "content": "I'd be happy to help!"}]}
    ```

    Ready to use directly with OpenAI's fine-tuning API.
  </Tab>

  <Tab title="Analysis (CSV)">
    Structured format for spreadsheet analysis:

    ```csv  theme={null}
    request_id,created_at,model,prompt_tokens,completion_tokens,cost,user_message,assistant_response
    req_123,2024-01-15,gpt-4o,50,100,0.002,"Hello","Hi there!"
    req_124,2024-01-15,gpt-4o,45,95,0.0019,"Help me","I'd be happy to help!"
    ```

    Import into Excel, Google Sheets, or data analysis tools.
  </Tab>
</Tabs>

### API Export

Retrieve dataset contents programmatically:

```typescript  theme={null}
// Query dataset contents
const response = await fetch(`https://api.helicone.ai/v1/helicone-dataset/${datasetId}/query`, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    limit: 100,
    offset: 0
  })
});

const data = await response.json();
```

## Use Cases

### Replace Expensive Models with Fine-Tuned Alternatives

The most common use case - using your expensive model logs to train cheaper, faster models:

<Steps>
  <Step title="Log high-quality outputs">
    Start logging successful requests from o3, Claude 4.1 Sonnet, Gemini 2.5 Pro, or other premium models that represent your ideal outputs
  </Step>

  <Step title="Build task-specific datasets">
    Create separate datasets for different tasks (e.g., "customer support", "code generation", "data extraction")
  </Step>

  <Step title="Curate for consistency">
    Review examples to ensure responses follow the same format, style, and quality standards
  </Step>

  <Step title="Fine-tune smaller models">
    Export JSONL and fine-tune o3-mini, GPT-4o-mini, Gemini 2.5 Flash, or other models that are 10-50x cheaper
  </Step>

  <Step title="Iterate with production data">
    Continue collecting examples from your fine-tuned model to improve it over time
  </Step>
</Steps>

### Task-Specific Evaluation Sets

Build evaluation datasets to test model performance:

```typescript  theme={null}
// Create eval sets for different capabilities
const datasets = {
  reasoning: 'Complex multi-step problems with verified solutions',
  extraction: 'Structured data extraction with known correct outputs',
  creativity: 'Creative writing with human-rated quality scores',
  edge_cases: 'Unusual inputs that often cause failures'
};
```

Use these to:

* Compare model versions before deploying
* Test prompt changes against consistent examples
* Identify model weaknesses and blind spots

### Continuous Improvement Pipeline

<Frame caption="Use scores and user feedback to identify your best examples">
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/scores.webp?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=a8181381e7f337ae64baeded1c9699d9" alt="Filtering requests by scores to identify best examples for datasets" data-og-width="1278" width="1278" data-og-height="770" height="770" data-path="images/datasets/scores.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/scores.webp?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=87672c9e9eb76d81072f5b6c741fade4 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/scores.webp?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=5075357477331946840eeb42ef025ad2 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/scores.webp?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=700a6b36621b46d060013e74f481398b 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/scores.webp?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=d21e6847eb91130c8c71e636ab80c7b9 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/scores.webp?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=b0fb2167301a2f39478092ce8adf4b60 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/datasets/scores.webp?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=51383f98d78a0454ff5e9f44c808ce97 2500w" />
</Frame>

Build a data flywheel for model improvement:

1. **Tag requests** with custom properties for easy filtering
2. **Score outputs** based on user feedback or automated metrics
3. **Auto-collect winners** into datasets when they meet quality thresholds
4. **Regular retraining** with newly curated examples
5. **A/B test** new models against production traffic

<Note>
  Start small - even 50-100 high-quality examples can significantly improve performance on specific tasks. Focus on one narrow use case first rather than trying to fine-tune a general-purpose model.
</Note>

## Best Practices

<CardGroup cols={2}>
  <Card title="Quality over Quantity" icon="star">
    Choose fewer, high-quality examples rather than large datasets with mixed quality
  </Card>

  <Card title="Diverse Examples" icon="shuffle">
    Include varied inputs, edge cases, and different user types in your datasets
  </Card>

  <Card title="Regular Updates" icon="arrows-rotate">
    Continuously add new examples as your application evolves and improves
  </Card>

  <Card title="Clear Criteria" icon="list-check">
    Document what makes a "good" example for each dataset's specific purpose
  </Card>
</CardGroup>

## Related Features

<CardGroup cols={2}>
  <Card title="Custom Properties" icon="tag" href="/features/advanced-usage/custom-properties">
    Tag requests to make dataset creation easier with filtering
  </Card>

  <Card title="User Metrics" icon="users" href="/features/advanced-usage/user-metrics">
    Track which users generate the best examples for your datasets
  </Card>

  <Card title="Sessions" icon="link" href="/features/sessions">
    Include full conversation context in your datasets
  </Card>

  <Card title="Feedback" icon="message" href="/features/advanced-usage/feedback">
    Use user ratings to automatically identify dataset candidates
  </Card>
</CardGroup>

***

Datasets turn your production LLM logs into valuable training and evaluation resources. Start small with a focused use case, then expand as you see the benefits of curated, high-quality data.
