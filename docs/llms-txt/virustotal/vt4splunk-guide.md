# Source: https://virustotal.readme.io/docs/vt4splunk-guide.md

# VT4Splunk, official VirusTotal app for Splunk

Configuration and use guide

## Overview

VT4Splunk automatically enriches your Splunk logs with threat intelligence coming from VirusTotal. It allows you to contextualize IoCs (files/hashes, domains, IP addresses, URLs) and confirm malicious intent/discard false positives. The context added includes: security industry reputation, severity, threat categories and labels, associated campaigns and threat actors, etc.

## Compatibility Matrix

* Unix OS
* Splunk version: 9.2.x, 9.1.x, 9.0.x
* Python version: Python3

## Installation

VT4Splunk app can be installed through UI as is shown below:

1. Log in to Splunk Web and navigate to Apps > Manage Apps.
2. Click `Install app from file`.
3. Click `Choose file` and select the `TA-virustotal-app` installation file.
4. Click on `Upload`.
5. Restart Splunk.

By the limitations of Splunk at the time of reading VT API key from indexers **VT4Splunk app will always run on the Search Head** so the add-on it only needs to be installed on the Search Head as usual, not on the indexers nor in the forwarders.

## Configuration

Configuring VT4Splunk:

### Proxy

Configure proxy settings:

|                |           |                                |
| -------------- | --------- | ------------------------------ |
| Enable Proxy   | Optional  | To enable or disable the proxy |
| Proxy Host     | Mandatory | Host or IP of the proxy server |
| Proxy Port     | Mandatory | Port for proxy server          |
| Proxy Username | Optional  | Username of the proxy server   |
| Proxy Password | Optional  | Password of the proxy server   |

### Logging

Configure the Logging level:

1. Navigate to the `Configuration` tab.
2. Click on the `Logging` tab.
3. Select the log level click on `Save`.

### General Settings

Configure basic values for the correct operation of the app:

* `VirusTotal API Key`:
  Your API key can be found at <https://www.virustotal.com/gui/my-apikey> (sign in required). As a premium user you can also generate service accounts in your group profile.

To test the connection you can execute this Splunk query after save the API key

```
| makeresults
| eval testip="8.8.8.8"
| vt4splunk ip=testip
```

* `Lookup table expiration (days)`:
  Elements stored in the lookup tables (iocs, campaigns, actors) will be removed when the last time they are seen in the events exceeds this value.

### Correlation Settings

Configure values which will affect to the automatic correlation and the data shown in the dashboards:

* `Enable automatic correlation`:
  Enable this to automatically correlate IoCs found in your events with VirusTotal context. VirusTotal enrichment will be scheduled every 30 minutes and findings will be summarized in the dashboards.

* `Data freshness (days)`:
  Optimizes your VirusTotal API quota. IoC enrichment will be retrieved from the local cache, instead of performing an API call, whenever the cached analysis' age is lower than this value.

* `Names for indexes`:
  Automatic correlation and dashboards will use this list of indexes to perform the search of the events in your catalog.

* `Fields names [Hash, URL, Domain, IP]`:
  Saved searches will perform automatic correlation using these field names to find IoCs in your events. Empty field disables that automatic correlation specifically.

## Commands

The app provides a main command `vt4splunk` to correlate IoCs found in your events with the VirusTotal information, also provides other commands to keep up-to-date the enrichment dataset:

* `vt4splunk`:

Adding the command to a SPL query will enrich events which contains the fieldname passed as argument, adding new fields to the event in search time with the prefix `vt_`, the command admits the following parameters:

| Parameter                   | Optional | Description                              |
| --------------------------- | -------- | ---------------------------------------- |
| hash \| domain \| url \| ip | No       | event fieldname                          |
| nocache                     | Yes      | Boolean lowercase value \[true \| false] |

Query examples:

```
sourcetype=access_* status=400 method=POST
| vt4splunk ip=clientip
```

Correlate `clientip` field of access log events.

```
sourcetype=access_* status=400 method=POST
| vt4splunk ip=clientip nocache=true
```

Forcing to get the enrichment data from VirusTotal instead of the lookup tables.

```
sourcetype=access_* status=400 method=POST
| vt4splunk ip=clientip nocache=true
| search vt_detections > 10
```

Get correlated events where detections are more than ten.

### Additional commands

The following additional commands are executed periodically by the saved searches, it rarely will be necessary to execute manually.

* `vtdeleteiocs`:

Delete IoCs older than 30 days by default. It can be also executed manually given a table with `vt_id` field as input and/or with some parameter to perform a more selective delete:

| Parameter | Optional | Description                                           |
| --------- | -------- | ----------------------------------------------------- |
| lookups   | Yes      | delete iocs of specific types (hash, domain, ip, url) |
| ttl       | Yes      | delete iocs older than this value (days)              |

Query examples:

```
| makeresults | vtdeleteiocs
```

Delete all IoCs.

```
| makeresults | vtdeleteiocs ttl=30
```

Delete all IoCs older than 30 days.

