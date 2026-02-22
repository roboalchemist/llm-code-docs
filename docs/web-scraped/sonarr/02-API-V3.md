# Sonarr V3 API

## Servers

- {protocol}://{hostpath}:

## API Information

**Version:** 3.0.0
**Title:** Sonarr

Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

## API Endpoints

### /

#### GET /

**Parameters:**

- `path` (path): N/A

**Responses:**

- `200`: OK

### /api

#### GET /api

**Responses:**

- `200`: OK

### /api/v3/autotagging

#### POST /api/v3/autotagging

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

#### GET /api/v3/autotagging

**Responses:**

- `200`: OK

### /api/v3/autotagging/schema

#### GET /api/v3/autotagging/schema

**Responses:**

- `200`: OK

### /api/v3/autotagging/{id}

#### PUT /api/v3/autotagging/{id}

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

#### DELETE /api/v3/autotagging/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/autotagging/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/blocklist

#### GET /api/v3/blocklist

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

#### DELETE /api/v3/blocklist/bulk

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

#### DELETE /api/v3/blocklist/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/calendar

#### GET /api/v3/calendar

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

#### GET /api/v3/calendar/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/command

#### POST /api/v3/command

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

#### GET /api/v3/command

**Responses:**

- `200`: OK

### /api/v3/command/{id}

#### DELETE /api/v3/command/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/command/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/downloadclient

#### GET /api/v3/config/downloadclient

**Responses:**

- `200`: OK

### /api/v3/config/downloadclient/{id}

#### PUT /api/v3/config/downloadclient/{id}

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

#### GET /api/v3/config/downloadclient/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/host

#### GET /api/v3/config/host

**Responses:**

- `200`: OK

### /api/v3/config/host/{id}

#### PUT /api/v3/config/host/{id}

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

#### GET /api/v3/config/host/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/importlist

#### GET /api/v3/config/importlist

**Responses:**

- `200`: OK

### /api/v3/config/importlist/{id}

#### PUT /api/v3/config/importlist/{id}

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

#### GET /api/v3/config/importlist/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/indexer

#### GET /api/v3/config/indexer

**Responses:**

- `200`: OK

### /api/v3/config/indexer/{id}

#### PUT /api/v3/config/indexer/{id}

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

#### GET /api/v3/config/indexer/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/mediamanagement

#### GET /api/v3/config/mediamanagement

**Responses:**

- `200`: OK

### /api/v3/config/mediamanagement/{id}

#### PUT /api/v3/config/mediamanagement/{id}

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

#### GET /api/v3/config/mediamanagement/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/naming

#### GET /api/v3/config/naming

**Responses:**

- `200`: OK

### /api/v3/config/naming/examples

#### GET /api/v3/config/naming/examples

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

#### PUT /api/v3/config/naming/{id}

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

#### GET /api/v3/config/naming/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/config/ui

#### GET /api/v3/config/ui

**Responses:**

- `200`: OK

### /api/v3/config/ui/{id}

#### PUT /api/v3/config/ui/{id}

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

#### GET /api/v3/config/ui/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/customfilter

#### GET /api/v3/customfilter

**Responses:**

- `200`: OK

#### POST /api/v3/customfilter

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

#### PUT /api/v3/customfilter/{id}

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

#### DELETE /api/v3/customfilter/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/customfilter/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/customformat

#### GET /api/v3/customformat

**Responses:**

- `200`: OK

#### POST /api/v3/customformat

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

#### PUT /api/v3/customformat/bulk

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

#### DELETE /api/v3/customformat/bulk

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

#### GET /api/v3/customformat/schema

**Responses:**

- `200`: OK

### /api/v3/customformat/{id}

#### PUT /api/v3/customformat/{id}

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

#### DELETE /api/v3/customformat/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/customformat/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/delayprofile

#### POST /api/v3/delayprofile

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

#### GET /api/v3/delayprofile

**Responses:**

- `200`: OK

### /api/v3/delayprofile/reorder/{id}

#### PUT /api/v3/delayprofile/reorder/{id}

**Parameters:**

- `id` (path): N/A
- `after` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/delayprofile/{id}

#### DELETE /api/v3/delayprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v3/delayprofile/{id}

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

#### GET /api/v3/delayprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/diskspace

#### GET /api/v3/diskspace

**Responses:**

- `200`: OK

### /api/v3/downloadclient

