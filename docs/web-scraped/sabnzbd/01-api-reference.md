# SABnzbd API Reference

Source: https://sabnzbd.org/wiki/configuration/4.5/api

## Introduction

The SABnzbd API can be reached via:

```text
http://host:port/api
```text

## Request types

Supported output types are `json` (default) and `xml`, which can be specified in the request:

```text
http://host:port/api?output=json
```text

## API Key and NZB key

API requires the users API key to be supplied all API requests in order for it to work. The API key is randomly generated and is static unless the user decides to change the key. The user can see their API key on the General page of the configuration pages.

```text
http://host:port/api?output=json&apikey=APIKEY
```text

If the API-key is missing the request will return `error: API Key Required`, if it is incorrect: `error: API Key Incorrect`.

There is also a separate NZB key, which only allows for adding, modifying and removing jobs in the queue. When this key is used for something else, the request will return `error: API Key Incorrect`.

The `version` and `auth` functions do not require the API key.

## Documentation

NOTE: In all examples below the `apikey=APIKEY&output=json` part is not shown but still necessary.

True/False indicates the API will return the status, for some functions it's always `true`, even if the operation failed.

```json
{
    "status": true
}
```text

---

# Queue functions

| Function | Description |
|----------|-------------|
| queue | Full Queue output |
| pause (queue) | Pause whole queue |
| resume (queue) | Resume whole queue |
| speedlimit | Set speedlimit |
| change_complete_action | Action on queue complete |
| sort | Sort the queue |
| addurl | Add NZB by URL |
| addfile | Add NZB by file upload |
| addlocalfile | Add NZB by local file path |
| pause (single job) | Pause a single job |
| resume (single job) | Resume a single job |
| delete | Delete job |
| purge | Delete all jobs or based on keyword |
| move | Change position of job in queue |
| change_cat | Change job category |
| change_script | Change job script |
| priority | Change job priority |
| change_opts | Change job post-processing |
| rename | Change name and password of job |
| get_files | Get details of files in a job |
| move_nzf_bulk | Move file(s) inside a job |
| delete_nzf | Remove file(s) from a job |

## Full Queue output

Full queue output with details about all jobs.

```text
api?mode=queue&start=START&limit=LIMIT&cat=CATEGORY&priority=PRIORITY&search=SEARCH&nzo_ids=NZO_ID_1,NZO_ID_2,NZO_ID_3
```text

NOTE: Some of the less obvious output parameters are described below.

| Input parameter | Description |
|-----------------|-------------|
| `start` optional | Index of job to start at |
| `limit` optional | Number of jobs to display |
| `search` optional | Filter job names by `search` term |
| `category` / `cat` optional | Only return jobs with the specified category or categories (separated by a comma). Use `*` for Default |
| `priority` optional | Only return jobs with the specified priority or priorities (separated by a comma) |

Priority levels:
- `-2` = Paused
- `-1` = Low Priority
- `0` = Normal Priority
- `1` = High Priority
- `2` = Force

| Input parameter | Description |
|-----------------|-------------|
| `status` optional | Only return jobs with the specified status or statuses (separated by a comma) |

Status values:
- `Downloading`
- `Queued`
- `Paused`
- `Propagating` = Delayed download
- `Fetching` = Job is downloading extra par2 files

| Input parameter | Description |
|-----------------|-------------|
| `nzo_ids` optional | Only return jobs with these `nzo_ids` (separated by a comma) |

| Output parameter | Description |
|------------------|-------------|
| `speedlimit` | In percentage of maximum set by user |
| `speedlimit_abs` | In bytes/s |
| `labels` | Labels like `DUPLICATE`, `ENCRYPTED` and `PROPAGATING X min` |
| `time_added` | Unix timestamp when the job was added to the queue |
| `unpackopts` | See change_opts |

Example output:

```json
{
    "queue": {
        "status": "Downloading",
        "speedlimit": "9",
        "speedlimit_abs": "4718592.0",
        "paused": false,
        "noofslots_total": 2,
        "noofslots": 2,
        "limit": 10,
        "start": 0,
        "timeleft": "0:16:44",
        "speed": "1.3 M",
        "kbpersec": "1296.02",
        "size": "1.2 GB",
        "sizeleft": "1.2 GB",
        "mb": "1277.65",
        "mbleft": "1271.58",
        "slots": [
            {
                "status": "Downloading",
                "index": 0,
                "password": "",
                "avg_age": "2895d",
                "time_added": 1469172000,
                "script": "None",
                "direct_unpack": "10/30",
                "mb": "1277.65",
                "mbleft": "1271.59",
                "mbmissing": "0.0",
                "size": "1.2 GB",
                "sizeleft": "1.2 GB",
                "filename": "TV.Show.S04E11.720p.HDTV.x264",
                "labels": [],
                "priority": "Normal",
                "cat": "tv",
                "timeleft": "0:16:44",
                "percentage": "0",
                "nzo_id": "SABnzbd_nzo_p86tgx",
                "unpackopts": "3"
            }
        ],
        "diskspace1": "161.16",
        "diskspace2": "161.16",
        "diskspacetotal1": "465.21",
        "diskspacetotal2": "465.21"
    }
}
```text

## Pause queue

Pauses the whole queue (do not confuse this with pausing an individual download, this is a global pause).

```text
api?mode=pause
```text

Pauses for `value` minutes.

```text
api?mode=config&name=set_pause&value=50
```text

## Resume queue

Resumes the whole queue (do not confuse this with resuming an individual download, this is a global resume).

```text
api?mode=resume
```text

## Set speedlimit

Sets the speedlimit to `value` in percentage of the maximum line speed (set by user).

```text
api?mode=config&name=speedlimit&value=30
```text

It can also be followed by `K,M` to define speedlimit in `KB/s,MB/s`, respectively.

```text
api?mode=config&name=speedlimit&value=400K
```text

## Action on queue complete

Set an end-of-queue action.

```text
api?mode=queue&name=change_complete_action&value=ACTION
```text

Options:

- `hibernate_pc`
- `standby_pc`
- `shutdown_program`
- Script: prefix the name of the script with `script_`, for example `script_test.py`

On some systems additional packages are required to allow SABnzbd to control power states, if there are problems in queue it will show as `power_options=false`.

## Sort the queue

Sort the queue by `avg_age`, `name`, `remaining` (Sort by % downloaded) or `size` in `asc` (low to high) or `desc` (high to low) order.

```text
api?mode=queue&name=sort&sort=avg_age&dir=desc
```text

## Add NZB by URL

Add NZB using an URL that needs to be accessible by SABnzbd, so make sure to include authentication information if the Indexer requires it. Example of a full request with everything set to default values is shown below, but only the `name` parameter is required.

```text
api?mode=addurl&name=https%3A%2F%indexer.info%2Fget.php%3Fguid%3Ded731c0b37f25f84aea563d6ddb210b1%26api%3D6f235b80fab0c76e1ce7da21b2c6c48c&nzbname=&cat=*&script=Default&priority=-100&pp=-1
```text

Returns the `nzo_id` of the job:

```json
{
    "status": true,
    "nzo_ids": ["SABnzbd_nzo_kyt1f0"]
}
```text

| Input parameter | Description |
|-----------------|-------------|
| `name` | URL-encoded version of the link to the NZB to be fetched |
| `nzbname` optional | Name of the job, if empty the NZB filename is used |
| `password` optional | Password to use when unpacking the job |
| `cat` optional | Category to be assigned, `*` means `Default`. List of available categories can be retrieved from get_cats |
| `script` optional | Script to be assigned, `Default` will use the script assigned to the category. List of available scripts can be retrieved from get_scripts |
| `priority` optional | Priority to be assigned |

Priority values:
- `-100` = Default Priority (of category)
- `-3` = Duplicate
- `-2` = Paused
- `-1` = Low Priority
- `0` = Normal Priority
- `1` = High Priority
- `2` = Force

| Input parameter | Description |
|-----------------|-------------|
| `pp` optional | Post-processing options |

Post-processing options:
- `-1` = Default (of category)
- `0` = None
- `1` = +Repair
- `2` = +Repair/Unpack
- `3` = +Repair/Unpack/Delete

## Add NZB by file upload

Upload NZB using `POST multipart/form-data`. In your form, set the value of the field `mode` to `addfile`; the file data should be in the field `name` or the field `nzbfile`.

For other parameters and output see addurl.

## Add NZB by local file path

Upload NZB from a location on the file system that SABnzbd can access. The path should be URL-encoded.

