# Source: https://virustotal.readme.io/reference/url-object.md

# URLs

Information about URLs.

URLs doesn't only represent information by themselves, but also can give\
contextual information about files and other elements on VT.

Different URL calls may return different URL-related objects that we list here.

## Object Attributes

* `categories`: <*dictionary*> they key is the partner who categorised the URL and the value is the URL's category according to that partner.
* `favicon` : <*dictionary*> dictionary including difference hash and md5 hash of the URL's favicon. Only returned in premium API.
  * `dhash`: <*string*> difference hash
  * `raw_md5`: <*string*> favicon's MD5 hash.
* `first_submission_date`: <*integer*> UTC timestamp of the date where the URL was first submitted to VirusTotal.
* `html_meta`: <*dictionary*> containing all meta tags (only for URLs downloading a HTML). Keys are the meta tag name and value is a list containing all values of that meta tag.
* `last_analysis_date`: <*integer*> UTC timestamp representing last time the URL was scanned.
* `last_analysis_results`: <*dictionary*> result from URL scanners. dict with scanner name as key and a dict with notes/result from that scanner as value.
  * `category`: <*string*> normalized result. can be:
    * "harmless" (site is not malicious),
    * "undetected" (scanner has no opinion about this site),
    * "suspicious" (scanner thinks the site is suspicious),
    * "malicious" (scanner thinks the site is malicious).
  * `engine_name`: <*string*> complete name of the URL scanning service.
  * `method`: <*string*> type of service given by that URL scanning service (i.e. "blacklist").
  * `result`: <*string*> raw value returned by the URL scanner ("clean", "malicious", "suspicious", "phishing"). It may vary from scanner to scanner, hence the need for the "category" field for normalisation.
* `last_analysis_stats`: <*dictionary*> number of different results from this scans.
  * `harmless`: <*integer*> number of reports saying that is harmless.
  * `malicious`: <*integer*> number of reports saying that is malicious.
  * `suspicious`: <*integer*> number of reports saying that is suspicious.
  * `timeout`: <*integer*> number of timeouts when checking this URL.
  * `undetected`: <*integer*> number of reports saying that is undetected.
* `last_final_url`: <*string*> if the original URL redirects, where does it end.
* `last_http_response_code`: <*integer*> HTTP response code of the last response.
* `last_http_response_content_length`: <*integer*> length in bytes of the content received.
* `last_http_response_content_sha256`: <*string*> URL response body's SHA256 hash.
* `last_http_response_cookies`: <*dictionary*> containing the website's cookies.
* `last_http_response_headers`: <*dictionary*> containing headers and values of last HTTP response.
* `last_modification_date`: <*integer*> UTC timestamp representing last modification date.
* `last_submission_date`: <*integer*> UTC timestamp representing last time it was sent to be analysed.
* `outgoing_links`: <*list of strings*> containing links to different domains.
* `redirection_chain`: <*list of strings*> history of redirections followed when visiting a given URL. The last URL of the chain is not included in the list since it is available at the `last_final_url` attribute.
* `reputation`: <*integer*> value of votes from VT community.
* `tags`: <*list of strings*> tags.
* `targeted_brand`: <*dictionary*> targeted brand info extracted from phishing engines.
* `times_submitted`: <*integer*> number of times that URL has been checked.
* `title`: <*string*> webpage title.
* `total_votes`: *\<dictionary*> containing the number of positive ("harmless") and negative ("malicious") votes received from VT community.
  * `harmless`: <*integer*> number of positive votes.
  * `malicious`: <*integer*> number of negative votes.
* `trackers`: <*dictionary*> contains all found trackers in that URL in a historical manner. Every key is a tracker name, which is a dictionary containing:
  * `id`: <*string*> tracker ID, if available.
  * `timestamp`: <*integer*> tracker ingestion date as UNIX timestamp.
  * `url`: <*string*> tracker script URL.
* `url`: <*string*> original URL to be scanned.
* `has_content`: <*boolean*> Whether the url has content in it.