#### GET /api/v3/downloadclient

**Responses:**

- `200`: OK

#### POST /api/v3/downloadclient

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

#### POST /api/v3/downloadclient/action/{name}

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

#### PUT /api/v3/downloadclient/bulk

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

#### DELETE /api/v3/downloadclient/bulk

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

#### GET /api/v3/downloadclient/schema

**Responses:**

- `200`: OK

### /api/v3/downloadclient/test

#### POST /api/v3/downloadclient/test

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

#### POST /api/v3/downloadclient/testall

**Responses:**

- `200`: OK

### /api/v3/downloadclient/{id}

#### PUT /api/v3/downloadclient/{id}

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

#### DELETE /api/v3/downloadclient/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/downloadclient/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/episode

#### GET /api/v3/episode

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

#### PUT /api/v3/episode/monitor

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

#### PUT /api/v3/episode/{id}

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

#### GET /api/v3/episode/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/episodefile

#### GET /api/v3/episodefile

**Parameters:**

- `seriesId` (query): N/A
- `episodeFileIds` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/episodefile/bulk

#### DELETE /api/v3/episodefile/bulk

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

#### PUT /api/v3/episodefile/bulk

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

#### PUT /api/v3/episodefile/editor

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

#### PUT /api/v3/episodefile/{id}

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

#### DELETE /api/v3/episodefile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/episodefile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/filesystem

#### GET /api/v3/filesystem

**Parameters:**

- `path` (query): N/A
- `includeFiles` (query): N/A
- `allowFoldersWithoutTrailingSlashes` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/filesystem/mediafiles

#### GET /api/v3/filesystem/mediafiles

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/filesystem/type

#### GET /api/v3/filesystem/type

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/health

#### GET /api/v3/health

**Responses:**

- `200`: OK

### /api/v3/history

#### GET /api/v3/history

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

#### POST /api/v3/history/failed/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/history/series

#### GET /api/v3/history/series

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `eventType` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/history/since

#### GET /api/v3/history/since

**Parameters:**

- `date` (query): N/A
- `eventType` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/importlist

#### GET /api/v3/importlist

**Responses:**

- `200`: OK

#### POST /api/v3/importlist

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

#### POST /api/v3/importlist/action/{name}

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

#### PUT /api/v3/importlist/bulk

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

#### DELETE /api/v3/importlist/bulk

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

#### GET /api/v3/importlist/schema

**Responses:**

- `200`: OK

### /api/v3/importlist/test

#### POST /api/v3/importlist/test

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

#### POST /api/v3/importlist/testall

**Responses:**

- `200`: OK

### /api/v3/importlist/{id}

#### PUT /api/v3/importlist/{id}

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

#### DELETE /api/v3/importlist/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/importlist/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/importlistexclusion

#### GET /api/v3/importlistexclusion

**Responses:**

- `200`: OK

#### POST /api/v3/importlistexclusion

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

#### DELETE /api/v3/importlistexclusion/bulk

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

#### GET /api/v3/importlistexclusion/paged

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/importlistexclusion/{id}

#### PUT /api/v3/importlistexclusion/{id}

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

#### DELETE /api/v3/importlistexclusion/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/importlistexclusion/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/indexer

#### GET /api/v3/indexer

**Responses:**

- `200`: OK

#### POST /api/v3/indexer

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

#### POST /api/v3/indexer/action/{name}

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

#### PUT /api/v3/indexer/bulk

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

#### DELETE /api/v3/indexer/bulk

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

#### GET /api/v3/indexer/schema

**Responses:**

- `200`: OK

### /api/v3/indexer/test

#### POST /api/v3/indexer/test

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

#### POST /api/v3/indexer/testall

**Responses:**

- `200`: OK

### /api/v3/indexer/{id}

#### PUT /api/v3/indexer/{id}

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

#### DELETE /api/v3/indexer/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/indexer/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/indexerflag

#### GET /api/v3/indexerflag

**Responses:**

- `200`: OK

### /api/v3/language

#### GET /api/v3/language

**Responses:**

- `200`: OK

### /api/v3/language/{id}

#### GET /api/v3/language/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/languageprofile

#### POST /api/v3/languageprofile

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

#### GET /api/v3/languageprofile

**Responses:**

- `200`: OK

### /api/v3/languageprofile/schema

#### GET /api/v3/languageprofile/schema

