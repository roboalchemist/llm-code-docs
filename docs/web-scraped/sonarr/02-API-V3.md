# Sonarr V3 API

## Servers

- {protocol}://{hostpath}: 

## API Information

**Version:** 3.0.0
**Title:** Sonarr

Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

## API Endpoints

### /

#### GET

**Parameters:**

- `path` (path): N/A

**Responses:**

- `200`: OK

### /api

#### GET

**Responses:**

- `200`: OK

### /api/v3/autotagging

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AutoTaggingResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/autotagging/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/autotagging/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/AutoTaggingResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/blocklist

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `seriesIds` (query): N/A
- `protocols` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/blocklist/bulk

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/BlocklistBulkResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/compone...
```

**Responses:**

- `200`: OK

### /api/v3/blocklist/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/calendar

#### GET

**Parameters:**

- `start` (query): N/A
- `end` (query): N/A
- `unmonitored` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisodeFile` (query): N/A
- `includeEpisodeImages` (query): N/A
- `tags` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/calendar/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/command

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CommandResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/command/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/downloadclient

#### GET

**Responses:**

- `200`: OK

### /api/v3/config/downloadclient/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DownloadClientConfigResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/host

#### GET

**Responses:**

- `200`: OK

### /api/v3/config/host/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/HostConfigResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/components...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/importlist

#### GET

**Responses:**

- `200`: OK

### /api/v3/config/importlist/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListConfigResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/indexer

#### GET

**Responses:**

- `200`: OK

### /api/v3/config/indexer/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/IndexerConfigResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/mediamanagement

#### GET

**Responses:**

- `200`: OK

### /api/v3/config/mediamanagement/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/MediaManagementConfigResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/naming

#### GET

**Responses:**

- `200`: OK

### /api/v3/config/naming/examples

#### GET

**Parameters:**

- `renameEpisodes` (query): N/A
- `replaceIllegalCharacters` (query): N/A
- `colonReplacementFormat` (query): N/A
- `customColonReplacementFormat` (query): N/A
- `multiEpisodeStyle` (query): N/A
- `standardEpisodeFormat` (query): N/A
- `dailyEpisodeFormat` (query): N/A
- `animeEpisodeFormat` (query): N/A
- `seriesFolderFormat` (query): N/A
- `seasonFolderFormat` (query): N/A
- `specialsFolderFormat` (query): N/A
- `id` (query): N/A
- `resourceName` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/config/naming/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/NamingConfigResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/componen...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/ui

#### GET

**Responses:**

- `200`: OK

### /api/v3/config/ui/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UiConfigResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/customfilter

#### GET

**Responses:**

- `200`: OK

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CustomFilterResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/customfilter/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CustomFilterResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/customformat

#### GET

**Responses:**

- `200`: OK

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CustomFormatResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/customformat/bulk

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CustomFormatBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CustomFormatBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/customformat/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/customformat/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/CustomFormatResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/delayprofile

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DelayProfileResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/delayprofile/reorder/{id}

#### PUT

**Parameters:**

- `id` (path): N/A
- `after` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/delayprofile/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DelayProfileResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/diskspace

#### GET

**Responses:**

- `200`: OK

### /api/v3/downloadclient

#### GET

**Responses:**

- `200`: OK

#### POST

**Parameters:**

- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DownloadClientResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/downloadclient/action/{name}

#### POST

**Parameters:**

- `name` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DownloadClientResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/downloadclient/bulk

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DownloadClientBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DownloadClientBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/downloadclient/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/downloadclient/test

#### POST

**Parameters:**

- `forceTest` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DownloadClientResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/downloadclient/testall

#### POST

**Responses:**

- `200`: OK

### /api/v3/downloadclient/{id}

#### PUT

**Parameters:**