```
| inputlookup vt_url_cache | search vt_detections < 10 | vtdeleteiocs lookups=url ttl=5
```

Delete URLs with less than 10 detections and older than 5 days.

```
| inputlookup vt_file_cache | search vt_tags=*cve-* | vtdeleteiocs lookups=hash
```

Delete hashes with CVE tags.

* `vtadversaryupdate`:

Keep up-to-date campaigns and threat actors.

* `vtvulnerabilitiesupdate`:

Keep up-to-date CVEs.

* `vtmitreupdate`:

Extract MITRE information of each hash and keep up-to-date the dashboard.

## Saved Searches

The app comes with several saved search which will correlated your events and will keep up-to-date the data in an unmanaged way:

* `VirusTotal Update File Lookup`
* `VirusTotal Update URL Lookup`
* `VirusTotal Update Domain Lookup`
* `VirusTotal Update IP Lookup`

The above saved searches are in charge of the automatic correlation, they will inspect new events in the last 30 minutes contained only in the indexes configured in the **Correlation Settings**.

* `VirusTotal Clean Lookups`

This saved search will remove IoCs from the lookup tables older than the value configured in the **Correlation Settings**, by default 30 days.

* `VirusTotal Keep Adversary Lookups Updated`
* `VirusTotal Keep CVE Lookup Updated`
* `VirusTotal Keep MITRE Lookup Updated`

The above saved searches keep up-to-date the data shown in the Vulnerability, Adversary and MITRE dashboards.

## Lookup tables

The app creates several lookup tables to store the enrichment data and to feed the dashboards:

* `vt_file_cache`: store the VirusTotal enrichment data for files
* `vt_domain_cache`: store the VirusTotal enrichment data for domains
* `vt_url_cache`: store the VirusTotal enrichment data for urls
* `vt_ip_cache`: store the VirusTotal enrichment data for ips
* `vt_collection_cache`: store the VirusTotal collections for flagged iocs (Campaigns and malware toolkits)
* `vt_threat_actor_cache`: store the VirusTotal threat actors for flagged iocs
* `vt_cve_cache`: store the CVEs extracted from file enrichment data
* `vt_mitre_cache`: store the MITRE information for files
* `vt_ignore_cache`: store the IoCs to be ignored in the dashboards

All of the above tables can be inspected running a search query like this: `| inputlookup vt_file_cache`.

### Ignoring specific IoCs

IoCs can be ignored adding them to a specific lookup table, preventing them from appearing in the dashboards, this can be useful if you have a well-known or false positives IoCs.

You can manage those IoCs with these queries:

* To add a single IoC:

```
| makeresults | eval vt_id="eed999fcf63eaa5dd73fac49a7d49d64fe19b945eb30730da4ab026d78746559", vt_type="hash"
| outputlookup append=true vt_ignore_cache
```

* To add multiple IoCs:

```
| makeresults format=csv data="vt_id, vt_type
eed999fcf63eaa5dd73fac49a7d49d64fe19b945eb30730da4ab026d78746559,hash
google.com,domain
https://www.google.com,url
127.0.0.1,ip"
| outputlookup append=true vt_ignore_cache
```

* To remove duplicate IoCs:

```
| inputlookup vt_ignore_cache | dedup vt_id vt_type | outputlookup vt_ignore_cache
```

## Troubleshooting

### Empty dashboards

* Saved searches only correlate events created in the last 30 minutes, if you want to do a backfill to start showing data perform a search adding the command **vt4splunk** as described above.

* Check lookup tables have information, if not try to execute the `vt4splunk` command manually over a search of events.

* Check the index names in the **Correlation Settings**.

## Release Notes

### Version 1.6.5

* Cloud compatibility

### Version 1.6.4

* Fixed bug when detecting if Splunk REST uses SSL or not.
* New unknown pivot en Severity pie chart.
* Fix empty values in pie charts.
* Upgrade Add-on builder version to 4.2.0.

### Version 1.6.3

* Added HTTPS proxy support.
* Added JARM information to IP addresses and domains.

### Version 1.6.2

* Improve saved searches performance.
* Disable saved searches by default.
* Improve fields validation to avoid inconsistent states.

### Upgrade from all versions

* We have changed the way the add-on stores some configuration values like the `Lookup table expiration`, `Index names` and the `Enable automatic correlation`. Values stored before the upgrade will not work as expected, please, after the upgrade, enter again the configuration in the General and Correlation Settings and save both forms.

### Version 1.6.1

* Run `vt4splunk` command locally.
* Fix compatibility with Splunk 9.1.\*.
* Added the IoC severity for VT Enterprise users.
* Fix bug when lists in Correlation Settings contained spaces.
* Added whois information to domains.

### Version 1.6.0

* Allow users to run `vt4splunk` command locally.
* Added VPN, Tor and Proxy IPs tab in Threat Intelligence dashboard.
* Added the number of VT comments on each IoC.
* Added the number of Crowdsource Yara rules matches to file IoCs.
* Avoid to enrich private IP addresses.
* `vtdeleteiocs` command is able to receive IoCs as input.
* Improved window time selector by allowing any relative time.
* Fix bug in hashes tables when displaying SHA256 instead of ID.
* Fix bug where the Configuration tab didn't open in some cases.

