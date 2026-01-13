# Specialized Date and Time Libraries - Quick Reference Guide

Fast lookup guide for selecting the right date/time library for your use case.

---

## By Programming Language

### Python

| Use Case | Recommended Library | Runner-up |
|----------|-------------------|-----------|
| Timezones (3.9+) | **zoneinfo** (stdlib) | pytz |
| Date math + parsing | **arrow** or **dateutil** | pendulum |
| Business days | **NumPy.busday_*** | bizdays |
| Human-readable time | **humanize** | arrow/pendulum |
| Simple formatting | **datetime** (stdlib) | - |

### JavaScript

| Use Case | Recommended Library | Runner-up |
|----------|-------------------|-----------|
| Bundle size critical | **Day.js** (6KB) | Luxon (40KB) |
| Date math + timezone | **Luxon** | date-fns + plugin |
| Functional API | **date-fns** | Luxon |
| Relative time only | **timeago.js** (1KB) | Native Intl API |
| Legacy codebase | **Moment.js** + **moment-timezone** | - |

### Rust

| Use Case | Recommended Library | Runner-up |
|----------|-------------------|-----------|
| New projects | **jiff** | chrono |
| Existing codebase | **chrono** + **chrono-tz** | jiff |
| Lightweight | **time crate** | - |
| Business logic | **jiff** | - |

### Go

| Use Case | Recommended Library | Runner-up |
|----------|-------------------|-----------|
| All cases | **time** (stdlib) | - |
| Memory-constrained | TinyTime/TinyDate | time |

### Java

| Use Case | Recommended Library | Runner-up |
|----------|-------------------|-----------|
| All modern code | **java.time** (stdlib) | - |
| Multiple calendars | **java.time.chrono** | ICU |
| Legacy code | java.text.SimpleDateFormat (deprecated) | - |

### C#/.NET

| Use Case | Recommended Library | Runner-up |
|----------|-------------------|-----------|
| Recommended | **Noda Time** | System.DateTime |
| Legacy | System.DateTime | - |

### C++

| Use Case | Recommended Library | Runner-up |
|----------|-------------------|-----------|
| Most complete | **HowardHinnant/date** | Boost.DateTime |
| Modern C++20 | **HowardHinnant/date** + chrono | - |

---

## By Feature

### Timezone Handling (IANA Database)

**Best libraries by language:**
```
Python:      zoneinfo, arrow, pendulum
JavaScript:  Luxon, Day.js + timezone plugin
Rust:        jiff, chrono + chrono-tz
Go:          time (built-in)
Java:        java.time (built-in)
C++:         HowardHinnant/date::tz
C#:          Noda Time
Ruby:        TZInfo
Dart:        timezone package
```

### Non-Gregorian Calendars

**Best libraries:**
- **C++**: HowardHinnant/date (Islamic, Julian calendars)
- **Java**: java.time.chrono (Islamic, Japanese, Buddhist, Chinese)
- **Multi-language**: ICU Library (100+ calendars, multiple languages)
- **Python**: convertdate, python-hijri-converter (specialized)
- **JavaScript**: hijri-converter, lunar-calendar (specialized)

### Date Parsing & Formatting

**Strongest parsing:**
- **Python**: dateutil (fuzzy parsing), arrow
- **JavaScript**: date-fns, Luxon
- **Rust**: jiff, chrono
- **Java**: java.time.format.DateTimeFormatter
- **C++**: HowardHinnant/date
- **Go**: time.Parse()

### Humanized/Relative Time

**Best libraries:**
- **JavaScript**: timeago.js (1KB standalone), date-fns, Luxon
- **Python**: humanize, arrow, pendulum
- **Native browser**: Intl.RelativeTimeFormat (no library)

### Business Day Calculations

**Specialized libraries:**
```
Python:
  - NumPy.busday_count() / busday_offset() [data science]
  - bizdays [finance]
  - python-networkdays [simple; no dependencies]
  - pybizday_utils [advanced]

Other languages:
  - No standard libraries
  - Consider NumPy from Python as reference implementation
```

---

## Decision Trees

### "Which timezone library should I use?"

```
Do you need to handle timezones?
├─ No → Use basic date library without timezone support
└─ Yes
   ├─ Python?
   │  ├─ Python 3.9+? → Use zoneinfo (stdlib)
   │  └─ Older? → Use pytz or arrow
   │
   ├─ JavaScript?
   │  ├─ Need small bundle? → Day.js + timezone plugin
   │  └─ Full-featured? → Luxon
   │
   ├─ Rust?
   │  ├─ New project? → jiff
   │  └─ Existing? → chrono + chrono-tz
   │
   ├─ Go?
   │  └─ Use time package (built-in)
   │
   ├─ Java?
   │  └─ Use java.time (built-in)
   │
   └─ C++?
      └─ Use HowardHinnant/date library
```

### "Which library for date parsing?"

```
Do you have complex date math?
├─ No
│  └─ Use standard library for your language
│
└─ Yes
   ├─ Python?
   │  ├─ Need fuzzy parsing? → dateutil
   │  └─ Chainable API? → arrow or pendulum
   │
   ├─ JavaScript?
   │  ├─ Functional style? → date-fns
   │  └─ Chainable API? → Luxon
   │
   ├─ Rust?
   │  ├─ New project? → jiff
   │  └─ Existing? → chrono
   │
   └─ Java?
      └─ Use java.time.format.DateTimeFormatter
```

