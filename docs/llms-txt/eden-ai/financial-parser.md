# Source: https://docs.edenai.co/v3/features/ocr/financial-parser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Financial Parser

> Financial Parser API is a powerful and versatile tool designed to streamline your financial data extraction process. This cutting-edge API combines Optical Character Recognition (OCR) technology with...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `ocr/financial_parser/{provider}[/{model}]`

## Input

| Field          | Type        | Required | Description                                                                                                         |
| -------------- | ----------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| file           | file\_input | Yes      | File ID from /v3/upload or direct file URL                                                                          |
| language       | string      | Yes      | Document language code                                                                                              |
| document\_type | enum        | No       | Specify the type of your document. Can be set to 'auto-detect' for automatic detection if the provider supports it. |

## Output

| Field                                    | Type           | Required | Description                                                                                                       |
| ---------------------------------------- | -------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| **extracted\_data**                      | array\[object] | No       | List of parsed financial data objects (per page).                                                                 |
|     **customer\_information**            | object         | Yes      |                                                                                                                   |
|         name                             | string         | No       | The name of the invoiced customer.                                                                                |
|         id\_reference                    | string         | No       | Unique reference ID for the customer.                                                                             |
|         mailling\_address                | string         | No       | The mailing address of the customer.                                                                              |
|         billing\_address                 | string         | No       | The explicit billing address for the customer.                                                                    |
|         shipping\_address                | string         | No       | The shipping address for the customer.                                                                            |
|         service\_address                 | string         | No       | The service address associated with the customer.                                                                 |
|         remittance\_address              | string         | No       | The address to which payments should be remitted.                                                                 |
|         email                            | string         | No       | The email address of the customer.                                                                                |
|         phone                            | string         | No       | The phone number associated with the customer.                                                                    |
|         vat\_number                      | string         | No       | VAT (Value Added Tax) number of the customer.                                                                     |
|         abn\_number                      | string         | No       | ABN (Australian Business Number) of the customer.                                                                 |
|         gst\_number                      | string         | No       | GST (Goods and Services Tax) number of the customer.                                                              |
|         pan\_number                      | string         | No       | PAN (Permanent Account Number) of the customer.                                                                   |
|         business\_number                 | string         | No       | Business registration number of the customer.                                                                     |
|         siret\_number                    | string         | No       | SIRET (Système d'Identification du Répertoire des Entreprises et de leurs Établissements) number of the customer. |
|         siren\_number                    | string         | No       | SIREN (Système d'Identification du Répertoire des Entreprises) number of the customer.                            |
|         customer\_number                 | string         | No       | Customer identification number.                                                                                   |
|         coc\_number                      | string         | No       | Chamber of Commerce registration number.                                                                          |
|         fiscal\_number                   | string         | No       | Fiscal identification number of the customer.                                                                     |
|         registration\_number             | string         | No       | Official registration number of the customer.                                                                     |
|         tax\_id                          | string         | No       | Tax identification number of the customer.                                                                        |
|         website                          | string         | No       | The website associated with the customer.                                                                         |
|         remit\_to\_name                  | string         | No       | The name associated with the customer's remittance address.                                                       |
|         city                             | string         | No       | The city associated with the customer's address.                                                                  |
|         country                          | string         | No       | The country associated with the customer's address.                                                               |
|         house\_number                    | string         | No       | The house number associated with the customer's address.                                                          |
|         province                         | string         | No       | The province associated with the customer's address.                                                              |
|         street\_name                     | string         | No       | The street name associated with the customer's address.                                                           |
|         zip\_code                        | string         | No       | The ZIP code associated with the customer's address.                                                              |
|         municipality                     | string         | No       | The municipality associated with the customer's address.                                                          |
|     **merchant\_information**            | object         | Yes      |                                                                                                                   |
|         name                             | string         | No       | Name of the merchant.                                                                                             |
|         address                          | string         | No       | Address of the merchant.                                                                                          |
|         phone                            | string         | No       | Phone number of the merchant.                                                                                     |
|         tax\_id                          | string         | No       | Tax identification number of the merchant.                                                                        |
|         id\_reference                    | string         | No       | Unique reference ID for the merchant.                                                                             |
|         vat\_number                      | string         | No       | VAT (Value Added Tax) number of the merchant.                                                                     |
|         abn\_number                      | string         | No       | ABN (Australian Business Number) of the merchant.                                                                 |
|         gst\_number                      | string         | No       | GST (Goods and Services Tax) number of the merchant.                                                              |
|         business\_number                 | string         | No       | Business registration number of the merchant.                                                                     |
|         siret\_number                    | string         | No       | SIRET (Système d'Identification du Répertoire des Entreprises et de leurs Établissements) number of the merchant. |
|         siren\_number                    | string         | No       | SIREN (Système d'Identification du Répertoire des Entreprises) number of the merchant.                            |
|         pan\_number                      | string         | No       | PAN (Permanent Account Number) of the merchant.                                                                   |
|         coc\_number                      | string         | No       | Chamber of Commerce registration number of the merchant.                                                          |
|         fiscal\_number                   | string         | No       | Fiscal identification number of the merchant.                                                                     |
|         email                            | string         | No       | Email address of the merchant.                                                                                    |
|         fax                              | string         | No       | Fax number of the merchant.                                                                                       |
|         website                          | string         | No       | Website of the merchant.                                                                                          |
|         registration                     | string         | No       | Official registration information of the merchant.                                                                |
|         city                             | string         | No       | City associated with the merchant's address.                                                                      |
|         country                          | string         | No       | Country associated with the merchant's address.                                                                   |
|         house\_number                    | string         | No       | House number associated with the merchant's address.                                                              |
|         province                         | string         | No       | Province associated with the merchant's address.                                                                  |
|         street\_name                     | string         | No       | Street name associated with the merchant's address.                                                               |
|         zip\_code                        | string         | No       | ZIP code associated with the merchant's address.                                                                  |
|         country\_code                    | string         | No       | Country code associated with the merchant's location.                                                             |
|     **payment\_information**             | object         | Yes      |                                                                                                                   |
|         amount\_due                      | float          | No       | Amount due for payment.                                                                                           |
|         amount\_tip                      | float          | No       | Tip amount in a financial transaction.                                                                            |
|         amount\_shipping                 | float          | No       | Shipping cost in a financial transaction.                                                                         |
|         amount\_change                   | float          | No       | Change amount in a financial transaction.                                                                         |
|         amount\_paid                     | float          | No       | Amount already paid in a financial transaction.                                                                   |
|         total                            | float          | No       | Total amount in the invoice.                                                                                      |
|         subtotal                         | float          | No       | Subtotal amount in a financial transaction.                                                                       |
|         total\_tax                       | float          | No       | Total tax amount in a financial transaction.                                                                      |
|         tax\_rate                        | float          | No       | Tax rate applied in a financial transaction.                                                                      |
|         discount                         | float          | No       | Discount amount applied in a financial transaction.                                                               |
|         gratuity                         | float          | No       | Gratuity amount in a financial transaction.                                                                       |
|         service\_charge                  | float          | No       | Service charge in a financial transaction.                                                                        |
|         previous\_unpaid\_balance        | float          | No       | Previous unpaid balance in a financial transaction.                                                               |
|         prior\_balance                   | float          | No       | Prior balance before the current financial transaction.                                                           |
|         payment\_terms                   | string         | No       | Terms and conditions for payment.                                                                                 |
|         payment\_method                  | string         | No       | Payment method used in the financial transaction.                                                                 |
|         payment\_card\_number            | string         | No       | Card number used in the payment.                                                                                  |
|         payment\_auth\_code              | string         | No       | Authorization code for the payment.                                                                               |
|         shipping\_handling\_charge       | float          | No       | Charge for shipping and handling in a financial transaction.                                                      |
|         transaction\_number              | string         | No       | Unique identifier for the financial transaction.                                                                  |
|         transaction\_reference           | string         | No       | Reference number for the financial transaction.                                                                   |
|     **financial\_document\_information** | object         | Yes      |                                                                                                                   |
|         invoice\_receipt\_id             | string         | No       | Identifier for the invoice.                                                                                       |
|         purchase\_order                  | string         | No       | Purchase order related to the document.                                                                           |
|         invoice\_date                    | string         | No       | Date of the invoice.                                                                                              |
|         time                             | string         | No       | Time associated with the document.                                                                                |
|         invoice\_due\_date               | string         | No       | Due date for the invoice.                                                                                         |
|         service\_start\_date             | string         | No       | Start date of the service associated with the document.                                                           |
|         service\_end\_date               | string         | No       | End date of the service associated with the document.                                                             |
|         reference                        | string         | No       | Reference number associated with the document.                                                                    |
|         biller\_code                     | string         | No       | Biller code associated with the document.                                                                         |
|         order\_date                      | string         | No       | Date of the order associated with the document.                                                                   |
|         tracking\_number                 | string         | No       | Tracking number associated with the document.                                                                     |
|         **barcodes**                     | array\[object] | No       | List of barcodes associated with the document.                                                                    |
|             value                        | string         | Yes      |                                                                                                                   |
|             type                         | string         | Yes      |                                                                                                                   |
|     **local**                            | object         | Yes      |                                                                                                                   |
|         currency                         | string         | No       | Currency used in financial transactions.                                                                          |
|         currency\_code                   | string         | No       | Currency code (e.g., USD, EUR).                                                                                   |
|         currency\_exchange\_rate         | string         | No       | Exchange rate for the specified currency.                                                                         |
|         country                          | string         | No       | Country associated with the local financial information.                                                          |
|         language                         | string         | No       | Language used in financial transactions.                                                                          |
|     **bank**                             | object         | Yes      |                                                                                                                   |
|         iban                             | string         | No       | International Bank Account Number.                                                                                |
|         swift                            | string         | No       | Society for Worldwide Interbank Financial Telecommunication code.                                                 |
|         bsb                              | string         | No       | Bank State Branch code (Australia).                                                                               |
|         sort\_code                       | string         | No       | Sort code for UK banks.                                                                                           |
|         account\_number                  | string         | No       | Bank account number.                                                                                              |
|         routing\_number                  | string         | No       | Routing number for banks in the United States.                                                                    |
|         bic                              | string         | No       | Bank Identifier Code.                                                                                             |
|     **item\_lines**                      | array\[object] | No       | List of line items associated with the document.                                                                  |
|         tax                              | float          | No       | Tax amount for the line item.                                                                                     |
|         amount\_line                     | float          | No       | Total amount for the line item.                                                                                   |
|         description                      | string         | No       | Description of the line item.                                                                                     |
|         quantity                         | float          | No       | Quantity of units for the line item.                                                                              |
|         unit\_price                      | float          | No       | Unit price for each unit in the line item.                                                                        |
|         unit\_type                       | string         | No       | Type of unit (e.g., hours, items).                                                                                |
|         date                             | string         | No       | Date associated with the line item.                                                                               |
|         product\_code                    | string         | No       | Product code or identifier for the line item.                                                                     |
|         purchase\_order                  | string         | No       | Purchase order related to the line item.                                                                          |
|         tax\_rate                        | float          | No       | Tax rate applied to the line item.                                                                                |
|         base\_total                      | float          | No       | Base total amount before any discounts or taxes.                                                                  |
|         sub\_total                       | float          | No       | Subtotal amount for the line item.                                                                                |
|         discount\_amount                 | float          | No       | Amount of discount applied to the line item.                                                                      |
|         discount\_rate                   | float          | No       | Rate of discount applied to the line item.                                                                        |
|         discount\_code                   | string         | No       | Code associated with any discount applied to the line item.                                                       |
|         order\_number                    | string         | No       | Order number associated with the line item.                                                                       |
|         title                            | string         | No       | Title or name of the line item.                                                                                   |
|     **document\_metadata**               | object         | Yes      |                                                                                                                   |
|         document\_index                  | int            | No       | Index of the detected document.                                                                                   |
|         document\_page\_number           | int            | No       | Page number within the document.                                                                                  |
|         document\_type                   | string         | No       | Type or category of the document.                                                                                 |

## Available Providers

| Provider        | Model String                         | Price           |
| --------------- | ------------------------------------ | --------------- |
| affinda         | `ocr/financial_parser/affinda`       | \$0.07 per page |
| amazon          | `ocr/financial_parser/amazon`        | \$0.01 per page |
| base64          | `ocr/financial_parser/base64`        | \$0.25 per page |
| eagledoc        | `ocr/financial_parser/eagledoc`      | \$0.03 per page |
| extracta        | `ocr/financial_parser/extracta`      | \$0.1 per page  |
| google          | `ocr/financial_parser/google`        | \$0.01 per page |
| klippa          | `ocr/financial_parser/klippa`        | \$0.1 per file  |
| microsoft       | `ocr/financial_parser/microsoft`     | \$0.01 per page |
| mindee          | `ocr/financial_parser/mindee`        | \$0.1 per page  |
| openai          | `ocr/financial_parser/openai`        | \$0.04 per page |
| openai (gpt-4o) | `ocr/financial_parser/openai/gpt-4o` | \$0.04 per page |
| tabscanner      | `ocr/financial_parser/tabscanner`    | \$0.08 per page |
| veryfi          | `ocr/financial_parser/veryfi`        | \$0.16 per file |

## Quick Start

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "ocr/financial_parser/affinda",
      "input": {
          "file": "YOUR_FILE_UUID_OR_URL",
          "language": "en"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/universal-ai \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "ocr/financial_parser/affinda",
      "input": {"file": "YOUR_FILE_UUID_OR_URL", "language": "en"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).