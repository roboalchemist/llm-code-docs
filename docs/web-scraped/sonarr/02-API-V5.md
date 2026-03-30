# Sonarr V5 API

## Servers

- {protocol}://{hostpath}:

## API Information

**Version:** 5.0.0
**Title:** Sonarr

Sonarr API docs - The v5 API docs apply to Sonarr v5 only.

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

### /api/v5/blocklist

#### GET /api/v5/blocklist

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `seriesIds` (query): N/A
- `protocols` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/blocklist/bulk

#### DELETE /api/v5/blocklist/bulk

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

### /api/v5/blocklist/{id}

#### DELETE /api/v5/blocklist/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/calendar

#### GET /api/v5/calendar

**Parameters:**

- `start` (query): N/A
- `end` (query): N/A
- `includeUnmonitored` (query): N/A
- `includeSpecials` (query): N/A
- `tags` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/calendar/{id}

#### GET /api/v5/calendar/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/command

#### POST /api/v5/command

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

#### GET /api/v5/command

**Responses:**

- `200`: OK

### /api/v5/command/{id}

#### DELETE /api/v5/command/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v5/command/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/connection

#### GET /api/v5/connection

**Responses:**

- `200`: OK

#### POST /api/v5/connection

**Parameters:**

- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ConnectionResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v5/connection/action/{name}

#### POST /api/v5/connection/action/{name}

**Parameters:**

- `name` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ConnectionResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v5/connection/schema

#### GET /api/v5/connection/schema

**Responses:**

- `200`: OK

### /api/v5/connection/test

#### POST /api/v5/connection/test

**Parameters:**

- `forceTest` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ConnectionResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v5/connection/testall

#### POST /api/v5/connection/testall

**Responses:**

- `200`: OK

### /api/v5/connection/{id}

#### PUT /api/v5/connection/{id}

**Parameters:**

- `id` (path): N/A
- `forceSave` (query): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ConnectionResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### DELETE /api/v5/connection/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v5/connection/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/customfilter

#### GET /api/v5/customfilter

**Responses:**

- `200`: OK

#### POST /api/v5/customfilter

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

### /api/v5/customfilter/{id}

#### PUT /api/v5/customfilter/{id}

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

#### DELETE /api/v5/customfilter/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v5/customfilter/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/diskspace

#### GET /api/v5/diskspace

**Responses:**

- `200`: OK

### /api/v5/episode

#### GET /api/v5/episode

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `episodeIds` (query): N/A
- `episodeFileId` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/episode/monitor

#### PUT /api/v5/episode/monitor

**Parameters:**

- `includeSubresources` (query): N/A

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

### /api/v5/episode/{id}

#### PUT /api/v5/episode/{id}

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

#### GET /api/v5/episode/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/episodefile

#### GET /api/v5/episodefile

**Parameters:**

- `seriesId` (query): N/A
- `episodeFileIds` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/episodefile/bulk

#### DELETE /api/v5/episodefile/bulk

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

#### PUT /api/v5/episodefile/bulk

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

### /api/v5/episodefile/{id}

#### PUT /api/v5/episodefile/{id}

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

#### DELETE /api/v5/episodefile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v5/episodefile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/filesystem

#### GET /api/v5/filesystem

**Parameters:**

- `path` (query): N/A
- `includeFiles` (query): N/A
- `allowFoldersWithoutTrailingSlashes` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/filesystem/mediafiles

#### GET /api/v5/filesystem/mediafiles

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/filesystem/type

#### GET /api/v5/filesystem/type

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/health

#### GET /api/v5/health

**Responses:**

- `200`: OK

### /api/v5/history

#### GET /api/v5/history

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `eventType` (query): N/A
- `episodeId` (query): N/A
- `downloadId` (query): N/A
- `seriesIds` (query): N/A
- `languages` (query): N/A
- `quality` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/history/episode

#### GET /api/v5/history/episode

**Parameters:**

- `episodeId` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/history/failed/{id}

#### POST /api/v5/history/failed/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/history/season

#### GET /api/v5/history/season

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/history/series

#### GET /api/v5/history/series

**Parameters:**

- `seriesId` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/history/since

#### GET /api/v5/history/since

**Parameters:**

- `date` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/localization

#### GET /api/v5/localization

