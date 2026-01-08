# DeepScan Rules and Analysis

# Source: https://deepscan.io/docs/rules

## Rule Organization

DeepScan organizes analysis rules into two primary categories:

### Error Rules
**"Code which might throw an exception at runtime or cause unintended execution"**

Error rules detect critical issues that could cause runtime failures.

### Code Quality Rules
**"Code which should be more readable, reusable and refactorable"**

Code quality rules focus on maintainability and best practices.

## Error Detection Rules (200+)

Identifies critical issues that could cause runtime failures:

### Null Reference Issues
- **NULL_POINTER**: Null pointer dereference - accessing properties on null/undefined values
- Type-related null check failures
- Missing null guards before property access

### Type and Coercion Issues
- Type mismatches in operations
- Implicit type coercion problems
- Type confusion and incorrect type usage
- Operator type compatibility

### Missing Operations
- Missing return statements in functions
- Missing await statements for promises
- Missing statements in conditionals
- Incomplete operation chains

### Control Flow Issues
- Unreachable code
- Dead code paths
- Impossible conditions
- Never-executed branches

### Regular Expression Issues
- Invalid regex patterns
- Problematic regex usage
- Regex performance issues
- Incorrect regex flags

### Event and Listener Issues
- Event listener registration problems
- Improper event handler setup
- Event cleanup and removal issues
- Memory leak potential from listeners

## Code Quality Rules (80+)

Focuses on maintainability and code organization:

### Dead Code
- Unused variables
- Unused imports
- Unreachable statements
- Dead code branches
- Unused function parameters

### Constant Conditions
- Always-true conditions
- Always-false conditions
- Conditions that are always satisfied
- Logic errors in conditionals

### Code Duplication
- Identical branch implementations
- Repeated logic patterns
- Copy-paste code issues
- Redundant implementations

### Loop Inefficiencies
- Unnecessary iterations
- Inefficient loop patterns
- Loop variable scope issues
- Repeated operations inside loops

### Unnecessary Complexity
- Over-engineered patterns
- Excessive nesting
- Convoluted logic
- Anti-patterns and code smells

## Framework-Specific Rules

### React Rules (50+)

Validates React-specific patterns and best practices:

**Component Lifecycle**
- Lifecycle method usage
- Lifecycle hook ordering
- State initialization patterns

**Hook Rules**
- Hook dependency arrays
- Hook usage in conditionals
- Hook call ordering
- Custom hook patterns

**JSX and Props**
- Prop type validation
- Props usage patterns
- JSX syntax correctness
- Component composition

**State Management**
- State immutability patterns
- State update patterns
- State scope and closure issues

**Unique Capability - Execution Flow Analysis**
DeepScan uniquely tracks execution flow to detect issues like:
- Invalid `this` binding in event handlers
- Missing bind() calls
- Arrow function usage patterns
- Method references in render

### Vue.js Rules (60+)

Covers Vue-specific patterns and conventions:

**Template Syntax**
- Template syntax validation
- Directive usage
- Event handler binding
- Expression evaluation

**Reactive Properties**
- Reactive property declaration
- Property observation patterns
- Data binding issues
- Computed property usage

**Lifecycle Hooks**
- Hook availability in composition
- Hook ordering
- Hook timing issues
- Lifecycle consistency

**Component Features**
- Component registration
- Props definition and usage
- Event emission patterns
- Slot usage and naming

### Node.js Rules

Addresses Node.js-specific patterns:

**Module System**
- `require()` usage patterns
- Module loading order
- Circular dependency detection
- CommonJS vs ESM mixing

**CommonJS Exports**
- Export pattern consistency
- Module.exports usage
- Named exports patterns

**Runtime Issues**
- Environment-specific APIs
- Callback patterns
- Async/await usage
- Error handling in Node.js

## Standards and Compliance

### Common Weakness Enumeration (CWE) Mapping

Rules map to CWE standards to address security vulnerabilities and code quality issues:

#### Critical Security Issues
- **CWE-476**: Null Pointer Dereference
- **CWE-628**: Incorrect Function Arguments
- **CWE-843**: Type Confusion

#### Additional Coverage
- **CWE-561**: Dead Code
- **CWE-571**: Expression Always True
- **CWE-572**: Call to Thread run() Instead of start()
- **CWE-573**: Improper Lock Validation
- And many others related to code quality and security

## Rule Configuration

### Default Behavior
- All rules **enabled by default** for comprehensive analysis
- Default configuration optimized for catching real issues
- Balanced approach to error rates

### Customization
- Rules can be **enabled/disabled per project**
- Custom rule configuration via project settings
- Team-wide rule policies for enterprise
- Flexible severity levels

### Configuration File Support
- Project configuration files for rule management
- Environment-specific configurations
- CI/CD integration with rule sets

## Analysis Execution

### When Analysis Runs
- **Pull Requests**: Automatic analysis on PR creation and updates
- **Commits**: Continuous analysis as commits are pushed
- **On-Demand**: Manual analysis trigger via dashboard or CLI
- **Scheduled**: Regular scheduled analysis for enterprise

### Output and Reporting
- Issue detection with precise location
- Issue severity and impact classification
- Code snippets showing problematic code
- Suggested fixes and improvements
- Historical comparison with previous runs

### Issue Filtering
- Filter by rule type
- Filter by severity level
- Filter by file or component
- Search and navigation features

## Best Practices

### Rule Adoption
1. Start with recommended rule set
2. Review rule results in pull requests
3. Adjust rules based on team needs
4. Document custom rule decisions

### False Positive Management
- Use impact classification to reduce noise
- Suppress specific issues when appropriate
- Review configuration regularly
- Communicate rule changes to team

### Continuous Improvement
- Monitor trend reports over time
- Address high-impact issues first
- Gradually improve code quality metrics
- Use grading system to track progress

---

**Learn More**: Visit [deepscan.io/docs/rules](https://deepscan.io/docs/rules) for detailed rule documentation.
