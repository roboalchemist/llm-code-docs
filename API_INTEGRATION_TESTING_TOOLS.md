# API Integration Testing Tools Catalog

## Overview

Comprehensive catalog of software tools and frameworks for API testing across multiple protocols, paradigms, and use cases. Includes REST, GraphQL, gRPC, contract testing, mocking, and performance testing solutions.

**Last Updated:** 2026-01-01
**Research Sources:** Tavily AI Search, Perplexity AI, current tool documentation

---

## Core API Testing Platforms (Multi-Protocol)

These platforms support multiple API types and testing approaches:

### 1. Postman
- **Protocols:** REST, GraphQL, gRPC (partial)
- **Key Features:** Collections, environments, contract testing, CI/CD integration, collaborative testing, mock servers
- **License:** Freemium (commercial enterprise)
- **Best For:** Teams needing unified REST/GraphQL/gRPC workflows

### 2. SoapUI
- **Protocols:** REST, SOAP, (limited GraphQL)
- **Key Features:** Functional testing, performance/load testing, security testing, mock services
- **License:** Open-source + commercial
- **Best For:** REST and SOAP API functional/performance testing

### 3. Katalon Studio
- **Protocols:** REST, GraphQL, (limited gRPC)
- **Key Features:** Low-code automation, data-driven tests, AI-powered features, UI/API integration
- **License:** Freemium (commercial)
- **Best For:** Teams wanting low-code API/UI test automation

### 4. Insomnia
- **Protocols:** REST, GraphQL, gRPC (partial)
- **Key Features:** Lightweight design/testing, request chaining, plugins, environment management
- **License:** Open-source (commercial sync features)
- **Best For:** Developers preferring lightweight client tools

### 5. Apidog
- **Protocols:** REST, GraphQL, gRPC (partial)
- **Key Features:** Smart auto-generation, dynamic value generation, IDE integration, collaborative workspace
- **License:** Commercial freemium
- **Best For:** Teams needing smart test generation and spec-driven testing

---

## REST API Testing Frameworks

### Open-Source Frameworks

#### 1. Karate
- **Language:** Java/Gherkin DSL
- **Key Features:** BDD-style API/UI testing, parallelism, contract testing, GraphQL support
- **GitHub:** KarateLabs/karate
- **Best For:** Developers wanting BDD-style API automation

#### 2. Citrus
- **Language:** Java
- **Key Features:** REST, SOAP, messaging (JMS, RabbitMQ), gRPC support, microservices testing
- **GitHub:** christophd/citrus
- **Best For:** Microservices and messaging integration testing

#### 3. REST Assured
- **Language:** Java
- **Key Features:** Fluent API for REST testing, JSON path validation, request chaining
- **GitHub:** rest-assured/rest-assured
- **Best For:** Java teams doing REST API unit/integration testing

#### 4. Tavern
- **Language:** Python
- **Key Features:** YAML-based REST/MQTT testing, pytest integration, contract verification
- **GitHub:** taverntesting/tavern
- **Best For:** Python teams wanting declarative REST testing

#### 5. HttpClient Testing (Language-Specific)
- **JavaScript/Node:** Supertest, Jest + fetch, axios, node-fetch
- **Python:** pytest + requests, httpx
- **Go:** httptest, testify
- **Ruby:** RSpec + WebMock, VCR
- **Rust:** reqwest, tokio

---

## GraphQL Testing Tools

### GraphQL-First Tools

#### 1. GraphQL Code Generator
- **Language:** TypeScript/JavaScript
- **Key Features:** Type-safe code generation from schema, operation types, testing utilities
- **GitHub:** dotansimha/graphql-code-generator
- **Best For:** Frontend teams using GraphQL with TypeScript

#### 2. GraphiQL
- **Platform:** Browser-based IDE
- **Key Features:** Query editor, autocomplete via introspection, schema exploration, error highlighting
- **GitHub:** graphql/graphiql
- **Best For:** Manual GraphQL query exploration and debugging

