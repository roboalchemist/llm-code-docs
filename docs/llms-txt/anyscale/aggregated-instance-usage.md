# Source: https://docs.anyscale.com/reference/aggregated-instance-usage.md

# Aggregated Instance Usage API Reference

[View Markdown](/reference/aggregated-instance-usage.md)

# Aggregated Instance Usage API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Aggregated Instance Usage CLI[​](#aggregated-instance-usage-cli "Direct link to Aggregated Instance Usage CLI")

### `anyscale aggregated-instance-usage download-csv`[​](#anyscale-aggregated-instance-usage-download-csv "Direct link to anyscale-aggregated-instance-usage-download-csv")

**Usage**

`anyscale aggregated-instance-usage download-csv [OPTIONS]`

Download an aggregated instance usage report as a zipped CSV to the provided directory.

**Options**

* **`--start-date`**: The start date (inclusive) of the aggregated instance usage report. Format: YYYY-MM-DD
* **`--end-date`**: The end date (inclusive) of the aggregated instance usage report. Format: YYYY-MM-DD
* **`--cloud`**: The name of the cloud to filter the report by.
* **`--project`**: The name of the project to filter the report by.
* **`--directory`**: The directory to save the CSV file to. Default is the current directory.
* **`--hide-progress-bar`**: Whether to hide the progress bar. Default is False.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
$ anyscale aggregated-instance-usage download-csv --start-date 2024-10-01 --end-date 2024-10-03
(anyscale +0.5s) Downloading aggregated instance usage CSV...
Download complete! File saved to 'aggregated_instance_usage_2024-10-01_2024-10-03.zip'
0:00:01 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.4 kB / 79.4 kB Downloading aggregated instance usage CSV
(anyscale +2.2s) Downloaded CSV to aggregated_instance_usage_2024-10-01_2024-10-03.zip
```

## Aggregated Instance Usage SDK[​](#aggregated-instance-usage-sdk "Direct link to Aggregated Instance Usage SDK")

### `anyscale.aggregated_instance_usage.download_csv`[​](#anyscaleaggregated_instance_usagedownload_csv "Direct link to anyscaleaggregated_instance_usagedownload_csv")

Download an aggregated instance usage report as a zipped CSV to the provided directory.

**Arguments**

* **`filters` ([DownloadCSVFilters](/reference/aggregated-instance-usage.md#downloadcsvfilters))**: The filter of the instance usage to download.

**Returns**: str

#### Examples[​](#examples-1 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.aggregated_instance_usage.models import DownloadCSVFilters

anyscale.aggregated_instance_usage.download_csv(
    DownloadCSVFilters(
        start_date="2024-10-01",
        end_date="2024-10-02",
        cloud="cloud_name",
        project="project_name",
        directory="/directory",
        hide_progress_bar=False,
    ),
)
```

## Aggregated Instance Usage Models[​](#aggregated-instance-usage-models "Direct link to Aggregated Instance Usage Models")

### `DownloadCSVFilters`[​](#downloadcsvfilters "Direct link to downloadcsvfilters")

Filters to use when downloading usage CSVs.

#### Fields[​](#fields "Direct link to Fields")

* **`start_date` (str)**: Start date (UTC inclusive) for the usage CSV.
* **`end_date` (str)**: End date (UTC inclusive) for the usage CSV.
* **`cloud` (str | None)**: Optional cloud name to filter by.
* **`project` (str | None)**: Optional project name to filter by.
* **`directory` (str | None)**: Optional directory to save the CSV to.
* **`hide_progress_bar` (bool | None)**: Optional hide progress bar.

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-2 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.aggregated_instance_usage.models import DownloadCSVFilters

download_csv_filters = DownloadCSVFilters(
    # Start date (UTC inclusive) for the usage CSV.
    start_date="2024-10-01",
    # End date (UTC inclusive) for the usage CSV.
    end_date="2024-10-31",
    # Optional cloud name to filter by.
    cloud="cloud_name",
    # Optional project name to filter by.
    project="project_name",
    # Optional directory to save the CSV to.
    directory="/directory",
    # Optional hide progress bar.
    hide_progress_bar=False,
)
```
