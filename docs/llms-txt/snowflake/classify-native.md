# Source: https://docs.snowflake.com/en/user-guide/classify-native.md

# Native semantic categories of sensitive data classification

A semantic category is a label that describes the meaning or type of information in a data column, beyond the fundamental data type.
You can use semantic categories to add business context and improve data goverance. Snowflake provides the following semantic categories
that identify common types of sensitive attributes, such as names and addresses. These native semantic categories can be sectioned into the
following privacy categories:

* Identifiers
* Quasi-identifiers
* Sensitive information

> **Important:**
>
> Under various laws and regulations, multiple semantic categories can be considered “Sensitive Personal Data”, “Special Categories of
> Data”, or similar terms. These semantic categories might require additional protections or controls.

To classify attributes that are not supported natively, refer to [Create custom categories for sensitive data](classify-custom.md).

## About semantic subcategories

If Snowflake identifies that the type of sensitive data is specific to a country, it records a *semantic subcategory* in the classification details. For example, a social security number (SSN) is an identifier in the United States (US), and its semantic subcategory is `NATIONAL_IDENTIFIER`.

You can find the semantic subcategory in the `Details` field of the JSON object returned by the classification
process. For more information about viewing this response object, refer to [Use SQL to view results](classify-results.md).

If the type of sensitive data is not specific to a country and is globally applicable, it does not have a semantic subcategory. This type of
sensitive data is categorized as a global identifier.

## Identifiers

Identifier semantic categories represent personally identifiable information (PII) or sensitive data elements that can be used to
identify individuals or entities.

### Global identifiers

Global identifer categories are semantic categories that are not specific to a country and are globally applicable.

| Semantic category | Notes |
| --- | --- |
| BANK_ACCOUNT | For countries outside of Cananda, New Zealand, and the United States, the semantic subcategory is International Bank Account Number (IBAN). |
| EMAIL |  |
| IMEI | An International Mobile Equiment Identity (IMEI) is a unique number that identifies a phone’s model and serial number. |
| IP_ADDRESS |  |
| NAME |  |
| PAYMENT_CARD |  |
| URL | A Uniform Resource Locator (URL) is the unique address of a resource (such as a document or website) on the Internet. |
| VIN | The Vehicle Identification Number. |

### Country-specific identifiers