**Responses:**

- `200`: OK

### /api/v3/languageprofile/{id}

#### DELETE /api/v3/languageprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v3/languageprofile/{id}

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

#### GET /api/v3/languageprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/localization

#### GET /api/v3/localization

**Responses:**

- `200`: OK

### /api/v3/localization/language

#### GET /api/v3/localization/language

**Responses:**

- `200`: OK

### /api/v3/localization/{id}

#### GET /api/v3/localization/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/log

#### GET /api/v3/log

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `level` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/log/file

#### GET /api/v3/log/file

**Responses:**

- `200`: OK

### /api/v3/log/file/update

#### GET /api/v3/log/file/update

**Responses:**

- `200`: OK

### /api/v3/log/file/update/{filename}

#### GET /api/v3/log/file/update/{filename}

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/log/file/{filename}

#### GET /api/v3/log/file/{filename}

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/manualimport

#### GET /api/v3/manualimport

**Parameters:**

- `folder` (query): N/A
- `downloadId` (query): N/A
- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `filterExistingFiles` (query): N/A

**Responses:**

- `200`: OK

#### POST /api/v3/manualimport

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

#### GET /api/v3/mediacover/{seriesId}/{filename}

**Parameters:**

- `seriesId` (path): N/A
- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/metadata

#### GET /api/v3/metadata

**Responses:**

- `200`: OK

#### POST /api/v3/metadata

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

#### POST /api/v3/metadata/action/{name}

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

#### GET /api/v3/metadata/schema

**Responses:**

- `200`: OK

### /api/v3/metadata/test

#### POST /api/v3/metadata/test

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

#### POST /api/v3/metadata/testall

**Responses:**

- `200`: OK

### /api/v3/metadata/{id}

#### PUT /api/v3/metadata/{id}

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

#### DELETE /api/v3/metadata/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/metadata/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/notification

#### GET /api/v3/notification

**Responses:**

- `200`: OK

#### POST /api/v3/notification

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

#### POST /api/v3/notification/action/{name}

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

#### GET /api/v3/notification/schema

**Responses:**

- `200`: OK

### /api/v3/notification/test

#### POST /api/v3/notification/test

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

#### POST /api/v3/notification/testall

**Responses:**

- `200`: OK

### /api/v3/notification/{id}

#### PUT /api/v3/notification/{id}

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

#### DELETE /api/v3/notification/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/notification/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/parse

#### GET /api/v3/parse

**Parameters:**

- `title` (query): N/A
- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/qualitydefinition

#### GET /api/v3/qualitydefinition

**Responses:**

- `200`: OK

### /api/v3/qualitydefinition/limits

#### GET /api/v3/qualitydefinition/limits

**Responses:**

- `200`: OK

### /api/v3/qualitydefinition/update

#### PUT /api/v3/qualitydefinition/update

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

#### PUT /api/v3/qualitydefinition/{id}

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

#### GET /api/v3/qualitydefinition/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/qualityprofile

#### POST /api/v3/qualityprofile

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

#### GET /api/v3/qualityprofile

**Responses:**

- `200`: OK

### /api/v3/qualityprofile/schema

#### GET /api/v3/qualityprofile/schema

**Responses:**

- `200`: OK

### /api/v3/qualityprofile/{id}

#### DELETE /api/v3/qualityprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v3/qualityprofile/{id}

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

#### GET /api/v3/qualityprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/queue

#### GET /api/v3/queue

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

#### DELETE /api/v3/queue/bulk

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

#### GET /api/v3/queue/details

**Parameters:**

- `seriesId` (query): N/A
- `episodeIds` (query): N/A
- `includeSeries` (query): N/A
- `includeEpisode` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/queue/grab/bulk

#### POST /api/v3/queue/grab/bulk

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

#### POST /api/v3/queue/grab/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/queue/status

#### GET /api/v3/queue/status

**Responses:**

- `200`: OK

### /api/v3/queue/{id}

#### DELETE /api/v3/queue/{id}

**Parameters:**

- `id` (path): N/A
- `removeFromClient` (query): N/A
- `blocklist` (query): N/A
- `skipRedownload` (query): N/A
- `changeCategory` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/release

#### POST /api/v3/release

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

#### GET /api/v3/release

**Parameters:**