For other parameters and output see addurl.

Example of adding a file `E:\Downloads\Movie.BRRip.x264.1080p-NPW.nzb`:

```text
api?mode=addlocalfile&name=E%3A%5CDownloads%5CMovie.BRRip.x264.1080p-NPW.nzb&nzbname=The.Job.Name&cat=*&script=Default&priority=-100&pp=-1
```text

## Pause single job

Pause a single job based on its `nzo_id`. Returns a boolean status, and a list of affected nzo_ids.

```text
api?mode=queue&name=pause&value=NZO_ID
```text

## Resume single job

Resume a single job based on its `nzo_id`. Returns a boolean status, and a list of affected nzo_ids.

```text
api?mode=queue&name=resume&value=NZO_ID
```text

## Delete jobs

Delete job(s) based on `nzo_id`. Returns a boolean status, and a list of affected nzo_ids.

NOTE: By default already download files of a job are not removed, add `del_files=1` to have all files removed.

```text
api?mode=queue&name=delete&value=NZO_ID
```text

Deleting multiple items:

```text
api?mode=queue&name=delete&value=NZO_ID_1,NZO_ID_2,NZO_ID_3
```text

Deleting all items:

```text
api?mode=queue&name=delete&value=all&del_files=1
```text

## Purge queue

Remove all jobs from the queue, or only the ones matching `search`. Returns `nzb_id` of the jobs removed.

```text
api?mode=queue&name=purge&search=SEARCH&del_files=1
```text

NOTE: By default already download files of a job are not removed, add `del_files=1` to have all files removed.

## Move job in queue

Job's can be switched by providing 2 `nzo_id`, `value` is the item you want to move, `value2` is the name of the job where you want to put `value` one above, shifting job `value2` down.

```text
api?mode=switch&value=NZO_ID_1&value2=NZO_ID_2
```text

You can also move to a specific location in the queue, where `0` is the top of the queue:

```text
api?mode=switch&value=NZO_ID&value2=2
```text

Both commands will return the new position and priority, since a job's location is also dependent on its priority:

```json
{
    "result": {
        "priority": 0,
        "position": 2
    }
}
```text

## Change job category

Change category of job with `nzo_id`. List of available categories can be retrieved from get_cats.

```text
api?mode=change_cat&value=NZO_ID&value2=Category
```text

## Change job script

Change script of job with `nzo_id`. List of available scripts can be retrieved from get_scripts.

```text
api?mode=change_script&value=NZO_ID&value2=script.py
```text

## Change job priority

Change priority of job with `nzo_id`.

Priority values:
- `-100` = Default Priority (of category)
- `-4` = Stop
- `-3` = Duplicate
- `-2` = Paused
- `-1` = Low Priority
- `0` = Normal Priority
- `1` = High Priority
- `2` = Force

```text
api?mode=queue&name=priority&value=NZO_ID&value2=0
```text

The command will return the new position, since a job's location also depends on its priority:

```json
{
    "position": 42
}
```text

## Change job post-processing options

Change post-processing of job with `nzo_id`.

Post-processing options:
- `0` = None
- `1` = +Repair
- `2` = +Repair/Unpack
- `3` = +Repair/Unpack/Delete

```text
api?mode=change_opts&value=NZO_ID&value2=0
```text

## Change job name

Change name and password of job with `nzo_id`.

NOTE: `value3` can be empty, but to set a password `value` and `value2` must also be filled, using the current name.

```text
api?mode=queue&name=rename&value=NZO_ID&value2=NEW_NAME&value3=PASSWORD
```text

Or you can set a password as part of the new name in `value2`, see: RAR with password.

```text
api?mode=queue&name=rename&value=NZO_ID&value2=NEW_NAME{{PASSWORD}}
```text

## Get files in job

Get files of job with `nzo_id`.

```text
api?mode=get_files&value=NZO_ID
```text

The `status` indicates if a file was `finished`, in the process of being downloaded (`active`) or will only be downloaded when necessary (`queued`, like `.par2` files). The `set` shows to which part of the download the `.par2` files belong to, in case of multiple sets in 1 job. Files are sorted in order: finished, active, queued.

