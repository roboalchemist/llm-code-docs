# Source: https://virustotal.readme.io/docs/virustotal-intelligence-introduction.md

# VirusTotal Intelligence Introduction

# How to perform file searches

***

VirusTotal Intelligence allows you to search through our dataset in order to identify files that match certain criteria (hash, antivirus detections, metadata, submission file names, file format structural properties, file size, etc.). We could say that it is pretty much like the "Google" of malware.

In order to ease the use of the application we have classified the search queries and modifiers into the following categories:

[Retrieving files by hash](#retrieving-files-by-hash)\
[Search Operators](#search-operators)\
[Example Use Cases](#example-use-cases)\
[Identifying files according to antivirus detections](https://virustotal.readme.io/docs/list-file-engines)\
[Search modifiers](https://virustotal.readme.io/docs/search-modifiers-full-list)\
[Content search (VTGrep)](https://virustotal.readme.io/docs/vtgrep)\
[File similarity search](https://virustotal.readme.io/docs/file-similarity-search)\
[URL search modifiers](https://virustotal.readme.io/docs/url-search-modifiers)\
[Domain search modifiers](https://virustotal.readme.io/docs/domain-search-modifiers)\
[IP address search modifiers](https://virustotal.readme.io/docs/ip-address-search-modifiers)\
[Results reports](https://virustotal.readme.io/docs/results-reports)

We also provided a script for [Batch file downloads](https://virustotal.readme.io/docs/batch-file-downloads) and some [Example use cases](#example-use-cases).

# Tiers

***

| Summary                    | Standard tiers                      | Threat Hunter PRO                  |
| -------------------------- | ----------------------------------- | ---------------------------------- |
| Hash lookups               | Till the beginning of times         | Till the beginning of times        |
| Advanced searching         | 90 days                             | 1 year                             |
| Retrohunt                  | 90 days (Up to 10K matches per job) | 1 year (Up to 10K matches per job) |
| Content searching (VTGREP) | 90 days                             | 1 year                             |

# Retrieving files by hash

***

To search for a file that has a given md5, sha1 or sha256 just type in the hash under consideration in the main [search box](https://www.virustotal.com/gui/home/search). Example, searching for the file with sha256: [142b638c6a60b60c7f9928da4fb85a5a8e1422a9ffdc9ee49e17e56ccca9cf6e](https://www.virustotal.com/gui/file/142b638c6a60b60c7f9928da4fb85a5a8e1422a9ffdc9ee49e17e56ccca9cf6e/detection).

![VirusTotal Intelligence hash search](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/intelligenceintroduction_hashsearch_20231110.png)

If you have a list of hashes (e.g. exported from some other application), with independence of the type of hash (md5, sha1 or sha256) and whether they are mixed, and you want to search for all of them at the same time you should refer to the search box feature at the main landing site. You just have to paste your hashes and press enter.

![VirusTotal Intelligence multiple hashes search](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/intelligenceintroduction_multiplehashes_20231110.png)

[Back to Top](#top)

# Search operators

***

All of the previous search modalities and search modifiers can be combined through the use of search operators. The query language supports some Boolean operators as well as parentheses for grouping parts of the query together. The supported Boolean operators are **AND, OR, and NOT**.

By default, when you create queries that match multiple fields at the same time, each value is combined with a Boolean AND. For the query as a whole to match, all the specified values must match.

*Note that operators can't be combined with direct hash (single or multiple) searches, for that you can use an [API script](https://docs.virustotal.com/reference/overview) to get all the reports and then filter by the modifiers.*

## AND Boolean operator

To search for all those PDFs that have and invalid XREF table have two options. We can just ignore the use of any boolean operator since by default search modifiers are concatenated via ANDs:

```
type:pdf tag:invalid-xref
```

## AND Boolean operator

Another option is to explicitely introduce the AND operator:

```
type:pdf AND tag:invalid-xref
```

## OR Boolean operator

We might be interested in retrieving all files that are either DLLs or executables, the OR operator can help us with this task:

```
type:pedll OR type:peexe
```

## NOT Boolean operator

Just as an example, let us use the NOT boolean operator to find all those Portable Executables identified by at least one antivirus vendor with the family name "zbot" and not being tagged as corrupt (i.e. are malformed and will not execute in a real system):

```
engines:zbot NOT tag:corrupt
```

## Parentheses for grouping parts

More complex queries can be built via the use of parenthesis. Let us extend the previous query also to identify other banking malware variants:

```
(engines:zbot OR engines:sinowal) NOT (tag:corrupt)
```

[Back to Top](#top)

# Example use cases

***

This section details some common searches users have asked for in the past, they serve just as examples to illustrate how all of the info provided in the previous sections glues together.

## Studying malicious PDFs

Some academics have used VirusTotal in the past to research malicious PDFs and develop new detection approaches. An example of this research is the [Static Detection of Malicious JavaScript-Bearing PDF Documents](http://134.2.173.143/laskov/papers/acsac2011.pdf)paper by fellows of the University of Tübingen.

In order to try to extract a study base of malicious PDFs from VirusTotal the first idea that comes to our minds is to do something as simple as:

```
type:pdf positives:5+
```

But this is not the only thing you can do. Very often PDFs with exploits will have an invalid XREF table, hence, it also makes sense to do something along the lines of:

```
type:pdf tag:invalid-xref
```

Other tags can also be combined to retrieve juicy PDFs, for example, let us get all those PDFs that contain JavScript and contains an automatic action (perhaps to launch the previous JavaScript):

```
type:pdf tag:autoaction tag:js-embedded
```

Even easier, there is a specific tag for exploits (whenever we have enough indications is or contains an exploit), so let us just make use of it:

```
type:pdf tag:exploit
```

## Retrieving exploit samples

The last example of the previous study case ended with the simplest form of searching for exploits:

```
tag:exploit
```

Even more interesting is the fact that you can search for samples tagged with specific Common Vulnerability and Exposure (CVE) identifiers:

```
tag:cve-2012-0158
```

## Identifying potential false positives

A false positive is another way of saying "mistake". As applied to the field of antivirus programs, a false positive occurs when an antivirus program mistakenly flags an innocent file as being malicious. This may seem harmless enough, but false positives can be a real nuisance.

VirusTotal can be used to identify potential false positives. For example, very often signed Portable Executables with a low number of detections will be a false positive (although not always). Let us just suppose we are interested in retrieving false positives by Symantec, we can do something along the lines of:

```
tag:signed positives:3- symantec:infected
```

These are most probably files that we want to check twice to verify that they are indeed malicious.

Solitary detections can also be sometimes potential false positives (although not always):

```
positives:1 symantec:infected
```

We surely also want to look at all those files that are either in the National Software Reference Library or an online reputed software collection and are being detected:

```
(tag:nsrl OR tag:software-collection) AND symantec:infected AND positives:10-
```

The number of unique sources that sent a given file to VirusTotal can also be a good indicator of whether a given file is innocuous. Very often, the files that are extremely widespread are benign in nature (although not always):

```
sources:2000+ symantec:infected
```

If you are interested in receiving further information regarding some study case of your own please do not hesitate to [contact us](https://www.virustotal.com/gui/contact-us/premium-services).

## Results Report

In the results report page you have different options:

![VirusTotal Intelligence search result](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/intelligenceintroduction_searchresult_20231110.png)

1. You can see the numbers of resources matching that search.

2. You can sort the results by: First seen, last seen, Ratio, Submissions or Size.

3. You can copy the hashes to clipboard and you can download a selection of them.

4. Different Tools depending on the resource type: Send to VT Diff, Open in VT Graph or Calculate commonalities.

5. Links to related documentation.

[Back to Top](#top)