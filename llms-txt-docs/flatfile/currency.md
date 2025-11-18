# Source: https://flatfile.com/docs/plugins/currency.md

# Currency Conversion Plugin

> Automatically converts currency values from a source currency to a target currency using Open Exchange Rates API with support for historical exchange rates.

This plugin automatically converts currency values from a source currency to a target currency for records within a Flatfile Sheet. It utilizes the Open Exchange Rates API to fetch both the latest and historical exchange rates.

The primary use case is for processing financial data, such as transaction logs or expense reports, where amounts need to be standardized into a single currency. The plugin can use a date from another field in the record to fetch the correct historical rate for the conversion. It can optionally store the calculated exchange rate and the date of conversion back into the record. The plugin operates by hooking into the record processing lifecycle, making it a seamless part of the data import process.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-convert-currency
```

## Configuration & Parameters

The plugin requires a configuration object with the following parameters:

### Required Parameters

| Parameter              | Type   | Description                                                            |
| ---------------------- | ------ | ---------------------------------------------------------------------- |
| `sheetSlug`            | string | The slug of the sheet the plugin should operate on                     |
| `sourceCurrency`       | string | The three-letter currency code (e.g., "USD") of the source amounts     |
| `targetCurrency`       | string | The three-letter currency code (e.g., "EUR") to convert the amounts to |
| `amountField`          | string | The field key/slug that contains the numerical amount to be converted  |
| `convertedAmountField` | string | The field key/slug where the converted amount will be stored           |

### Optional Parameters

| Parameter             | Type   | Description                                                                                          | Default Behavior                                 |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `dateField`           | string | The field key/slug containing the date (in YYYY-MM-DD format) for fetching historical exchange rates | Uses current date to fetch latest exchange rates |
| `exchangeRateField`   | string | The field key/slug where the calculated exchange rate for the conversion will be stored              | Exchange rate is not stored on the record        |
| `conversionDateField` | string | The field key/slug where the timestamp of the conversion will be stored in ISO format                | Conversion date is not stored on the record      |

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from "@flatfile/listener";
  import { currencyConverterPlugin } from "@flatfile/plugin-convert-currency";

  export default function (listener) {
    listener.use(
      currencyConverterPlugin({
        sheetSlug: "transactions",
        sourceCurrency: "USD",
        targetCurrency: "EUR",
        amountField: "amount",
        convertedAmountField: "amountInEUR",
      })
    );
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener } from "@flatfile/listener";
  import { currencyConverterPlugin } from "@flatfile/plugin-convert-currency";

  export default function (listener: FlatfileListener) {
    listener.use(
      currencyConverterPlugin({
        sheetSlug: "transactions",
        sourceCurrency: "USD",
        targetCurrency: "EUR",
        amountField: "amount",
        convertedAmountField: "amountInEUR",
      })
    );
  }
  ```
</CodeGroup>

### Full Configuration with Historical Rates

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from "@flatfile/listener";
  import { currencyConverterPlugin } from "@flatfile/plugin-convert-currency";

  export default function (listener) {
    listener.use(
      currencyConverterPlugin({
        sheetSlug: "transactions",
        sourceCurrency: "USD",
        targetCurrency: "EUR",
        amountField: "amount",
        dateField: "transactionDate",
        convertedAmountField: "amountInEUR",
        exchangeRateField: "exchangeRate",
        conversionDateField: "conversionDate",
      })
    );
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener } from "@flatfile/listener";
  import { currencyConverterPlugin } from "@flatfile/plugin-convert-currency";

  export default function (listener: FlatfileListener) {
    listener.use(
      currencyConverterPlugin({
        sheetSlug: "transactions",
        sourceCurrency: "USD",
        targetCurrency: "EUR",
        amountField: "amount",
        dateField: "transactionDate",
        convertedAmountField: "amountInEUR",
        exchangeRateField: "exchangeRate",
        conversionDateField: "conversionDate",
      })
    );
  }
  ```
</CodeGroup>

### Using Utility Functions

<CodeGroup>
  ```javascript JavaScript
  import { 
    validateAmount, 
    validateDate, 
    convertCurrency, 
    calculateExchangeRate 
  } from "@flatfile/plugin-convert-currency";

  // Validate an amount
  const amountResult = validateAmount(150.75);
  // Returns: { value: 150.75 }

  // Validate a date
  const dateResult = validateDate('2023-10-27');
  // Returns: { value: '2023-10-27' }

  // Convert currency
  const converted = convertCurrency(100, 0.92, 1.0);
  // Returns: 108.6957

  // Calculate exchange rate
  const rate = calculateExchangeRate(0.92, 0.80);
  // Returns: 0.869565
  ```

  ```typescript TypeScript
  import { 
    validateAmount, 
    validateDate, 
    convertCurrency, 
    calculateExchangeRate 
  } from "@flatfile/plugin-convert-currency";

  // Validate an amount
  const amountResult = validateAmount(150.75);
  // Returns: { value: 150.75 }

  // Validate a date
  const dateResult = validateDate('2023-10-27');
  // Returns: { value: '2023-10-27' }

  // Convert currency
  const converted: number = convertCurrency(100, 0.92, 1.0);
  // Returns: 108.6957

  // Calculate exchange rate
  const rate: number = calculateExchangeRate(0.92, 0.80);
  // Returns: 0.869565
  ```
</CodeGroup>

## Troubleshooting

### Common Error Messages

| Error                            | Cause                                           | Solution                                                      |
| -------------------------------- | ----------------------------------------------- | ------------------------------------------------------------- |
| "Invalid source/target currency" | Currency codes are not valid three-letter codes | Check that currency codes are valid and supported by the API  |
| "Network error" or "Status: 401" | API key issues                                  | Verify `OPENEXCHANGERATES_API_KEY` is correct and not expired |
| "Amount must be a valid number"  | Invalid amount data                             | Ensure amount field contains numeric values                   |
| "Invalid date format"            | Date not in YYYY-MM-DD format                   | Ensure date field uses YYYY-MM-DD format                      |

### Error Handling

The plugin handles errors gracefully by attaching them directly to records in Flatfile:

* **Validation errors**: Attached to specific fields using `record.addError(fieldName, message)`
* **API/Network errors**: Attached as general record errors using `record.addError('general', message)`

## Notes

### Requirements

* An active subscription to the Open Exchange Rates API is required
* The `OPENEXCHANGERATES_API_KEY` environment variable must be set in your Flatfile Space with your API key

### Limitations

* All currency conversions are routed through USD as a base currency due to Open Exchange Rates API limitations on free/lower-tier plans
* The `dateField` must contain dates in `YYYY-MM-DD` format only
* Converted amounts are fixed to 4 decimal places
* Exchange rates are fixed to 6 decimal places

### Default Behavior

* When `dateField` is not provided, the plugin uses the current date to fetch the latest exchange rates
* When `exchangeRateField` is not provided, the calculated exchange rate is not stored on the record
* When `conversionDateField` is not provided, the conversion timestamp is not stored on the record
* Empty date fields default to the current date in YYYY-MM-DD format
