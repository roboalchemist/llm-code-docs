# Source: https://virustotal.readme.io/reference/file-behaviour-summary.md

# Files Behaviour

File behaviour reports

File behaviour reports are obtained either by using the [GET /files/{id}/behaviours](https://virustotal.readme.io/reference/files-relationships) endpoint or the [sandbox behavior feed](https://virustotal.readme.io/reference/feeds-file-behaviour) . They summarize the observed behaviour during the execution or opening of a file. Note that some of these actions could be triggered by children of the file under consideration.

## Object Attributes

In a file\_behaviour object you will find these attributes:

* `analysis_date`: <*integer*> Unix epoch UTC time (seconds).
* `behash`: <*string*> used to find similar behaviour analyses.
* `calls_highlighted`: <*list of strings*> API calls/Syscalls worth highlighting.
* `command_executions`: <*list of strings*> shell command executions observed during the analysis of the given file.
* `files_opened`: <*list of strings*>  files opened during execution.
* `files_written`: <*list of strings*>   files written to during execution.
* `files_deleted`  <*list of strings*> names of the files deleted.
* `files_attribute_changed`: <*list of strings*> full path of files subject to some sort of active attribute modification.
* `has_html_report`: <boolean> whether there is an HTML report for this behaviour analysis.
* `has_evtx`: <boolean> whether there is a EVTX file for this behaviour analysis. Check out [/file\_behaviours/{sandbox_id}/evtx](https://virustotal.readme.io/reference/get-file-behaviours-evtx) for more information.
* `has_memdump`: <boolean> whether there is a memdump file for this behaviour analysis. Check out [/file\_behaviours/{sandbox_id}/memdump](https://virustotal.readme.io/reference/get-file-behaviours-memdump).
* `has_pcap`: <boolean> whether there is a PCAP network capture for this behaviour analysis. Check out [/file\_behaviours/{sandbox_id}/pcap](https://virustotal.readme.io/reference/get-file-behaviours-pcap) for more information.
* `hosts_file`: <*string*> the hosts file field stores the content of the local hostname-ip mapping  hosts file IF AND ONLY IF the file was modified, else this field is not  populated.
* `ids_alerts`: <*list of dictionaries*> list of IDS alerts, sorted by timestamp. Every item contains the following keys:
  * `alert_context`: <*dictionary*> matched alert context:
    * `dest_ip`: <*string*> destination IP.
    * `dest_port`: <*integer*> destination port.
    * `hostname`: <*string*> if the alert is related to an HTTP communication, destination hostname.
    * `protocol`: <*string*> communication protocol name.
    * `src_ip`: <*string*> source IP.
    * `src_port`: <*integer*> source port.
    * `url`: <*string*> if the alert is related to an HTTP communication, destination URL.
  * `alert_severity`: <*string*> one of `high`, `medium`, `low` or `info`.
  * `rule_category`: <*string*> alert category.
  * `rule_id`: <*string*> rule SID.
  * `rule_msg`: <*string*> alert description.
  * `rule_source`: <*string*> rule source, determined by SID range.
* `processes_terminated`: <*list of strings*> name of the processes that were terminated during the execution of a given file.
* `processes_killed`: <*list of strings*> name of the processes that were killed during the execution of a given file.
* `processes_injected`: <*list of strings*> name of the processes that were subjected to some kind of code injection during the execution of the given file.
* `services_opened`: <*list of strings*> names of the services for which a handle was acquired during the analysis of the given file.
* `services_created`: <*list of strings*> new services created.
* `services_started`: <*list of strings*>  new services started.
* `services_stopped`: <*list of strings*> services stopped during the execution of the given file.
* `services_deleted`: <*list of strings*> services deleted during the execution of the given file.
* `services_bound`: <*list of strings*> service binding, mainly in Android, see: <https://developer.android.com/guide/components/bound-services.html>.
* `windows_searched`: <*list of strings*> names of windows that are searched for.
* `windows_hidden`: <*list of strings*>  names of windows that are set up to be invisible.
* `mutexes_opened`: <*list of strings*> name of the mutexes for which the file acquires a handle.
* `mutexes_created`: <*list of strings*> new mutexes created.
* `signals_observed`: <*list of strings*> OS Signals and broadcast events, note that Android broadcasts are categorized here also.
* `invokes`: <*list of strings*> method/functionality called via reflection or some sort of runtime instantiation. The best example are Java reflection calls, in those cases we flatten the structure to a string: <class>.<method>.
* `crypto_algorithms_observed`: <*list of strings*> Example: RSA.
* `crypto_keys`: <*list of strings*> e.g. "MySecret".
* `crypto_plain_text`: <*list of strings*> strings that are either ciphered or deciphered during the observed time frame, we record just the plaintext.
* `text_decoded`: <*list of strings*> plaintext which is the result of a decoding operation.
* `text_highlighted`  <*list of strings*> interesting text seen in window dialogs, titles, etc.
* `verdict_confidence`: <*integer*> 99 = 99% confident verdict is correct.
* `ja3_digests`: <*list of strings*> [JA3](https://github.com/salesforce/ja3) fingerprinting of TLS client connections.
* `tls`: <*list of dictionaries*> contacted domains/IPs certificates. Each entry contains the following fields:
  * `issuer`: <*dictionary*> certificate issuer information. Keys are certificate fields (C, CN, O, etc) as string and values are always string.
  * `ja3`: <*string*> certificate JA3.
  * `ja3s`: <*string*> certificate JA3s.
  * `serial_number`: <*string*> certificate serial number.
  * `sni`: <*string*> certificate's server name indication.
  * `subject`: <*dictionary*> certificate subject information. Same format as `issuer` field.
  * `thumbprint`: <*string*> certificate thumbprint.
  * `version`: <*string*> TLS version.
* `sigma_analysis_results`: <*list of dictionaries*> aggregated [sigma](https://github.com/SigmaHQ/sigma) analyses results from all sandbox generated EVTX files. Each item contains the following subfields:
  * `rule_title`: <*string*> matched sigma rule title.
  * `rule_source`: <*string*> sigma ruleset where this rule belongs to.
  * `match_context`: <*dictionary*> specific matched events. This dictionary contains the following key:
    * `values`: <*list of map\<str, str>>* all matched events represented as key-value.
  * `rule_level`: <*string*> rule level, can be either of "critical", "high", "medium", "low".
  * `rule_description`: <*string*> rule description
  * `rule_author`: <*string*> rule author
  * `rule_id`: <*string*> rule ID in VirusTotal. You can use this to find other files matching this same rule.
* `signature_matches`: <*list of dictionaries*>  aggregated list of matching signatures. Each item contains the following subfields:
  * `format`: <*string*> any of the following formats: SIG\_FORMAT\_UNKNOWN, SIG\_FORMAT\_YARA, SIG\_FORMAT\_SIGMA, SIG\_FORMAT\_CAPA or SIG\_FORMAT\_OPENIOC.
  * `authors`: <*dictionary*> list of authors.
  * `rule_src`: <*string*> rule source.
  * `name`: <*string*> rule name.
  * `description`: <*string*> rule description.
* `mitre_attack_techniques`: < \_list of dictionaries\_> aggregated list of mitre attack techniques. Each item contains the following subfields:
  * `signature_description`: <*string*> description.
  * `id`: <*string*> identifier.
  * `severity`: <*string*> severity.

Android specific fields:

* `activities_started`: <*list of strings*> Android activities launched by the app under study.
* `content_model_observers`: <*list of strings*> content for which an Android app registers logic to be informed about any changes to it.
* `content_model_sets`: <*list of dictionaries*> content model entries performed by an Android app.
* `databases_deleted`: <*list of strings*> e.g. Android SQLite DBs deleted.
* `databases_opened`: <*list of strings*> interactions with databases, e.g. when an Android app opens an SQLite DB.
* `permissions_requested`: <*list of strings*> Android permissions requested by the app during runtime. In Windows it should also record process token privilege modifications such as SE\_LOAD\_DRIVER\_PRIVILEGE.
* `shared_preferences_lookups`: <*list of strings*> entries in Android's shared preferences that are checked (<https://developer.android.com/reference/android/content/SharedPreferences.html>).
* `shared_preferences_sets`: <*list of dictionaries*> entries written in Android's shared preferences. Every subitem contains the following fields:
  * `key`: <*string*> preference name.
  * `value`: <*string*> set value.
* `signals_hooked`: <*list of strings*> registering a receiver in Android is considered as a broadcast hook. In windows this field will contain `SetWindowsHookExA` activity and the like.
* `system_property_lookups`: <*list of strings*> interactions with Android's system properties dataset (getInt, getString, putInt, putString, etc. all get simply translated into strings. android.os.SystemProperties.).
* `system_property_sets`: <*list of dictionaries*> keys and values set in Android's system properties dataset.

Windows specific fields:

* `modules_loaded`: <*list of strings*> operations related to dynamic loading of libraries, shared objects and components.
* `registry_keys_opened`: <*list of strings*> Windows registry keys for which a handle is acquired.
* `registry_keys_set`: <*list of dictionaries*> keys and values of registry keys that are set. It is a list of dictionaries, each one containing the following fields:
  * `key`: <*string*> modified registry key.
  * `value`: <*string*> value set to the registry key.
* `registry_keys_deleted`: <*list of strings*> names of Windows registry keys that are deleted.

```json File behaviour report
{
    "data": {
        "attributes": {
            "activities_started": [
                "<string>"
            ],
            "analysis_date": <int:timestamp>,
            "behash": "<string>",
            "calls_highlighted": [
                "<string>"
            ],
            "command_executions": [
                "<string>"
            ],
            "files_opened": [
                "<string>"
            ],
            "files_written": [
                "<string>"
            ],
            "has_html_report": <boolean>,
            "has_pcap": <boolean>,
            "ids_results": [  
              {
                "alert_context": {
                  "dest_ip": "<string>",
                  "dest_port": <int>,
                  "hostname": "<string>",
                  "protocol": "<string>",
                  "src_ip": "<string>",
                  "src_port": <int>,
                  "url": "<string>"
                },
                "alert_severity": "<string>",
                "rule_id": "<string>",
                "rule_msg": "<string>",
                "rule_source": "<string>"
              },
            ],
            "last_modification_date": <int:timestamp>,
            "modules_loaded": [
                "<string>"
            ],
            "mutexes_created": [
                "<string>"
            ],
            "mutexes_opened": [
                "<string>"
            ],
            "processes_created": [
                "<string>"
            ],
            "processes_terminated": [
                "<string>"
            ]
            "registry_keys_deleted": [
                "<string>"
            ],
            "registry_keys_opened": [
                "<string>"
            ],
            "registry_keys_set": [
                {
                    "key": "<string>",
                    "value": "<string>"
                }
            ],
            "sandbox_name": "<string>",
            "shared_preferences_sets": [
                {
                    "key": "<string>",
                    "value": "<string>"
                }
            ],
            "sigma_analysis_results": [{
              "rule_title": "<string>",
              "rule_source": "<string>",
              "match_context": [{
                "values": {
                  "<string>": "<string>"}}],
              "rule_level": "<string>",
              "rule_description": "<string>",
              "rule_author": "<string>",
              "rule_id": "<string>"
            }],
            "tags": [
                "<string>"
            ],
            "text_highlighted": [
                "<string>"
            ],
            "tls": [
                {
                    "issuer": {
                        "<string>": "<string>"
                    },
                    "ja3": "<string>",
                    "ja3s": "<string>",
                    "serial_number": "<string>",
                    "sni": "<string>",
                    "subject": {
                        "<string>": "<string>"
                    },
                    "thumbprint": "<string>",
                    "version": "<string>"
                }
            ],
            "verdicts": [
                "<string>"
            ]
        },
        "id": "<file_sha256>_<sandbox_name>",
        "links": {
            "self": "https://www.virustotal.com/api/v3/file_behaviours/<id>"
        },
        "type": "file_behaviour"
    }
}
```
```json Windows example
{
    "data": {
        "id": "f55fe457929044e4c4cdc62b4ad0a4955bd2faac2b642318649beede66086eb4_VirusTotal Jujubox",
        "type": "file_behaviour",
        "links": {
            "self": "https://www.virustotal.com/api/v3/file_behaviours/f55fe457929044e4c4cdc62b4ad0a4955bd2faac2b642318649beede66086eb4_VirusTotal Jujubox"
        },
        "attributes": {
            "has_evtx": false,
            "tags": [
                "DIRECT_CPU_CLOCK_ACCESS",
                "RUNTIME_MODULES"
            ],
            "files_written": [
                "c:\\users\\<USER>\\appdata\\local\\temp\\krkr_51755ecf6166_210437_2468\\3134adde34d7.dll"
            ],
            "last_modification_date": 1671811052,
            "calls_highlighted": [
                "GetTickCount"
            ],
            "sandbox_name": "VirusTotal Jujubox",
            "modules_loaded": [
                "ADVAPI32.dll",
                "C:\\Users\\<USER>\\Downloads\\hmaid.exe",
                "CRYPTSP.dll",
                "CRYPTBASE.dll"
            ],
            "has_html_report": true,
            "ip_traffic": [
                {
                    "transport_layer_protocol": "TCP",
                    "destination_ip": "209.197.3.8",
                    "destination_port": 80
                }
            ],
            "processes_tree": [
                {
                    "process_id": "2468",
                    "name": "hmaid.exe"
                }
            ],
            "registry_keys_opened": [
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontLink\\SystemLink",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\Disable",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\DataFilePath",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback\\Tahoma"
            ],
            "text_highlighted": [
                "Kirikiri",
                "Script exception raised\nCannot find storage file://./c/users/<USER>/downloads/data.xp3"
            ],
            "behash": "e77446099f5d2fe3278cd6613bc70a76",
            "has_memdump": false,
            "has_pcap": true,
 "files_opened": [
                "C:\\Windows\\system32\\tzres.dll",
                "C:\\Users\\<USER>\\Downloads\\hmaid.cf",
                "C:\\Users\\<USER>\\Documents",
                "C:\\Users\\<USER>\\AppData\\Roaming",
                "C:\\Users\\<USER>\\Saved Games",
                "C:\\Users\\<USER>\\Downloads\\savedata\\hmaid.cfu",
                "C:\\Users\\<USER>\\Downloads\\savedata",
                "C:\\Users\\<USER>\\Downloads",
                "C:\\Users\\<USER>\\AppData\\Local\\Temp\\krkr_51755ecf6166_210437_2468",
                "C:\\Users\\<USER>\\AppData\\Local\\Temp",
                "c:\\users\\<USER>\\appdata\\local\\temp\\krkr_51755ecf6166_210437_2468\\3134adde34d7.dll",
                "C:\\Windows\\system32\\CRYPTSP.dll",
                "C:\\Windows\\system32\\rsaenh.dll",
                "c:\\users\\<USER>\\downloads\\data.xp3",
                "c:\\users\\<USER>\\downloads\\savedata\\krkr.console.log",
                "C:\\Windows\\Fonts\\staticcache.dat",
                "C:\\Windows\\system32\\ole32.dll"
            ],
            "files_dropped": [
                {
                    "path": "c:\\users\\<USER>\\appdata\\local\\temp\\krkr_51755ecf6166_210437_2468\\3134adde34d7.dll",
                    "sha256": "4752a1781840cbb27557eaf48dd69fee02d4590df4ab63d4243bdf98cab419c9"
                }
            ],
            "analysis_date": 1671810990
        }
    }
}
```
```json Android example
{
    "data": {
        "id": "a877ae2826a67c90ee9b022542c53c6b25225906f72422fb1fb9a43903e04808_VirusTotal R2DBox",
        "type": "file_behaviour",
        "links": {
            "self": "https://www.virustotal.com/api/v3/file_behaviours/a877ae2826a67c90ee9b022542c53c6b25225906f72422fb1fb9a43903e04808_VirusTotal R2DBox"
        },
        "attributes": {
            "tags": [
                "OBFUSCATED",
                "REFLECTION"
            ],
            "has_pcap": false,
            "http_conversations": [
                {
                    "url": "https://assets.adobedtm.com/95c3e405673d/203501b7db77/launch-9a8e39d25589.json",
                    "request_method": "GET",
                    "response_headers": {
                        "X-Android-Sent-Millis": "1708992604680",
                        "X-Android-Selected-Protocol": "http/1.1",
                        "X-Android-Received-Millis": "1708992604733",
                        "X-Android-Response-Source": "NETWORK 200",
                        "Accept-Ranges": "bytes",
                        "Expires": "Tue, 27 Feb 2024 05:08:28 GMT",
                        "Vary": "Accept-Encoding",
                        "Server": "AkamaiNetStorage",
                        "Last-Modified": "Tue, 22 Nov 2022 11:03:37 GMT",
                        "Connection": "keep-alive",
                        "ETag": "\"3bf6be55e9f12f2fd6686382ebc78dd9:1669115017.570167\"",
                        "Cache-Control": "max-age=3600",
                        "Date": "Tue, 27 Feb 2024 04:08:28 GMT",
                        "null": "HTTP/1.1 200 OK",
                        "Content-Type": "application/json",
                        "Timing-Allow-Origin": "*"
                    },
                    "response_status_code": 200,
                    "request_headers": {
                        "Accept-Language": "en-US",
                        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; Standard PC (i440FX + PIIX, 1996) Build/OPM8.190605.003)"
                    }
                }
            ],
            "files_copied": [
                {
                    "source": "/data/user/0/com.bancomer.mbanking/files/PersistedInstallation3610913398658957513tmp",
                    "destination": "/data/user/0/com.bancomer.mbanking/files/PersistedInstallation.W0RFRkFVTFRd+MTozNDE0OTM3OTk5MDc6YW5kcm9pZDpkZTNiMGU4Y2NmY2ZlZTVk.json"
                },
                {
                    "source": "/data/user/0/com.bancomer.mbanking/shared_prefs/local.storage.irl.xml",
                    "destination": "/data/user/0/com.bancomer.mbanking/shared_prefs/local.storage.irl.xml.bak"
                }
            ],
            "has_html_report": true,
            "ip_traffic": [
                {
                    "transport_layer_protocol": "TCP",
                    "destination_ip": "23.62.164.244",
                    "destination_port": 443
                }
            ],
            "behash": "9e0453efbcd8556bd0ee5557677adf3f",
            "files_written": [
                "/data/user/0/com.bancomer.mbanking/no_backup/com.google.android.gms.appid-no-backup",
                "/data/user/0/com.bancomer.mbanking/files/PersistedInstallation3610913398658957513tmp",
                "/data/user/0/com.bancomer.mbanking/shared_prefs/com.google.android.gms.measurement.prefs.xml",
                "/data/user/0/com.bancomer.mbanking/shared_prefs/local.storage.irl.xml"
            ],
            "has_memdump": false,
            "sandbox_name": "VirusTotal R2DBox",
            "services_opened": [
                "user"
            ],
            "invokes": [
                "com.android.org.conscrypt.ConscryptFileDescriptorSocket.setUseSessionTickets",
                "com.android.org.conscrypt.ConscryptFileDescriptorSocket.setHostname",
                "com.android.org.conscrypt.ConscryptFileDescriptorSocket.getAlpnSelectedProtocol",
                "com.android.org.conscrypt.ConscryptFileDescriptorSocket.setAlpnProtocols",
                "sun.misc.Unsafe.getLong",
                "android.os.Trace.isTagEnabled",
                "libcore.io.Memory.pokeLong",
                "sun.misc.Unsafe.putLong",
                "sun.misc.Unsafe.arrayIndexScale",
                "sun.misc.Unsafe.objectFieldOffset",
                "com.android.org.conscrypt.OpenSSLSocketImpl.setHostname",
                "sun.misc.Unsafe.arrayBaseOffset",
                "com.android.org.conscrypt.OpenSSLSocketImpl.setAlpnProtocols",
                "dalvik.system.CloseGuard.open",
                "libcore.io.Memory.peekInt",
                "sun.misc.Unsafe.getInt",
                "libcore.io.Memory.peekLong",
                "sun.misc.Unsafe.putInt",
                "kotlin.reflect.jvm.internal.impl.builtins.PrimitiveType.values",
                "libcore.io.Memory.pokeByte",
                "libcore.io.Memory.peekByteArray",
                "com.android.org.conscrypt.OpenSSLSocketImpl.getAlpnSelectedProtocol",
                "libcore.io.Memory.pokeByteArray",
                "libcore.io.Memory.pokeInt",
                "sun.misc.Unsafe.getObject",
                "dalvik.system.CloseGuard.warnIfOpen",
                "android.security.net.config.RootTrustManager.checkServerTrusted",
                "dalvik.system.CloseGuard.get",
                "com.android.org.conscrypt.OpenSSLSocketImpl.setUseSessionTickets",
                "libcore.io.Memory.peekByte",
                "sun.misc.Unsafe.putObject",
                "android.security.net.config.RootTrustManager.isSameTrustConfiguration"
            ],
            "files_opened": [
                "/data/user/0/com.bancomer.mbanking/files/PersistedInstallation3610913398658957513tmp",
                "/data/user/0/com.bancomer.mbanking/shared_prefs/com.google.android.gms.measurement.prefs.xml",
                "/data/user/0/com.bancomer.mbanking/files/PersistedInstallation.W0RFRkFVTFRd+MTozNDE0OTM3OTk5MDc6YW5kcm9pZDpkZTNiMGU4Y2NmY2ZlZTVk.json",
                "/data/user/0/com.bancomer.mbanking/files/generatefid.lock",
                "/data/user/0/com.bancomer.mbanking/shared_prefs/local.storage.irl.xml"
            ],
            "encoding_algorithms_observed": [
                "base64"
            ],
            "files_deleted": [
                "/data/user/0/com.bancomer.mbanking/shared_prefs/com.google.android.gms.measurement.prefs.xml.bak",
                "/data/user/0/com.bancomer.mbanking/shared_prefs/FirebaseAppHeartBeat.xml.bak"
            ],
            "last_modification_date": 1709007067,
            "analysis_date": 9,
            "has_evtx": false,
            "shared_preferences_sets": [
                {
                    "key": "fire-installations-id",
                    "value": "1708992605816"
                },
                {
                    "key": "fire-global",
                    "value": "1708992605816"
                }
            ]
        }
    }
}
```

## Relationships

In addition to the previously described attributes, file behaviour objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships)  section.

The following table shows a summary of available relationships.

| Relationship       | Return object type                                   |
| :----------------- | :--------------------------------------------------- |
| file               | A single [File](https://virustotal.readme.io/reference/files)                           |
| attack\_techniques | A list of [Attack Techniques](https://virustotal.readme.io/reference/attack-techniques) |