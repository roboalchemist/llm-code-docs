# Popular Date and Time Libraries Across Major Programming Languages (2026)

A comprehensive research document covering the most widely used date and time libraries across JavaScript/TypeScript, Python, Java, Go, Rust, Ruby, PHP, and C#.

---

## JavaScript & TypeScript

### Top Libraries

**1. Moment.js**
- **Status**: Legacy but widely used
- **Description**: A lightweight library for parsing, validating, manipulating, and formatting dates
- **Key Features**:
  - Frequent updates and detailed documentation
  - Extensive plugin ecosystem
  - Good internationalization support
- **Best For**: Projects with legacy dependencies; teams already invested in the ecosystem
- **Considerations**: Industry moving toward modern alternatives due to bundle size concerns

**2. Luxon**
- **Status**: Modern standard
- **Creator**: Created by Moment.js maintainer as the modern replacement
- **Key Features**:
  - Immutable objects (functional programming support)
  - 1-indexed months (more intuitive than Moment's 0-indexed approach)
  - Leverages ECMAScript Internationalization API for localization and timezone
  - Built-in timezone support without bundling timezone data
- **Bundle Size**: Reasonable; integrates with native browser APIs
- **Best For**: Production applications; projects prioritizing correctness and modernity
- **Documentation**: Excellent

**3. Day.js**
- **Status**: Most popular for bundle-size-conscious projects
- **Key Metrics**: Only 2KB minified and gzipped
- **Key Features**:
  - Plugin system for optional features
  - Immutability support
  - API largely compatible with Moment.js for easier migration
  - Exceptional performance
  - Tree-shakeable
- **Best For**: Frontend applications; projects with strict bundle size constraints
- **Use Case**: Projects where every kilobyte matters (mobile, embedded web)

**4. date-fns**
- **Status**: Highly popular, modular-first approach
- **Key Features**:
  - Supports 70+ locales
  - Purely functional library
  - Tree-shakeable: import only needed functions
  - Excellent TypeScript support
  - Immutable by design
- **Bundle Size**: Small when using selective imports
- **Best For**: Functional programming enthusiasts; large applications where modularity matters
- **Documentation**: Comprehensive with excellent examples

**5. Tempo**
- **Status**: Newer tree-shakeable library
- **Key Features**:
  - Designed for handling complex date operations across timezones
  - Works as a collection of utilities for native Date object
  - Uses JavaScript's Intl.DateTimeFormat for timezone and locale support
  - Minimal footprint (~2KB minified and compressed)
  - Modern API design
- **Best For**: Modern TypeScript applications; timezone-heavy operations
- **Documentation**: Growing community support

**6. Spacetime**
- **Status**: Specialized timezone library
- **Key Features**:
  - Handles daylight savings transitions
  - Leap years support
  - Hemispheric awareness (different DST rules by region)
  - Accounts for quarters, seasons, months, weeks
  - Lightweight
- **Best For**: Applications with complex timezone requirements
- **Use Case**: Global scheduling, reporting across timezones

**7. Datejs**
- **Status**: Legacy, minimal maintenance
- **Description**: Open-source wrapper around JavaScript's native Date constructor
- **Limitations**: Limited recent updates
- **Best For**: Beginner projects; educational purposes only
- **Not Recommended**: For production use

---

## Python

### Built-in Standard

**datetime** (Standard Library)
- **Status**: Built-in, recommended standard
- **Implementation**: Written in C for CPython performance
- **Key Classes**:
  - `datetime`: Complete date and time
  - `date`: Date only
  - `time`: Time only
  - `timedelta`: Time intervals
- **Timezone Support**: Basic (requires pytz or zoneinfo)
- **Used By**: Django, Flask, and most Python frameworks
- **Performance**: Baseline (other libraries are typically 2-3x slower)
- **Best For**: Standard library stability; when timezone handling isn't complex

### Third-Party Libraries

**2. python-dateutil**
- **Status**: Industry standard extension
- **Key Features**:
  - Powerful relative datetime parsing
  - Robust timezone support
  - RRuleParser for recurring dates
  - Fuzzy parsing capabilities
- **Use Cases**: Parsing arbitrary date strings; recurring event calculations
- **Integration**: Works seamlessly with datetime module
- **Best For**: Data processing; ETL pipelines; flexible date parsing

**3. pytz**
- **Status**: Standard for timezone handling
- **Key Features**:
  - Comprehensive timezone database (IANA TZ Database)
  - Localization support
  - DST-aware arithmetic
- **Considerations**: Heavy (includes entire timezone database); new Python versions include `zoneinfo`
- **Alternative**: Use `zoneinfo` (built-in, Python 3.9+) instead for new projects
- **Best For**: Legacy applications; complex timezone requirements

**4. Pendulum**
- **Status**: Popular modern alternative
- **Key Features**:
  - Fluent API design
  - Chainable method calls
  - Timezone-aware by default
  - Built-in internationalization
  - Immutable by default
  - Natural language parsing
- **Performance**: Slower than datetime (2-3x overhead)
- **Ecosystem**: Includes testing utilities
- **Best For**: Development-friendly code; projects prioritizing developer experience
- **Documentation**: Excellent with many examples

**5. Arrow**
- **Status**: Popular for simplicity
- **Key Features**:
  - Cleaner API than datetime
  - Timezone manipulation utilities
  - ISO 8601 parsing and formatting
  - `humanize()` for human-readable relative time
  - Excellent for datetime conversions
- **Performance**: Similar slowdown as Pendulum vs datetime
- **Best For**: Web applications; logging; API timestamp handling
- **Community**: Active; well-documented

**6. dateparser**
- **Status**: Specialized parser
- **Purpose**: Parse dates from arbitrary strings
- **Key Features**:
  - Supports 200+ date formats
  - Multi-language parsing
  - Timezone inference
  - Fuzzy matching
- **Best For**: Text processing; user input parsing; data cleaning
- **Not General Purpose**: Use for parsing, not for regular datetime operations

**7. frozengun** (Testing)
- **Status**: Specialized testing utility
- **Purpose**: Mock datetime in tests
- **Key Features**:
  - Freeze time for testing
  - Time travel in tests
  - Decorator and context manager support
- **Best For**: Unit testing; mocking datetime

**8. zoneinfo** (Python 3.9+)
- **Status**: Modern built-in replacement for pytz
- **Key Features**:
  - Part of standard library (IANA TZ Database built-in)
  - Lighter weight than pytz
  - Uses IANA timezone names
- **Recommendation**: Preferred over pytz for new projects (Python 3.9+)
- **Best For**: New projects targeting Python 3.9+

---

## Java

### Built-in Standard

**java.time**
- **Status**: Modern standard (introduced Java 8, 2014)
- **Architecture**: Follows immutable, thread-safe design
- **Key Classes**:
  - `LocalDate`: Date without time
  - `LocalTime`: Time without date
  - `LocalDateTime`: Date and time (no timezone)
  - `ZonedDateTime`: Date and time with timezone
  - `Instant`: Machine timestamp
  - `Duration`: Time interval
  - `Period`: Date interval
- **Timezone Support**: Full IANA timezone support
- **API Design**: Fluent, chainable methods
- **Performance**: Baseline for Java
- **Best For**: All new Java projects; standard choice
- **Documentation**: Extensive (official Java docs)

### Legacy & Alternatives

**2. Joda-Time**
- **Status**: De facto standard before Java 8
- **Current Status**: No longer recommended for new development
- **Why Superseded**: java.time was directly influenced by Joda-Time design
- **Legacy Use**: Older projects may still use this
- **Migration**: Spring and other frameworks have dropped Joda-Time in favor of java.time
- **Best For**: Legacy project maintenance only

**3. ThreeTenBP (Backport)**
- **Status**: Backport of java.time to older Java versions
- **Purpose**: Use java.time API on Java 6 and Java 7
- **Key Features**:
  - Drop-in replacement for java.time
  - Enables java.time usage before Java 8
- **Current Relevance**: Limited (Java 6 and 7 are obsolete)
- **Best For**: Very legacy projects stuck on ancient JVMs
- **Not Recommended**: For new development

**4. Time4J**
- **Status**: Advanced third-party library
- **Key Features**:
  - More granular time handling than java.time
  - Extended calendar systems
  - Complex time calculations
- **Best For**: Niche applications with specialized calendar needs
- **Market Share**: Minimal compared to java.time

---

## Go

### Built-in Standard

**time Package**
- **Status**: Standard library (net/http, databases, all core libs use it)
- **Key Types**:
  - `time.Time`: Point in time with nanosecond precision
  - `time.Duration`: Time interval
  - `time.Location`: Timezone information
- **Timezone Support**: IANA timezone database built-in
- **API**: Unconventional reference time (Mon Jan 2 15:04:05 MST 2006)
- **Performance**: Baseline; efficient
- **Thread Safety**: Immutable; safe for concurrent use
- **Best For**: All Go applications (no practical alternative)
- **Considerations**: Reference time format takes adjustment for new developers

### Third-Party Libraries

**2. dateutil** (Parsing)
- **Status**: Popular for date string parsing
- **Key Features**: Flexible date parsing from various formats
- **Best For**: User input parsing; log file processing

**3. iso8601**
- **Status**: Specialized parser
- **Key Features**: Efficient ISO8601 date-time parsing without regex
- **Best For**: Performance-critical parsing scenarios

**4. kair**
- **Status**: Go date/time formatting library
- **Use Case**: Custom date formatting utilities

**5. now**
- **Status**: Time toolkit for Go
- **Key Features**: Convenience methods for common time operations
- **Best For**: Simplifying time calculations

**Recommendation**: Go's built-in `time` package covers virtually all use cases. Third-party libraries address very specific parsing needs.

---

## Rust

### Popular Crates

**1. Jiff** (Emerging Standard)
- **Status**: Newest library; strong community enthusiasm
- **Repository**: https://github.com/BurntSushi/jiff
- **Key Features**:
  - **Timezone-aware by default**: Stores full geographical timezone information (tzinfo)
  - Safe daylight saving time arithmetic
  - Flexible parsing: Implements FromStr, parses multiple datetime formats with full timezone support
  - ISO 8601 serialization by default
  - Intuitive API design
- **Performance**: Efficient; designed for modern Rust patterns
- **Community Consensus**: Emerging as "clear winner to replace" chrono and time
- **Best For**: New Rust projects; production applications
- **Documentation**: Growing; excellent GitHub documentation

**2. Chrono**
- **Status**: Established standard
- **Key Features**:
  - Mature ecosystem
  - Timezone support through **chrono-tz** companion crate
  - Comprehensive time manipulation
- **Trade-offs**:
  - Embeds entire Time Zone Database in binary (increases binary size)
  - Depends on chrono-tz updates for latest timezone info
  - Less safe DST arithmetic than jiff
- **Market Share**: Historically the go-to library
- **Best For**: Existing projects; established codebase compatibility
- **Considerations**: May be superseded by jiff for new projects

**3. time**
- **Status**: Established but with limitations
- **Version**: 0.3.36 and later
- **Key Features**:
  - Timezone offset-aware datetime (OffsetDateTime)
  - Immutable API
- **Critical Limitation**:
  - `OffsetDateTime` cannot perform daylight saving time safe arithmetic
  - Stores offset only, not timezone rules
  - Loses context about DST transitions
- **Performance**: Efficient
- **Best For**: Simple offset-based needs; when DST isn't a factor
- **Not Recommended**: For applications with complex timezone requirements

**4. chrono-tz**
- **Status**: Companion to chrono
- **Purpose**: Provides full IANA timezone database for chrono
- **Trade-off**: Binary bloat (entire TZ database embedded)
- **Best For**: Chrono users who need timezone support

**5. dayjs** (Port)
- **Status**: Rust port of JavaScript library
- **Ecosystem**: Limited compared to native Rust options
- **Best For**: Developers familiar with JavaScript date handling

---

## Ruby

### Built-in Standard Classes

**1. Time** (Recommended)
- **Status**: Primary choice for modern Ruby
- **Key Features**:
  - Represents specific moment in time
  - Microsecond precision
  - Handles time zones correctly
  - More efficient than DateTime
- **Performance**: Best among the three core classes
- **Best For**: Current timestamps, logging, most applications
- **Rails Integration**: Works well with Rails conventions
- **Recommendation**: **Use this for virtually all new code**

**2. Date**
- **Status**: Lightweight specialized class
- **Key Features**:
  - Represents calendar dates only
  - No time component
  - Lower overhead than Time
- **Best For**: When only date information needed (birthdays, anniversaries)
- **Explicitly Required**: May need `require 'date'` in some contexts

**3. DateTime** (Legacy)
- **Status**: Older approach; generally discouraged
- **Key Features**:
  - Combines date and time
  - Fractional second precision
  - Supports fractional days for arithmetic
  - Extensive date range (4712 BCE to 9999 CE)
- **Drawbacks**:
  - Significantly slower than Time
  - More complex than needed for most use cases
- **Best For**: Historical date calculations, edge cases with fractional day precision
- **Not Recommended**: For modern development

### Framework Integration

**4. ActiveSupport** (Rails)
- **Status**: Rails extension library
- **Key Enhancements**:
  - `before?` and `after?` comparison methods
  - Chainable duration methods
  - Readable time zones
  - Human-readable relative time
- **Integration**: Makes date/time comparisons and operations more intuitive in Rails
- **Best For**: Rails applications
- **Examples**:
  ```ruby
  Time.now.before?(Time.now + 1.hour)
  1.day.ago
  2.weeks.from_now
  ```

**5. Chronic** (Parser)
- **Status**: Natural language date parsing
- **Key Features**: Parses human-readable date strings ("tomorrow", "next Friday")
- **Best For**: User-facing date input parsing
- **Considerations**: Less accurate than structured parsing

---

## PHP

### Built-in Standard

**DateTime**
- **Status**: Native PHP solution
- **Key Features**:
  - Combines date and time
  - Timezone support
  - Formatting and parsing
- **Limitations**:
  - Unintuitive behaviors (adding months uses "day-exact" rather than "month-exact")
  - Mutable by default (error-prone)
  - Verbose syntax
- **Best For**: Minimal projects; when dependencies should be avoided
- **Not Recommended**: For production apps requiring clarity and safety

### Third-Party Libraries

**2. Carbon** (Most Popular)
- **Status**: Industry standard for PHP
- **Created By**: Brian Nesbit
- **Key Features**:
  - Extends PHP's DateTime class
  - Creates dates with intuitive methods: `create()`, `createFromDate()`
  - Add/subtract operations: `addDays()`, `subtractDays()`, etc.
  - Human-readable time differences: `diffForHumans()` ("2 hours ago")
  - Extensive formatting options
- **API Design**: Developer-friendly, chainable
- **Best For**: Web applications, Laravel ecosystem
- **Market Share**: Dominant in PHP ecosystem
- **Documentation**: Excellent; widely used
- **Integration**: Works with Eloquent ORM, Laravel built-in

**3. Chronos** (Modern Alternative)
- **Status**: Modern, zero-dependency library
- **Created By**: CakePHP team
- **Key Differences from Carbon**:
  - **Immutable by default** (extends DateTimeImmutable)
  - Separate classes for specific needs: `ChronosDate`, `ChronosTime`
  - Better performance for creating many instances
  - Fixes PHP core inconsistencies (proper month-exact addition)
- **Architecture**: More robust for functional programming
- **Best For**: Projects prioritizing immutability; performance-critical operations
- **Comparison to Carbon**:
  - Chronos: Safer, immutable, modern architecture
  - Carbon: More popular, broader ecosystem, slightly more verbose
- **Documentation**: Comprehensive CakePHP documentation

---

## C# / .NET

### Built-in Types

**1. DateTime**
- **Status**: Primary built-in type
- **Key Characteristics**:
  - Value type (struct); immutable
  - Allows arithmetic operations
  - Flexible formatting options
  - Date comparisons
- **Critical Limitation**: **Does NOT store timezone information**
  - Only represents a "local" moment without context
  - Causes problems in multi-timezone systems
- **Performance**: Excellent (baseline)
- **Best For**: Simple scenarios; when timezone handling isn't needed
- **Not Recommended**: For production code in distributed systems

**2. DateTimeOffset** (Recommended)
- **Status**: Preferred for most applications
- **Key Features**:
  - Stores both local date/time AND UTC offset
  - Immutable; value type
  - Solves the timezone problem with DateTime
  - Recommended as default choice
- **Use Cases**: All production applications; API timestamps
- **Recommendation**: **Use this instead of DateTime for virtually all code**
- **Performance**: Minimal overhead vs DateTime

**3. TimeZoneInfo**
- **Status**: Represent any timezone on Earth
- **Purpose**: Timezone conversion between zones
- **Key Features**:
  - IANA timezone database
  - DST handling
  - Conversion methods
- **Best For**: Complex timezone operations
- **Integration**: Works with DateTime and DateTimeOffset

**4. TimeSpan**
- **Status**: Time interval representation
- **Purpose**: Duration calculations; time arithmetic
- **Key Features**:
  - Represents elapsed time
  - Can be negative (past intervals)
  - Arithmetic operations
- **Use Cases**: Measuring elapsed time; timeout calculations

**5. DateOnly** & **TimeOnly** (Modern)
- **Status**: Introduced in .NET 6
- **Purpose**: Store date-only or time-only values
- **Key Features**:
  - Solves problem of DateTime always containing both components
  - Type-safe separation
  - Immutable
- **Best For**: APIs; database schemas; models with date-only fields
- **Recommendation**: Use when your domain needs only one component

### Third-Party Alternatives

**6. NodaTime**
- **Status**: Significant third-party library
- **Purpose**: Advanced date/time handling beyond .NET built-ins
- **Key Use Cases**: Complex calendar systems; specialized datetime logic
- **Current Relevance**: Reduced since .NET added DateOnly and TimeOnly (which were inspired by NodaTime)
- **Best For**: Very specialized requirements; extensive datetime logic
- **Market Share**: Niche; most projects use built-in types

---

## Summary Comparison Table

| Language | Standard/Primary | Modern Alternative | Bundle Size Concern? | Best Feature |
|----------|------------------|-------------------|----------------------|--------------|
| **JS/TS** | Moment.js (legacy) | Day.js, date-fns, Luxon | Yes (critical) | Tree-shakeable modularity |
| **Python** | datetime (stdlib) | Pendulum, Arrow | No | Fluent API; timezone awareness |
| **Java** | java.time | None needed | No | Immutable; comprehensive |
| **Go** | time (stdlib) | Specialized parsers | No | IANA TZ built-in; efficient |
| **Rust** | Jiff (emerging) | chrono, time | No | Safe DST arithmetic |
| **Ruby** | Time | None needed | No | Simple, performant |
| **PHP** | DateTime (stdlib) | Carbon (standard choice) | No | Human-friendly API |
| **C#** | DateTimeOffset | NodaTime (niche) | No | Timezone-aware by default |

---

## Industry Trends & Recommendations (2026)

### Migration Patterns
1. **JavaScript**: Moving away from Moment.js to Day.js/date-fns for new projects
2. **Python**: Legacy projects use pytz; new projects use zoneinfo + datetime
3. **Rust**: Jiff gaining momentum as replacement for chrono/time
4. **PHP**: Carbon dominance; Chronos growing for immutability-first projects

### Key Considerations
- **Timezone Handling**: Critical for distributed systems; prioritize libraries with full IANA support
- **Bundle Size**: JavaScript/TypeScript remains the primary concern (use Day.js, not Moment.js)
- **Immutability**: Modern languages prefer immutable designs (Luxon, date-fns, Pendulum, Jiff, Chronos)
- **Performance**: Built-in standards generally outperform third-party libraries by 2-3x
- **API Design**: Fluent/chainable methods increasingly expected (Arrow, Carbon, Luxon)

### Documentation Availability
All libraries listed have substantial documentation available:
- Official websites with comprehensive guides
- GitHub repositories with README documentation
- Tutorials and blog posts
- Integration guides for popular frameworks
- API reference documentation

---

## Research Sources

### JavaScript/TypeScript
- https://phrase.com/blog/posts/best-javascript-date-time-libraries/
- https://betterstack.com/community/guides/scaling-nodejs/momentjs-alternatives/
- https://tempo.formkit.com
- https://github.com/moment/luxon

### Python
- https://deepnote.com/blog/ultimate-guide-to-the-datetime-library-in-python
- https://docs.python.org/3/library/datetime.html
- https://www.anaconda.com/guide/open-source-python-libraries

### Java
- https://barta.me/new-date-time-api-in-java-8/
- https://www.joda.org/joda-time/
- https://www.baeldung.com/java-date-time-history

### Go
- https://awesome-go.com
- https://threedots.tech/post/list-of-recommended-libraries/

### Rust
- https://users.rust-lang.org/t/jiff-is-a-new-date-time-library-for-rust-that-encourages-you-to-jump-into-the-pit-of-success/114781
- https://github.com/BurntSushi/jiff
- https://news.ycombinator.com/item?id=42877195
- https://docs.rs/jiff/latest/jiff/_documentation/comparison/index.html

### Ruby
- https://betterstack.com/community/guides/scaling-ruby/date-and-time/
- https://ruby-doc.org/core-2.6.8/Time.html

### PHP
- https://www.twilio.com/en-us/blog/developers/community/manage-dates-times-php-using-carbon
- https://packagist.org/packages/cakephp/chronos
- https://php.libhunt.com/compare-chronos-vs-carbon

### C#
- https://www.influxdata.com/blog/c-sharp-time-tutorial/
- https://learn.microsoft.com/en-us/dotnet/standard/datetime/choosing-between-datetime
- https://codeblog.jonskeet.uk/2012/05/02/more-fun-with-datetime/

---

**Document Generated**: 2026-01-01
**Research Methods**: Web search via Perplexity API with citations; community discussions; official documentation
**Coverage**: 8 major programming languages; 40+ libraries and frameworks
