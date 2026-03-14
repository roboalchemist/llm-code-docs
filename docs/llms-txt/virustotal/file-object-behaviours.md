# Source: https://virustotal.readme.io/reference/file-object-behaviours.md

# 🔀 behaviours

Behaviour reports for the file.

The *behaviours* relationship returns the list of ***all behaviour reports for a given file***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/files-relationships). The response contains a list of [File behaviour](https://virustotal.readme.io/reference/file-behaviour-summary) objects.

```json /files/{file_hash}/behaviours
{
  "data": [
    <FILE_BEHAVIOUR_OBJECT>,
    <FILE_BEHAVIOUR_OBJECT>,
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    "count": <int>,
    "cursor": "<string>"
  }
}
```
```json Example
{
	"data": [
		{
			"attributes": {
				"analysis_date": 1593158333,
				"behash": "34650b9e56550c5815451152e5a5d505",
				"files_opened": [
					"C:\\Windows\\syswow64\\en-US\\USER32.dll.mui"
				],
				"has_html_report": true,
				"has_pcap": true,
				"last_modification_date": 1593158334,
				"modules_loaded": [
					"C:\\Users\\<USER>\\Downloads\\myfile.ENU",
					"C:\\Users\\<USER>\\Downloads\\myfile.EN"
				],
				"registry_keys_opened": [
					"HKCU\\Software\\Borland\\Locales",
					"HKCU\\Software\\Borland\\Delphi\\Locales"
				],
				"sandbox_name": "VirusTotal Jujubox",
				"tags": [
					"RUNTIME_MODULES"
				],
				"text_highlighted": [
					"C:\\Windows\\system32\\cmd.exe"
				]
			},
			"id": "30d1125d95914b55119a55b4105027b592065853e95eb7d5adb5e6b523548891_VirusTotal Jujubox",
			"links": {
				"self": "https://www.virustotal.com/api/v3/file_behaviours/30d1125d95914b55119a55b4105027b592065853e95eb7d5adb5e6b523548891_VirusTotal Jujubox"
			},
			"type": "file_behaviour"
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/files/30d1125d95914b55119a55b4105027b592065853e95eb7d5adb5e6b523548891/behaviours?limit=10"
	},
	"meta": {
		"count": 1
	}
}
```