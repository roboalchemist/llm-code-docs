# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/taking-action.md

# Taking Action

> Take actionable steps in Galileo LLM Fine-Tune to address model performance issues, refine outputs, and achieve targeted AI improvements.

Once you've identified [issues in your data](/galileo/gen-ai-studio-products/galileo-llm-fine-tune/console-walkthrough), Galileo empowers you to take action on them. Galileo supports the following actions:

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-taking-action.png)

* Find Similar - Need to add more "similar" samples to your dataset? Find similar helps you find samples from other splits or from unlabeled datasets.

* Export - Download the selected samples as a CSV file, to S3/GCS, or programmatically.

* Removing Samples - Remove samples from your dataset. This is useful if you've found garbage samples or are looking to reduce your dataset size.

* Editing Samples - Edit the Target (Expected Output) of your sample. Use this if you've found an error in your Target.

* Send to Annotators - Do you use a labeling tool to manage your annotation work? Send to Annotators leverages our labeling integrations to hook into your annotation tool. Send your samples to your annotators for relabeling.

### Edits Cart

The **Edits Cart** serves as the single place to track all your changes. From here you can track who's done what changes, review their work, and download "clean" versions of your dataset.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-taking-action-cart.png)

### Retrain

Once you're satisfied with the changes you've made to your dataset. You can export the "clean" dataset, and retrain your model to see your model improvements.
