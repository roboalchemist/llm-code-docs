# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-02-05-sensitive-data-classification-json.md

# Feb 05, 2026: Sensitive data classification: Support for semi-structured data (*General availability*)

Sensitive data classification now supports the VARIANT, ARRAY, and OBJECT data types, which means Snowflake can classify fields in
semi-structured data into native semantic categories as long as the data is in JSON format. For example, if a VARIANT column contains JSON
objects with email addresses and phone numbers, Snowflake can classify the email field as EMAIL and the phone field as PHONE_NUMBER.

For more information, including an example of classification results for JSON data, see [Results for JSON columns](../../../user-guide/classify-results.md).
