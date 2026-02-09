# Source: https://docs.unstructured.io/examplecode/codesamples/apioss/table-extraction-from-pdf.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Table extraction from PDF

> This section describes two methods for extracting tables from PDF files.

<Note>
  This sample code utilizes the [Unstructured Open Source](/open-source/introduction/overview "Open Source") library and also provides an alternative method the utilizing the legacy [Unstructured Partition Endpoint](/api-reference/legacy-api/partition/overview).
</Note>

## Method 1: Using partition\_pdf

To extract the tables from PDF files using the [partition\_pdf](/open-source/core-functionality/partitioning#partition-pdf), set the `skip_infer_table_types` parameter to `False` and `strategy` parameter to `hi_res`.

**Usage**

```python  theme={null}
from unstructured.partition.pdf import partition_pdf

fname = "example-docs/pdf/layout-parser-paper.pdf"

elements = partition_pdf(filename=fname,
                         skip_infer_table_types=False,
                         strategy='hi_res',
           )

tables = [el for el in elements if el.category == "Table"]

print(tables[0].text)
print(tables[0].metadata.text_as_html)

```

## Method 2: Using Auto Partition or Unstructured API

By default, table extraction from all file types is enabled. To extract tables from PDFs and images using [Auto Partition](/open-source/core-functionality/partitioning#partition) or [Unstructured API parameters](/api-reference/legacy-api/partition/api-parameters) simply set `strategy` parameter to `hi_res`.

**Usage: Auto Partition**

```python  theme={null}
from unstructured.partition.auto import partition

filename = "example-docs/pdf/layout-parser-paper.pdf"

elements = partition(filename=filename,
                     strategy='hi_res',
           )

tables = [el for el in elements if el.category == "Table"]

print(tables[0].text)
print(tables[0].metadata.text_as_html)

```

**Usage: API Parameters**

```bash  theme={null}
curl -X 'POST' \
    'https://api.unstructured.io' \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'files=@sample-docs/layout-parser-paper-with-table.jpg' \
    -F 'strategy=hi_res' \
    | jq -C . | less -R

```
