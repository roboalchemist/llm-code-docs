# Browser Mocking, Network Mocking, and Frontend Test Mocking Tools

## E2E Testing Frameworks with Built-in Network Mocking

### Browser Automation Frameworks

1. **Playwright** - Microsoft's cross-browser automation tool with native request interception, response modification, and network condition simulation (failures, delays, latency) for Chromium, Firefox, and WebKit.

2. **Puppeteer** - Google's Node.js library for headless Chrome/Chromium control with rich Chrome DevTools Protocol access for network interception, request/response manipulation, and low-level browser automation.

3. **Selenium** - Industry-standard open-source framework (20+ years) supporting all major browsers via language bindings with distributed testing via Selenium Grid and network mocking through extensions or proxy-based solutions.

4. **Cypress** - JavaScript-focused E2E framework with built-in network request interception, stubbing, and spying capabilities; excellent for frontend-first testing with visual debugging and time-travel debugging.

5. **WebdriverIO** - WebDriver standard-based automation framework combining Selenium, Appium, and devtools capabilities for cross-browser testing with network stubbing and mocking support.

6. **BrowserStack Automate** - Cloud platform extending Playwright/Puppeteer/Selenium with AI-powered features like self-healing locators, network throttling simulation, and flakiness detection across real devices/browsers.

## Service Worker and API Mocking

### Service Worker-Based Mocking

7. **Mock Service Worker (MSW)** - Service worker-based library intercepting and mocking HTTP requests at the network level in browsers, supporting REST APIs, GraphQL, and WebSockets with realistic request handling in both browser and Node.js environments.

8. **Service Worker Mock** - Minimal library for testing service workers by providing a mock Service Worker environment without requiring a full browser context or network requests.

## HTTP/Network Request Mocking (Node.js & Browser)

### HTTP Server Mocking

9. **Nock** - Node.js library intercepting and mocking HTTP requests with flexible URL/header/parameter matching, predefined responses, and request recording for unit and integration tests.

10. **Mirage JS** - In-memory API mocking library creating simulated backend behavior (models, relationships, pagination, errors, delays) for frontend development and E2E testing in the browser without real API calls.

11. **json-server** - Zero-config fake REST API server using JSON files as database; serves static JSON files with full REST API support for rapid prototyping and frontend development without backend implementation.

12. **http-server** - Simple, zero-configuration static HTTP server serving local files on any port; useful for serving mocked API responses or testing frontend against local files with custom MIME types.

### Network Interception at Protocol Level

13. **Sinon.JS** - Standalone JavaScript library for spying, stubbing, and mocking functions, timers, and XMLHttpRequest; compatible with any testing framework (Jest, Vitest, Mocha) for precise control over function behavior.

14. **Axios Mock Adapter** - Library intercepting Axios HTTP client requests with configurable responses, matching, and request verification for unit/integration testing without network calls.

15. **MSW Standalone** - Service Worker-based mocking that works in both browser and Node.js, intercepting fetch and XHR requests without modifying application code or using spy/stub patterns.

16. **Unfetch Mock** - Lightweight mocking library for the Unfetch HTTP client providing fake fetch/XMLHttpRequest responses for testing with minimal overhead.

## Frontend Module and Component Mocking

### Testing Framework Built-in Mocking

17. **Jest** - Facebook's testing framework with native module mocking via `jest.mock()`, function spying via `jest.fn()`, and timer control; standard for React component testing and module isolation.

18. **Vitest** - Vite-powered test runner with Jest-compatible API, faster execution for modern frontend projects, native module mocking, and strong support for ES modules and single-file components.

19. **Mocha** - Flexible JavaScript test runner (not built-in mocking) often paired with assertion libraries (Chai) and mocking libraries (Sinon) for granular control over test behavior.

20. **Jasmine** - BDD-style testing framework with built-in spy and mock functions via `spyOn()`, mock object creation, and clock manipulation for unit testing without external dependencies.

### React/Vue Component Mocking

21. **React Testing Library** - Testing utility focusing on testing component behavior (not implementation) with mock functions via Jest, element queries, and user interaction simulation; encourages testing user workflows.

22. **Vue Test Utils** - Official Vue component testing library with mocking support for child components, modules, and async operations; pairs with Jest/Vitest for complete component test coverage.

23. **@testing-library/react** - Built on React Testing Library principles, providing utilities for rendering components, mocking dependencies, and querying DOM elements in a user-centric testing approach.

24. **jest.mock()** - Jest built-in function for module-level mocking, replacing entire modules with mock implementations or manual mocks from `__mocks__` directories.

25. **vi.mock()** - Vitest equivalent to `jest.mock()` for module mocking with Vite compatibility and faster execution in modern frontend projects.

### Component Isolation and Visual Testing

26. **Storybook** - UI component development environment with built-in mocking for component props, Redux state, and API calls; supports snapshot testing and visual regression detection without requiring E2E tests.

27. **Chromatic** - Visual regression testing service for Storybook, automatically detecting UI changes across components with Percy-style snapshot comparisons.

28. **Styleguidist** - Living style guide generator with component documentation, examples, and isolated testing via Webpack; includes mock data and isolated component rendering.

## Request/Response Stubbing and Spying

### Spy and Stub Libraries