**Responses:**

- `200`: OK

### /api/v5/localization/language

#### GET /api/v5/localization/language

**Responses:**

- `200`: OK

### /api/v5/localization/{id}

#### GET /api/v5/localization/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/log

#### GET /api/v5/log

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `level` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/log/file

#### GET /api/v5/log/file

**Responses:**

- `200`: OK

### /api/v5/log/file/update

#### GET /api/v5/log/file/update

**Responses:**

- `200`: OK

### /api/v5/log/file/update/{filename}

#### GET /api/v5/log/file/update/{filename}

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/log/file/{filename}

#### GET /api/v5/log/file/{filename}

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/manualimport

#### GET /api/v5/manualimport

**Parameters:**

- `folder` (query): N/A
- `downloadIds` (query): N/A
- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `filterExistingFiles` (query): N/A

**Responses:**

- `200`: OK

#### POST /api/v5/manualimport

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

### /api/v5/metadata

#### GET /api/v5/metadata

**Responses:**

- `200`: OK

#### POST /api/v5/metadata

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

### /api/v5/metadata/action/{name}

#### POST /api/v5/metadata/action/{name}

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

### /api/v5/metadata/schema

#### GET /api/v5/metadata/schema

**Responses:**

- `200`: OK

### /api/v5/metadata/test

#### POST /api/v5/metadata/test

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

### /api/v5/metadata/testall

#### POST /api/v5/metadata/testall

**Responses:**

- `200`: OK

### /api/v5/metadata/{id}

#### PUT /api/v5/metadata/{id}

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

#### DELETE /api/v5/metadata/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v5/metadata/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/parse

#### GET /api/v5/parse

**Parameters:**

- `title` (query): N/A
- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/qualitydefinition

#### GET /api/v5/qualitydefinition

**Responses:**

- `200`: OK

#### PUT /api/v5/qualitydefinition

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

### /api/v5/qualitydefinition/{id}

#### PUT /api/v5/qualitydefinition/{id}

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

#### GET /api/v5/qualitydefinition/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/qualityprofile

#### POST /api/v5/qualityprofile

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

#### GET /api/v5/qualityprofile

**Responses:**

- `200`: OK

### /api/v5/qualityprofile/schema

#### GET /api/v5/qualityprofile/schema

**Responses:**

- `200`: OK

### /api/v5/qualityprofile/{id}

#### DELETE /api/v5/qualityprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v5/qualityprofile/{id}

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

#### GET /api/v5/qualityprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/queue

#### GET /api/v5/queue

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `includeUnknownSeriesItems` (query): N/A
- `seriesIds` (query): N/A
- `protocol` (query): N/A
- `languages` (query): N/A
- `quality` (query): N/A
- `status` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/queue/bulk

#### DELETE /api/v5/queue/bulk

**Parameters:**

- `message` (query): N/A
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

### /api/v5/queue/details

#### GET /api/v5/queue/details

**Parameters:**

- `seriesId` (query): N/A
- `episodeIds` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/queue/grab/bulk

#### POST /api/v5/queue/grab/bulk

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

### /api/v5/queue/grab/{id}

#### POST /api/v5/queue/grab/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/queue/status

#### GET /api/v5/queue/status

**Responses:**

- `200`: OK

### /api/v5/queue/{id}

#### DELETE /api/v5/queue/{id}

**Parameters:**

- `id` (path): N/A
- `message` (query): N/A
- `removeFromClient` (query): N/A
- `blocklist` (query): N/A
- `skipRedownload` (query): N/A
- `changeCategory` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/release

#### POST /api/v5/release

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ReleaseGrabResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET /api/v5/release

**Parameters:**

