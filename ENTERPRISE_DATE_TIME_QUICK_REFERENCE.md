# Enterprise Date/Time Libraries - Quick Reference Guide

Quick lookup table for selecting date/time tools based on specific use cases and requirements.

---

## 1. Choose Your Core Date/Time Library

### JavaScript/TypeScript Decision Tree

```
Need immutable, timezone-safe, modern?
  → YES: Use LUXON (premium choice)
  → NO: Functional, modular approach?
         → YES: Use DATE-FNS (modern standard)
         → NO: Lightweight + moment.js API?
                → YES: Use DAY.JS
                → NO: Legacy system?
                       → YES: Use MOMENT.JS
                       → NO: Future standard?
                              → Use TEMPORAL API
```

**TL;DR for JavaScript:**
- **Modern projects**: Use **Luxon** or **Date-fns**
- **Performance critical**: Use **date-fns** (tree-shakeable)
- **Lightweight**: Use **day.js** (<2KB)
- **Legacy projects**: Keep **moment.js**
- **Future-ready**: Study **Temporal API**

### Python Decision Tree

```
Python version >= 3.9?
  → YES: Use ZONEINFO (built-in, modern)
  → NO: Use PYTZ (legacy support)

Need simple API similar to moment.js?
  → YES: Use ARROW or PENDULUM
  → NO: Need specific feature (recurrence, fuzzy)?
         → Recurrence: Use DATEUTIL.RRULE
         → Fuzzy: Use DATEUTIL.PARSER
```

**TL;DR for Python:**
- **Python 3.9+**: Use **zoneinfo** + **arrow/pendulum**
- **Legacy Python**: Use **pytz** + **arrow**
- **Complex patterns**: Use **dateutil**
- **DST-critical**: Use **pendulum** (best DST handling)
- **Data science**: Use **pandas.bdate_range()**

### Java Decision Tree

```
Java version >= 8?
  → YES: Use JAVA.TIME (always, no exceptions)
  → NO: Migrate to Java 8+

Need advanced features (better DST, immutability)?
  → YES: Consider NODATIME if enterprise C#/.NET
  → NO: java.time is sufficient
```

**TL;DR for Java:**
- **All new projects**: Use **java.time** exclusively
- **Scheduling**: Use **Quartz** with **java.time**
- **Enterprise needs**: java.time covers 99% of use cases

### Go Decision Tree

```
Does time package handle your needs?
  → YES: Use TIME package (always)
  → NO: This is rare; verify requirement
```

**TL;DR for Go:**
- **Always use built-in TIME package**
- Standard library covers all needs
- Use `time.LoadLocation()` for timezone operations

### C# / .NET Decision Tree

```
Need timezone support?
  → YES: Use DATETIMEOFFSET + TIMEZONEINFO
  → NO: Use DATETIME

Need advanced immutability and semantics?
  → YES: Use NODATIME
  → NO: Built-in classes sufficient
```

**TL;DR for C#:**
- **Basic operations**: Use **DateTime**
- **Distributed systems**: Use **DateTimeOffset**
- **Enterprise/advanced**: Use **NodaTime**

---

## 2. Add Validation Layer

| Language | Use Case | Library | Code Example |
|----------|----------|---------|--------------|
| **JavaScript** | API validation | Zod | `z.date().min(new Date())` |
| **JavaScript** | Form validation | yup | `yup.date().required()` |
| **JavaScript** | Enterprise schemas | Joi | `Joi.date().iso()` |
| **TypeScript** | Type-driven | io-ts | Custom codec + runtime check |
| **Python** | API/models | pydantic | `date_field: datetime` |
| **Python** | Serialization | marshmallow | `DateTime()` field |
| **Java** | Entity validation | Hibernate Validator | `@Future`, `@Past` |
| **Java** | Batch validation | Commons Validator | `DateValidator.isValid()` |
| **C#** | Model validation | Data Annotations | `[DataType(DataType.Date)]` |

---

## 3. Handle Specific Requirements

### Requirement: Parse and Schedule Cron Expressions

| Language | Library | Install | Quick Start |
|----------|---------|---------|-------------|
| **Python** | croniter | `pip install croniter` | `cron = croniter('0 0 * * *', now)` |
| **JavaScript** | cron-parser | `npm install cron-parser` | `parser.parseExpression('0 0 * * *')` |
| **Node.js** | node-cron | `npm install node-cron` | `cron.schedule('0 0 * * *', task)` |
| **Java** | Cronsmith | Maven dependency | Extends `AbstractCron` |
| **Go** | Standard library | Built-in | `time.NewTicker()` |

