# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/xxe-injection.md

---
title: Potential XXE attack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Potential XXE attack
---

# Potential XXE attack

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/xxe-injection`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

This rule detects potential XML External Entity (XXE) vulnerabilities in Python code. XXE attacks occur when an application parses XML input containing external entity references, which can lead to data exposure, denial of service, or other security issues. The vulnerability arises when untrusted XML content is processed without proper configuration to disable external entity resolution.

To avoid this vulnerability, always use safe XML parsing practices. For example, avoid parsing XML from untrusted sources directly with default settings, such as `ElementTree.parse(content)`. Instead, parse XML from trusted file paths or configure the parser to disable external entity resolution. Using libraries or methods that do not process external entities by default is also recommended.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import xml
import xml.etree import ElementTree

tree = ElementTree.parse(f"${something}")
```

```python
import xml

tree = xml.etree.ElementTree.parse(content)
```

```python
import xml
import xml.etree import ElementTree

tree = ElementTree.parse(content)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
# safe parser
parser = defusedxml.ElementTree.DefusedXMLParser(
    forbid_dtd=True, forbid_entities=True, forbid_external=True
)
tree = defusedxml.ElementTree.parse(test_svg, parser=parser)
root = tree.getroot()
assert root is not None
```

```python
import xml
import xml.etree import ElementTree

tree = ElementTree.parse('myfile.xml')
tree = ElementTree.parse("myfile.xml")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 