- `seriesId` (query): N/A
- `episodeId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/release/push

#### POST /api/v5/release/push

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/ReleasePushResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v5/release/push/{id}

#### GET /api/v5/release/push/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/releaseprofile

#### POST /api/v5/releaseprofile

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

#### GET /api/v5/releaseprofile

**Responses:**

- `200`: OK

### /api/v5/releaseprofile/{id}

#### DELETE /api/v5/releaseprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v5/releaseprofile/{id}

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

#### GET /api/v5/releaseprofile/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/remotepathmapping

#### POST /api/v5/remotepathmapping

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

#### GET /api/v5/remotepathmapping

**Responses:**

- `200`: OK

### /api/v5/remotepathmapping/{id}

#### DELETE /api/v5/remotepathmapping/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### PUT /api/v5/remotepathmapping/{id}

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

#### GET /api/v5/remotepathmapping/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/rename

#### GET /api/v5/rename

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/rename/bulk

#### GET /api/v5/rename/bulk

**Parameters:**

- `seriesIds` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/rootfolder

#### POST /api/v5/rootfolder

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

#### GET /api/v5/rootfolder

**Responses:**

- `200`: OK

### /api/v5/rootfolder/{id}

#### DELETE /api/v5/rootfolder/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v5/rootfolder/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/seasonpass

#### POST /api/v5/seasonpass

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

### /api/v5/series

#### GET /api/v5/series

**Parameters:**

- `tvdbId` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

#### POST /api/v5/series

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

### /api/v5/series/editor

#### PUT /api/v5/series/editor

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

#### DELETE /api/v5/series/editor

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

### /api/v5/series/import

#### POST /api/v5/series/import

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

### /api/v5/series/lookup

#### GET /api/v5/series/lookup

**Parameters:**

- `term` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/series/{id}

#### GET /api/v5/series/{id}

**Parameters:**

- `id` (path): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

#### PUT /api/v5/series/{id}

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

#### DELETE /api/v5/series/{id}

**Parameters:**

- `id` (path): N/A
- `deleteFiles` (query): N/A
- `addImportListExclusion` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/series/{id}/folder

#### GET /api/v5/series/{id}/folder

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/series/{id}/season

#### PUT /api/v5/series/{id}/season

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/SeasonResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v5/settings/mediamanagement

#### GET /api/v5/settings/mediamanagement

**Responses:**

- `200`: OK

### /api/v5/settings/mediamanagement/{id}

#### PUT /api/v5/settings/mediamanagement/{id}

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/MediaManagementSettingsResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET /api/v5/settings/mediamanagement/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/settings/naming

#### GET /api/v5/settings/naming

**Responses:**

- `200`: OK

### /api/v5/settings/naming/examples

#### GET /api/v5/settings/naming/examples

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

### /api/v5/settings/naming/{id}

#### PUT /api/v5/settings/naming/{id}

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/NamingSettingsResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/compon...
```

**Responses:**

- `200`: OK

#### GET /api/v5/settings/naming/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/settings/ui

#### GET /api/v5/settings/ui

**Responses:**

- `200`: OK

### /api/v5/settings/ui/{id}

#### PUT /api/v5/settings/ui/{id}

**Parameters:**

- `id` (path): N/A

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UiSettingsResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

#### GET /api/v5/settings/ui/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/settings/update

#### GET /api/v5/settings/update

**Responses:**

- `200`: OK

#### PUT /api/v5/settings/update

**Request Body:**

```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/UpdateSettingsResource"
      }
    },
    "text/json": {
      "schema": {
        "$ref": "#/compon...
```

**Responses:**

- `200`: OK

### /api/v5/settings/update/{id}

#### GET /api/v5/settings/update/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/system/backup

#### GET /api/v5/system/backup

**Responses:**

- `200`: OK

### /api/v5/system/backup/restore/upload

#### POST /api/v5/system/backup/restore/upload

**Responses:**

- `200`: OK

### /api/v5/system/backup/restore/{id}

#### POST /api/v5/system/backup/restore/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/system/backup/{id}

#### DELETE /api/v5/system/backup/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/system/restart

#### POST /api/v5/system/restart

**Responses:**

- `200`: OK

### /api/v5/system/routes

#### GET /api/v5/system/routes

**Responses:**

- `200`: OK

### /api/v5/system/routes/duplicate

#### GET /api/v5/system/routes/duplicate

**Responses:**

- `200`: OK

### /api/v5/system/shutdown

#### POST /api/v5/system/shutdown

**Responses:**

- `200`: OK

### /api/v5/system/status

#### GET /api/v5/system/status

**Responses:**

- `200`: OK

### /api/v5/system/task

#### GET /api/v5/system/task

**Responses:**

- `200`: OK

### /api/v5/system/task/{id}

#### GET /api/v5/system/task/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/tag

#### GET /api/v5/tag

