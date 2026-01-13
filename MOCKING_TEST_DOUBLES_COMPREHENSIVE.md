# Test Doubles Framework Comprehensive Guide

A comprehensive catalog of test double frameworks, libraries, and tools for mocking, stubbing, faking, and spying across programming languages.

## Core Java Mocking Frameworks

- **Mockito** - Popular Java mocking framework that enables creating mocks, spies, and stubs for clean, readable unit tests without requiring runtime bytecode modification.
- **JMockit** - Advanced Java library for mocking, stubbing, and verifying using Java agents for bytecode manipulation to handle complex scenarios like final classes and static methods.
- **PowerMock** - Extension of Mockito and EasyMock for Java that allows mocking of static methods, constructors, final classes, and private methods via bytecode manipulation.
- **EasyMock** - Java mocking framework that simplifies creating dynamic mock objects to simulate dependencies and verify interactions using a record-replay-verify model.
- **Mockk** - Lightweight mocking library for Kotlin that supports coroutines, dynamic DSL, and relaxed mocks with concise, idiomatic syntax for Android and JVM testing.

## JavaScript/TypeScript Mocking Frameworks

- **Jest** - Comprehensive JavaScript testing framework with built-in mocking capabilities for modules, timers, and functions, commonly used for React and Node.js testing.
- **Vitest** - Vite-powered unit testing framework for JavaScript/TypeScript with native ESM support, fast execution, and mocking features similar to Jest for modern web projects.
- **Sinon.js** - JavaScript library providing spies, stubs, and mocks for standalone test doubles, fake timers, XHR, and server features with flexible chaining and assertions.
- **testdouble.js** - Minimalistic JavaScript library for creating intuitive test doubles with a streamlined API using functions like `td.function`, `td.object`, and `td.replace` for stubbing and verification.

## Python Mocking and Test Libraries

- **unittest.mock** - Python's standard library module for patching, mocking objects, and asserting call interactions in unittest-based tests without external dependencies.
- **pytest-mock** - Pytest plugin that provides flexible monkeypatching and fixture-based mocking for creating test doubles and verifying interactions in Python tests.
- **freezegun** - Python library for freezing and manipulating datetime objects in tests to control time-dependent behavior without altering system clocks.
- **mock** - Backport of unittest.mock for older Python versions, providing mocking and patching utilities for legacy projects.

## Go Mocking and Test Libraries

- **GoMock** - Google's official Go mocking framework that generates mocks from interfaces using the mockgen tool for precise verification in table-driven tests.
- **testify** - Go toolkit including assertions, mocking, and suite support with mock objects generated from interfaces for expressive and maintainable tests.
- **afero** - Go filesystem abstraction library enabling in-memory or mock filesystems as test doubles to isolate file I/O operations during testing.
- **memfs** - Go in-memory filesystem implementation used as a test double to simulate disk operations without real file system side effects.

## HTTP/API Mocking Tools

- **WireMock** - Java-based tool for HTTP mocking and stubbing that simulates API responses, faults, and proxying to isolate services during integration testing.
- **MockServer** - Tool for mocking HTTP, HTTPS, and SOCKS services, allowing simulation of APIs, fault injection, proxying, and verification of client-server interactions.
- **Prism** - Open-source HTTP mock server and proxy tool designed for testing API clients by simulating responses, capturing traffic, and supporting OpenAPI specifications.
- **Mockoon** - Desktop application for creating and running realistic mock REST APIs, enabling fast API mocking without coding for development and testing workflows.

## Integration Testing & Database Mocking

- **Testcontainers** - Java library that allows spinning up real Docker containers for integration tests, providing disposable environments for databases, browsers, and services.
- **Spring Boot Test** - Official testing module of Spring Boot offering annotations and utilities like @SpringBootTest for comprehensive integration testing of Spring applications with auto-configured contexts.
- **REST-Assured** - Java DSL for simplifying testing of REST services by making HTTP requests and validating responses in a readable, chainable syntax.

## Assertion & Verification Libraries

- **AssertJ** - Fluent assertion library for Java that provides readable, chainable assertions with rich error messages, improving test code clarity over standard JUnit asserts.
- **Hamcrest** - Java library providing matcher objects for more expressive and readable assertions in unit tests, commonly used with JUnit and other testing frameworks.

---

## Organization by Category

### Mocking Frameworks (by Language)