- `id` (path): N/A
- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/DownloadClientResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/episode

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `episodeIds` (query): N/A
- `episodeFileId` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisodeFile` (query): N/A
- `includeImages` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/episode/monitor

#### PUT

**Parameters:**

- `includeImages` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/EpisodesMonitoredResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/episode/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/EpisodeResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/episodefile

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `episodeFileIds` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/episodefile/bulk

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/EpisodeFileListResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/EpisodeFileResource"
        }
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/episodefile/editor

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/EpisodeFileListResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/episodefile/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/EpisodeFileResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/filesystem

#### GET

**Parameters:**

- `path` (query): N/A
- `includeFiles` (query): N/A
- `allowFoldersWithoutTrailingSlashes` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/filesystem/mediafiles

#### GET

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/filesystem/type

#### GET

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/health

#### GET

**Responses:**

- `200`: OK

### /api/v3/history

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A
- `eventType` (query): N/A
- `episodeId` (query): N/A
- `downloadId` (query): N/A
- `seriesIds` (query): N/A
- `languages` (query): N/A
- `quality` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/history/failed/{id}

#### POST

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/history/series

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `eventType` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/history/since

#### GET

**Parameters:**

- `date` (query): N/A
- `eventType` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/importlist

#### GET

**Responses:**

- `200`: OK

#### POST

**Parameters:**

- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/importlist/action/{name}

#### POST

**Parameters:**

- `name` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/importlist/bulk

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/importlist/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/importlist/test

#### POST

**Parameters:**

- `forceTest` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/importlist/testall

#### POST

**Responses:**

- `200`: OK

### /api/v3/importlist/{id}

#### PUT

**Parameters:**

- `id` (path): N/A
- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/importlistexclusion

#### GET

**Responses:**

- `200`: OK

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListExclusionResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/importlistexclusion/bulk

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListExclusionBulkResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": ...
```

**Responses:**

- `200`: OK

### /api/v3/importlistexclusion/paged

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/importlistexclusion/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ImportListExclusionResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/indexer

#### GET

**Responses:**

- `200`: OK

#### POST

**Parameters:**

- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/IndexerResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/indexer/action/{name}

#### POST

**Parameters:**

- `name` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/IndexerResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/indexer/bulk

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/IndexerBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/IndexerBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/indexer/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/indexer/test

#### POST

**Parameters:**

- `forceTest` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/IndexerResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/indexer/testall

#### POST

**Responses:**

- `200`: OK

### /api/v3/indexer/{id}

#### PUT

**Parameters:**

- `id` (path): N/A
- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/IndexerResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/indexerflag

#### GET

**Responses:**

- `200`: OK

### /api/v3/language

#### GET

**Responses:**

- `200`: OK

### /api/v3/language/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/languageprofile

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/LanguageProfileResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/languageprofile/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/languageprofile/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/LanguageProfileResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/localization

#### GET

**Responses:**

- `200`: OK

### /api/v3/localization/language

#### GET

**Responses:**

- `200`: OK

### /api/v3/localization/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/log

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `level` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/log/file

#### GET

**Responses:**

- `200`: OK

### /api/v3/log/file/update

#### GET

**Responses:**

- `200`: OK

### /api/v3/log/file/update/{filename}

#### GET

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/log/file/{filename}

#### GET

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/manualimport

#### GET

**Parameters:**

- `folder` (query): N/A
- `downloadId` (query): N/A
- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `filterExistingFiles` (query): N/A

**Responses:**

- `200`: OK

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/ManualImportReprocessResource"
        }
      }
    }
...
```

**Responses:**

- `200`: OK

### /api/v3/mediacover/{seriesId}/{filename}

#### GET

**Parameters:**

- `seriesId` (path): N/A
- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/metadata

#### GET

**Responses:**

- `200`: OK

#### POST

**Parameters:**

- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/MetadataResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/metadata/action/{name}

#### POST

**Parameters:**

- `name` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/MetadataResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/metadata/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/metadata/test

#### POST

**Parameters:**

- `forceTest` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/MetadataResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/metadata/testall

#### POST

**Responses:**

- `200`: OK

### /api/v3/metadata/{id}

#### PUT

**Parameters:**

- `id` (path): N/A
- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/MetadataResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/notification

#### GET

**Responses:**

- `200`: OK

#### POST

**Parameters:**

- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/NotificationResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/notification/action/{name}

#### POST

**Parameters:**

- `name` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/NotificationResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/notification/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/notification/test

#### POST

**Parameters:**

- `forceTest` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/NotificationResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/notification/testall

#### POST

**Responses:**

- `200`: OK

### /api/v3/notification/{id}

#### PUT

**Parameters:**

- `id` (path): N/A
- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/NotificationResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/parse

#### GET

**Parameters:**

- `title` (query): N/A
- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/qualitydefinition

#### GET

**Responses:**

- `200`: OK

### /api/v3/qualitydefinition/limits

#### GET

**Responses:**

- `200`: OK

### /api/v3/qualitydefinition/update

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/QualityDefinitionResource"
        }
      }
    },
   ...
```