```json
{
    "files": [
        {
            "status": "finished",
            "mbleft": "0.00",
            "mb": "0.05",
            "age": "25d",
            "bytes": "52161.00",
            "filename": "93a4ec7c37752640deab48dabb46b164.par2",
            "nzf_id": "SABnzbd_nzf_1lk0ij"
        }
    ]
}
```text

## Move file(s) inside a job

Move files specified by `nzf_ids` inside job `nzo_id` to `top` or `bottom`. To move a file a `size` number of spots, use `up` or `down`.

```text
api?mode=move_nzf_bulk&name=LOCATION&value=NZO_ID&nzf_ids=NZF_ID,NZF_ID2&size=X
```text

## Remove file(s) from a job

Remove file(s) using `nzo_id` of the job and `nzf_id` of the file(s). Returns the `nzf_ids` of removed file.

```text
api?mode=queue&name=delete_nzf&value=NZO_ID&value2=NZF_ID,NZF_ID2
```text

---

# History functions

| Function | Description |
|----------|-------------|
| history | Full history output |
| retry | Retry failed job |
| retry_all | Retry all failed jobs |
| delete | Delete/Archive history item |
| mark_as_completed | Mark failed job as completed |

## History output

Full history output with details about all jobs. The `queue` and the `history` output share many common fields, but the history also contains statistics about how much has been downloaded in the past day, week, month and total.

```text
api?mode=history&start=START&limit=LIMIT&cat=CATEGORY&search=SEARCH&nzo_ids=NZO_ID_1,NZO_ID_2,NZO_ID_3&failed_only=0
```text

NOTE: Some of the less obvious output parameters are described below.

| Input parameter | Description |
|-----------------|-------------|
| `start` optional | Index of job to start at |
| `limit` optional | Number of jobs to display |
| `archive` optional | Display history (default) or archived items |
| `search` optional | Filter job names by `search` term |
| `category` / `cat` optional | Only return jobs with the specified category or categories (separated by a comma). Use `*` for Default |
| `status` optional | Only return jobs with the specified status or statuses (separated by a comma) |

Status values:
- `Completed`
- `Failed`
- `Queued` = Waiting for post-processing
- `QuickCheck`
- `Verifying`
- `Repairing`
- `Fetching` = Job is downloading extra par2 files
- `Extracting`
- `Moving`
- `Running` = Post-processing script is running

| Input parameter | Description |
|-----------------|-------------|
| `nzo_ids` optional | Only return jobs with these `nzo_ids` (separated by a comma) |
| `failed_only` optional | Only show failed jobs (shorthand for `status=Failed`) |
| `last_history_update` optional | Only return full output if anything has changed since `last_history_update`, the last update is given by a previous call to `history` |

| Output parameter | Description |
|------------------|-------------|
| `time_added` | Unix timestamp when the job was added to the queue |
| `duplicate_key` | How SABnzbd identified the show and season/episode info |
| `pp` | Different format than the queue: `R` = +Repair, `U` = +Repair/Unpack, `D` = +Repair/Unpack/Delete |
| `path` | Temporary destination |
| `storage` | Final destination |
| `loaded` | If `true`, item is post-processing |

Example output:

```json
{
    "history": {
        "noofslots": 220,
        "ppslots": 1,
        "day_size": "1.9 G",
        "week_size": "30.4 G",
        "month_size": "167.3 G",
        "total_size": "678.1 G",
        "last_history_update": 1469210913
    }
}
```text

## Retry history item

Retry history item(s) based on `nzo_id`. Optionally provide a `password` and an additional NZB as `POST multipart/form-data` in the `nzbfile` field.

NOTE: Pay attention to the different variable names used here: `value` and `nzbfile`.

```text
api?mode=retry&value=NZO_ID&password=password
```text

## Retry all history items

Will retry all failed jobs in the history. However, you are not able to supply passwords or extra NZB's.

```text
api?mode=retry_all
```text

## Delete/Archive history items

Delete or archive history item(s) based on `nzo_id`.

NOTE: By default files of failed jobs are not removed, add `del_files=1` to also have them removed.

NOTE: By default items are moved to the Archive, add `archive=0` to completely remove them.

```text
api?mode=history&name=delete&value=NZO_ID
```text

Deleting multiple items (skipping Archive):

```text
api?mode=history&name=delete&archive=0&value=NZO_ID_1,NZO_ID_2,NZO_ID_3
```text

