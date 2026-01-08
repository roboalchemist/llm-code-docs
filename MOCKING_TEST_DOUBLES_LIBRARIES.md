# Mocking Libraries and Test Doubles Frameworks - 2025

Comprehensive reference of popular mocking libraries and test doubles frameworks across major programming languages.

## Python

### Core Mocking Libraries

- **pytest-mock** - Wraps unittest.mock to provide seamless integration with pytest fixtures for effortless mock creation in pytest-based test suites.
- **unittest.mock** - Python's built-in standard library module since 3.3 providing patching, MagicMock, and spy capabilities for unit and integration testing.
- **Pytest (with plugins)** - Core testing framework with extensible fixture system for creating test doubles, enhanced via pytest-mock plugin for advanced mocking.
- **Nose2** - Plugin-based extension of unittest providing flexible mocking support and modern Python 3 compatibility for legacy test suite upgrades.
- **Testify** - Provides test doubles alongside discovery and reporting features, offering alternative to pytest/unittest for test structure.
- **Hypothesis** - Property-based testing library that generates test data and scenarios complementing traditional mocks for comprehensive test coverage.

## JavaScript & TypeScript

### Comprehensive Testing Frameworks

- **Jest** - Full-featured testing framework with zero-configuration setup, built-in mocking, module mocking, and parallel test execution across React, Vue, Angular, and Node.js.
- **ts-mockito** - TypeScript-specific mocking library providing compile-time type checking and type-safe mocks for full TypeScript integration.

### Specialized Mocking Libraries

- **Sinon.JS** - Standalone library for spying, stubbing, and mocking JavaScript functions with fine-grained control and fake timer support for Node.js unit testing.
- **Nock** - HTTP request interceptor for Node.js that mocks HTTP requests without a real backend using URL, query parameter, and header matching.
- **Axios Mock Adapter** - Purpose-built HTTP mocking library for projects using Axios HTTP client with static and dynamic response definition.
- **MirageJS** - In-memory API simulation framework creating realistic backend behavior for frontend development and testing of React, Vue, and Ember applications.

## Java

### Primary Mocking Frameworks

- **Mockito** - Most widely recommended Java mocking framework with intuitive API, annotation-based mocks (@Mock, @InjectMocks), and seamless JUnit/TestNG integration for behavior verification.
- **JMockit** - Advanced mocking tool supporting bytecode manipulation to mock static methods, final classes, constructors, and private methods for legacy code testing.
- **PowerMock** - Extension of Mockito and EasyMock enabling mocking of hard-to-test elements like private methods, final classes, and static methods in untestable code.
- **EasyMock** - Dynamic mock generation framework focused on TDD and BDD patterns with simple setup for interface-heavy applications and isolated testing.
- **Spock** - Groovy-based testing framework with built-in mocking and stubbing, data-driven testing, and readable BDD syntax reducing external library dependencies.

## Go

### Code Generation-Based Mocking

- **gomock (Uber fork)** - Industry-standard Go mocking tool maintained by Uber providing code-generated mocks, order-based expectations, and mature API for interface mocking.
- **mockery (testify + mockery)** - Code generation tool integrated with testify assertions supporting Go generics (v3) for widely-used assertion and mocking framework combination.
- **moq** - CLI-based mock generator from Go interfaces providing simple and reliable code-generation approach for creating type-safe test doubles.

### Runtime Mocking

- **mockio** - Runtime mocking library requiring no code generation with superior call introspection and parameter inspection for minimal-setup mock creation.
- **minimock** - Fast runtime mock generation supporting call capturing and parameter inspection without code-generation overhead for maintenance-free mocking.

## C# & .NET

### Primary Mocking Frameworks

- **Moq** - Most popular .NET mocking framework (6.3k GitHub stars) with LINQ-based expression trees, type safety, VS IntelliSense support, and unified setup syntax for interfaces and classes.
- **NSubstitute** - Mocking framework offering the cleanest API syntax without setup boilerplate using argument matching (Arg.Any<T>()) and intuitive method chaining.
- **FakeItEasy** - Intuitive mocking framework providing flexible assertions and any-argument matching with readable syntax for common mocking scenarios.

### Legacy & Specialized Tools

- **Typemock Isolator** - Advanced mocking tool handling edge cases like non-virtual methods, static methods, and constructor mocking for legacy .NET code testing.
- **Rhino Mocks** - Earlier mocking framework for .NET with Record/Replay patterns, now less prominent but still available for legacy projects.

## Test Double Patterns Supported

### Common Across All Languages

- **Mocks** - Objects with predefined behavior and expected method calls, used for verifying interactions and behavior in unit tests.
- **Stubs** - Simplified replacements providing canned responses without recording interactions, reducing test complexity.
- **Spies** - Wrappers around real objects capturing calls while maintaining original behavior for partial mocking and call verification.
- **Fakes** - Lightweight working implementations replacing external dependencies for faster testing without external system integration.

## Selection Guide by Language

### Python
Start with **pytest-mock** for pytest users; use **unittest.mock** for standard library projects. Consider **Hypothesis** for advanced property-based testing scenarios.

### JavaScript/TypeScript
Choose **Jest** for React/Vue/Angular projects with zero configuration; **Sinon.JS** for fine-grained control; **ts-mockito** for TypeScript type safety; **Nock** or **Axios Mock Adapter** for HTTP mocking; **MirageJS** for frontend development without real backend.

### Java
Start with **Mockito** for new code due to simplicity and community support; use **JMockit** or **PowerMock** for legacy code with statics/finals; consider **Spock** for BDD-style testing on JVM.

### Go
Choose **mockery + testify** for code generation with modern generics support; **gomock (Uber fork)** for mature, order-based expectations; **mockio** for runtime mocking without generation overhead.

### C# & .NET
Default to **Moq** for power and community adoption; choose **NSubstitute** for cleaner, more readable syntax; **FakeItEasy** as third option; **Typemock Isolator** for non-virtual and static method mocking.

---

Research compiled from: Jetbrains, BrowserStack, LambdaTest, GeeksForGeeks, TestGrid, and community surveys (2025)
