# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/hardcoded-tmp-file.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/hardcoded-tmp-file.md

---
title: Do not hardcode temporary file or directory names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not hardcode temporary file or directory names
---

# Do not hardcode temporary file or directory names

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/hardcoded-tmp-file`

**Language:** Python

**Severity:** Info

**Category:** Best Practices

**CWE**: [377](https://cwe.mitre.org/data/definitions/377.html)

## Description{% #description %}

Do not hardcode the names of temporary files or directories. This may constitute a security vulnerability because an attacker might use that name to create a link to a file they want to overwrite or read.

Instead of hardcoding values, use the `tempfile` Python module to create unpredictable names.

#### Learn More{% #learn-more %}

- [CWE-377 - Insecure Temporary File](https://cwe.mitre.org/data/definitions/377.html)
- [Create, use and remove. temporary files securely](https://security.openstack.org/guidelines/dg_using-temporary-files-securely.html)
- [`tempfile` module](https://docs.python.org/3/library/tempfile.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
with open("/tmp/acme.pub", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

def foobar():
    api_key_file = Path('/tmp/supersecret.txt')

keyfile = '/tmp/vulpy.apikey.{}.{}'.format(username, key)
keyfile = f"/tmp/vulpy.apikey.{username}.{key}"
def authenticate(request):
    if 'X-APIKEY' not in request.headers:
        return None

    key = request.headers['X-APIKEY']

    for f in Path('/tmp/').glob('vulpy.apikey.*.' + key):
        return f.name.split('.')[2]

    return None
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
secure_temp = tempfile.mkstemp(prefix="pre_",suffix="_suf")
print(secure_temp)

temp = tempfile.NamedTemporaryFile()
print(temp)
print(temp.name)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
