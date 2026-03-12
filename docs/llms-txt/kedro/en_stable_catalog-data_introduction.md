# Source: https://docs.kedro.org/en/stable/catalog-data/introduction/index.md

# Data Catalog

In a Kedro project, the Data Catalog is a registry of all data sources available for use by the project. The catalog is stored in a YAML file (`catalog.yml`) that maps the names of node inputs and outputs as keys in the `DataCatalog` class.

The [kedro-datasets documentation](https://docs.kedro.org/projects/kedro-datasets/en/stable/) package offers built-in datasets for common file types and file systems.

## Introduction to the Data Catalog

We first introduce the basic sections of `catalog.yml`, which is the file used to register data sources for a Kedro project.

- [Introduction to the Data Catalog](https://docs.kedro.org/en/stable/catalog-data/data_catalog/index.md)

## Examples of data catalog YAML

The following page offers a range of examples of YAML specification for various Data Catalog use cases:

- [Data Catalog YAML Examples](https://docs.kedro.org/en/stable/catalog-data/data_catalog_yaml_examples/index.md)

Once you are familiar with the format of `catalog.yml`, you may find your catalog gets repetitive if you need to load multiple datasets with similar configuration. From Kedro 0.18.12 you can use dataset factories to generalise the configuration and reduce the number of similar catalog entries. This works by matching datasets used in your project’s pipelines to dataset factory patterns and is explained in a new page about Kedro dataset factories:

- [Kedro Dataset Factories](https://docs.kedro.org/en/stable/catalog-data/kedro_dataset_factories/index.md)

## Advanced concepts

Further pages describe more advanced concepts:

- [Advanced: Access the Data Catalog in code](https://docs.kedro.org/en/stable/catalog-data/advanced_data_catalog_usage/index.md)
- [Advanced: Lazy loading](https://docs.kedro.org/en/stable/catalog-data/lazy_loading/index.md)
- [Advanced: Partitioned and incremental datasets](https://docs.kedro.org/en/stable/catalog-data/partitioned_and_incremental_datasets/index.md)

This section on handing data with Kedro concludes with an advanced use case, illustrated with a tutorial that explains how to create your own custom dataset:

- [Advanced: Tutorial to create a custom dataset](https://docs.kedro.org/en/stable/extend/how_to_create_a_custom_dataset/index.md)
