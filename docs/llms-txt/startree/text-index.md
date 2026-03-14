# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/text-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Index (Lucene)

> The Text index (Lucene) enhances complex text search capabilities by enabling efficient phrase matching, regex, and prefix searches on large text fields.

## Overview and Purpose

Pinot supports super-fast query processing through its indexes on non-BLOB like columns. Queries with exact match filters are run efficiently through a combination of dictionary encoding, inverted index, and sorted index.

This is useful for a query like the following, which looks for exact matches on two columns of type STRING and INT respectively:

```javascript  theme={null}
SELECT COUNT(*) 
FROM Foo 
WHERE STRING_COL = 'ABCDCD' 
AND INT_COL > 2000
```

For arbitrary text data that falls into the BLOB/CLOB territory, we need more than exact matches. This often involves using regex, phrase, fuzzy queries on BLOB like data. Text indexes can efficiently perform arbitrary search on STRING columns where each column value is a large BLOB of text using the `TEXT_MATCH` function, like this:

```javascript  theme={null}
SELECT COUNT(*) 
FROM Foo 
WHERE TEXT_MATCH (<column_name>, '<search_expression>')
```

where `<column_name>` is the column text index is created on and `<search_expression>` conforms to one of the following:

| **Search Expression Type** | **Example**                                                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Phrase query               | TEXT\_MATCH (\<column\_name>, '"distributed system"')                                                                                      |
| Term Query                 | TEXT\_MATCH (\<column\_name>, 'Java')                                                                                                      |
| Boolean Query              | TEXT\_MATCH (\<column\_name>, 'Java AND c++')                                                                                              |
| Prefix Query               | TEXT\_MATCH (\<column\_name>, 'stream\*')                                                                                                  |
| Regex Query                | TEXT\_MATCH (\<column\_name>, '/Exception.\*/')                                                                                            |
| Not Query                  | TEXT\_MATCH (\<column\_name>, '*\*:\** NOT c%')                                                    NOT TEXT\_MATCH (\<column\_name>, 'c%') |

A text index is a specialized data structure that enables efficient text search operations on large text data stored in STRING columns. Unlike traditional indexes that support exact matches or range queries, text indexes facilitate complex text search capabilities including phrase matching, term queries, regex patterns, and prefix searches.

In StarTree Cloud (powered by Apache Pinot), the text index bridges the gap between structured query processing and text search functionality. It allows users to perform flexible search operations on text data that would otherwise require expensive full table scans and string manipulations.

Text indexes are particularly valuable for:

* Log analysis where each log entry contains large chunks of text
* Document search across free-form text fields
* Search across JSON blobs stored as strings
* Any use case involving queries on large text values where exact matching is insufficient

<Info>
  Text indexes provide significant performance benefits for search operations on STRING columns containing large text values (BLOB/CLOB-like data) that don't fit the pattern of dictionary-encoded exact matches.
</Info>

## How the Index Works

### Core Concepts

Traditional indexing approaches in Pinot (dictionary encoding, inverted index, sorted index) excel at exact match and range queries but are inefficient for complex text search operations on large text values.

The text index in StarTree Cloud:

1. **Text Processing Pipeline**: During indexing, each text value is processed through a pipeline that includes:
   * Tokenization: Breaking the text into individual terms
   * Stop word removal: Filtering out common words with low search value
   * Term normalization: Converting terms to a standard form
2. **Inverted Index Creation**: An inverted index is built that maps terms to the documents containing them, enabling fast lookup.
3. **Query Processing**: At query time, search expressions are analyzed and used to efficiently locate matching documents without full table scans.

### Example Illustration

Consider a column containing Apache access logs where each row stores an entire log entry:

```
109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
```

Without a text index:

* To find all log entries containing "Firefox", the system would need to scan every row and check if the string "Firefox" appears in the text.

With a text index:

* During indexing, the log entry is tokenized into terms including "Firefox"
* The term "Firefox" is linked to the documents containing it
* At query time, the system can directly retrieve the rows containing "Firefox" without scanning all data

This approach significantly improves query performance for text search operations, especially on large datasets.

## **Enable a per-column text index**

