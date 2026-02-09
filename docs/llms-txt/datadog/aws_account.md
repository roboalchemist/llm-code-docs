# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_account.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_account{% #aws_account %}

## `account_arn`{% #account_arn %}

**Type**: `STRING`

## `account_id`{% #account_id %}

**Type**: `STRING`

## `alternate_contact`{% #alternate_contact %}

**Type**: `STRUCT`**Provider name**: `AlternateContact`**Description**: A structure that contains the details for the specified alternate contact.

- `alternate_contact_type`**Type**: `STRING`**Provider name**: `AlternateContactType`**Description**: The type of alternate contact.
- `email_address`**Type**: `STRING`**Provider name**: `EmailAddress`**Description**: The email address associated with this alternate contact.
- `name`**Type**: `STRING`**Provider name**: `Name`**Description**: The name associated with this alternate contact.
- `phone_number`**Type**: `STRING`**Provider name**: `PhoneNumber`**Description**: The phone number associated with this alternate contact.
- `title`**Type**: `STRING`**Provider name**: `Title`**Description**: The title associated with this alternate contact.

## `alternate_contacts`{% #alternate_contacts %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `AlternateContact`**Description**: A structure that contains the details for the specified alternate contact.

- `alternate_contact_type`**Type**: `STRING`**Provider name**: `AlternateContactType`**Description**: The type of alternate contact.
- `email_address`**Type**: `STRING`**Provider name**: `EmailAddress`**Description**: The email address associated with this alternate contact.
- `name`**Type**: `STRING`**Provider name**: `Name`**Description**: The name associated with this alternate contact.
- `phone_number`**Type**: `STRING`**Provider name**: `PhoneNumber`**Description**: The phone number associated with this alternate contact.
- `title`**Type**: `STRING`**Provider name**: `Title`**Description**: The title associated with this alternate contact.

## `contact_information`{% #contact_information %}

**Type**: `STRUCT`**Provider name**: `ContactInformation`**Description**: Contains the details of the primary contact information associated with an Amazon Web Services account.

- `address_line1`**Type**: `STRING`**Provider name**: `AddressLine1`**Description**: The first line of the primary contact address.
- `address_line2`**Type**: `STRING`**Provider name**: `AddressLine2`**Description**: The second line of the primary contact address, if any.
- `address_line3`**Type**: `STRING`**Provider name**: `AddressLine3`**Description**: The third line of the primary contact address, if any.
- `city`**Type**: `STRING`**Provider name**: `City`**Description**: The city of the primary contact address.
- `company_name`**Type**: `STRING`**Provider name**: `CompanyName`**Description**: The name of the company associated with the primary contact information, if any.
- `country_code`**Type**: `STRING`**Provider name**: `CountryCode`**Description**: The ISO-3166 two-letter country code for the primary contact address.
- `district_or_county`**Type**: `STRING`**Provider name**: `DistrictOrCounty`**Description**: The district or county of the primary contact address, if any.
- `full_name`**Type**: `STRING`**Provider name**: `FullName`**Description**: The full name of the primary contact address.
- `phone_number`**Type**: `STRING`**Provider name**: `PhoneNumber`**Description**: The phone number of the primary contact information. The number will be validated and, in some countries, checked for activation.
- `postal_code`**Type**: `STRING`**Provider name**: `PostalCode`**Description**: The postal code of the primary contact address.
- `state_or_region`**Type**: `STRING`**Provider name**: `StateOrRegion`**Description**: The state or region of the primary contact address. If the mailing address is within the United States (US), the value in this field can be either a two character state code (for example, `NJ`) or the full state name (for example, `New Jersey`). This field is required in the following countries: `US`, `CA`, `GB`, `DE`, `JP`, `IN`, and `BR`.
- `website_url`**Type**: `STRING`**Provider name**: `WebsiteUrl`**Description**: The URL of the website associated with the primary contact information, if any.

## `primary_email`{% #primary_email %}

**Type**: `STRING`**Provider name**: `PrimaryEmail`**Description**: Retrieves the primary email address associated with the specified account.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`
