# Source: https://www.psycopg.org/docs/news.html

Title: Release notes — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/news.html

Markdown Content:
Current release[¶](https://www.psycopg.org/docs/news.html#current-release "Link to this heading")
-------------------------------------------------------------------------------------------------

### What’s new in psycopg 2.9.11[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-11 "Link to this heading")

* Add support for Python 3.14.

* Avoid a segfault passing more arguments than placeholders if Python is built with assertions enabled (ticket [#1791](https://github.com/psycopg/psycopg2/issues/1791)).

* Add riscv64 platform binary packages (ticket [#1813](https://github.com/psycopg/psycopg2/issues/1813)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map and [`errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") classes updated to PostgreSQL 18.

* Drop support for Python 3.8.

### What’s new in psycopg 2.9.10[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-10 "Link to this heading")

* Add support for Python 3.13.

* Receive notifications on commit (ticket [#1728](https://github.com/psycopg/psycopg2/issues/1728)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map and [`errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") classes updated to PostgreSQL 17.

* Drop support for Python 3.7.

### What’s new in psycopg 2.9.9[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-9 "Link to this heading")

* Add support for Python 3.12.

* Drop support for Python 3.6.

### What’s new in psycopg 2.9.8[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-8 "Link to this heading")

* Wheel package bundled with PostgreSQL 16 libpq in order to add support for recent features, such as `sslcertmode`.

### What’s new in psycopg 2.9.7[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-7 "Link to this heading")

* Fix propagation of exceptions raised during module initialization (ticket [#1598](https://github.com/psycopg/psycopg2/issues/1598)).

* Fix building when pg_config returns an empty string (ticket [#1599](https://github.com/psycopg/psycopg2/issues/1599)).

* Wheel package bundled with OpenSSL 1.1.1v.

### What’s new in psycopg 2.9.6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-6 "Link to this heading")

* Package manylinux 2014 for aarch64 and ppc64le platforms, in order to include libpq 15 in the binary package (ticket [#1396](https://github.com/psycopg/psycopg2/issues/1396)).

* Wheel package bundled with OpenSSL 1.1.1t.

### What’s new in psycopg 2.9.5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-5 "Link to this heading")

* Add support for Python 3.11.

* Add support for rowcount in MERGE statements in binary packages (ticket [#1497](https://github.com/psycopg/psycopg2/issues/1497)).

* Wheel package bundled with OpenSSL 1.1.1r and PostgreSQL 15 libpq.

### What’s new in psycopg 2.9.4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-4 "Link to this heading")

* Fix [`register_composite()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_composite "psycopg2.extras.register_composite"), [`register_range()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_range "psycopg2.extras.register_range") with customized `search_path` (ticket [#1487](https://github.com/psycopg/psycopg2/issues/1487)).

* Handle correctly composite types with names or in schemas requiring escape.

* Find `pg_service.conf` file in the `/etc/postgresql-common` directory in binary packages (ticket [#1365](https://github.com/psycopg/psycopg2/issues/1365)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map and [`errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") classes updated to PostgreSQL 15.

* Wheel package bundled with OpenSSL 1.1.1q and PostgreSQL 14.4 libpq.

### What’s new in psycopg 2.9.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-3 "Link to this heading")

* Alpine (musl) wheels now available (ticket [#1392](https://github.com/psycopg/psycopg2/issues/1392)).

* macOS arm64 (Apple M1) wheels now available (ticket [1482](https://github.com/psycopg/psycopg2/issues/1482)).

### What’s new in psycopg 2.9.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-2 "Link to this heading")

* Raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") for dates >= Y10k (ticket [#1307](https://github.com/psycopg/psycopg2/issues/1307)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map and [`errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") classes updated to PostgreSQL 14.

* Add preliminary support for Python 3.11 (tickets [#1376](https://github.com/psycopg/psycopg2/issues/1376), [#1386](https://github.com/psycopg/psycopg2/issues/1386)).

* Wheel package bundled with OpenSSL 1.1.1l and PostgreSQL 14.1 libpq (ticket [#1388](https://github.com/psycopg/psycopg2/issues/1388)).

### What’s new in psycopg 2.9.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9-1 "Link to this heading")

* Fix regression with named [`Placeholder`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Placeholder "psycopg2.sql.Placeholder") (ticket [#1291](https://github.com/psycopg/psycopg2/issues/1291)).

What’s new in psycopg 2.9[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

* `with connection` starts a transaction on autocommit transactions too (ticket [#941](https://github.com/psycopg/psycopg2/issues/941)).

* Timezones with fractional minutes are supported on Python 3.7 and following (ticket [#1272](https://github.com/psycopg/psycopg2/issues/1272)).

* Escape table and column names in [`copy_from()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_from "cursor.copy_from") and [`copy_to()`](https://www.psycopg.org/docs/cursor.html#cursor.copy_to "cursor.copy_to").

* Connection exceptions with sqlstate `08XXX` reclassified as [`OperationalError`](https://www.psycopg.org/docs/module.html#psycopg2.OperationalError "psycopg2.OperationalError") (a subclass of the previously used [`DatabaseError`](https://www.psycopg.org/docs/module.html#psycopg2.DatabaseError "psycopg2.DatabaseError")) (ticket [#1148](https://github.com/psycopg/psycopg2/issues/1148)).

* Include library dirs required from libpq to work around MacOS build problems (ticket [#1200](https://github.com/psycopg/psycopg2/issues/1200)).

Other changes:

* Dropped support for Python 2.7, 3.4, 3.5 (tickets [#1198](https://github.com/psycopg/psycopg2/issues/1198), [#1000](https://github.com/psycopg/psycopg2/issues/1000), [#1197](https://github.com/psycopg/psycopg2/issues/1197)).

* Dropped support for mx.DateTime.

* Use [`datetime.timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "(in Python v3.14)") objects by default in datetime objects instead of [`FixedOffsetTimezone`](https://www.psycopg.org/docs/tz.html#psycopg2.tz.FixedOffsetTimezone "psycopg2.tz.FixedOffsetTimezone").

* The [`psycopg2.tz`](https://www.psycopg.org/docs/tz.html#module-psycopg2.tz "psycopg2.tz") module is deprecated and scheduled to be dropped in the next major release.

* Provide [**PEP 599**](https://peps.python.org/pep-0599/) wheels packages (manylinux2014 tag) for i686 and x86_64 platforms.

* Provide [**PEP 600**](https://peps.python.org/pep-0600/) wheels packages (manylinux_2_24 tag) for aarch64 and ppc64le platforms.

* Wheel package bundled with OpenSSL 1.1.1k and PostgreSQL 13.3 libpq.

* Build system for Linux/MacOS binary packages moved to GitHub Actions.

### What’s new in psycopg 2.8.7[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8-7 "Link to this heading")

* Accept empty params as [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect") (ticket [#1250](https://github.com/psycopg/psycopg2/issues/1250)).

* Fix attributes refcount in `Column` initialisation (ticket [#1252](https://github.com/psycopg/psycopg2/issues/1252)).

* Allow re-initialisation of static variables in the C module (ticket [#1267](https://github.com/psycopg/psycopg2/issues/1267)).

### What’s new in psycopg 2.8.6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8-6 "Link to this heading")

* Fixed memory leak changing connection encoding to the current one (ticket [#1101](https://github.com/psycopg/psycopg2/issues/1101)).

* Fixed search of mxDateTime headers in virtualenvs (ticket [#996](https://github.com/psycopg/psycopg2/issues/996)).

* Added missing values from errorcodes (ticket [#1133](https://github.com/psycopg/psycopg2/issues/1133)).

* [`cursor.query`](https://www.psycopg.org/docs/cursor.html#cursor.query "cursor.query") reports the query of the last `COPY` operation too (ticket [#1141](https://github.com/psycopg/psycopg2/issues/1141)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map and [`errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") classes updated to PostgreSQL 13.

* Added wheel packages for ARM architecture (ticket [#1125](https://github.com/psycopg/psycopg2/issues/1125)).

* Wheel package bundled with OpenSSL 1.1.1g.

### What’s new in psycopg 2.8.5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8-5 "Link to this heading")

* Fixed use of `connection_factory` and `cursor_factory` together (ticket [#1019](https://github.com/psycopg/psycopg2/issues/1019)).

* Added support for [`LoggerAdapter`](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter "(in Python v3.14)") in [`LoggingConnection`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LoggingConnection "psycopg2.extras.LoggingConnection") (ticket [#1026](https://github.com/psycopg/psycopg2/issues/1026)).

* [`Column`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column "psycopg2.extensions.Column") objects in [`cursor.description`](https://www.psycopg.org/docs/cursor.html#cursor.description "cursor.description") can be sliced (ticket [#1034](https://github.com/psycopg/psycopg2/issues/1034)).

* Added AIX support (ticket [#1061](https://github.com/psycopg/psycopg2/issues/1061)).

* Fixed `copy()` of [`DictCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictCursor "psycopg2.extras.DictCursor") rows (ticket [#1073](https://github.com/psycopg/psycopg2/issues/1073)).

### What’s new in psycopg 2.8.4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8-4 "Link to this heading")

* Fixed building with Python 3.8 (ticket [#854](https://github.com/psycopg/psycopg2/issues/854)).

* Don’t swallow keyboard interrupts on connect when a password is specified in the connection string (ticket [#898](https://github.com/psycopg/psycopg2/issues/898)).

* Don’t advance replication cursor when the message wasn’t confirmed (ticket [#940](https://github.com/psycopg/psycopg2/issues/940)).

* Fixed inclusion of `time.h` on linux (ticket [#951](https://github.com/psycopg/psycopg2/issues/951)).

* Fixed int overflow for large values in [`table_oid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.table_oid "psycopg2.extensions.Column.table_oid") and [`type_code`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.type_code "psycopg2.extensions.Column.type_code") (ticket [#961](https://github.com/psycopg/psycopg2/issues/961)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map and [`errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") classes updated to PostgreSQL 12.

* Wheel package bundled with OpenSSL 1.1.1d and PostgreSQL at least 11.4.

### What’s new in psycopg 2.8.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8-3 "Link to this heading")

* Added _interval\_status_ parameter to [`start_replication()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "psycopg2.extras.ReplicationCursor.start_replication") method and other facilities to send automatic replication keepalives at periodic intervals (ticket [#913](https://github.com/psycopg/psycopg2/issues/913)).

* Fixed namedtuples caching introduced in 2.8 (ticket [#928](https://github.com/psycopg/psycopg2/issues/928)).

### What’s new in psycopg 2.8.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8-2 "Link to this heading")

* Fixed [`RealDictCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictCursor "psycopg2.extras.RealDictCursor") when there are repeated columns (ticket [#884](https://github.com/psycopg/psycopg2/issues/884)).

* Binary packages built with openssl 1.1.1b. Should fix concurrency problems (tickets [#543](https://github.com/psycopg/psycopg2/issues/543), [#836](https://github.com/psycopg/psycopg2/issues/836)).

### What’s new in psycopg 2.8.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8-1 "Link to this heading")

* Fixed [`RealDictRow`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictRow "psycopg2.extras.RealDictRow") modifiability (ticket [#886](https://github.com/psycopg/psycopg2/issues/886)).

* Fixed “there’s no async cursor” error polling a connection with no cursor (ticket [#887](https://github.com/psycopg/psycopg2/issues/887)).

What’s new in psycopg 2.8[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

New features:

* Added [`errors`](https://www.psycopg.org/docs/errors.html#module-psycopg2.errors "psycopg2.errors") module. Every PostgreSQL error is converted into a specific exception class (ticket [#682](https://github.com/psycopg/psycopg2/issues/682)).

* Added [`encrypt_password()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.encrypt_password "psycopg2.extensions.encrypt_password") function (ticket [#576](https://github.com/psycopg/psycopg2/issues/576)).

* Added [`BYTES`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.BYTES "psycopg2.extensions.BYTES") adapter to manage databases with mixed encodings on Python 3 (ticket [#835](https://github.com/psycopg/psycopg2/issues/835)).

* Added [`table_oid`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.table_oid "psycopg2.extensions.Column.table_oid") and [`table_column`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Column.table_column "psycopg2.extensions.Column.table_column") attributes on [`cursor.description`](https://www.psycopg.org/docs/cursor.html#cursor.description "cursor.description") items (ticket [#661](https://github.com/psycopg/psycopg2/issues/661)).

* Added [`connection.info`](https://www.psycopg.org/docs/connection.html#connection.info "connection.info") object to retrieve various PostgreSQL connection information (ticket [#726](https://github.com/psycopg/psycopg2/issues/726)).

* Added [`get_native_connection()`](https://www.psycopg.org/docs/connection.html#connection.get_native_connection "connection.get_native_connection") to expose the raw `PGconn` structure to C extensions via Capsule (ticket [#782](https://github.com/psycopg/psycopg2/issues/782)).

* Added [`pgconn_ptr`](https://www.psycopg.org/docs/connection.html#connection.pgconn_ptr "connection.pgconn_ptr") and [`pgresult_ptr`](https://www.psycopg.org/docs/cursor.html#cursor.pgresult_ptr "cursor.pgresult_ptr") to expose raw C structures to Python and interact with libpq via ctypes (ticket [#782](https://github.com/psycopg/psycopg2/issues/782)).

* [`Identifier`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Identifier "psycopg2.sql.Identifier") can represent qualified names in SQL composition (ticket [#732](https://github.com/psycopg/psycopg2/issues/732)).

* Added `ReplicationCursor`.[`wal_end`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.wal_end "psycopg2.extras.ReplicationCursor.wal_end") attribute (ticket [#800](https://github.com/psycopg/psycopg2/issues/800)).

* Added _fetch_ parameter to [`execute_values()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.execute_values "psycopg2.extras.execute_values") function (ticket [#813](https://github.com/psycopg/psycopg2/issues/813)).

* `str()` on [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") produces a human-readable representation (ticket [#773](https://github.com/psycopg/psycopg2/issues/773)).

* [`DictCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictCursor "psycopg2.extras.DictCursor") and [`RealDictCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictCursor "psycopg2.extras.RealDictCursor") rows maintain columns order (ticket [#177](https://github.com/psycopg/psycopg2/issues/177)).

* Added [`severity_nonlocalized`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics.severity_nonlocalized "psycopg2.extensions.Diagnostics.severity_nonlocalized") attribute on the [`Diagnostics`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics "psycopg2.extensions.Diagnostics") object (ticket [#783](https://github.com/psycopg/psycopg2/issues/783)).

* More efficient [`NamedTupleCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.NamedTupleCursor "psycopg2.extras.NamedTupleCursor") (ticket [#838](https://github.com/psycopg/psycopg2/issues/838)).

Bug fixes:

* Fixed connections occasionally broken by the unrelated use of the multiprocessing module (ticket [#829](https://github.com/psycopg/psycopg2/issues/829)).

* Fixed async communication blocking if results are returned in different chunks, e.g. with notices interspersed to the results (ticket [#856](https://github.com/psycopg/psycopg2/issues/856)).

* Fixed adaptation of numeric subclasses such as [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python v3.14)") (ticket [#591](https://github.com/psycopg/psycopg2/issues/591)).

Other changes:

* Dropped support for Python 2.6, 3.2, 3.3.

* Dropped `psycopg1` module.

* Dropped deprecated `register_tstz_w_secs()` (was previously a no-op).

* Dropped deprecated `PersistentConnectionPool`. This pool class was mostly designed to interact with Zope. Use `ZPsycopgDA.pool` instead.

* Binary packages no longer installed by default. The ‘psycopg2-binary’ package must be used explicitly.

* Dropped `PSYCOPG_DISPLAY_SIZE` build parameter.

* Dropped support for mxDateTime as the default date and time adapter. mxDatetime support continues to be available as an alternative to Python’s builtin datetime.

* No longer use 2to3 during installation for Python 2 & 3 compatibility. All source files are now compatible with Python 2 & 3 as is.

* The `psycopg2.test` package is no longer installed by

```
python setup.py
install
```

.

* Wheel package bundled with OpenSSL 1.0.2r and PostgreSQL 11.2 libpq.

### What’s new in psycopg 2.7.7[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-7 "Link to this heading")

* Cleanup of the cursor results assignment code, which might have solved double free and inconsistencies in concurrent usage (tickets [#346](https://github.com/psycopg/psycopg2/issues/346), [#384](https://github.com/psycopg/psycopg2/issues/384)).

* Wheel package bundled with OpenSSL 1.0.2q.

### What’s new in psycopg 2.7.6.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-6-1 "Link to this heading")

* Fixed binary package broken on OS X 10.12 (ticket [#807](https://github.com/psycopg/psycopg2/issues/807)).

* Wheel package bundled with PostgreSQL 11.1 libpq.

### What’s new in psycopg 2.7.6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-6 "Link to this heading")

* Close named cursors if exist, even if [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") wasn’t called (ticket [#746](https://github.com/psycopg/psycopg2/issues/746)).

* Fixed building on modern FreeBSD versions with Python 3.7 (ticket [#755](https://github.com/psycopg/psycopg2/issues/755)).

* Fixed hang trying to `COPY` via [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") in asynchronous connections (ticket [#781](https://github.com/psycopg/psycopg2/issues/781)).

* Fixed adaptation of arrays of empty arrays (ticket [#788](https://github.com/psycopg/psycopg2/issues/788)).

* Fixed segfault accessing the connection’s [`readonly`](https://www.psycopg.org/docs/connection.html#connection.readonly "connection.readonly") and [`deferrable`](https://www.psycopg.org/docs/connection.html#connection.deferrable "connection.deferrable") attributes repeatedly (ticket [#790](https://github.com/psycopg/psycopg2/issues/790)).

* [`execute_values()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.execute_values "psycopg2.extras.execute_values") accepts [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") objects (ticket [#794](https://github.com/psycopg/psycopg2/issues/794)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map updated to PostgreSQL 11.

* Wheel package bundled with PostgreSQL 10.5 libpq and OpenSSL 1.0.2p.

### What’s new in psycopg 2.7.5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-5 "Link to this heading")

* Allow non-ascii chars in namedtuple fields (regression introduced fixing ticket [#211](https://github.com/psycopg/psycopg2/issues/211)).

* Fixed adaptation of arrays of arrays of nulls (ticket [#325](https://github.com/psycopg/psycopg2/issues/325)).

* Fixed building on Solaris 11 and derivatives such as SmartOS and illumos (ticket [#677](https://github.com/psycopg/psycopg2/issues/677)).

* Maybe fixed building on MSYS2 (as reported in ticket [#658](https://github.com/psycopg/psycopg2/issues/658)).

* Allow string subclasses in connection and other places (ticket [#679](https://github.com/psycopg/psycopg2/issues/679)).

* Don’t raise an exception closing an unused named cursor (ticket [#716](https://github.com/psycopg/psycopg2/issues/716)).

* Wheel package bundled with PostgreSQL 10.4 libpq and OpenSSL 1.0.2o.

### What’s new in psycopg 2.7.4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-4 "Link to this heading")

* Moving away from installing the wheel package by default. Packages installed from wheel raise a warning on import. Added package `psycopg2-binary` to install from wheel instead (ticket [#543](https://github.com/psycopg/psycopg2/issues/543)).

* Convert fields names into valid Python identifiers in [`NamedTupleCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.NamedTupleCursor "psycopg2.extras.NamedTupleCursor") (ticket [#211](https://github.com/psycopg/psycopg2/issues/211)).

* Fixed Solaris 10 support (ticket [#532](https://github.com/psycopg/psycopg2/issues/532)).

* [`cursor.mogrify()`](https://www.psycopg.org/docs/cursor.html#cursor.mogrify "cursor.mogrify") can be called on closed cursors (ticket [#579](https://github.com/psycopg/psycopg2/issues/579)).

* Fixed setting session characteristics in corner cases on autocommit connections (ticket [#580](https://github.com/psycopg/psycopg2/issues/580)).

* Fixed [`MinTimeLoggingCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingCursor "psycopg2.extras.MinTimeLoggingCursor") on Python 3 (ticket [#609](https://github.com/psycopg/psycopg2/issues/609)).

* Fixed parsing of array of points as floats (ticket [#613](https://github.com/psycopg/psycopg2/issues/613)).

* Fixed [`__libpq_version__`](https://www.psycopg.org/docs/module.html#psycopg2.__libpq_version__ "psycopg2.__libpq_version__") building with libpq >= 10.1 (ticket [#632](https://github.com/psycopg/psycopg2/issues/632)).

* Fixed [`rowcount`](https://www.psycopg.org/docs/cursor.html#cursor.rowcount "cursor.rowcount") after [`executemany()`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany") with `RETURNING` statements (ticket [#633](https://github.com/psycopg/psycopg2/issues/633)).

* Fixed compatibility problem with pypy3 (ticket [#649](https://github.com/psycopg/psycopg2/issues/649)).

* Wheel packages bundled with PostgreSQL 10.1 libpq and OpenSSL 1.0.2n.

* Wheel packages for Python 2.6 no more available (support dropped from wheel building infrastructure).

### What’s new in psycopg 2.7.3.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-3-2 "Link to this heading")

* Wheel package bundled with PostgreSQL 10.0 libpq and OpenSSL 1.0.2l (tickets [#601](https://github.com/psycopg/psycopg2/issues/601), [#602](https://github.com/psycopg/psycopg2/issues/602)).

### What’s new in psycopg 2.7.3.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-3-1 "Link to this heading")

* Dropped libresolv from wheel package to avoid incompatibility with glibc 2.26 (wheels ticket #2).

### What’s new in psycopg 2.7.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-3 "Link to this heading")

* Restored default `timestamptz[]` typecasting to Python `datetime`. Regression introduced in Psycopg 2.7.2 (ticket [#578](https://github.com/psycopg/psycopg2/issues/578)).

### What’s new in psycopg 2.7.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-2 "Link to this heading")

* Fixed inconsistent state in externally closed connections (tickets [#263](https://github.com/psycopg/psycopg2/issues/263), [#311](https://github.com/psycopg/psycopg2/issues/311), [#443](https://github.com/psycopg/psycopg2/issues/443)). Was fixed in 2.6.2 but not included in 2.7 by mistake.

* Fixed Python exceptions propagation in green callback (ticket [#410](https://github.com/psycopg/psycopg2/issues/410)).

* Don’t display the password in [`connection.dsn`](https://www.psycopg.org/docs/connection.html#connection.dsn "connection.dsn") when the connection string is specified as an URI (ticket [#528](https://github.com/psycopg/psycopg2/issues/528)).

* Return objects with timezone parsing “infinity” `timestamptz` (ticket [#536](https://github.com/psycopg/psycopg2/issues/536)).

* Dropped dependency on VC9 runtime on Windows binary packages (ticket [#541](https://github.com/psycopg/psycopg2/issues/541)).

* Fixed segfault in [`lobject()`](https://www.psycopg.org/docs/connection.html#connection.lobject "connection.lobject") when _mode_=`None` (ticket [#544](https://github.com/psycopg/psycopg2/issues/544)).

* Fixed [`lobject()`](https://www.psycopg.org/docs/connection.html#connection.lobject "connection.lobject") keyword argument _lobject\_factory_ (ticket [#545](https://github.com/psycopg/psycopg2/issues/545)).

* Fixed [`consume_stream()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream "psycopg2.extras.ReplicationCursor.consume_stream")_keepalive\_interval_ argument (ticket [#547](https://github.com/psycopg/psycopg2/issues/547)).

* Maybe fixed random import error on Python 3.6 in multiprocess environment (ticket [#550](https://github.com/psycopg/psycopg2/issues/550)).

* Fixed random `SystemError` upon receiving abort signal (ticket [#551](https://github.com/psycopg/psycopg2/issues/551)).

* Accept [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") objects in [`start_replication_expert()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication_expert "psycopg2.extras.ReplicationCursor.start_replication_expert") (ticket [#554](https://github.com/psycopg/psycopg2/issues/554)).

* Parse intervals returned as microseconds from Redshift (ticket [#558](https://github.com/psycopg/psycopg2/issues/558)).

* Added [`Json`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Json "psycopg2.extras.Json")`prepare()` method to consider connection params when adapting (ticket [#562](https://github.com/psycopg/psycopg2/issues/562)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map updated to PostgreSQL 10 beta 1.

### What’s new in psycopg 2.7.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7-1 "Link to this heading")

* Ignore `None` arguments passed to [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect") and [`make_dsn()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.make_dsn "psycopg2.extensions.make_dsn") (ticket [#517](https://github.com/psycopg/psycopg2/issues/517)).

* OpenSSL upgraded from major version 0.9.8 to 1.0.2 in the Linux wheel packages (ticket [#518](https://github.com/psycopg/psycopg2/issues/518)).

* Fixed build with libpq versions < 9.3 (ticket [#520](https://github.com/psycopg/psycopg2/issues/520)).

What’s new in psycopg 2.7[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

New features:

* Added [`sql`](https://www.psycopg.org/docs/sql.html#module-psycopg2.sql "psycopg2.sql") module to generate SQL dynamically (ticket [#308](https://github.com/psycopg/psycopg2/issues/308)).

* Added [Replication protocol support](https://www.psycopg.org/docs/advanced.html#replication-support) (ticket [#322](https://github.com/psycopg/psycopg2/issues/322)). Main authors are Oleksandr Shulgin and Craig Ringer, who deserve a huge thank you.

* Added [`parse_dsn()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.parse_dsn "psycopg2.extensions.parse_dsn") and [`make_dsn()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.make_dsn "psycopg2.extensions.make_dsn") functions (tickets [#321](https://github.com/psycopg/psycopg2/issues/321), [#363](https://github.com/psycopg/psycopg2/issues/363)). [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect") now can take both _dsn_ and keyword arguments, merging them together.

* Added [`__libpq_version__`](https://www.psycopg.org/docs/module.html#psycopg2.__libpq_version__ "psycopg2.__libpq_version__") and [`libpq_version()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.libpq_version "psycopg2.extensions.libpq_version") to inspect the version of the `libpq` library the module was bundled with (tickets [#35](https://github.com/psycopg/psycopg2/issues/35), [#323](https://github.com/psycopg/psycopg2/issues/323)).

* The attributes [`notices`](https://www.psycopg.org/docs/connection.html#connection.notices "connection.notices") and [`notifies`](https://www.psycopg.org/docs/connection.html#connection.notifies "connection.notifies") can be customized replacing them with any object exposing an `append()` method (ticket [#326](https://github.com/psycopg/psycopg2/issues/326)).

* Adapt network types to [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "(in Python v3.14)") objects when available. When not enabled, convert arrays of network types to lists by default. The old `Inet` adapter is deprecated (tickets [#317](https://github.com/psycopg/psycopg2/issues/317), [#343](https://github.com/psycopg/psycopg2/issues/343), [#387](https://github.com/psycopg/psycopg2/issues/387)).

* Added [`quote_ident()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.quote_ident "psycopg2.extensions.quote_ident") function (ticket [#359](https://github.com/psycopg/psycopg2/issues/359)).

* Added [`get_dsn_parameters()`](https://www.psycopg.org/docs/connection.html#connection.get_dsn_parameters "connection.get_dsn_parameters") connection method (ticket [#364](https://github.com/psycopg/psycopg2/issues/364)).

* [`callproc()`](https://www.psycopg.org/docs/cursor.html#cursor.callproc "cursor.callproc") now accepts a dictionary of parameters (ticket [#381](https://github.com/psycopg/psycopg2/issues/381)).

* Give precedence to `__conform__()` over superclasses to choose an object adapter (ticket [#456](https://github.com/psycopg/psycopg2/issues/456)).

* Using Python C API decoding functions and codecs caching for faster unicode encoding/decoding (ticket [#473](https://github.com/psycopg/psycopg2/issues/473)).

* [`executemany()`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany") slowness addressed by [`execute_batch()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.execute_batch "psycopg2.extras.execute_batch") and [`execute_values()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.execute_values "psycopg2.extras.execute_values") (ticket [#491](https://github.com/psycopg/psycopg2/issues/491)).

* Added `async_` as an alias for `async` to support Python 3.7 where `async` will become a keyword (ticket [#495](https://github.com/psycopg/psycopg2/issues/495)).

* Unless in autocommit, do not use `default_transaction_*` settings to control the session characteristics as it may create problems with external connection pools such as pgbouncer; use `BEGIN` options instead (ticket [#503](https://github.com/psycopg/psycopg2/issues/503)).

* [`isolation_level`](https://www.psycopg.org/docs/connection.html#connection.isolation_level "connection.isolation_level") is now writable and entirely separated from [`autocommit`](https://www.psycopg.org/docs/connection.html#connection.autocommit "connection.autocommit"); added [`readonly`](https://www.psycopg.org/docs/connection.html#connection.readonly "connection.readonly"), [`deferrable`](https://www.psycopg.org/docs/connection.html#connection.deferrable "connection.deferrable") writable attributes.

Bug fixes:

* Throw an exception trying to pass `NULL` chars as parameters (ticket [#420](https://github.com/psycopg/psycopg2/issues/420)).

* Fixed error caused by missing decoding [`LoggingConnection`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LoggingConnection "psycopg2.extras.LoggingConnection") (ticket [#483](https://github.com/psycopg/psycopg2/issues/483)).

* Fixed integer overflow in `interval` seconds (ticket [#512](https://github.com/psycopg/psycopg2/issues/512)).

* Make [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") objects picklable (ticket [#462](https://github.com/psycopg/psycopg2/issues/462)).

* Fixed version parsing and building with PostgreSQL 10 (ticket [#489](https://github.com/psycopg/psycopg2/issues/489)).

Other changes:

* Dropped support for Python 2.5 and 3.1.

* Dropped support for client library older than PostgreSQL 9.1 (but older server versions are still supported).

* [`isolation_level`](https://www.psycopg.org/docs/connection.html#connection.isolation_level "connection.isolation_level") doesn’t read from the database but will return [`ISOLATION_LEVEL_DEFAULT`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISOLATION_LEVEL_DEFAULT "psycopg2.extensions.ISOLATION_LEVEL_DEFAULT") if no value was set on the connection.

* Empty arrays no more converted into lists if they don’t have a type attached (ticket [#506](https://github.com/psycopg/psycopg2/issues/506))

### What’s new in psycopg 2.6.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-6-2 "Link to this heading")

* Fixed inconsistent state in externally closed connections (tickets [#263](https://github.com/psycopg/psycopg2/issues/263), [#311](https://github.com/psycopg/psycopg2/issues/311), [#443](https://github.com/psycopg/psycopg2/issues/443)).

* Report the server response status on errors (such as ticket [#281](https://github.com/psycopg/psycopg2/issues/281)).

* Raise `NotSupportedError` on unhandled server response status (ticket [#352](https://github.com/psycopg/psycopg2/issues/352)).

* Allow overriding string adapter encoding with no connection (ticket [#331](https://github.com/psycopg/psycopg2/issues/331)).

* The [`wait_select`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.wait_select "psycopg2.extras.wait_select") callback allows interrupting a long-running query in an interactive shell using Ctrl-C (ticket [#333](https://github.com/psycopg/psycopg2/issues/333)).

* Fixed `PersistentConnectionPool` on Python 3 (ticket [#348](https://github.com/psycopg/psycopg2/issues/348)).

* Fixed segfault on `repr()` of an unitialized connection (ticket [#361](https://github.com/psycopg/psycopg2/issues/361)).

* Allow adapting bytes using [`QuotedString`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.QuotedString "psycopg2.extensions.QuotedString") on Python 3 (ticket [#365](https://github.com/psycopg/psycopg2/issues/365)).

* Added support for setuptools/wheel (ticket [#370](https://github.com/psycopg/psycopg2/issues/370)).

* Fix build on Windows with Python 3.5, VS 2015 (ticket [#380](https://github.com/psycopg/psycopg2/issues/380)).

* Fixed `errorcodes.lookup` initialization thread-safety (ticket [#382](https://github.com/psycopg/psycopg2/issues/382)).

* Fixed `read()` exception propagation in copy_from (ticket [#412](https://github.com/psycopg/psycopg2/issues/412)).

* Fixed possible NULL TZ decref (ticket [#424](https://github.com/psycopg/psycopg2/issues/424)).

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map updated to PostgreSQL 9.5.

### What’s new in psycopg 2.6.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-6-1 "Link to this heading")

* Lists consisting of only [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") are escaped correctly (ticket [#285](https://github.com/psycopg/psycopg2/issues/285)).

* Fixed deadlock in multithread programs using OpenSSL (ticket [#290](https://github.com/psycopg/psycopg2/issues/290)).

* Correctly unlock the connection after error in flush (ticket [#294](https://github.com/psycopg/psycopg2/issues/294)).

* Fixed `MinTimeLoggingCursor.callproc()` (ticket [#309](https://github.com/psycopg/psycopg2/issues/309)).

* Added support for MSVC 2015 compiler (ticket [#350](https://github.com/psycopg/psycopg2/issues/350)).

What’s new in psycopg 2.6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-6 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

New features:

* Added support for large objects larger than 2GB. Many thanks to Blake Rouse and the MAAS Team for the feature development.

* Python [`time`](https://docs.python.org/3/library/time.html#module-time "(in Python v3.14)") objects with a tzinfo specified and PostgreSQL `timetz` data are converted into each other (ticket [#272](https://github.com/psycopg/psycopg2/issues/272)).

Bug fixes:

* Json adapter’s `str()` returns the adapted content instead of the `repr()` (ticket [#191](https://github.com/psycopg/psycopg2/issues/191)).

### What’s new in psycopg 2.5.5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-5-5 "Link to this heading")

* Named cursors used as context manager don’t swallow the exception on exit (ticket [#262](https://github.com/psycopg/psycopg2/issues/262)).

* [`cursor.description`](https://www.psycopg.org/docs/cursor.html#cursor.description "cursor.description") can be pickled (ticket [#265](https://github.com/psycopg/psycopg2/issues/265)).

* Propagate read error messages in COPY FROM (ticket [#270](https://github.com/psycopg/psycopg2/issues/270)).

* PostgreSQL time 24:00 is converted to Python 00:00 (ticket [#278](https://github.com/psycopg/psycopg2/issues/278)).

### What’s new in psycopg 2.5.4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-5-4 "Link to this heading")

* Added `jsonb` support for PostgreSQL 9.4 (ticket [#226](https://github.com/psycopg/psycopg2/issues/226)).

* Fixed segfault if COPY statements are passed to [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") instead of using the proper methods (ticket [#219](https://github.com/psycopg/psycopg2/issues/219)).

* Force conversion of pool arguments to integer to avoid potentially unbounded pools (ticket [#220](https://github.com/psycopg/psycopg2/issues/220)).

* Cursors `WITH HOLD` don’t begin a new transaction upon move/fetch/close (ticket [#228](https://github.com/psycopg/psycopg2/issues/228)).

* Cursors `WITH HOLD` can be used in autocommit (ticket [#229](https://github.com/psycopg/psycopg2/issues/229)).

* [`callproc()`](https://www.psycopg.org/docs/cursor.html#cursor.callproc "cursor.callproc") doesn’t silently ignore an argument without a length.

* Fixed memory leak with large objects (ticket [#256](https://github.com/psycopg/psycopg2/issues/256)).

* Make sure the internal `_psycopg.so` module can be imported stand-alone (to allow modules juggling such as the one described in ticket [#201](https://github.com/psycopg/psycopg2/issues/201)).

### What’s new in psycopg 2.5.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-5-3 "Link to this heading")

* Work around [pip issue #1630](https://github.com/pypa/pip/issues/1630) making installation via `pip -e git+url` impossible (ticket [#18](https://github.com/psycopg/psycopg2/issues/248)).

* Copy operations correctly set the [`cursor.rowcount`](https://www.psycopg.org/docs/cursor.html#cursor.rowcount "cursor.rowcount") attribute (ticket [#180](https://github.com/psycopg/psycopg2/issues/180)).

* It is now possible to call `get_transaction_status()` on closed connections.

* Fixed unsafe access to object names causing assertion failures in Python 3 debug builds (ticket [#188](https://github.com/psycopg/psycopg2/issues/188)).

* Mark the connection closed if found broken on `poll()` (from ticket [#192](https://github.com/psycopg/psycopg2/issues/192) discussion)

* Fixed handling of dsn and closed attributes in connection subclasses failing to connect (from ticket [#192](https://github.com/psycopg/psycopg2/issues/192) discussion).

* Added arbitrary but stable order to `Range` objects, thanks to Chris Withers (ticket [#193](https://github.com/psycopg/psycopg2/issues/193)).

* Avoid blocking async connections on connect (ticket [#194](https://github.com/psycopg/psycopg2/issues/194)). Thanks to Adam Petrovich for the bug report and diagnosis.

* Don’t segfault using poorly defined cursor subclasses which forgot to call the superclass init (ticket [#195](https://github.com/psycopg/psycopg2/issues/195)).

* Mark the connection closed when a Socket connection is broken, as it happens for TCP connections instead (ticket [#196](https://github.com/psycopg/psycopg2/issues/196)).

* Fixed overflow opening a lobject with an oid not fitting in a signed int (ticket [#203](https://github.com/psycopg/psycopg2/issues/203)).

* Fixed handling of explicit default `cursor_factory=None` in [`connection.cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor") (ticket [#210](https://github.com/psycopg/psycopg2/issues/210)).

* Fixed possible segfault in named cursors creation.

* Fixed debug build on Windows, thanks to James Emerton.

### What’s new in psycopg 2.5.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-5-2 "Link to this heading")

* Fixed segfault pickling the exception raised on connection error (ticket [#170](https://github.com/psycopg/psycopg2/issues/170)).

* Meaningful connection errors report a meaningful message, thanks to Alexey Borzenkov (ticket [#173](https://github.com/psycopg/psycopg2/issues/173)).

* Manually creating `lobject` with the wrong parameter doesn’t segfault (ticket [#187](https://github.com/psycopg/psycopg2/issues/187)).

### What’s new in psycopg 2.5.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-5-1 "Link to this heading")

* Fixed build on Solaris 10 and 11 where the round() function is already declared (ticket [#146](https://github.com/psycopg/psycopg2/issues/146)).

* Fixed comparison of `Range` with non-range objects (ticket [#164](https://github.com/psycopg/psycopg2/issues/164)). Thanks to Chris Withers for the patch.

* Fixed double-free on connection dealloc (ticket [#166](https://github.com/psycopg/psycopg2/issues/166)). Thanks to Gangadharan S.A. for the report and fix suggestion.

What’s new in psycopg 2.5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-5 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

New features:

* Added [JSON adaptation](https://www.psycopg.org/docs/extras.html#adapt-json).

* Added [support for PostgreSQL 9.2 range types](https://www.psycopg.org/docs/extras.html#adapt-range).

* [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") and [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor") objects can be used in `with` statements as context managers as specified by recent [DB API 2.0](https://www.python.org/dev/peps/pep-0249/) extension.

* Added [`Diagnostics`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Diagnostics "psycopg2.extensions.Diagnostics") object to get extended info from a database error. Many thanks to Matthew Woodcraft for the implementation (ticket [#149](https://github.com/psycopg/psycopg2/issues/149)).

* Added [`connection.cursor_factory`](https://www.psycopg.org/docs/connection.html#connection.cursor_factory "connection.cursor_factory") attribute to customize the default object returned by [`cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor").

* Added support for backward scrollable cursors. Thanks to Jon Nelson for the initial patch (ticket [#108](https://github.com/psycopg/psycopg2/issues/108)).

* Added a simple way to [customize casting of composite types](https://www.psycopg.org/docs/extras.html#adapt-composite) into Python objects other than namedtuples. Many thanks to Ronan Dunklau and Tobias Oberstein for the feature development.

* [`connection.reset()`](https://www.psycopg.org/docs/connection.html#connection.reset "connection.reset") implemented using `DISCARD ALL` on server versions supporting it.

Bug fixes:

* Properly cleanup memory of broken connections (ticket [#148](https://github.com/psycopg/psycopg2/issues/148)).

* Fixed bad interaction of `setup.py` with other dependencies in Distribute projects on Python 3 (ticket [#153](https://github.com/psycopg/psycopg2/issues/153)).

Other changes:

* Added support for Python 3.3.

* Dropped support for Python 2.4. Please use Psycopg 2.4.x if you need it.

* [`errorcodes`](https://www.psycopg.org/docs/errorcodes.html#module-psycopg2.errorcodes "psycopg2.errorcodes") map updated to PostgreSQL 9.2.

* Dropped Zope adapter from source repository. ZPsycopgDA now has its own project at <[https://github.com/psycopg/ZPsycopgDA](https://github.com/psycopg/ZPsycopgDA)>.

### What’s new in psycopg 2.4.6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4-6 "Link to this heading")

* Fixed ‘cursor()’ arguments propagation in connection subclasses and overriding of the ‘cursor_factory’ argument. Thanks to Corry Haines for the report and the initial patch (ticket [#105](https://github.com/psycopg/psycopg2/issues/105)).

* Dropped GIL release during string adaptation around a function call invoking a Python API function, which could cause interpreter crash. Thanks to Manu Cupcic for the report (ticket [#110](https://github.com/psycopg/psycopg2/issues/110)).

* Close a green connection if there is an error in the callback. Maybe a harsh solution but it leaves the program responsive (ticket [#113](https://github.com/psycopg/psycopg2/issues/113)).

* ‘register_hstore()’, ‘register_composite()’, ‘tpc_recover()’ work with RealDictConnection and Cursor (ticket [#114](https://github.com/psycopg/psycopg2/issues/114)).

* Fixed broken pool for Zope and connections re-init across ZSQL methods in the same request (tickets [#123](https://github.com/psycopg/psycopg2/issues/123), [#125](https://github.com/psycopg/psycopg2/issues/125), [#142](https://github.com/psycopg/psycopg2/issues/142)).

* connect() raises an exception instead of swallowing keyword arguments when a connection string is specified as well (ticket [#131](https://github.com/psycopg/psycopg2/issues/131)).

* Discard any result produced by ‘executemany()’ (ticket [#133](https://github.com/psycopg/psycopg2/issues/133)).

* Fixed pickling of FixedOffsetTimezone objects (ticket [#135](https://github.com/psycopg/psycopg2/issues/135)).

* Release the GIL around PQgetResult calls after COPY (ticket [#140](https://github.com/psycopg/psycopg2/issues/140)).

* Fixed empty strings handling in composite caster (ticket [#141](https://github.com/psycopg/psycopg2/issues/141)).

* Fixed pickling of DictRow and RealDictRow objects.

### What’s new in psycopg 2.4.5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4-5 "Link to this heading")

* The close() methods on connections and cursors don’t raise exceptions if called on already closed objects.

* Fixed fetchmany() with no argument in cursor subclasses (ticket [#84](https://github.com/psycopg/psycopg2/issues/84)).

* Use lo_creat() instead of lo_create() when possible for better interaction with pgpool-II (ticket [#88](https://github.com/psycopg/psycopg2/issues/88)).

* Error and its subclasses are picklable, useful for multiprocessing interaction (ticket [#90](https://github.com/psycopg/psycopg2/issues/90)).

* Better efficiency and formatting of timezone offset objects thanks to Menno Smits (tickets [#94](https://github.com/psycopg/psycopg2/issues/94), [#95](https://github.com/psycopg/psycopg2/issues/95)).

* Fixed ‘rownumber’ during iteration on cursor subclasses. Regression introduced in 2.4.4 (ticket [#100](https://github.com/psycopg/psycopg2/issues/100)).

* Added support for ‘inet’ arrays.

* Fixed ‘commit()’ concurrency problem (ticket [#103](https://github.com/psycopg/psycopg2/issues/103)).

* Codebase cleaned up using the GCC Python plugin’s static analysis tool, which has revealed several unchecked return values, possible NULL dereferences, reference counting problems. Many thanks to David Malcolm for the useful tool and the assistance provided using it.

### What’s new in psycopg 2.4.4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4-4 "Link to this heading")

* ‘register_composite()’ also works with the types implicitly defined after a table row, not only with the ones created by ‘CREATE TYPE’.

* Values for the isolation level symbolic constants restored to what they were before release 2.4.2 to avoid breaking apps using the values instead of the constants.

* Named DictCursor/RealDictCursor honour itersize (ticket [#80](https://github.com/psycopg/psycopg2/issues/80)).

* Fixed rollback on error on Zope (ticket [#73](https://github.com/psycopg/psycopg2/issues/73)).

* Raise ‘DatabaseError’ instead of ‘Error’ with empty libpq errors, consistently with other disconnection-related errors: regression introduced in release 2.4.1 (ticket [#82](https://github.com/psycopg/psycopg2/issues/82)).

### What’s new in psycopg 2.4.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4-3 "Link to this heading")

* connect() supports all the keyword arguments supported by the database

* Added ‘new_array_type()’ function for easy creation of array typecasters.

* Added support for arrays of hstores and composite types (ticket [#66](https://github.com/psycopg/psycopg2/issues/66)).

* Fixed segfault in case of transaction started with connection lost (and possibly other events).

* Fixed adaptation of Decimal type in sub-interpreters, such as in certain mod_wsgi configurations (ticket [#52](https://github.com/psycopg/psycopg2/issues/52)).

* Rollback connections in transaction or in error before putting them back into a pool. Also discard broken connections (ticket [#62](https://github.com/psycopg/psycopg2/issues/62)).

* Lazy import of the slow uuid module, thanks to Marko Kreen.

* Fixed NamedTupleCursor.executemany() (ticket [#65](https://github.com/psycopg/psycopg2/issues/65)).

* Fixed –static-libpq setup option (ticket [#64](https://github.com/psycopg/psycopg2/issues/64)).

* Fixed interaction between RealDictCursor and named cursors (ticket [#67](https://github.com/psycopg/psycopg2/issues/67)).

* Dropped limit on the columns length in COPY operations (ticket [#68](https://github.com/psycopg/psycopg2/issues/68)).

* Fixed reference leak with arguments referenced more than once in queries (ticket [#81](https://github.com/psycopg/psycopg2/issues/81)).

* Fixed typecasting of arrays containing consecutive backslashes.

* ‘errorcodes’ map updated to PostgreSQL 9.1.

### What’s new in psycopg 2.4.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4-2 "Link to this heading")

* Added ‘set_session()’ method and ‘autocommit’ property to the connection. Added support for read-only sessions and, for PostgreSQL 9.1, for the “repeatable read” isolation level and the “deferrable” transaction property.

* Psycopg doesn’t execute queries at connection time to find the default isolation level.

* Fixed bug with multithread code potentially causing loss of sync with the server communication or lock of the client (ticket [#55](https://github.com/psycopg/psycopg2/issues/55)).

* Don’t fail import if mx.DateTime module can’t be found, even if its support was built (ticket [#53](https://github.com/psycopg/psycopg2/issues/53)).

* Fixed escape for negative numbers prefixed by minus operator (ticket [#57](https://github.com/psycopg/psycopg2/issues/57)).

* Fixed refcount issue during copy. Reported and fixed by Dave Malcolm (ticket [#58](https://github.com/psycopg/psycopg2/issues/58), Red Hat Bug 711095).

* Trying to execute concurrent operations on the same connection through concurrent green thread results in an error instead of a deadlock.

* Fixed detection of pg_config on Window. Report and fix, plus some long needed setup.py cleanup by Steve Lacy: thanks!

### What’s new in psycopg 2.4.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4-1 "Link to this heading")

* Use own parser for bytea output, not requiring anymore the libpq 9.0 to parse the hex format.

* Don’t fail connection if the client encoding is a non-normalized variant. Issue reported by Peter Eisentraut.

* Correctly detect an empty query sent to the backend (ticket [#46](https://github.com/psycopg/psycopg2/issues/46)).

* Fixed a SystemError clobbering libpq errors raised without SQLSTATE. Bug vivisectioned by Eric Snow.

* Fixed interaction between NamedTuple and server-side cursors.

* Allow to specify –static-libpq on setup.py command line instead of just in ‘setup.cfg’. Patch provided by Matthew Ryan (ticket [#48](https://github.com/psycopg/psycopg2/issues/48)).

What’s new in psycopg 2.4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

New features and changes:

* Added support for Python 3.1 and 3.2. The conversion has also brought several improvements:

  * Added ‘b’ and ‘t’ mode to large objects: write can deal with both bytes strings and unicode; read can return either bytes strings or decoded unicode.

  * COPY sends Unicode data to files implementing ‘io.TextIOBase’.

  * Improved PostgreSQL-Python encodings mapping.

  * Added a few missing encodings: EUC_CN, EUC_JIS_2004, ISO885910, ISO885916, LATIN10, SHIFT_JIS_2004.

  * Dropped repeated dictionary lookups with unicode query/parameters.

* Improvements to the named cursors:

  * More efficient iteration on named cursors, fetching ‘itersize’ records at time from the backend.

  * The named cursors name can be an invalid identifier.

* Improvements in data handling:

  * Added ‘register_composite()’ function to cast PostgreSQL composite types into Python tuples/namedtuples.

  * Adapt types ‘bytearray’ (from Python 2.6), ‘memoryview’ (from Python 2.7) and other objects implementing the “Revised Buffer Protocol” to ‘bytea’ data type.

  * The ‘hstore’ adapter can work even when the data type is not installed in the ‘public’ namespace.

  * Raise a clean exception instead of returning bad data when receiving bytea in ‘hex’ format and the client libpq can’t parse them.

  * Empty lists correctly roundtrip Python -> PostgreSQL -> Python.

* Other changes:

  * ‘cursor.description’ is provided as named tuples if available.

  * The build script refuses to guess values if ‘pg_config’ is not found.

  * Connections and cursors are weakly referenceable.

Bug fixes:

* Fixed adaptation of None in composite types (ticket [#26](https://github.com/psycopg/psycopg2/issues/26)). Bug report by Karsten Hilbert.

* Fixed several reference leaks in less common code paths.

* Fixed segfault when a large object is closed and its connection no more available.

* Added missing icon to ZPsycopgDA package, not available in Zope 2.12.9 (ticket [#30](https://github.com/psycopg/psycopg2/issues/30)). Bug report and patch by Pumukel.

* Fixed conversion of negative infinity (ticket [#40](https://github.com/psycopg/psycopg2/issues/40)). Bug report and patch by Marti Raudsepp.

### What’s new in psycopg 2.3.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-3-2 "Link to this heading")

* Fixed segfault with middleware not passing DateStyle to the client (ticket [#24](https://github.com/psycopg/psycopg2/issues/254)). Bug report and patch by Marti Raudsepp.

### What’s new in psycopg 2.3.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-3-1 "Link to this heading")

* Fixed build problem on CentOS 5.5 x86_64 (ticket [#23](https://github.com/psycopg/psycopg2/issues/253)).

What’s new in psycopg 2.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-3 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

psycopg 2.3 aims to expose some new features introduced in PostgreSQL 9.0.

Main new features:

* [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") to `hstore` adapter and `hstore` to [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") typecaster, using both 9.0 and pre-9.0 syntax.

* Two-phase commit protocol support as per DBAPI specification.

* Support for payload in notifications received from the backend.

* `namedtuple`-returning cursor.

* Query execution cancel.

Other features and changes:

* Dropped support for protocol 2: Psycopg 2.3 can only connect to PostgreSQL servers with version at least 7.4.

* Don’t issue a query at every connection to detect the client encoding and to set the datestyle to ISO if it is already compatible with what expected.

* `mogrify()` now supports unicode queries.

* Subclasses of a type that can be adapted are adapted as the superclass.

* `errorcodes` knows a couple of new codes introduced in PostgreSQL 9.0.

* Dropped deprecated Psycopg “own quoting”.

* Never issue a ROLLBACK on close/GC. This behaviour was introduced as a bug in release 2.2, but trying to send a command while being destroyed has been considered not safe.

Bug fixes:

* Fixed use of `PQfreemem` instead of `free` in binary typecaster.

* Fixed access to freed memory in `conn_get_isolation_level()`.

* Fixed crash during Decimal adaptation with a few 2.5.x Python versions (ticket [#7](https://github.com/psycopg/psycopg2/issues/237)).

* Fixed notices order (ticket [#9](https://github.com/psycopg/psycopg2/issues/239)).

### What’s new in psycopg 2.2.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-2-2 "Link to this heading")

Bux fixes:

* the call to logging.basicConfig() in pool.py has been dropped: it was messing with some projects using logging (and a library should not initialize the logging system anyway.)

* psycopg now correctly handles time zones with seconds in the UTC offset. The old register_tstz_w_secs() function is deprecated and will raise a warning if called.

* Exceptions raised by the column iterator are propagated.

* Exceptions raised by executemany() iterators are propagated.

### What’s new in psycopg 2.2.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-2-1 "Link to this heading")

Bux fixes:

* psycopg now builds again on MS Windows.

What’s new in psycopg 2.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-2 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

This is the first release of the new 2.2 series, supporting not just one but two different ways of executing asynchronous queries, thanks to Jan and Daniele (with a little help from me and others, but they did 99% of the work so they deserve their names here in the news.)

psycopg now supports both classic select() loops and “green” coroutine libraries. It is all in the documentation, so just point your browser to doc/html/advanced.html.

Other new features:

* truncate() method for lobjects.

* COPY functions are now a little bit faster.

* All builtin PostgreSQL to Python typecasters are now available from the psycopg2.extensions module.

* Notifications from the backend are now available right after the execute() call (before client code needed to call isbusy() to ensure NOTIFY reception.)

* Better timezone support.

* Lots of documentation updates.

Bug fixes:

* Fixed some gc/refcounting problems.

* Fixed reference leak in NOTIFY reception.

* Fixed problem with PostgreSQL not casting string literals to the correct types in some situations: psycopg now add an explicit cast to dates, times and bytea representations.

* Fixed TimestampFromTicks() and TimeFromTicks() for seconds >= 59.5.

* Fixed spurious exception raised when calling C typecasters from Python ones.

### What’s new in psycopg 2.0.14[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-14 "Link to this heading")

New features:

* Support for adapting tuples to PostgreSQL arrays is now enabled by default and does not require importing psycopg2.extensions anymore.

* “can’t adapt” error message now includes full type information.

* Thank to Daniele Varrazzo (piro) psycopg2’s source package now includes full documentation in HTML and plain text format.

Bug fixes:

* No loss of precision when using floats anymore.

* decimal.Decimal “nan” and “infinity” correctly converted to PostgreSQL numeric NaN values (note that PostgreSQL numeric type does not support infinity but just NaNs.)

* psycopg2.extensions now includes Binary.

It seems we’re good citizens of the free software ecosystem and that big big big companies and people ranting on the pgsql-hackers mailing list we’ll now not dislike us. _g_ (See LICENSE file for the details.)

### What’s new in psycopg 2.0.13[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-13 "Link to this heading")

New features:

* Support for UUID arrays.

* It is now possible to build psycopg linking to a static libpq library.

Bug fixes:

* Fixed a deadlock related to using the same connection with multiple cursors from different threads.

* Builds again with MSVC.

### What’s new in psycopg 2.0.12[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-12 "Link to this heading")

New features:

* The connection object now has a reset() method that can be used to reset the connection to its default state.

Bug fixes:

* copy_to() and copy_from() now accept a much larger number of columns.

* Fixed PostgreSQL version detection.

* Fixed ZPsycopgDA version check.

* Fixed regression in ZPsycopgDA that made it behave wrongly when receiving serialization errors: now the query is re-issued as it should be by propagating the correct exception to Zope.

* Writing “large” large objects should now work.

### What’s new in psycopg 2.0.11[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-11 "Link to this heading")

New features:

* DictRow and RealDictRow now use less memory. If you inherit on them remember to set **slots** for your new attributes or be prepare to go back to old memory usage.

Bug fixes:

* Fixed exception in setup.py.

* More robust detection of PostgreSQL development versions.

* Fixed exception in RealDictCursor, introduced in 2.0.10.

### What’s new in psycopg 2.0.10[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-10 "Link to this heading")

New features:

* A specialized type-caster that can parse time zones with seconds is now available. Note that after enabling it (see extras.py) “wrong” time zones will be parsed without raising an exception but the result will be rounded.

* DictCursor can be used as a named cursor.

* DictRow now implements more dict methods.

* The connection object now expose PostgreSQL server version as the .server_version attribute and the protocol version used as .protocol_version.

* The connection object has a .get_parameter_status() methods that can be used to obtain useful information from the server.

Bug fixes:

* None is now correctly always adapted to NULL.

* Two double memory free errors provoked by multithreading and garbage collection are now fixed.

* Fixed usage of internal Python code in the notice processor; this should fix segfaults when receiving a lot of notices in multithreaded programs.

* Should build again on MSVC and Solaris.

* Should build with development versions of PostgreSQL (ones with -devel version string.)

* Fixed some tests that failed even when psycopg was right.

### What’s new in psycopg 2.0.9[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-9 "Link to this heading")

New features:

* “import psycopg2.extras” to get some support for handling times and timestamps with seconds in the time zone offset.

* DictCursors can now be used as named cursors.

Bug fixes:

* register_type() now accept an explicit None as its second parameter.

* psycopg2 should build again on MSVC and Solaris.

### What’s new in psycopg 2.0.9[¶](https://www.psycopg.org/docs/news.html#id1 "Link to this heading")

New features:

* COPY TO/COPY FROM queries now can be of any size and psycopg will correctly quote separators.

* float values Inf and NaN are now correctly handled and can round-trip to the database.

* executemany() now return the numer of total INSERTed or UPDATEd rows. Note that, as it has always been, executemany() should not be used to execute multiple SELECT statements and while it will execute the statements without any problem, it will return the wrong value.

* copy_from() and copy_to() can now use quoted separators.

* “import psycopg2.extras” to get UUID support.

Bug fixes:

* register_type() now works on connection and cursor subclasses.

* fixed a memory leak when using lobjects.

### What’s new in psycopg 2.0.8[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-8 "Link to this heading")

New features:

* The connection object now has a get_backend_pid() method that returns the current PostgreSQL connection backend process PID.

* The PostgreSQL large object API has been exposed through the Cursor.lobject() method.

Bug fixes:

* Some fixes to ZPsycopgDA have been merged from the Debian package.

* A memory leak was fixed in Cursor.executemany().

* A double free was fixed in pq_complete_error(), that caused crashes under some error conditions.

### What’s new in psycopg 2.0.7[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-7 "Link to this heading")

Improved error handling:

* All instances of psycopg2.Error subclasses now have pgerror, pgcode and cursor attributes. They will be set to None if no value is available.

* Exception classes are now chosen based on the SQLSTATE value from the result. (#184)

* The commit() and rollback() methods now set the pgerror and pgcode attributes on exceptions. (#152)

* errors from commit() and rollback() are no longer considered fatal. (#194)

* If a disconnect is detected during execute(), an exception will be raised at that point rather than resulting in “ProgrammingError: no results to fetch” later on. (#186)

Better PostgreSQL compatibility:

* If the server uses standard_conforming_strings, perform appropriate quoting.

* BC dates are now handled if psycopg is compiled with mxDateTime support. If using datetime, an appropriate ValueError is raised. (#203)

Other bug fixes:

* If multiple sub-interpreters are in use, do not share the Decimal type between them. (#192)

* Buffer objects obtained from psycopg are now accepted by psycopg too, without segfaulting. (#209)

* A few small changes were made to improve DB-API compatibility. All the dbapi20 tests now pass.

Miscellaneous:

* The PSYCOPG_DISPLAY_SIZE option is now off by default. This means that display size will always be set to “None” in cursor.description. Calculating the display size was expensive, and infrequently used so this should improve performance.

* New QueryCanceledError and TransactionRollbackError exceptions have been added to the psycopg2.extensions module. They can be used to detect statement timeouts and deadlocks respectively.

* Cursor objects now have a “closed” attribute. (#164)

* If psycopg has been built with debug support, it is now necessary to set the PSYCOPG_DEBUG environment variable to turn on debug spew.

### What’s new in psycopg 2.0.6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-6 "Link to this heading")

Better support for PostgreSQL, Python and win32:

* full support for PostgreSQL 8.2, including NULLs in arrays

* support for almost all existing PostgreSQL encodings

* full list of PostgreSQL error codes available by importing the psycopg2.errorcodes module

* full support for Python 2.5 and 64 bit architectures

* better build support on win32 platform

Support for per-connection type-casters (used by ZPsycopgDA too, this fixes a long standing bug that made different connections use a random set of date/time type-casters instead of the configured one.)

Better management of times and dates both from Python and in Zope.

copy_to and copy_from now take an extra “columns” parameter.

Python tuples are now adapted to SQL sequences that can be used with the “IN” operator by default if the psycopg2.extensions module is imported (i.e., the SQL_IN adapter was moved from extras to extensions.)

Fixed some small buglets and build glitches:

* removed double mutex destroy

* removed all non-constant initializers

* fixed PyObject_HEAD declarations to avoid memory corruption on 64 bit architectures

* fixed several Python API calls to work on 64 bit architectures

* applied compatibility macros from PEP 353

* now using more than one argument format raise an error instead of a segfault

### What’s new in psycopg 2.0.5.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-5-1 "Link to this heading")

* Now it really, really builds on MSVC and older gcc versions.

### What’s new in psycopg 2.0.5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-5 "Link to this heading")

* Fixed various buglets such as:

  * segfault when passing an empty string to Binary()

  * segfault on null queries

  * segfault and bad keyword naming in .executemany()

  * OperationalError in connection objects was always None

* Various changes to ZPsycopgDA to make it more zope2.9-ish.

* connect() now accept both integers and strings as port parameter

### What’s new in psycopg 2.0.4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-4 "Link to this heading")

* Fixed float conversion bug introduced in 2.0.3.

### What’s new in psycopg 2.0.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-3 "Link to this heading")

* Fixed various buglets and a memory leak (see ChangeLog for details)

### What’s new in psycopg 2.0.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-2 "Link to this heading")

* Fixed a bug in array typecasting that sometimes made psycopg forget about the last element in the array.

* Fixed some minor buglets in string memory allocations.

* Builds again with compilers different from gcc (#warning about PostgreSQL version is issued only if **GCC** is defined.)

### What’s new in psycopg 2.0.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-1 "Link to this heading")

* ZPsycopgDA now actually loads.

What’s new in psycopg 2.0[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

* Fixed handle leak on win32.

* If available the new “safe” encoding functions of libpq are used.

* django and tinyerp people, please switch to psycopg 2 _without_ using a psycopg 1 compatibility layer (this release was anticipated so that you all stop grumbling about psycopg 2 is still in beta.. :)

### What’s new in psycopg 2.0 beta 7[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-beta-7 "Link to this heading")

* Ironed out last problems with times and date (should be quite solid now.)

* Fixed problems with some arrays.

* Slightly better ZPsycopgDA (no more double connection objects in the menu and other minor fixes.)

* ProgrammingError exceptions now have three extra attributes: .cursor (it is possible to access the query that caused the exception using error.cursor.query), .pgerror and .pgcode (PostgreSQL original error text and code.)

* The build system uses pg_config when available.

* Documentation in the doc/ directory! (With many kudos to piro.)

### What’s new in psycopg 2.0 beta 6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-beta-6 "Link to this heading")

* Support for named cursors.

* Safer parsing of time intervals.

* Better parsing of times and dates, no more locale problems.

* Should now play well with py2exe and similar tools.

* The “decimal” module is now used if available under Python 2.3.

### What’s new in psycopg 2.0 beta 5[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-beta-5 "Link to this heading")

* Fixed all known bugs.

* The initial isolation level is now read from the server and .set_isolation_level() now takes values defined in psycopg2.extensions.

* .callproc() implemented as a SELECT of the given procedure.

* Better docstrings for a few functions/methods.

* Some time-related functions like psycopg2.TimeFromTicks() now take the local timezone into account. Also a tzinfo object (as per datetime module specifications) can be passed to the psycopg2.Time and psycopg2.Datetime constructors.

* All classes have been renamed to exist in the psycopg2._psycopg module, to fix problems with automatic documentation generators like epydoc.

* NOTIFY is correctly trapped.

### What’s new in psycopg 2.0 beta 4[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-beta-4 "Link to this heading")

* psycopg module is now named psycopg2.

* No more segfaults when a UNICODE query can’t be converted to the backend encoding.

* No more segfaults on empty queries.

* psycopg2.connect() now takes an integer for the port keyword parameter.

* “python setup.py bdist_rpm” now works.

* Fixed lots of small bugs, see ChangeLog for details.

### What’s new in psycopg 2.0 beta 3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-beta-3 "Link to this heading")

* ZPsycopgDA now works (except table browsing.)

* psycopg build again on Python 2.2.

### What’s new in psycopg 2.0 beta 2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-beta-2 "Link to this heading")

* Fixed ZPsycopgDA version check (ZPsycopgDA can now be imported in Zope.)

* psycopg.extras.DictRow works even after a new query on the generating cursor.

* Better setup.py for win32 (should build with MSCV or mingw.)

* Generic fixed and memory leaks plugs.

### What’s new in psycopg 2.0 beta 1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0-beta-1 "Link to this heading")

* Officially in beta (i.e., no new features will be added.)

* Array support: list objects can be passed as bound variables and are correctly returned for array columns.

* Added the psycopg.psycopg1 compatibility module (if you want instant psycopg 1 compatibility just “from psycopg import psycopg1 as psycopg”.)

* Complete support for BYTEA columns and buffer objects.

* Added error codes to error messages.

* The AsIs adapter is now exported by default (also Decimal objects are adapted using the AsIs adapter (when str() is called on them they already format themselves using the right precision and scale.)

* The connect() function now takes “connection_factory” instead of “factory” as keyword argument.

* New setup.py code to build on win32 using mingw and better error messages on missing datetime headers,

* Internal changes that allow much better user-defined type casters.

* A lot of bugfixes (binary, datetime, 64 bit arches, GIL, .executemany())

### What’s new in psycopg 1.99.13[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-13 "Link to this heading")

* Added missing .executemany() method.

* Optimized type cast from PostgreSQL to Python (psycopg should be even faster than before.)

### What’s new in psycopg 1.99.12[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-12 "Link to this heading")

* .rowcount should be ok and in sync with psycopg 1.

* Implemented the new COPY FROM/COPY TO code when connection to the backend using libpq protocol 3 (this also removes all asprintf calls: build on win32 works again.) A protocol 3-enabled psycopg _can_ connect to an old protocol 2 database and will detect it and use the right code.

* getquoted() called for real by the mogrification code.

### What’s new in psycopg 1.99.11[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-11 "Link to this heading")

* ‘cursor’ argument in .cursor() connection method renamed to ‘cursor_factory’.

* changed ‘tuple_factory’ cursor attribute name to ‘row_factory’.

* the .cursor attribute is gone and connections and cursors are properly gc-managed.

* fixes to the async core.

### What’s new in psycopg 1.99.10[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-10 "Link to this heading")

* The adapt() function now fully supports the adaptation protocol described in PEP 246. Note that the adapters registry now is indexed by (type, protocol) and not by type alone. Change your adapters accordingly.

* More configuration options moved from setup.py to setup.cfg.

* Fixed two memory leaks: one in cursor deallocation and one in row fetching (.fetchXXX() methods.)

### What’s new in psycopg 1.99.9[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-9 "Link to this heading")

* Added simple pooling code (psycopg.pool module).

* Added DECIMAL typecaster to convert postgresql DECIMAL and NUMERIC types (i.e, all types with an OID of NUMERICOID.) Note that the DECIMAL typecaster does not set scale and precision on the created objects but uses Python defaults.

* ZPsycopgDA back in and working using the new pooling code.

* Isn’t that enough? :)

### What’s new in psycopg 1.99.8[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-8 "Link to this heading")

* added support for UNICODE queries.

* added UNICODE typecaster; to activate it just do:

psycopg.extensions.register_type(psycopg.extensions.UNICODE)
Note that the UNICODE typecaster override the STRING one, so it is not activated by default.

* cursors now really support the iterator protocol.

* solved the rounding errors in time conversions.

* now cursors support .fileno() and .isready() methods, to be used in select() calls.

* .copy_from() and .copy_in() methods are back in (still using the old protocol, will be updated to use new one in next release.)

* fixed memory corruption bug reported on win32 platform.

### What’s new in psycopg 1.99.7[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-7 "Link to this heading")

* added support for tuple factories in cursor objects (removed factory argument in favor of a .tuple_factory attribute on the cursor object); see the new module psycopg.extras for a cursor (DictCursor) that return rows as objects that support indexing both by position and column name.

* added support for tzinfo objects in datetime.timestamp objects: the PostgreSQL type “timestamp with time zone” is converted to datetime.timestamp with a FixedOffsetTimezone initialized as necessary.

### What’s new in psycopg 1.99.6[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-6 "Link to this heading")

* sslmode parameter from 1.1.x

* various datetime conversion improvements.

* now psycopg should compile without mx or without native datetime (not both, obviously.)

* included various win32/MSVC fixes (pthread.h changes, winsock2 library, include path in setup.py, etc.)

* ported interval fixes from 1.1.14/1.1.15.

* the last query executed by a cursor is now available in the .query attribute.

* conversion of unicode strings to backend encoding now uses a table (that still need to be filled.)

* cursors now have a .mogrify() method that return the query string instead of executing it.

* connection objects now have a .dsn read-only attribute that holds the connection string.

* moved psycopg C module to _psycopg and made psycopg a python module: this allows for a neat separation of DBAPI-2.0 functionality and psycopg extensions; the psycopg namespace will be also used to provide python-only extensions (like the pooling code, some ZPsycopgDA support functions and the like.)

### What’s new in psycopg 1.99.3[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-3 "Link to this heading")

* added support for python 2.3 datetime types (both ways) and made datetime the default set of typecasters when available.

* added example: dt.py.

### What’s new in psycopg 1.99.3[¶](https://www.psycopg.org/docs/news.html#id2 "Link to this heading")

* initial working support for unicode bound variables: UTF-8 and latin-1 backend encodings are natively supported (and the encoding.py example even works!)

* added .set_client_encoding() method on the connection object.

* added examples: encoding.py, binary.py, lastrowid.py.

### What’s new in psycopg 1.99.2[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-2 "Link to this heading")

* better typecasting:

  * DateTimeDelta used for postgresql TIME (merge from 1.1)

  * BYTEA now is converted to a real buffer object, not to a string

* buffer objects are now adapted into Binary objects automatically.

* ported scroll method from 1.1 (DBAPI-2.0 extension for cursors)

* initial support for some DBAPI-2.0 extensions:

  * .rownumber attribute for cursors

  * .connection attribute for cursors

  * .next() and .**iter**() methods to have cursors support the iterator protocol

  * all exception objects are exported to the connection object

### What’s new in psycopg 1.99.1[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-1 "Link to this heading")

* implemented microprotocols to adapt arbitrary types to the interface used by psycopg to bind variables in execute;

* moved qstring, pboolean and mxdatetime to the new adapter layout (binary is still missing; python 2.3 datetime needs to be written).

### What’s new in psycopg 1.99.0[¶](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-1-99-0 "Link to this heading")

* reorganized the whole source tree;

* async core is in place;

* splitted QuotedString objects from mx stuff;

* dropped autotools and moved to pythonic setup.py (needs work.)
