# Test Doubles & Mocking Index

Comprehensive research index for test double frameworks, mocking libraries, and related testing tools across multiple programming languages.

## Research Files

### 1. **MOCKING_TEST_DOUBLES_COMPREHENSIVE.md** (Primary Reference)
Complete guide with:
- 25+ test double frameworks and libraries
- One-sentence descriptions of each tool
- Organization by category (Java, JavaScript, Python, Go, HTTP/API)
- Integration & assertion libraries
- Feature coverage matrix showing capabilities
- Language-specific recommendations
- Selection guide by use case
- Recent trends and updates for 2026

### 2. **MOCKING_TEST_DOUBLES_QUICK_REFERENCE.md** (Fast Lookup)
Quick reference guide including:
- Tools organized by language
- Tools organized by use case
- Feature comparison tables
- Quick lookup by problem statement
- Package names and import statements
- Learning curve estimates
- Maintenance status summary

### 3. **MOCKING_TEST_DOUBLES_TOOLS_CATALOG.csv** (Data Export)
Structured catalog with columns:
- Tool name, Language, Category, Type
- Primary use case, Mocking capabilities
- Special features (time, database, file system)
- Support matrix (mocks, stubs, spies, fakes)
- Notes on adoption and compatibility

## Key Tools by Category

### Core Mocking Frameworks
- **Java:** Mockito, JMockit, PowerMock, EasyMock
- **Kotlin:** Mockk
- **JavaScript:** Jest, Vitest, Sinon.js, testdouble.js
- **Python:** unittest.mock, pytest-mock
- **Go:** GoMock, testify

### Specialized Categories

**Time/Date Mocking:**
- freezegun (Python)
- Jest/Vitest fake timers (JavaScript)
- Sinon.js fake timers (JavaScript)

**File System Mocking:**
- afero (Go filesystem abstraction)
- memfs (Go in-memory filesystem)
- pytest-monkeypatch (Python)
- jest.mock() (JavaScript)

**Database Testing:**
- Testcontainers (Docker-based, language-agnostic)
- Spring Boot Test (Spring applications)

**API/HTTP Mocking:**
- WireMock (Java HTTP mocking)
- MockServer (multi-protocol)
- Prism (OpenAPI-driven)
- Mockoon (no-code desktop app)

**Assertion Libraries:**
- AssertJ (Java fluent assertions)
- Hamcrest (Java matchers)

## Research Methodology

Information gathered from:
- Perplexity AI with citations (current 2026 data)
- Tavily AI-powered search (web research)
- Official documentation and project websites

### Coverage Areas

1. **Test Double Types:** Mocks, stubs, spies, fakes
2. **Dependency Injection:** Mocking support in Spring Boot, Guice, Dagger, FastAPI, Go interfaces
3. **Database Mocking:** Testcontainers, in-memory databases, connection mocking
4. **Time/Date Mocking:** System clock control, datetime freezing
5. **File System Mocking:** Virtual filesystems, path mocking
6. **API/HTTP Mocking:** Service mocking, traffic simulation
7. **Language Support:** Java, Kotlin, JavaScript, TypeScript, Python, Go

## Quick Selection Guide

### By Language
| Language | Primary | Alternative | Specialized |
|----------|---------|-------------|------------|
| Java | Mockito | EasyMock | JMockit (advanced), WireMock (API) |
| Kotlin | Mockk | Mockito | - |
| JavaScript | Jest | Vitest | Sinon.js (standalone) |
| Python | unittest.mock | pytest-mock | freezegun (time) |
| Go | GoMock | testify | afero (files), memfs (FS) |

### By Use Case
| Scenario | Recommended Tools |
|----------|-------------------|
| Unit testing with DI | Mockito (Java), Mockk (Kotlin), Jest (JS), unittest.mock (Python), GoMock (Go) |
| Time-dependent tests | freezegun (Python), Jest/Sinon.js (JavaScript) |
| File system testing | afero/memfs (Go), pytest-monkeypatch (Python), jest.mock (JavaScript) |
| Integration testing | Testcontainers (all languages), Spring Boot Test (Spring) |
| API testing | WireMock, MockServer, REST-Assured (Java), Prism |
| Advanced mocking | JMockit, PowerMock (static/final/private methods) |

## Feature Comparison Summary