29. **Sinon Stubs** - Part of Sinon.JS, replacing object/function behavior with controllable stubs for unit testing without external dependencies or network calls.

30. **Jest Spies** - Jest built-in `jest.spyOn()` for spying on object methods, tracking calls, and replacing implementations without full module mocking.

31. **cy.stub()** - Cypress-specific stubbing for functions and methods within tests with automatic cleanup and integration with Cypress command chaining.

32. **cy.intercept()** - Cypress network interception for HTTP/HTTPS requests, responses, and WebSocket messages with matching, modification, and stubbing capabilities.

## Proxy-Based Network Mocking

### Proxy Servers for Mocking

33. **Bright Data Scraping Browser** - Integrates Puppeteer/Playwright/Selenium with proxy and fingerprint mocking for anti-detection; useful for testing with network masking and bot detection evasion.

34. **Fiddler** - Web debugging proxy intercepting HTTP/HTTPS traffic for inspection, modification, and mocking at the system level; works with any browser or automation tool.

35. **Charles Proxy** - HTTP/HTTPS debugging proxy for monitoring, blocking, and modifying network traffic; useful for testing with network throttling and response simulation.

36. **mitmproxy** - Free, open-source interactive HTTPS proxy for traffic inspection and modification; scriptable for automated request/response mocking without tool-specific integrations.

## GraphQL-Specific Mocking

### GraphQL Request Mocking

37. **Apollo MockedProvider** - React component wrapper providing mocked GraphQL responses for Apollo Client testing without network requests; pairs with Jest for component-level GraphQL testing.

38. **GraphQL Mock** - Library for mocking GraphQL servers and resolvers, providing realistic GraphQL responses with custom field values and error simulation.

39. **easygraphql-mock** - GraphQL schema-based mocking generating realistic mock data matching your GraphQL schema types and relationships.

## WebSocket and Real-time Mocking

### Real-time Protocol Mocking

40. **MSW WebSocket Support** - Mock Service Worker includes native WebSocket mocking for testing real-time features without requiring actual WebSocket servers.

41. **Socket.io Mock** - Library for mocking Socket.io connections in tests, simulating real-time events and messages without live socket servers.

42. **WS Mock** - WebSocket library with built-in mocking for testing WebSocket clients without real WebSocket connections.

## Specialized Mocking Solutions

### Database and File System Mocking

43. **Mock Object Pattern** - General pattern for creating mock objects (not a library) that replace real dependencies with test doubles; used in combination with libraries like Sinon or Jest.

44. **Memorydb** - In-memory database implementations (Redis, MongoDB clones) for testing database interactions without spinning up actual database servers.

45. **MSW Database Handlers** - MSW extension pattern for mocking database operations by simulating database queries and responses at the API/handler level.

### Time and Timer Mocking

46. **Jest Fake Timers** - Jest built-in fake timer control with `jest.useFakeTimers()` for testing time-dependent code without actual delays.

47. **Vitest Fake Timers** - Vitest timer mocking with support for both "legacy" and "modern" implementations, faster execution than Jest for timer tests.

48. **Sinon Clock** - Part of Sinon.JS, providing fake timer implementation for testing setTimeout, setInterval, and date-dependent code.

49. **Lolex** - Standalone fake timer library (used by Sinon internally) providing complete JavaScript timer implementation for testing without actual delays.

## Authentication and Session Mocking

### Auth Mocking

50. **Mock Auth0** - Library for mocking Auth0 authentication in tests, simulating login flows and token generation without contacting Auth0 servers.

51. **JWT Mock** - Library for mocking JWT token generation and verification in tests without external authentication services.

52. **Passport Mock** - Testing utility for mocking Passport.js authentication strategies and sessions for backend API testing.

## Summary by Use Case

| Use Case | Recommended Tools |
|----------|-------------------|
| **E2E Browser Testing** | Playwright, Puppeteer, Cypress, Selenium |
| **API Mocking in Browser** | MSW, Mirage JS, MirageJS |
| **API Mocking in Node.js** | Nock, json-server, http-server |
| **HTTP Stubbing/Spying** | Sinon.JS, Axios Mock Adapter |
| **Component Testing** | Jest/Vitest + React Testing Library |
| **Module Mocking** | jest.mock(), vi.mock() (Vitest) |
| **Network Interception** | MSW, Playwright interception, Cypress cy.intercept() |
| **GraphQL Mocking** | Apollo MockedProvider, GraphQL Mock |
| **WebSocket Mocking** | MSW WebSocket, Socket.io Mock |
| **Timer Testing** | Jest Fake Timers, Sinon Clock, Lolex |
| **Proxy-Level Mocking** | mitmproxy, Charles Proxy, Fiddler |
| **Visual Testing** | Storybook, Chromatic |
| **Development Server** | json-server, http-server, webpack-dev-server with mock middleware |

---

**Research Sources:**
- Perplexity AI Research (2026) - E2E testing frameworks, mocking libraries, browser automation tools
- BrowserStack Guide - JavaScript Mocking Libraries and Browser Testing Tools
- LogRocket - React Testing Libraries Comparison
- Zuplo - API Mocking Frameworks
- BetterStack - Node.js Testing Libraries Guide
- Dev.to - Best API Mocking Tools Reviews