**Best Practices:**
- Use **croniter** for Python (de facto standard)
- Use **cron-parser** for Node.js validation
- Use **node-cron** for actual scheduling
- Use **Quartz** for enterprise Java

---

### Requirement: Calculate Business Days/Hours

| Language | Library | Supports | Best For |
|----------|---------|----------|----------|
| **Python** | bizdays | Custom holidays, config | Flexible scheduling |
| **Python** | python-networkdays | Weekends, holidays | Payroll systems |
| **Python** | NumPy busday_count() | Bulk calculations | Vectorized operations |
| **Python** | pandas bdate_range() | Date ranges | Data science |
| **JavaScript** | business-days | Weekends, holidays | Modern projects |
| **JavaScript** | moment-business-days | With moment.js | Legacy projects |
| **Java** | Custom TemporalAdjusters | Custom logic | Enterprise |

**Quick Implementation:**
```python
# Python - Simple approach
from datetime import timedelta, date

def business_days_between(start, end):
    current = start
    count = 0
    while current <= end:
        if current.weekday() < 5:  # Mon-Fri
            count += 1
        current += timedelta(days=1)
    return count
```

---

### Requirement: Multi-Country Holiday Support

| Language | Library | Coverage | Use Case |
|----------|---------|----------|----------|
| **Python** | holidays | 100+ countries | Go-to standard |
| **Python** | workalendar | 100+ countries | Calendar systems |
| **JavaScript** | holiday-calendar | Multiple countries | Node.js apps |
| **Java** | jollyday | 100+ countries | Enterprise |

**Quick Example:**
```python
# Python - Holiday checking
import holidays

us_holidays = holidays.US()
christmas = date(2026, 12, 25)
if christmas in us_holidays:
    print(f"{christmas}: {us_holidays.get(christmas)}")
```

---

### Requirement: Localization & i18n

| Language | Solution | Support | Best For |
|----------|----------|---------|----------|
| **JavaScript** | Intl.DateTimeFormat | Native (all browsers) | No dependency |
| **JavaScript** | date-fns locales | 50+ locales | Comprehensive |
| **JavaScript** | Luxon + Intl | Leverage native API | Modern projects |
| **Python** | Babel | 500+ locales | Full CLDR support |
| **Python** | Arrow/Pendulum | Basic localization | Simple formatting |
| **Java** | java.time + Locale | Full support | All projects |
| **Java** | ICU4J | 500+ locales | Advanced formatting |

**Quick Example:**
```javascript
// JavaScript - Native localization
new Intl.DateTimeFormat('de-DE', {
  dateStyle: 'long',
  timeStyle: 'short'
}).format(new Date())
// Output: "15. Januar 2026, 14:30"
```

---

### Requirement: Timezone Handling

| Scenario | JavaScript | Python | Java | C# |
|----------|-----------|--------|------|-----|
| **Store internally** | ISO 8601 | UTC (pytz) | Instant | UTC |
| **Convert to local** | luxon.toLocal() | astimezone() | toLocalDateTime() | ToLocalTime() |
| **DST transitions** | luxon handles | pendulum (best) | java.time | NodaTime |
| **Parse from string** | date-fns.parse() | dateutil.parser | LocalDateTime.parse() | DateTime.Parse() |
| **Format for display** | Intl API | datetime.strftime() | DateTimeFormatter | ToString(fmt) |

**Production Pattern:**
```javascript
// Store and transmit in ISO 8601
const isoString = new Date().toISOString();  // "2026-01-15T14:30:00Z"

// Convert to user timezone for display
const userTz = Intl.DateTimeFormat().resolvedOptions().timeZone;
const formatter = new Intl.DateTimeFormat('default', {
  timeZone: userTz,
  dateStyle: 'long'
});
console.log(formatter.format(new Date()));
```

---

### Requirement: Relative Time ("2 hours ago")

| Language | Library | Size | Pattern |
|----------|---------|------|---------|
| **JavaScript** | date-fns | Modular | `formatDistanceToNow(date)` |
| **JavaScript** | Lately.js | ~1KB | Lightweight option |
| **JavaScript** | day.js + plugin | <2KB | `dayjs().fromNow()` |
| **JavaScript** | Intl.RelativeTimeFormat | Native | No dependency |
| **Python** | arrow | Simple | `arrow.now().shift(days=-5).humanize()` |
| **Python** | pendulum | Simple | `pendulum.now().subtract(hours=3).diff_for_humans()` |