**Responses:**

- `200`: OK

#### POST /api/v5/tag

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

### /api/v5/tag/detail

#### GET /api/v5/tag/detail

**Responses:**

- `200`: OK

### /api/v5/tag/detail/{id}

#### GET /api/v5/tag/detail/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/tag/{id}

#### PUT /api/v5/tag/{id}

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

#### DELETE /api/v5/tag/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

#### GET /api/v5/tag/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/update

#### GET /api/v5/update

**Responses:**

- `200`: OK

### /api/v5/wanted/cutoff

#### GET /api/v5/wanted/cutoff

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `monitored` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/wanted/cutoff/{id}

#### GET /api/v5/wanted/cutoff/{id}

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/wanted/missing

#### GET /api/v5/wanted/missing

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `monitored` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/wanted/missing/{id}

#### GET /api/v5/wanted/missing/{id}

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

### /feed/v5/calendar/sonarr.ics

#### GET /feed/v5/calendar/sonarr.ics

**Parameters:**

- `pastDays` (query): N/A
- `futureDays` (query): N/A
- `tags` (query): N/A
- `unmonitored` (query): N/A
- `premieresOnly` (query): N/A
- `asAllDay` (query): N/A
- `includeSpecials` (query): N/A

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

### AuthenticationType

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
- `source` (string): N/A
- `series` (unknown): N/A

### BlocklistResourcePagingResource

**Properties:**

- `page` (integer): N/A
- `pageSize` (integer): N/A
- `sortKey` (string): N/A
- `sortDirection` (unknown): N/A
- `totalRecords` (integer): N/A
- `records` (array): N/A

### CalendarSubresource

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

### ConnectionResource

**Properties:**

- `id` (integer): N/A
- `name` (string): N/A
- `fields` (array): N/A
- `implementationName` (string): N/A
- `implementation` (string): N/A
- `configContract` (string): N/A
- `infoLink` (string): N/A
- `message` (unknown): N/A
- `tags` (array): N/A
- `presets` (array): N/A
- `link` (string): N/A
- `onGrab` (boolean): N/A
- `onDownload` (boolean): N/A
- `onUpgrade` (boolean): N/A
- `onImportComplete` (boolean): N/A
- `onRename` (boolean): N/A
- `onSeriesAdd` (boolean): N/A
- `onSeriesDelete` (boolean): N/A
- `onEpisodeFileDelete` (boolean): N/A
- `onEpisodeFileDeleteForUpgrade` (boolean): N/A
- `onHealthIssue` (boolean): N/A
- `includeHealthWarnings` (boolean): N/A
- `onHealthRestored` (boolean): N/A
- `onApplicationUpdate` (boolean): N/A
- `onManualInteractionRequired` (boolean): N/A
- `supportsOnGrab` (boolean): N/A
- `supportsOnDownload` (boolean): N/A
- `supportsOnUpgrade` (boolean): N/A
- `supportsOnImportComplete` (boolean): N/A
- `supportsOnRename` (boolean): N/A
- `supportsOnSeriesAdd` (boolean): N/A
- `supportsOnSeriesDelete` (boolean): N/A
- `supportsOnEpisodeFileDelete` (boolean): N/A
- `supportsOnEpisodeFileDeleteForUpgrade` (boolean): N/A
- `supportsOnHealthIssue` (boolean): N/A
- `supportsOnHealthRestored` (boolean): N/A
- `supportsOnApplicationUpdate` (boolean): N/A
- `supportsOnManualInteractionRequired` (boolean): N/A
- `testCommand` (string): N/A

### CustomFilterResource

**Properties:**

- `id` (integer): N/A
- `type` (string): N/A
- `label` (string): N/A
- `filters` (array): N/A

### CustomFormatResource

**Properties:**

- `id` (integer): N/A
- `name` (string): N/A
- `includeCustomFormatWhenRenaming` (boolean): N/A
- `specifications` (array): N/A

### CustomFormatSpecificationSchema

**Properties:**

- `id` (integer): N/A
- `name` (string): N/A
- `implementation` (string): N/A
- `implementationName` (string): N/A
- `infoLink` (string): N/A
- `negate` (boolean): N/A
- `required` (boolean): N/A
- `fields` (array): N/A
- `presets` (array): N/A
