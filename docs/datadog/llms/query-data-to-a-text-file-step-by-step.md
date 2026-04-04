# Source: https://docs.datadoghq.com/developers/guide/query-data-to-a-text-file-step-by-step.md

---
title: Query data to a text file, step by step
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Developers > Developer Guides > Query data to a text file, step by step
---

# Query data to a text file, step by step

This article explains how to set up an environment to make the most of the Datadog API and includes how to pull or push events, metrics, and monitors from [Datadog's public API](https://docs.datadoghq.com/api/) to a local file.

Prerequisite: Python and `pip` installed on your localhost. Windows users see [Installing Python 2 on Windows](http://docs.python-guide.org/en/latest/starting/install/win).

1. Open a terminal.
1. Verify the directory: `pwd` on macOS, `dir` on Windows.
1. Create a new folder: `mkdir <NAME_OF_THE_FOLDER>`.
1. Enter the folder: `cd <NAME_OF_THE_FOLDER>`.
1. Download the script [api_query_data.py](https://docs.datadoghq.com/resources/python/api_query_data.py) to the folder created in step 3 and edit it:
   1. Replace `<YOUR_DD_API_KEY>` and `<YOUR_DD_APP_KEY>` with your [Datadog API and app keys](https://app.datadoghq.com/organization-settings/api-keys).
   1. Replace `system.cpu.idle` with a metric you want to fetch. A list of your metrics is displayed in the [Datadog Metric Summary](https://app.datadoghq.com/metric/summary).
   1. Optionally, replace `*` with a host to filter the data. A list of your hosts is displayed in the [Datadog Infrastructure List](https://app.datadoghq.com/infrastructure).
   1. Optionally, change the time period to collect the data. The current setting is 3600 seconds (one hour). **Note**: If you run this too aggressively, you may reach the [Datadog API limits](https://docs.datadoghq.com/api/latest/rate-limits/).
   1. Save your file and confirm its location.

Once the above is complete:

1. It is best practice to create a virtual environment to install Python packages into. One virtual environment manager is [virtualenv](https://virtualenv.pypa.io/en/stable).
1. Create a new virtual environment in the directory you created earlier by running `virtualenv venv`.
1. Activate the environment by running `source venv/bin/activate` (Mac/Linux) or `> \path\to\env\Scripts\activate` (Windows).
1. Run `pip install datadog` to install the [Datadog API package](https://pypi.org/project/datadog). This enables the Python file to interact with the Datadog API.
1. In the terminal, run the script: `python api_query_data.py`.

If successful, your data displays in the terminal and a file is created in your folder named `out.txt`.

See additional examples in the [Datadog API documentation](https://docs.datadoghq.com/api/).
