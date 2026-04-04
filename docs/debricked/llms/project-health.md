# Source: https://docs.debricked.com/product/project-health.md

# Project health

Project health is an important aspect to consider when selecting dependencies. But what does Project Health even entail? OpenText Core SCA's Open-Source Health Metrics can help you gain an understanding of key aspects of any open-source project and make informed decisions when choosing what to bring into your codebase.

### **What is a health metric?**

A Metric is a measurement of a key aspect of an open-source project’s overall quality. For example, its contributors or its popularity. Our underlying data model aggregates data points into sub-metrics, which are then aggregated into a metric. We call these:

* Features - The lowest level datapoints
* Practices - The aggregated sub-metrics
* Metrics - The final aggregation of practices

You can think of a metric as the area that you want to investigate (for example, is the project popular? is there a healthy contributor community?), and practices as more specific questions you want answered (for example, how experienced are the contributors?), how long do contributors stay with the project?).

Between each layer, there are weights that determine the impact of any given feature on a practice, and of any given practice on a metric. You can find the data model of each metric illustrated in [Contributors](https://docs.debricked.com/product/project-health/contributors), [Popularity](https://docs.debricked.com/product/project-health/popularity), and [Security](https://docs.debricked.com/product/project-health/security).
