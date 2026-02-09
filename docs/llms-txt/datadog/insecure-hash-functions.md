# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/insecure-hash-functions.md

---
title: Do not use insecure functions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use insecure functions
---

# Do not use insecure functions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/insecure-hash-functions`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

Do not use a broken or risky cryptographic algorithm. This exposes you to unwanted attacks.

It checks the following modules

- [hashlib](https://docs.python.org/3/library/hashlib.html)
- [cryptography](https://cryptography.io/)

#### Learn More{% #learn-more %}

- [CWE-327](https://cwe.mitre.org/data/definitions/327.html) - Use of a Broken or Risky Cryptographic Algorithm
- [CWE-328](https://cwe.mitre.org/data/definitions/328.html) - Use of Weak Hash

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from hashlib import md5
from typing import NamedTuple, Optional

from aiopg import Connection


class User(NamedTuple):
    id: int
    first_name: str
    middle_name: Optional[str]
    last_name: str
    username: str
    pwd_hash: str
    is_admin: bool

    @classmethod
    def from_raw(cls, raw: tuple):
        return cls(*raw) if raw else None

    @staticmethod
    async def get(conn: Connection, id_: int):
        async with conn.cursor() as cur:
            await cur.execute(
                'SELECT id, first_name, middle_name, last_name, '
                'username, pwd_hash, is_admin FROM users WHERE id = %s',
                (id_,),
            )
            return User.from_raw(await cur.fetchone())

    @staticmethod
    async def get_by_username(conn: Connection, username: str):
        async with conn.cursor() as cur:
            await cur.execute(
                'SELECT id, first_name, middle_name, last_name, '
                'username, pwd_hash, is_admin FROM users WHERE username = %s',
                (username,),
            )
            return User.from_raw(await cur.fetchone())

    def check_password(self, password: str):
        return self.pwd_hash == md5(password.encode('utf-8')).hexdigest()
```

```python
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.MD5())
```

```python
import hashlib

hashlib.new('md5')
hashlib.new('md4')


hashlib.md5("bla")

md = hashlib.md5()
md.update("foo")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
md5 = hashlib.md5(usedforsecurity=False)
```

```python
import hashlib

hashlib.new('sha256')
hashlib.new('sha3_256')
```

```python
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256())
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 