# Source: https://docs.startree.ai/thirdeye/how-tos/database.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect a Data Source

A `datasource` is an entity, such as an Apache Pinot instance. Data sources must be registered in ThirdEye to enable ThirdEye to use them. A datasource can have many `datasets` which are like tables. Those datasets can have many `metrics`.

Currently ThirdEye supports connecting with Apache Pinot. To connect to other data sources, [reach out to StarTree](https://startree.ai/demo).

## Steps to register a new datasource

<p>
  <img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/AddDatasource.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=23f4807baa33afa70654848864ead20b" alt="Add Datasource" width="1640" data-path="img/thirdeye/AddDatasource.png" />
</p>

1. Visit the Configuration Page
2. Click on Create
3. Click on "Create Datasource"

<p>
  <img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/AddDatasourceForm.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=49155275ecd07bf02f0851a4a9d21186" alt="Add Datasource Form" width="1640" data-path="img/thirdeye/AddDatasourceForm.png" />
</p>

1. Enter the configuration for your datasource
2. Optionally you can choose to auto onboard all the datasets that currently exist in the datasource. Note that this is the only time you can do this
3. Click Next and Finish

## Steps to add a new dataset

<p>
  <img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/AddDataset.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=5ccdf8a686aa74eb1ed205bbf669ab01" alt="Add Dataset" width="1640" data-path="img/thirdeye/AddDataset.png" />
</p>

1. Visit the Configuration Page
2. Click on Create
3. Click on "Onboard Dataset"

<p>
  <img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/AddDatasetForm.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=e40250941d2e520145153eefb0b564ad" alt="Add Dataset" width="1640" data-path="img/thirdeye/AddDatasetForm.png" />
</p>

1. Enter the name of the dataset you want to add. Make sure its the exact table name
2. Choose the datasource the dataset is from
3. Click Next and Finish

Built with [Mintlify](https://mintlify.com).
