# Snapshot Testing - Quick Reference Guide

A rapid reference guide for selecting and implementing snapshot testing tools and libraries.

---

## By Programming Language

### JavaScript/TypeScript
```
Primary:        Jest, Vitest
HTTP Mocking:   MSW, nock, WireMock
Schema Validation: AJV, Zod, Joi
OpenAPI:        Spectral, Prism, Dredd
Visual:         Playwright, Storybook
```

### Python
```
Primary:        Syrupy, pytest-snapshot
HTTP Recording: Betamax, Responses
OpenAPI:        Schemathesis
Data:           Great Expectations, Dbt
```

### Go
```
Snapshots:      Cupaloy
HTTP Recording: Go-VCR
General:        Testify, httptest
```

### Rust
```
Primary:        Insta (production), Snaptest
Testing:        Criterion (benchmarks)
```

### Java
```
Snapshots:      ApprovalTests, AssertJ Snapshot
Architecture:   ArchUnit
Database:       DbUnit, Testcontainers
Contracts:      Spring Cloud Contract
```

### .NET
```
Primary:        Verify
Alternative:    Approve
Visual:         Playwright .NET
```

---

## By Use Case

### API Response Testing
```
Contract Testing:     Pact, PactFlow, HyperTest
OpenAPI-First:        Dredd, Schemathesis, Spectral
Record/Replay:        VCR, WireMock, MockServer, Prism
Mock Servers:         Mockoon, json-server, Postman Mock Server
```

### Data Structure Comparison
```
JSON Schema:          AJV, Zod, Joi, TypeBox
Complex Objects:      Verify (.NET), AssertJ Snapshot (Java), ApprovalTests
Binary Formats:       Protocol Buffers, Avro, MessagePack
Serialization:        Thrift (cross-language)
```

### Database Testing
```
Fast Test Isolation:  SQL Server/Oracle Snapshots
Containerized:        Testcontainers
Schema Management:    Liquibase, Flyway
Data Validation:      Great Expectations, Dbt
```

### Microservices Testing
```
Consumer-Driven:      Pact + Pact Broker
Modern Alternative:   HyperTest
Spring Framework:     Spring Cloud Contract
Language-Agnostic:    Dredd
```

### Visual Regression
```
UI Components:        Storybook, Percy
Full Screenshots:     Playwright, Cypress, BackstopJS
CSS Regression:       PhantomCSS, BackstopJS
Self-Hosted:          BackstopJS
```

---

## Decision Matrix

### I need to test...

**REST API responses**
- Lightweight mock: `json-server`, `Mockoon`, `MSW`
- Record/replay: `WireMock`, `Prism`, HTTP mocking libs
- Contract testing: `Pact` or `HyperTest`
- Specification compliance: `Dredd`, `Schemathesis`

**JSON data**
- Validation: `AJV` (JS), `Zod` (TS), `Joi` (Node.js)
- Complex shapes: `ApprovalTests`, `Verify`
- OpenAPI responses: `Spectral`, `Apidog`

**Microservices together**
- Consumer-driven contracts: `Pact` + `Pact Broker`
- Modern approach: `HyperTest`, `PactFlow`
- Spring apps: `Spring Cloud Contract`

**Database state**
- Quick test cycles: SQL Server/Oracle snapshots
- Multiple databases: `Testcontainers`
- Schema changes: `Liquibase`, `Flyway`
- Data quality: `Great Expectations`, `Dbt`

**UI components**
- Snapshot testing: `Jest`, `Vitest`, `Storybook`
- Visual regression: `Percy`, `BackstopJS`, `Playwright`
- CSS regression: `PhantomCSS`

**Serialized data**
- Protocol buffers: Schema versioning built-in
- Avro: Schema evolution support
- BSON: MongoDB-native testing

**Smart contracts**
- Fuzzing: `Echidna`, `Medusa`
- Security analysis: `Slither`
- Development: `Foundry`, `Hardhat`
- Simulation: `Tenderly`

---

## Cross-Language Tools

| Tool | Languages | Best For |
|------|-----------|----------|
| **ApprovalTests** | 14+ languages | Golden master snapshot testing |
| **Testcontainers** | Java, Go, Python, Node.js, .NET | Containerized integration testing |
| **Protocol Buffers** | All major languages | gRPC, typed serialization |
| **Avro** | All major languages | Data pipelines, schema evolution |

---

## 2025 Trends

1. **AI-Augmented:** PactFlow auto-generates tests from code/specs
2. **Spec-First:** Spectral, Prism, Dredd for OpenAPI validation
3. **Multi-Language:** Testcontainers ecosystem expanding
4. **TypeScript:** Zod, TypeBox, Vitest dominance
5. **Contract Focus:** HyperTest, PactFlow for microservices

