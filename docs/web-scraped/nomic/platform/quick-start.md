# Nomic Documentation

Source: https://docs.nomic.ai/platform/quick-start

## Create Account​

Visit the Nomic Plaform and sign up for a free account. You'll then be asked to onboard your organization and get started with our Developer API's.

## Platform Dashboard​

Once you are signed up for the Nomic Platform and logged in, visit https://atlas.nomic.ai/data to open your Dashboard.

Your organization's files, documents and Datasets live in the datasets tab. For new organizations with no datasets yet, you will be prompted to create one.

## Dataset Creation​

Here are a few pathways available to bring data into the Nomic Platform:

### Using an Integration​

This path involves using an integration to bring in a dataset from an external platform (e.g.Hugging Face integration).

Your browser does not support the video tag.

### Drag & Drop Upload​

Datasets lets you take a row-orientated data format (in CSV, TSV JSON, or JSONL format) and upload it directly into a Dataset. Platform uses DuckDB to intelligently parse and infer the types in your CSV files.

Your browser does not support the video tag.

Visit our Dataset docs for more information about acceptable data formats and options for dataset upload and configuration. For specific details on how CSV files are parsed and how data types are inferred, see the section on CSV parsing with DuckDB.

### SDK upload​

Here is an example of using the Atlas Python SDK to upload data for an Atlas data map.

First, login to Nomic with your API key at your terminal/command line:

```
nomic login nk-...
```

Then, create a dataset and add your data (e.g. as a pandas DataFrame), and create a map from it:

```
from nomic import AtlasDatasetimport pandas as pddf = pd.read_csv('https://docs.nomic.ai/singapore_airlines_reviews.csv')dataset = AtlasDataset("example-dataset-airline-reviews")dataset.add_data(df)atlas_map = dataset.create_index(indexed_field='text')
```

Developers can see more examples of uploading data to Atlas in our Python SDK documentation.

- Create Account
- Platform Dashboard
- Dataset CreationUsing an IntegrationDrag & Drop UploadSDK upload
- Using an Integration
- Drag & Drop Upload
- SDK upload