**Responses:**

- `200`: OK

### /api/v3/qualitydefinition/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/QualityDefinitionResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/com...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/qualityprofile

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/QualityProfileResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/qualityprofile/schema

#### GET

**Responses:**

- `200`: OK

### /api/v3/qualityprofile/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/QualityProfileResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/queue

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `includeUnknownSeriesItems` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A
- `seriesIds` (query): N/A
- `protocol` (query): N/A
- `languages` (query): N/A
- `quality` (query): N/A
- `status` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/queue/bulk

#### DELETE

**Parameters:**

- `removeFromClient` (query): N/A
- `blocklist` (query): N/A
- `skipRedownload` (query): N/A
- `changeCategory` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/QueueBulkResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/components/...
```

**Responses:**

- `200`: OK

### /api/v3/queue/details

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `episodeIds` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/queue/grab/bulk

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/QueueBulkResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/queue/grab/{id}

#### POST

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/queue/status

#### GET

**Responses:**

- `200`: OK

### /api/v3/queue/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A
- `removeFromClient` (query): N/A
- `blocklist` (query): N/A
- `skipRedownload` (query): N/A
- `changeCategory` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/release

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ReleaseResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `episodeId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/release/push

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ReleaseResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/releaseprofile

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ReleaseProfileResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/compon...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/releaseprofile/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ReleaseProfileResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/compon...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/remotepathmapping

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/RemotePathMappingResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/remotepathmapping/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/RemotePathMappingResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/com...
```

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/rename

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/rootfolder

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/RootFolderResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /api/v3/rootfolder/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/seasonpass

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SeasonPassResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/series

#### GET

**Parameters:**

- `tvdbId` (query): N/A
- `includeSeasonImages` (query): N/A

**Responses:**

- `200`: OK

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SeriesResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/series/editor

#### PUT

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SeriesEditorResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/componen...
```

**Responses:**

- `200`: OK

#### DELETE

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SeriesEditorResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/componen...
```

**Responses:**

- `200`: OK

### /api/v3/series/import

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/SeriesResource"
        }
      }
    },
    "text/json...
```

**Responses:**

- `200`: OK

### /api/v3/series/lookup

#### GET

**Parameters:**

- `term` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/series/{id}

#### GET

**Parameters:**

- `id` (path): N/A
- `includeSeasonImages` (query): N/A

**Responses:**

- `200`: OK

#### PUT

**Parameters:**

- `moveFiles` (query): N/A
- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SeriesResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A
- `deleteFiles` (query): N/A
- `addImportListExclusion` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/series/{id}/folder

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/system/backup

#### GET

**Responses:**

- `200`: OK

### /api/v3/system/backup/restore/upload

#### POST

**Responses:**

- `200`: OK

### /api/v3/system/backup/restore/{id}

#### POST

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/system/backup/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/system/restart

#### POST

**Responses:**

- `200`: OK

### /api/v3/system/routes

#### GET

**Responses:**

- `200`: OK

### /api/v3/system/routes/duplicate

#### GET

**Responses:**

- `200`: OK

### /api/v3/system/shutdown

#### POST

**Responses:**

- `200`: OK

### /api/v3/system/status

#### GET

**Responses:**

- `200`: OK

### /api/v3/system/task

#### GET

**Responses:**

- `200`: OK

### /api/v3/system/task/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/tag

#### GET

**Responses:**

- `200`: OK

#### POST

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TagResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v3/tag/detail

#### GET

**Responses:**

- `200`: OK

### /api/v3/tag/detail/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/tag/{id}

#### PUT

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/TagResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/update

#### GET

**Responses:**

- `200`: OK