---

### Requirement: Date Ranges & Recurrence

| Language | Library | Feature | Example |
|----------|---------|---------|---------|
| **Python** | dateutil.rrule | RFC 5545 RRULE | `rrule(DAILY, count=5, dtstart=now)` |
| **Python** | arrow.range() | Date sequences | `arrow.utcnow().range('day', end_date)` |
| **Python** | pendulum.range() | Period handling | `pendulum.parse('2026-01').range('day')` |
| **JavaScript** | date-fns intervals | Interval math | `isWithinInterval(date, interval)` |
| **JavaScript** | moment-range | Range arithmetic | `range.contains(date)` |
| **Java** | java.time streams | Period calculations | `temporal.until(temporal, period)` |

**Python Recurrence Example:**
```python
from dateutil.rrule import rrule, DAILY, MONTHLY

# Every weekday for 10 days
rule = rrule(DAILY, dtstart=datetime(2026, 1, 15), count=10, byweekday=[0,1,2,3,4])
for dt in rule:
    print(dt)
```

---

## 4. Testing Date-Dependent Code

| Language | Tool | Install | Usage |
|----------|------|---------|-------|
| **Python** | freezegun | `pip install freezegun` | `@freeze_time('2026-01-15')` |
| **JavaScript** | Jest Fake Timers | Built-in | `jest.useFakeTimers()` |
| **Java** | java-time in tests | No dependency | Create test instances |
| **Go** | Custom mocks | Manual | Inject time interface |
| **C#** | Moq | NuGet | Mock ISystemClock |

**Python Testing Example:**
```python
from freezegun import freeze_time

@freeze_time("2026-01-15 12:00:00")
def test_birthday_discount():
    assert calculate_discount() == 0.1  # 10% discount
```

---

## 5. Decision Flowchart: Which Library to Choose?

```
START
  ↓
What's your primary language?
  ├─→ JavaScript/TypeScript
  │    ├─→ Need timezone support?
  │    │    ├─→ YES → LUXON (best)
  │    │    └─→ NO → DATE-FNS or DAY.JS
  │    └─→ Legacy app?
  │         ├─→ YES → MOMENT.JS
  │         └─→ NO → See above
  │
  ├─→ Python
  │    ├─→ Python version >= 3.9?
  │    │    ├─→ YES → ZONEINFO + (ARROW or PENDULUM)
  │    │    └─→ NO → PYTZ + DATEUTIL
  │    └─→ Need DST safety?
  │         ├─→ YES → PENDULUM
  │         └─→ NO → ARROW is fine
  │
  ├─→ Java
  │    └─→ Java >= 8?
  │         ├─→ YES → JAVA.TIME (always)
  │         └─→ NO → Upgrade! But use JODA-TIME temporarily
  │
  ├─→ Go
  │    └─→ Use TIME package (standard library)
  │         └─→ ALWAYS (no exceptions)
  │
  └─→ C# / .NET
       ├─→ Basic datetime?
       │    └─→ DATETIME
       └─→ Timezone-aware?
            ├─→ YES → DATETIMEOFFSET
            └─→ Enterprise-grade → NODATIME
```

---

## 6. Performance Comparison (Bundle Sizes)

```
JavaScript Library Sizes (gzipped):
┌─────────────────┬──────────┐
│ Library         │ Size     │
├─────────────────┼──────────┤
│ day.js          │ <2 KB    │ ← Smallest
│ luxon           │ 15 KB    │
│ date-fns        │ 5-30 KB  │ (tree-shakeable)
│ moment.js       │ 67 KB    │ ← Largest
│ Temporal        │ Built-in │ ← No extra
└─────────────────┴──────────┘

Recommendation: Use day.js for size-critical apps,
luxon for enterprise, date-fns for modular approach.
```

---

## 7. Ecosystem Integration Examples

### Express.js + Luxon
```javascript
const { DateTime } = require('luxon');
app.get('/api/event/:id', (req, res) => {
  const eventTime = DateTime.fromISO(req.body.time).toUTC();
  res.json({ scheduledAt: eventTime.toISO() });
});
```