#### 3. GraphQL Playground
- **Platform:** Desktop/browser IDE
- **Key Features:** Enhanced GraphiQL, multi-tabs, HTTP headers, persistent history, schema docs
- **GitHub:** graphql-playground/graphql-playground
- **Best For:** Manual testing with enhanced collaboration features

#### 4. Apollo Studio
- **Platform:** Cloud-based registry
- **Key Features:** Schema registry, operation metrics, explorer, federation insights, testing
- **Company:** Apollo GraphQL
- **Best For:** Teams using Apollo ecosystem

#### 5. Apollo Client Testing Utilities
- **Language:** TypeScript/JavaScript
- **Key Features:** Schema-driven testing, @graphql-tools libraries for integration tests
- **Part Of:** @apollo/client (v3.10+)
- **Best For:** React apps with GraphQL data fetching

#### 6. Schemathesis
- **Language:** Python/CLI
- **Key Features:** Schema-based test generation from OpenAPI/GraphQL, property-based testing
- **GitHub:** schemathesis/schemathesis
- **Best For:** API schema compliance and edge case testing

#### 7. GraphQL Inspector
- **Language:** TypeScript/CLI
- **Key Features:** Schema validation, linting, schema comparison, breaking change detection
- **GitHub:** kamilkisiuk/graphql-inspector
- **Best For:** CI/CD schema validation and version control

#### 8. Supertest + Jest (GraphQL)
- **Language:** JavaScript/TypeScript
- **Key Features:** Programmatic backend testing, query execution, assertion testing
- **Commonly Paired:** Express, Apollo Server
- **Best For:** Node.js GraphQL backend testing

#### 9. MSW (Mock Service Worker)
- **Language:** JavaScript/TypeScript
- **Key Features:** Client-side mocking for GraphQL/REST, Jest/Vitest integration
- **GitHub:** mswjs/msw
- **Best For:** Frontend component testing with mocked GraphQL

---

## gRPC Testing Tools

### UI-Based Clients

#### 1. Kreya
- **Platform:** Desktop GUI
- **Key Features:** gRPC/REST/GraphQL support, .proto import, all streaming types, SSL/TLS, JWT, offline mode
- **License:** Commercial freemium
- **Best For:** gRPC developers needing rich GUI tooling

#### 2. BloomRPC
- **Platform:** Desktop GUI
- **Key Features:** gRPC-focused UI, .proto-based testing, method invocation
- **GitHub:** uw-labs/bloomrpc
- **Best For:** Quick gRPC method testing

#### 3. gRPC-UI
- **Platform:** Web browser
- **Key Features:** Browser-based .proto reflection, web-based gRPC testing
- **GitHub:** grpc-ecosystem/grpc-web
- **Best For:** Web-based gRPC exploration

#### 4. grpc-Web
- **Language:** JavaScript/TypeScript
- **Key Features:** gRPC bridge for browsers, web client generation
- **GitHub:** grpc/grpc-web
- **Best For:** Browser-based gRPC client communication

### Command-Line Tools

#### 1. grpcurl
- **Language:** Go CLI
- **Key Features:** Request invocation from .proto files, unary/streaming support, reflection
- **GitHub:** fullstorydev/grpcurl
- **Best For:** gRPC CLI debugging and scripting

#### 2. ghz (gRPC Benchmarking)
- **Language:** Go
- **Key Features:** Open-source benchmarking, .proto/protoset/reflection support, load testing
- **GitHub:** ghz/ghz
- **Best For:** gRPC performance and load testing

#### 3. strest-grpc
- **Language:** Go
- **Key Features:** Load testing for gRPC, scenario-based stress testing
- **Best For:** gRPC scalability and stress testing

### Framework Integration

#### 1. grpcmock
- **Language:** Java
- **Key Features:** Mocking framework for gRPC unit/integration tests
- **Best For:** Java gRPC testing

#### 2. karate-grpc
- **Language:** Java
- **Key Features:** Karate framework integration for gRPC testing via .proto
- **Best For:** BDD-style gRPC testing in Java