**Java:**
- Mockito
- JMockit
- PowerMock
- EasyMock
- Mockk (Kotlin)

**JavaScript/TypeScript:**
- Jest
- Vitest
- Sinon.js
- testdouble.js

**Python:**
- unittest.mock
- pytest-mock
- freezegun

**Go:**
- GoMock
- testify

### Database & Integration Testing

- Testcontainers (Docker-based integration testing)
- Spring Boot Test (Spring applications)
- REST-Assured (REST API testing)

### File System Mocking

- afero (Go filesystem abstraction)
- memfs (Go in-memory filesystem)
- pytest-monkeypatch (Python file patching)
- jest.mock() (JavaScript module mocking)

### Time/Date Mocking

- freezegun (Python)
- Sinon.js fake timers (JavaScript)
- Jest fake timers (JavaScript)
- testify mocks (Go time.Now)
- Mockito (Java Clock/TimeProvider)

### API & HTTP Mocking

- WireMock (Java HTTP mocking)
- MockServer (Multi-protocol mocking)
- Prism (OpenAPI-driven mocking)
- Mockoon (No-code API mocking)

### Assertion & Verification

- AssertJ (Java fluent assertions)
- Hamcrest (Java matchers)

---

## Coverage Matrix

| Tool | Mocks | Stubs | Spies | Fakes | DI Support | Time Mock | DB Mock | FS Mock |
|------|-------|-------|-------|-------|------------|-----------|---------|---------|
| Mockito | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| JMockit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PowerMock | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| EasyMock | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Mockk | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Jest | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Vitest | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sinon.js | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| testdouble.js | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| unittest.mock | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| pytest-mock | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| freezegun | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ |
| GoMock | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| testify | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| WireMock | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| MockServer | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Testcontainers | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ | ✗ |

---

## Language-Specific Recommendation Summary

### Java
- **Primary:** Mockito (general purpose, widely adopted)
- **Advanced:** JMockit or PowerMock (for static/final/private methods)
- **API Testing:** WireMock or REST-Assured
- **Integration:** Testcontainers or Spring Boot Test
- **Assertions:** AssertJ for fluent assertions

### Kotlin
- **Primary:** Mockk (idiomatic Kotlin syntax, coroutine support)
- **Fallback:** Mockito (compatible with JVM)

### JavaScript/TypeScript
- **Primary:** Jest (React/Vue projects, Node.js)
- **Modern:** Vitest (ESM support, Vite projects)
- **Standalone:** Sinon.js (framework-independent)
- **Minimal:** testdouble.js (lean API)

### Python
- **Standard:** unittest.mock (built-in, no dependencies)
- **With pytest:** pytest-mock (fixture-based approach)
- **Time Mocking:** freezegun (datetime control)

### Go
- **Interface Mocking:** GoMock + mockgen (code generation)
- **General Assertions:** testify (suite, assert, mock)
- **File System:** afero (filesystem abstraction)

---

## Selection Guide

### For Unit Testing
- **Java:** Mockito or EasyMock
- **JavaScript:** Jest or Vitest
- **Python:** unittest.mock or pytest-mock
- **Go:** GoMock or testify

### For Time-Dependent Tests
- **Python:** freezegun
- **JavaScript:** Jest fake timers or Sinon.js
- **Java:** Mockito + Clock injection
- **Go:** testify + time.Now mocking

### For File System Testing
- **Go:** afero or memfs
- **Python:** pytest-monkeypatch
- **JavaScript:** jest.mock() or Sinon.js
- **Java:** PowerMock or custom mocks

### For API/HTTP Testing
- **WireMock:** Comprehensive HTTP mocking (Java)
- **MockServer:** Multi-protocol support
- **Prism:** OpenAPI-spec-driven testing
- **Mockoon:** GUI-based API mocking

### For Integration Testing
- **Testcontainers:** Docker-based (databases, services)
- **Spring Boot Test:** Spring application context
- **REST-Assured:** REST endpoint testing

---

## Recent Trends & Updates (2026)

- **Go:** Increased adoption of interface-based mocking with GoMock and testify
- **JavaScript:** Vitest gaining adoption in ESM-first projects as Jest alternative
- **Python:** freezegun remains standard for time mocking; unittest.mock stable in 3.13+
- **Java:** Mockito continues dominance; PowerMock usage declining in favor of refactoring patterns
- **Integration:** Testcontainers increasingly popular for reliable integration tests vs. in-memory databases

