# Tox

When using tox [https://tox.wiki/en/stable/] you can have ultra-compact configuration - you can have all of it in
`tox.ini`:

```
[tox]
envlist = ...

[tool:pytest]
...

[coverage:paths]
...

[coverage:run]
...

[coverage:report]
..

[testenv]
commands = ...

```
