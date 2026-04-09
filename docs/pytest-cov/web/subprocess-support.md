# Subprocess support

Subprocess support was removed in pytest-cov 7.0 due to various complexities resulting from coverage’s own subprocess support.
To migrate you should change your coverage config to have at least this:

```
[run]
patch = subprocess

```