```json "url" object
{
  "data": {
    "attributes": {
      "categories": {dict},
      "favicon": {
        "dhash": "<string>",
        "raw_md5": "<string>"
      },
      "first_submission_date": <int:timestamp>,
      "html_meta": {
        "<str:tag_name>": ["<tag_value:string>"]
      },
      "last_analysis_date": <int:timestamp>,
      "last_analysis_results": {
        "<str:scanner name>": {
          "category": "<string>",
          "engine_name": "<string>",
          "method": "<string>",
          "result": "<string>"
          }, ...
        },
      "last_analysis_stats": {
        "harmless": <int>,
        "malicious": <int>,
        "suspicious": <int>,
        "timeout": <int>,
        "undetected": <int>
        },
      "last_final_url": "<string>",
      "last_http_response_code": <int>,
      "last_http_response_content_length": <int>,
      "last_http_response_content_sha256": "<string>",
      "last_http_response_cookies": {"<string>": "<string>", ... },
      "last_http_response_headers": {"<string>": "<string>", ... },
      "last_modification_date": <int:timestamp>,
      "last_submission_date": <int:timestamp>,
      "outgoing_links": ["<string>"],
      "redirection_chain": ["<string>"],
      "reputation": <int>,
      "tags": [<strings>],
      "targeted_brand": {
      	"<str:engine_name>": "string"
      },
      "times_submitted": <int>,
      "title": "<string>",
      "total_votes": {
        "harmless": <int>,
      	"malicious": <int>
      },
      "trackers": {
        "<str:tracker_name>": [
          {
            "id": "<string>",
            "timestamp": <int:timestamp>,
            "url": "<string>"
          },...
        ],....
      },
      "url": "<string>"
      },
    "id": "<URL SHA256>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/urls/<URL SHA256>"
    }
    "type": "url"
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "categories": {
                "BitDefender": "business",
                "Forcepoint ThreatSeeker": "web hosting"
            },
            "favicon": {
                "dhash": "30d6d6dec869b6a6",
             		"raw_md5": "f6c933a8a01167c2bfgb5fg65183781"
          	},
            "first_submission_date": 1591711462,
            "has_content": true,
            "html_meta": {
                "description": [
                    "dezpipccner p\u0142bntno\u015bci intesnebofe holpne wla kv\u017cwego"
                ],
                "sessid": [
                    "6555835"
                ],
                "viewport": [
                    "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"
                ]
            },
            "last_analysis_date": 1591715484,
            "last_analysis_results": {
                "ADMINUSLabs": {
                    "category": "harmless",
                    "engine_name": "ADMINUSLabs",
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
                },
                "Antiy-AVL": {
                    "category": "harmless",
                    "engine_name": "Antiy-AVL",
                    "method": "blacklist",
                    "result": "clean"
                },
                "Artists Against 419": {
                    "category": "harmless",
                    "engine_name": "Artists Against 419",
                    "method": "blacklist",
                    "result": "clean"
                }
            },
            "last_analysis_stats": {
                "harmless": 64,
                "malicious": 7,
                "suspicious": 0,
                "timeout": 0,
                "undetected": 9
            },
            "last_final_url": "http://pocvttpalok.net/qwlotnvsc8090067532",
            "last_http_response_code": 200,
            "last_http_response_content_length": 28195,
            "last_http_response_content_sha256": "45b81b2d4c58ada2c13q503hb56daf440ec1b9b69f3737df4cf460a080c0ab63",
            "last_http_response_cookies": {
                "PHPSESSID": "5aivcogd1tjp2b4kbfm5551mo0",
                "SameSite": "Lax,",
                "__cfduid": "d84e7486e1p2cc5a7ff3vd85d128183624591715485",
                "sessid": "494429474"
            },
            "last_http_response_headers": {
                "cache-control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
                "cf-cache-status": "DYNAMIC",
                "cf-ray": "5a0b78f576668hch-OhD",
                "cf-request-id": "03hb3befhc00h083h9dh9c820h0h0h01",
                "connection": "keep-alive",
                "content-type": "text/html; charset=UTF-8",
                "date": "Tue, 09 Jun 2020 15:11:25 GMT",
                "expires": "Thu, 19 Nov 1981 08:52:00 GMT",
                "pragma": "no-cache",
                "server": "cloudflare",
                "set-cookie": "__cfduid=d8ded48de1d2dc1da7df34d85d1bd1d56d1d9d7d5d85; expires=Thu, 09-Jul-20 15:11:25 GMT; path=/; domain=.fpofztfpflfk.net; HttpOnly; SameSite=Lax, PHPSESSID=5afvcfgf1tjs2bakf1mfvfqfo0; path=/, sessid=665627777; expires=Thu, 09-Jul-2020 15:10:43 GMT; Max-Age=2592000; path=/",
                "transfer-encoding": "chunked"
            },
            "last_modification_date": 1591715488,
            "last_submission_date": 1591715484,
            "outgoing_links": [
                "https://ssl.dgtuww.pl/files/reg2lafif_gttp3w_way.pdf",
                "http://www.dtywpwy.pl/polwtwka-wwikow-wowkiws/"
            ],
            "reputation": -44,
            "redirection_chain": [
                "http://wwwcztapwlwk.net/plafgxc80333067532",
                "http://wwwcztapwlwk.net/step2"
            ],
            "tags": [
                "base64-embedded"
            ],
            "targeted_brand": {
                "Phishtank": "Bank Blablabla"
            },
            "times_submitted": 2,
            "title": "Dwtpww - Bwzpiwczww plwtnwww wntwrnewowe wa kwzdego!",
            "total_votes": {
                "harmless": 0,
                "malicious": 1
            },
            "trackers": {
                "Google Tag Manager": [
                    {
                        "id": "UA-162655555-1",
                        "timestamp": 1603372118,
                        "url": "https://www.googletagmanager.com/gtag/js?id=UA-162655555-1"
                    }
                ]
            },
            "url": "http://wwwcztapwlwk.net/plafgxc80333067532"
        },
        "id": "661q6ceqa60e4qaf1998qa8aa8q6d8daq4c51qc2qfqc5fcd6d885700c0acee3b",
        "links": {
            "self": "https://www.virustotal.com/ui/urls/661q6ceqa60e4qaf1998qa8aa8q6d8daq4c51qc2qfqc5fcd6d885700c0acee3b"
        },
        "type": "url"
    }
}
```

