# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition/tabular-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tabular data

Edge Impulse has been a powerful platform for processing raw data like time-series and images, and now we’re taking it even further. With tabular data import, we’re empowering users by enabling seamless integration of pre-processed data, giving you more flexibility in how you work. Whether you process data externally or face restrictions with raw data, this update makes it even easier to leverage Edge Impulse for all your data handling and model training needs.

Check out the [announcement blog](https://www.edgeimpulse.com/blog/unlock-greater-data-flexibility-ingest-tabular-data/)!

<Frame caption="Tabular data">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tabular-data/main.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=e9a3d3133ec23b80f1f704e2c316b772" width="1600" height="855" data-path=".assets/images/tabular-data/main.png" />
</Frame>

## Upload tabular data samples

### 1. Using the CSV Wizard

If your dataset is in the CSV format and contains a label column, the [CSV Wizard](/studio/projects/data-acquisition/csv-wizard) is probably the easiest method to import your tabular data.

Once your CSV Wizard is configured, you can use the [Studio Uploader](/studio/projects/data-acquisition/uploader), the [CLI Uploader](/tools/clis/edge-impulse-cli/uploader) or the [Ingestion API](/apis/ingestion).

### 2. Using Edge Impulse `info.labels` description file

The other way is to create a `info.labels` file, present in your dataset. Edge Impulse will automatically detect it when you upload your dataset and will use this file to set the labels.

Once you have your `info.labels` file available, to upload it, you can use the [Studio Uploader](/studio/projects/data-acquisition/uploader), the [CLI Uploader](/tools/clis/edge-impulse-cli/uploader) or the [Ingestion API](/apis/ingestion).

### Visualizing tabular data samples

<Frame caption="Tabular data sample preview">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tabular-data/preview.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=37e3eed02b5e714e99cc9e63c7fd12a4" width="1332" height="1000" data-path=".assets/images/tabular-data/preview.png" />
</Frame>

### Classify tabular data

In the **Live classification** tab, you can classify your tabular/pre-processed test samples:

<Frame caption="Test tabular data samples">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tabular-data/live-classification.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=31a1040d76c7aef4925637f59dd6d30d" width="1600" height="901" data-path=".assets/images/tabular-data/live-classification.png" />
</Frame>

### Resources

#### Public projects

* [HRV AFIB - Tabular data](https://studio.edgeimpulse.com/public/520145/live)


Built with [Mintlify](https://mintlify.com).