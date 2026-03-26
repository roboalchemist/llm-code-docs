# Configuration

This plugin provides a clean minimal set of command line options that are added to pytest. For
further control of coverage use a coverage config file [https://coverage.readthedocs.io/en/latest/config.html].

CLI options:

–cov [SOURCE]        Path or package name to measure during execution (multi-allowed). Use –cov= to not do any source filtering and record everything.
–cov-reset           Reset cov sources accumulated in options so far.
–cov-report TYPE     Type of report to generate: term, term-missing, annotate, html, xml, json, markdown, markdown-append, lcov (multi-allowed). term, term-missing may be followed by “:skip-covered”.

annotate, html, xml, json, markdown, markdown-append and lcov may be followed by “:DEST” where DEST specifies the output location. Use –cov-report= to not generate any output.
