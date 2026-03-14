# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_extract.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_EXTRACT

Extracts information from an input string or file.

## Syntax

**Extract information from an input string:**

```sqlsyntax
AI_EXTRACT( <text>, <responseFormat> )
```

```sqlsyntax
AI_EXTRACT( text => <text>,
            responseFormat => <responseFormat> )
```

**Extract information from a file:**

```sqlsyntax
AI_EXTRACT( <file>, <responseFormat> )
```

```sqlsyntax
AI_EXTRACT( file => <file>,
            responseFormat => <responseFormat> )
```

## Arguments

`text`
:   An input string for extraction.

`file`
:   A [FILE](../data-types-unstructured.md) for extraction.

    Supported file formats:

    * PDF
    * PNG
    * PPTX, PPT
    * EML
    * DOC, DOCX
    * JPEG, JPG
    * HTM, HTML
    * TEXT, TXT
    * TIF, TIFF
    * BMP, GIF, WEBP
    * MD

    The files must be less than 100 MB in size.

`responseFormat`
:   Information to be extracted. The format depends on the type of extraction.

    **Entity extraction formats**

    Extract single values by providing one of the following formats:

    * Simple object schema that maps the label and information to be extracted:

      ```output
      {'name': 'What is the last name of the employee?', 'address': 'What is the address of the employee?'}
      ```
    * An array of strings that contain the information to be extracted:

      ```output
      ['What is the last name of the employee?', 'What is the address of the employee?']
      ```
    * An array of arrays that contain two strings (label and the information to be extracted):

      ```output
      [['name', 'What is the last name of the employee?'], ['address', 'What is the address of the employee?']]
      ```
    * A JSON schema with `'type': 'string'` on the sub-object:

      ```output
      {
        'schema': {
          'type': 'object',
          'properties': {
            'title': {
              'description': 'What is the title of the document?',
              'type': 'string'
            }
          }
        }
      }
      ```

    **List extraction format**

    Extract arrays of values using a JSON schema with `'type': 'array'` on the sub-object:

    ```output
    {
      'schema': {
        'type': 'object',
        'properties': {
          'employees': {
            'description': 'What are the names of employees?',
            'type': 'array'
          }
        }
      }
    }
    ```

    **Table extraction format**

    Extract tabular data using a JSON schema with `'type': 'object'` and `column_ordering`. Each column is defined as a
    nested property with `'type': 'array'` and a `description` that matches the column name in the file:

    ```output
    {
      'schema': {
        'type': 'object',
        'properties': {
          'income_table': {
            'description': 'Income for FY2026Q2',
            'type': 'object',
            'column_ordering': ['month', 'income'],
            'properties': {
              'month': {
                'description': 'Month',
                'type': 'array'
              },
              'income': {
                'description': 'Income',
                'type': 'array'
              }
            }
          }
        }
      }
    }
    ```

    > **Note:**
    >
    > * You can’t combine the JSON schema format with other response formats. If `responseFormat` contains the `schema` key,
    >   you must define all questions within the JSON schema. Additional keys are not supported.
    > * The model only accepts certain shapes of JSON schema. Top level type must always be an object, which contains independently extracted sub-objects.
    >   Sub-objects may be a table (object of lists of strings representing columns), a list of strings, or a string.
    >
    >   String is currently the only supported scalar type.
    > * Use the `description` field to provide context to the model; for example, to help the model localize the right table in a document. You can enter the column header name,
    >   or describe the column in other way.
    > * Use the `column_ordering` field to specify the order of all columns in the extracted table. The `column_ordering` field is case-sensitive and must match
    >   the column names defined in the `properties` field. The order should reflect the order of the columns in the document.

## Returns

A JSON object containing the extracted information. The structure of the response depends on the type of extraction.

### Entity extraction

Returns a JSON object with key-value pairs for each extracted entity:

```output
{
  "error": null,
  "response": {
    "title": "Financial report"
  }
}
```

### List extraction

Returns a JSON object with arrays of extracted values:

```output
{
  "error": null,
  "response": {
    "employees": [
      "Smith",
      "Johnson",
      "Doe"
    ]
  }
}
```

### Table extraction

Returns a JSON object with column arrays representing the extracted table:

```output
{
  "error": null,
  "response": {
    "income_table": {
      "income": ["$120 678","$130 123","$150 998"],
      "month": ["February", "March", "April"]
    }
  }
}
```

### Combined extraction

When extracting entities, lists, and tables in a single call, the response contains all extraction types:

