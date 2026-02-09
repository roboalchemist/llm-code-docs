# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/dataset-slices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dataset Slices

> Slices is a powerful Galileo feature that allows you to monitor, across training runs, a sub-population of the dataset based on metadata filters.

### Creating Your First Simple Slice

Imagine you want to monitor model performance on samples containing the keyword "star wars." To do so, you can simply type "star wars" into the search panel and save the resulting data as a new custom **Slice** (see Figure below).

<Frame caption="Fig. Slice for reviews with 'star wars' in it">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/galileo/galileo-nlp-studio/galileo-product-features/images/dataset-s-1.avif" />
</Frame>

When creating a new slice you are presented a pop up that allows you to give a **custom name** to your slice and displays slice level details: 1) Slice project scope, 2) Slice Recipe (filter rules to create the slice). Your newly created slice will be available across all training runs within the selected project.

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-1.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=35c3246edea6c1ff97d45ac515aa3be8" data-og-width="2430" width="2430" data-og-height="1436" height="1436" data-path="images/dataset-slice-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-1.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e13864a8dd1906f4944153b01463023e 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-1.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0d1be575f3285c8751797eae61baa56d 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-1.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6b79cdedd3f86b7dde5756737601070b 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-1.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c5bccc81c3c124b89eaa88005cceda4d 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-1.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=942e5a3055ad634dbfd52ee7974768cb 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-1.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=f01ff3cef1a8d5f9a92fefcf623c6678 2500w" />

### Complex Slices

You can create a custom slice in many different ways e.g. using [similarity search](/galileo/how-to-and-faq/galileo-product-features/similarity-search), using subsets etc. Moreover, you can create complex slices based on multiple filtering criteria. For example, the figure below walks through creating a slice by first using similarity search and then filtering for samples that contain the keyword "worst."

<Frame
  caption="Fig. Creation of complex slice (Recipe: Similar to (with 880 samples) + Search keyword(s) = `worst`)
"
>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/galileo/galileo-nlp-studio/galileo-product-features/images/dataset-s-2.gif" />
</Frame>

The final "Slice Recipe" is as follows:

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-2.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=9d7cc7fe1c13d6d953de680389bb859b" data-og-width="2214" width="2214" data-og-height="578" height="578" data-path="images/dataset-slice-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-2.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6701230faa5769b55dd297b4b8d14c94 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-2.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=90f841f4dd643dc9b132d3e382692a96 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-2.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=2bc2a58d7c2b06da530778ad36ae4c73 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-2.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0bf5c2b5895e016a8ed3d0128abf1d34 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-2.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6e23fe2284d832b494440649822bf102 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dataset-slice-2.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=8e1b5294a88504163add883c1eb3e4df 2500w" />
