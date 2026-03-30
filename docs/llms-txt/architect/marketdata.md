# Source: https://docs.architect.co/sdk-reference/marketdata.md

# Marketdata

* [Marketdata](#marketdata)
  * [Get market status](#get-market-status)
  * [Get ticker](#get-ticker)
  * [Get L1 book snapshot](#get-l1-book-snapshot)
  * [Stream L1 book snapshots](#stream-l1-book-snapshots)
  * [Subscribe to L1 book](#subscribe-to-l1-book)
  * [Get L2 book snapshot](#get-l2-book-snapshot)
  * [Stream L2 book updates](#stream-l2-book-updates)
    * [Applying diffs](#applying-diffs)
    * [Sequence numbers](#sequence-numbers)
  * [Subscribe to L2 book](#subscribe-to-l2-book)
  * [Stream trades](#stream-trades)
  * [Stream candles (klines)](#stream-candles-klines)
    * [Streaming candles availability and request limits](#streaming-candles-availability-and-request-limits)
  * [Get historical candles](#get-historical-candles)
    * [Historical candles availability and request limits](#historical-candles-availability-and-request-limits)

## Get market status

Get the market status for a symbol and venue, e.g. if it's currently quoting or trading.

{% tabs %}
{% tab title="Python" %}

```python
status = await client.get_market_status(
    symbol="BTC Crypto/USD",
    venue="COINBASE"
)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::MarketStatus;

let status: MarketStatus = client.get_market_status("BTC Crypto/USD", "COINBASE").await?;
```

{% endtab %}

{% tab title="Example JSON response" %}

```json5
{
  "s": "BTC Crypto/USD",  // symbol
  "is_quoting": true,
  "is_trading": true
}
```

{% endtab %}
{% endtabs %}

## Get ticker

Get a marketdata ticker for a symbol and venue. Tickers include basic summary statistics like volumes, open interest, settlement price, as well as slowly changing dimensions e.g. dividend yields, P/E ratios, market caps for equities.

{% tabs %}
{% tab title="Python" %}

```python
ticker = await client.get_ticker(
    symbol="AAPL US Equity/USD",
    venue="US-EQUITIES"
)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::Ticker;

let ticker: Ticker = client.get_ticker("AAPL US Equity/USD", "US-EQUITIES").await?;
```

{% endtab %}
{% endtabs %}

## Get L1 book snapshot

{% tabs %}
{% tab title="Python" %}

```python
snap = await client.get_l1_book_snapshot(
    symbol="GC 20250626 CME Future/USD",
    venue="CME"
)

# get multiple snapshots
snaps = await client.get_l1_book_snapshots(
    symbols=["GC 20250626 CME Future/USD", "ES 20250620 CME Future/USD"],
    venue="CME"
)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::L1BookSnapshot;

let snap: L1BookSnapshot = client.get_l1_book_snapshot(
    "GC 20250626 CME Future/USD",
    "CME"
).await?;

// get multiple snapshots
let snaps: Vec<L1BookSnapshot> = client.get_l1_book_snapshots(
    &[
        "GC 20250626 CME Future/USD",
        "ES 20250620 CME Future/USD"
    ],
    "CME"
).await?;
```

{% endtab %}

{% tab title="Example JSON response" %}

```json5
{
  "s": "GC 20250626 CME Future/USD",  // symbol
  "tn": 710661000,                    // timestamp (seconds since epoch)
  "ts": 1747336563,                   // nanoseconds part of timestamp
  "a": ["3227.500000000", "3"],       // ask price and size
  "b": ["3227.200000000", "3"]        // bid price and size
}
```

{% endtab %}
{% endtabs %}

## Stream L1 book snapshots

Stream L1 book snapshots for the given symbols, for the given venue.

{% tabs %}
{% tab title="Python" %}

```python
async for snap in client.stream_l1_book_snapshots(
    symbols=["BTC Crypto/USD"], 
    venue="COINBASE"
):
    print(snap)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::L1BookSnapshot;
use futures::StreamExt;

let mut stream = client.stream_l1_book_snapshots(&["BTC Crypto/USD"], "COINBASE", false).await?;
while let Some(item) = stream.next().await {
    let snap: L1BookSnapshot = item?;
}
```

{% endtab %}
{% endtabs %}

## Subscribe to L1 book

Subscribe to the L1 book for a symbol and venue in a background task. The current state of the book is available anytime via the returned reference. Calling subscribe again for the same symbol and venue will return the same reference. Call the unsubscribe method to terminate the subscription.

{% tabs %}
{% tab title="Python" %}

```python
book = await client.subscribe_l1_book(
    symbol="BTC Crypto/USD",
    venue="COINBASE"
)

# ...
await client.unsubscribe_l1_book(
    symbol="BTC Crypto/USD",
    venue="COINBASE"
)
```

{% endtab %}
{% endtabs %}

## Get L2 book snapshot

{% tabs %}
{% tab title="Python" %}

```python
book = await client.get_l2_book_snapshot(
    symbol="GC 20250626 CME Future/USD",
    venue="CME"
)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::L2BookSnapshot;

let book: L2BookSnapshot = client.get_l2_book_snapshot("GC 20250626 CME Future/USD", "CME").await?;
```

{% endtab %}

{% tab title="Example JSON response" %}

```json5
{
  "sid": 14673246569842529083,  // sequence id
  "sn": 3722556,                // sequence number
  "tn": 710661000,              // timestamp (seconds since epoch)
  "ts": 1747336563,             // nanoseconds part of timestamp
  "a": [                        // asks (price, size)
    ["3228.600000000", "2"],
    ["3228.700000000", "6"],
    ["3228.800000000", "6"],
    // ...
  ],
  "b": [                        // bids (price, size)
    ["3227.200000000", "3"],
    // ...
  ]
}
```

{% endtab %}
{% endtabs %}

## Stream L2 book updates

Stream L2 book updates for a given symbol and venue. This is a diff stream; the first message will contain a full snapshot, and subsequent messages represent diffs to be applied successively to maintain the state of the book.

{% tabs %}
{% tab title="Python" %}

```python
from architect_py import L2BookSnapshot, L2BookDiff

async for update in client.stream_l2_book_updates(
    symbol="BTC Crypto/USD",
    venue="COINBASE"
):
    if isinstance(update, L2BookSnapshot):
        print(update)
    elif isinstance(update, L2BookDiff):
        print(update)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::L2BookUpdate;
use futures::StreamExt;

let mut stream = client.stream_l2_book_updates("BTC Crypto/USD", "COINBASE").await?;

while let Some(item) = stream.next().await {
    let up = item?;
    match up {
        L2BookUpdate::Snapshot(snap) => {},
        L2BookUpdate::Diff(diff) => {}
    }
}
```

{% endtab %}
{% endtabs %}

### Applying diffs

For each diff message, a price level with non-zero quantity indicates that that price level should be updated to the stated quantity. A price level with a quantity of zero indicates that the price level should be removed from the book.

### Sequence numbers

Sequence numbers are monotonically increasing integers that are assigned to each message. They can be used to detect gaps in the stream. From the first snapshot, each diff message should have a sequence number that is exactly one greater than the sequence number of the last received update.

Additionally, messages include a sequence ID field. Sequence IDs must be the same for all updates in a stream; if the sequence ID is observed to change, diff updates are no longer valid and the subscription should be restarted with a new snapshot.

## Subscribe to L2 book

Subscribe to and maintain an L2 book for a given symbol and venue in a background task. The current state of the book is available anytime via the returned reference. Calling subscribe again for the same symbol and venue will return the same reference.

{% tabs %}
{% tab title="Python" %}

```python
book = await client.subscribe_l2_book(
    symbol="BTC Crypto/USD",
    venue="COINBASE"
)
```

{% endtab %}
{% endtabs %}

## Stream trades

Stream the latest trades for a given symbol and venue.

{% tabs %}
{% tab title="Python" %}

```python
async for trade in client.stream_trades(
    symbol="BTC Crypto/USD",
    venue="COINBASE"
):
    print(trade)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::Trade;
use futures::StreamExt;

let mut stream = client.stream_trades(Some("BTC Crypto/USD"), "CME").await?;

while let Some(item) = stream.next().await {
    let trade: Trade = item?;
}
```

{% endtab %}

{% tab title="Example JSON response" %}

```json5
{
  "s": "BTC Crypto/USD",  // symbol
  "tn": 710661000,        // timestamp (seconds since epoch)
  "ts": 1747336563,       // nanoseconds part of timestamp
  "p": "3227.200000000",  // price
  "q": "3",               // size
  "d": "BUY"              // trade direction or side 
}
```

{% endtab %}
{% endtabs %}

## Stream candles (klines)

Candles are produced at different fixed periods and include the open, high, low, close, and volumes for that period. Not all exchange feeds produce all candle widths.

{% tabs %}
{% tab title="Python" %}

```python
from architect_py import CandleWidth

stream = client.stream_candles(
  symbol="BTC Crypto/USD", 
  venue="COINBASE",
  candle_widths=[CandleWidth.OneSecond]
)

async for candle in stream:
    print(candle)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::{Candle, CandleWidth};
use futures::StreamExt;

let mut stream = client.stream_candles(
    "BTC Crypto/USD",
    "COINBASE",
    Some(&[CandleWidth::OneSecond])
).await?;

while let Some(item) = stream.next().await {
    let candle: Candle = item?;
}
```

{% endtab %}
{% endtabs %}

### Streaming candles availability and request limits

<table><thead><tr><th width="154.92578125">Venue</th><th>Available candle widths for streaming</th></tr></thead><tbody><tr><td>CME</td><td>1s, 1h, 15m, 1h, 1d</td></tr><tr><td>CFE</td><td>1s, 1h, 15m, 1h, 1d</td></tr><tr><td>US-EQUITIES</td><td></td></tr></tbody></table>

## Get historical candles

Retrieve historical candles for a symbol and venue.

{% tabs %}
{% tab title="Python" %}

```python
from architect_py import CandleWidth
from datetime import datetime, timedelta, timezone

candles = await client.get_historical_candles(
    symbol="GC 20250428 CME Future/USD",
    venue="CME",
    candle_width=CandleWidth.OneHour,
    start=datetime.now(timezone.utc) - timedelta(days=1),
    end=datetime.now(timezone.utc)
    # pass as_dataframe=True to return a pandas DataFrame
)
```

{% endtab %}

{% tab title="Rust" %}

```rust
use architect_api::marketdata::{Candle, CandleWidth};
use chrono::{Utc, Duration};

let now = Utc::now();
let candles: Vec<Candle> = client.get_historical_candles(
    "GC 20250428 CME Future/USD",
    "CME",
    CandleWidth::OneHour,
    now - Duration::hours(12),
    now 
).await?;
```

{% endtab %}

{% tab title="Example JSON response" %}

```json5
{
  "s": "GC 20250626 CME Future/USD", // symbol
  "w": 3600,                         // width
  "tn": 0,                           // timestamp (seconds since epoch)
  "ts": 1747292400,                  // nanoseconds part of timestamp
  "v": "14029",                      // volume
  "av": "6767",                      // ask volume
  "bv": "6748",                      // bid volume
  "o": "3153.500000000",             // open price
  "h": "3155.500000000",             // high price
  "l": "3134.200000000",             // low price
  "c": "3145.400000000",             // close price
  "ao": "3153.500000000",            // ask open price
  "ah": "3155.600000000",            // ask high price
  "al": "3134.300000000",            // ask low price
  "ac": "3145.400000000",            // ask close price
  "bo": "3153.200000000",            // bid open price
  "bh": "3155.400000000",            // bid high price
  "bl": "3134.000000000",            // bid low price
  "bc": "3145.100000000",            // bid close price
  "mo": "3153.3500000000",           // mid price
  "mh": "3155.5000000000",           // mid high price
  "ml": "3134.1500000000",           // mid low price
  "mc": "3145.2500000000",           // mid close price
}
```

{% endtab %}
{% endtabs %}

### Historical candles availability and request limits

<table><thead><tr><th width="119.26171875">Candle width</th><th>Maximum allowed start/end timespan in one request</th></tr></thead><tbody><tr><td>1s</td><td>8 hours</td></tr><tr><td>5s</td><td>1 day</td></tr><tr><td>1m</td><td>7 days</td></tr><tr><td>15m</td><td>90 days</td></tr><tr><td>1h</td><td>365 days (~1 year)</td></tr><tr><td>1d</td><td>3650 days (~10 years)</td></tr></tbody></table>

<table><thead><tr><th width="146.44921875">Venue</th><th>Earliest available data</th><th>Latest available data</th></tr></thead><tbody><tr><td>CME</td><td></td><td></td></tr><tr><td>CFE</td><td></td><td></td></tr><tr><td>US-EQUITIES</td><td></td><td></td></tr></tbody></table>
