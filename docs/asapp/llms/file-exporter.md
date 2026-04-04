# Source: https://docs.asapp.com/reporting/file-exporter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# File Exporter

> Learn how to use File Exporter to retrieve data from Standalone ASAPP Services.

Use ASAPP's File Exporter service to securely retrieve AI Services data via API. The service provides a specific link to access the requested data based on the file parameters of the request that include the feed, version, format, date, and time interval of interest.

The File Exporter service is meant to be used as a batch mechanism for exporting data to your data warehouse, either on a scheduled basis (e.g. nightly, weekly) or for ad hoc analyses. Data that populates feeds for the File Exporter service updates once daily at 2:00AM UTC.

<Note>
  Data feeds are not available by default. Reach out to your ASAPP account contact to ensure data feeds are enabled for your implementation.
</Note>

## Before You Begin

To use ASAPP's APIs, all apps must be registered through the AI Services Developer Portal. Once registered, each app will be provided unique API keys for ongoing use.

<Tip>
  Get your API credentials and learn how to set up AI Service APIs by visiting our [Developer Quick Start Guide](/getting-started/developers).
</Tip>

## Endpoints

The File Exporter service uses six parameters to specify a target file:

* `feed`: The name of the data feed of interest
* `version`: The version number of the feed
* `format`: The file format
* `date`: The date of interest
* `interval`: The time interval of interest
* `fileName`: The data file name

Each parameter is retrieved from a dedicated endpoint. Once all parameters are retrieved, the target file is retrieved using the endpoint (`/fileexporter/v1/static/getfeedfile`), which takes these parameters in the request and returns a URL.

* `POST` `/fileexporter/v1/static/listfeeds`
  Use this endpoint to retrieve an array of feed names available for your implementation.
* `POST` `/fileexporter/v1/static/listfeedversions`
  Use this endpoint to retrieve an array of versions available for a given data feed.
* `POST` `/fileexporter/v1/static/listfeedformats`
  Use this endpoint to retrieve an array of available file formats for a given feed and version.
* `POST` `/fileexporter/v1/static/listfeeddates`
  Use this endpoint to retrieve an array of available dates for a given feed/version/format.
* `POST` `/fileexporter/v1/static/listfeedintervals`
  Use this endpoint to retrieve an array of available intervals for a given feed/version/format/date.
* `POST` `/fileexporter/v1/static/listfeedfiles`
  Use this endpoint to retrieve an array of file names for a given feed/version/format/date/interval.
* `POST` `/fileexporter/v1/static/getfeedfile`
  Use this endpoint to retrieve a single file URL for the data specified using parameters returned from the above endpoints.

<Tip>
  Values for `file` will differ based on the requested `date` and `interval` parameters. Always call this endpoint prior to calling `/getfeedfile`.
</Tip>

<Tip>
  In the `getfeedfile` request, all parameters are required except `interval`
</Tip>

### Endpoint List

1. `POST /fileexporter/v1/static/listfeeds`
   Retrieve an array of feed names available for your implementation.

2. `POST /fileexporter/v1/static/listfeedversions`
   Retrieve an array of versions available for a given data feed.

3. `POST /fileexporter/v1/static/listfeedformats`
   Retrieve an array of available file formats for a given feed and version.

4. `POST /fileexporter/v1/static/listfeeddates`
   Retrieve an array of available dates for a given feed/version/format.

5. `POST /fileexporter/v1/static/listfeedintervals`
   Retrieve an array of available intervals for a given feed/version/format/date.

6. `POST /fileexporter/v1/static/listfeedfiles`
   Retrieve an array of file names for a given feed/version/format/date/interval.

   <Tip>
     Values for `file` will differ based on the requested `date` and `interval` parameters. Always call this endpoint prior to calling `/getfeedfile`.
   </Tip>

7. `POST /fileexporter/v1/static/getfeedfile`
   Retrieve a single file URL for the data specified using parameters returned from the above endpoints.

   <Tip>
     In the `getfeedfile` request, all parameters are required except `interval`
   </Tip>

## Making Routine Requests

Only two requests are needed for exporting data on an ongoing basis for different timeframes. To export a file each time, make these two calls:

1. Call `/listfeedfiles`
   using the same `feed`, `version`, `format` parameters, and alter the `date` and `interval` parameters as necessary (`interval` is optional) to specify the time period of the data file you wish to retrieve.
   In response, you will receive the name(s) of the `file` needed for making the next request.

2. Call `/getfeedfile`
   with the same parameters as above and the `file` name parameter returned from `/listfeedfiles`. In response, you will receive the access `url`.

3. Call `/listfeedfiles` using the same `feed`, `version`, `format` parameters, and alter the `date` and `interval` parameters as necessary (`interval` is optional) to specify the time period of the data file you wish to retrieve. In response, you will receive the name(s) of the `file` needed for making the next request.

4. Call `/getfeedfile` with the same parameters as above and the `file` name parameter returned from `/listfeedfiles`. In response, you receive the access `url`.

Your final request to `/getfeedfile` for the file `url` would look like this:

```json  theme={null}
{
  "feed": "feed_test",
  "version": "version=1",
  "format": "format=jsonl",
  "date": "dt=2022-06-27",
  "fileName": "file1.jsonl"
}
```

## Data Feeds

File Exporter makes the following data feeds available:

1. **Conversation State**: `staging_conversation_state`
   Combines ASAPP conversation identifiers with metadata including summaries, augmentation counts, intent, crafting times, and important timestamps.
2. **Utterance State**: `staging_utterance_state`
   Combines ASAPP utterance identifiers with metadata including sender type, augmentations, crafting times, and important timestamps. **NOTE:** Does not include utterance text.
3. **Utterances**: `utterances`
   Combines ASAPP conversation and utterance identifiers with utterance text and timestamps. Identifiers can be used to join utterance text with metadata from utterance state feed.
4. **GenerativeAgent**: `generativeagent`
   Contains the per conversation data for GenerativeAgent.

   [GenerativeAgent Feed Data can be found here](/generativeagent/reporting/data-reference)
5. **Free-Text Summaries**: `autosummary_free_text`
   Retrieves data from free-text summaries generated by AI Summary. This feed has one record per free-text summary produced and can have multiple summaries per conversation .
6. **Feedback**: `autosummary_feedback`
   Retrieves the text of the feedback submitted by the agent. Developers can join this feed to the AI Summary free-text feed using the summary ID.
7. **Structured Data**: `autosummary_structured_data`
   Retrieves structured data to extract information and insights from conversations in the form of yes/no answers (up to 20) from summaries generated by AI Summary.

[Click here to view the full schema](/reporting/fileexporter-feeds) for each feed table.

<Note>
  Feed table names that include the prefix `staging_` are not referencing a lower environment; table names have no connection to environments.
</Note>