### FastAPI + Pydantic
```python
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    scheduled_at: datetime

@app.post('/api/event')
def create_event(event: Event):
    return {"created": event.scheduled_at}
```

### Spring Boot + java.time
```java
@RestController
@RequestMapping("/api/events")
public class EventController {
    @PostMapping
    public ResponseEntity<Event> create(@RequestBody Event event) {
        event.setScheduledAt(ZonedDateTime.now(ZoneId.of("UTC")));
        return ResponseEntity.ok(event);
    }
}
```

### Node.js + node-cron
```javascript
const cron = require('node-cron');

cron.schedule('0 0 * * *', async () => {
  console.log('Daily cleanup task');
  await performCleanup();
});
```

---

## 8. Migration Strategies

### Migrating from Moment.js to Luxon
```javascript
// Before (moment.js)
const m = moment('2026-01-15').tz('America/New_York');
console.log(m.format('YYYY-MM-DD HH:mm'));

// After (luxon)
const { DateTime } = require('luxon');
const dt = DateTime.fromISO('2026-01-15').setZone('America/New_York');
console.log(dt.toFormat('yyyy-MM-dd HH:mm'));
```

### Migrating from Moment.js to Date-fns
```javascript
// Before (moment.js)
const m = moment().add(1, 'day').format('YYYY-MM-DD');

// After (date-fns)
import { addDays, format } from 'date-fns';
const formatted = format(addDays(new Date(), 1), 'yyyy-MM-dd');
```

### Migrating from pytz to zoneinfo (Python 3.9+)
```python
# Before (pytz)
import pytz
tz = pytz.timezone('America/New_York')
dt = datetime.now(tz=pytz.UTC).astimezone(tz)

# After (zoneinfo)
from zoneinfo import ZoneInfo
dt = datetime.now(tz=ZoneInfo('America/New_York'))
```

---

## 9. Common Pitfalls & Solutions

| Pitfall | Cause | Solution |
|---------|-------|----------|
| **DST bugs** | Naive datetime usage | Use library with explicit DST handling (pendulum, luxon) |
| **Timezone confusion** | Storing local time | Always store UTC, convert for display |
| **Month off-by-one** | moment.js 0-indexing | Use luxon or date-fns (1-indexed) |
| **Immutability issues** | moment.js mutates | Use luxon or date-fns (immutable) |
| **Large bundles** | Using moment.js | Switch to date-fns or day.js |
| **Parsing fails** | Inconsistent formats | Use ISO 8601, or library with fuzzy parsing |
| **Leap seconds** | JavaScript Date ignorance | Shouldn't affect most apps; be aware |
| **Ambiguous times** | Clock fallback during DST | Handle explicitly (luxon supports this) |

---

## 10. Checklist for Production Deployments

- [ ] **Timezone handling**: All times stored in UTC
- [ ] **Display conversion**: User-local timezone for UI
- [ ] **DST transitions**: Test around spring/fall changes
- [ ] **Validation**: Input dates validated against constraints
- [ ] **Serialization**: Use ISO 8601 for APIs
- [ ] **Testing**: Date-dependent code tested with frozen time
- [ ] **i18n**: Date formatting respects user locale
- [ ] **Holidays**: Business logic accounts for holidays
- [ ] **Cron jobs**: Tested with edge cases (year boundaries)
- [ ] **Performance**: Bundle size acceptable for app
- [ ] **Documentation**: Team aware of chosen libraries
- [ ] **Migration path**: Plan for deprecation (moment.js → luxon)

---

## Quick Command Reference

### Installation Commands

**JavaScript/TypeScript:**
```bash
npm install luxon       # Premium
npm install date-fns    # Functional
npm install dayjs       # Lightweight
npm install zod         # Validation
```

**Python:**
```bash
pip install python-dateutil  # Core
pip install arrow            # Friendly API
pip install pendulum         # DST-aware
pip install pydantic         # Validation
pip install holidays         # Holiday calendars
```

**Java:** (gradle)
```gradle
implementation 'org.quartz-scheduler:quartz:2.3.2'
// java.time is built-in, no dependency needed
```

**Go:** (built-in)
```go
import "time"  // Standard library
```

**C#:** (nuget)
```bash
dotnet add package NodaTime
```

---

**Last Updated**: 2026-01-01
**Version**: 1.0
**Coverage**: 70+ libraries across 5 languages