Deleting all items:

```text
api?mode=history&name=delete&value=all
```text

Deleting all failed items:

```text
api?mode=history&name=delete&value=failed
```text

## Mark failed job as completed

Mark a failed history item as completed based on `nzo_id`. This is useful when you want to manually mark a failed job as completed without having to delete it from history.

NOTE: This will automatically remove any incomplete download files associated with the job and update the job status to "Completed".

```text
api?mode=history&name=mark_as_completed&value=NZO_ID
```text

Marking multiple items as completed:

```text
api?mode=history&name=mark_as_completed&value=NZO_ID_1,NZO_ID_2,NZO_ID_3
```text

---

# Status functions

NOTE: Added in 3.4.0, older versions only have fullstatus.

| Function | Description |
|----------|-------------|
| status / fullstatus | All status information |
| unblock_server | Unblock server |
| delete_orphan | Delete orphaned job |
| `mode=status` `name=delete_all_orphan` | Delete all orphaned jobs |
| add_orphan | Retry orphaned job |
| `mode=status` `name=add_all_orphan` | Retry all orphaned jobs |

## Status information

Get all status information available from SABnzbd. Below are only the values that are different from calls to `queue`. NOTE: Getting the public IPv4 address might take some time, so it can be skipped by setting `skip_dashboard=1`. To calculate performance measures, add `calculate_performance=1`.

```text
api?mode=status&skip_dashboard=0
```text

NOTE: Some of the less obvious output parameters are described below.

| Output parameter | Description |
|------------------|-------------|
| `darwin` | `true` when OS running SABnzbd is macOS |
| `nt` | `true` when OS running SABnzbd is Windows |
| `folders` | The orphaned job folder left in the Incomplete folder. Orphaned jobs can only be removed from a skin, not through the API |
| `pystone` | Indication of CPU speed, see Highspeed Downloading |
| `loadavg` | On Linux this will contain a string with information about system load |

Example output:

```json
{
    "status": {
        "localipv4": "192.168.0.1",
        "ipv6": null,
        "publicipv4": "46.00.00.103",
        "dnslookup": "OK"
    }
}
```text

## Unblock server

Unblock server based on `servername` from the status.

```text
api?mode=status&name=unblock_server&value=SERVERNAME
```text

## Delete orphaned job

Delete orphaned job based on the folder name from the status. Make sure that you URL-encode the folder name.

```text
api?mode=status&name=delete_orphan&value=FOLDERNAME
```text

## Retry orphaned job

Retry orphaned job based on the folder name from the status. Make sure that you URL-encode the folder name.

```text
api?mode=status&name=add_orphan&value=FOLDERNAME
```text

---

# Other functions

NOTE: Other functions are listed below, some straightforward commands are described only in this table and can simply be activated by calling:

```text
api?mode=FUNCTION
```text

| Function | Description |
|----------|-------------|
| `version` | Get version of running SABnzbd |
| `auth` | Get authentication methods available for interaction with the API |
| warnings | Get all active warnings |
| warnings clear | Clear all active warnings |
| get_cats | Get all categories |
| get_scripts | Get all scripts |
| server_stats | Get download statistics |
| showlog | Get the anonymized log file |
| del_config | Delete a configuration item within the "servers", "rss", "categories", or "sorters" sections |
| get_config | Get value of configuration item |
| set_config | Set configuration item to value |
| set_config_default | Reset config item to default value |
| `shutdown` | Shutdown SABnzbd |
| `restart` | Restart SABnzbd |
| `restart_repair` | Restart SABnzbd and perform a queue repair |
| `pause_pp` | Pause post-processing queue |
| `resume_pp` | Resume post-processing queue |
| `rss_now` | Fetch and process all RSS feeds |
| `watched_now` | Scan Watched Folder now |
| `reset_quota` | Reset the user defined quota to 0 |
| `mode=config` `name=set_apikey` | Reset the API key, returns the new key |
| `mode=config` `name=set_nzbkey` | Reset the NZB key, returns the new key |
| `mode=config` `name=regenerate_certs` | Regenerate the self-signed certificate for HTTPS connection to interface, requires SABnzbd restart to take effect |
| translate | Translate a text to user's locale |

## Get all categories

```text
api?mode=get_cats
```text

```json
{
    "categories": [
        "*",
        "movies",
        "series",
        "tv"
    ]
}
```text

