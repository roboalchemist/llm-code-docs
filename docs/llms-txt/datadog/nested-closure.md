# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/nested-closure.md

---
title: Closure expressions should not be nested too deeply
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Closure expressions should not be nested too deeply
---

# Closure expressions should not be nested too deeply

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/nested-closure`

**Language:** Swift

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Closure expressions should not be nested too deeply, as excessive nesting makes code harder to read, understand, and maintain. Closures are intended to provide clear, concise logic, but when stacked inside one another, they quickly become confusing and error-prone. Extracting nested logic into separate functions keeps the codebase cleaner and easier to follow.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
import SwiftUI

struct AlbumDetail: View {
    var album: Album

    var body: some View {
        List(album.songs) { song in
            HStack {
                Image(album.cover)
                VStack(alignment: .leading) {
                    Text(song.title)
                    Text(song.artist.name)
                        .foregroundStyle(.secondary)

          VStack(alignment: .leading) {
            Text(song.title)
            Text(song.artist.name)
              .foregroundStyle(.secondary)
            VStack(alignment: .leading) {
              Text(song.title)
              Text(song.artist.name)
                .foregroundStyle(.secondary)
            }
          }
                }
            }
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import SwiftUI

struct AlbumDetail: View {
    var album: Album

    var body: some View {
        List(album.songs) { song in
            HStack {
                Image(album.cover)
                VStack(alignment: .leading) {
                    Text(song.title)
                    Text(song.artist.name)
                        .foregroundStyle(.secondary)
                }
            }
        }
    }
}
```

```swift
func multPlus(x:Int) {
  foobar(x) {
    print(x * 42)
  }
  print(x + 42)
}

foo(42) { (x: Int) in
    bar(x, multPlus)
    print(x - 42)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
