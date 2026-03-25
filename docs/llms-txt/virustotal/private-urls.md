# Source: https://virustotal.readme.io/reference/private-urls.md

# 🔒 Private URLs

Information about private URLs

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Private URLs are similar to [URLs](https://virustotal.readme.io/reference/url-object), but they are only visible to the user who uploads the URL.

## Object attributes

Most [URL's](https://virustotal.readme.io/reference/url-object) attributes are present in private URLs.

```json Private URL object
{
    "data": {
        "id": <string>,
        "type": "private_url",
        "links": {
            "self": "https://www.virustotal.com/api/v3/private/urls/<id>"
        },
        "attributes": {
            "tags": [
                <string>,
                ...
            ],
            "html_meta": {
                "<str:tag_name>": ["<tag_value:string>"]
            },
            "favicon": {
                "raw_md5": <string>,
                "dhash": <string>
            },
            "title": <string>,
            "redirection_chain": [
                <string>,
                ...
            ],
            "tld": <string>,
            "url": <string>,
            "last_final_url": <string>,
            "last_analysis_results": {
                "Google Safebrowsing": {
                    "method": <string>,
                    "engine_name": <string>,
                    "category": <string>,
                    "result": <string>
                }
            },
            "last_http_response_content_length": <int>,
            "trackers": {
        		"<str:tracker_name>": [
          			{
            			"id": "<string>",
            			"timestamp": <int:timestamp>,
            			"url": "<string>"
          			},...
        		],....
            },
            "outgoing_links": [
                <string>,
                ...
            ],
            "last_http_response_content_sha256": <string>
            "last_http_response_code": <int>,
            "expiration": <int>,
            "last_analysis_stats": {
                "malicious": <int>,
                "suspicious": <int>,
                "undetected": <int>,
                "harmless": <int>,
                "timeout": <int>
            },
            "last_http_response_headers": {
                <string>,
                ...
            }
        }
    }
}
```
```json Example
{
    "data": {
        "id": "7f182b8f63e6709a54645053736825e4c487e434239557ca197ae2cabe75feec",
        "type": "private_url",
        "links": {
            "self": "https://www.virustotal.com/api/v3/private/urls/7f182b8f63e6709a54645053736825e4c487e434239557ca197ae2cabe75feec"
        },
        "attributes": {
            "html_meta": {},
            "redirection_chain": [
                "http://masmetodo.com/"
            ],
            "last_http_response_content_length": 57,
            "last_http_response_code": 200,
            "tags": [],
            "title": "",
            "tld": "com",
            "last_http_response_content_sha256": "7c80d872930ea719369314ee88eefa05181d758fc87e0a0a5cccbf9d36456966",
            "url": "http://masmetodo.com/",
            "last_analysis_results": {
                "Google Safebrowsing": {
                    "method": "blacklist",
                    "engine_name": "Google Safebrowsing",
                    "category": "harmless",
                    "result": "clean"
                }
            },
            "expiration": 1723897413,
            "outgoing_links": [],
            "last_analysis_stats": {
                "malicious": 0,
                "suspicious": 0,
                "undetected": 0,
                "harmless": 1,
                "timeout": 0
            },
            "last_http_response_headers": {
                "Connection": "keep-alive",
                "Content-Encoding": "gzip",
                "Content-Type": "text/html",
                "Transfer-Encoding": "chunked",
                "X-Accel-Version": "0.01",
                "X-Powered-By": "PleskLin",
                "Date": "Wed, 07 Aug 2024 12:46:37 GMT",
                "ETag": "W/\"260a46-39-605eeffe33b7a\"",
                "Last-Modified": "Fri, 22 Sep 2023 09:11:53 GMT",
                "Server": "nginx",
                "Vary": "Accept-Encoding"
            },
            "last_final_url": "http://masmetodo.com/",
        }
    }
}
```

## Relationships

Additionally, private URLs objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section.

The following table shows a summary of available relationships.

| Relationship               | Return object type                                                   |
| :------------------------- | :------------------------------------------------------------------- |
| analyses                   | List of [Private Analyses](https://virustotal.readme.io/reference/private-analyses)                     |
| behaviours                 | List of [Private URLs Behaviours](https://virustotal.readme.io/reference/private-url-behaviours)        |
| last\_serving\_ip\_address | A single [IP address](https://virustotal.readme.io/reference/ip-object)                                 |
| network\_location          | A single [IP address](https://virustotal.readme.io/reference/ip-object) or [Domain](https://virustotal.readme.io/reference/domains-object) |
| downloaded\_files          | List of downloaded [Files](https://virustotal.readme.io/reference/files)                                |