### Capabilities Matrix
- **Full Support (Mocks, Stubs, Spies, Fakes):** Mockito, JMockit, PowerMock, Mockk, Jest, Vitest, Sinon.js, testdouble.js, unittest.mock, pytest-mock, GoMock, testify
- **Partial Support:** EasyMock (no spies), freezegun (time-only), afero/memfs (file system only)
- **API-Only:** WireMock, MockServer, Prism, Mockoon

### Advanced Features
- **Bytecode Manipulation:** JMockit, PowerMock (for static/final methods)
- **Fake Timers:** freezegun, Jest, Vitest, Sinon.js
- **In-Memory FS:** memfs, afero
- **Docker Integration:** Testcontainers
- **OpenAPI Support:** Prism
- **No-Code UI:** Mockoon

## Maintenance & Adoption Status

### Highly Active (Regular Updates)
- Mockito, JMockit, Mockk
- Jest, Vitest
- freezegun
- GoMock, testify
- Testcontainers

### Stable (Mature)
- EasyMock, PowerMock
- Sinon.js, testdouble.js
- unittest.mock
- WireMock, MockServer
- AssertJ, Hamcrest

### Declining
- PowerMock (being phased out in favor of refactoring)
- Jasmine (superseded by Jest/Vitest)

## Usage Patterns

### Dependency Injection Mocking
```
Spring Boot: Mockito + @Mock/@InjectMocks
Go: GoMock + interface-based design
FastAPI: unittest.mock + pytest fixtures
Angular: Jasmine/Karma (legacy) or Jest
```

### Database Mocking
```
Integration Testing: Testcontainers + real database
Unit Testing: Mockito (Java), unittest.mock (Python)
ORM Testing: WireMock or mock at connection level
```

### Time-Dependent Testing
```
Python: freezegun.freeze_time() decorator
JavaScript: jest.useFakeTimers() or sinon.useFakeTimers()
Java: Mockito + Clock/TimeProvider injection
Go: Interface-based time.Now() mocking
```

### File System Mocking
```
Go: afero.Fs interface
Python: monkeypatch.setattr() or mock.patch()
JavaScript: jest.mock('fs') or memfs
Java: PowerMock for static file operations
```

## Recommended Reading Order

1. **Start Here:** MOCKING_TEST_DOUBLES_QUICK_REFERENCE.md
   - Fast overview, language-specific recommendations

2. **For Details:** MOCKING_TEST_DOUBLES_COMPREHENSIVE.md
   - Full descriptions, coverage matrix, selection guide

3. **For Lookup:** MOCKING_TEST_DOUBLES_TOOLS_CATALOG.csv
   - Data export, feature comparison, structured format

## Related Resources

- **Testing Frameworks:** Jest, Vitest, Pytest, Go testing
- **Integration Tools:** Testcontainers, Docker
- **API Documentation:** OpenAPI/Swagger specifications
- **CI/CD Integration:** GitHub Actions, Jenkins

## Statistics

- **Total Tools Cataloged:** 24+
- **Languages Covered:** 5 (Java, Kotlin, JavaScript, Python, Go)
- **Categories:** 6 (Mocking, API, Database, File System, Time, Assertions)
- **Research Sources:** 15+ citations from 2026
- **Last Updated:** 2026-01-01

---

## Document Descriptions

### MOCKING_TEST_DOUBLES_COMPREHENSIVE.md
- **Type:** Reference documentation
- **Size:** 500+ lines
- **Audience:** Developers, architects, QA engineers
- **Contents:** Full tool descriptions, feature matrix, recommendations
- **Use:** Deep dives, architecture decisions, comprehensive comparison

### MOCKING_TEST_DOUBLES_QUICK_REFERENCE.md
- **Type:** Quick lookup guide
- **Size:** 300+ lines
- **Audience:** Developers looking for fast answers
- **Contents:** Tables, quick lookups, code examples
- **Use:** Day-to-day development, tool selection, syntax reference

### MOCKING_TEST_DOUBLES_TOOLS_CATALOG.csv
- **Type:** Data export
- **Format:** CSV (importable to spreadsheets, databases)
- **Columns:** 14 fields (name, language, type, features, etc.)
- **Use:** Data analysis, filtering, integration with other tools

---

Generated with comprehensive research using Perplexity AI and Tavily search.
