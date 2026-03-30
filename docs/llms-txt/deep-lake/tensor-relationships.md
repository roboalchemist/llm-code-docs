# Source: https://docs-v3.activeloop.ai/v3.0.0/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/3.1.0/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/3.1.1/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/how-it-works/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/technical-details/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/technical-details/data-format/tensor-relationships.md

# Source: https://docs-v3.activeloop.ai/technical-details/data-format/tensor-relationships.md

# Tensor Relationships

## Understanding the Relationships Between Deep Lake Tensors

### Indexing

Hub datasets and their tensors are indexed like `ds[index]` or `ds.tensor_name[index]`, and data at the same index are assumed to be related. For example, a `bounding_box` at index 100 is assumed to apply to the `image` at index 100.

### Relationships Between Tensors

For datasets with multiple tensors, it is important to follow the conventions below in order for the visualizer to correctly infer how tensors are related.

{% hint style="info" %}
By default, in the absence of `groups`, the visualizer assumes that all tensors are related to each other.&#x20;
{% endhint %}

This works well for simple use cases. For example, it is correct to assume that the `images`, `labels`, and `boxes` tensors are related in the dataset below:

```
ds
-> images (htype = image)
-> labels (htype = class_label)
-> boxes (htype = bbox)
```

However, if datasets are highly complex, assuming that all tensor are related may lead to visualization errors, because every tensor may not be related to every other tensor:

```
ds
-> images (htype = image)
-> vehicle_labels (htype = class_label)
-> vehicle_boxes (htype = bbox)
-> people_labels (htype = class_label)
-> people_masks (htype = binary_mask)
```

In the example above, only some of the annotation tensors are related to each other:&#x20;

* `vehicle_labels -> vehicle_boxes`: Boxes and labels describing cars, trucks, etc.
* `people_labels -> people_masks`: Binary masks and labels describing adults, toddlers, etc.

{% hint style="info" %}
The best method for disambiguating the relationships between tensors is to place them in `groups`, because the visualizer assumes that annotation tensors in different groups are not related.
{% endhint %}

In the example above, the following groups could be used to disambiguate the annotations:

```
ds
-> images (htype = image)
-> vehicles (group)
   -> vehicle_labels (htype = class_label)
   -> vehicle_boxes (htype = bbox)
-> people (group)
   -> people_labels (htype = class_label)
   -> people_masks (htype = binary_mask) 
```
