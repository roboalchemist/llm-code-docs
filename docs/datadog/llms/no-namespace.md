# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-namespace.md

---
title: Avoid TypeScript namespaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid TypeScript namespaces
---

# Avoid TypeScript namespaces

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-namespace`

**Language:** TypeScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Namespaces should be avoided as an outdated feature of TypeScript. Use module syntax instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
module foo {}
namespace foo {}
module foo {}
namespace foo {}
module foo {}
namespace foo {}
declare module foo {}
declare namespace foo {}
declare module foo {}
declare namespace foo {}
namespace foo {}
module foo {}
declare module foo {}
declare namespace foo {}
namespace Foo.Bar {}
namespace Foo.Bar { namespace Baz.Bas { interface X {} } }
namespace A { namespace B { declare namespace C {} }
namespace A { namespace B { export declare namespace C {} } }
namespace A { declare namespace B { namespace C {} } }
namespace A { export declare namespace B { namespace C {} } }
namespace A { export declare namespace B { declare namespace C {} } }
namespace A { export declare namespace B { export declare namespace C {} } }
namespace A { declare namespace B { export declare namespace C {} } }
namespace A { export namespace B { export declare namespace C {} } }
export namespace A { namespace B { declare namespace C {} } }
export namespace A { namespace B { export declare namespace C {} } }
export namespace A { declare namespace B { namespace C {} } }
export namespace A { export declare namespace B { namespace C {} } }
export namespace A { export declare namespace B { declare namespace C {} } }
export namespace A { export declare namespace B { export declare namespace C {} } }
export namespace A { declare namespace B { export declare namespace C {} } }
export namespace A { export namespace B { export declare namespace C {} } }
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
declare global {}
declare module 'foo' {}
declare module foo {}
declare namespace foo {}
declare global { namespace foo {} }
declare module foo { namespace bar {} }
declare global { namespace foo { namespace bar {} } }
declare namespace foo { namespace bar { namespace baz {} } }
export declare namespace foo { export namespace bar { namespace baz {} } }
namespace foo {}
module foo {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