Enable a text index on a column in the [table configuration](https://docs.pinot.apache.org/configuration-reference/table) by adding a new section with the name "fieldConfigList".

```json  theme={null}
"fieldConfigList":[
  {
     "name":"text_col_1",
     "encodingType":"RAW",
     "indexTypes":["TEXT"]
  },
  {
     "name":"text_col_2",
     "encodingType":"RAW",
     "indexTypes":["TEXT"]
  }
]
```

Each column that has a text index should also be specified as `noDictionaryColumns` in `tableIndexConfig`:

```json  theme={null}
"tableIndexConfig": {
   "noDictionaryColumns": [
     "text_col_1",
     "text_col_2"
 ]}
```

You can configure text indexes in the following scenarios:

* Adding a new table with text index enabled on one or more columns.
* Adding a new column with text index enabled to an existing table.
* Enabling a text index on an existing column.

### Important Configuration Considerations

1. **Column Requirements**:
   * The column must be of type STRING
   * The column must be single-valued (not multi-valued)
   * The column should use RAW encoding (no dictionary)
2. **noDictionaryColumns**: Text-indexed columns should be added to the noDictionaryColumns list in tableIndexConfig to reduce storage overhead.
3. **Index Coexistence**: Using a text index in coexistence with other Pinot indexes on the same column is not supported.

### Customizing Stop Words

You can customize the stop words used during indexing:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "log_content",
      "encodingType": "RAW",
      "indexes": {
        "text": {}
      },
      "properties": {
        "stopWordInclude": "incl1, incl2, incl3",
        "stopWordExclude": "it"
      }
    }
  ]
}
```

* **stopWordInclude**: Comma-separated list of words to include as stop words (in addition to defaults)
* **stopWordExclude**: Comma-separated list of words to exclude from the default stop words list

### Enabling Prefix/Suffix Matching in Phrase Queries

For more flexible phrase matching across term boundaries:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "log_content",
      "encodingType": "RAW",
      "indexes": {
        "text": {}
      },
      "properties": {
        "enablePrefixSuffixMatchingInPhraseQueries": "true"
      }
    }
  ]
}
```

### Tuning Lucene Index Creation

For optimizing index creation performance:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "log_content",
      "encodingType": "RAW",
      "indexes": {
        "text": {}
      },
      "properties": {
        "luceneUseCompoundFile": "false",
        "luceneMaxBufferSizeMB": "128"
      }
    }
  ]
}
```

## **TEXT\_MATCH Query Options**

The `TEXT_MATCH` function supports an optional third parameter for specifying Lucene query parser options at query time. This allows for flexible and advanced text search without changing table configuration.

**Function Signature:**

```
TEXT_MATCH(text_column_name, search_expression [, options])
```

* `text_column_name`: Name of the column to perform text search on.
* `search_expression`: The query string for text search.
* `options` (optional): Comma-separated string of key-value pairs to control query parsing and search behavior.

**Available Options:**

| **Option**             | **Values**                                           | **Description**                                                              |
| :--------------------- | :--------------------------------------------------- | :--------------------------------------------------------------------------- |
| `parser`               | `CLASSIC`, `STANDARD`, `COMPLEX, MATCHPHRASE, MATCH` | Selects the Lucene query parser to use. Default is `CLASSIC`.                |
| `allowLeadingWildcard` | `true`, `false`                                      | Allows queries to start with a wildcard (e.g., `*term`). Default is `false`. |
| `defaultOperator`      | `AND`, `OR`                                          | Sets the default boolean operator for multi-term queries. Default is `OR`.   |

**Query Parsers Summary**

| **Parser**          | **Best For**                                                                  |
| :------------------ | :---------------------------------------------------------------------------- |
| `CLASSIC (Default)` | Standard Lucene syntax with wildcards and boolean operators.                  |
| `STANDARD`          | Advanced regex pattern matching and field-specific queries.                   |
| `COMPLEX`           | Enhanced phrase matching that allows wildcards inside quotes.                 |
| `MATCHPHRASE`       | Autocomplete-style phrase search with prefix matching.                        |
| `MATCH`             | Queries requiring a specific number of term matches (minimum\_should\_match). |

### **Parser-Specific Options**

**1. CLASSIC Parser (Default)**

The standard Lucene query parser. It is robust and handles most boolean and wildcard requirements.

**Options Supported:**

* allowLeadingWildcard: (Boolean) Enable to allow queries like \*term. Default: false.
* defaultOperator: (String) Logic between terms if no operator is provided. Values: OR (default), AND.
* analyzeWildcard: (Boolean) Whether to analyze terms within wildcard queries. Default: false.
* fuzzyMinSim: (Float) Minimum similarity for fuzzy matching (\~). Default: 2.0 (edit distance).

**2. STANDARD Parser**

Based on the StandardQueryParser, this is a more flexible and modern parser that supports advanced expressions like regular expressions.

* **Options Supported:**
  * allowLeadingWildcard: (Boolean) Default: false.
  * defaultOperator: (String) Values: OR, AND.

**3. COMPLEX Parser**

Designed for phrase queries that require internal wildcards (e.g., "standard \*index").

* **Options Supported:**
  * allowLeadingWildcard: (Boolean) Default: false.
  * defaultOperator: (String) Values: OR, AND.
  * inOrder: (Boolean) If true, terms in a phrase must appear in the exact order specified. Default: true.

**4. MATCHPHRASE Parser**

A specialized parser for "starts-with" behavior on phrases, often used for search-as-you-type features.

* **Options Supported:**
  * enablePrefixMatch: (Boolean) When true, the last term of the phrase is treated as a prefix. Default: true.
  * slop: (Integer) The number of "jumps" allowed between words in the phrase. Default: 0.

**5. MATCH Parser**

A simplified parser focused on multi-term matching and match quality control.

* **Options Supported:**
  * minimumShouldMatch: (String) Defines how many terms must match for a document to be returned. Supports:
    * Integer: 2 (exactly two terms).
    * Percentage: 75% (at least 75% of terms).
    * Negative: -1 (all but one term).

## **Examples of Advanced Search Patterns**

### **1. Regex Pattern Matching (.\*text.\*)**

For highly specific patterns that go beyond simple wildcards, you can use regular expressions. This requires the STANDARD parser.

```javascript  theme={null}
-- Finds any document containing the sequence "exception" anywhere in a term

