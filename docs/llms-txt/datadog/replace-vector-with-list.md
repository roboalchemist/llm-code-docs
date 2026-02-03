# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/replace-vector-with-list.md

---
title: Replace Vector with List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Replace Vector with List
---

# Replace Vector with List

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/replace-vector-with-list`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Replace your `Vector` class usage with the newer `java.util.ArrayList`, unless you need expensive thread-safe operations.

`Vector` uses unnecessary synchronization, which can slow down single-threaded applications whereas `ArrayList` can perform better in such cases. In addition, it offers modern features which make the transition easy while retaining flexibility for thread safety when needed.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    void bar() {
        Vector vector1 = new Vector(); // consider using java.util.List instead
        Vector<Integer> vector2 = new Vector<>();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
package com.dd.logs.rum.sessionreducer;

import static io.vavr.API.Vector;

import com.dd.logs.launcher.Features;
import com.dd.logs.launcher.ModuleLauncher;
import com.dd.logs.rule_engine.reducer.main.ReducerWorkloadBundle;
import com.dd.logs.usage.UsageComponent;
import com.dd.logs.usage.UsageTrackerClientBundle;
import com.dd.logs.workload.assigner.AssignerClientBundle;
import io.vavr.collection.Vector;
import java.util.List;

public class Main {

  public static void main(String[] args) {
    new ModuleLauncher(
            List.of(
                new AssignerClientBundle(),
                new UsageTrackerClientBundle(UsageComponent.SESSIONIZATION),
                new ReducerWorkloadBundle(new RumReducerWorkloadBundleParams())),
            // disconnected from mongo
            Features.builder().withKafka().build())
        .launchOrExit();

    Vector<String> x = returnSomeVavrVector();
    x.stdout();
  }

  private static Vector<String> returnSomeVavrVector() {
    return Vector();
  }
}
```

```java
public class Foo {
    void bar() {
        List list = new ArrayList();
        List<Integer> list2 = new ArrayList<>();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 