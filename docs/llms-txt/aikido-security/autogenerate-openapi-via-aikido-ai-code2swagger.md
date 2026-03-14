# Source: https://help.aikido.dev/dast-surface-monitoring/api-scanning/autogenerate-openapi-via-aikido-ai-code2swagger.md

# Autogenerate OpenAPI via Aikido AI (Code2Swagger)

Aikido can automatically generate an OpenAPI specification directly from your codebase, eliminating the need for manual documentation while ensuring accurate API scanning.&#x20;

It uses LLM to parse your source code to find routes, parameters and body information without the need to build your own API specification.

Aikido will regularly rescan your code to keep the OpenAPI specification up to date.

{% hint style="success" %}
Aikido recommends using [Zen Firewall](https://help.aikido.dev/zen-firewall) whenever possible as it will give more accurate results because it's based on the the actual traffic to your API.&#x20;
{% endhint %}

### How to use

Follow the [Setting up REST API Scanning](https://help.aikido.dev/dast-surface-monitoring/rest-api-scanning#setting-up-rest-api-scanning) guide and choose the **Aikido AI** option.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FdZZAi56RuVtO0eohevbi%2FScreenshot%202025-07-14%20at%2010.28.09.png?alt=media&#x26;token=d185c060-f88e-48c2-a150-34e464a2366d" alt=""><figcaption></figcaption></figure>

### Supported Programming Languages

{% hint style="warning" %}
This feature supports back-end code analysis only; front-end code is not supported.
{% endhint %}

* C
* C++
* C# / Dotnet
* Dart
* Elixir
* Go
* Java
* Javascript
* Kotlin
* PHP
* Python
* Ruby
* Rust
* Swift
* Scala
* Typescript / TSX
* VB.NET (only route discovery)

<br>
