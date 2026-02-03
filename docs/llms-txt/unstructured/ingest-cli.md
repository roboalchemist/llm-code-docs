# Source: https://docs.unstructured.io/open-source/ingestion/ingest-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Process files in batches by using the Unstructured Ingest CLI

The Unstructured Ingest CLI enables you to use command-line scripts to send files in batches to Unstructured for processing, and to tell Unstructured where to deliver the processed data. [Learn more](/open-source/ingestion/overview#unstructured-ingest-cli).

<Note>
  The Unstructured Ingest CLI does not work with the Unstructured API.

  For information about the Unstructured API, see the [Unstructured API Overview](/api-reference/workflow/overview).
</Note>

## Getting started

You can use the Unstructured Ingest CLI to process files locally, or you can use the Ingest CLI to send files in batches to Unstructured for processing.

Local processing does not use an Unstructured API key or API URL.

Using the Ingest CLI to send files in batches to Unstructured for processing is more robust, and usage is billed to you on a pay-as-you-go basis. Usage requires an Unstructured API key and API URL, as follows:

1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
   After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
   </Note>

2. If you have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
     or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
   </Note>

3. Get your Unstructured API key:<br />

   a. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

   <Note>
     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).
   </Note>

   b. Click **Generate API Key**.<br />
   c. Follow the on-screen instructions to finish generating the key.<br />
   d. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

3) The Unstructured API URL for Unstructured Ingest was provided to you when your Unstructured account was created.
   If you do not have this URL, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

<Note>
  The default URL for Unstructured Ingest is the same as the default URL for the legacy Unstructured Partition Endpoint: `https://api.unstructuredapp.io/general/v0/general`.
  However, you should always use the URL that was provided to you when your Unstructured account was created.
</Note>

## Installation

One approach to get started quickly with the Unstructured Ingest CLI is to install Python and then run the following command:

```bash  theme={null}
pip install unstructured-ingest
```

This default installation option enables the ingestion of plain text files, HTML, XML, JSON and emails that do not require any extra dependencies. This default option also enables you to specify local source and destination locations.

You might also need to install additional dependencies, depending on your needs. [Learn more](/open-source/ingestion/ingest-dependencies).

For additional installation options, see [Unstructured Ingest CLI](/open-source/ingestion/overview#unstructured-ingest-cli) in the [Ingest](/open-source/ingestion/overview) section.

<Info>To migrate from older, deprecated versions of the Ingest CLI that used `pip install unstructured`, see the [migration guide](/open-source/ingestion/overview#migration-guide).</Info>

## Usage

To call the Unstructured Ingest CLI, follow this calling pattern, where:

* `<source>` is the command name for one of the available [source](/open-source/ingestion/source-connectors/overview) (input) connectors, such as `local` for a local source location, `azure` for an Azure Storage account source, `s3` for an Amazon S3 bucket source, and so on.
* `<destination>` is the command name for one of the available [destination](/open-source/ingestion/destination-connectors/overview) (output) connectors, such as `local` for a local destination, `azure` for an Azure Storage account destination, `s3` for an Amazon S3 bucket destination, and so on.
* `<setting>` is one or more command-line options for specifying how and where Unstructured will ingest the files from the `<source>`, or how and where to deliver the processed data to the `<destination>`.

```bash CLI theme={null}
#!/usr/bin/env bash

unstructured-ingest \
  <source> \
    --<setting1> <value1> \
    --<setting2> <value2> \
    --<settingN> <valueN> \
  <destination> \
    --<setting1> <value1> \
    --<setting2> <value2> \
    --<settingN> <valueN>
```

To learn how to use the Unstructured Ingest CLI to work with a specific source (input) and destination (output) location, see the CLI script examples for the [source](/open-source/ingestion/source-connectors/overview) and [destination](/open-source/ingestion/destination-connectors/overview) connectors that are available for you to choose from.

See also the [ingest configuration](/open-source/ingestion/ingest-configuration/overview) settings for command-line options that enable you to further control how batches are sent and processed.
