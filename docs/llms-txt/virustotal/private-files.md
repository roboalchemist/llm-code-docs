# Source: https://virustotal.readme.io/reference/private-files.md

# 🔒 Private Files

Information about private files

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Private files are similar to [Files](https://virustotal.readme.io/reference/files), but they are only visible to the user who uploads the file.

A private file object ID is its SHA256 hash.

## Object attributes

Most [File's](https://virustotal.readme.io/reference/files) attributes are present in private files, except for `last_analysis_stats` and `last_analysis_results` since private files are not run by antivirus.

```json Private file object
{
	"data": {
		"attributes": {
			"androguard": <dict>,
			"authentihash": <string>,
			"bundle_info": <dict>,
			"class_info": <dict>,
			"creation_date": <int: timestamp>,
			"crowdsourced_yara_results": [
				{
					"description": <string>,
					"match_in_subfile": <boolean>,
					"rule_name": <string>,
					"ruleset_id": <string>,
					"ruleset_name": <string>,
					"source": <string>
				}
			],
			"deb_info": <dict>,
			"dmg_info": <dict>,
			"dot_net_assembly": <dict>,
			"dot_net_guids": <dict>,
			"elf_info": <dict>,
			"exiftool": <dict>,
			"html_info": <dict>,
			"image_code_injections": <string>,
			"ipa_info": <dict>,
			"isoimage_info": <dict>,
			"jar_info": <dict>,
			"javascript_info": <dict>,
			"magic": <string>,
			"macho_info": [
				<dict>,
				...
			],
			"main_icon": <dict>,
			"md5": <string>,
			"office_info": <dict>,
			"openxml_info": <dict>,
			"pdf_info": <dict>,
			"packers": <dict>,
			"pe_info": <dict>,
			"powershell_info": <dict>,
			"rombios_info": <dict>,
			"rtf_info": <dict>,
			"sandbox_verdicts": {
				<string: sandbox_name>: {
					"category": <string>,
					"confidence": <int>,
					"malware_classification": [
						<string>
					],
					"malware_names": [
						<string>
					],
					"sandbox_name": <string>
				},
			},
			"sha1": <string>,
			"sha256": <string>,
			"signature_info": <dict>,
			"size": <int>,
			"ssdeep": <string>,
			"swf_info": <dict>,
			"tags": [
				<string>,
				...
			],
			"telfhash": <string>,
			"tlsh": <string>,
			"trid": [
				<dict>,
				...
			],
			"type_description": <string>,
			"type_extension": <string>,
			"type_tag": <string>,
			"vba_info": <dict>,
			"vhash": <string>
		},
		"type": "private_file",
		"id": <string>,
		"links": {
			"self": "https://www.virustotal.com/api/v3/private/files/<id>"
		}
	}
}
```
```json Example
{
  "data": {
    "attributes": {
      "sha1": "7bae8076a5771865123be7112468b79e9d78a640",
      "magic": "ASCII text",
      "tags": [
        "text"
      ],
      "exiftool": {
        "MIMEType": "text/plain",
        "LineCount": "1",
        "MIMEEncoding": "us-ascii",
        "FileTypeExtension": "txt",
        "FileType": "TXT",
        "WordCount": "1",
        "Newlines": "Unix LF"
      },
      "trid": [
        {
          "file_type": "file seems to be plain text/ASCII",
          "probability": 0.0
        }
      ],
      "vhash": "9eecb7db59d16c80417c72d1e1f4fbf1",
      "sha256": "11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772",
      "ssdeep": "3:tdn:T",
      "md5": "e5828c564f71fea3a12dde8bd5d27063",
      "size": 5
    },
    "type": "private_file",
    "id": "11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772",
    "links": {
      "self": "https://virustotal.com/api/v3/private/files/11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772"
    }
  }
}
```

## Relationships

In addition to the previously described attributes, private file objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section.

The following table shows a summary of available relationships.

| Relationship       | Return object type                                             |
| :----------------- | :------------------------------------------------------------- |
| behaviours         | List of [Private File Behaviours](https://virustotal.readme.io/reference/private-file-behaviours) |
| dropped\_files     | List of [Private Files](https://virustotal.readme.io/reference/private-files)                     |
| execution\_parents | List of [Private Files](https://virustotal.readme.io/reference/private-files)                     |