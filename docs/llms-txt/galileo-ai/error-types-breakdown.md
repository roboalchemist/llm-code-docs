# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/error-types-breakdown.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Types Breakdown

> For use cases with complex data and error types (e.g. Named Entity Recognition, Object Detection or Semantic Segmentation), the **Error Types Chart** gives you an insight into exactly how the Ground Truth differed from your model's predictions

It allows you to get a sense of what types of mistakes your model is making, with what frequency and, in the case of Object Detection, what impact these errors had on your overall performance metric.

<Frame>
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-t.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c9ef59838770619cd0d26a9919e4ab2f" data-og-width="559" width="559" data-og-height="588" height="588" data-path="images/e-t.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-t.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=3085a3a5c0e109d9db47b91b308d28c1 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-t.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e50ea942d97ed6d9dc1c76b76dc2a188 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-t.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=08342ab927c4a81e1044316cda3d1126 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-t.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=4099ccb0e024d32d5a2c21e9779b7d3e 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-t.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c782426efa0a450bff7b51d87c6f2932 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-t.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=ead1351befc27d9ce676c3721d4c4a95 2500w" />
</Frame>

Error Types for a Object Detection model

**How does this work?**

For Named Entity Recognition, Galileo surfaces *Ghost Spans, Span Shifts, Missed Spans* or *Wrong Tag Errors*.

For Object Detection, Galileo leverages the [TIDE](https://arxiv.org/abs/2008.08115) framework to find associations between Ground Truth and Predicted objects and break differences between the two into one of: *Localization*, *Classification*, *Background*, *Missed*, *Duplicates* or *Localization and Classification* mistakes. See a thorough write-up of how that's done and the definition of each error type [here](/galileo/gen-ai-studio-products/galileo-ai-research/errors-in-object-detection).

**How should I leverage this chart?**

Click on an error type to filter the dataset to samples with that error type. From there, you can inspect your erroneous samples and fix them.

One common flow we see is selecting *Ghost Spans (NER)* or *Background Confusion Errors* (Obj. Detection) combined with a high DEP filter can be used to surface Missed Annotations from your labelers. You can send these samples to your labeling tool or fix them with the Galileo console.