---

## Setup Time Estimates

| Tool | Setup Time | Configuration |
|------|-----------|---------------|
| Jest | 5 min | Zero-config default |
| Vitest | 5 min | Vite integration |
| Syrupy | 5 min | `pip install`, one import |
| Testcontainers | 10 min | Docker required |
| Pact | 15 min | Broker setup optional |
| Dredd | 10 min | OpenAPI spec required |
| SQL Server Snapshots | 2 min | Native SQL commands |

---

## Free vs Paid

### Completely Free/Open Source
```
Jest, Vitest, Syrupy, ApprovalTests, Insta, Pact, Dredd
Spectral, AJV, Zod, WireMock, Mockoon, json-server
Testcontainers, Liquibase, Flyway, Great Expectations
Playwright, Cypress, BackstopJS, Puppeteer
Protocol Buffers, Avro, Thrift
```

### Free with Premium Options
```
PactFlow (free tier + enterprise)
Apidog (free + paid)
Postman (free + paid)
Percy (free tier + SaaS)
Tenderly (free tier + enterprise)
```

### Fully Paid/Commercial
```
HyperTest (modern contract testing)
MockServer (commercial support)
Swagger Editor (Stoplight ecosystem)
```

---

## Common Workflows

### Workflow: REST API Testing (No Real Backend)
```
1. Define OpenAPI spec
2. Mock server: Prism or Mockoon
3. HTTP mocking: MSW or nock
4. Schema validation: AJV or Zod
5. Contract testing: Pact (optional)
```

### Workflow: Microservices Testing
```
1. Define service contracts
2. Generate stubs: Spring Cloud Contract or Pact
3. Consumer-driven tests: Pact
4. Deploy gates: Pact Broker "can-i-deploy"
5. Specification validation: Dredd (optional)
```

### Workflow: Python API Testing
```
1. Define OpenAPI (optional)
2. HTTP recording: Betamax or Responses
3. Snapshots: Syrupy
4. Schema: JSON validation via Pydantic
5. Test generation: Schemathesis (from OpenAPI)
```

### Workflow: Database Integration Testing
```
1. Container setup: Testcontainers
2. Schema migration: Flyway or Liquibase
3. Data fixtures: Snapshots or DbUnit
4. Data validation: Great Expectations
5. Teardown: Auto-cleanup from containers
```

### Workflow: Component/UI Snapshot Testing
```
1. Test framework: Jest or Vitest
2. Component testing: React Testing Library
3. Snapshots: Built-in to test runner
4. Visual regression: Storybook or Percy
5. Review: GitHub-integrated visual diffs
```

---

## Performance Considerations

| Tool | Speed | Considerations |
|------|-------|-----------------|
| Jest snapshots | Very Fast | In-memory, optimized |
| Syrupy | Very Fast | Pure Python, pytest integration |
| WireMock | Fast | HTTP stub matching |
| Testcontainers | Slower | Container startup overhead |
| SQL snapshots | Very Fast | <1 second rollback |
| Percy | Slow | Cloud processing required |
| Dredd | Medium | HTTP requests required |

---

## Testing Coverage

| Category | Tool | Coverage |
|----------|------|----------|
| Unit Snapshots | Jest, Vitest, Syrupy | Functions, objects |
| API Snapshots | Pact, Dredd, Schemathesis | Request/response pairs |
| Database | Testcontainers, Snapshots | Schema, data states |
| Contract | Pact, HyperTest, Spring Cloud | Service interactions |
| Visual | Storybook, Percy, Playwright | Component rendering |
| Security | Slither, Echidna, Manticore | Smart contracts |

---

## Integration Checklist

- [ ] Snapshot files in version control? (Usually yes)
- [ ] Snapshot review process? (GitHub/Gitea review)
- [ ] Automated snapshot updates? (Jest `--updateSnapshot`)
- [ ] CI/CD gates? (Fail on unexpected changes)
- [ ] Snapshot cleanup? (Remove obsolete snapshots)
- [ ] Performance monitoring? (Snapshot size, comparison time)

---

## Recommended Stacks by Team Size

### Solo Developer
```
Jest/Vitest + Syrupy + MSW + AJV
Minimal setup, maximum productivity
```

### Small Team (2-5)
```
Jest + Pact (optional) + Testcontainers + Spectral
Add contract testing as team grows
```

### Growing Team (5-15)
```
Pact Broker + HyperTest + Dredd + Great Expectations
Full microservices testing suite
```

### Enterprise
```
PactFlow + Spring Cloud Contract + Testcontainers + Dbt
AI-augmented testing, comprehensive pipelines
```