```output
{
  "error": null,
  "response": {
    "employees": [
      "Smith",
      "Johnson",
      "Doe"
    ],
    "income_table": {
      "income": ["$120 678","$130 123","$150 998"],
      "month": ["February", "March", "April"]
    },
    "title": "Financial report"
  }
}
```

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
For information about granting this privilege, see [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md).

## Usage notes

* AI_EXTRACT is optimized for documents both digital-born and scanned.
* You can’t use both `text` and `file` parameters simultaneously in the same function call.
* You can either ask questions in natural language or describe information to be extracted (such as city, street, ZIP code); for example:

  > ```output
  > ['address': 'City, street, ZIP', 'name': 'First and last name']
  > ```
>
* The following languages are supported:

  * Arabic
  * Bengali
  * Burmese
  * Cebuano
  * Chinese
  * Czech
  * Dutch
  * English
  * French
  * German
  * Hebrew
  * Hindi
  * Indonesian
  * Italian
  * Japanese
  * Khmer
  * Korean
  * Lao
  * Malay
  * Persian
  * Polish
  * Portuguese
  * Russian
  * Spanish
  * Tagalog
  * Thai
  * Turkish
  * Urdu
  * Vietnamese
* The documents must be no more than 125 pages long.
* In a single AI_EXTRACT call, you can ask a maximum of 100 questions for entity extraction, and a maximum of 10 questions for table extraction.

  A table extraction question is equal to 10 entity extraction questions. For example, you can ask 4 table extraction questions and
  60 entity extraction questions in a single AI_EXTRACT call.
* The maximum output length for entity extraction is 512 tokens per question. For table extraction, the model returns answers that are a maximum of 4096 tokens.
* Client-side encrypted stages are not supported.
* Confidence scores are not supported.

## Cost considerations

The Cortex AI_EXTRACT function incurs compute cost based on the number of pages per document, input prompt tokens, and
output tokens processed.

* For paged file formats (PDF, DOCX, TIF, TIFF), each page is counted as 970 tokens.
* For image file formats (JPEG, JPG, PNG), each individual image file is billed as a page and counted as 970 tokens.

Snowflake recommends executing queries that call the Cortex AI_EXTRACT function in a smaller warehouse (no larger than
MEDIUM). Larger warehouses do not increase performance.

## Regional availability

AI_EXTRACT is available to accounts in the following regions:

| Cloud platform | Region name |
| --- | --- |
| Amazon Web Services (AWS) | *US East (N. Virginia)* US West (Oregon) *Canada (Central)* South America (Sao Paulo) *EU (Ireland)* EU (Frankfurt) *Asia Pacific (Tokyo)* Asia Pacific (Sydney) |
| Microsoft Azure | *East US 2 (Virginia)* West US 2 (Washington) *South Central US (Texas)* North Europe (Ireland) *West Europe (Netherlands)* Southeast Asia (Singapore) *Australia East (New South Wales)* Central India (Pune) * Japan East (Tokyo) |

AI_EXTRACT has cross-region support. For information on enabling Cortex AI cross-region support,
see [Cross-region inference](../../user-guide/snowflake-cortex/cross-region-inference.md).

## Error conditions

AI_EXTRACT can produce the following error messages:

| Message | Explanation |
| --- | --- |
| `Internal error.` | A system error occurred. Wait and try again. If the error persists, contact Snowflake support. |
| `Not found.` | The file was not found. |
| `Provided file cannot be found.` | The file was not found. |
| `Provided file cannot be accessed.` | The current user does not have sufficient privileges too access the file. |
| `The provided file format {file_extension} isn't supported.` | The document is not in a supported format. |
| `The provided file isn't in the expected format or is client-side encrypted or is corrupted.` | The document is not stored in a stage with server-side encryption. |
| `Empty request.` | No parameters were provided. |
| `Missing or empty response format.` | No response format was provided. |
| `Invalid response format.` | The response format is not valid JSON. |
| `Duplicate feature name found: {feature_name}.` | The response format contains one or more duplicate feature names. |
| `Too many questions: {number} complex and {number} simple = {number} total, complex question weight {number}`. | The number of questions exceeds the allowed limit. |
| `Maximum number of 125 pages exceeded. The document has {actual_pages} pages.` | The document exceeds the 125-page limit. |
| `Page size in pixels exceeds 10000x10000. The page size is {actual_px} pixels.` | Image input or a converted document page is larger than the supported dimensions. |
| `Page size in inches exceeds 50x50 (3600x3600 pt). The page size is {actual_in} inches ({actual_pt} pt).` | Page is larger than the supported dimensions. |
| `Maximum file size of 104857600 bytes exceeded. The file size is {actual_size} bytes.` | The document is larger than 100 MB. |

## Examples

### Entity extraction

