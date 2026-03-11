# Source: https://docs.startree.ai/thirdeye/concepts-data-alerts-notifications/concepts-heatmaps.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Heatmaps

The dimension heatmap provides a visualization of how the metric - sliced by each dimension - changes when compared to a baseline. By default, the baseline is one week before the anomaly period.

The figure below shows an example of dimension heatmaps.

The metric has 15 dimensions. Each row represents one dimension, and each cell within the row is a dimension value. The size of the cell is proportional to the number of observations having the cell value. It is called *contribution*.

For instance, for dimension `assignees`, around 90% of the observations have the value `<EMPTY_VALUE>`(^1)

When there are too many small values, they are grouped into a “OTHER” category.

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_heatmap.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=fb7891e54ef1565cea153e985e531694" width="80%" className="medium-zoom-image" data-path="img/thirdeye/_heatmap.png" />

The color of the cell is determined by the change. The more important is a change, the more intense is the color. Blue means change up. Red means change down.
The change is defined as the percentage point (pp) difference between the baseline contribution and the current contribution.

For instance: for dimension `userType`, in the baseline, `Bot` dimension represents 20% of the traffic. In the current observations, `Bot` represents `50%` of the traffic. This is a +30%pp change. `Bot` is deep blue.

<img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/_color_scale.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=f4492d2626f08814b3f2fe9a0758ab8a" alt="" width="1253" height="189" data-path="img/thirdeye/_color_scale.png" />

(^1): Empty value 90% of time?? This is fine, the example dataset is GitHub pull requests. It just means around 90% of PRs are not assigned.

Built with [Mintlify](https://mintlify.com).
