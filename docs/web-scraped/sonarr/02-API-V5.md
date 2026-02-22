# Sonarr V5 API

## Servers

- {protocol}://{hostpath}: 

## API Information

**Version:** 5.0.0
**Title:** Sonarr

Sonarr API docs - The v5 API docs apply to Sonarr v5 only.

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

### /api/v5/blocklist

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

### /api/v5/blocklist/bulk

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

### /api/v5/blocklist/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/calendar

#### GET

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

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/command

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

### /api/v5/command/{id}

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

### /api/v5/connection

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
        "$ref": "#/components/schemas/ConnectionResource"
      }
    }
  }
}...
```

**Responses:**

- `200`: OK

### /api/v5/connection/action/{name}

#### POST

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

#### GET

**Responses:**

- `200`: OK

### /api/v5/connection/test

#### POST

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

#### POST

**Responses:**

- `200`: OK

### /api/v5/connection/{id}

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
        "$ref": "#/components/schemas/ConnectionResource"
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

### /api/v5/customfilter

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

### /api/v5/customfilter/{id}

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

### /api/v5/diskspace

#### GET

**Responses:**

- `200`: OK

### /api/v5/episode

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `episodeIds` (query): N/A
- `episodeFileId` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/episode/monitor

#### PUT

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

### /api/v5/episodefile

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `episodeFileIds` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/episodefile/bulk

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

### /api/v5/episodefile/{id}

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

### /api/v5/filesystem

#### GET

**Parameters:**

- `path` (query): N/A
- `includeFiles` (query): N/A
- `allowFoldersWithoutTrailingSlashes` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/filesystem/mediafiles

#### GET

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/filesystem/type

#### GET

**Parameters:**

- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/health

#### GET

**Responses:**

- `200`: OK

### /api/v5/history

#### GET

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

#### GET

**Parameters:**

- `episodeId` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/history/failed/{id}

#### POST

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/history/season

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/history/series

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/history/since

#### GET

**Parameters:**

- `date` (query): N/A
- `eventType` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/localization

#### GET

**Responses:**

- `200`: OK

### /api/v5/localization/language

#### GET

**Responses:**

- `200`: OK

### /api/v5/localization/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/log

#### GET

**Parameters:**

- `page` (query): N/A
- `pageSize` (query): N/A
- `sortKey` (query): N/A
- `sortDirection` (query): N/A
- `level` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/log/file

#### GET

**Responses:**

- `200`: OK

### /api/v5/log/file/update

#### GET

**Responses:**

- `200`: OK

### /api/v5/log/file/update/{filename}

#### GET

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/log/file/{filename}

#### GET

**Parameters:**

- `filename` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/manualimport

#### GET

**Parameters:**

- `folder` (query): N/A
- `downloadIds` (query): N/A
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

### /api/v5/metadata

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

### /api/v5/metadata/action/{name}

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

### /api/v5/metadata/schema

#### GET

**Responses:**

- `200`: OK

### /api/v5/metadata/test

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

### /api/v5/metadata/testall

#### POST

**Responses:**

- `200`: OK

### /api/v5/metadata/{id}

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

### /api/v5/parse

#### GET

**Parameters:**

- `title` (query): N/A
- `path` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/qualitydefinition

#### GET

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
          "$ref": "#/components/schemas/QualityDefinitionResource"
        }
      }
    },
   ...
```

**Responses:**

- `200`: OK

### /api/v5/qualitydefinition/{id}

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

### /api/v5/qualityprofile

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

### /api/v5/qualityprofile/schema

#### GET

**Responses:**

- `200`: OK

### /api/v5/qualityprofile/{id}

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

### /api/v5/queue

#### GET

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

#### DELETE

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

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `episodeIds` (query): N/A
- `includeSubresources` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/queue/grab/bulk

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

### /api/v5/queue/grab/{id}

#### POST

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/queue/status

#### GET

**Responses:**

- `200`: OK

### /api/v5/queue/{id}

#### DELETE

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

#### POST

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

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `episodeId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/release/push

#### POST

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

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/releaseprofile

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

### /api/v5/releaseprofile/{id}

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

### /api/v5/remotepathmapping

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

### /api/v5/remotepathmapping/{id}

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

### /api/v5/rename

#### GET

**Parameters:**

- `seriesId` (query): N/A
- `seasonNumber` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/rename/bulk

#### GET

**Parameters:**

- `seriesIds` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/rootfolder

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

### /api/v5/rootfolder/{id}

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

### /api/v5/seasonpass

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

### /api/v5/series

#### GET

**Parameters:**

- `tvdbId` (query): N/A
- `includeSubresources` (query): N/A

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

### /api/v5/series/editor

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

### /api/v5/series/import

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

### /api/v5/series/lookup

#### GET

**Parameters:**

- `term` (query): N/A

**Responses:**

- `200`: OK

### /api/v5/series/{id}

#### GET

**Parameters:**

- `id` (path): N/A
- `includeSubresources` (query): N/A

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

### /api/v5/series/{id}/folder

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/series/{id}/season

#### PUT

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

#### GET

**Responses:**

- `200`: OK

### /api/v5/settings/mediamanagement/{id}

#### PUT

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

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/settings/naming

#### GET

**Responses:**

- `200`: OK

### /api/v5/settings/naming/examples

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

### /api/v5/settings/naming/{id}

#### PUT

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

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/settings/ui

#### GET

**Responses:**

- `200`: OK

### /api/v5/settings/ui/{id}

#### PUT

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

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/settings/update

#### GET

**Responses:**

- `200`: OK

#### PUT

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

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/system/backup

#### GET

**Responses:**

- `200`: OK

### /api/v5/system/backup/restore/upload

#### POST

**Responses:**

- `200`: OK

### /api/v5/system/backup/restore/{id}

#### POST

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/system/backup/{id}

#### DELETE

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/system/restart

#### POST

**Responses:**

- `200`: OK

### /api/v5/system/routes

#### GET

**Responses:**

- `200`: OK

### /api/v5/system/routes/duplicate

#### GET

**Responses:**

- `200`: OK

### /api/v5/system/shutdown

#### POST

**Responses:**

- `200`: OK

### /api/v5/system/status

#### GET

**Responses:**

- `200`: OK

### /api/v5/system/task

#### GET

**Responses:**

- `200`: OK

### /api/v5/system/task/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/tag

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

### /api/v5/tag/detail

#### GET

**Responses:**

- `200`: OK

### /api/v5/tag/detail/{id}

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/tag/{id}

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

### /api/v5/update

#### GET

**Responses:**

- `200`: OK

### /api/v5/wanted/cutoff

#### GET

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

#### GET

**Parameters:**

- `id` (path): N/A

**Responses:**

- `200`: OK

### /api/v5/wanted/missing

#### GET

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

### /feed/v5/calendar/sonarr.ics

#### GET

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

