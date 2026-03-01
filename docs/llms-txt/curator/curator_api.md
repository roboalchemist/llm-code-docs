# Source: https://docs.curator.interworks.com/curator_api/api_docs/curator_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Curator API

> Complete API reference for Curator including portal information, user management and system endpoints.

## /portal/info

Returns all information about Curator.

**Parameters:**

**boolean**
ini Shows PHP ini settings
**boolean**
extensions Shows loaded PHP extensions

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "version": "2020.09.17-01",
        "kernel_build": 446,
        "key": "[YOUR KEY HERE]",
        "php_version": "7.2.11",
        "os": "Linux ip-XX-XX-XX-XXXus-west.compute.internal 4.14.77-86.82.amzn2.x86_64 #1 SMP Tue Dec 1 20:40:13 UTC 2018 x86_64",
        "user": "apache",
        "server_addr": "ip-XXX-XX-XX-XXX.us-west-2.compute.internal",
        "server_ips": [
            "XX.XXX.XXX.X,
            "XXX.XX.XX.XXX",
            "curatordemo.interworks.com",
            "ip-XX-XX-XX-XXX.us-west.compute.internal"
        ],
        "database": "mysql",
        "display_errors": "Off",
        "max_execution_time": "60",
        "cache": "memcached",
        "gd": true,
        "fileinfo": true,
        "zip": true,
        "zlib": true,
        "curl": true,
        "openssl": true,
        "memcached": true,
        "php_ini_path": "\/etc\/php.ini",
        "tableau_version": "2018.1",
        "php_location": "\/usr\/bin\/php",
        "is_windows": false,
        "post_max_size": "250M",
        "upload_max_filesize": "250M",
        "memory_limit": "1024M",
        "webroot": "\/var\/www\/html",
        "cron_timestamp": "2019-01-08T21:01:02+00:00",
        "writeable": true,
        "upload_max_filesize_bytes": 262144000,
        "post_max_size_bytes": 262144000,
        "memory_limit_bytes": 1073741824,
        "install_files": false,
        "cron_check": true
    }
```

## /portal/version

Returns version information about the Curator portal.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "version": "2017.08.10-01"
    }
```

## /portal/key

Returns key for the Curator portal.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "key": "1234-5678-9101-1112-1314"
    }
```

## /portal/setKey

Sets the Curator's portal key.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/upgrade

Upgrades Curator to the latest version.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/cron

Runs the Curator Schedules.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/migrations

Runs database migrations.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/clearCache

Clears Curator cache.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/phpinfo

Returns the PHP Information Page

**Returns:**

array

## /portal/setPortalName

Sets the Curator portal name.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/octoberUpgrade

Upgrades the underlying OctoberCMS.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/export

Exports Curator portal data.

**Parameters:**

**string**
models (optional) Comma separated list of models to export. Default: everything.  Options include:

* `api_keys`
* `attributes`
* `commands`
* `connections`
* `dashboards`
* `favorites`
* `files`
* `filter_categories`
* `filters`
* `fonts`
* `frontend_groups`
* `frontend_group_overrides`
* `groups`
* `items`
* `interworks_authentication_settings`
* `interworks_integration_settings`
* `interworks_portal_settings`
* `interworks_tableauviz_settings`
* `interworks_usermgmt_samlsettings`
* `keywords`
* `loading_screens`
* `navigation`
* `notices`
* `pages`
* `parameters`
* `powerbi_dashboards`
* `powerbi_reports`
* `scheduledreport`
* `scripts`
* `slideshows`
* `themes`
* `tos`
* `tutorials`
* `user_comments  `

**boolean**
thumbnails (optional) Whether to include thumbnails in the export. Default: false.

**boolean**
tiles (optional) Whether the output data should use the tile information instead of export. Default: false.

**Returns:**

array

## /portal/cacheInfo

Returns all cache information about Curator

**Parameters:**
**boolean**
ini Shows PHP ini settings
**boolean**
extensions Shows loaded PHP extensions

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": {
            "cms_cache_path": "5.7 KB",
            "cms_combiner_path": "964.04 KB",
            "twig_cache": "529.57 KB",
            "framework_cache": "1.05 MB",
            "thumbnails": "28.95 MB"
        }
    }
```

## /portal/setAnalyticsSettings

Sets the analytics tracking settings.

**Returns:**

array

## /portal/setParameter

Sets a system parameter.

**Parameters:**
**Returns:**

array

## /portal/cleanSettings

Cleans up settings data, if there are duplicates.

**Returns:**

array

## /portal/fixStoragePerms

Attempts to fix storage file permissions, recursively.

**Returns:**

array

## /portal/checkSettings

Check settings items.

**Returns:**

array

## /portal/downloadLog

Exports Curator's system log data.

**Returns:**

array

## /portal/cleanUploadDir

Cleans out old uploaded files.

**Returns:**

array

## /portal/features

Returns information on features in use.

**Returns:**

array

## /portal/stats

Returns stats on Curator.

**Returns:**

array

## /portal/styles

Returns head insert and custom stylesheet from Portal Settings.

**Returns:**

array
