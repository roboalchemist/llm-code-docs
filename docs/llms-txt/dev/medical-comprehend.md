# Source: https://dev.writer.com/home/medical-comprehend.md

# Extract entities from unstructured medical text

<Warning>
  **Deprecation notice**: The [medical comprehend API endpoint](/api-reference/tool-api/comprehend-medical) at `/v1/tools/comprehend/medical` is deprecated and will be removed on **December 22, 2025**.

  **Migration path**: Use the [LLM tool](/home/model-delegation) in chat completions to delegate medical analysis tasks to the `palmyra-med` model. This approach provides the same medical analysis capabilities within a chat completion workflow. See the [migration guide](/api-reference/migration-guides/comprehend-medical) for detailed instructions.
</Warning>

The [medical comprehend endpoint](/api-reference/tool-api/comprehend-medical) analyzes unstructured medical text to extract entities and label them with standardized medical codes. Each extracted entity comes with a confidence score, making it useful for processing clinical notes, medical records, and other healthcare-related documents.

## Use cases

* Automating medical records processing and classification
* Extracting diagnosis codes from clinical notes for billing and insurance purposes
* Creating structured datasets from unstructured medical documentation
* Identifying and categorizing medications and their attributes in patient records
* Standardizing medical terminology across different healthcare systems using SNOMED CT codes

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Endpoint overview

**URL:** `POST https://api.writer.com/v1/tools/comprehend/medical`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/tools/comprehend/medical' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --data '{
      "content": "the symptoms are soreness, a temperature and cough", 
      "response_type": "SNOMED CT"
  }'
  ```

  ```python Python theme={null}
  import os
  from writerai import Writer

  client = Writer(
      # This is the default and can be omitted
      api_key=os.environ.get("WRITER_API_KEY"),
  )
  medical = client.tools.comprehend.medical(
      content="the symptoms are soreness, a temperature and cough",
      response_type="Entities",
  )
  print(medical.entities)
  ```

  ```javascript JavaScript theme={null}
  import Writer from 'writer-sdk';

  const client = new Writer({
    apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
  });

  async function main() {
    const medical = await client.tools.comprehend.medical({ content: 'the symptoms are soreness, a temperature and cough', response_type: 'Entities' });

    console.log(medical.entities);
  }

  main();
  ```
</CodeGroup>

### Request body

The request body includes the following parameters:

| Parameter       | Type   | Description                                |
| --------------- | ------ | ------------------------------------------ |
| `content`       | string | **Required.** The medical text to analyze. |
| `response_type` | string | **Required.** The desired response format. |

Response type options include:

* `Entities`: Returns medical entities with their categories.
* `RxNorm`: [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/overview.html) provides normalized names and unique identifiers for medicines and drugs, allowing computer systems to communicate drug-related information efficiently and unambiguously.
* `ICD-10-CM`: [ICD-10-CM](https://www.cdc.gov/nchs/icd/icd-10-cm/index.html) is a standardized system used to code diseases and medical conditions (morbidity) data.
* `SNOMED CT`: [SNOMED CT](https://www.snomed.org/what-is-snomed-ct) is a standardized, multilingual vocabulary of clinical terminology that is used by physicians and other healthcare providers for the electronic exchange of health information.

### Response parameters

Returns an array of medical entities, where each entity includes:

| Parameter    | Type   | Description                                                |
| ------------ | ------ | ---------------------------------------------------------- |
| `category`   | string | The medical category of the entity                         |
| `text`       | string | The actual text that was identified                        |
| `score`      | float  | Confidence score for the entity (0-1)                      |
| `traits`     | array  | Array of trait objects with names and scores               |
| `concepts`   | array  | Array of medical concepts with codes and descriptions      |
| `attributes` | array  | Related attributes with their own scores and relationships |
| `type`       | string | The entity type                                            |

See the full [response schema](/api-reference/tool-api/comprehend-medical) for more details.

```json example response [expandable] theme={null}
{
  "entities": [
    {
      "category": "MEDICAL_CONDITION",
      "begin_offset": 17,
      "end_offset": 25,
      "text": "soreness",
      "traits": [
        {
          "score": 0.5752319693565369,
          "name": "HYPOTHETICAL"
        },
        {
          "score": 0.7299559712409973,
          "name": "SYMPTOM"
        }
      ],
      "concepts": [
        {
          "code": "71393004",
          "score": 0.9435068368911743,
          "description": "Soreness (finding)"
        },
        {
          "code": "279074008",
          "score": 0.27141574025154114,
          "description": "Sore skin (finding)"
        },
        {
          "code": "247348008",
          "score": 0.20372514426708221,
          "description": "Tenderness (finding)"
        },
        {
          "code": "410713007",
          "score": 0.18387910723686218,
          "description": "Sore sensation quality (qualifier value)"
        },
        {
          "code": "267102003",
          "score": 0.15431177616119385,
          "description": "Sore throat symptom (finding)"
        }
      ],
      "score": 0.7172441482543945,
      "attributes": [],
      "type": "DX_NAME"
    },
    {
      "category": "MEDICAL_CONDITION",
      "begin_offset": 29,
      "end_offset": 40,
      "text": "temperature",
      "traits": [
        {
          "score": 0.7299559712409973,
          "name": "HYPOTHETICAL"
        },
        {
          "score": 0.8787732124328613,
          "name": "SYMPTOM"
        }
      ],
      "concepts": [
        {
          "code": "703421000",
          "score": 0.4236489236354828,
          "description": "Temperature (observable entity)"
        },
        {
          "code": "386661006",
          "score": 0.4029766321182251,
          "description": "Fever (finding)"
        },
        {
          "code": "246508008",
          "score": 0.26857706904411316,
          "description": "Temperature (attribute)"
        },
        {
          "code": "56342008",
          "score": 0.26122674345970154,
          "description": "Temperature taking (procedure)"
        },
        {
          "code": "722490005",
          "score": 0.1763012409210205,
          "description": "Temperature (property) (qualifier value)"
        }
      ],
      "score": 0.8435389995574951,
      "attributes": [],
      "type": "DX_NAME"
    },
    {
      "category": "MEDICAL_CONDITION",
      "begin_offset": 45,
      "end_offset": 50,
      "text": "cough",
      "traits": [
        {
          "score": 0.9013108015060425,
          "name": "HYPOTHETICAL"
        },
        {
          "score": 0.9817302823066711,
          "name": "SYMPTOM"
        }
      ],
      "concepts": [
        {
          "code": "49727002",
          "score": 0.9173739552497864,
          "description": "Cough (finding)"
        },
        {
          "code": "263731006",
          "score": 0.20544156432151794,
          "description": "Coughing (observable entity)"
        },
        {
          "code": "247410004",
          "score": 0.18926720321178436,
          "description": "Painful cough (finding)"
        },
        {
          "code": "11833005",
          "score": 0.18911097943782806,
          "description": "Dry cough (finding)"
        },
        {
          "code": "135883003",
          "score": 0.1864289492368698,
          "description": "Cough with fever (finding)"
        }
      ],
      "score": 0.9584784507751465,
      "attributes": [],
      "type": "DX_NAME"
    }
  ]
}
```
