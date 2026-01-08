# Test Doubles Quick Reference

Fast lookup guide for selecting test double frameworks by language and use case.

## By Language

### Java
```
Core Mocking:
  - Mockito (widest adoption, clean API)
  - EasyMock (record-replay-verify model)

Advanced:
  - JMockit (static/final/private methods)
  - PowerMock (extends Mockito/EasyMock)

API Testing:
  - WireMock (HTTP mocking)
  - REST-Assured (REST DSL)

Integration:
  - Testcontainers (Docker containers)
  - Spring Boot Test (Spring context)

Assertions:
  - AssertJ (fluent, chainable)
  - Hamcrest (matchers)
```

### Kotlin
```
Primary:
  - Mockk (idiomatic Kotlin, coroutines)

Fallback:
  - Mockito (JVM-compatible)
```

### JavaScript/TypeScript
```
Frameworks:
  - Jest (comprehensive, React)
  - Vitest (ESM, Vite-native, Jest-compatible)

Standalone:
  - Sinon.js (spies, stubs, fakes, timers)
  - testdouble.js (minimal API)
```

### Python
```
Standard:
  - unittest.mock (built-in)

With pytest:
  - pytest-mock (fixture-based)

Time Mocking:
  - freezegun (freeze/advance time)
```

### Go
```
Interface Mocking:
  - GoMock + mockgen (code generation)
  - testify (suite, assert, mock)

File System:
  - afero (filesystem abstraction)
  - memfs (in-memory filesystem)
```

---

## By Use Case

### Unit Testing
| Language | Tool | Key Feature |
|----------|------|-------------|
| Java | Mockito | Clean DSL, no bytecode modification |
| Kotlin | Mockk | Coroutines, idiomatic syntax |
| JavaScript | Jest | Built-in mocking, comprehensive |
| Python | unittest.mock | Built-in, no dependencies |
| Go | GoMock | Interface-based, code generation |

### Time-Dependent Testing
| Language | Tool |
|----------|------|
| Python | freezegun |
| JavaScript | Jest fake timers, Sinon.js |
| Java | Mockito + Clock/TimeProvider injection |
| Go | testify + time.Now mocking |

### File System Mocking
| Language | Tool |
|----------|------|
| Go | afero, memfs |
| Python | pytest-monkeypatch |
| JavaScript | jest.mock(), Sinon.js |
| Java | PowerMock, custom mocks |

### Database Testing
| Language | Tool |
|----------|------|
| Java | Testcontainers |
| All | Testcontainers (Docker-based) |
| Spring | Spring Boot Test |

### API/HTTP Testing
| Purpose | Tool |
|---------|------|
| HTTP Mocking | WireMock, MockServer, Prism |
| No-code API Mocking | Mockoon |
| REST Endpoint Testing | REST-Assured |
| OpenAPI-driven | Prism |

### Assertion/Verification
| Language | Tool |
|----------|------|
| Java | AssertJ, Hamcrest |
| All | Framework-specific (Jest, Vitest, etc.) |

---

## Feature Comparison

### Mocking Capabilities
```
Full Support (Mocks, Stubs, Spies, Fakes):
  - Mockito, JMockit, PowerMock
  - Mockk
  - Jest, Vitest, Sinon.js, testdouble.js
  - unittest.mock, pytest-mock
  - GoMock, testify

Limited Support:
  - EasyMock (no spies)
  - freezegun (time fakes only)
```

### Special Features
```
Bytecode Manipulation (advanced):
  - JMockit, PowerMock

Fake Timers:
  - freezegun (Python)
  - Jest, Vitest, Sinon.js (JavaScript)

In-Memory File Systems:
  - memfs (Go)
  - afero (Go)

Docker Integration:
  - Testcontainers

OpenAPI Support:
  - Prism

GUI/No-Code:
  - Mockoon
```

---

## Quick Lookup by Problem

### "I need to mock a static method in Java"
→ JMockit or PowerMock

### "I need to freeze time in Python tests"
→ freezegun

### "I need to mock an HTTP API"
→ WireMock (Java), MockServer, Prism, or Mockoon

### "I need in-memory database testing"
→ Testcontainers (real Docker DB)

### "I need ESM-native testing in JavaScript"
→ Vitest

### "I need interface-based mocking in Go"
→ GoMock with mockgen

### "I need file system mocking in Go"
→ afero or memfs

### "I need coroutine mocking in Kotlin"
→ Mockk

### "I need fluent assertions in Java"
→ AssertJ

### "I need minimal, framework-independent JS mocking"
→ testdouble.js or Sinon.js

### "I need Spring Boot integration testing"
→ Spring Boot Test with @SpringBootTest

### "I need multi-protocol mocking (HTTP, HTTPS, SOCKS)"
→ MockServer

---

## Package Names & Imports

### Java
```gradle
// Mockito
testImplementation 'org.mockito:mockito-core:5.x'
testImplementation 'org.mockito:mockito-junit-jupiter:5.x'

// JMockit
testImplementation 'org.jmockit:jmockit:1.x'

// PowerMock
testImplementation 'org.powermock:powermock-module-junit4:2.x'

// Mockk (Kotlin)
testImplementation 'io.mockk:mockk:1.x'

// WireMock
testImplementation 'com.github.tomakehurst:wiremock-jre8:3.x'

// Testcontainers
testImplementation 'org.testcontainers:testcontainers:1.x'

// REST-Assured
testImplementation 'io.rest-assured:rest-assured:5.x'

// AssertJ
testImplementation 'org.assertj:assertj-core:3.x'

// Hamcrest
testImplementation 'org.hamcrest:hamcrest:2.x'
```

### JavaScript
```json
{
  "devDependencies": {
    "jest": "^29.x",
    "vitest": "^1.x",
    "sinon": "^17.x",
    "testdouble": "^3.x"
  }
}
```

### Python
```python
# unittest.mock (built-in)
from unittest.mock import Mock, patch, MagicMock

# pytest-mock
pip install pytest-mock

# freezegun
pip install freezegun
```

### Go
```bash
# GoMock
go install github.com/golang/mock/cmd/mockgen@latest

# testify
go get github.com/stretchr/testify

# afero
go get github.com/spf13/afero

# memfs
go get github.com/psanford/memfs
```

---

## Estimated Learning Curve

### Easy (< 1 day)
- Mockito
- unittest.mock
- Jest (for module mocking)
- Sinon.js

### Moderate (1-3 days)
- JMockit
- PowerMock
- pytest-mock
- GoMock
- testify
- Vitest

### Steep (3+ days)
- Testcontainers (complex setup)
- WireMock (stateful mocking)
- Spring Boot Test (context management)

---

## Active Maintenance Status (2026)

### Actively Maintained
- Mockito (Java)
- Mockk (Kotlin)
- Jest, Vitest (JavaScript)
- freezegun (Python)
- GoMock, testify (Go)
- Testcontainers (Java)

### Stable/Mature
- EasyMock (Java)
- unittest.mock (Python)
- Sinon.js (JavaScript)
- WireMock (Java)

### Declining
- PowerMock (replaced by refactoring patterns)
- Jasmine (replaced by Jest/Vitest)