- `seriesId` (query): N/A
- `episodeId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/release/push

#### POST /api/v3/release/push

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

#### POST /api/v3/releaseprofile

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

#### GET /api/v3/releaseprofile

**Responses:**

- `200`: OK

### /api/v3/releaseprofile/{id}

#### DELETE /api/v3/releaseprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v3/releaseprofile/{id}

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

#### GET /api/v3/releaseprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/remotepathmapping

#### POST /api/v3/remotepathmapping

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

#### GET /api/v3/remotepathmapping

**Responses:**

- `200`: OK

### /api/v3/remotepathmapping/{id}

#### DELETE /api/v3/remotepathmapping/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v3/remotepathmapping/{id}

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

#### GET /api/v3/remotepathmapping/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/rename

#### GET /api/v3/rename

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/rootfolder

#### POST /api/v3/rootfolder

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

#### GET /api/v3/rootfolder

**Responses:**

- `200`: OK

### /api/v3/rootfolder/{id}

#### DELETE /api/v3/rootfolder/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/rootfolder/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/seasonpass

#### POST /api/v3/seasonpass

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

#### GET /api/v3/series

**Parameters:**

- `tvdbId` (query): N/A
- `includeSeasonImages` (query): N/A

**Responses:**

- `200`: OK

#### POST /api/v3/series

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

#### PUT /api/v3/series/editor

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

#### DELETE /api/v3/series/editor

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

#### POST /api/v3/series/import

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

#### GET /api/v3/series/lookup

**Parameters:**

- `term` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/series/{id}

#### GET /api/v3/series/{id}

**Parameters:**

- `id` (path): N/A
- `includeSeasonImages` (query): N/A

**Responses:**

- `200`: OK

#### PUT /api/v3/series/{id}

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

#### DELETE /api/v3/series/{id}

**Parameters:**

- `id` (path): N/A
- `deleteFiles` (query): N/A
- `addImportListExclusion` (query): N/A

**Responses:**

- `200`: OK

### /api/v3/series/{id}/folder

#### GET /api/v3/series/{id}/folder

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/system/backup

#### GET /api/v3/system/backup

**Responses:**

- `200`: OK

### /api/v3/system/backup/restore/upload

#### POST /api/v3/system/backup/restore/upload

**Responses:**

- `200`: OK

### /api/v3/system/backup/restore/{id}

#### POST /api/v3/system/backup/restore/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/system/backup/{id}

#### DELETE /api/v3/system/backup/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/system/restart

#### POST /api/v3/system/restart

**Responses:**

- `200`: OK

### /api/v3/system/routes

#### GET /api/v3/system/routes

**Responses:**

- `200`: OK

### /api/v3/system/routes/duplicate

#### GET /api/v3/system/routes/duplicate

**Responses:**

- `200`: OK

### /api/v3/system/shutdown

#### POST /api/v3/system/shutdown

**Responses:**

- `200`: OK

### /api/v3/system/status

#### GET /api/v3/system/status

**Responses:**

- `200`: OK

### /api/v3/system/task

#### GET /api/v3/system/task

**Responses:**

- `200`: OK

### /api/v3/system/task/{id}

#### GET /api/v3/system/task/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/tag

#### GET /api/v3/tag

**Responses:**

- `200`: OK

#### POST /api/v3/tag

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

#### GET /api/v3/tag/detail

**Responses:**

- `200`: OK

### /api/v3/tag/detail/{id}

#### GET /api/v3/tag/detail/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/tag/{id}

#### PUT /api/v3/tag/{id}

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

#### DELETE /api/v3/tag/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v3/tag/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/update

#### GET /api/v3/update

**Responses:**

- `200`: OK

### /api/v3/wanted/cutoff

#### GET /api/v3/wanted/cutoff

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

#### GET /api/v3/wanted/cutoff/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v3/wanted/missing

#### GET /api/v3/wanted/missing

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

#### GET /api/v3/wanted/missing/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /content/{path}

#### GET /content/{path}

**Parameters:**

- `path` (path): N/A

**Responses:**

- `200`: OK

### /feed/v3/calendar/sonarr.ics

#### GET /feed/v3/calendar/sonarr.ics

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

#### POST /login

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

#### GET /login

**Responses:**

- `200`: OK

### /logout

#### GET /logout

**Responses:**

- `200`: OK

### /ping

#### GET /ping

**Responses:**

- `200`: OK

### /{path}

#### GET /{path}

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