#### 3. hazana
- **Language:** Go
- **Key Features:** Go package for gRPC load testing
- **Best For:** Go-based gRPC performance testing

### Load Testing with gRPC Support

- **JMeter with gRPC Plugin** - Distributed load testing
- **k6** - JavaScript-based performance testing
- **Locust.io** - Python-based distributed testing

---

## API Mocking & Stubbing Tools

### Open-Source Mocking

#### 1. WireMock
- **Language:** Java
- **Key Features:** HTTP mock library, request matching, response templating, proxying, stateful behavior
- **GitHub:** tomakehurst/wiremock
- **Best For:** Java projects and standalone mock server

#### 2. Hoverfly
- **Language:** Go (multiple language bindings)
- **Key Features:** Capture/replay, lightweight proxy, random data generation, latency simulation
- **GitHub:** SpectoLabs/hoverfly
- **Best For:** Record-replay testing, CI/CD integration

#### 3. Mountebank
- **Language:** Node.js
- **Key Features:** Multi-protocol (HTTP/TCP/SMTP), simple config files, error simulation
- **GitHub:** bbyars/mountebank
- **Best For:** Cross-platform mocking, complex error scenarios

#### 4. MockServer
- **Language:** Java
- **Key Features:** Proxying, templating, logging, Java-based, Docker support
- **GitHub:** jamesdbloom/mockserver
- **Best For:** Integration testing, performance testing

#### 5. Prism (Stoplight)
- **Language:** Node.js/CLI
- **Key Features:** OpenAPI-driven mocking, validation, error simulation
- **GitHub:** stoplightio/prism
- **Best For:** Spec-first API development

#### 6. MSW (Mock Service Worker)
- **Language:** JavaScript
- **Key Features:** Client-side mocking, browser/Node.js support, GraphQL/REST
- **GitHub:** mswjs/msw
- **Best For:** Frontend component testing

#### 7. Microcks
- **Language:** Java/Docker
- **Key Features:** Customizable mocks, realistic examples, transformations
- **GitHub:** microcks/microcks
- **Best For:** Microservices mocking with realistic data

### Cloud-Based Mocking

#### 1. Postman Mock Servers
- **Platform:** Cloud (Postman workspace)
- **Key Features:** One-click mocks from collections, team sharing, versioning
- **Best For:** Teams already using Postman

#### 2. Mocki
- **Platform:** Cloud
- **Key Features:** Collaborative editing, random data generation, public URLs
- **Best For:** Remote team collaboration

#### 3. MockAPI
- **Platform:** Cloud
- **Key Features:** No-code GUI, Faker data generation, public sharing
- **Best For:** Quick mock endpoint sharing

#### 4. Beeceptor
- **Platform:** Cloud
- **Key Features:** Simple endpoint simulation, request inspection, error injection
- **Best For:** Quick temporary mocking

#### 5. Zuplo
- **Platform:** Cloud edge
- **Key Features:** Code-first edge mocking, policies, analytics
- **Best For:** Edge-deployed API mocking

#### 6. Apigee
- **Platform:** Cloud/On-premises
- **Key Features:** Enterprise API platform with mocking, policies, analytics
- **Best For:** Enterprise API management

#### 7. Requestly
- **Platform:** Browser extension/desktop
- **Key Features:** HTTP interception, response modification, request chaining
- **Best For:** Browser-based request/response manipulation

#### 8. Mockbin.io
- **Platform:** Cloud
- **Key Features:** Zero-setup OpenAPI mocking
- **Best For:** Quick OpenAPI-based mocking

---

## Contract Testing Tools

### Consumer-Driven Contract (CDC) Testing

#### 1. Pact
- **Language:** Multi-language (Java, JavaScript, Python, Go, Ruby, etc.)
- **Key Features:** Consumer-driven contracts, contract broker (PactFlow), provider verification
- **GitHub:** pact-foundation/pact
- **Best For:** Microservices ensuring consumer-provider compatibility

