# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/init-method-required.md

---
title: ensure classes have an __init__ method
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > ensure classes have an __init__ method
---

# ensure classes have an __init__ method

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/init-method-required`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Ensure that a class has an `__init__` method. This check is bypassed for dataclass-like decorators (`@dataclass`, `@frozen`, `@bindable_dataclass`).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Foo:  # need to define __init__
    def foo(bar):
        pass
    def bar(baz):
        pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
@define
class Foo:
    def foo(bar):
        pass
    def bar(baz):
        pass
```

```python
import pandas as pd


@binding.bindable_dataclass
class MyClass:
    cost_source_type: str = "Metric"
    cost_metric_name: str = "test.evp.costs"
    cost_filter: str = ""
    datacenters: list[str] = field(default_factory=lambda: ["us1.prod.dog"])

    def fetch_something(self) -> pd.DataFrame:
        pass
```

```python
# dataclass do not require an init class
@dataclass
class Requests:
    cpu: float  # expressed in cpu cores
    memory: int  # expressed in bytes

    @staticmethod
    def from_pod(pod: V1Pod):
        cpu = 0.0
        memory = 0

        for container in pod.spec.containers:
            cpu += parse_cpu_string(container.resources.requests["cpu"])
            memory += parse_memory_string(container.resources.requests["memory"])

        return Requests(cpu, memory)

    def add(self, other):
        self.cpu += other.cpu
        self.memory += other.memory

@dataclasses.dataclass
class DependencyKey:
    name: str
    version: str

    def __hash__(self):
        if self.version is None:
            version = ""
        else:
            version = self.version
        return hash(self.name + version)

@frozen
class AnotherClass:
    cpu: float
    memory: int
    def add(self, other):
        self.cpu += other.cpu
        self.memory += other.memory

@dataclasses.dataclass(frozen=True)
class Settings:
    keys: list[[str, str]]

    def get_keys(self):
        return self.keys
```

```python
class Child(Parent):
  def fn():
      pass

class AnotherChild(modname.Parent):
  def another_fn():
    pass
```

```python
class UserLoginTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_correct_credentials(self):
        user = authenticate(username=self.username, password=self.password)
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_incorrect_credentials(self):
        user = authenticate(username=self.username, password='wrongpassword')
        self.assertIsNone(user)
```

```python
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
    ]
```

```python
@dataclass
class Foo:  # no __init__ required for dataclass
    value = 51
```

```python
class Foo:
    def __init__(self):
        pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
