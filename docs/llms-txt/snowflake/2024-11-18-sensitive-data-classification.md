# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-11-18-sensitive-data-classification.md

# November 18, 2024 — Sensitive data classification

## Automatic Sensitive Data Classification — *Preview*

Snowflake is pleased to announce Automatic Sensitive Data Classification, a serverless feature that can help automatically detect sensitive
data using native and custom classifiers. It can also apply user-defined tags and masking policies on columns automatically
when sensitive data is detected.

For information, see [Use SQL to set up sensitive data classification](../../../user-guide/classify-auto.md).

## Classifier improvements

The following classifiers are now available:

| Country | Classifier |
| --- | --- |
| New Zealand | *Organization identifier now includes business number.* National identifier now includes student number. |
| Japan | *Phone number* Postal code |

The accuracy of the following geo-specific classifiers has been improved:

| Supported country | Classifier |
| --- | --- |
| Australia | Phone Number |
| Canada | *City* Phone number *Street address* Bank account |
| New Zealand | *City* Street address * Bank account |
| United Kingdom | *Postal code* Phone number |
| United States | *City* Phone number *Street address* Bank account |

The accuracy of the following global classifiers has been improved:

* Name
* Latitude
* Longitude
* Payment card