### /api/v3/wanted/cutoff

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisodeFile` (query): N/A
- `includeImages` (query): N/A
- `monitored` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/wanted/cutoff/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/wanted/missing

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `includeSeries` (query): N/A
- `includeImages` (query): N/A
- `monitored` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/wanted/missing/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /content/{path}

#### GET

**Parameters:**

- `path` (path): N/A

**Responses:**

- `200`: OK

### /feed/v3/calendar/sonarr.ics

#### GET

**Parameters:**

- `pastDays` (query): N/A
- `futureDays` (query): N/A
- `tags` (query): N/A
- `unmonitored` (query): N/A
- `premieresOnly` (query): N/A
- `asAllDay` (query): N/A

**Responses:**

- `200`: OK

### /login

#### POST

**Parameters:**

- `returnUrl` (query): N/A

**Request Body:**

```json
{
  "content": {
    "multipart/form-data": {
      "schema": {
        "type": "object",
        "properties": {
          "username": {
            "type": "string"
          },
          "password"...
```

**Responses:**

- `200`: OK

#### GET

**Responses:**

- `200`: OK

### /logout

#### GET

**Responses:**

- `200`: OK

### /ping

#### GET

**Responses:**

- `200`: OK

### /{path}

#### GET

**Parameters:**

- `path` (path): N/A

**Responses:**

- `200`: OK

## Data Models

### AddSeriesOptions

**Properties:**

- `ignoreEpisodesWithFiles` (boolean): N/A
- `ignoreEpisodesWithoutFiles` (boolean): N/A
- `monitor` (unknown): N/A
- `searchForMissingEpisodes` (boolean): N/A
- `searchForCutoffUnmetEpisodes` (boolean): N/A

### AlternateTitleResource

**Properties:**

- `title` (string): N/A
- `seasonNumber` (integer): N/A
- `sceneSeasonNumber` (integer): N/A
- `sceneOrigin` (string): N/A
- `comment` (string): N/A

### ApplyTags

### AuthenticationRequiredType

### AuthenticationType

### AutoTaggingResource

**Properties:**

- `id` (integer): N/A
- `name` (string): N/A
- `removeTagsAutomatically` (boolean): N/A
- `tags` (array): N/A
- `specifications` (array): N/A

### AutoTaggingSpecificationSchema

**Properties:**

- `id` (integer): N/A
- `name` (string): N/A
- `implementation` (string): N/A
- `implementationName` (string): N/A
- `negate` (boolean): N/A
- `required` (boolean): N/A
- `fields` (array): N/A

### BackupResource

**Properties:**

- `id` (integer): N/A
- `name` (string): N/A
- `path` (string): N/A
- `type` (unknown): N/A
- `size` (integer): N/A
- `time` (string): N/A

### BackupType

### BlocklistBulkResource

**Properties:**

- `ids` (array): N/A

### BlocklistResource

**Properties:**

- `id` (integer): N/A
- `seriesId` (integer): N/A
- `episodeIds` (array): N/A
- `sourceTitle` (string): N/A
- `languages` (array): N/A
- `quality` (unknown): N/A
- `customFormats` (array): N/A
- `date` (string): N/A
- `protocol` (unknown): N/A
- `indexer` (string): N/A
- `message` (string): N/A
- `series` (unknown): N/A

### BlocklistResourcePagingResource

**Properties:**

- `page` (integer): N/A
- `pageSize` (integer): N/A
- `sortKey` (string): N/A
- `sortDirection` (unknown): N/A
- `totalRecords` (integer): N/A
- `records` (array): N/A

### CertificateValidationType

### Command

**Properties:**

- `sendUpdatesToClient` (boolean): N/A
- `updateScheduledTask` (boolean): N/A
- `completionMessage` (string): N/A
- `requiresDiskAccess` (boolean): N/A
- `isExclusive` (boolean): N/A
- `isLongRunning` (boolean): N/A
- `name` (string): N/A
- `lastExecutionTime` (string): N/A
- `lastStartTime` (string): N/A
- `trigger` (unknown): N/A
- `suppressMessages` (boolean): N/A
- `clientUserAgent` (string): N/A

### CommandPriority

### CommandResource

**Properties:**

- `id` (integer): N/A
- `name` (string): N/A
- `commandName` (string): N/A
- `message` (string): N/A
- `body` (unknown): N/A
- `priority` (unknown): N/A
- `status` (unknown): N/A
- `result` (unknown): N/A
- `queued` (string): N/A
- `started` (string): N/A
- `ended` (string): N/A
- `duration` (string): N/A
- `exception` (string): N/A
- `trigger` (unknown): N/A
- `clientUserAgent` (string): N/A
- `stateChangeTime` (string): N/A
- `sendUpdatesToClient` (boolean): N/A
- `updateScheduledTask` (boolean): N/A
- `lastExecutionTime` (string): N/A

### CommandResult

### CommandStatus

### CommandTrigger

### CustomFilterResource

**Properties:**

- `id` (integer): N/A
- `type` (string): N/A
- `label` (string): N/A
- `filters` (array): N/A

