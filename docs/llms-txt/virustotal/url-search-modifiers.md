# Source: https://virustotal.readme.io/docs/url-search-modifiers.md

# URL search modifiers

[VirusTotal Intelligence](https://www.virustotal.com/gui/intelligence-overview) allows you to perform advanced faceted searches over the historical collection of URLs. These searches can act on basically all the metadata that we generate for URLs: url string, path, query parameters and values, favicon, meta tags, contained Ad trackers, tags, reputation, etc.

VirusTotal Intelligence searches by default over the historical collection of files, **in order to search over URLs you need to add the facet condition *entity:url***. For example, let's ask for all those URLs that have been detected by more than 5 URL scanners and were first submitted after October 17th 2019:

[entity:url p:5+ fs:2019-10-17+](https://www.virustotal.com/gui/search/entity%253Aurl%2520positives%253A5%252B%2520fs%253A2019-10-17%252B/urls)

You can click on the filter icon inside the main search box in order to navigate to a URL search assistant:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/urlsearchmodifiers_20231108.png",
        null,
        "URL search modifiers"
      ],
      "align": "center"
    }
  ]
}
[/block]

Note that the assistant will not allow you to build complex searches combining **AND, OR and NOT** conditions. For example:

[(entity:url AND positives:5+ AND fs:2019-10-17+) AND (tld:ru OR tld:tk)](https://www.virustotal.com/gui/search/\(entity%253Aurl%2520AND%2520positives%253A5%252B%2520AND%2520fs%253A2019-10-17%252B\)%2520AND%2520\(tld%253Aru%2520OR%2520tld%253Atk\)/urls)

The following table describes all the search modifiers (facets) that can be used, you can combine any number of them:

The following modifiers admits wildcards: **hostname** , **outgoing\_link**, **path** , **url**.

[block:parameters]
{
  "data": {
    "h-0": "",
    "h-1": "",
    "0-0": "**comment:**",
    "0-1": "Search for URLs that have a VirusTotal Community comment containing the word or phrase provided. <br/>Example: [entity:url comment:IOCs](https://www.virustotal.com/gui/search/entity%253Aurl%2520comment%253AIOCs/urls)",
    "1-0": "**comment\\_author:**",
    "1-1": "Search for URLs that have been commented by the user with the username provided.<br/>Example: [entity:url comment\\_author:68h7EGyNm](https://www.virustotal.com/gui/search/entity%253Aurl%2520comment_author%253A68h7EGyNm/urls)",
    "2-0": "**fs:**",
    "2-1": "Filter URLs based on the first seen date in VirusTotal. Note that less than and greater than syntax is allowed.<br/>Examples: [entity:url fs:2019-10-10+](https://www.virustotal.com/gui/search/entity%253Aurl%2520fs%253A2019-10-10%252B/urls), [entity:url fs:2019-10-10-](https://www.virustotal.com/gui/search/entity%253Aurl%2520fs%253A2019-10-10-/urls)",
    "3-0": "**ls:**",
    "3-1": "Filter URLs based on the last seen date in VirusTotal. Note that less than and greater than syntax is allowed.<br/>Examples: [entity:url ls:2019-10-10-](https://www.virustotal.com/gui/search/entity%253Aurl%2520ls%253A2019-10-10-/urls), [entity:url ls:2019-10-10+](https://www.virustotal.com/gui/search/entity%253Aurl%2520ls%253A2019-10-10%252B/urls)",
    "4-0": "**la:**",
    "4-1": "Filters URLs to be returned according to their last analysis datetime. Normally the last analysis datetime will be the same as the last submission datetime, however, sometimes users will rescan a URL but will then decide to view the latest report on the URL rather than waiting for the rescanning, in those cases both dates may differ. It allows you to specify larger than or smaller than values. <br/> Examples: [entity:url la:2025-08-21T16:00:00](https://www.virustotal.com/gui/search/entity%253Aurl%2520la%253A2025-08-21T16%253A00%253A00), [entity:url la:2025-01-01T19:59:22-](https://www.virustotal.com/gui/search/entity%253Aurl%2520la%253A2025-01-01T19%253A59%253A22-), [entity:url la:2025-08-21T16:59:22+](https://www.virustotal.com/gui/search/entity%253Aurl%2520la%253A2025-08-21T16%253A59%253A22%252B), [entity:url la:2025-08-21T16:00:00+](https://www.virustotal.com/gui/search/entity%253Aurl%2520la%253A2025-08-21T16%253A00%253A00%252B), [entity:url la:2025-08-21T16:59:22-](https://www.virustotal.com/gui/search/entity%253Aurl%2520la%253A2025-08-21T16%253A59%253A22-), [entity:url la:3d+ ](https://www.virustotal.com/gui/search/entity%253Aurl%2520la%253A3d%252B)",
    "5-0": "**lm:**<br/>**last_modification_date:**<br/>**last_modified:**",
    "5-1": "Filters URLs to be returned according to their last modification datetime. It allows you to specify larger than or smaller than values. <br/>Examples: [entity:url lm:2025-08-22T06:40:59](https://www.virustotal.com/gui/search/entity%253Aurl%2520lm%253A2025-08-22T06%253A40%253A59?type=urls), [entity:url lm:2026-01-01T19:59:22-](https://www.virustotal.com/gui/search/entity%253Aurl%2520lm%253A2025-01-01T19%253A59%253A22-?type=urls), [entity:url lm:2025-08-21T16:59:22+](https://www.virustotal.com/gui/search/entity%253Aurl%2520lm%253A2025-08-21T16%253A59%253A22%252B), [entity:url lm:2025-08-2116:00:00+](https://www.virustotal.com/gui/search/entity%253Aurl%2520lm%253A2025-08-2116%253A00%253A00%252B?type=urls) [entity:url lm:2025-08-2116:59:22-](https://www.virustotal.com/gui/search/entity%253Aurl%2520lm%253A2025-08-2116%253A59%253A22-?type=urls), [entity:url lm:3d+](https://www.virustotal.com/gui/search/entity%253Aurl%2520lm%253A3d%252B?type=urls)",
    "6-0": "**main\\_icon\\_dhash:**",
    "6-1": "Search for URLs with a favicon which is visually similar to another favicon, a visual similarity hash is used for this purpose. This search can be triggered by clicking on the favicon preview of the URL in the search listings. Can be useful to discover phishing sites targeting a given company.<br/>Example: [entity:url main\\_icon\\_dhash:\"cc8cccccaae070b2\" NOT hostname:\"dropbox.com\" NOT hostname:\"dropboxforum.com\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520main_icon_dhash%253A%2522cc8cccccaae070b2%2522%2520NOT%2520hostname%253A%2522dropbox.com%2522%2520NOT%2520hostname%253A%2522dropboxforum.com%2522/urls)",
    "7-0": "**p:** <br/>**positives:**",
    "7-1": "Filter URLs according to the number of engines/blocklists that detect them. Less than and greater than syntax is allowed.<br/>Examples: [entity:url p:10+](https://www.virustotal.com/gui/search/entity%253Aurl%2520p%253A10%252B/urls), [entity:url p:10-](https://www.virustotal.com/gui/search/entity%253Aurl%2520p%253A10-/urls)",
    "8-0": "**engines:**",
    "8-1": "Focus on URLs that have been detected with a given label by at least one scanner/blocklist.<br/>Example: [entity:url engines:malware](https://www.virustotal.com/gui/search/entity%253Aurl%2520engines%253Amalware/urls)",
    "9-0": "**_engine_name:_**",
    "9-1": "Focus on URLs that have been detected with a given label by a specific scanner/blocklist.<br/>You can check the full list of engines names in this [link](https://virustotal.readme.io/docs/list-file-engines)<br/>Example: [entity:url fortinet:malware](https://www.virustotal.com/gui/search/entity%253Aurl%2520fortinet%253Amalware/urls)",
    "10-0": "**reputation:**",
    "10-1": "Filter URLs according to its reputation among the VirusTotal user base.<br/>Example: [entity:url reputation:70+](https://www.virustotal.com/gui/search/entity%253Aurl%2520reputation%253A70%252B/urls)",
    "11-0": "**s:**<br/>**submissions:**",
    "11-1": "Filter URLs according to the number of times they have been sent to VirusTotal for analysis. Less than and greater than syntax is allowed.<br/>Examples: [entity:url s:10+](https://www.virustotal.com/gui/search/entity%253Aurl%2520s%253A10%252B/urls), [entity:url s:10-](https://www.virustotal.com/gui/search/entity%253Aurl%2520s%253A10-/urls)",
    "12-0": "**submitter:**",
    "12-1": "Search for URLs submitted via a given interface (API, web) or sent from a given country (two-letter ISO country code).<br/>Example: [entity:url submitter:web submitter:MY](https://www.virustotal.com/gui/search/entity%253Aurl%2520submitter%253Aweb%2520submitter%253AMY/urls)",
    "13-0": "**first\\_submitter:**",
    "13-1": "Search for URLs which first submission was sent from a given country (two-letter ISO country code).<br/>Example: [entity:url first\\_submitter:ua](https://www.virustotal.com/gui/search/entity%253Aurl%2520first_submitter%253Aua/urls)",
    "14-0": "**tag:**",
    "14-1": "Filter URLs according to their tags.<br/>Example: [entity:url tag:\"downloads-pe\" header\\_value:\"image/jpeg\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520tag%253A%2522downloads-pe%2522%2520header_value%253A%2522image%252Fjpeg%2522/urls)<br/>List of available tags:<br/><ul><li>**_ip:_** the URL's hostname is a bare IP address rather than a domain.</li><li>**_non-ascii:_** the URL's hostname contains non-ascii characters, i.e. punycode.</li><li>**_downloads-pe:_** the URL downloads a windows executable.</li><li>**_downloads-apk:_** the URL downloads an Android APK.</li><li>**_downloads-elf:_** the URL downloads a Linux executable.</li><li> **_downloads-dmg:_** the URL downloads an OS X package.</li><li>**_downloads-zip:_** the URL downloads a ZIP bundle.</li><li>**_downloads-pdf:_** the URL downloads a PDF document.</li><li>**_downloads-doc:_** the URL downloads a Microsoft Office document.</li><li>**_opendir:_** the URL is an open directory, i.e. directory browsing is possible.</li><li>**_contains-pe:_**the URL is an open directory and it lists at least one file with an .exe extension.</li><li>**_contains-zip_**: same as above but for .zip extension.</li><li>**_contains-msi:_**same as above but for .msi extension.</li><li>**_contains-apk:_** same as above but for .apk extension.</li><li>**_contains-dmg:_** same as above but for .dmg extension.<br/>_For a complete list of tags, see [Full list of VirusTotal Intelligence tag modifier](https://virustotal.readme.io/docs/intelligence-tag-list)_",
    "15-0": "**asn:**<br/>**autonomous\\_system\\_number:**",
    "15-1": "Search for URLs in domains that resolve to an IP address under the responsibility of the given autonomous system number.<br/>Example: [entity:url asn:7506](https://www.virustotal.com/gui/search/entity%253Aurl%2520asn%253A7506/urls)",
    "16-0": "**aso:**<br/>**as\\_owner:**<br/>**autonomous\\_system\\_owner:**",
    "16-1": "Search for URLs in domains that resolve to an IP address under the responsibility of the given autonomous system owner label.<br/>Example: [entity:url aso:\"Google LLC\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520aso%253A%2522Google%2520LLC%2522/urls)",
    "17-0": "**category:**",
    "17-1": "Filter URLs according to the content category of its domain, as depicted in the details section of the pertinent domain report.<br/>Examples: [entity:url category:\"business and economy\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520category%253A%2522business%2520and%2520economy%2522/urls), [entity:url category:\"known infection source\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520category%253A%2522known%2520infection%2520source%2522/urls)",
    "18-0": "**cookie:**",
    "18-1": "Filter URLs according to the cookie name set in the HTTP server response. Note that this is a fulltext search, you can search for the entire cookie name or for subwords of it.<br/>Example: [entity:url cookie:\"VT\\_PREFERRED\\_LANGUAGE\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520cookie%253A%2522VT_PREFERRED_LANGUAGE%2522/urls)",
    "19-0": "**cookie\\_value:**",
    "19-1": "Filter URLs according to a cookie value set in the HTTP server response. Note that this is a fulltext search, you can search for the entire cookie value or for subwords of it.<br/>Example: [entity:url cookie:\"VT\\_PREFERRED\\_LANGUAGE\" cookie\\_value:\"en\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520cookie%253A%2522VT_PREFERRED_LANGUAGE%2522%2520cookie_value%253A%2522en%2522/urls)",
    "20-0": "**header:**",
    "20-1": "Filter URLs according to the HTTP server response header keys.<br/>Example: [entity:url header:\"set-cookie\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520header%253A%2522set-cookie%2522/urls)",
    "21-0": "**header\\_value:**",
    "21-1": "Filter URLs according to the HTTP server response header values.<br/>Example: [entity:url header\\_value:\"PHP/5.3.29, PleskLin\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520header_value%253A%2522PHP%252F5.3.29%252C%2520PleskLin%2522/urls)",
    "22-0": "**hostname:**",
    "22-1": "Filter URLs according to the hostname. Note that this is a fulltext search, meaning that subwords can be used.<br/>Example: [entity:url hostname:santander NOT hostname:bancosantander](https://www.virustotal.com/gui/search/entity%253Aurl%2520hostname%253Asantander%2520NOT%2520hostname%253Abancosantander/urls)",
    "23-0": "**ip:**",
    "23-1": "Filter URLs according to the IP address to which its domain resolved at the time of analysis. Allows range searches and CIDRs.<br/>Examples: [entity:url ip:\"200.61.38.216\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520ip%253A%2522200.61.38.216%2522/urls), [entity:url ip:\"200.61.38.216/24\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520ip%253A%2522200.61.38.216%252F24%2522/urls)",
    "24-0": "**max\\_url\\_positives:**",
    "24-1": "Filter URLs according to the maximum number of detections considering all historical analyses performed on the URL.<br/>Example: [entity:url max\\_url\\_positives:10+ positives:0](https://www.virustotal.com/gui/search/entity%253Aurl%2520max_url_positives%253A10%252B%2520positives%253A0/urls)",
    "25-0": "**meta:**",
    "25-1": "Filter URLs according to the META tags contained in the HTML that gets returned. Can be used to discover phishing sites.<br/>Example: [entity:url meta:\"NAB personal banking financial solutions\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520meta%253A%2522NAB%2520personal%2520banking%2520financial%2520solutions%2522/urls)",
    "26-0": "**password:**",
    "26-1": "Focus on URLs that have a password field and match a given text. <br/>Example: [entity:url have:password NOT username:mailto](https://www.virustotal.com/gui/search/entity%253Aurl%2520have%253Apassword%2520NOT%2520username%253Amailto%2520hostname%253Aamazonaws/urls)",
    "27-0": "**path:**",
    "27-1": "Filter URLs according to path sequences or subwords within the URL’s path.<br/>Example: [entity:url path:\"gate.php\" response\\_code:200](https://www.virustotal.com/gui/search/entity%253Aurl%2520path%253A%2522gate.php%2522%2520response_code%253A200/urls)",
    "28-0": "**exact\\_path:**",
    "28-1": "Filter URLs whose path is exactly the given value.<br/>Example: [entity:url exact\\_path:\"/virustotal/\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520exact_path%253A%2522%252Fvirustotal%252F%2522/urls)",
    "29-0": "**extension:**",
    "29-1": "Filter URLs according to extension parsing based on the URL path or content disposition filename HTTP response header.<br/>Example: [entity:url extension:jpg tag:downloads-pe](https://www.virustotal.com/gui/search/entity%253Aurl%2520extension%253Ajpg%2520tag%253Adownloads-pe/urls)",
    "30-0": "**port:**",
    "30-1": "Filter URLs according to the port on which the HTTP server is operating.<br/>Example: [entity:url port:8080](https://www.virustotal.com/gui/search/entity%253Aurl%2520port%253A8080/urls)",
    "31-0": "**query\\_field:**",
    "31-1": "Filter URLs according to the key/name of query fields contained in the URL.<br/>Example: [entity:url query\\_field:\"loginpage\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520query_field%253A%2522loginpage%2522/urls)",
    "32-0": "**query\\_value:**",
    "32-1": "Filter URLs according to the value contained in its query values.<br/>Example: [entity:url query\\_value:\"walala10.cab\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520query_value%253A%2522walala10.cab%2522/urls)",
    "33-0": "**redirects\\_to:**",
    "33-1": "Identify URLs that redirect to a given URL. This is a fulltext search, meaning that subwords can be used:<br/>Example: [entity:url redirects\\_to:\"login.php\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520redirects_to%253A%2522login.php%2522/urls)",
    "34-0": "**response\\_code:**",
    "34-1": "Filter URLs according to the HTTP status code returned by the server.<br/>Example: [entity:url response\\_code:200 path:\"gate.php\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520response_code%253A200%2520path%253A%2522gate.php%2522/urls)",
    "35-0": "**response\\_positives:**",
    "35-1": "Filter URLs according to the number of antivirus detections for the content that the URL delivers.<br/>Example: [entity:url positives:0 response\\_positives:10+](https://www.virustotal.com/gui/search/entity%253Aurl%2520positives%253A0%2520response_positives%253A10%252B/urls)",
    "36-0": "**response\\_size:**",
    "36-1": "Filter URLs according to the size of the content returned, in bytes.<br/>Example: [entity:url response\\_code:200 response\\_size:1000000+](https://www.virustotal.com/gui/search/entity%253Aurl%2520response_code%253A200%2520response_size%253A1000000%252B/urls)",
    "37-0": "**scheme:**",
    "37-1": "Filter URLs according to their protocol scheme.<br/>Example: [entity:url scheme:https response\\_code:200 path:”gate.php”](https://www.virustotal.com/gui/search/entity%253Aurl%2520scheme%253Ahttps%2520response_code%253A200%2520path%253A%2522gate.php%2522/urls)",
    "38-0": "**title:**",
    "38-1": "Filter URLs according to the title tag contained in their HTML response, if any. Can be used to identify phishing against particular entities.<br/>Example: [entity:url title:\"NAB Personal Banking\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520title%253A%2522NAB%2520Personal%2520Banking%2522/urls)",
    "39-0": "**tld:**",
    "39-1": "Filter URLs according to their top level domain.<br/>Example: [entity:url tld:ru path:\"gate.php\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520tld%253Aru%2520path%253A%2522gate.php%2522/urls)",
    "40-0": "**tracker:**",
    "40-1": "Focus on URLs sharing a given ads tracker in their HTML bodies.<br/>Example: [entity:url tracker:\"15015754\"](https://www.virustotal.com/gui/search/entity:url%20tracker:%2215015754%22/urls)",
    "41-0": "**url:**",
    "41-1": "Filter URLs according to subwords contained in the URL string. <br/>Example: [entity:url url:bankofamerica NOT hostname:bankofamerica](https://www.virustotal.com/gui/search/entity%253Aurl%2520url%253Abankofamerica%2520NOT%2520hostname%253Abankofamerica/urls)",
    "42-0": "**username:**",
    "42-1": "Filter URLs according to the URI username portion.<br/> Example: [entity:url username:anonymous](https://www.virustotal.com/gui/search/entity%253Aurl%2520username%253Aanonymous/urls)",
    "43-0": "**have:**",
    "43-1": "Allows you to impose a condition that the URL’s indexed metadata should meet, it accepts any of the modifiers above and it means that the URL should have data for a given modifier.<br/>Example: [entity:url p:3+ have:tracker](https://www.virustotal.com/gui/search/entity%253Aurl%2520p%253A3%252B%2520have%253Atracker/urls)",
    "44-0": "**parent\\_domain:**",
    "44-1": "Filter URLs based on the parent Domain.<br/>Example:[entity:url parent\\_domain:dropbox.com](https://www.virustotal.com/gui/search/entity%253Aurl%2520parent_domain%253Adropbox.com/urls)",
    "45-0": "**threat\\_actor**<br/>**related_actor**",
    "45-1": "Filter URLs which have that related threat actor. <br/>Example: [entity:url threat\\_actor:\"Lazarus Group\"](https://www.virustotal.com/gui/search/entity%253Aurl%2520threat_actor%253A%2522Lazarus%2520Group%2522/urls)",
    "46-0": "**targeted\\_brand**",
    "46-1": "Filter URLs based on info extracted from phishing engines. <br/>Example: [entity:url targeted\\_brand:apple](https://www.virustotal.com/gui/search/entity%253Aurl%2520targeted_brand%253Aapple?type=urls)"
  },
  "cols": 2,
  "rows": 47,
  "align": [
    null,
    null
  ]
}
[/block]