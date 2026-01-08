# Mocking Documentation Research - Summary

**Date:** 2026-01-01
**Topic:** Mocking, test doubles, API mocking, and testing frameworks

## Overview

Comprehensive research on mocking tools and testing frameworks to identify documentation gaps in llm-code-docs. Used 5 parallel haiku sub-agents with perplexity-cli and tavily skills to research across multiple categories.

## Research Categories

1. **Language-specific mocking libraries** - Python, JavaScript/TypeScript, Java, Go, .NET, Kotlin
2. **API/HTTP mocking tools** - Service virtualization, HTTP mocking, GraphQL mocking
3. **Test doubles frameworks** - Mocks, stubs, fakes, spies
4. **Browser/E2E mocking** - Playwright, Puppeteer, Cypress, Selenium network interception
5. **Specialized mocking** - Cloud services, Docker/containers, message queues, gRPC, WebSockets

## Key Findings

### Total Tools Identified: ~150+

**Already documented in llm-code-docs:**
- Vitest, Postman, Prism, Apollo, GraphQL, Moto, Storybook, Cypress

**Missing documentation: 62 high-priority tools**

Created TRCKR tickets **TRCKR-2533 through TRCKR-2594** in the DOCS project with `docs-add` labels for:

### Language-Specific Frameworks (17 tools)
- Mockito, Sinon.JS, pytest-mock, GoMock, Moq, Mockk, Spock, Testify
- JMockit, PowerMock, EasyMock, ts-mockito, testdouble.js
- NSubstitute, FakeItEasy, mockery, moq (CLI)

### API/HTTP Mocking (16 tools)
- WireMock, Mockoon, MSW (Mock Service Worker), Nock, Hoverfly, Mitmproxy
- Microcks, MirageJS, Axios Mock Adapter, GraphQL Faker, VCR.py
- Fiddler, Charles Proxy, Apollo MockedProvider, graphql-tools, json-server

### Browser/E2E Testing (5 tools)
- Playwright, Puppeteer, Selenium, WebdriverIO, BrowserStack

### Cloud/Container Mocking (2 tools)
- LocalStack, Testcontainers

### Specialized Mocking (22 tools)
- Time mocking: freezegun
- Testing frameworks: Jasmine
- WebSocket: Service Worker Mock, socket.io-mock, mock-socket
- Assertions: AssertJ, Hamcrest
- Integration: REST-Assured, Spring Boot Test
- gRPC: grpcmock, grpc-go-testing, ghz
- Message queues: rabbitmq-mock, kafka-unit, embedded-kafka
- Databases: redis-mock, dynamodb-local, mongomock, H2 Database
- Filesystem: afero
- Component testing: React Testing Library, Vue Test Utils

## Research Artifacts

Created comprehensive reference documents (in /tmp/ or working directory):

1. **MOCKING_TEST_DOUBLES_LIBRARIES.md** - Language-specific mocking frameworks by language
2. **API_MOCKING_TOOLS_COMPREHENSIVE.md** - HTTP/API mocking servers and tools
3. **MOCKING_TEST_DOUBLES_COMPREHENSIVE.md** - Complete test doubles framework guide
4. **MOCKING_TEST_DOUBLES_TOOLS_CATALOG.csv** - Structured data for analysis
5. **MOCKING_TEST_DOUBLES_QUICK_REFERENCE.md** - Quick lookup guide
6. **BROWSER_MOCKING_NETWORK_MOCKING_TOOLS.md** - Browser and frontend mocking
7. **SPECIALIZED_MOCKING_TOOLS.md** - Cloud, container, gRPC, WebSocket mocking

## TRCKR Tickets Created

All 62 tickets created in DOCS project with:
- Status: `todo`
- Priority: `medium`
- Labels: `docs-add`
- Description: One-sentence summary of each tool

## Next Steps

Documentation writer agents (llm-code-docs-writer) can pick up any of these tickets to:
1. Check if documentation exists via llms.txt
2. Probe for llms.txt at official domains
3. Check GitHub repos for documentation
4. Create scrapers as last resort

## Statistics

- Total mocking tools researched: 150+
- High-priority tools needing docs: 62
- Tickets created: TRCKR-2533 to TRCKR-2594
- Research agents used: 5 (parallel haiku agents)
- Categories covered: 5 major, 15+ subcategories
- Documentation already present: 8 tools

## Tool Distribution by Language

- Python: 28+ tools
- JavaScript/TypeScript: 22+ tools
- Java: 18+ tools
- Go: 15+ tools
- .NET: 5 tools
- Multi-language/Docker: 12+ tools

## Top Cross-Platform Tools

- **testcontainers** - Java/Python/Go/JavaScript
- **localstack** - Python/JS/Go/Java
- **Playwright** - Multi-language browser automation
- **Selenium** - Multi-language browser automation
- **MSW** - JavaScript/TypeScript (browser + Node.js)
- **WireMock** - Java (with ports to other languages)

## Research Methodology

Used the following tools for research:
- **perplexity-cli** - Web-searched answers with citations
- **tavily** - AI-powered search and content extraction
- **Multiple haiku agents in parallel** - 5 agents researching different categories simultaneously
- **De-duplication** - Combined results and removed duplicates
- **Documentation gap analysis** - Checked existing llm-code-docs content

---

*This research provides a comprehensive foundation for expanding llm-code-docs coverage of mocking and testing tools across all major programming languages and testing scenarios.*
