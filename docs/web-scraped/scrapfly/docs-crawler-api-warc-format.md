# Source: https://scrapfly.io/docs/crawler-api/warc-format

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/crawler-api/warc-format

Markdown Content:
WARC Format Reference
---------------------

The WARC (Web ARChive) format is an industry-standard file format for archiving web content. Scrapfly Crawler API uses WARC files to provide you with complete, archival-quality snapshots of your crawled data.

[What is WARC?](https://scrapfly.io/docs/crawler-api/warc-format#what-is-warc)
------------------------------------------------------------------------------

WARC (Web ARChive) is an ISO standard (ISO 28500:2017) for archiving web content. It captures complete HTTP request/response pairs, including headers, status codes, and response bodies.

### Key Benefits

*   **Complete Data** - Captures full HTTP transactions (request + response)
*   **Industry Standard** - Universally supported by archival and analysis tools
*   **Compressed Storage** - Gzip compression for efficient storage
*   **Offline Processing** - Query and analyze data without API calls
*   **Long-term Archival** - Format designed for preservation
*   **Tool Ecosystem** - Many libraries and tools available

[WARC File Structure](https://scrapfly.io/docs/crawler-api/warc-format#file-structure)
--------------------------------------------------------------------------------------

A WARC file contains a series of **records**. Each record has:

*   **WARC Headers** - Metadata about the record (record type, IDs, timestamps)
*   **HTTP Headers** - HTTP request or response headers (if applicable)
*   **Payload** - The actual content (HTML, JSON, binary data, etc.)

### Record Types

| Record Type | Description | Content |
| --- | --- | --- |
| `warcinfo` | File metadata and crawl information | Crawler version, settings, timestamps |
| `request` | HTTP request sent to the server | Request method, URL, headers, body |
| `response` | HTTP response received from server | Status code, headers, response body (HTML, JSON, etc.) |
| `conversion` | Extracted/converted content | Markdown, text, or clean HTML extracted from response |

In addition to standard WARC headers, Scrapfly adds custom metadata to help you analyze and process your crawled data more effectively.

### Custom Headers for All Records

| Header | Type | Description |
| --- | --- | --- |
| `WARC-Scrape-Log-Id` | String | Unique identifier for the scraping log entry. Use this to: * Track individual page scrapes * Look up detailed logs in dashboard * Cross-reference with billing data |
| `WARC-Scrape-Country` | String (ISO 3166) | ISO 3166-1 alpha-2 country code of the proxy used (e.g., `US`, `GB`, `FR`). Useful for analyzing geo-specific content variations. |

### Custom Headers for Response Records

| Header | Type | Description |
| --- | --- | --- |
| `WARC-Scrape-Duration` | Float (seconds) | Time taken to complete the HTTP request in seconds (e.g., `1.234`). Useful for performance analysis and identifying slow pages. |
| `WARC-Scrape-Retry` | Integer | Number of retry attempts for this request (`0` means first attempt succeeded). Helps identify problematic URLs that required retries. |

### Example WARC Record with Custom Headers

```
WARC/1.0
WARC-Type: response
WARC-Record-ID: 
WARC-Date: 2025-01-15T10:30:45Z
WARC-Target-URI: https://web-scraping.dev/products/page/1
Content-Type: application/http; msgtype=response
Content-Length: 15234

# Custom Scrapfly Headers
WARC-Scrape-Log-Id: abcd1234-5678-90ef-ghij-klmnopqrstuv
WARC-Scrape-Country: US
WARC-Scrape-Duration: 1.234
WARC-Scrape-Retry: 0

HTTP/2.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 15000
Date: Wed, 15 Jan 2025 10:30:45 GMT

...
```

[Downloading WARC Files](https://scrapfly.io/docs/crawler-api/warc-format#downloading)
--------------------------------------------------------------------------------------

WARC files are available once your crawler completes (`is_finished: true`).

`curl https://api.scrapfly.io/crawl/{crawler_uuid}/artifact?key=&type=warc -o crawl.warc.gz`

The file is returned as `crawl.warc.gz` (gzip-compressed for efficient transfer).

[Reading WARC Files](https://scrapfly.io/docs/crawler-api/warc-format#reading-tools)
------------------------------------------------------------------------------------

WARC files can be read using various tools and libraries in different programming languages.

### Python - warcio Library

[warcio](https://github.com/webrecorder/warcio) is the recommended Python library for reading WARC files.

#### Installation

`pip install warcio`

#### Reading WARC Files

```
import gzip
from warcio.archiveiterator import ArchiveIterator

# Open and decompress WARC file
with gzip.open('crawl.warc.gz', 'rb') as warc_file:
    # Iterate through all records
    for record in ArchiveIterator(warc_file):
        # Get record type
        record_type = record.rec_type

        # Get WARC headers
        warc_headers = record.rec_headers

        # Access standard WARC headers
        record_id = warc_headers.get_header('WARC-Record-ID')
        target_uri = warc_headers.get_header('WARC-Target-URI')
        date = warc_headers.get_header('WARC-Date')

        # Access Scrapfly custom headers
        log_id = warc_headers.get_header('WARC-Scrape-Log-Id')
        country = warc_headers.get_header('WARC-Scrape-Country')
        duration = warc_headers.get_header('WARC-Scrape-Duration')
        retry = warc_headers.get_header('WARC-Scrape-Retry')

        # Read record content
        content = record.content_stream().read()

        # Process different record types
        if record_type == 'response':
            # Get HTTP status code
            http_headers = record.http_headers
            status = http_headers.get_statuscode()

            print(f"URL: {target_uri}")
            print(f"Status: {status}")
            print(f"Country: {country}")
            print(f"Duration: {duration}s")
            print(f"Log ID: {log_id}")
            print(f"Content length: {len(content)} bytes")
            print("---")

        elif record_type == 'conversion':
            # Extracted content (markdown, text, etc.)
            content_type = warc_headers.get_header('Content-Type')
            print(f"Conversion: {content_type}")
            print(f"Refers to: {warc_headers.get_header('WARC-Refers-To')}")
```

#### Filtering Specific Records

```
import gzip
from warcio.archiveiterator import ArchiveIterator

with gzip.open('crawl.warc.gz', 'rb') as warc_file:
    for record in ArchiveIterator(warc_file):
        # Only process successful responses
        if record.rec_type == 'response':
            status = record.http_headers.get_statuscode()

            if status == '200':
                url = record.rec_headers.get_header('WARC-Target-URI')
                content = record.content_stream().read()

                # Process successful page
                print(f"Processing: {url}")
                # ... your processing logic here
```

### JavaScript/Node.js - node-warc

[node-warc](https://github.com/N0taN3rd/node-warc) provides WARC parsing for Node.js applications.

#### Installation

`npm install node-warc`

#### Reading WARC Files

```
const WARCStreamTransform = require('node-warc');
const fs = require('fs');
const zlib = require('zlib');

// Create gunzip and WARC parser streams
const gunzip = zlib.createGunzip();
const parser = new WARCStreamTransform();

// Read compressed WARC file
fs.createReadStream('crawl.warc.gz')
    .pipe(gunzip)
    .pipe(parser)
    .on('data', (record) => {
        const recordType = record.warcType;
        const targetURI = record.warcTargetURI;

        // Access custom Scrapfly headers
        const logId = record.warcHeader('WARC-Scrape-Log-Id');
        const country = record.warcHeader('WARC-Scrape-Country');
        const duration = record.warcHeader('WARC-Scrape-Duration');

        if (recordType === 'response') {
            console.log(`URL: ${targetURI}`);
            console.log(`Country: ${country}`);
            console.log(`Duration: ${duration}s`);

            // Access HTTP headers
            const statusCode = record.httpHeaders.statusCode;
            const contentType = record.httpHeaders.headers.get('content-type');

            // Get response body
            const content = record.content.toString('utf8');
        }
    })
    .on('end', () => {
        console.log('Finished reading WARC file');
    });
```

### Java - jwat

[JWAT](https://github.com/netarchivesuite/jwat) is a Java library for reading and writing WARC files.

#### Maven Dependency

```
org.jwat
    jwat-warc
    1.1.1
```

#### Reading WARC Files

```
import org.jwat.warc.*;
import java.io.*;
import java.util.zip.GZIPInputStream;

public class WarcReader {
    public static void main(String[] args) throws IOException {
        // Open compressed WARC file
        FileInputStream fis = new FileInputStream("crawl.warc.gz");
        GZIPInputStream gzis = new GZIPInputStream(fis);

        // Create WARC reader
        WarcReader reader = WarcReaderFactory.getReader(gzis);
        WarcRecord record;

        // Iterate through records
        while ((record = reader.getNextRecord()) != null) {
            // Get WARC headers
            WarcHeader header = record.header;
            String recordType = header.warcTypeStr;
            String targetUri = header.warcTargetUriStr;

            // Access custom Scrapfly headers
            String logId = header.getHeader("WARC-Scrape-Log-Id").value;
            String country = header.getHeader("WARC-Scrape-Country").value;

            if ("response".equals(recordType)) {
                // Get HTTP status
                HttpHeader httpHeader = record.getHttpHeader();
                String statusCode = httpHeader.statusCode;

                System.out.println("URL: " + targetUri);
                System.out.println("Status: " + statusCode);
                System.out.println("Country: " + country);
            }

            record.close();
        }

        reader.close();
    }
}
```

### Go - go-warc

[gowarc](https://github.com/nlnwa/gowarc) is a Go library for reading and writing WARC files.

#### Installation

`go get github.com/nlnwa/gowarc`

#### Reading WARC Files

```
package main

import (
    "compress/gzip"
    "fmt"
    "github.com/nlnwa/gowarc"
    "os"
)

func main() {
    // Open compressed WARC file
    f, err := os.Open("crawl.warc.gz")
    if err != nil {
        panic(err)
    }
    defer f.close()

    // Decompress
    gz, err := gzip.NewReader(f)
    if err != nil {
        panic(err)
    }
    defer gz.Close()

    // Create WARC reader
    reader := gowarc.NewReader(gz)

    // Iterate through records
    for {
        record, err := reader.Next()
        if err != nil {
            break
        }

        // Get WARC headers
        recordType := record.Type()
        targetURI := record.WarcHeader().Get("WARC-Target-URI")

        // Access custom Scrapfly headers
        logID := record.WarcHeader().Get("WARC-Scrape-Log-Id")
        country := record.WarcHeader().Get("WARC-Scrape-Country")
        duration := record.WarcHeader().Get("WARC-Scrape-Duration")

        if recordType == gowarc.Response {
            fmt.Printf("URL: %s\n", targetURI)
            fmt.Printf("Country: %s\n", country)
            fmt.Printf("Duration: %ss\n", duration)
        }
    }
}
```

### Rust - warc_parser

[warc_parser](https://github.com/commoncrawl/warc_parser) is a high-performance Rust library for reading WARC files, originally developed for Common Crawl.

#### Installation

```
# Add to Cargo.toml
[dependencies]
warc_parser = "2.0"
flate2 = "1.0"  # For gzip decompression
```

#### Reading WARC Files

```
use std::fs::File;
use std::io::{BufReader, Read};
use flate2::read::GzDecoder;
use warc_parser::{WarcReader, RecordType};

fn main() -> Result<(), Box> {
    // Open compressed WARC file
    let file = File::open("crawl.warc.gz")?;
    let gz = GzDecoder::new(file);
    let buf_reader = BufReader::new(gz);

    // Create WARC reader
    let mut warc_reader = WarcReader::new(buf_reader);

    // Iterate through records
    while let Some(record) = warc_reader.next_item()? {
        // Get WARC headers
        let headers = &record.warc_headers;

        // Access standard WARC headers
        let record_type = headers.get("WARC-Type");
        let target_uri = headers.get("WARC-Target-URI");
        let record_id = headers.get("WARC-Record-ID");

        // Access Scrapfly custom headers
        let log_id = headers.get("WARC-Scrape-Log-Id");
        let country = headers.get("WARC-Scrape-Country");
        let duration = headers.get("WARC-Scrape-Duration");
        let retry = headers.get("WARC-Scrape-Retry");

        // Read record body
        let body = record.body;

        // Process different record types
        if record_type == Some("response") {
            println!("URL: {:?}", target_uri);
            println!("Country: {:?}", country);
            println!("Duration: {:?}s", duration);
            println!("Log ID: {:?}", log_id);
            println!("Body size: {} bytes", body.len());
            println!("---");
        }
    }

    Ok(())
}
```

#### Performance Filtering

Rust\'s performance makes it ideal for processing large WARC archives efficiently.

```
use std::fs::File;
use std::io::BufReader;
use flate2::read::GzDecoder;
use warc_parser::WarcReader;

fn main() -> Result<(), Box> {
    let file = File::open("crawl.warc.gz")?;
    let gz = GzDecoder::new(file);
    let buf_reader = BufReader::new(gz);
    let mut warc_reader = WarcReader::new(buf_reader);

    let mut success_count = 0;
    let mut error_count = 0;

    while let Some(record) = warc_reader.next_item()? {
        let headers = &record.warc_headers;

        if headers.get("WARC-Type") == Some("response") {
            // Parse HTTP status from body (simplified)
            let body_str = String::from_utf8_lossy(&record.body);

            if body_str.contains("HTTP/1.1 200") || body_str.contains("HTTP/2 200") {
                success_count += 1;

                // Process successful responses
                let url = headers.get("WARC-Target-URI").unwrap_or("");
                let country = headers.get("WARC-Scrape-Country").unwrap_or("unknown");

                println!("✓ {} (from {})", url, country);
            } else {
                error_count += 1;
            }
        }
    }

    println!("\nStats:");
    println!("  Successful: {}", success_count);
    println!("  Errors: {}", error_count);

    Ok(())
}
```

### C++ - warcpp

[warcpp](https://github.com/pisa-engine/warcpp) is a single-header C++ parser for WARC files with modern error handling using std::variant.

#### Installation

```
git clone https://github.com/pisa-engine/warcpp.git
cd warcpp
mkdir build && cd build
cmake ..
make
```

#### Reading WARC Files

```
#include 
#include 
#include 
#include 

using warcpp::match;
using warcpp::Record;
using warcpp::Error;

int main() {
    // Open compressed WARC file
    std::ifstream file("crawl.warc.gz", std::ios::binary);

    // Process records with pattern matching
    while (file) {
        auto result = warcpp::read_subsequent_record(file);

        match(
            result,
            [](const Record& record) {
                // Access WARC headers
                auto warc_type = record.header("WARC-Type");
                auto target_uri = record.header("WARC-Target-URI");
                auto record_id = record.header("WARC-Record-ID");

                // Access Scrapfly custom headers
                auto log_id = record.header("WARC-Scrape-Log-Id");
                auto country = record.header("WARC-Scrape-Country");
                auto duration = record.header("WARC-Scrape-Duration");
                auto retry = record.header("WARC-Scrape-Retry");

                if (warc_type == "response") {
                    std::cout << "URL: " << target_uri << std::endl;
                    std::cout << "Country: " << country << std::endl;
                    std::cout << "Duration: " << duration << "s" << std::endl;
                    std::cout << "Log ID: " << log_id << std::endl;
                    std::cout << "Content length: " << record.content_length() << " bytes" << std::endl;
                    std::cout << "---" << std::endl;
                }
            },
            [](const Error& err) {
                // Handle parsing errors
                std::cerr << "Error reading record" << std::endl;
            }
        );
    }

    return 0;
}
```

#### Efficient Error Handling

warcpp uses std::variant for type-safe error handling without exceptions.

```
#include 
#include 

int main() {
    std::ifstream file("crawl.warc.gz", std::ios::binary);

    // Extract specific data with error handling
    auto size = match(
        warcpp::read_subsequent_record(file),
        [](const Record& rec) {
            // Successfully read record
            return rec.content_length();
        },
        [](const Error& err) {
            // Error occurred, return default
            return 0u;
        }
    );

    std::cout << "Record size: " << size << " bytes" << std::endl;
    return 0;
}
```

### PHP - Mixnode WARC Reader

[mixnode-warcreader-php](https://github.com/Mixnode/mixnode-warcreader-php) provides native PHP support for reading WARC files, both raw and gzipped.

#### Installation

`composer require mixnode/mixnode-warcreader-php`

#### Reading WARC Files

```
nextRecord()) !== FALSE) {
    // Access WARC headers
    $headers = $record['header'];
    $content = $record['content'];

    // Get standard WARC fields
    $warc_type = $headers['WARC-Type'] ?? null;
    $target_uri = $headers['WARC-Target-URI'] ?? null;
    $record_id = $headers['WARC-Record-ID'] ?? null;

    // Access Scrapfly custom headers
    $log_id = $headers['WARC-Scrape-Log-Id'] ?? null;
    $country = $headers['WARC-Scrape-Country'] ?? null;
    $duration = $headers['WARC-Scrape-Duration'] ?? null;
    $retry = $headers['WARC-Scrape-Retry'] ?? null;

    // Process response records
    if ($warc_type === 'response') {
        echo "URL: $target_uri\n";
        echo "Country: $country\n";
        echo "Duration: {$duration}s\n";
        echo "Log ID: $log_id\n";
        echo "Content size: " . strlen($content) . " bytes\n";
        echo "---\n";
    }
}
```

#### Filtering Specific Records

```
nextRecord()) !== FALSE) {
    $headers = $record['header'];
    $content = $record['content'];

    // Only process responses
    if (($headers['WARC-Type'] ?? null) === 'response') {
        // Check HTTP status in content
        if (preg_match('/^HTTP\/[12](?:\.[01])? (\d{3})/', $content, $matches)) {
            $status_code = (int)$matches[1];

            if ($status_code === 200) {
                $successful_urls[] = [
                    'url' => $headers['WARC-Target-URI'] ?? null,
                    'country' => $headers['WARC-Scrape-Country'] ?? null,
                    'duration' => $headers['WARC-Scrape-Duration'] ?? null,
                ];
            } else {
                $error_count++;
            }
        }
    }
}

echo "Found " . count($successful_urls) . " successful requests\n";
echo "Errors: $error_count\n";

// Process successful URLs
foreach ($successful_urls as $url_data) {
    echo "✓ {$url_data['url']} (from {$url_data['country']})\n";
}
```

### Command-Line Tools

#### warcio (Python CLI)

Extract and inspect WARC files from the command line.

```
# Install warcio
pip install warcio

# List all records
warcio index crawl.warc.gz

# Extract all HTML responses
warcio extract --type response crawl.warc.gz > responses.txt

# Filter by URL pattern
warcio index crawl.warc.gz | grep "products"
```

#### zgrep - Search Compressed WARC

Search for specific content without decompressing.

```
# Search for specific URL
zgrep "WARC-Target-URI: https://web-scraping.dev" crawl.warc.gz

# Search for specific log ID
zgrep "WARC-Scrape-Log-Id: abc123" crawl.warc.gz

# Search for requests from specific country
zgrep "WARC-Scrape-Country: US" crawl.warc.gz
```

#### gunzip - Decompress WARC

```
# Decompress WARC file
gunzip crawl.warc.gz

# Now you have crawl.warc (uncompressed)
# Can use standard text tools like grep, awk, etc.
grep "WARC-Type: response" crawl.warc
```

[Common Use Cases](https://scrapfly.io/docs/crawler-api/warc-format#use-cases)
------------------------------------------------------------------------------

##### Long-term Archival

Store complete snapshots of websites for historical preservation, compliance, or research purposes using an industry-standard format.

##### Offline Analysis

Download once and analyze locally without additional API calls. Perfect for data science, ML training sets, or bulk processing.

##### Performance Monitoring

Use `WARC-Scrape-Duration` and `WARC-Scrape-Retry` to identify slow pages, analyze performance patterns, and optimize crawling strategies.

##### Geo-specific Analysis

Compare content variations across regions using `WARC-Scrape-Country`. Analyze geo-blocking, localized pricing, or regional content differences.

[Converting WARC to Parquet](https://scrapfly.io/docs/crawler-api/warc-format#warc-to-parquet)
----------------------------------------------------------------------------------------------

Convert WARC archives to Apache Parquet format for efficient querying, analytics, and long-term storage. Parquet's columnar format with bloom filter indexing enables lightning-fast URL lookups and SQL-based analysis.

### Python Implementation with Bloom Filters

This example converts WARC to Parquet with bloom filter indexing on URLs for fast lookups.

#### Installation

`pip install warcio pyarrow pandas`

#### Conversion Script

```
import gzip
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from warcio.archiveiterator import ArchiveIterator
from datetime import datetime

def warc_to_parquet(warc_path, parquet_path):
    """
    Convert WARC to Parquet with bloom filter on URL column.

    Bloom filters enable O(1) URL lookups - perfect for checking
    if a specific URL exists without reading the entire file.
    """
    records = []

    with gzip.open(warc_path, 'rb') as warc_file:
        for record in ArchiveIterator(warc_file):
            # Only process response records
            if record.rec_type != 'response':
                continue

            headers = record.rec_headers
            http_headers = record.http_headers

            # Extract data into columnar format
            row = {
                # Standard WARC fields
                'url': headers.get_header('WARC-Target-URI'),
                'record_id': headers.get_header('WARC-Record-ID'),
                'date': headers.get_header('WARC-Date'),

                # HTTP response data
                'status_code': int(http_headers.get_statuscode()) if http_headers else None,
                'content_type': http_headers.get_header('Content-Type') if http_headers else None,
                'content_length': len(record.content_stream().read()),

                # Scrapfly custom headers
                'log_id': headers.get_header('WARC-Scrape-Log-Id'),
                'country': headers.get_header('WARC-Scrape-Country'),
                'duration': float(headers.get_header('WARC-Scrape-Duration', 0)),
                'retry_count': int(headers.get_header('WARC-Scrape-Retry', 0)),
            }

            records.append(row)

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Define schema with optimized types
    schema = pa.schema([
        ('url', pa.string()),
        ('record_id', pa.string()),
        ('date', pa.timestamp('us')),
        ('status_code', pa.int16()),  # Smaller int for status codes
        ('content_type', pa.string()),
        ('content_length', pa.int32()),
        ('log_id', pa.string()),
        ('country', pa.string()),
        ('duration', pa.float32()),  # 32-bit sufficient for duration
        ('retry_count', pa.int8()),   # Very small int
    ])

    # Convert DataFrame to PyArrow Table
    table = pa.Table.from_pandas(df, schema=schema)

    # Write Parquet with bloom filter on URL column
    pq.write_table(
        table,
        parquet_path,
        compression='zstd',  # Better compression than gzip
        compression_level=9,
        # Enable bloom filter for O(1) URL lookups
        bloom_filter_columns=['url'],
        # Enable statistics for query optimization
        write_statistics=True,
        # Row group size affects query performance
        row_group_size=100000,
    )

    print(f"Converted {len(records)} records to {parquet_path}")
    print(f"Bloom filter enabled on 'url' column for fast lookups")

# Usage
warc_to_parquet('crawl.warc.gz', 'crawl.parquet')
```

#### Querying Parquet with DuckDB

Once converted to Parquet, you can query your crawl data with SQL. Bloom filters make URL lookups instant, even on multi-GB files.

```
import duckdb

# Connect to DuckDB (in-memory)
con = duckdb.connect()

# Fast URL lookup using bloom filter
result = con.execute("""
    SELECT url, status_code, country, duration
    FROM read_parquet('crawl.parquet')
    WHERE url = 'https://web-scraping.dev/products/1'
""").fetchall()

print("Exact URL match:", result)

# Analytics queries - leveraging columnar format
stats = con.execute("""
    SELECT
        country,
        COUNT(*) as total_requests,
        AVG(duration) as avg_duration,
        COUNT(CASE WHEN status_code = 200 THEN 1 END) as success_count
    FROM read_parquet('crawl.parquet')
    GROUP BY country
    ORDER BY total_requests DESC
""").df()

print("\nStats by country:")
print(stats)

# Find slow requests (queries are FAST thanks to columnar format)
slow_requests = con.execute("""
    SELECT url, duration, retry_count, country
    FROM read_parquet('crawl.parquet')
    WHERE duration > 5.0
    ORDER BY duration DESC
    LIMIT 10
""").df()

print("\nSlowest requests:")
print(slow_requests)
```

#### Partitioning for Large Crawls

For crawls with millions of URLs, partition by date or country for even faster queries.

```
import pyarrow.dataset as ds

# Write partitioned dataset (by country and date)
df['date'] = pd.to_datetime(df['date'])
df['partition_date'] = df['date'].dt.date

# Convert to PyArrow table
table = pa.Table.from_pandas(df)

# Write partitioned dataset
ds.write_dataset(
    table,
    'crawl_partitioned/',
    format='parquet',
    partitioning=['country', 'partition_date'],
    # Bloom filters on each partition
    parquet_writer_kwargs={
        'compression': 'zstd',
        'bloom_filter_columns': ['url'],
    }
)

# Query specific partition (only reads relevant files)
import duckdb
con = duckdb.connect()

us_results = con.execute("""
    SELECT url, status_code, duration
    FROM read_parquet('crawl_partitioned/country=US/**/*.parquet')
    WHERE status_code = 200
""").df()

print(f"Found {len(us_results)} successful US requests")
```

[Best Practices](https://scrapfly.io/docs/crawler-api/warc-format#best-practices)
---------------------------------------------------------------------------------

**Keep files compressed**

Use `.warc.gz` for storage efficiency (10x+ compression)

**Use streaming readers**

Process large files without loading into memory

**Index `WARC-Scrape-Log-Id`**

For fast lookups and cross-referencing

**Store original WARC files**

For audit trails and reprocessing

**Leverage custom headers**

For analytics and debugging

**Don't load entire files into memory**

Use streaming iterators instead

**Remember to decompress**

Use `gzip.open` before reading

**Multiple records per URL**

WARC files may contain retries and redirects

**Custom headers are optional**

Check for `None` before using

[Next Steps](https://scrapfly.io/docs/crawler-api/warc-format#next-steps)
-------------------------------------------------------------------------

*   Learn about [all retrieval methods](https://scrapfly.io/docs/crawler-api/results) available for crawler results
*   Understand [crawler billing](https://scrapfly.io/docs/crawler-api/billing) and how WARC downloads are charged
*   Explore [crawler configuration options](https://scrapfly.io/docs/crawler-api/getting-started)
*   View the complete [crawler API specification](https://scrapfly.io/docs/crawler-api/getting-started#spec)

[External Resources](https://scrapfly.io/docs/crawler-api/warc-format#external-resources)
-----------------------------------------------------------------------------------------

*   [ISO 28500:2017 WARC Standard](https://www.iso.org/standard/68004.html) - Official WARC specification 
*   [warcio (Python)](https://github.com/webrecorder/warcio) - Recommended Python library 
*   [node-warc (JavaScript)](https://github.com/N0taN3rd/node-warc) - Node.js WARC library 
*   [JWAT (Java)](https://github.com/netarchivesuite/jwat) - Java WARC library 
*   [gowarc (Go)](https://github.com/nlnwa/gowarc) - Go WARC library
