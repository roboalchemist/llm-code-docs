# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/dataset-view.md

# Dataset View

> The Dataset View provides an interactive data table for inspecting your datasets.

Individual data samples from your dataset or selected data subset are shown, where each sample is a row in the table. In addition to the text, a sample's associated gold label, predicted label, and DEP score are included as data attribute columns. By default, the samples are sorted by decreasing DEP score.

<Frame caption="Fig. The Dataset View">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dataset-1.webp" />
</Frame>

### Customization

As shown below, the Dataset View can be customized in the following ways:

* Sorting by DEP, Confidence or Metadata Columns

* Filtering to a specific class, DEP range, error type or metadata values

* Selecting and de-selecting dataset columns

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dataset-2.gif" />
</Frame>

### Data Selection

Each row or data sample can be selected to perform an action. As demonstrated in Test Drive Galileo - Movie Reviews, we can easily identify and export data samples with annotation errors for relabeling and/or further inspection. See [Actions](/galileo/how-to-and-faq/galileo-product-features/actions) for more details.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dataset-3.gif" />
</Frame>
