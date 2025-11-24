# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/dataset-slices.md

# Dataset Slices

> Slices is a powerful Galileo feature that allows you to monitor, across training runs, a sub-population of the dataset based on metadata filters.

### Creating Your First Simple Slice

Imagine you want to monitor model performance on samples containing the keyword "star wars." To do so, you can simply type "star wars" into the search panel and save the resulting data as a new custom **Slice** (see Figure below).

<Frame caption="Fig. Slice for reviews with 'star wars' in it">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/galileo/galileo-nlp-studio/galileo-product-features/images/dataset-s-1.avif" />
</Frame>

When creating a new slice you are presented a pop up that allows you to give a **custom name** to your slice and displays slice level details: 1) Slice project scope, 2) Slice Recipe (filter rules to create the slice). Your newly created slice will be available across all training runs within the selected project.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dataset-slice-1.png" />

### Complex Slices

You can create a custom slice in many different ways e.g. using [similarity search](/galileo/how-to-and-faq/galileo-product-features/similarity-search), using subsets etc. Moreover, you can create complex slices based on multiple filtering criteria. For example, the figure below walks through creating a slice by first using similarity search and then filtering for samples that contain the keyword "worst."

<Frame
  caption="Fig. Creation of complex slice (Recipe: Similar to (with 880 samples) + Search keyword(s) = `worst`)
"
>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/galileo/galileo-nlp-studio/galileo-product-features/images/dataset-s-2.gif" />
</Frame>

The final "Slice Recipe" is as follows:

<img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dataset-slice-2.png" />
