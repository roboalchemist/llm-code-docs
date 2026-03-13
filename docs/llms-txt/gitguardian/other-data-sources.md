# Source: https://docs.gitguardian.com/ggshield-docs/integrations/other-data-sources/other-data-sources.md

# Scanning Other Data Sources for Secrets

> Describes the ggshield docset input format for scanning non-git data sources like messaging systems and wikis using the secret scan docset command.

## Prelude

`ggshield` supports a generic input format via its `secret scan docset` command.
The input files for that command must be in JSONL format, each line containing a "docset" JSON object.

A docset represents a set of documents for a given type. Each document has authors and content.
Authors may have a name, an email and a role. This is a simple and flexible model to ease preparing data for ggshield consumption.
See below for more details.

## The Docset Format

### Docset structure

For a more detailed view of the format, here is the structure of a docset:

```
{
  // Required. Defines the type of data stored in the docset.
  "type": "",

  // Required. A string to uniquely identify this docset.
  // Content depends on the type and is considered opaque but will be displayed in the output.
  "id": "",

  // Optional. Authors of the doc set.
  // Only set if the whole docset has the same authors.
  "authors": [$author],

  // Required. The documents of the docset.
  "documents": [$document]
}
```

### Author's structure

```json
{
  // Required. Content depends on the format and is considered opaque.
  // Could be an email, a username or a system specific ID.
  "id": "",
  // Optional. The author name, if available.
  "name": "",
  // Optional. The author email, if available.
  // This field should be set even if email is used as the ID, since the ID is
  // considered opaque.
  "email": "",
  // Optional. Meaning depends on the format.
  // For example in a commit it would be "author" or "committer".
  "role": ""
}
```

### Document's structure

```json
{
  // Required. A string to uniquely identify the document inside the docset.
  // Content depends on the type and is considered opaque but will be displayed in the output.
  "id": "",

  // Optional. If defined, it replaces (not extend) the global docset authors.
  "authors": [$author],

  // Required. The content of the document in UTF-8.
  "content": ""
}
```
