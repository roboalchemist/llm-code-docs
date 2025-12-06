# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/storage

Storing datasets in the Nomic Platform gives you a data layer to access, update, and operate over the datasets that impact your applications.

Datasets let you upload, store and manipulate data like a standard noSQL document engine. After you upload a dataset, you can add, update, read and delete (CRUD) the data in your dataset via API calls from the Python client.

## What kind of unstructured data can I store?​

Atlas can natively store:

- Embedding vectors
- Text Documents
- Images
Audio, and video as modalities are on their way to Atlas soon!

## How is Atlas different from a noSQL database?​

Unlike existing data stores, Atlas is built with embedding vectors, and maps are first class citizens. Embedding vectors are representations of data that computers can semantically manipulate. Most operations you do in Atlas — like search and de-duplication — are performed on embeddings under the hood.

## Data formats and integrity​

Atlas stores and transfers data using a subset of the Apache Arrow standard.

pyarrow is used to convert python, pandas, and numpy data types to Arrow types;
you can also pass any Arrow table (created by polars, duckdb, pyarrow, etc.) directly to Atlas
and the types will be automatically converted.

```
pyarrow
```

Before being uploaded, all data is converted with the following rules:

- Strings are converted to Arrow strings and stored as UTF-8.
- Integers are converted to 32-bit integers. (In the case that you
have larger integers, they are probably either IDs, in which case you
should convert them to strings;
or they are a field that you want perform analysis on, in which case you should convert them to floats.)
- Floats are converted to 32-bit (single-precision) floats.
- Embeddings, regardless of precision, are uploaded as 16-bit (half-precision) floats, and stored in Arrow as FixedSizeList.
- All dates and datetimes are converted to Arrow timestamps with millisecond precision and no time zone. (If you have a use case that requires timezone information or micro/nanosecond precision, please let us know.)
- Categorical types (called 'dictionary' in Arrow) are supported, but values stored as categorical must be strings.
Other data types (including booleans, binary, lists, and structs) are not supported.
Values stored as a dictionary must be strings.

All fields besides embeddings and the user-specified ID field are nullable.

- What kind of unstructured data can I store?
- How is Atlas different from a noSQL database?
- Data formats and integrity