| Semantic category | Country | Semantic subcategory | Notes |
| --- | --- | --- | --- |
| BANK_ACCOUNT | Canada (CA) | CA_BANK_ACCOUNT |  |
|  | New Zealand (NZ) | NZ_BANK_ACCOUNT |  |
|  | United States (US) | US_BANK_ACCOUNT |  |
| DRIVERS_LICENSE | Austria (AT) | AT_DRIVERS_LICENSE |  |
|  | Australia (AU) | AU_DRIVERS_LICENSE |  |
|  | Belgium (BE) | BE_DRIVERS_LICENSE |  |
|  | Bulgaria (BG) | BG_DRIVERS_LICENSE |  |
|  | Canada (CA) | CA_DRIVERS_LICENSE |  |
|  | Croatia (HR) | HR_DRIVERS_LICENSE |  |
|  | Cyprus (CY) | CY_DRIVERS_LICENSE |  |
|  | Czechia (CZ) | CZ_DRIVERS_LICENSE |  |
|  | Denmark (DK) | DK_DRIVERS_LICENSE |  |
|  | Estonia (EE) | EE_DRIVERS_LICENSE |  |
|  | Finland (FI) | FI_DRIVERS_LICENSE |  |
|  | France (FR) | FR_DRIVERS_LICENSE |  |
|  | Germany (DE) | DE_DRIVERS_LICENSE |  |
|  | Greece (GR) | GR_DRIVERS_LICENSE |  |
|  | Hungary (HU) | HU_DRIVERS_LICENSE |  |
|  | India (IN) | IN_DRIVERS_LICENSE |  |
|  | Ireland (IE) | IE_DRIVERS_LICENSE |  |
|  | Italy (IT) | IT_DRIVERS_LICENSE |  |
|  | Latvia (LV) | LV_DRIVERS_LICENSE |  |
|  | Lithuania (LT) | LT_DRIVERS_LICENSE |  |
|  | Luxembourg (LU) | LU_DRIVERS_LICENSE |  |
|  | Malta (MT) | MT_DRIVERS_LICENSE |  |
|  | Netherlands (NL) | NL_DRIVERS_LICENSE |  |
|  | New Zealand (NZ) | NZ_DRIVERS_LICENSE |  |
|  | Poland (PL) | PL_DRIVERS_LICENSE |  |
|  | Portugal (PT) | PT_DRIVERS_LICENSE |  |
|  | Romania (RO) | RO_DRIVERS_LICENSE |  |
|  | Slovakia (SK) | SK_DRIVERS_LICENSE |  |
|  | Slovenia (SI) | SI_DRIVERS_LICENSE |  |
|  | Spain (ES) | ES_DRIVERS_LICENSE |  |
|  | Sweden (SE) | SE_DRIVERS_LICENSE |  |
|  | United States (US) | US_DRIVERS_LICENSE |  |
| MEDICARE_NUMBER | Australia (AU) | AU_MEDICARE_NUMBER |  |
|  | New Zealand (NZ) | NZ_NHI_NUMBER |  |
| NATIONAL_IDENTIFIER | Austria (AT) | AT_IDENTITY_CARD  AT_SSN |  |
|  | Belgium (BE) | BE_NATIONAL_NUMBER |  |
|  | Bulgaria (BG) | BG_UNIFORM_CIVIL_NUMBER |  |
|  | Canada (CA) | CA_SOCIAL_INSURANCE_NUMBER |  |
|  | Croatia (HR) | HR_PERSONAL_IDENTIFICATION_NUMBER |  |
|  | Cyprus (CY) | CY_IDENTITY_CARD |  |
|  | Czechia (CZ) | CZ_PERSONAL_IDENTITY_NUMBER |  |
|  | Denmark (DK) | DK_PERSONAL_IDENTIFICATION_NUMBER |  |
|  | Estonia (EE) | EE_PERSONAL_IDENTIFICATION_CODE |  |
|  | Finland (FI) | FI_NATIONAL_IDENTITY_CARD |  |
|  | France (FR) | FR_CNI  FR_SSN | The FR_SSN is also known as the INSEE number. |
|  | Germany (DE) | DE_IDENTITY_CARD |  |
|  | Greece (GR) | GR_NATIONAL_IDENTITY_CARD  GR_SSN | The GR_SSN is also known as the AMKA number. |
|  | Hungary (HU) | HU_PERSONAL_IDENTIFICATION_NUMBER  HU_SSN | The HU_SSN is also known as the TAJ number. |
|  | India (IN) | IN_PAN  IN_AADHAAR  IN_VOTER_ID |  |
|  | Ireland (IE) | IE_PERSONAL_PUBLIC_SERVICE_NUMBER |  |
|  | Latvia (LV) | LV_PERSONAL_CODE |  |
|  | Lithuania (LT) | LT_PERSONAL_CODE |  |
|  | Luxembourg (LU) | LU_NATIONAL_IDENTIFICATION_NUMBER_NATURAL_PERSONS  LU_NATIONAL_IDENTIFICATION_NUMBER_NON_NATURAL_PERSONS |  |
|  | Malta (MT) | MT_IDENTITY_CARD |  |
|  | Netherlands (NL) | NL_CITIZEN_SERVICE_NUMBER |  |
|  | New Zealand (NZ) | NZ_STUDENT_NUMBER |  |
|  | Poland (PL) | PL_NATIONAL_ID |  |
|  | Portugal (PT) | PT_CITIZEN_CARD_NUMBER |  |
|  | Romania (RO) | RO_PERSONAL_NUMERIC_CODE |  |
|  | Singapore (SG) | SG_NATIONAL_REGISTRATION_IDENTITY_CARD |  |
|  | Slovakia (SK) | SK_PERSONAL_NUMBER |  |
|  | Slovenia (SI) | SI_UNIQUE_MASTER_CITIZEN_NUMBER |  |
|  | Spain (ES) | ES_DNI  ES_SSN |  |
|  | Sweden (SE) | SE_NATIONAL_ID |  |
|  | United Kingdom (UK) | UK_NATIONAL_INSURANCE_NUMBER |  |
|  | United States (US) | US_SSN |  |
| ORGANIZATION_IDENTIFIER | Australia (AU) | AU_BUSINESS_NUMBER  AU_COMPANY_NUMBER |  |
|  | New Zealand (NZ) | NZ_BUSINESS_NUMBER |  |
|  | Singapore (SG) | SG_UNIQUE_ENTITY_NUMBER |  |
| PASSPORT | Australia (AU) | AU_PASSPORT |  |
|  | Austria (AT) | AT_PASSPORT |  |
|  | Belgium (BE) | BE_PASSPORT |  |
|  | Bulgaria (BG) | BG_PASSPORT |  |
|  | Canada (CA) | CA_PASSPORT |  |
|  | Croatia (HR) | HR_PASSPORT |  |
|  | Cyprus (CY) | CY_PASSPORT |  |
|  | Czechia (CZ) | CZ_PASSPORT |  |
|  | Denmark (DK) | DK_PASSPORT |  |
|  | Estonia (EE) | EE_PASSPORT |  |
|  | Finland (FI) | FI_PASSPORT |  |
|  | France (FR) | FR_PASSPORT |  |
|  | Germany (DE) | DE_PASSPORT |  |
|  | Greece (GR) | GR_PASSPORT |  |
|  | Hungary (HU) | HU_PASSPORT |  |
|  | Ireland (IE) | IE_PASSPORT |  |
|  | Italy (IT) | IT_PASSPORT |  |
|  | Latvia (LV) | LV_PASSPORT |  |
|  | Lithuania (LT) | LT_PASSPORT |  |
|  | Luxembourg (LU) | LU_PASSPORT |  |
|  | Malta (MT) | MT_PASSPORT |  |
|  | Netherlands (NL) | NL_PASSPORT |  |
|  | New Zealand (NZ) | NZ_PASSPORT |  |
|  | Poland (PL) | PL_PASSPORT |  |
|  | Portugal (PT) | PT_PASSPORT |  |
|  | Romania (RO) | RO_PASSPORT |  |
|  | Singapore (SG) | SG_PASSPORT |  |
|  | Slovakia (SK) | SK_PASSPORT |  |
|  | Slovenia (SI) | SI_PASSPORT |  |
|  | Spain (ES) | ES_PASSPORT |  |
|  | Sweden (SE) | SE_PASSPORT |  |
|  | United States (US) | US_PASSPORT |  |
| PHONE_NUMBER | Australia (AU) | AU_PHONE_NUMBER |  |
|  | Canada (CA) | CA_PHONE_NUMBER |  |
|  | Japan (JP) | JP_PHONE_NUMBER |  |
|  | United Kingdom (UK) | UK_PHONE_NUMBER |  |
|  | United States (US) | US_PHONE_NUMBER |  |
| STREET_ADDRESS | Canada (CA) | CA_STREET_ADDRESS |  |
|  | New Zealand (NZ) | NZ_STREET_ADDRESS |  |
|  | United States (US) | US_STREET_ADDRESS |  |
| TAX_IDENTIFIER | Australia (AU) | AU_TAX_NUMBER |  |
|  | Austria (AT) | AT_TAX_ID_NUMBER |  |
|  | Cyprus (CY) | CY_TAX_ID_NUMBER |  |
|  | France (FR) | FR_TAX_ID_NUMBER |  |
|  | Germany (DE) | DE_TAX_ID_NUMBER |  |
|  | Greece (GR) | GR_TAX_ID_NUMBER |  |
|  | Hungary (HU) | HU_TAX_ID_NUMBER |  |
|  | India (IN) | IN_GST_NUMBER |  |
|  | Italy (IT) | IT_FISCAL_CODE |  |
|  | Malta (MT) | MT_TAX_ID_NUMBER |  |
|  | Netherlands (NL) | NL_TAX_ID_NUMBER |  |
|  | New Zealand (NZ) | NZ_INLAND_REVENUE_NUMBER |  |
|  | Poland (PL) | PL_TAX_ID_NUMBER |  |
|  | Portugal (PT) | PT_TAX_ID_NUMBER |  |
|  | Slovenia (SI) | SI_TAX_ID_NUMBER |  |
|  | Spain (ES) | ES_TAX_ID_NUMBER |  |
|  | Sweden (SE) | SE_TAX_ID_NUMBER |  |
|  | United States (US) | US_TAX_IDENTIFIER | The semantic subcategory US_TAX_IDENTIFIER is an identifier because it is the ITIN of an individual. The EMPLOYER_IDENTIFICATION_NUMBER subcategory of the TAX_IDENTIFIER category is a quasi-identifier because it is the EIN of a company. |

