# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/actions.md

# Actions

> Actions help close the inspection loop and error discovery process. We support a number of actions.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/actions.gif" />
</Frame>

Generally these actions fall under two categories:

1. Fixing data in-tool:

* Edit Data

* Remove

* Change Label

2. Exporting Data to fix it elsewhere:

* Send to Labelers

* Export Data

### Fixing Data In-Tool

**Edit Data**

This feature is only supported for NLP tasks. Through *Edit Data* you can quickly make small changes to your text samples. For Classification tasks, you can find and replace text (indivually or in bulk). For NER tasks, you can also use *Edit Data* to shift spans, add new spans or remove spans.

**Removing Data**

Sometimes you find data samples that simply shouldn't be part of your dataset (e.g. garbage data) or simply want to remove mislabeled samples from your training dataset. "Remove data" allows you to remove these samples from your dataset. Upon selecting some samples, you'll have the option to remove them. Removed samples go to your Edits Cart, from where you can download your "fixed" dataset to train another model iteration.

**Change Label**

For Classification tasks, *Change Label* allows you to change the label of you selected samples. You can either set the label to what the model predicted or manually enter the label you'd like these samples to have.

### Exporting Data to fix it elsewhere:

At any point in the inspection process you can export any selection of data. You can download your data as a CSV, download to an S3, GCS or DeltaLake bucket, or programmatically fetch it through `dq.metrics`

Additionally, after taking actions like the ones mentioned above, your Changes will show up on the Edits Cart. From there you can export your full dataset (including or excluding changes) to train a new model run.

**Send to Labelers**

Sometimes you want your labelers to fix your data. Once you've identified a cohort of data that is mislabeled, you can use the *Send to Labelers* button and leverage our labeling integrations to send your samples to your labeling provider in one click.