#### 2. PactFlow
- **Platform:** Cloud SaaS + AI
- **Key Features:** Contract registry, AI-driven test generation, SmartBear HaloAI integration
- **Company:** SmartBear (evolved from Pact)
- **Best For:** Teams wanting AI-powered CDC with maintenance

#### 3. Spring Cloud Contract
- **Language:** Java
- **Key Features:** Consumer-driven contracts, stub runner, HTTP/messaging support
- **Part Of:** Spring Cloud ecosystem
- **Best For:** Spring-based microservices

### OpenAPI/Spec-Based Contract Testing

#### 1. Dredd
- **Language:** Node.js/CLI
- **Key Features:** Validates API implementations against OpenAPI/API Blueprint, hooks for setup/cleanup
- **GitHub:** apiaryio/dredd
- **Best For:** API specification compliance validation

#### 2. Schemathesis
- **Language:** Python/CLI
- **Key Features:** Test generation from OpenAPI/GraphQL specs, property-based testing, coverage
- **GitHub:** schemathesis/schemathesis
- **Best For:** Comprehensive spec-based contract testing

#### 3. HyperTest
- **Platform:** Commercial SaaS
- **Key Features:** Auto-generates tests from recorded traffic, REST/GraphQL/gRPC/queues support
- **Company:** HyperTest.co
- **Best For:** Traffic-based automated test generation

#### 4. Signadot SmartTests
- **Platform:** Commercial SaaS
- **Key Features:** AI-powered zero-maintenance testing, detects breaking changes via real service behavior
- **Company:** Signadot
- **Best For:** Kubernetes-optimized REST API contract testing

#### 5. Tavern (Contract Mode)
- **Language:** Python
- **Key Features:** YAML-based contract verification for REST/MQTT
- **GitHub:** taverntesting/tavern
- **Best For:** Python teams wanting declarative contract testing

---

## API Performance & Load Testing Tools

### Open-Source Load Testing

#### 1. Apache JMeter
- **Language:** Java GUI/CLI
- **Key Features:** Thread groups, HTTP samplers, assertions, plugins, detailed reporting, CI/CD integration
- **GitHub:** apache/jmeter
- **Best For:** Versatile load/stress testing with rich UI

#### 2. k6
- **Language:** JavaScript/CLI
- **Key Features:** Developer-friendly scripting, high concurrency, cloud distribution, gRPC support
- **GitHub:** grafana/k6
- **Best For:** Modern load testing with JavaScript scripting

#### 3. Gatling
- **Language:** Scala DSL
- **Key Features:** Code-based load testing, asynchronous architecture, high performance, cloud support
- **GitHub:** gatling/gatling
- **Best For:** High-concurrency performance testing

#### 4. Locust
- **Language:** Python
- **Key Features:** Distributed load testing, real-time web UI, customizable user behaviors
- **GitHub:** locustio/locust
- **Best For:** Python-based customizable load testing

#### 5. Artillery
- **Language:** YAML/Node.js
- **Key Features:** Microservices load testing, cloud distribution, third-party integrations
- **GitHub:** artilleryio/artillery
- **Best For:** Microservices and serverless load testing

### Commercial Load Testing Platforms

#### 1. LoadRunner
- **Language:** Proprietary/C/JavaScript
- **Key Features:** Enterprise comprehensive testing, mobile/web/APIs, cloud support
- **Company:** Micro Focus
- **Best For:** Enterprise-scale performance testing

#### 2. BlazeMeter
- **Platform:** Cloud SaaS (JMeter-compatible)
- **Key Features:** Global traffic simulation, geographic distribution, integration with JMeter
- **Company:** BlazeMeter (Broadcom subsidiary)
- **Best For:** Cloud-native large-scale load testing

#### 3. Postman (Load Testing)
- **Platform:** Cloud (Postman workspace)
- **Key Features:** Collection-based load testing, integration with existing tests
- **Best For:** Teams already using Postman collections