* The following example extracts entities from the input text using a simple object schema:

  ```sqlexample
  SELECT AI_EXTRACT(
    text => 'John Smith lives in San Francisco and works for Snowflake',
    responseFormat => {'name': 'What is the first name of the employee?', 'city': 'What is the address of the employee?'}
  );
  ```

* The following example extracts and parses entities from the input text:

  ```sqlexample
  SELECT AI_EXTRACT(
    text => 'John Smith lives in San Francisco and works for Snowflake',
    responseFormat => PARSE_JSON('{"name": "What is the first name of the employee?", "address": "What is the address of the employee?"}')
  );
  ```

* The following example extracts entities from the `document.pdf` file:

  ```sqlexample
  SELECT AI_EXTRACT(
    file => TO_FILE('@db.schema.files','document.pdf'),
    responseFormat => [['name', 'What is the first name of the employee?'], ['city', 'Where does the employee live?']]
  );
  ```

* The following example extracts entities from all files in a directory on a stage:

  > **Note:**
  >
  > Ensure that the directory table is enabled. For more information, see [Manage directory tables](../../user-guide/data-load-dirtables-manage.md).

  ```sqlexample
  SELECT AI_EXTRACT(
    file => TO_FILE('@db.schema.files', relative_path),
    responseFormat => [
      'What is the document ID?',
      'What is the address of the company?'
    ]
  ) FROM DIRECTORY (@db.schema.files);
  ```

* The following example extracts the `title` entity from the `report.pdf` file using a JSON schema:

  ```sqlexample
  SELECT AI_EXTRACT(
    file => TO_FILE('@db.schema.files', 'report.pdf'),
    responseFormat => {
      'schema': {
        'type': 'object',
        'properties': {
          'title': {
            'description': 'What is the title of document?',
            'type': 'string'
          }
        }
      }
    }
  );
  ```

### List extraction

The following example extracts the `employees` list from the `report.pdf` file:

```sqlexample
SELECT AI_EXTRACT(
  file => TO_FILE('@db.schema.files', 'report.pdf'),
  responseFormat => {
    'schema': {
      'type': 'object',
      'properties': {
        'employees': {
          'description': 'What are the surnames of employees?',
          'type': 'array'
        }
      }
    }
  }
);
```

### Table extraction

The following example extracts the `income_table` table from the `report.pdf` file:

```sqlexample
SELECT AI_EXTRACT(
  file => TO_FILE('@db.schema.files', 'report.pdf'),
  responseFormat => {
    'schema': {
      'type': 'object',
      'properties': {
        'income_table': {
          'description': 'Income for FY2026Q2',
          'type': 'object',
          'column_ordering': ['month', 'income'],
          'properties': {
            'month': {
              'description': 'Month',
              'type': 'array'
            },
            'income': {
              'description': 'Income',
              'type': 'array'
            }
          }
        }
      }
    }
  }
);
```

### Combined extraction

The following example extracts a table (`income_table`), entity (`title`), and list (`employees`) from the `report.pdf`
file in a single call:

```sqlexample
SELECT AI_EXTRACT(
  file => TO_FILE('@db.schema.files', 'report.pdf'),
  responseFormat => {
    'schema': {
      'type': 'object',
      'properties': {
        'income_table': {
          'description': 'Income for FY2026Q2',
          'type': 'object',
          'column_ordering': ['month', 'income'],
          'properties': {
            'month': {
              'description': 'Month',
              'type': 'array'
            },
            'income': {
              'description': 'Income',
              'type': 'array'
            }
          }
        },
        'title': {
          'description': 'What is the title of document?',
          'type': 'string'
        },
        'employees': {
          'description': 'What are the surnames of employees?',
          'type': 'array'
        }
      }
    }
  }
);
```

### Extraction using a fine-tuned `arctic-extract` model

To use the fine-tuned `arctic-extract` model for inference with the AI_EXTRACT function,
specify the model using the `model` parameter as shown in the following example:

```sqlexample
SELECT AI_EXTRACT(
  model => 'db.schema.my_tuned_model',
  file => TO_FILE('@db.schema.files','document.pdf')
);
```

You can overwrite questions used for fine-tuning by using the `responseFormat` parameter as shown in the following example:

```sqlexample
SELECT AI_EXTRACT(
  model => 'db.schema.my_tuned_model',
  file => TO_FILE('@db.schema.files','document.pdf'),
  responseFormat => [['name', 'What is the first name of the employee?'], ['city', 'Where does the employee live?']]
);
```

For more information, see [Fine-tuning arctic-extract models](../../user-guide/snowflake-cortex/arctic-extract-finetuning.md).

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md) for legal notices.
