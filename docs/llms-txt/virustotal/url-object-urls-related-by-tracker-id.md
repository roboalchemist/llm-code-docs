# Source: https://virustotal.readme.io/reference/url-object-urls-related-by-tracker-id.md

# 🔀🔒 urls_related_by_tracker_id

URLs having trackers with the same IDs

The *urls\_related\_by\_tracker\_id* relationship returns a list of all URLs **having at least one tracker ID in common with a given URL**. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/urls-relationships). The response contains a list of [URL](https://virustotal.readme.io/reference/url-object) objects. The relationship contains the following context attributes:

* `url`: <*string*> the URL is added as context attribute in case it's missing in the VirusTotal dataset.

```json /urls/{url_id}/urls_related_by_tracker_id
{
  "data": [
    {
      "attributes": <URL_OBJECT>,
      "context_attributes": {
        "url": "<string>"
        }
    },
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
        "categories": {
          "Forcepoint ThreatSeeker": "web and email marketing"
        },
        "first_submission_date": 1444169312,
        "has_content": false,
        "html_meta": {
          "robots": [
            "noindex"
          ],
          "viewport": [
            "width=1024"
          ]
        },
        "last_analysis_date": 1611178249,
        "last_analysis_results": {
          "ADMINUSLabs": {
            "category": "harmless",
            "engine_name": "ADMINUSLabs",
            "method": "blacklist",
            "result": "clean"
          },
          "AICC (MONITORAPP)": {
            "category": "harmless",
            "engine_name": "AICC (MONITORAPP)",
            "method": "blacklist",
            "result": "clean"
          },
          "AegisLab WebGuard": {
            "category": "harmless",
            "engine_name": "AegisLab WebGuard",
            "method": "blacklist",
            "result": "clean"
          },
          "AlienVault": {
            "category": "harmless",
            "engine_name": "AlienVault",
            "method": "blacklist",
            "result": "clean"
          }
        },
        "last_analysis_stats": {
          "harmless": 4,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "undetected": 0
        },
        "last_final_url": "https://example.com/lpc_not_found.html",
        "last_http_response_code": 404,
        "last_http_response_content_length": 15181,
        "last_http_response_content_sha256": "e6369031a13be93f3773d41307386eb33fd33f923c693a1a3a8d6333bd695da8",
        "last_http_response_cookies": {
          "core": "9i4ao44mi046l4srcs732rn9m8",
          "gr83p_59db3474322417e4c009441064df45dd": "true"
        },
        "last_http_response_headers": {
          "cache-control": "no-store, no-cache, must-revalidate",
          "content-type": "text/html; charset=UTF-8",
          "date": "Wed, 20 Jan 2021 21:30:50 GMT",
          "expires": "Thu, 19 Nov 1981 08:52:00 GMT",
          "pragma": "no-cache",
          "strict-transport-security": "max-age=31536000",
          "transfer-encoding": "chunked",
          "x-content-type-options": "nosniff",
          "x-frame-options": "sameorigin",
          "x-xss-protection": "1; mode=block"
        },
        "last_modification_date": 1611178260,
        "last_submission_date": 1611178249,
        "reputation": 0,
        "tags": [
          "ip"
        ],
        "targeted_brand": {},
        "threat_names": [],
        "times_submitted": 4,
        "title": "Welcome to my webpage!",
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "trackers": {
          "Google Tag Manager": [
            {
              "id": "GTM-XXXXXX",
              "timestamp": 1611178249,
              "url": "//www.googletagmanager.com/ns.html?id=GTM-XXXXXX"
            },
            {
              "id": "GTM-XXXXXX",
              "timestamp": 1611178249,
              "url": "//www.googletagmanager.com/gtm.js?id='+i+dl"
            }
          ],
          "New Relic": [
            {
              "timestamp": 1611178249,
              "url": ""
            },
            {
              "timestamp": 1611178249,
              "url": "{beacon:\"bam.nr-data.net\",errorBeacon:\"bam.nr-data.net\",agent:\"js-agent.newrelic.com/nr-1194.min.js\"}"
            }
          ]
        },
        "url": "http://105.150.54.55/"
      },
      "context_attributes": {
        "url": "http://105.150.54.55/"
      },
      "id": "57c1f1040f4c2cc47473493a4402c4d75a4a4b4431a964d7c4efa44ed9aab571",
      "links": {
        "self": "https://www.virustotal.com/api/v3/urls/57c1f1040f4c2cc47473493a4402c4d75a4a4b4431a964d7c4efa44ed9aab571"
      },
      "type": "url"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/urls/57c1f1040f4c2cc47473493a4402c4d75a4a4b4431a964d7c4efa44ed9aab571/urls_related_by_tracker_id?cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D&limit=1",
    "self": "https://www.virustotal.com/api/v3/urls/57c1f1040f4c2cc47473493a4402c4d75a4a4b4431a964d7c4efa44ed9aab571/urls_related_by_tracker_id?limit=1"
  },
  "meta": {
    "count": 1263,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ=="
  }
}
```