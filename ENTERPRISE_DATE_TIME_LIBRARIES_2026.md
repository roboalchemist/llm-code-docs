# Enterprise-Grade and Specialized Date/Time Libraries (2026)

A comprehensive catalog of production-ready date/time manipulation, validation, and scheduling libraries across major programming languages.

---

## Table of Contents

1. [Core Date/Time Libraries by Language](#core-datetime-libraries-by-language)
2. [Date/Time Validation Libraries](#datetime-validation-libraries)
3. [Cron Expression Parsers](#cron-expression-parsers)
4. [Business Hours & Working Days](#business-hours--working-days)
5. [Date Range & Period Libraries](#date-range--period-libraries)
6. [Localization & Internationalization (i18n)](#localization--internationalization-i18n)
7. [Holiday & Calendar Management](#holiday--calendar-management)
8. [Relative Time & Fuzzy Parsing](#relative-time--fuzzy-parsing)
9. [Timezone & DST Handling](#timezone--dst-handling)
10. [Enterprise Scheduling & Temporal](#enterprise-scheduling--temporal)

---

## Core Date/Time Libraries by Language

### JavaScript/TypeScript

#### **moment.js** (Deprecated - Legacy Support)
- **Status**: Officially recommended against for new projects; widely used in legacy systems
- **Bundle Size**: ~67KB
- **Key Features**:
  - Comprehensive date parsing, validation, manipulation, formatting
  - Extensive timezone handling capabilities
  - Chainable API with fluent interface
  - 246 locales supported
  - Relative time calculations (e.g., "2 hours ago")
- **Best For**: Legacy application maintenance, backward compatibility
- **Documentation**: https://momentjs.com/
- **License**: MIT

#### **luxon** (Modern Premium Choice)
- **Status**: Actively maintained; recommended modern replacement for moment.js
- **Bundle Size**: ~45KB (gzipped: ~15KB)
- **Key Features**:
  - Immutable objects (prevents accidental mutations)
  - Proper timezone handling with named timezones
  - 1-indexed months (more intuitive than moment's 0-indexing)
  - Integration with Intl API for localization
  - Robust DST handling
  - Chainable API similar to moment.js for easy migration
- **Best For**: Enterprise applications needing robust timezone support
- **Documentation**: https://moment.github.io/luxon/
- **License**: MIT

#### **date-fns** (Functional Approach)
- **Status**: Actively maintained; growing adoption in modern projects
- **Bundle Size**: ~200+ modular functions, tree-shakeable
- **Key Features**:
  - Functional programming paradigm (no method chaining)
  - 50+ locales for internationalization
  - Immutable by design
  - Excellent TypeScript support
  - Superior performance and bundle size optimization
  - Tree-shakeable modules allow importing only needed functions
  - Comprehensive date manipulation (add, subtract, difference, formatting)
- **Best For**: Modern bundler-based projects, performance-critical applications
- **Documentation**: https://date-fns.org/
- **License**: MIT

#### **dayjs** (Lightweight Alternative)
- **Status**: Actively maintained; minimal footprint
- **Bundle Size**: <2KB (gzipped)
- **Key Features**:
  - API fully compatible with moment.js for easy migration
  - Minimalist core with optional plugins
  - Plugin ecosystem for extended functionality
  - Supports timezone via plugins
  - Supports localization with 50+ locale plugins
  - Chainable API
- **Best For**: Lightweight applications, size-constrained environments, mobile web
- **Documentation**: https://day.js.org/
- **License**: MIT

#### **js-joda** (Java Port to JavaScript)
- **Status**: Maintained; niche use for Java-familiar developers
- **Key Features**:
  - Ports Java's java.time API to JavaScript
  - Immutable temporal objects
  - Comprehensive timezone support (IANA timezone database)
  - ZonedDateTime, LocalDate, LocalTime, LocalDateTime, Instant
  - Full JSR-310 (java.time) semantics
- **Best For**: Teams migrating from Java, projects needing java.time semantics
- **Documentation**: https://js-joda.github.io/js-joda/
- **License**: BSD-3-Clause

#### **Temporal API** (Emerging Standard)
- **Status**: Stage 3 ECMAScript proposal; not yet universally available in 2026
- **Key Features**:
  - Built-in time zone support via Temporal.ZonedDateTime
  - Separate date-only and time-only types (Temporal.PlainDate, Temporal.PlainTime)
  - Proper handling of DST transitions and ambiguous times
  - Calendar systems beyond Gregorian (Hebrew, Islamic, etc.)
  - ISO 8601 formatting
  - Zero-based arithmetic and intuitive semantics
- **Best For**: Future-forward applications, greenfield projects planning for ES2026+
- **Documentation**: https://tc39.es/proposal-temporal/
- **Status**: Polyfills available (tc39/proposal-temporal-polyfill)

---

### Python

#### **datetime** (Standard Library)
- **Status**: Built-in; foundational for all Python date/time work
- **Key Features**:
  - Core classes: datetime, date, time, timedelta, timezone
  - Basic arithmetic with timedelta
  - Comparison operations
  - Formatting with strftime/strptime
  - timezone-aware datetime support (Python 3.2+)
- **Limitations**: Basic functionality; no parsing, no i18n, no DST handling
- **Best For**: Simple date/time operations, always available
- **License**: PSF

#### **pytz** (Timezone Database)
- **Status**: Standard choice for timezone handling
- **Key Features**:
  - IANA timezone database integration
  - Handles DST transitions
  - Naive and aware datetime conversions
  - Localization of datetimes to specific timezones
- **Best For**: Applications requiring robust timezone support
- **Documentation**: https://pypi.org/project/pytz/
- **License**: MIT

#### **zoneinfo** (Python 3.9+ Standard Library)
- **Status**: Modern replacement for pytz; built-in since Python 3.9
- **Key Features**:
  - IANA timezone database access
  - Better DST handling than pytz
  - Part of standard library (no external dependency)
  - Preferred for Python 3.9+ projects
- **Best For**: New projects targeting Python 3.9+
- **License**: PSF

#### **dateutil** (De Facto Standard)
- **Status**: Widely used; comprehensive date utilities
- **Key Features**:
  - Flexible date parsing (parser.parse())
  - Relative time calculations (relativedelta)
  - Recurring date rules via rrule module
  - Timezone handling (tzlocal, tzfile)
  - Fuzzy date parsing with unrecognized text
- **Best For**: Complex date manipulation, recurring events, flexible parsing
- **Documentation**: https://dateutil.readthedocs.io/
- **License**: Dual: BSD / Apache 2.0

#### **arrow** (Friendly Date API)
- **Status**: Actively maintained; simpler than dateutil
- **Key Features**:
  - Simplified datetime manipulation API
  - Built on top of dateutil
  - Timezone handling
  - Relative time string parsing ("in 2 hours")
  - Range calculations
  - Humanized output ("2 days ago")
- **Best For**: Readable, developer-friendly date operations
- **Documentation**: https://arrow.readthedocs.io/
- **License**: Apache 2.0

#### **pendulum** (Poetry's Date Library)
- **Status**: Actively maintained; rivals arrow in popularity
- **Key Features**:
  - Fluent API similar to moment.js
  - Excellent DST handling (better than arrow)
  - Timezone support with proper DST transitions
  - Range/period calculations
  - Relative time parsing
  - Built on dateutil but with better DST semantics
- **Best For**: Projects using Poetry, robust DST handling needed
- **Documentation**: https://pendulum.eustace.io/
- **License**: MIT

#### **freezegun** (Testing Utility)
- **Status**: Essential for testing date-dependent code
- **Key Features**:
  - Mock datetime.datetime.now() and time.time()
  - Tick forward through time in tests
  - Works with all major frameworks
  - Freeze time at specific moments
- **Best For**: Unit testing date/time logic
- **Documentation**: https://github.com/spulec/freezegun
- **License**: MIT

---

### Java

#### **java.time** (Standard Library - Java 8+)
- **Status**: De facto standard for all new Java development
- **Bundle**: Part of JDK
- **Key Classes**:
  - **LocalDate**: Date without time (e.g., 2026-01-15)
  - **LocalTime**: Time without date
  - **LocalDateTime**: Date and time without timezone
  - **ZonedDateTime**: Date/time with timezone
  - **OffsetDateTime**: Date/time with fixed UTC offset
  - **Instant**: Point in time on timeline
  - **Duration**: Time between two instants
  - **Period**: Time between two local dates
- **Key Features**:
  - Immutable and thread-safe
  - Comprehensive timezone support
  - Proper DST handling
  - ISO 8601 formatting
  - Extensible calendar systems
- **Integration**: Native support in Hibernate, Spring Data, JPA
- **Best For**: All new Java projects
- **Documentation**: https://docs.oracle.com/javase/tutorial/datetime/
- **License**: Oracle GPL

#### **Joda-Time** (Legacy - Use java.time Instead)
- **Status**: Superseded by java.time; maintained for legacy code only
- **Note**: Joda-Time inspired java.time design and remains available for backward compatibility
- **Best For**: Legacy system maintenance only

---

### Go

#### **time** (Standard Library)
- **Status**: Built-in; comprehensive for production use
- **Key Functions**:
  - **time.Now()**: Current local time
  - **time.Date()**: Construct specific datetime
  - **time.Parse()**: Parse time from string
  - **time.Format()**: Format time to string
  - **Add()/AddDate()**: Time arithmetic
  - **Sub()**: Calculate time differences
  - **Before()/After()/Equal()**: Time comparisons
  - **time.Ticker**: Recurring intervals
  - **time.Timer**: One-off delays
- **Timezone Support**:
  - **time.FixedZone()**: Custom fixed-offset zones
  - **time.LoadLocation()**: Load named timezones (e.g., "America/New_York")
  - IANA timezone database support
- **Key Features**:
  - Gregorian calendar only
  - Nanosecond precision
  - No leap second support
  - Layout-based formatting (no format strings)
- **Best For**: All production Go applications
- **Documentation**: https://golang.org/pkg/time/
- **License**: BSD

---

### C# / .NET

#### **DateTime / DateTimeOffset** (BCL - Framework Class Library)
- **Status**: Built-in; standard choice
- **Key Types**:
  - **DateTime**: 64-bit date/time value
  - **DateTimeOffset**: DateTime with UTC offset (preferred for distributed systems)
  - **DateOnly**: Date without time (C# 10+)
  - **TimeOnly**: Time without date (C# 10+)
  - **TimeSpan**: Duration between two times
  - **TimeZoneInfo**: Timezone conversion and DST handling
- **Key Features**:
  - Ticks-based internal representation (100-nanosecond intervals)
  - Comparison operators: <, >, <=, >=, ==, !=
  - DateTime.Compare() and CompareTo() methods
  - Arithmetic with TimeSpan
  - ToString() with format specifiers
- **Best Practices**:
  - Use DateTimeOffset for distributed/cloud systems
  - Use UTC internally, convert for display
  - Use TimeZoneInfo for DST-aware conversions
  - Apply tolerance thresholds when comparing calculated DateTimes
- **Best For**: Most .NET applications
- **License**: Microsoft (Part of Framework)

#### **NodaTime** (Third-Party - Premium)
- **Status**: Actively maintained; industry-standard alternative
- **Key Features**:
  - Comprehensive timezone support
  - Immutable value types
  - Better semantic clarity (LocalDateTime, ZonedDateTime, etc.)
  - Comprehensive calendar systems
  - Excellent test/mock support
  - Culture-aware formatting (similar to Temporal API)
  - Interval arithmetic
- **Best For**: Enterprise applications needing robust date/time semantics
- **Documentation**: https://nodatime.org/
- **License**: Apache 2.0

---

## Date/Time Validation Libraries

### JavaScript/TypeScript

#### **Zod** (Runtime Schema Validation)
- **Status**: Popular modern validation library
- **Date Support**: z.date() with min/max/refine methods
- **Example**:
  ```typescript
  z.date().min(new Date("2026-01-01")).max(new Date("2026-12-31"))
  ```
- **Best For**: API request validation, form validation
- **Documentation**: https://zod.dev/
- **License**: MIT

#### **Joi** (Comprehensive Validation)
- **Status**: Enterprise-grade; widely adopted in Hapi ecosystem
- **Date Support**: .date() with .min(), .max(), .iso() for ISO 8601
- **Example**:
  ```javascript
  Joi.date().iso().min('now').max('2026-12-31')
  ```
- **Best For**: Complex validation schemas, Hapi.js applications
- **Documentation**: https://joi.dev/
- **License**: BSD-3-Clause

#### **yup** (Simple Schema Validation)
- **Status**: Lightweight; popular in React/form validation
- **Date Support**: .date() with min/max/typeError methods
- **Example**:
  ```javascript
  yup.date().min(new Date(), "Past dates not allowed").required()
  ```
- **Best For**: Form validation, React applications
- **Documentation**: https://github.com/jquense/yup
- **License**: MIT

#### **io-ts** (Type-Driven Validation)
- **Status**: Functional programming approach
- **Date Support**: Custom date codec for runtime validation
- **Best For**: Functional TypeScript applications, type-safe validation
- **License**: MIT

#### **runtypes** (Type System Validation)
- **Status**: Runtime type checking with TypeScript integration
- **Date Support**: Custom date validators
- **Best For**: Type-driven development, API contract validation
- **License**: MIT

---

### Python

#### **pydantic** (Data Validation)
- **Status**: De facto standard for Python validation
- **Date Support**:
  - datetime, date, time field types
  - Built-in parsing from strings, timestamps, numeric values
  - Custom validators with field_validator decorator
- **Example**:
  ```python
  from pydantic import BaseModel, field_validator

  class Event(BaseModel):
      scheduled_date: datetime

      @field_validator('scheduled_date')
      @classmethod
      def validate_future(cls, v):
          if v < datetime.now():
              raise ValueError('Must be future date')
          return v
  ```
- **Best For**: FastAPI, data model validation, API schemas
- **Documentation**: https://docs.pydantic.dev/
- **License**: MIT

#### **marshmallow** (Serialization/Deserialization)
- **Status**: Established library; pre-dates pydantic
- **Date Support**: DateTime, Date, Time fields with configurable formats
- **Best For**: API serialization, legacy applications
- **License**: MIT

---

### Java

#### **Hibernate Validator** (JSR 380)
- **Status**: Standard Java validation framework
- **Date Support**:
  - @Past, @PastOrPresent annotations
  - @Future, @FutureOrPresent annotations
  - @NotNull, @NotEmpty for temporal types
  - Custom validation constraints for date ranges
- **Best For**: Enterprise applications, JPA entities, REST validation
- **License**: Apache 2.0

#### **Apache Commons Validator**
- **Status**: Legacy option; still maintained
- **Date Support**: DateValidator for string-to-date conversion and validation
- **Best For**: Non-annotation-based validation, batch processing
- **License**: Apache 2.0

---

## Cron Expression Parsers

### **croniter** (Python)
- **Status**: Standard Python cron parser
- **Key Features**:
  - Parse standard and extended cron syntax
  - Calculate next/previous occurrence dates
  - Get cron expressions as tuples
  - Supports 5 and 6-field cron expressions
  - Timezone-aware calculations
- **Example**:
  ```python
  from croniter import croniter
  cron = croniter('0 0 * * *', datetime.now())
  next_run = cron.get_next(datetime)
  ```
- **Documentation**: https://github.com/kiorky/croniter
- **License**: Python Software Foundation

### **cron-parser** (JavaScript/Node.js)
- **Status**: Popular Node.js cron parser
- **Key Features**:
  - Parse and validate cron expressions
  - Calculate next/previous run times
  - Get interval information
  - Support for seconds field (6-field cron)
- **Example**:
  ```javascript
  const parser = require('cron-parser');
  const interval = parser.parseExpression('0 0 * * *');
  const nextDate = interval.next().toDate();
  ```
- **Documentation**: https://github.com/harrisiirak/cron-parser
- **License**: MIT

### **node-cron** (JavaScript/Node.js)
- **Status**: Scheduler with asyncio integration
- **Key Features**:
  - Schedule tasks at cron intervals
  - Support for scheduling down to seconds
  - Built-in task execution
  - Graceful shutdown support
- **Example**:
  ```javascript
  const cron = require('node-cron');
  cron.schedule('0 0 * * *', () => { /* task */ });
  ```
- **Documentation**: https://github.com/node-cron/node-cron
- **License**: MIT

### **croner** (JavaScript/Rust)
- **Status**: Modern cron implementation with better UX
- **Key Features**:
  - Timezone support in expressions
  - Syntax comparison/documentation
  - High-performance implementation
  - Pattern recognition and suggestions
- **Documentation**: https://github.com/hexagon/croner
- **License**: MIT

### **croncpp** (C++)
- **Status**: Header-only C++ library
- **Key Features**:
  - Cross-platform (C++11/14/17)
  - Parse expressions and compute next occurrences
  - No external dependencies
- **Best For**: C++ applications, embedded systems
- **License**: MIT

### **Cronsmith** (Java)
- **Status**: Complex cron expression handler
- **Key Features**:
  - Object-oriented API
  - Spring and Quartz framework integration
  - Extended syntax: 'L' (last), 'W' (weekday)
  - Fine-grained scheduling control
- **Best For**: Enterprise Java scheduling
- **License**: Apache 2.0

### **cron-converter** (Python)
- **Status**: Lightweight Python library
- **Key Features**:
  - String and list-based cron parsing
  - Datetime iteration with cron-like format
  - Timezone-aware calculations
- **License**: MIT

---

## Business Hours & Working Days

### Python

#### **python-networkdays**
- **Status**: Pure Python, no dependencies
- **Key Features**:
  - Calculate business days between dates
  - Account for weekends (configurable)
  - Holiday support
  - Optimized performance
- **Best For**: Payroll, project scheduling, date calculations
- **License**: MIT

#### **pybizday_utils**
- **Status**: Comprehensive business utilities
- **Key Features**:
  - Calculate nth business day before/after date
  - Count business days between dates
  - Find first/last business day of month
  - Add years/months with business end-of-month handling
  - Custom holiday definitions
  - Configurable working days (Mon-Fri)
- **Best For**: Financial calculations, project tracking
- **License**: BSD

#### **bizdays** (Python)
- **Status**: Flexible business day calculator
- **Key Features**:
  - Configurable working days and holidays
  - Calculate business day ranges
  - Timezone support
  - Holiday calendar management
- **Best For**: Flexible scheduling, multi-calendar systems
- **License**: Apache 2.0

#### **business** (python-business)
- **Status**: Calendar-class-based approach
- **Key Features**:
  - Calendar class with custom working days
  - Holiday lists
  - Flexible day definitions
- **Best For**: Object-oriented business logic
- **License**: MIT

#### **business_calendar**
- **Status**: Simple business day calculations
- **Key Features**:
  - Custom work week definitions
  - Holiday lists
  - Business day calculations
- **Best For**: Simple business calendar needs
- **License**: MIT

#### **NumPy / Pandas (for bulk calculations)**
- **numpy.busday_count()**: Count business days between dates
- **pandas.bdate_range()**: Generate business date ranges
- **Best For**: Vectorized calculations, large datasets
- **Documentation**: https://numpy.org/doc/stable/reference/arrays.datetimes.html

### JavaScript

#### **moment-business-days**
- **Status**: Moment.js plugin (legacy, with moment.js deprecation caveat)
- **Key Features**: Add business days, get next/previous business day
- **Depends on**: moment.js (deprecated)
- **Note**: Consider day.js or luxon alternatives for new projects

#### **business-days** (JavaScript)
- **Status**: Standalone business day calculator
- **Key Features**: Business day arithmetic, holiday support
- **Best For**: Modern JavaScript projects
- **License**: MIT

### Java

#### **WorkCalendar Pattern** (java.time-based)
- **Status**: Custom implementation using java.time
- **Approach**: Use EnumSet for working days, custom holiday calculation
- **Best For**: Enterprise Java applications
- **Example**:
  ```java
  LocalDate nextBusinessDay(LocalDate date, Set<LocalDate> holidays) {
      do {
          date = date.plusDays(1);
      } while (!isBusinessDay(date, holidays));
      return date;
  }
  ```

---

## Date Range & Period Libraries

### Python

#### **dateutil.rrule** (Recurrence Rules)
- **Status**: Part of dateutil; de facto standard
- **Key Features**:
  - Create recurring datetimes
  - RFC 5545 RRULE format
  - Support for complex patterns (FREQ, INTERVAL, UNTIL, COUNT)
  - Timezone-aware recurrence
- **Example**:
  ```python
  from dateutil.rrule import rrule, DAILY
  rrule(DAILY, count=5, dtstart=datetime.now())
  ```
- **Documentation**: https://dateutil.readthedocs.io/en/stable/rrule.html

#### **dateutil.relativedelta** (Relative Time)
- **Status**: Part of dateutil
- **Key Features**:
  - Calculate time differences
  - Add/subtract with years, months, days, hours, etc.
  - Handle DST transitions
- **Example**:
  ```python
  from dateutil.relativedelta import relativedelta
  date = datetime(2026, 1, 15)
  date + relativedelta(months=1, days=5)  # 2026-02-20
  ```

#### **arrow.range()** (Date Ranges)
- **Status**: Part of arrow library
- **Key Features**: Generate sequences of dates with custom intervals
- **Example**:
  ```python
  import arrow
  for r in arrow.utcnow().range('day', arrow.utcnow().shift(days=10)):
      print(r)
  ```

#### **pendulum.period()** (Periods)
- **Status**: Part of pendulum library
- **Key Features**: Define date/time periods with start/end
- **Example**:
  ```python
  from pendulum import parse
  period = parse('2026-01-01').range('day', parse('2026-01-31'))
  ```

### JavaScript

#### **date-fns/interval** (Functional Intervals)
- **Status**: Part of date-fns ecosystem
- **Key Features**: Calculate interval properties, check date inclusion
- **Documentation**: https://date-fns.org/

#### **moment-range** (Moment.js Plugin)
- **Status**: Moment.js plugin (legacy caveat)
- **Key Features**: Range arithmetic, inclusion checks
- **Note**: Look for day.js or luxon alternatives for new projects

---

## Localization & Internationalization (i18n)

### JavaScript/TypeScript

#### **Intl.DateTimeFormat** (Native ECMAScript API)
- **Status**: Built into all modern browsers and Node.js 12+
- **Key Features**:
  - Format dates/times according to locale
  - Timezone support
  - Customizable formatting options
  - No external dependency
- **Example**:
  ```javascript
  new Intl.DateTimeFormat('de-DE', {
    dateStyle: 'long',
    timeStyle: 'short'
  }).format(new Date())  // "15. Januar 2026, 14:30"
  ```
- **Documentation**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat

#### **Intl.RelativeTimeFormat** (Native API)
- **Status**: Modern ECMAScript API
- **Key Features**: Format relative times ("in 2 days")
- **Example**:
  ```javascript
  new Intl.RelativeTimeFormat('en-US').format(-1, 'day')  // "1 day ago"
  ```

#### **date-fns with Locales** (50+ Locales)
- **Status**: Comprehensive i18n support
- **Key Features**:
  - 50+ locale files
  - Format dates in any language
  - Relative time formatting
  - Timezone-aware formatting
- **Example**:
  ```javascript
  import { format } from 'date-fns';
  import { de } from 'date-fns/locale';
  format(new Date(), 'PPPP', { locale: de })  // "Mittwoch, 15. Januar 2026"
  ```

#### **luxon with Intl** (Intl Integration)
- **Status**: Leverages native Intl API
- **Key Features**:
  - Automatic locale detection
  - Currency, unit, and time zone formatting
  - Fallback to English for unsupported locales
- **Example**:
  ```javascript
  DateTime.now().setLocale('de').toLocaleString(DateTime.DATETIME_FULL)
  ```

#### **day.js with Locale Plugins**
- **Status**: 50+ locale plugins available
- **Key Features**: Lightweight locale support
- **Example**:
  ```javascript
  dayjs.locale('de');
  dayjs().format('LLLL')  // "Mittwoch, 15. Januar 2026"
  ```

#### **Temporal API** (with Intl Integration)
- **Status**: Emerging standard with CLDR support
- **Key Features**:
  - Multiple calendar systems (Hebrew, Islamic, Buddhist, etc.)
  - Full Intl API integration
  - Non-Gregorian calendar support
- **Example**:
  ```javascript
  Temporal.PlainDate.from('2026-01-15').toLocaleString('en-US')
  Temporal.PlainDate.from('2026-01-15').toLocaleString('ar-SA', {
    calendar: 'islamic'
  })
  ```

### Python

#### **pytz** (Timezone Localization)
- **Status**: Standard library for timezone handling
- **Key Features**:
  - Localize naive datetimes to timezones
  - Convert between timezones
  - Handle DST transitions
  - 400+ timezone definitions
- **Example**:
  ```python
  import pytz
  tz = pytz.timezone('Europe/Berlin')
  dt = datetime.now(tz=pytz.UTC).astimezone(tz)
  ```

#### **zoneinfo** (Python 3.9+)
- **Status**: Modern built-in replacement for pytz
- **Key Features**: IANA timezone database, better DST handling
- **Example**:
  ```python
  from zoneinfo import ZoneInfo
  dt = datetime.now(tz=ZoneInfo('Europe/Berlin'))
  ```

#### **Babel** (Localization Framework)
- **Status**: Comprehensive i18n framework
- **Key Features**:
  - Format dates/times for any locale
  - CLDR data support
  - 500+ locales
  - Pluralization rules
- **Example**:
  ```python
  from babel.dates import format_datetime
  format_datetime(datetime.now(), locale='de_DE')  # "15. Jan 2026"
  ```

#### **arrow with Localization**
- **Status**: i18n support via underlying dateutil
- **Example**:
  ```python
  import arrow
  arrow.now().format('DDDD', locale='de')  # "15. Januar"
  ```

### Java

#### **java.time with Locale** (java.time API)
- **Status**: Built-in localization support
- **Key Features**: Format dates/times for any locale
- **Example**:
  ```java
  DateTimeFormatter formatter = DateTimeFormatter
      .ofLocalizedDateTime(FormatStyle.LONG)
      .withLocale(Locale.GERMAN);
  formatter.format(ZonedDateTime.now());  // "15. Januar 2026"
  ```

#### **ICU4J** (Unicode CLDR Support)
- **Status**: Comprehensive internationalization library
- **Key Features**:
  - Advanced locale data
  - Complex date formatting
  - Calendar systems (Hebrew, Islamic, Buddhist, etc.)
  - 500+ locales
- **Documentation**: https://icu.unicode.org/
- **License**: Unicode License

#### **NodaTime with Culture** (NodaTime, C#/.NET)
- **Status**: Comprehensive culture support
- **Key Features**: Locale-aware formatting for any culture
- **Example**:
  ```csharp
  var fmt = CultureInfo.GetCultureInfo("de-DE");
  zonedDateTime.ToString("F", fmt);  // German long format
  ```

---

## Holiday & Calendar Management

### Python

#### **holidays** (Multi-Country Support)
- **Status**: De facto standard for holiday calculations
- **Key Features**:
  - 100+ countries and subdivisions supported
  - Fast and efficient
  - Date membership testing
  - Holiday name retrieval
  - Custom holiday additions
  - Multi-country combinations
- **Supported**: USA, India, Brazil, China, Russia, Singapore, Japan, UK, Germany, France, Canada, Australia, Mexico, and more
- **Example**:
  ```python
  import holidays
  us_holidays = holidays.US()
  if datetime(2026, 12, 25) in us_holidays:
      print(us_holidays.get(datetime(2026, 12, 25)))  # "Christmas Day"
  ```
- **Documentation**: https://github.com/vacanza/holidays
- **License**: MIT

#### **workalendar** (Calendar Systems)
- **Status**: Comprehensive calendar library
- **Key Features**:
  - Multiple calendar systems (solar, lunar, Buddhist, Islamic)
  - Holiday calendars for 100+ countries
  - Working days calculation
  - RPA Framework integration
- **Documentation**: https://github.com/novapost/workalendar
- **License**: MIT

#### **RPA Framework Calendar** (with Holidays)
- **Status**: Part of RPA Framework
- **Key Features**:
  - Integrates holidays and pendulum
  - Business day and holiday contexts
  - Custom holiday management
  - Holiday dictionary retrieval
- **Best For**: RPA workflows, business process automation
- **Documentation**: https://robocorp.com/docs/libraries/rpa-framework

### JavaScript

#### **holiday-calendar** (Multi-Country)
- **Status**: Node.js holiday library
- **Key Features**: Multi-country holiday detection
- **Best For**: Node.js applications

### Java

#### **java.time.temporal.TemporalAdjusters** (Built-in)
- **Status**: Part of java.time API
- **Key Features**: Find next/previous business day, end of month, etc.
- **Example**:
  ```java
  LocalDate nextBusinessDay = today.with(
      TemporalAdjusters.next(DayOfWeek.MONDAY)
  );
  ```

#### **jollyday** (Open Source Holiday Library)
- **Status**: Maintains holiday calendars for 100+ countries
- **Key Features**: Holiday date management, custom calendars
- **License**: Apache 2.0

---

## Relative Time & Fuzzy Parsing

### JavaScript

#### **Lately.js** (Lightweight)
- **Status**: Extremely lightweight relative time formatter
- **Bundle Size**: ~1KB
- **Key Features**: Format dates as "3 days ago", "in 2 weeks"
- **Best For**: Size-constrained projects

#### **moment.js Relative Time** (Legacy)
- **Status**: Built into moment.js, avoid for new projects
- **Example**: moment().fromNow()  // "2 hours ago"

#### **date-fns humanize** (Modern Alternative)
- **Status**: Modular relative time functions
- **Functions**: formatDistance, formatDistanceToNow, formatRelative
- **Example**:
  ```javascript
  import { formatDistanceToNow } from 'date-fns';
  formatDistanceToNow(new Date(2024, 5, 15), { addSuffix: true })  // "about 2 years ago"
  ```

#### **dayjs RelativeTime Plugin**
- **Status**: Optional plugin for day.js
- **Example**:
  ```javascript
  dayjs.extend(require('dayjs/plugin/relativeTime'));
  dayjs().fromNow()  // "a few seconds ago"
  ```

#### **Intl.RelativeTimeFormat** (Native)
- **Status**: Proper internationalized relative time
- **Best For**: Modern browsers and Node.js 12+

### Python

#### **arrow humanize()** (Friendly Format)
- **Status**: Built into arrow
- **Example**:
  ```python
  import arrow
  arrow.now().shift(days=-5).humanize()  # "5 days ago"
  ```

#### **pendulum humanize()** (Friendly Format)
- **Status**: Built into pendulum
- **Example**:
  ```python
  import pendulum
  pendulum.now().subtract(hours=3).diff_for_humans()  # "3 hours ago"
  ```

#### **Natural Language Processing** (Advanced)
- **dateutil.parser.parse()**: Fuzzy parsing
  ```python
  from dateutil import parser
  parser.parse("January 15, 2026", fuzzy=True)
  ```

---

## Timezone & DST Handling

### Best Practices for All Languages

1. **Store in UTC**: Always store dates/times in UTC internally
2. **Display in Local**: Convert to user's timezone for display only
3. **Use Tested Libraries**:
   - JavaScript: luxon, date-fns, day.js (with plugins)
   - Python: zoneinfo (3.9+) or pytz, arrow, pendulum
   - Java: java.time.ZonedDateTime
   - Go: time.LoadLocation() from standard library
   - C#: DateTimeOffset, TimeZoneInfo, or NodaTime

### DST-Aware Libraries

| Library | Language | DST Support | Notes |
|---------|----------|-------------|-------|
| **luxon** | JavaScript | Excellent | Handles ambiguous times |
| **pendulum** | Python | Excellent | Better than arrow for DST |
| **arrow** | Python | Good | DST handling adequate |
| **date-fns** | JavaScript | Good | With timezone plugin |
| **java.time** | Java | Excellent | Native DST support |
| **NodaTime** | C# | Excellent | Better than TimeZoneInfo |
| **time.LoadLocation** | Go | Excellent | IANA database built-in |
| **zoneinfo** | Python 3.9+ | Excellent | Modern standard library |

### Ambiguous/Invalid Time Handling

When clocks are set back during DST, times become ambiguous. Best libraries handle this:

- **luxon**: `Interval.fromDateTimes()` with explicit disambiguation
- **java.time**: `ZoneRules.getValidations()`
- **NodaTime**: Explicit disambiguation strategies
- **pendulum**: Automatic handling with detailed transitions

---

## Enterprise Scheduling & Temporal

### Quartz Scheduler (Java)
- **Status**: Industry standard Java job scheduling
- **Integration**: Works with java.time API
- **Key Features**: Cron-based and custom trigger scheduling
- **License**: Apache 2.0

### APScheduler (Python)
- **Status**: Advanced Python scheduler
- **Trigger Types**: cron, interval, date
- **Documentation**: https://apscheduler.readthedocs.io/
- **License**: MIT

### Bull/BullMQ (JavaScript/Node.js)
- **Status**: Redis-based job queue
- **Key Features**: Job scheduling, retry logic, persistence
- **License**: MIT

### Temporal (Distributed Workflows)
- **Status**: Open source workflow orchestration
- **Key Features**: Temporal queries on workflow history
- **Documentation**: https://temporal.io/
- **License**: Temporal Community License

---

## Quick Reference Matrix

| Use Case | JavaScript | Python | Java | Go | C# |
|----------|------------|--------|------|----|----|
| **Basic Date/Time** | day.js | datetime | java.time | time | DateTime |
| **Timezone Support** | luxon | zoneinfo | java.time | time | NodaTime |
| **Validation** | Zod, yup | pydantic | Hibernate Validator | N/A | NodaTime |
| **Cron Parsing** | cron-parser | croniter | Cronsmith | N/A | NCrontab |
| **Business Days** | business-days | bizdays | Custom | Custom | NodaTime |
| **Holidays** | holiday-calendar | holidays | jollyday | N/A | Nager.Date |
| **Localization** | date-fns | Babel | java.time | strftime | NodaTime |
| **Relative Time** | date-fns | arrow | N/A | N/A | Humanizer |
| **Recurring Events** | rrule | dateutil.rrule | Custom | Custom | NodaTime |
| **Testing** | Jest snapshots | freezegun | LocalDateTimeUtils | Custom | Moq |

---

## Installation Quick Start

### JavaScript
```bash
npm install moment@latest    # Legacy
npm install luxon            # Modern premium
npm install date-fns         # Functional approach
npm install dayjs            # Lightweight
npm install zod              # Validation
```

### Python
```bash
pip install python-dateutil  # Core utilities
pip install arrow            # Friendly API
pip install pendulum         # DST-aware
pip install pydantic         # Validation
pip install holidays         # Holiday calendars
pip install pytz             # Timezone (legacy)
```

### Java
```xml
<!-- java.time is built-in, no dependency needed -->
<!-- For enterprise scheduling -->
<dependency>
    <groupId>org.quartz-scheduler</groupId>
    <artifactId>quartz</artifactId>
    <version>2.3.2</version>
</dependency>
```

### Go
```bash
# Standard library is sufficient for most use cases
# time package is built-in
```

### C#
```bash
# NuGet - for advanced features
dotnet add package NodaTime
```

---

## Summary & Recommendations

### For New Projects
- **JavaScript**: Use **luxon** or **date-fns** (avoid moment.js)
- **Python**: Use **zoneinfo** (Python 3.9+) with **pydantic** for validation
- **Java**: Use **java.time** exclusively
- **Go**: Use standard **time** package
- **C#**: Use **DateTimeOffset** with **NodaTime** for complex scenarios

### For Enterprise Systems
- Combine a core date/time library with:
  - Validation layer (Zod, pydantic, Joi)
  - Timezone manager (luxon, zoneinfo, java.time.ZonedDateTime)
  - Business logic (bizdays/holidays library)
  - Cron support (croniter, cron-parser)
  - Testing utilities (freezegun, Jest mocks)

### For Legacy Maintenance
- **moment.js**: Still works but plan migration to luxon/date-fns
- **Joda-Time**: Superseded by java.time; migrate if possible
- **pytz**: Use zoneinfo in Python 3.9+; pytz maintained for compatibility

---

## Resources

- **Temporal API Proposal**: https://tc39.es/proposal-temporal/
- **CLDR**: https://cldr.unicode.org/
- **IANA Timezone Database**: https://www.iana.org/time-zones
- **RFC 5545 (iCalendar)**: https://tools.ietf.org/html/rfc5545
- **ISO 8601**: https://en.wikipedia.org/wiki/ISO_8601

---

**Last Updated**: 2026-01-01
**Total Libraries Covered**: 70+
**Languages**: JavaScript/TypeScript, Python, Java, Go, C#/.NET
