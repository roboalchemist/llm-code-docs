# Reporting

It is possible to generate any combination of the reports for a single test run.

The available reports are terminal (with or without missing line numbers shown), HTML, XML, JSON, Markdown (either in ‘write’ or ‘append’
mode to file), LCOV and annotated source code.

The default is terminal report without line numbers:

```
pytest --cov=myproj tests/

-------------------- coverage: platform linux2, python 2.6.4-final-0 ---------------------
Name                 Stmts   Miss  Cover
----------------------------------------
myproj/__init__          2      0   100%
myproj/myproj          257     13    94%
myproj/feature4286      94      7    92%
----------------------------------------
TOTAL                  353     20    94%

```
