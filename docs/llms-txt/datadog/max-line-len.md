# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/max-line-len.md

---
title: Line cannot exceed default max length
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Line cannot exceed default max length
---

# Line cannot exceed default max length

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/max-line-len`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule ensures that no line in your Kotlin code exceeds a certain maximum length, set to 140 characters by default. Exceeding this limit can lead to code that is difficult to read and understand, especially when working with complex codebases or reviewing code changes. It can also cause issues with version control systems that have difficulty handling long lines.

The rule take the argument `max-line-length` to adapt its behavior with your coding style and guidelines.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val fooooooooooooooo = "fooooooooooooooooooooo"
val foo = "foo" + "ooooooooooooooooooooooooooo"
val foooooooooooooo = "foooooooooooooooooooo" // some comment
val bad = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
val foooooooooooooo = "foooooooooooooooooooo"                                                                                             // some comment
foo(bar,                       baz, bli, blo, foooooooooooooooooooo, foooooooooooooooooooo2, foooooooooooooooooooo3, foooooooooooooooooooo43)
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
package com.datadog.client.model.ucap

import com.datadog.intellij.toolkit.serialization.InstantISO8601Serializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import java.time.Instant

@Serializable
@JvmInline
value class ActionId(val value: String)

@Serializable
class Action(val id: ActionId, val attributes: ActionAttributes)

@Serializable
data class ActionAttributes(
    val name: String,
    val description: String?,
    val detail: String?,
    @Serializable(with = InstantISO8601Serializer::class) val timestamp: Instant,
    @SerialName("annotation_id") val annotationId: AnnotationId,
    @SerialName("action_key") val actionKey: String,
    val status: Status,
    val recomputable: Boolean,
    val recommendation: String?,
    val modification: Modification?,
) {
    enum class Status {
        GENERATING,
        READY,
        FAILED
    }

    @Serializable
    data class Modification(
        @SerialName("repository_url") val repositoryUrl: String,
        @SerialName("commit_sha") val commitSha: String,
        val patch: String
    )
}
```

```kotlin
val fooooooooooooooo = "fooooooooooooooooooooo"
val foo = "foo" + "ooooooooooooooooooooooooooo"
val foooooooooooooo = "foooooooooooooooooooo" // some comment
foo(bar)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
