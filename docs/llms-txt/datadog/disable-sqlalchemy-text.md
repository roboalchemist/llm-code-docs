# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/disable-sqlalchemy-text.md

---
title: Do not use text() as it leads to SQL injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use text() as it leads to SQL injection
---

# Do not use text() as it leads to SQL injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/disable-sqlalchemy-text`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

The `text` function from SQLAlchemy lets you build custom SQL statements. It is recommended to use the ORM functions to build queries and avoid building custom queries, which are vulnerable to SQL injections.

#### Learn More{% #learn-more %}

- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from sqlalchemy.sql import text


con = engine.connect()

data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
            { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
)

statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")

for line in data:
    con.execute(statement, **line)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
con = engine.connect()

data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
            { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
)

statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")

for line in data:
    con.execute(statement, **line)
```

```python
from sqlalchemy import text

BOOKS = meta.tables['books']
query = sqlalchemy.select(BOOKS).where(BOOKS.c.genre == 'fiction')
result = engine.execute(query).fetchall()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 