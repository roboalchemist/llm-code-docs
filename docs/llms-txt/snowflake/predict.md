# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/methods/predict.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/document-intelligence/methods/predict.md

# <model_build_name>!PREDICT

Extracts information from documents in a stage, and provides answers in a JSON object. If you specify a single document, the method returns results for that document. Otherwise, the method returns results for each document in the stage.

## Syntax

```sqlsyntax
<model_build_name>!PREDICT(<presigned_url>,
                           [ <model_build_version> ]
                          )
```

## Arguments

**Required:**

`presigned_url`
:   Pre-signed URL of the staged documents.

    To get the pre-signed URL to pass in as an argument, call the GET_PRESIGNED_URL function. See [GET_PRESIGNED_URL](../../../functions/get_presigned_url.md).

    For more information, see Example.

    > **Note:**
    >
    > The [GET_PRESIGNED_URL](../../../functions/get_presigned_url.md) function has a default expiration time (60 minutes).
    > For more information about extending the expiration time, see [GET_PRESIGNED_URL](../../../functions/get_presigned_url.md).

**Optional:**

`model_build_version`
:   Version of the Document AI model build.

    If not specified, the latest available model build version is used by default.

## Returns

Returns a JSON object with the following fields:

> `ocrScore`
> :   Specifies the confidence score for the optical character recognition (OCR) process.
>
> `score`
> :   Specifies the confidence score for a specific value.
>
> `value`
> :   Specifies the extracted answer to the question.

### Entity extraction

```json
{
  "__documentMetadata": {
    "ocrScore": 0.918
  },
  "invoice_number": [
    {
      "score": 0.925,
      "value": "123/20"
    }
  ],
  "invoice_items": [
    {
      "score": 0.839,
      "value": "NEW CRUSHED VELVET DIVAN BED"
    },
    {
      "score": 0.839,
      "value": "Vintage Radiator"
    },
    {
      "score": 0.839,
      "value": "Solid Wooden Worktop"
    },
    {
      "score": 0.839,
      "value": "Sienna Crushed Velvet Curtains"
    }
  ],
  "tax_amount": [
    {
      "score": 0.879,
      "value": "77.57"
    }
  ],
  "total_amount": [
    {
      "score": 0.809,
      "value": "465.43 GBP"
    }
  ],
  "buyer_name": [
    {
      "score": 0.925
    }
  ]
  "vendor_name": [
    {
      "score": 0.9,
      "value": "UK Exports & Imports Ltd"
    }
  ]
}
```

### Table extraction

```json
{
  "__documentMetadata": {
    "ocrScore": 0.887
  },
  "table1|gross": [
    {
      "score": 0.961,
      "value": "10"
    },
    {
      "score": 0.961,
      "value": "31"
    },
    {
      "score": 0.961,
      "value": "10"
    }
  ],
  "table1|item": [
    {
      "score": 0.961,
      "value": "apples"
    },
    {
      "score": 0.961,
      "value": "bananas"
    },
    {
      "score": 0.961,
      "value": "pears"
    }
  ],
  "table1|net": [
    {
      "score": 0.961,
      "value": "9"
    },
    {
      "score": 0.961,
      "value": "30"
    },
    {
      "score": 0.961,
      "value": "10"
    }
  ],
  "table1|tax": [
    {
      "score": 0.961,
      "value": "1"
    },
    {
      "score": 0.961,
      "value": "1"
    },
    {
      "score": 0.961
    }
  ],
  "table2|age": [
    {
      "score": 0.894,
      "value": "23"
    },
    {
      "score": 0.894,
      "value": "56"
    },
    {
      "score": 0.894,
      "value": "76"
    },
    {
      "score": 0.894,
      "value": "98"
    }
  ],
"table2|date": [
    {
      "score": 0.894
    },
    {
      "score": 0.894
    },
    {
      "score": 0.894
    },
    {
      "score": 0.894
    }
  ],
"table2|name": [
    {
      "score": 0.894,
      "value": "John"
    },
    {
      "score": 0.894,
      "value": "Ana"
    },
    {
      "score": 0.894,
      "value": "Lisa"
    },
    {
      "score": 0.894,
      "value": "Jerome"
    }
  ],
  "table2|surname": [
    {
      "score": 0.894,
      "value": "Smith"
    },
    {
      "score": 0.894,
      "value": "Nixon"
    },
    {
      "score": 0.894,
      "value": "Gonzales"
    },
    {
      "score": 0.894,
      "value": "Tate"
    }
  ],
"table3|column1": [
    {
      "score": 0.855
    }
  ],
  "table3|column2": [
    {
      "score": 0.855
    }
  ],
  "table3|column3": [
    {
      "score": 0.855
    }
  ]
}
```

## Access control requirements

To extract information with Document AI, you must use an account role that is granted the SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role. For more information, see [Document AI access control](../../../../user-guide/snowflake-cortex/document-ai/setting-up.md).

## Usage notes

* Ensure you meet the prerequisites for using this method. For more information, see [Prerequisites](../../../../user-guide/snowflake-cortex/document-ai/extract-information.md).
* Document AI has a limitation for the number of documents processed in one query. For more information, see [Known limitations to Document AI](../../../../user-guide/snowflake-cortex/document-ai/limitations.md).
* All documents must be in the same directory of the stage.
* Document AI uses directory tables. For more information, see [Query directory tables](../../../../user-guide/data-load-dirtables-query.md).
* The Document AI model can return lists. See the `invoice_items` field as an example.
* If the Document AI model does not find an answer in the document, the model does not return a `value` key. However, it does return the `score` key, which indicates how confident the model is that the document does not contain the answer. See the `buyer_name` field as an example.
* In table extraction, if a cell is empty, the Document AI model does not return a `value` key. However, it does return the `score` key, which indicates how confident the model is that the cell is empty. For example, `table1` contains empty cell in column `age`, `table2` contains a completely empty column `date`, and `table3` is an empty table that only consists of headers.
* In table extraction, the values in the JSON output are provided in the same order as the rows in the table, so columns can be easily joined.

## Example

The following example extracts information from all of the documents on the `pdf_inspections_stage` stage for version `1` of the `inspections` model build:

```sqlexample
SELECT inspections!PREDICT(
  GET_PRESIGNED_URL(@pdf_inspections_stage, RELATIVE_PATH), 1)
  FROM DIRECTORY(@pdf_inspections_stage);
```

The following example extracts information from the `'paystubs/paystub01.pdf'` document on the `pdf_paystubs_stage` stage for version `1` of the `paystubs` model build:

```sqlexample
SELECT paystubs!PREDICT(
  GET_PRESIGNED_URL(@pdf_paystubs_stage, 'paystubs/paystub01.pdf'), 1);
```
