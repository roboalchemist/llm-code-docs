# Source: https://docs.axonius.com/docs/ukg-pro-ultimate-software-ultipro.md

# UKG Pro (Ultimate Software UltiPro)

UKG Pro (formerly Ultimate Software UltiPro) is cloud-based human capital management (HCM) software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Permissions

## Parameters

1. **Domain** *(required, default: `https://service2.ultipro.com`)* - The base URL of the UKG Pro system.

2. **User Name** and **Password** *(required)* - The credentials for a web service account that has the permissions to fetch assets. For more information see [Service Accounts](https://developer.ukg.com/hcm/docs/web-service-account).

3. **US Customer API Key** *(required)* - An API Key associated with a web service account that has permissions to fetch assets.

4. **Verify SSL**  - Select to verify the SSL certificate offered by the value supplied in **Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Domain**.

6. **HTTPS Proxy User Name** *(optional* - The user name to use when connecting to the value supplied in **Domain** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Domain** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![UKGAdapter.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UKGAdapter.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch person details** *(default: true)* - Select whether to fetch information about person details as users. This includes personal data such as:
   1. Personal fields (nationality, gender,origin country, ..)
   2. Health Fields(blood type, eye color, hair, height, is smoker,…) - PII data
   3. Other (military service info, visa type, visa expiration, …) - PII data

2. **Fetch employee details** - Select whether to fetch information about employee details for each user. This includes information such as:
   1. Identity fields (employee ID, first & last name, mail,..)
   2. Contact fields (phone numbers, address,..)
   3. Employment fields (employee number, job title, status, employment type,…)
   4. Organizational fields (Organization department, product, division)

3. **Ignore employees with termination date greater than X days** *(default: 90)*  - Ignore employees with a termination date greater than the number of days set. This only applies to employees fetched from **Fetch employee details** .

4. **Field(s) to exclude** *(optional)* - Specify fields to exclude from the Basic and Advanced views, such as fields containing sensitive data or fields that display irrelevant information. To specify multiple values, separate them by a comma. For example you could exclude fields such as `ssn, ssnIsSuppressed, nationality1, ethnicDescription, gender`.

<Callout icon="📘" theme="info">
  Note

  * If you do not configure the **Field(s) to exclude** successfully the adapter will fetch all fields, which might also include PII. See [PII Fields Recommended to Exclude](/docs/ukg-pro-ultimate-software-ultipro#pii-fields-recommended-to-exclude) to learn which fields are recommended to exclude.

  * Make sure that the specified fields are only from the **Advanced** view. Adding field names only displayed in the Basic view will not exclude them from the fetch.

  * The specified names must be in the raw values from the API response.

  * Fields from the Advanced view that are added to the **Field(s) to exclude** parameter will not fetch data from Basic and Advanced views.
</Callout>

5. **Parse employee number as employee ID** - Select this option to use the value of the “employeenumber”  as Employee ID.

<Callout icon="📘" theme="info">
  Note

  To learn more about general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [UKG Pro API](https://developer.ukg.com/hcm/reference/welcome-to-the-ukg-pro-api).

The **Fetch employee details** parameter accesses the [UKG Employee Changes API](https://developer.ukg.com/hcm/reference/employeechanges_get).

The **Fetch person details** parameter accesses the [UKG EmploymentDetails API](https://developer.ukg.com/hcm/reference/get_personnel-v1-employment-details).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials for the UltiPro service account that have  the "View" role for the [UKG Employee Changes API](https://connect.ultipro.com/documentation#/api/199/Changes%20By%20Date/get__personnel_v1_employee-changes) and [UKG Person Details API](https://connect.ultipro.com/documentation#/api/811/PersonDetails/get__personnel_v1_person-details).

## PII Fields Recommended to Exclude

Below is a list of PIIs we recommend to exclude using the **Field(s) to exclude** advanced configuration.

* ssn
* ssnIsSuppressed
* nationality1
* ethnicDescription
* gender
* dateOfBirth
* emailAddressAlternate
* healthBloodType
* homePhone
* nationalId
* ethnicIDCode
* healthHeightFeet
* healthHeightInches
* healthLastDonateDate
* healthWeight
* homePhoneCountry
* isSmoker
* maritalStatusCode
* previousSSN
* militaryService
* militarySeparationDate
* militaryIsOthEligVetBasis
* militaryIsOthEligVet
* militaryIsMedalVet
* militaryIsDisabledVet
* militaryIsActiveWartimeVet
* militaryEra
* militaryBranchServed
* healthHair
* healthEyes
* disabilityType
* addressZipCode
* addressState
* addressSms
* addressLine4
* addressLine3
* addressLine2
* addressLine1
* addressLatitude
* employeeAddress1
* employeeAddress2
* alternateEmailAddress
* zipCode
* isDisabled