### Version 1.5.3

* Fix bug when `vt4splunk` command process records with non utf-8 encoding.

### Version 1.5.2

* Fix bug when checking the API key.

### Version 1.5.1

* Added `vt_ignore_cache` to ignore desired IoCs.
* Fix bug when using proxy with username and password.
* Fix bug in Vulnerability Intelligence dashboard when using the time window selector.

### Version 1.5.0

* Added signature severity to MITRE ATT\&CK techniques in Adversary Intelligence dashboard.
* Added a control to filter by signature severity to MITRE ATT\&CK techniques in Adversary Intelligence dashboard.
* Change flagged files by extension chart to by type in Threat Intelligence dashboard.
* Clicking on cards works as clicking on tabs in Threat and Adversary Intelligence dashboards.
* Fix a bug in MITRE ATT\&CK dashboard when number of files with MITRE ATT\&CK techniques was greater than 100.
* Change workflow action endpoint for URLs.
* Fix bug when using saved searches in distributed environment.
* Fix cloud compatibility.

### Upgrade from 1.4.\* versions

* Delete content of the MITRE lookup table to make it compatible with the new version:

```
| outputlookup vt_mitre_cache
```

### Version 1.4.1

* Fix cloud compatibility.

### Version 1.4.0

* Added a brand new MITRE ATT\&CK matrix dashboard.
* Added a new command `vtmitreupdate` to extract tactics and techniques from IoCs.
* Added a new attack techniques and sub-techniques table to the Adversary dashboard.
* Added a saved search to keep up-to-date the MITRE data.
* Added a validator to the API key field to avoid enter by mistake an invalid value.
* Improve errors feedback, no quota, API key not set or other errors are now displayed in all dashboards.
* Improve the support on distributed installations, now the app and config are replicated across the search head cluster.
* Improve logging, app logs can now be read at $SPLUNK\_HOME/var/log/splunk/ta\_virustotal*app*\*.log.
* Now automatic correlation can be disabled per IoC type, leaving the input of the field names empty.
* Now saved searches don't run if there is not a valid API key configured.
* Fix the vt4splunk command search error `_last_correlation_date`.
* Fix the vt4splunk command search error `vt_tags`.
* Fix workflow action error for URLs.

### Version 1.3.0

* Added a new Adversary Intelligence dashboard.
* Added a new command `vtdeleteiocs` to delete iocs selectively.
* Added a new command `vtadversaryupdate` to gather adversary intelligence data from VirusTotal.
* Added a new command `vtvulnerabilitiesupdate` to extract vulnerabilities from the iocs.
* Added a saved search to delete iocs older than a configured value.
* Added a saved search to keep up-to-date the adversary intelligence data.
* Added a saved search to keep up-to-date the vulnerabilities data.
* Added a malware category pie chart (file) to the Threat Intelligence dashboard.
* Added a categories pie chart (urls, domains) to the Threat Intelligence dashboard.
* Added a country pie chart (ip) to the Threat Intelligence dashboard.
* Added a TLD pie chart (urls, domains) to the Threat Intelligence dashboard.
* Added a ASN pie chart (ip) to the Threat Intelligence dashboard.
* Added country flags.
* Improve quota errors feedback when `vt4splunk` is executed.
* Fix a bug when a non-valid IoC aborts the entire query.
* Breaking change: `vt_malicious` has been renamed to `vt_detections`.

### Upgrade from 1.2.0 version

* Delete content of the ioc lookup tables to make them compatible with the new version:

```
| outputlookup vt_file_cache
| outputlookup vt_domain_cache
| outputlookup vt_url_cache
| outputlookup vt_ip_cache
| outputlookup vt_cve_cache
```

### Version 1.2.0

* Added saved searches to automate the v4splunk enrichment.
* Added a malware category pie chart in the Threat Intelligence dashboard.
* Added a lookup date column in the Threat Intelligence dashboard.
* Fix bug where the VT Augment didn't open in some cases.

### Version 1.1.0

* Fix several dashboards errors.
* Fix proxy error when user and pass were missing.

### Version: 1.0.0

* Added a `vt4splunk` command to enrich events.
* Added a threat intelligence dashboard to show all malicious IoCs collected from your events.
* Added a dashboard to show all CVEs found in your events.
* Added a dashboard to monitor the consumption of the VT API quota.

## Support

* Email [contact@virustotal.com](contact@virustotal.com)

* When contacting to support, please indicate your VT4Splunk version, Splunk version, if Enterprise or Cloud, and some screenshots and logs by executing:

```
index="_internal" | search source="*ta_virustotal_app*"
```

To get all logs stored by VT4Splunk.

```
index="_internal" | search "virustotal" "ERROR"
```

To get all logs stored by Splunk about VT4splunk.

**Copyright (c) 2024 Google. All rights reserved.**