# Source: https://docs.axonius.com/docs/wiz-reports.md

# Wiz Reports

Wiz Reports provides additional data for Wiz assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

This adapter gets device and users assets from an input of a CSV file. The adapter parameters and the functionality are the same as the CSV adapter parameters. Refer to [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv) for full details about configuring CSV adapters.
Note that the adapter parameters are the same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except for the    'File contains users information' nor the 'File contains installed software information' parameters.   These fields are not part of the Wiz Reports adapter configuration.

Instead from the Report Type field select you can either select **Hosted Technology** or **Data Findings** to upload a report file.

<Image alt="WizReportsTop" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WizReportsTop.png" />

Fields that must be contained in the file:
The CSV file uploaded must contain the following fields.

### HOSTED\_TECHNOLOGY

From HOSTED\_TECHNOLOGY

* cpe
* extendedSupport
* isLatestVersion
* isVersionEndOfLife
* latestVersion
* latestVersionReleaseDate
* `path` or `softwarePath`
* techId
* techName
* version
* versionEndOfLifeDate
* versionReleaseDate

From the assets that the software (for HOSTED\_TECHNOLOGY)  is installed on (e.g. VIRTUAL\_MACHINE, CONTAINER, etc):

* name
* entityType (this should be one of VIRTUAL\_MACHINE, CONTAINER, etc)
* cloudPlatform (AWS, GCP, Azure, etc)
* subscriptionId
* externalId
* providerUniqueId
* id (this is the Wiz ID of the asset in the form of a UUID, e.g. 1073303b-76fb-5669-9460-f9fd830dd978)
* cloudProviderURL

### DATA\_FINDING

From DATA\_FINDING

* findingId (the Wiz ID of the data finding, should be a UUID)
* findingName (the name of the data finding)
* totalMatchCount
* uniqueMatchCount
* anonymizerType (the anonimyzer type of the data classifier for the data finding)
* category (the category of the data classifier)
* description (the description of the data classifier)
* dataClassifierId (the Wiz ID of the data classifier, should be a UUID)
* matcherType (the matcher type of the data classifier)
* dataClassifierName (the name of the data classifier)
* severity (the severity of the data classifier)
* validatorType (the validator type of the data classifier)
* country (the country of the data finding)
* countryCode (the country code of the data finding)

From the assets that the data findings relate to (e.g. BUCKET, DATABASE, VIRTUAL\_MACHINE)

* assetId (the Wiz ID of the asset, should be a UUID)
* assetName
* entityType (this should be one of VIRTUAL\_MACHINE, CONTAINER, etc)
* cloudPlatform (AWS, GCP, Azure, etc)
* subscriptionId
* externalId
* providerUniqueId
* cloudProviderURL