## Get all scripts

```text
api?mode=get_scripts
```text

```json
{
    "scripts": [
        "None",
        "Notify.py",
        "sabnzbd-notify.py"
    ]
}
```text

## Download statistics

Return download statistics in bytes, total and per-server.

```text
api?mode=server_stats
```text

```json
{
    "day": 2352634799,
    "week": 32934490677,
    "month": 179983557488,
    "total": 728426161290,
    "servers": {
        "eunews.server.com": {
            "week": 19783288936,
            "total": 163741252273,
            "day": 2352634799,
            "month": 90478917031
        }
    }
}
```text

## Get the anonymized log file

The log file is automatically anonymized and a copy of the `sabnzbd.ini` is attached.

NOTE: This call ignores the `output` parameter, it will always serve the file as a download.

```text
api?mode=showlog
```text

## Delete a configuration item within the "servers", "rss", "categories", or "sorters" sections

Used to delete an entry from the limited sections.

Example of deleting a `servers` by keyword:

```text
api?mode=del_config&section=servers&keyword=ServerName
```text

Example of deleting a `rss` by keyword:

```text
api?mode=del_config&section=rss&keyword=Feed1
```text

Example of deleting a `categories` by keyword:

```text
api?mode=del_config&section=categories&keyword=audio
```text

If you attempt to delete the default category `*` from the `categories` section, the system will replace the default categories.

```text
api?mode=del_config&section=categories&keyword=*
```text

## Get config item(s)

You can read the whole configuration, a sub-set or a single setting.

NOTE: You will never receive passwords, each character will be replaced by `***` characters. You can set new passwords through the set_config call.

```text
api?mode=get_config
```text

All elements in `misc` section:

```text
api?mode=get_config&section=misc
```text

Example of filtering the server settings by keyword:

```text
api?mode=get_config&section=servers&keyword=ServerName
```text

## Set config item

In order to change a setting, you need to provide the `section` and `keyword` of the setting:

```text
api?mode=set_config&section=SECTION&keyword=KEYWORD&value=VALUE
```text

Returns the new setting when saved successfully.

For example, changing the Cleanup-list to `.sfv,.nzb,.nfo,.ext` would look like this:

```text
api?mode=set_config&section=misc&keyword=cleanup_list&value=.sfv,.nzb,.nfo,.ext
```text

## Setting server, RSS feed, category, or sorter settings

Changing settings for these sections is a bit different and requires one to specify the correct `name` of the server, RSS feed, category, or sorter. This `name` you can find in between double square brackets in the relevant section of your `sabnzbd.ini`, where it will for example say `[[news.newshosting.com]]` within the `[servers]` section, or `[[Feed1]]` in the `[rss]` section, and so on. Below the name you can see all variables you could set via the API for an item in that section. If the specified `name` doesn't match an existing one in the given section, it will be added there as a new item.

Server example:

```text
api?mode=set_config&section=servers&name=SERVER_NAME&username=VALUE_1&connections=VALUE_2
```text

Category example:

```text
api?mode=set_config&section=categories&name=CATEGORY_NAME&dir=CATEGORY_DIR
```text

RSS feed example:

```text
api?mode=set_config&section=rss&name=FEED_NAME&enable=VALUE_1&pp=VALUE_2
```text

Sorter example:

```text
api?mode=set_config&section=sorters&name=SORTER_NAME&sort_string=VALUE_1&sort_cats=VALUE_2&sort_type=VALUE_3
```text

## Reset config item to default value

NOTE: Currently only for settings in the `misc` section of the config. Can accept multiple keywords to reset.

```text
api?mode=set_config_default&keyword=SETTING_1&keyword=SETTING_2
```text

## Get all active warnings

```text
api?mode=warnings
```text

```json
{
    "warnings": [
        {
            "text": "API key missing, please enter the API key from Config->General into your 3rd party program",
            "type": "WARNING",
            "time": 1505153489
        }
    ]
}
```text

## Clear all active warnings

```text
api?mode=warnings&name=clear
```text

## Translate a text

Translate any text known to SABnzbd from English to the locale setting of the user.

```text
api?mode=translate&value=Watched%20Folder
```text

Will return for Dutch:

```json
{
    "value": "Bewaakte map"
}
```text