SELECT * FROM MyTable 

WHERE TEXT_MATCH(comments, '/.*exception/', 'parser=STANDARD')
```

* **Matches**: "NullPointerException", "Runtime\_exception", "exception\_handler".
* **Note**: Regular expressions are wrapped in forward slashes (/pattern/).

### **2. Field and Anchor Search (^)**

The STANDARD parser allows for more granular control, such as boosting specific terms or using anchors if supported by the underlying analyzer. In Lucene-based searches, the ^ symbol is also frequently used for **Term Boosting**, allowing you to give more weight to certain words.

```javascript  theme={null}
-- Finds "java" or "python", but gives "java" twice the relevance weight

SELECT * FROM MyTable 

WHERE TEXT_MATCH(comments, 'java^2 python', 'parser=STANDARD')
```

### **3. Prefix and Suffix Search**

Find documents containing words that start or end with a specific sequence.

**Prefix (Starts With):**

```javascript  theme={null}
-- Matches "stream", "streaming", "streamed"

SELECT _FROM MyTable WHERE TEXT_MATCH(comments, 'stream_ ', 'parser=CLASSIC')
```

**Suffix (Ends With):**

```javascript  theme={null}
-- Matches "streaming", "processing", "learning"

SELECT * FROM MyTable 

WHERE TEXT_MATCH(comments, '*ing', 'parser=CLASSIC,allowLeadingWildcard=true')
```

### **4. Contains Search**

Find a term regardless of its position or surrounding characters.

```javascript  theme={null}
-- Matches "realtime" anywhere in the text

SELECT * FROM MyTable 

WHERE TEXT_MATCH(comments, '*realtime*', 'parser=CLASSIC,allowLeadingWildcard=true')
```

### **5. Exact Match**

Search for a specific term or a specific phrase in its exact order.

* **Single Term Exact Match:**

```javascript  theme={null}
-- Matches documents containing the word "java"

SELECT * FROM MyTable WHERE TEXT_MATCH(comments, 'java')
```

* **Exact Phrase Match:** Use double quotes within the query string to ensure terms appear together and in order.

```javascript  theme={null}
-- Matches "realtime data processing", but not "data processing realtime"
SELECT * FROM MyTable 
WHERE TEXT_MATCH(comments, '"realtime data processing"', 'parser=CLASSIC')
```

### Other Miscellaneous examples

```javascript  theme={null}
-- Use CLASSIC parser with leading wildcard support
SELECT * FROM myTable WHERE TEXT_MATCH(myCol, '*search*', 'parser=CLASSIC, allowLeadingWildcard=true')

-- Use STANDARD parser with AND operator
SELECT * FROM myTable WHERE TEXT_MATCH(myCol, 'term1 term2', 'parser=STANDARD, defaultOperator=AND')

-- Use COMPLEX parser for advanced queries
SELECT * FROM myTable WHERE TEXT_MATCH(myCol, 'complex query', 'parser=COMPLEX')
```

## **Technical Syntax Reference**

For deep-dive syntax on how to write query\_string expressions (e.g., using \~ for fuzzy, ^ for boosting, or \[] for ranges), please refer to the official[<u>Apache Lucene Query Parser Syntax</u>](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html) .

**Note:** Apache Pinot implements Lucene 8.x/9.x logic. While the core syntax remains the same, advanced field-specific features may behave differently based on your Pinot Table Index configuration.

## **Best Practices**

* **Leading Wildcards**: Using *term is slower than term* because it requires a more intensive index scan.
* **Index Requirement**: TEXT\_MATCH only works with Lucene-based text indexes, not native Pinot text indexes.

**Cluster Configuration for Text Search**

When text search queries contain too many terms or clauses, Lucene may throw `TooManyClauses` exceptions, causing query failures. This commonly occurs with:

* Complex boolean queries with many OR conditions
* Wildcard queries that expand to many terms
* Queries with large numbers of search terms To handle such cases, you can increase the maximum clause count at the cluster level. See the [<u>cluster configuration reference</u>](https://github.com/pinot-contrib/pinot-docs/blob/latest/configuration-reference/cluster.md) for the `pinot.lucene.max.clause.count` setting.

Built with [Mintlify](https://mintlify.com).
