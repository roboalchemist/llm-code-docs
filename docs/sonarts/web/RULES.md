# SonarTS Rules and Detection Capabilities

## Source
https://github.com/SonarSource/SonarTS

## Rule Categories

SonarTS implemented comprehensive rules for TypeScript code quality and security analysis across multiple categories.

### Code Smells

Code smells represent maintainability issues that don't necessarily indicate bugs but suggest design problems:

#### Cognitive Complexity
- **Rule**: Cognitive Complexity
- **Purpose**: Detects overly complex functions that are hard to understand and maintain
- **Example**: Deeply nested conditionals and loops

#### Duplicated Code
- **Rule**: `no-all-duplicated-branches`
- **Purpose**: Identifies when all branches of a conditional do the same thing
- **Impact**: Suggests code can be simplified
- **Example**:
  ```typescript
  if (condition) {
    doSomething();
  } else {
    doSomething();  // Same as above
  }
  ```

#### Dead Code
- **Rule**: Dead Code Detection
- **Purpose**: Finds code that can never be executed
- **Example**:
  ```typescript
  function test() {
    return 42;
    console.log("Never executed");  // Dead code
  }
  ```

#### Unused Variables
- **Rule**: Unused Variable Detection
- **Purpose**: Identifies declared variables that are never read
- **Example**:
  ```typescript
  const unused = calculateValue();  // Never referenced
  ```

### Bugs

Bug-prone patterns that are likely to cause incorrect behavior:

#### Identical Expressions
- **Rule**: `no-identical-expressions`
- **Purpose**: Detects logically identical expressions that might indicate a copy-paste error
- **Example**:
  ```typescript
  if (a > b && a > b) {  // Redundant condition
    // ...
  }
  ```

#### Dead Stores
- **Rule**: Dead Store Detection
- **Purpose**: Variables assigned but the value is never used before being overwritten
- **Example**:
  ```typescript
  let x = 5;      // Dead store
  x = 10;         // Value reassigned before use
  console.log(x); // Only final value is read
  ```

#### Logic Errors
- Variables used in wrong conditions
- Incorrect array indexing
- Off-by-one errors in loops

### Vulnerabilities

Security-related issues detected through data-flow analysis:

#### OWASP Top 10 Coverage
- SQL Injection patterns
- Cross-Site Scripting (XSS) vectors
- Path Traversal vulnerabilities
- Sensitive data exposure

#### Examples

**SQL Injection Detection**:
```typescript
const userId = getUserInput();
const query = `SELECT * FROM users WHERE id = ${userId}`;
// Tainted data flows into SQL query
db.execute(query);
```

**XSS Vulnerability**:
```typescript
const userInput = getQueryParameter('name');
document.body.innerHTML = userInput;  // Potential XSS
```

**Weak Cryptography**:
```typescript
import crypto from 'crypto';
const hash = crypto.createHash('md5');  // Deprecated algorithm
```

### Design Issues

Architectural and design pattern violations:

#### Function Parameters
- Functions with too many parameters
- Mixed parameter types
- Unclear parameter purpose

#### Class Structure
- Classes with too many methods
- Circular dependencies
- Tight coupling

## Analysis Techniques

### Abstract Syntax Tree (AST) Analysis

SonarTS uses AST-based analysis to understand code structure:

```typescript
// Rule: All if-else branches do the same thing
if (isAdmin) {
  sendEmail(user);
  logAction();
} else {
  sendEmail(user);
  logAction();
}
// Better:
sendEmail(user);
logAction();
```

### Live Variable Analysis

Determines which variables are "live" (their values are used) at each point:

```typescript
function process() {
  let temp = getValue();      // Live: value will be used
  let unused = getOther();    // Dead: never read after assignment
  unused = 0;                 // Dead store
  console.log(temp);
}
```

### Symbolic Execution

Traces data flow through the program to detect security issues:

```typescript
// Data-flow analysis example
const input = request.query.id;        // Source: untrusted input
const query = buildQuery(input);       // Flows through function
database.execute(query);               // Sink: dangerous operation
```

### Control Flow Analysis

Analyzes program paths to detect unreachable code:

```typescript
function example() {
  if (true) {
    return;
  }
  console.log("Unreachable");  // Detected as unreachable
}
```

## Configuration of Rules

### Rule Properties

Each rule in SonarTS has:
- **Key**: Unique identifier (e.g., `no-identical-expressions`)
- **Name**: Human-readable rule name
- **Severity**: INFO, MINOR, MAJOR, CRITICAL, BLOCKER
- **Type**: CODE_SMELL, BUG, VULNERABILITY
- **Tags**: Category labels (e.g., `pitfall`, `security`, `performance`)

### Severity Levels

| Severity | Use Case |
|----------|----------|
| INFO | Minor style or documentation issues |
| MINOR | Minor code quality issues |
| MAJOR | Significant quality issues that could affect functionality |
| CRITICAL | Critical bugs or security vulnerabilities |
| BLOCKER | Issues that must be fixed immediately |

## Rule Examples by Type

### Bug Rules

1. **Identical Conditions**
   - Condition appears in both if and else branches
   - Severity: MAJOR
   - Type: BUG

2. **Collection Size vs Empty Check**
   - Using `.length` instead of `.isEmpty()`
   - Severity: MINOR
   - Type: CODE_SMELL

3. **Infinite Loops**
   - Loop condition never changes
   - Severity: MAJOR
   - Type: BUG

### Vulnerability Rules

1. **Tainted Data Flow**
   - Unsanitized user input flows to dangerous operations
   - Severity: CRITICAL
   - Type: VULNERABILITY

2. **Insecure Randomness**
   - Using `Math.random()` for security purposes
   - Severity: CRITICAL
   - Type: VULNERABILITY

3. **Weak Encryption**
   - Using deprecated or weak cryptographic algorithms
   - Severity: CRITICAL
   - Type: VULNERABILITY

### Code Smell Rules

1. **Cognitive Complexity**
   - Function is too complex to understand
   - Severity: MAJOR
   - Type: CODE_SMELL

2. **Duplicate Literals**
   - Magic numbers or strings repeated multiple times
   - Severity: MINOR
   - Type: CODE_SMELL

3. **Long Parameter Lists**
   - Function has too many parameters
   - Severity: MINOR
   - Type: CODE_SMELL

## Modern Equivalents

For current TypeScript projects, use:

### SonarQube/SonarCloud JavaScript/TypeScript Analyzer
Provides enhanced versions of these rules with:
- More sophisticated data-flow analysis
- Additional security rules
- Support for modern JavaScript/TypeScript features
- AI-powered fix suggestions
- Better IDE integration

### ESLint
Community-driven JavaScript/TypeScript linting:
- Faster feedback (runs locally)
- Community plugins
- Easier customization
- Pre-commit integration

### SonarJS ESLint Plugin
`eslint-plugin-sonarjs` provides SonarJS rules for ESLint users:
```javascript
// .eslintrc.json
{
  "plugins": ["sonarjs"],
  "extends": ["plugin:sonarjs/recommended"]
}
```

## Summary

SonarTS provided comprehensive analysis across bugs, vulnerabilities, and code smells. Modern solutions offer:

- **SonarQube/SonarCloud**: Production-grade analysis with ongoing updates
- **ESLint with sonarjs plugin**: Lightweight, community-driven approach
- **SonarLint**: Real-time IDE feedback during development

For legacy SonarTS installations, migrate to modern solutions for continued support and enhanced capabilities.
