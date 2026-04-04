# Source: https://docs.aporia.com/ml-monitoring-as-code/data-segments.md

# Data Segments

This guide will show you how to automatically add data segments to your model from code using the Python SDK.&#x20;

For more information on data segments, see the [tracking-data-segments](https://docs.aporia.com/core-concepts/tracking-data-segments "mention") documentation.

## Defining Data Segments

To add new data segments:

```python
platform_segment = aporia.Segment(
    "Platform",
    field="platform",
    values=["desktop", "mobile"]
)

country_segment = aporia.Segment(
    "Country",
    field="country",
    values=["US", "IL", "DE", "FR", "GB", "DK"]
)
```

In this example, we're adding two new data segments - **platform** and **country**. To add the segments to your model, pass them to the model object:

```python
model = aporia.Model(
    "My Model",
    type=aporia.ModelType.RANKING,
    versions=[model_version],
    segments=[platform_segment, country_segments]
)
```