#### 4. SoapUI (Load Testing)
- **Language:** Java
- **Key Features:** SOAP/REST load patterns, quick test execution
- **Best For:** SOAP/REST focused performance testing

### Specialized Performance Tools

#### 1. Apache Bench (ab)
- **Language:** C CLI
- **Key Features:** Simple HTTP benchmarking
- **Part Of:** Apache HTTP Server
- **Best For:** Quick single-endpoint benchmarking

#### 2. Loader.io
- **Platform:** Cloud SaaS
- **Key Features:** Free cloud-based load testing
- **Best For:** Quick free load testing trials

#### 3. LoadNinja
- **Platform:** Cloud SaaS
- **Key Features:** Browser-based load testing with JavaScript
- **Company:** Smartbear
- **Best For:** JavaScript-based load simulation

#### 4. NeoLoad
- **Language:** Proprietary
- **Key Features:** API/web/mobile performance testing
- **Company:** Micro Focus
- **Best For:** Enterprise performance testing

#### 5. Tsung
- **Language:** Erlang
- **Key Features:** Distributed load testing, high concurrency
- **Best For:** Systems requiring extreme concurrency

#### 6. WebLOAD
- **Language:** Proprietary
- **Key Features:** Web/API load testing
- **Best For:** Enterprise web/API performance

#### 7. Siege
- **Language:** C CLI
- **Key Features:** HTTP load testing and benchmarking
- **Best For:** Quick HTTP load testing

---

## Framework-Specific API Testing

### Python Ecosystem

- **pytest** - Test framework foundation
- **requests** + **pytest** - REST API testing
- **httpx** - Modern async HTTP client testing
- **responses** - Mock requests library
- **pytest-mock** - Mocking utilities
- **faker** - Test data generation

### JavaScript/TypeScript Ecosystem

- **Jest** - Test framework foundation
- **Supertest** - Express/HTTP testing
- **axios** - HTTP client for API calls
- **node-fetch** - Fetch API for testing
- **@testing-library** - Component testing
- **jest-mock-extended** - Advanced mocking
- **nock** - HTTP request mocking
- **jest-openapi** - OpenAPI schema validation

### Java Ecosystem

- **JUnit** - Test framework foundation
- **REST Assured** - Fluent REST testing API
- **TestNG** - Alternative test framework
- **Mockito** - Mocking framework
- **WireMock** - HTTP mocking
- **Spring Test** - Spring integration testing
- **RestTemplate + MockMvc** - Spring REST testing

### Go Ecosystem

- **testing** - Standard library
- **httptest** - Built-in HTTP server mocking
- **testify** - Assertions and mocking
- **go-resty** - HTTP client for testing
- **gomock** - Interface mocking

### Ruby Ecosystem

- **RSpec** - Testing framework
- **WebMock** - HTTP mocking
- **VCR** - HTTP request recording
- **Sinatra/Rails testing** - Framework-specific

---

## API Testing Tool Comparison Matrix

| Category | Tool | REST | GraphQL | gRPC | Contract | Mocking | Load Test | Open Source |
|----------|------|------|---------|------|----------|---------|-----------|-------------|
| **Core Platforms** | Postman | ✓ | ✓ | ◐ | ✓ | ✓ | ◐ | ✗ |
| | SoapUI | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ◐ |
| | Katalon Studio | ✓ | ✓ | ✗ | ◐ | ✓ | ✗ | ✗ |
| | Insomnia | ✓ | ✓ | ◐ | ✓ | ✓ | ✗ | ◐ |
| | Apidog | ✓ | ✓ | ◐ | ✓ | ✓ | ✗ | ✗ |
| **REST Frameworks** | Karate | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| | Citrus | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ |
| | REST Assured | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ |
| | Tavern | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ |
| **GraphQL** | GraphQL Inspector | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ |
| | Schemathesis | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ |
| | MSW | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ |
| **gRPC** | Kreya | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| | BloomRPC | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ |
| | grpcurl | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ |
| | ghz | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ |
| **Mocking** | WireMock | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ |
| | Hoverfly | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ |
| | Mountebank | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ |
| | MockServer | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ |
| | Prism | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ◐ |
| **Contract Testing** | Pact | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ |
| | Dredd | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ |
| | Spring Cloud Contract | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ |
| **Load Testing** | JMeter | ✓ | ✗ | ◐ | ✗ | ✗ | ✓ | ✓ |
| | k6 | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ |
| | Gatling | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| | Locust | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| | Artillery | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| | LoadRunner | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ |
| | BlazeMeter | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ |

Legend: ✓ = Full support | ◐ = Partial support | ✗ = No support

---

## Tool Selection Guide

### By API Type

**REST APIs:**
- Lightweight: Insomnia, Hoppscotch
- Enterprise: Postman, SoapUI, Katalon
- Automation: Karate, REST Assured, Tavern

**GraphQL APIs:**
- Manual testing: GraphiQL, GraphQL Playground, Apollo Studio
- Automation: Schemathesis, Supertest + Jest, MSW
- Schema validation: GraphQL Inspector

**gRPC Services:**
- GUI tools: Kreya, BloomRPC, Postman
- CLI tools: grpcurl, ghz
- Load testing: ghz, k6, JMeter (with plugin)

**Microservices:**
- Integration: Citrus, Karate
- Contract testing: Pact, Spring Cloud Contract
- Mocking: WireMock, Hoverfly, MockServer

### By Team Size

**Solo/Small Developers:**
- Insomnia, Postman (free tier), k6

**Mid-Size Teams:**
- Postman (paid), Katalon, Karate framework + CI/CD

**Enterprise:**
- LoadRunner, BlazeMeter, Katalon Studio, SoapUI

### By Use Case

**CI/CD Integration:**
- Karate, REST Assured, Dredd, k6, Artillery

**Performance Testing:**
- JMeter, k6, Gatling, Locust, LoadRunner, BlazeMeter

**Mocking/Stubbing:**
- WireMock, Hoverfly, MockServer, Prism, Postman Mock Servers

**Contract Testing:**
- Pact, Dredd, Schemathesis, Spring Cloud Contract

**Manual API Exploration:**
- Postman, Insomnia, Apidog, Kreya

---

## Installation & Getting Started

### Popular Framework Quick Starts

**Karate (Java/Maven):**
```xml
<dependency>
  <groupId>com.intuit.karate</groupId>
  <artifactId>karate-junit5</artifactId>
  <version>1.4.0</version>
</dependency>
```

**REST Assured (Java/Maven):**
```xml
<dependency>
  <groupId>io.rest-assured</groupId>
  <artifactId>rest-assured</artifactId>
  <version>5.3.1</version>
</dependency>
```

**Tavern (Python/pip):**
```bash
pip install tavern[pytest]
```

**k6:**
```bash
# macOS
brew install k6

# Direct
curl https://github.com/grafana/k6/releases/download/v0.47.0/k6-v0.47.0-macos-amd64.zip
```

**Pact:**
```bash
# JavaScript
npm install --save-dev @pact-foundation/pact

# Python
pip install pact
```

---

## Research Notes

This catalog was compiled from:
- Current tool documentation (2025-2026)
- Perplexity AI research with citations
- Tavily AI-powered search results
- Tool GitHub repositories and official sites
- Industry comparison studies and blogs

The field of API testing continues to evolve with increasing focus on:
- AI-driven test generation (HyperTest, PactFlow, Signadot)
- Contract-first development (OpenAPI, gRPC, Pact)
- Performance-as-code approaches (k6, Gatling)
- Multi-protocol support in unified platforms

---

## Related Topics

- API Development: OpenAPI, AsyncAPI, gRPC specifications
- Test Frameworks: Jest, Pytest, JUnit, TestNG
- CI/CD Platforms: GitHub Actions, GitLab CI, Jenkins
- Observability: Monitoring, tracing, logging for APIs
- Security Testing: OWASP ZAP, Burp Suite, security scanning

