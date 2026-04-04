# Source: https://docs.startree.ai/corecapabilities/manage-data/set-up-tiered-storage/use-text-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Index support for Tiered Storage

## Context

Having text index support for data stored in remote tiered storage is crucial for accelerating performance for text search based queries. Previously, text indexes were not supported in StarTree Tiered storage due to various reasons (text index stored separate from Pinot segment and not integrated in columns.psf)

Starting **Startree release 0.11.1**, text indexes can now be used in conjunction with Startree Tiered storage configuration.

Key changes made to enable this support

* **File Consolidation**: Text index directories are now consolidated into the columns.psf file.
* **Tiered Storage Enabled**: The inclusion of text indexes within `columns.psf` automatically enables tiered storage support.
* **Minimal Configuration**: Activation of the new format merely requires setting the storeInSegmentFile flag.

**Operational Mechanism**

* **Default Mode**: Text indexes continue to employ separate directories, thereby lacking tiered storage support.
* **Consolidated Mode**: When `storeInSegmentFile: "true"` is configured, text indexes are stored within columns.psf, enabling tiered storage support.

**Backward Compatibility**: Existing segments containing text indexes in separate directories remain fully functional without alteration.

## Sample configuration

The `storeInSegmentFile` flag controls whether text indexes are stored within the segment file or in separate directories:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "your_text_column",
      "indexes": {
        "text": {
    ...
          "storeInSegmentFile": "true"
        }
      },
   ...
```

With this, users can leverage text index with tiered storage enabled tables.

# **How to Enable Text Index for S3 Tiered Storage**

## New Table with Text Index and S3 Tiered Storage Support

For new tables, you have two options for configuring text indexes with S3 tiered storage support:

### Case 1: Both Local and S3 in Consolidated Format

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "text_column",
      "indexes": {
        "text": {
          "storeInSegmentFile": "true"  // Both local and S3 in consolidated format
        }
      },
      "properties": {
        "luceneUseCompoundFile": "false",
        "luceneMaxBufferSizeMB": "128",
        "useANDForMultiTermQueries": "true",
        "luceneAnalyzerClass": "org.apache.lucene.analysis.standard.StandardAnalyzer",
        "luceneQueryParserClass": "org.apache.lucene.queryparser.classic.QueryParser"
      }
    }
  ]
}
```

### Case 2: Local in Default Format, S3 in Consolidated Format

In this case, we use the `tierOverwrites` to decouple local vs S3 format.

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "text_column",
      "indexes": {
        "text": {
          "storeInSegmentFile": "false"  // Local storage in default format
        }
      },
      "properties": {
        "luceneUseCompoundFile": "false",
        "luceneMaxBufferSizeMB": "128",
        "useANDForMultiTermQueries": "true",
        "luceneAnalyzerClass": "org.apache.lucene.analysis.standard.StandardAnalyzer",
        "luceneQueryParserClass": "org.apache.lucene.queryparser.classic.QueryParser"
      },
      "tierOverwrites": {
        "s3Tier": {
          "indexes": {
            "text": {
              "storeInSegmentFile": "true"  // S3 storage in consolidated format
            }
          }
        }
      }
    }
  ]
}
```

## Enable Text Index on Existing Table with S3 Tiered Storage

For existing tables, local storage can remain as it is (default format), and tierOverwrites with storeInSegmentFile: "true" can be used to enable text index on S3 tiered storage:

**Note**: For existing tables, the new flag will take effect on existing segments after a table reload but new segments(data) will pick the changes. Table reload can take some time based on the data size in tables.

**Important**: Local storage can remain in default format (separate directories), but when moving to S3, storeInSegmentFile must be set to "true" for tiered storage to work.

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "your_text_column",
      "indexes": {
        "text": {
         ...
        }
      },
      "properties": {
       ...
      },
      "tierOverwrites": {
        "myS3Tier": {
          "indexes": {
            "text": {
              "deriveNumDocsPerChunk": false,
              "rawIndexWriterVersion": 4,
              "storeInSegmentFile": "true"  // Enable consolidation for new segments
            }
          }
        }
      }
    }
  ]
}
```

## How to Pin the Text Index

\*\*Text index pinning works the same way as inverted index pinning and is specified using \*\*preload.keys in the tier configuration. For detailed information on preloaded index configuration, refer to the[<u>StarTree documentation on preloaded index</u>](https://docs.startree.ai/corecapabilities/manage-data/set-up-tiered-storage/setup#preloaded-index) .

To pin text indexes to specific storage tiers, configure the preload.keys in your tierConfigs:

```json  theme={null}
{
  "tierConfigs": [
    {
      "name": "remoteTier",
      "segmentSelectorType": "time",
      "segmentAge": "7d",
      "storageType": "pinot_server",
      "serverTag": "RemoteTenant_OFFLINE",
      "tierBackend": "s3",
      "tierBackendProperties": {
        "pathPrefix": "<pathPrefix>",
        "region": "<region>",
        "bucket": "<bucket>"
      },
      "preload.index.keys.override": "*.text_index"  // Pin text index to this tier
    }
  ]
}
```

**Note**\
Tiered storage features for text indexes work similar to other indexes (for example, inverted index). Once text indexes are consolidated into the pinot segment file with storeInSegmentFile: "true", they can be moved between storage tiers just like any other index type.

Built with [Mintlify](https://mintlify.com).
