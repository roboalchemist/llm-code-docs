# arXiv API User's Manual

## Preface

The arXiv API User's Manual serves both beginning and advanced users seeking to understand API functionality, with examples in multiple programming languages.

## Overview

The arXiv API enables programmatic access to hundreds of thousands of e-prints hosted on arXiv.org. The API returns results in Atom 1.0 XML format.

## 1. API QuickStart

The simplest API call searches for articles:

```text
http://export.arxiv.org/api/query?search_query=all:electron
```

Complex searches combine terms with Boolean operators:

```text
http://export.arxiv.org/api/query?search_query=all:electron+AND+all:proton
```

## 2. Structure of the API

### 2.1 Calling the API

Base URL format:

```text
http://export.arxiv.org/api/{method_name}?{parameters}
```

#### Query Parameters

- `search_query` (string, optional): Search query for finding articles
- `id_list` (comma-delimited, optional): List of arXiv IDs
- `start` (integer, default 0): First result index (0-based)
- `max_results` (integer, default 10): Number of results returned

#### Parameter Logic

- Only `search_query`: returns matching articles
- Only `id_list`: returns specified articles
- Both parameters: returns articles in `id_list` matching `search_query`

### 2.1.2 Paging

Results are paginated using `start` and `max_results`:

```text
http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10
http://export.arxiv.org/api/query?search_query=all:electron&start=10&max_results=10
```

#### Important Constraints

- Maximum `max_results` per request: 2,000
- Maximum total retrievable: 30,000 results
- Requests exceeding 30,000 return HTTP 400 error
- Recommended delay between calls: 3 seconds
- Results cached daily; no benefit to calling multiple times

### 2.1.3 Sorting

Two sorting parameters available:

`sortBy` options:

- "relevance" (default, Apache Lucene RELEVANCE ordering)
- "lastUpdatedDate"
- "submittedDate"

`sortOrder` options:

- "ascending"
- "descending"

Example:

```text
http://export.arxiv.org/api/query?search_query=ti:"electron thermal conductivity"&sortBy=lastUpdatedDate&sortOrder=ascending
```

### 2.2 API Response

All responses return Atom 1.0 XML format, including errors. Responses include feed-level metadata and entry-level article information.

### 2.3 Atom Feed Structure

#### 2.3.1 Feed Metadata

XML Declaration and Namespace:

```xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
```

Key Feed Elements:

- `<title>`: Canonicalized query representation
- `<id>`: Unique identifier for the query
- `<link>`: URL to retrieve feed via GET
- `<updated>`: Last update time (midnight of current day)

OpenSearch Extension Elements:

- `<opensearch:totalResults>`: Total number of results
- `<opensearch:startIndex>`: 0-based index of first result
- `<opensearch:itemsPerPage>`: Number returned

#### 2.3.2 Entry Metadata

**Article Identification:**

- `<title>`: Article title
- `<id>`: URL to abstract page (format: `http://arxiv.org/abs/{arxiv_id}`)
- `<published>`: Submission date of version 1
- `<updated>`: Submission date of retrieved version

**Article Content:**

- `<summary>`: Abstract text
- `<author>`: One element per author with `<name>` subelement
- `<category>`: Classification tags (arXiv, ACM, or MSC schemes)

**Links:**

Three possible `<link>` elements distinguished by `rel` and `title`:

| rel | title | refers to | always present |
|-----|-------|-----------|-----------------|
| alternate | — | abstract page | yes |
| related | pdf | PDF file | yes |
| related | doi | resolved DOI | no |

**arXiv Extension Elements:**

- `<arxiv:primary_category>`: Primary subject classification
- `<arxiv:comment>`: Author comments
- `<arxiv:affiliation>`: Author affiliation (subelement of `<author>`)
- `<arxiv:journal_ref>`: Journal publication reference
- `<arxiv:doi>`: DOI identifier

### 2.4 Errors

Errors return as Atom feeds with single error entry. The `<summary>` contains error message; `<link>` provides detailed explanation.

Common Error Conditions:

- `start` must be integer ≥ 0
- `max_results` must be integer ≥ 0
- Malformed arXiv IDs rejected
- Invalid date formats cause parsing errors

## 3. Programming Examples

### 3.1 Simple Examples

#### Perl (using LWP)

```perl
use LWP;
my $url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1';
my $browser = LWP::UserAgent->new();
my $response = $browser->get($url);
print $response->content();
```

#### Python 3 (using urllib)

```python
import urllib.request as libreq
with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
    r = url.read()
print(r)
```

#### Ruby (using net/http)

```ruby
require 'net/http'
require 'uri'
url = URI.parse('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1')
res = Net::HTTP.get_response(url)
print res.body
```

#### PHP (using file_get_contents)

```php
<?php
$url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1';
$response = file_get_contents($url);
print_r($response);
?>
```

### 3.2 Detailed Parsing Libraries

| Language | Library | Features |
|----------|---------|----------|
| Perl | XML::Atom | Atom parsing |
| Python | feedparser | Feed parsing |
| Ruby | feedtools | Feed parsing |
| PHP | SimplePie | Feed parsing |

## 4. Appendices

### 4.1 Query Construction Details

#### Field Search Prefixes

| prefix | explanation |
|--------|-------------|
| ti | Title |
| au | Author |
| abs | Abstract |
| co | Comment |
| jr | Journal Reference |
| cat | Subject Category |
| rn | Report Number |
| id | arXiv ID |
| all | All fields |

#### Search Examples

Find articles by author Adrian Del Maestro:

```text
http://export.arxiv.org/api/query?search_query=au:del_maestro
```

Date filtering using `submittedDate`:

```text
https://export.arxiv.org/api/query?search_query=au:del_maestro+AND+submittedDate:[202301010600+TO+202401010600]
```

#### Boolean Operators

- `AND`: Both conditions required
- `OR`: Either condition acceptable
- `ANDNOT`: Exclude results matching condition

#### Grouping

- Parentheses: `%28` for `(`, `%29` for `)`
- Phrase searching: `%22` for quotation marks
- Spaces: `+` in URLs

Example with grouping:

```text
http://export.arxiv.org/api/query?search_query=au:del_maestro+ANDNOT+%28ti:checkerboard+OR+ti:Pyrochlore%29
```

#### 4.1.1 Article Versions

Each article has version numbers (starting at 1). To retrieve:

- Latest version: use ID without version suffix
- Specific version: append `v{n}` to ID

Examples:

```text
http://export.arxiv.org/api/query?id_list=cond-mat/0207270        (latest)
http://export.arxiv.org/api/query?id_list=cond-mat/0207270v1      (version 1)
```

### 4.2 Atom Elements Reference

**Feed-Level Elements:**

- `<title>`: Canonicalized query
- `<id>`: Unique query identifier
- `<updated>`: Midnight of current day
- `<link>`: Retrievable URL
- `<opensearch:totalResults>`: Total matching articles
- `<opensearch:startIndex>`: First result index
- `<opensearch:itemsPerPage>`: Results returned

**Entry-Level Elements:**

- `<title>`: Article title
- `<id>`: Abstract page URL
- `<published>`: Version 1 submission date
- `<updated>`: Retrieved version submission date
- `<summary>`: Abstract
- `<author>`: Author information
- `<link>`: Associated URLs
- `<category>`: Classification
- `<arxiv:primary_category>`: Primary classification
- `<arxiv:comment>`: Author comments
- `<arxiv:affiliation>`: Author affiliation
- `<arxiv:journal_ref>`: Journal reference
- `<arxiv:doi>`: DOI identifier

### 4.3 Subject Classifications

Complete arXiv subject classifications available at the taxonomy page.

## Important Notes

- Review Terms of Use for arXiv APIs before using
- Results cached daily; no benefit calling multiple times same day
- Feed readers can subscribe to custom API queries
- For bulk harvesting, OAI-PMH interface more suitable
- HTML interface sorts by submission date descending; API sorts by relevance
