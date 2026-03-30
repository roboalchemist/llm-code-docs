# Source: https://sourceware.org/pipermail/cygwin-announce/2026-March/012878.html

Title: cygwin 3.6.7-1

URL Source: https://sourceware.org/pipermail/cygwin-announce/2026-March/012878.html

Markdown Content:
**corinna-cygwin@cygwin.com**[corinna-cygwin@cygwin.com](mailto:corinna-cygwin%40cygwin.com?Subject=Re:%20Re%3A%20cygwin%203.6.7-1&In-Reply-To=%3C20260302223121.1737232-1-corinna-cygwin%40cygwin.com%3E "cygwin 3.6.7-1")

_Mon Mar 2 21:31:21 GMT 2026_
*   Previous message (by thread): [cygport 0.37.7-1](https://sourceware.org/pipermail/cygwin-announce/2026-March/012877.html)
*   Next message (by thread): [gawk 5.4.0-1](https://sourceware.org/pipermail/cygwin-announce/2026-March/012879.html)
*   **Messages sorted by:**[[ date ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/date.html#12878)[[ thread ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/thread.html#12878)[[ subject ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/subject.html#12878)[[ author ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/author.html#12878)

* * *

The following packages have been uploaded to the Cygwin distribution:

* cygwin-3.6.7-1
* cygwin-devel-3.6.7-1
* cygwin-doc-3.6.7-1

Fixes:
------

- Guard c32rtomb() against invalid input characters.
  Addresses a testsuite error in current gawk git master.

- Allow changing primary group even when running with cygserver account
  caching.
  Addresses: [https://cygwin.com/pipermail/cygwin/2026-January/259250.html](https://cygwin.com/pipermail/cygwin/2026-January/259250.html)

- Correctly handle i->Ä°, I->Ä± conversion in turk and azerbaijani languages
  (LC_CTYPE=tr_TR, tr_CY, az_AZ).

- Fix uid/gid mapping from unix id to Cygwin id in certain scenarios when
  accessing Samba or NFS shares on unixoid OS.

- gencat: Fix a bug in octal value handling in catalog input files.
  Addresses a flaw in tcsh's cataloge file generation.

- Bump default_POSIX_C_SOURCE to 202405.

* * *

*   Previous message (by thread): [cygport 0.37.7-1](https://sourceware.org/pipermail/cygwin-announce/2026-March/012877.html)
*   Next message (by thread): [gawk 5.4.0-1](https://sourceware.org/pipermail/cygwin-announce/2026-March/012879.html)
*   **Messages sorted by:**[[ date ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/date.html#12878)[[ thread ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/thread.html#12878)[[ subject ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/subject.html#12878)[[ author ]](https://sourceware.org/pipermail/cygwin-announce/2026-March/author.html#12878)

* * *

[More information about the Cygwin-announce mailing list](https://cygwin.com/mailman/listinfo/cygwin-announce)
