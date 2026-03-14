# Source: https://docs.statsig.com/metrics/metric-family.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metric Family

> Making it easier to manage metric variant.

It can be difficult to managing a large catalog of metrics that are a slight variant of one another. A common challenge we hear is the difficulty of ensuring that each metric variant inherit the same changes when the metrics need to be updated.

Metric Families let you create metric variants as child metrics of a parent metric. When a parent metric is updated, those changes automatically cascade to its child metrics, keeping all related metric definitions consistent and in sync.

The table below lists all supported metric types along with the modifications that can be applied to their child metrics.

| Available Metric Type | Modifiable Configs                                                                                                                |   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- | - |
| SUM <br /> COUNT      | <ul><li>Add metric source filter</li><li>Outlier Management</li><li>Variance Reduction</li><li>Cohorts and Delayed Data</li></ul> |   |

## Getting Started

To create a child metric look for the “Create Child Metric” option the the drop down menu found in the top right corner of a metric.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HB9FoKhwaIPpC1gV/images/metrics/metric-family/create-child.png?fit=max&auto=format&n=HB9FoKhwaIPpC1gV&q=85&s=5c05b5539aa3e0f165a17e6f39abe636" alt="Creating a child metric" width="1018" height="527" data-path="images/metrics/metric-family/create-child.png" />
</Frame>

You will be able to track the child metrics for a given parent metrics in the top right metric family icon

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HB9FoKhwaIPpC1gV/images/metrics/metric-family/tree-child.png?fit=max&auto=format&n=HB9FoKhwaIPpC1gV&q=85&s=b167503c6e24377c01ead94bccc87f93" alt="Tracking tree of child metrics" width="1016" height="288" data-path="images/metrics/metric-family/tree-child.png" />
</Frame>

## Deleting and Archiving

When a parent metric is deleted or archived, all of its child metrics are deleted or archived as well. Re-enabling the parent will automatically restore those child metrics. Child metrics disabled through the parent cannot be restored individually—they can only be re-enabled by restoring the parent metric.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HB9FoKhwaIPpC1gV/images/metrics/metric-family/delete.png?fit=max&auto=format&n=HB9FoKhwaIPpC1gV&q=85&s=1bc478f18b12cee52c7cd1bcb23ae822" alt="Metric deletion confirmation message" width="532" height="297" data-path="images/metrics/metric-family/delete.png" />
</Frame>

If a child metric is deleted or archived independently of its parent, it can be restored on its own—but it will return as a standalone metric, without its original parent-child relationship.

## In Experiments

Clicking on a Parent Metric option in Experiment setup will add all of it's child metrics as well. You can remove any metrics you don’t need in the experiment

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HB9FoKhwaIPpC1gV/images/metrics/metric-family/in-experiment.png?fit=max&auto=format&n=HB9FoKhwaIPpC1gV&q=85&s=1d2e039ab3fe446ec0a984ac95b884b0" alt="Adding parent metric to an experiment will add all child metrics with it" width="1898" height="421" data-path="images/metrics/metric-family/in-experiment.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).