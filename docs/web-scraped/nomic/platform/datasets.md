# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/

### Prepare Data for Atlas

Learn how to prepare and format your data for analysis in Atlas

### Export Spreadsheet Data

Export data from common spreadsheet platforms to analyze in Atlas

Atlas Datasets are the foundation for storing and managing data in Atlas. They provide a scalable, columnar storage format that supports text, images, and embeddings.

## Core Concepts​

Atlas Datasets store data in a columnar format optimized for large-scale operations. When you create a dataset, Atlas automatically handles data partitioning, caching, and synchronization between your local environment and Atlas servers. This enables efficient access to large datasets without loading everything into memory at once.

Each dataset belongs to an organization and has a unique identifier in the format organization-name/dataset-name. Datasets can be public (accessible to anyone) or private (accessible only to organization members).

Every Atlas Dataset can have one or more maps. While the dataset stores your raw data, maps provide additional resources and Atlas-generated metadata for visualization and interaction.

Think of a Atlas Dataset as the source of truth for your data, and an Atlas Data Map as a snapshot of the data in time.

To work with Atlas Datasets, you typically follow these steps:

- Create or Load: Initialize a dataset by specifying an organization and dataset name. You can create a new dataset or load an existing one.
Create or Load: Initialize a dataset by specifying an organization and dataset name. You can create a new dataset or load an existing one.

- Add Data: Add data to your dataset in batches. Atlas supports various input formats including lists of dictionaries, pandas DataFrames, and PyArrow Tables.
Add Data: Add data to your dataset in batches. Atlas supports various input formats including lists of dictionaries, pandas DataFrames, and PyArrow Tables.

- Create Maps: Atlas will automatically generate embeddings and other useful resources for your dataset.
Create Maps: Atlas will automatically generate embeddings and other useful resources for your dataset.

- Operationalize Data: Vector search, retrieval, RAG integrations can now use your Atlas Dataset.
Operationalize Data: Vector search, retrieval, RAG integrations can now use your Atlas Dataset.

## Data Types and Storage​

Atlas natively supports several data types:

- Text documents and metadata
Text documents and metadata

- Images (as files or URLs)
Images (as files or URLs)

- Embedding vectors (high-dimensional numerical arrays)
Embedding vectors (high-dimensional numerical arrays)

Data is stored in Apache Arrow format, providing efficient memory usage and fast data access. When you interact with a dataset, Atlas dynamically loads data to your local environment with automatic caching.

## Best Practices​

When working with Atlas Datasets:

- Data cannot be added while a map is building
Data cannot be added while a map is building

- Use descriptive dataset names that reflect the content
Use descriptive dataset names that reflect the content

- Specify a unique ID field when creating datasets to ensure consistent data tracking
Specify a unique ID field when creating datasets to ensure consistent data tracking

- Batch large data uploads into manageable chunks
Batch large data uploads into manageable chunks

- Use PyArrow Tables for memory-efficient data access with large datasets
Use PyArrow Tables for memory-efficient data access with large datasets

- Consider data privacy requirements when setting dataset visibility
Consider data privacy requirements when setting dataset visibility

- Core Concepts
- Data Types and Storage
- Best Practices
