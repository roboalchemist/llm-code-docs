# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition/csv-wizard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CSV Wizard

The CSV Wizard allows users with larger or more complex datasets to easily upload their data without having to worry about converting it to the [data acquisition format](/tools/specifications/data-acquisition/json-cbor).

To access the CSV Wizard, navigate to the **Data Acquisition** tab of your Edge Impulse project and click on the CSV Wizard button:

<Frame caption="Edge Impulse Studio CSV Wizard">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-wizard.PNG?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=dd9e5169015b30260ab85dc3dd6833ce" width="1600" height="470" data-path=".assets/images/csv-wizard.PNG" />
</Frame>

<Info>
  **The CSV Wizard supports** `.csv` **and** `.parquet` **files**

  Although the name of the wizard implies only supporting CSV files, Parquet files are also supported.
</Info>

## How to use the CSV Wizard

We can take a look at some sample data from a Heart Rate Monitor (Polar H10). We can see there is a lot of extra information we don’t need:

<Frame caption="Raw CSV sample.">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-wizard-raw-csv-sample.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=9d0f3c6064ecda092a6cbb6aeb2f2274" width="1600" height="275" data-path=".assets/images/csv-wizard-raw-csv-sample.png" />
</Frame>

### Step 1: Upload a file

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-step-1.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=f3bbe4eac85a5665b93bacc41383ef75" width="1600" height="838" data-path=".assets/images/csv-step-1.png" />
</Frame>

Choose a CSV file to upload and select "Upload File". The file will be automatically analyzed and the results will be displayed in the next step. Here I have selected an export from a HR monitor. You can try it out yourself by downloading this file:

[Download polar\_hr.csv](https://cdn.edgeimpulse.com/datasets/polar_hr.csv)

### Step 2: Analyze your data

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-step-2.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=f32b7c85e4dee1c34b7aa259e3537046" width="1600" height="838" data-path=".assets/images/csv-step-2.png" />
</Frame>

When processing your data, we will check for the following:

* Does this data contain a label?
* Is this data time series data?
* Is this data raw sensor data or processed features?
* Is this data separated by a standard delimiter?
* Is this data separated by a non-standard delimiter?

If there are settings that need to be adjusted, (for the start of your data you can select skip first x lines or no header, and adjust the delimiter) you can do so before selecting **looks good, next**"\*\*.

### Step 3: About your data

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-step-3.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=528b5f4abf82de59b1b4023aa22c5f01" width="1600" height="838" data-path=".assets/images/csv-step-3.png" />
</Frame>

Here you can select the timestamp column, or row and the frequency of the timestamps. If you do not have a timestamp column, you can select **No timestamp column** and add a timestamp later. If you do have a timestamp column you can select: the timestamp format, e.g. full timestamp, and the frequency of the timestamps, overriding is also possible via **Override timestamp difference**. For example Selecting 20000 will give you the detected frequency of: 0.05 Hz.

### Step 4: CSV Wizard: About your values

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-step-4.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=9b2b23d2cfae2c39171af5cb418108db" width="1600" height="838" data-path=".assets/images/csv-step-4.png" />
</Frame>

Here you can select the label column, or row. If you do not have a label column, you can select **No (no worries, you can provide this when you upload data)** and add a label later. If you do have a label column you can select: **Yes it's "Value"** The CSV Wizard allows users with larger or more complex datasets to easily upload their data without having to worry about converting it to CBOR format. You can also select the columns that contain your values.

### Step 5: Split up your samples

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-step-5.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=e4c53b8d5da91905e3a98e36cd632f9e" width="1600" height="787" data-path=".assets/images/csv-step-5.png" />
</Frame>

**How long do you want your samples to be?**

In this section, you can set a length limit to your sample size. For example, if your CSV contains 30 seconds of data, when setting a limit of 3000ms, it will create 10 distinct data samples of 3 seconds.

**How should we deal with multiple labels in a sample?**

See [Multi-label](/studio/projects/data-acquisition/csv-wizard#multi-label) below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-step-6.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=139d2f9c759a5b3db129985437cd6b00" width="1600" height="838" data-path=".assets/images/csv-step-6.png" />
</Frame>

Congratulations! 🚀 You have successfully created a CSV transform with the CSV Wizard. You can now save this transform and use it to process your data.

## Multi-label

If your CSV contains multiple labels, like in this [coffee machine stages dataset](https://cdn.edgeimpulse.com/datasets/coffee_machine_stages_multi_label.zip), in the final step, select:

**How should we **deal with multiple labels in** a sample?**

◉ The sample should have multiple labels

◯ Use the *last* value of "label as the label for each sample (see the table on the right)

<Frame caption="Multi-label workflow">
  <img src="https://mintcdn.com/edgeimpulse/knIbhhrHdvFnasBb/.assets/images/multi-label.gif?s=194ce0db229fd093f55e1f54406038dd" width="1544" height="936" data-path=".assets/images/multi-label.gif" />
</Frame>

<Info>
  **Read on** See the dedicated [multi-label](/studio/projects/data-acquisition/multi-label) documentation page.
</Info>

## What happens next?

<Frame caption="CSV transform saved">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/csv-transform-saved.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=818fa8f9e9bbcef585934fe525d6f1a9" width="1294" height="220" data-path=".assets/images/csv-transform-saved.png" />
</Frame>

Any CSV files that you upload into your project - whether it's through the uploader, the CLI, the API or through data sources - will now be processed according to the rules you set up with the CSV Wizard!

### Troubleshooting

#### Large CSV files

If you're working with large CSV files (over 25,000 rows), you may need to split them into smaller batches before uploading:

**Splitting large CSV files**:

For Windows users, you can use batch scripts or GUI tools to split large CSV files:

* GUI tool: [Split a Huge CSV/Excel file](https://thegeekpage.com/split-a-huge-csv-excel/)
* The documentation above also includes batch script examples for automated splitting

For command-line users, standard shell scripts can be used to split CSV files into manageable chunks before uploading to Edge Impulse.

#### Azure CSV exports

When exporting CSV files from Azure services, be aware of the following:

**Azure limitations**: Azure Resource Graph has a limitation of 25,000 rows for CSV exports. If you're exporting data from Azure services, you may need to limit your output by selecting a smaller set of subscriptions or time ranges. [Read on](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/work-with-data)


Built with [Mintlify](https://mintlify.com).