## Quasi-identifiers

Quasi-identifiers are attributes that do not uniquely identify an individual on their own, but when combined with other data, could
be used to re-identify someone. Examples of quasi-identifiers include demographic information, geographic data, and administrative regions.

### Global quasi-identifiers

Global quasi-identifiers are quasi-identifier semantic categories that are not specific to a country and are globally applicable.

| Semantic subcategory |
| --- |
| AGE |
| COUNTRY |
| DATE_OF_BIRTH |
| ETHNICITY |
| GENDER |
| LATITUDE |
| LAT_LONG |
| LONGITUDE |
| MARITAL_STATUS |
| OCCUPATION |
| YEAR_OF_BIRTH |

### Country-specific quasi-identifiers

| Semantic category | Country | Semantic subcategory | Notes |
| --- | --- | --- | --- |
| ADMINISTRATIVE_AREA_1 | Canada (CA) | CA_PROVINCE_OR_TERRITORY |  |
|  | New Zealand (NZ) | NZ_REGION |  |
|  | United States (US) | US_STATE_OR_TERRITORY |  |
| ADMINISTRATIVE_AREA_2 | United States (US) | US_COUNTY |  |
| CITY | Canada (CA) | CA_CITY |  |
|  | New Zealand (NZ) | NZ_CITY |  |
|  | United States (US) | US_CITY |  |
| POSTAL_CODE | Australia (AU) | AU_POSTAL_CODE |  |
|  | Canada (CA) | CA_POSTAL_CODE |  |
|  | Japan (JP) | JP_POSTAL_CODE |  |
|  | New Zealand (NZ) | NZ_POSTAL_CODE |  |
|  | Switzerland (CH) | CH_POSTAL_CODE |  |
|  | United Kingdom (UK) | UK_POSTAL_CODE | Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). |
|  | United States (US) | US_POSTAL_CODE |  |
| TAX_IDENTIFIER | United States (US) | EMPLOYER_IDENTIFICATION_NUMBER | The semantic subcategory EMPLOYER_IDENTIFICATION_NUMBER is a quasi-identifier, not an identifier, because it is the EIN of a company. The US_TAX_IDENTIFIER subcategory of the TAX_IDENTIFIER category represents the ITIN of an individual, and is an identifier. |

## Sensitive information

Sensitive information includes data elements that contain confidential or private details. While the data do not directly identify an
individual, they require protection due to their sensitive nature.

### Global sensitive information

| Semantic category |
| --- |
| SALARY |