## Relationships

In addition to the previously described attributes, URL objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section. The available relationships are described bellow.

| Relationship               | Description                                                    | Accessibility             | Return object type                                                    |
| :------------------------- | :------------------------------------------------------------- | :------------------------ | :-------------------------------------------------------------------- |
| analyses                   | Analyses for the URL.                                          | VT Enterprise users only. | List of [Analyses](https://virustotal.readme.io/reference/analyses-object).                              |
| comments                   | Community posted comments about the URL.                       | Everyone.                 | List of [Comments](https://virustotal.readme.io/reference/comments).                                     |
| communicating\_files       | Files that communicate with a given URL when they're executed. | VT Enterprise users only. | List of [Files](https://virustotal.readme.io/reference/files).                                           |
| contacted\_domains         | Domains from which the URL loads some kind of resource.        | VT Enterprise users only. | List of [Domains](https://virustotal.readme.io/reference/domains-object).                                |
| contacted\_ips             | IPs from which the URL loads some kind of resource.            | VT Enterprise users only. | List of [IP addresses](https://virustotal.readme.io/reference/ip-object).                                |
| downloaded\_files          | Files downloaded from the URL.                                 | VT Enterprise users only. | List of [Files](https://virustotal.readme.io/reference/files).                                           |
| graphs                     | Graphs including the URL.                                      | Everyone.                 | List of [Graphs](https://virustotal.readme.io/reference/graph-object).                                   |
| last\_serving\_ip\_address | Last IP address that served the URL.                           | Everyone.                 | A single [IP address](https://virustotal.readme.io/reference/ip-object).                                 |
| network\_location          | Domain or IP for the URL.                                      | Everyone.                 | A single [IP address](https://virustotal.readme.io/reference/ip-object) or [Domain](https://virustotal.readme.io/reference/domains-object). |
| referrer\_files            | Files containing the URL.                                      | VT Enterprise users only. | A list of [Files](https://virustotal.readme.io/reference/files).                                         |
| referrer\_urls             | URLs referring the URL.                                        | VT Enterprise users only. | A list of [URLs](https://virustotal.readme.io/reference/url-object).                                     |
| redirecting\_urls          | URLs that redirected to the given URL.                         | VT Enterprise users only. | A list of [URLs](https://virustotal.readme.io/reference/url-object).                                     |
| redirects\_to              | URLs that the URL redirects to.                                | VT Enterprise users only. | A list of [URLs](https://virustotal.readme.io/reference/url-object).                                     |
| related\_comments          | Community posted comments in the URL's related objects.        | Everyone.                 | A list of [Comments](https://virustotal.readme.io/reference/comments).                                   |
| related\_references        | References related to the URL.                                 | VT Enterprise users only. | A list of [References](https://virustotal.readme.io/reference/references).                               |
| related\_threat\_actors    | Threat actors related to the URL.                              | VT Enterprise users only. | A list of [Threat Actors](https://virustotal.readme.io/reference/threat-actors-object).                  |
| submissions                | URL's submissions.                                             | VT Enterprise users only. | A list of [Submissions](https://virustotal.readme.io/reference/submission-object).                       |