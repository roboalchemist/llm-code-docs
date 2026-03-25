# Source: https://virustotal.readme.io/reference/url-object-related-references.md

# 🔀🔒 related_references

Related references for a given URL.

The *related\_references* relationship returns a list of ***references related to the URL***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/urls-relationships). The response contains a list of [References](https://virustotal.readme.io/reference/references) objects.

```json /urls/{url_id}/related_references
{
    "meta": {
        "count": <int>
    },
    "data": [
        {
            "attributes": {
								...
            },
            "type": "reference",
            "id": <string>,
            "context_attributes": {
                "related_from": [
                    {
                        "type": <string>,
                        "id": <string>
                    }
                ]
            }
        },
        {
            "attributes": {
                ...
            },
            "type": "reference",
            "id": <string>,
            "context_attributes": {
                "related_from": [
                    {
                        "type": <string>,
                        "id": <string>
                    }
                ]
            }
        }
    ],
}
```
```json Example
{
	"meta": {
		"count": 241,
		"cursor": "eyJsaW1pdCI6IDIsICJvZmZzZXQiOiAyfQ=="
	},
	"data": [
		{
			"attributes": {
				"url": "https://www.proofpoint.com/us/threat-insight/post/holiday-lull-not-so-much",
				"creation_date": 1515715200,
				"author": "Proofpoint Staff",
				"title": "Holiday lull? Not so much"
			},
			"type": "reference",
			"id": "0082e68274dfccb553cd7e19047f0119d01661e7e96af6376743fc853c930a20",
			"links": {
				"self": "https://www.virustotal.com/api/v3/references/0082e68274dfccb553cd7e19047f0119d01661e7e96af6376743fc853c930a20"
			},
			"context_attributes": {
				"related_from": [
					{
						"attributes": {
							"name": "Emotet"
						},
						"type": "collection",
						"id": "malpedia_win_emotet"
					}
				]
			}
		},
		{
			"attributes": {
				"url": "https://www.fortinet.com/blog/threat-research/ms-office-files-involved-again-in-recent-emotet-trojan-campaign-part-ii",
				"creation_date": 1647993600,
				"author": "Xiaopeng Zhang",
				"title": "MS Office Files Involved Again in Recent Emotet Trojan Campaign – Part II"
			},
			"type": "reference",
			"id": "00c52c0a22dc7e6da4aeb3690a573cf3a13521b93b5af0e06cefb51b1face030",
			"links": {
				"self": "https://www.virustotal.com/api/v3/references/00c52c0a22dc7e6da4aeb3690a573cf3a13521b93b5af0e06cefb51b1face030"
			},
			"context_attributes": {
				"related_from": [
					{
						"attributes": {
							"name": "Emotet"
						},
						"type": "collection",
						"id": "malpedia_win_emotet"
					}
				]
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/urls/9a99a24b65c8336298d5dcd773303675c0fa79fd53f6ec19da03588ddb57836a/related_references?limit=2",
		"next": "https://www.virustotal.com/api/v3/urls/9a99a24b65c8336298d5dcd773303675c0fa79fd53f6ec19da03588ddb57836a/related_references?cursor=eyJsaW1pdCI6IDIsICJvZmZzZXQiOiAyfQ%3D%3D&limit=2"
	}
}
```