### "Which library for humanized time display?"

```
Which language?
├─ JavaScript?
│  ├─ Standalone only? → timeago.js (1KB)
│  ├─ Native browser? → Intl.RelativeTimeFormat
│  └─ Full library? → date-fns or Luxon
│
├─ Python?
│  ├─ Multiple value types? → humanize
│  └─ Just relative time? → arrow or pendulum
│
└─ Other?
   └─ Implement custom or use language-specific alternative
```

---

## Common Combinations

### "Full-featured date library with everything"

**Python**: arrow + humanize
```python
import arrow
from humanize import naturaltime
```

**JavaScript**: Luxon
```javascript
import { DateTime } from 'luxon';
```

**Rust**: jiff
```rust
use jiff::{civil, tz};
```

**Java**: java.time (built-in)
```java
import java.time.*;
```

### "Lightweight bundle-size optimized"

**JavaScript**: Day.js (6KB) + plugins
```javascript
import dayjs from 'dayjs';
import timezone from 'dayjs/plugin/timezone';
dayjs.extend(timezone);
```

**Python**: datetime (stdlib) + zoneinfo (stdlib, 3.9+)
```python
import datetime
from zoneinfo import ZoneInfo
```

### "Maximum compatibility, minimal dependencies"

**JavaScript**: Native Intl APIs + timeago.js
```javascript
const rtf = new Intl.RelativeTimeFormat('en');
```

**Python**: datetime + zoneinfo (both stdlib in 3.9+)
```python
from datetime import datetime
from zoneinfo import ZoneInfo
```

**Go**: time (stdlib)
```go
import "time"
```

---

## Performance Characteristics

### Bundle Size (JavaScript)

| Library | Gzipped | Notes |
|---------|---------|-------|
| relative-time.js | <1KB | Minimal relative time only |
| timeago.js | ~1KB | Relative time with languages |
| Lately.js | ~1KB | ISO 8601 to relative |
| Day.js | 6KB | Full date library |
| Luxon | ~40KB | Full-featured date library |
| date-fns | 18KB | Functional date library |
| Moment.js | ~70KB | Historically dominant |

**Recommendation**: Use Day.js for bundle-size-critical applications.

### Memory Usage (Rust)

| Library | DateTime Size | Notes |
|---------|---------------|-------|
| time crate | ~16 bytes | Offset only (no timezone rules) |
| chrono | ~24 bytes | With timezone support |
| jiff | ~24 bytes | With timezone support |

### Data Science (Python)

**NumPy business day functions are fastest** for vectorized operations on large arrays:
```python
import numpy as np
business_days = np.busday_count(start, end)
```

---

## Version Recommendations

### Python

- **Python 3.9+**: Use `zoneinfo` (no install needed)
- **Python 3.8 and below**: Use `pytz` or `arrow`

### JavaScript

- **Modern projects**: Luxon or date-fns
- **Bundle-size critical**: Day.js
- **Legacy codebases**: Moment.js (in maintenance mode)

### Rust

- **New projects**: jiff (modern API, full timezone support)
- **Existing codebases**: chrono (mature, widely used)

### Java

- **Java 8+**: Use java.time (built-in)
- **Legacy Java**: java.text.SimpleDateFormat (deprecated)

---

## Known Limitations

### Python

- **datetime module**: Doesn't account for leap seconds, limited parsing
- **pytz**: Some ambiguity edge cases with UTC+offset
- **dateutil**: Can be slower for simple operations

### JavaScript

- **Moment.js**: Large bundle size, no tree-shaking (in maintenance mode)
- **Day.js**: Plugins not always consistent
- **date-fns**: Large single-file imports can bloat bundles

### Rust

- **chrono**: Timezone data must come from companion crates
- **time crate**: No full DST support (offset-only)
- **jiff**: Newer, less battle-tested than chrono

### Go

- **time package**: Basic relative time requires custom implementation

---

## Testing Checklist

When choosing a library, verify:

- [ ] Timezone database is current (within 2 releases of latest IANA)
- [ ] DST transitions are handled correctly
- [ ] Parsing handles ISO 8601 format
- [ ] Performance is acceptable for your scale
- [ ] Bundle size fits your constraints
- [ ] Localization covers your target locales
- [ ] API matches your coding style (functional vs OOP vs chainable)
- [ ] License is compatible with your project
- [ ] Community/maintenance status is healthy

---

## Additional Resources

**Standards & Specifications:**
- IANA Time Zone Database: https://www.iana.org/time-zones
- ISO 8601 Standard: https://en.wikipedia.org/wiki/ISO_8601
- Unicode CLDR: https://cldr.unicode.org/
- TC39 Temporal Proposal: https://tc39.es/proposal-temporal/

**Library Comparisons:**
- JavaScript: https://www.dhiwise.com/post/date-fns-vs-dayjs-the-battle-of-javascript-date-libraries
- Python: https://docs.python.org/3/library/datetime.html
- Rust: https://docs.rs/jiff/latest/jiff/_documentation/comparison/index.html

---

**Last Updated**: 2026-01-01
**Version**: 1.0
