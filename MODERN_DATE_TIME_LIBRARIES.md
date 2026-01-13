# Modern Date and Time Libraries and Standards (2026)

A comprehensive guide to actively-maintained, modern date/time libraries across programming languages, including ISO 8601 support, temporal APIs, duration handling, and recurring event libraries.

---

## Table of Contents

1. [JavaScript/TypeScript Libraries](#javascripttypescript-libraries)
2. [Python Libraries](#python-libraries)
3. [Rust Libraries](#rust-libraries)
4. [Go Libraries](#go-libraries)
5. [Recurring Event & Scheduling Libraries](#recurring-event--scheduling-libraries)
6. [ISO 8601 Standard & Specifications](#iso-8601-standard--specifications)
7. [Temporal API (JavaScript TC39)](#temporal-api-javascript-tc39)
8. [Duration and Interval Libraries](#duration-and-interval-libraries)

---

## JavaScript/TypeScript Libraries

### Luxon
- **Repository**: https://github.com/moment/luxon
- **Purpose**: Modern replacement for Moment.js with excellent timezone handling
- **Key Features**:
  - Built on JavaScript's `Intl` API for localization
  - Immutable API design
  - Comprehensive timezone support via geographical regions
  - Excellent internationalization support
  - Friendly API with method chaining
- **Best For**: Applications requiring accurate timezone conversions and localization
- **Bundle Size**: Larger (comprehensive feature set)
- **Status**: Actively maintained, production-ready

### date-fns
- **Repository**: https://github.com/date-fns/date-fns
- **Purpose**: Utility library of pure functions for date manipulation
- **Key Features**:
  - Modular imports (tree-shakeable for bundle optimization)
  - Each function is a standalone import
  - Pure functions with no side effects
  - Comprehensive date manipulation utilities
  - Works with native JavaScript `Date` objects
- **Best For**: Bundle size optimization and performance-conscious applications
- **Bundle Size**: Small (import only what you need)
- **Status**: Actively maintained, very popular

### Day.js
- **Repository**: https://github.com/iamkun/dayjs
- **Purpose**: Minimalist date/time library with small footprint
- **Key Features**:
  - Extremely small size (~2KB minified and gzipped)
  - Moment.js-like API for easy migration
  - Plugin ecosystem for extended functionality
  - Immutable by default
  - Chainable API
- **Best For**: Lightweight projects, minimal dependencies
- **Bundle Size**: ~2KB (smallest major option)
- **Status**: Actively maintained, lightweight alternative

### isoformat
- **Repository**: Not widely documented (lightweight utility)
- **Purpose**: ISO 8601 formatting and parsing with minimal overhead
- **Key Features**:
  - Formats dates to shortest valid ISO 8601 string
  - Returns date-only format when time is midnight UTC
  - Accepts 10+ ISO 8601 format variations
  - Zero dependencies
  - UTC-based
- **Best For**: Strict ISO 8601 compliance with minimal overhead
- **Status**: Specialized utility library

### Temporal Polyfills
- **@js-temporal/polyfill**: Alpha release available
  - Official TC39 polyfill implementation
  - Can be used today before native support
- **temporal-polyfill** (fullcalendar): Beta release available
  - Alternative implementation by fullcalendar project
- **Purpose**: Early adoption of Temporal API features
- **Status**: Polyfills available now; native support rolling out 2026+

---

## Python Libraries

### Standard `datetime` Module
- **Purpose**: Built-in standard library for all date/time operations
- **Key Features**:
  - Core types: `datetime.datetime`, `datetime.date`, `datetime.time`, `datetime.timedelta`
  - Timezone-aware with `tzinfo` support
  - `strftime()` formatting and `strptime()` parsing
  - Calendar arithmetic with `timedelta`
  - ~3x faster than pure Python alternatives (C implementation in CPython)
  - Python 3.9+ includes `zoneinfo` module for IANA timezone data
- **Best For**: Standard date/time operations, timezone handling
- **Status**: Standard library, continuously improved

### python-dateutil
- **Repository**: https://github.com/dateutil/dateutil
- **Purpose**: Extended date/time functionality and parsing
- **Key Features**:
  - `rrule` module for recurrence rules (RFC 2445 iCalendar standard)
  - `parser` for flexible date string parsing
  - `tz` module for timezone handling
  - `relativedelta` for intuitive date arithmetic
  - Supports YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY frequencies
  - `rruleset` for complex recurrence patterns (multiple rules, inclusions, exclusions)
- **Best For**: Recurring events, complex date parsing, iCalendar integration
- **Status**: Actively maintained, widely used

### Arrow
- **Repository**: https://github.com/arrow-py/arrow
- **Purpose**: Replacement for `datetime` with API inspired by moment.js
- **Key Features**:
  - Chainable API (moment.js style)
  - Human-readable date formatting
  - Timezone-aware operations
  - Simple date arithmetic
- **Best For**: Developers familiar with moment.js style APIs
- **Status**: Actively maintained

### Pendulum
- **Repository**: https://github.com/sdispater/pendulum
- **Purpose**: Modern Python date/time library focusing on ease of use
- **Key Features**:
  - Immutable and timezone-aware by default
  - Chainable API
  - Improved `timedelta` with better arithmetic
  - Supports duration objects
  - Localization support
- **Best For**: Modern Python applications needing clean APIs
- **Status**: Actively maintained

### Testing Libraries: Freezegun vs Time-machine
- **Freezegun** (Established Standard)
  - Mocks time in tests using decorator or context manager
  - Broad Python version support
  - Simple API for time mocking
  - Status: Mature and widely used

- **Time-machine** (Modern Alternative)
  - Performance-optimized alternative (C extensions)
  - Sophisticated time control for incremental advancement
  - Thread-local time mocking
  - Better performance in performance-critical tests
  - Status: Newer, gaining adoption

---

## Rust Libraries

### Chrono
- **Repository**: https://github.com/chronotope/chrono
- **Purpose**: Mature, widely-used date/time library
- **Key Features**:
  - Timezone-aware `DateTime` types by default
  - Configurable parsing and formatting with `strftime`-inspired syntax
  - System timezone support via `Local`
- **Limitations**:
  - Timezone data not shipped by default (requires `chrono-tz` or `tzfile`)
  - Partial leap second support
  - Date range limited to approximately ±262,000 years
- **Best For**: Legacy projects, existing ecosystem integration
- **Status**: Mature, widely used

### Time Crate (time v0.3.36+)
- **Repository**: https://github.com/time-rs/time
- **Purpose**: Alternative to Chrono with different API design
- **Key Features**:
  - Timezone offset-aware `OffsetDateTime` type
  - Modern async-friendly design
- **Critical Limitation**: Cannot safely perform DST arithmetic (only understands offsets, not timezone rules)
- **Best For**: Applications not requiring DST calculations
- **Status**: Actively maintained

### Jiff
- **Repository**: Emerging modern library (2025+)
- **Purpose**: Modern date/time library designed for correctness
- **Key Features**:
  - **Default ISO 8601 serialization** for standard format compatibility
  - **Full timezone support by default** with geographical regions (not just offsets)
  - Prevents DST-related bugs automatically
  - Flexible parsing accepting multiple formats
  - **Intelligent duration handling** accounting for varying month/year lengths
  - Reference date required for duration calculations (correct approach)
  - Described as "jumping into the pit of success"
- **Best For**: New Rust projects prioritizing correctness and ease of use
- **Status**: Newer (2025+), strongly recommended for new projects

### temporal_rs
- **Repository**: Emerging library based on ECMAScript Temporal
- **Purpose**: Calendar and timezone-aware library implementing TC39 Temporal spec
- **Key Features**:
  - Based on ECMAScript's Temporal API
  - ICU4X integration for internationalization
  - Highly conformant Temporal implementation
  - Cross-platform consistency with JavaScript
  - Full timezone and calendar support
- **Best For**: JavaScript-compatible datetime handling, cross-platform consistency
- **Status**: Recent release, designed for TC39 compatibility

---

## Go Libraries

### Standard `time` Package
- **Purpose**: Go's built-in date/time library
- **Key Features**:
  - Core types: `time.Time`, `time.Duration`, `time.Location`
  - Zero external dependencies
  - `time.Now()` for current time with timezone
  - `time.Format()` with reference time layout `Mon Jan 2 15:04:05 MST 2006`
  - `time.Parse()` for parsing date strings
  - Duration arithmetic with `time.Hour`, `time.Minute`, `time.Second`
  - Time comparison: `Before()`, `After()`, `Equal()`
  - Timezone handling: `time.UTC()`, `time.Local()`, `time.LoadLocation()`
- **Best For**: Most Go applications
- **Status**: Standard library, comprehensive

### Alternative Libraries
- Third-party libraries extend Go's date capabilities with flexible parsing and intuitive operations
- Comparisons available with libraries like Carbon and `strftime`-style formatting
- Standard `time` package typically sufficient for most use cases

---

## Recurring Event & Scheduling Libraries

### rrule (Recurrence Rule) Libraries

#### python-dateutil rrule
- **Language**: Python
- **Repository**: https://github.com/dateutil/dateutil
- **Purpose**: RFC 2445 iCalendar standard implementation
- **Key Features**:
  - Supports: YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY
  - Customization: `byweekday`, `bymonth`, `bymonthday`, `byhour`, etc.
  - `rruleset` for complex patterns (multiple rules, inclusions, exclusions)
  - Caching available for performance optimization
- **Status**: Actively maintained, production-ready

#### rrule.js
- **Language**: JavaScript
- **Repository**: https://github.com/jkbrzt/rrule
- **Purpose**: JavaScript/TypeScript port of Python's dateutil rrule
- **Key Features**:
  - Parsing and serialization of recurrence rules
  - Browser and Node.js compatible
  - Suitable for calendar event applications
- **Status**: Actively maintained

### APScheduler
- **Language**: Python
- **Repository**: https://github.com/agronholm/apscheduler
- **Purpose**: Task scheduling library for Python
- **Key Features**:
  - Advanced job scheduling capabilities
  - Cron-style scheduling support
  - Persistent job store options
  - Distributed scheduling support
- **Best For**: Task scheduling and job execution
- **Status**: Actively maintained

### node-cron
- **Language**: JavaScript/Node.js
- **Repository**: https://github.com/kelektiv/node-cron
- **Purpose**: Cron job scheduler for Node.js
- **Key Features**:
  - Cron expression parsing
  - Non-blocking task execution
  - Simple API for scheduling tasks
- **Best For**: Recurring tasks in Node.js
- **Status**: Actively maintained

### Celery
- **Language**: Python
- **Repository**: https://github.com/celery/celery
- **Purpose**: Distributed task queue system
- **Key Features**:
  - Distributed job scheduling
  - Recurring task support (celery-beat)
  - Multiple broker backends (Redis, RabbitMQ)
  - Task retries and error handling
- **Best For**: Distributed systems, task queues
- **Status**: Actively maintained, widely used

### iCalendar Libraries

#### icalendar (Python)
- **Language**: Python
- **Repository**: https://github.com/collective/icalendar
- **Purpose**: RFC 5545 iCalendar format parser and generator
- **Key Features**:
  - Full iCalendar specification support
  - Recurring event handling
  - Timezone support
  - Export to iCalendar format
- **Status**: Actively maintained

#### ical.js (JavaScript)
- **Language**: JavaScript
- **Repository**: https://github.com/mozilla-comm/ical.js
- **Purpose**: iCalendar and VEVENT parsing
- **Key Features**:
  - RFC 5545 compliance
  - Browser and Node.js support
  - Recurring event support via RRULE
- **Status**: Actively maintained by Mozilla

---

## ISO 8601 Standard & Specifications

### Standard Definition
- **Official Standard**: ISO 8601-1:2019 (Date and time — Representations for information interchange)
- **Latest Update**: 2019 revision
- **Key Standards**:
  - ISO 8601-1: Dates and times
  - ISO 8601-2: Time intervals and recurring events

### Format Specifications

#### Date Formats
- **Combined date and time**: `YYYY-MM-DDTHH:mm:ss`
- **Date only**: `YYYY-MM-DD`
- **Time only**: `HH:mm:ss`
- **With timezone**: `YYYY-MM-DDTHH:mm:ss±HH:mm` or `YYYY-MM-DDTHH:mm:ssZ` (UTC)
- **T separator**: Now mandatory between date and time (2019 standard)

#### Duration Format
- **Format**: `P[n]Y[n]M[n]DT[n]H[n]M[n]S`
  - `P`: Period designator
  - `Y`: Years, `M`: Months, `D`: Days (date components)
  - `T`: Time separator
  - `H`: Hours, `M`: Minutes, `S`: Seconds (time components)
- **Examples**:
  - `P3Y6M4DT12H30M5S`: 3 years, 6 months, 4 days, 12 hours, 30 minutes, 5 seconds
  - `PT2H15M`: 2 hours, 15 minutes
  - `P1M`: 1 month (note: without T)
  - `PT1M`: 1 minute (note: with T)
- **Decimal Support**: Fractional values like `P0.5Y` (half year)
- **Ambiguity Resolution**: T prefix required to distinguish months from minutes

#### Interval Format
ISO 8601 defines three interval representations:
1. **Start and end**: `YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss`
2. **Start and duration**: `YYYY-MM-DDThh:mm:ss/PnYnMnDTnHnMnS`
3. **Duration and end**: `PnYnMnDTnHnMnS/YYYY-MM-DDThh:mm:ss`

### Platform Support
- **Oracle Database**: Native support for ISO 8601 in SQL
- **Schema.org**: Requires ISO 8601 for structured data markup
- **JavaScript**: Temporal API implements ISO 8601 Duration format
- **Most modern frameworks**: Wide support across Python, JavaScript, Rust, Go, Java

### Important Notes
- **Spaces not permitted** in ISO 8601 expressions (per standard)
- **SQL Alternative**: SQL (ISO 9075) uses space instead of T (also valid but different standard)
- **Timezone T separator**: Mandatory in 2019 standard

---

## Temporal API (JavaScript TC39)

### Current Status
- **TC39 Stage**: Stage 3 (specification complete, review finished, implementation in progress)
- **Availability**:
  - Firefox 139+: Shipping (most mature implementation)
  - Chrome/V8: Under implementation
  - Safari/JavaScriptCore: Under implementation
  - Node.js: Under implementation (via V8)

### Using Temporal Today
1. **TC39 Playground**: Test directly at https://tc39.es/proposal-temporal/
2. **@js-temporal/polyfill**: Alpha release available
3. **temporal-polyfill**: Beta release by fullcalendar project

### Key Features

#### Date Objects
- **Temporal.PlainDate**: Date without time or timezone
- **Temporal.PlainTime**: Time without date or timezone
- **Temporal.PlainDateTime**: Date and time without timezone
- **Temporal.ZonedDateTime**: Date, time, and timezone (DST-aware)
- **Temporal.Instant**: Exact moment in UTC

#### Arithmetic Operations
- **Temporal.PlainDate.add()** and **.subtract()**: Date calculations with duration parameters
- **Temporal.Instant.until()** and **.since()**: Time differences between moments
- **Duration operations**: Over 200 utility methods for date/time operations
- **Nanosecond precision**: vs. milliseconds in legacy Date

#### Key Advantages Over Legacy Date
- **Immutable objects**: Prevents accidental mutations
- **Nanosecond precision**: More accurate time representation
- **DST handling**: Automatically handles daylight saving time
- **Multiple calendar systems**: Not limited to Gregorian calendar
- **Timezone-aware**: Proper timezone and offset handling
- **Date arithmetic**: Intuitive methods for adding/subtracting time

#### Temporal.Duration
- **ISO 8601 Implementation**: Conforms to ISO 8601-1 standard
- **Positive durations only**: Follows ISO 8601 specification
- **Weeks constraint**: Cannot be combined with other duration units
- **Format**: `P[n]Y[n]M[n]DT[n]H[n]M[n]S`

### Example API Preview
```javascript
// Create dates
const date = Temporal.PlainDate.from('2026-01-15');
const zonedDate = Temporal.ZonedDateTime.from('2026-01-15T10:30:00[America/New_York]');

// Arithmetic
const nextMonth = date.add({ months: 1 });
const yesterday = date.subtract({ days: 1 });

// Duration
const duration = Temporal.Duration.from('P1Y2M3DT4H5M6S');

// Comparisons
date.until(nextMonth); // Returns duration between dates
```

---

## Duration and Interval Libraries

### Core Concepts
- **ISO 8601 Duration**: Standard format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`
- **Date Range**: Specified as start/end datetimes or start + duration or duration + end
- **Interval Arithmetic**: Adding, subtracting, comparing time intervals

### Language-Specific Implementations

#### JavaScript
- **Temporal.Duration**: TC39 implementation, available via polyfills or Firefox 139+
- **date-fns**: Provides duration utilities (via Temporal polyfills in newer versions)
- **Luxon**: Duration objects for interval arithmetic
- **Day.js**: Duration plugin available

#### Python
- **datetime.timedelta**: Built-in for time deltas (not full ISO 8601 support)
- **python-dateutil**: Full ISO 8601 duration support via rrule module
- **pendulum.Duration**: Extended duration with better arithmetic
- **Arrow**: Simple duration calculations

#### Rust
- **Jiff**: Intelligent duration handling with reference dates
- **Chrono**: Duration operations via `Duration` type
- **time crate**: Duration support for offset-based calculations

#### Go
- **time.Duration**: Standard library duration type
- **time arithmetic**: Native support for adding/subtracting durations

### Key Considerations
- **Month/Year Ambiguity**: Months and years have variable lengths
  - **Correct approach**: Require reference date (Jiff uses this)
  - **Naive approach**: Assume fixed lengths (can be incorrect)
- **DST Handling**: Durations crossing DST boundaries need special handling
- **Timezone Awareness**: Duration calculations may depend on timezone

---

## Comparison Matrix

| Library | Language | Best For | Bundle/Size | Maturity | Key Strength |
|---------|----------|----------|-------------|----------|--------------|
| **Luxon** | JavaScript | Timezone handling | Larger | Mature | Comprehensive timezone |
| **date-fns** | JavaScript | Bundle optimization | Small | Mature | Tree-shakeable |
| **Day.js** | JavaScript | Minimal footprint | ~2KB | Mature | Lightweight |
| **Temporal** | JavaScript | Future-proof | Polyfill | Stage 3 | Immutable, precise |
| **Arrow** | Python | moment.js-like API | Medium | Active | Chainable API |
| **Pendulum** | Python | Modern Python | Medium | Active | Clean API |
| **python-dateutil** | Python | Recurring events | Medium | Mature | RFC 2445 iCalendar |
| **Chrono** | Rust | Mature ecosystem | Medium | Mature | Widely used |
| **Jiff** | Rust | Correctness | Medium | New | DST safety by default |
| **temporal_rs** | Rust | JS compatibility | Medium | New | TC39 compliant |
| **time.Time** | Go | Standard ops | Built-in | Mature | Zero dependencies |

---

## Recommendations by Use Case

### Web Application (JavaScript/TypeScript)
- **Small bundle required**: Day.js + date-fns for utilities
- **Timezone complexity**: Luxon
- **Future-proof**: Temporal API (via polyfill or wait for Firefox+ native support)

### Backend Application (Python)
- **Standard operations**: Built-in `datetime` + `zoneinfo`
- **Recurring events**: python-dateutil with rrule
- **Modern API**: Pendulum or Arrow
- **Task scheduling**: APScheduler or Celery

### Systems Programming (Rust)
- **New project**: Jiff (recommended for 2025+)
- **Existing ecosystem**: Chrono
- **Strict DST requirements**: Jiff or temporal_rs

### Backend Services (Go)
- **Standard library**: `time` package (usually sufficient)
- **Extended functionality**: Third-party alternatives for custom parsing

---

## Key Takeaways

1. **ISO 8601** remains the standard for date/time interchange across all platforms
2. **Temporal API** (Stage 3) brings DST-safe, timezone-aware date handling to JavaScript (2026+)
3. **Jiff** is the recommended new standard for Rust (2025+), offering DST safety by default
4. **Python's datetime** + **zoneinfo** (3.9+) covers most standard needs; dateutil for iCalendar
5. **Go's time** package is comprehensive for most applications
6. **Recurring events** should use RFC 2445-compliant libraries (rrule, python-dateutil)
7. **Immutable APIs** (Temporal, Pendulum, Jiff, Luxon) prevent common bugs in date arithmetic

---

## References

- [TC39 Temporal Proposal](https://github.com/tc39/proposal-temporal)
- [ISO 8601 Standard (Wikipedia)](https://en.wikipedia.org/wiki/ISO_8601)
- [RFC 2445 - iCalendar (Internet Calendaring and Scheduling Core Object Specification)](https://tools.ietf.org/html/rfc2445)
- [RFC 5545 - Internet Calendaring and Scheduling Core Object Specification](https://tools.ietf.org/html/rfc5545)
- [MDN: JavaScript Temporal API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
