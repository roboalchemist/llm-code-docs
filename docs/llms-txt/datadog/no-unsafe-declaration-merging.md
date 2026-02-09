# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unsafe-declaration-merging.md

---
title: Avoid unsafe declaration merging
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unsafe declaration merging
---

# Avoid unsafe declaration merging

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-unsafe-declaration-merging`

**Language:** TypeScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

Do not merge class and interface declarations. The compiler won't check property initialization, which might lead to runtime errors.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
interface Foo {}
class Foo {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
interface Foo {}
class Bar implements Foo {}

namespace Baz {}
namespace Baz {}
enum Baz {}

namespace Qux {}
function Qux() {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 