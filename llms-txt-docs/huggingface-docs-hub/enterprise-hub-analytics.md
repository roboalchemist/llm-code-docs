# Source: https://huggingface.co/docs/hub/enterprise-hub-analytics.md

# Analytics

> [!WARNING]
> This feature is part of the Team & Enterprise plans.

## Publisher Analytics Dashboard

Track all your repository activity with a detailed downloads overview that shows total downloads for all the Models and Datasets published by your organization. Toggle between "All Time" and "Last Month" views to gain insights across your repositories over different periods.

### Per-repo breakdown

Explore the metrics of individual repositories with the per-repository drill-down table. Utilize the built-in search feature to quickly locate specific repositories. Each row also features a time-series graph that illustrates the trend of downloads over time.

## Export Publisher Analytics as CSV

Download a comprehensive CSV file containing analytics for all your repositories, including model and dataset download activity.

### Response Structure

The CSV file is made of daily download records for each of your models and datasets.

```csv
repoType,repoName,total,timestamp,downloads
model,huggingface/CodeBERTa-small-v1,4362460,2021-01-22T00:00:00.000Z,4
model,huggingface/CodeBERTa-small-v1,4362460,2021-01-23T00:00:00.000Z,7
model,huggingface/CodeBERTa-small-v1,4362460,2021-01-24T00:00:00.000Z,2
dataset,huggingface/documentation-images,2167284,2021-11-27T00:00:00.000Z,3
dataset,huggingface/documentation-images,2167284,2021-11-28T00:00:00.000Z,18
dataset,huggingface/documentation-images,2167284,2021-11-29T00:00:00.000Z,7
```

### Repository Object Structure

Each record in the CSV contains:

- `repoType`: The type of repository (e.g., "model", "dataset")
- `repoName`: Full repository name including organization (e.g., "huggingface/documentation-images")
- `total`: Cumulative number of downloads for this repository
- `timestamp`: ISO 8601 formatted date (UTC)
- `downloads`: Number of downloads for that day

Records are ordered chronologically and provide a daily granular view of download activity for each repository.

