# DeepScan Features & Capabilities

# Source: https://deepscan.io/features

## Core Features

### Static Code Analysis with Data-Flow
DeepScan performs static code analysis that goes beyond ESLint by including data-flow analysis capabilities. This allows inspection of JavaScript code at a semantic level to detect potential errors without executing the code.

### Technology Support
The platform supports modern JavaScript development including:
- Latest ECMAScript specifications
- TypeScript
- React and Vue.js frameworks
- Astro framework
- Node.js environments

### Team Collaboration Dashboard
Users can configure teams and add GitHub repositories for continuous analysis. The system provides "an overall picture of your team regarding its quality status, code issues and lines of code" as commits are pushed.

**Dashboard Capabilities:**
- View team-wide quality metrics
- Track code issues across projects
- Monitor lines of code statistics
- See quality trends over time
- Manage team members and permissions

### Issue Tracking Over Time
The system automatically merges issues despite code changes, allowing teams to:
- Observe when problems were first detected
- View fixed issues with corresponding code snippets from that period
- Track issue resolution across refactoring
- Build historical records of code quality

### Project Grading System
DeepScan assigns simple grades ("Poor", "Normal", "Good") based on detected issues and their project impact. This grading mechanism aims to motivate code quality maintenance by providing:
- Simple, understandable quality metrics
- Clear visibility into project health
- Motivation for continuous improvement
- Historical grade trends

## Integration Capabilities

### Native GitHub Integration
- Automatic repository synchronization
- Pull request code review with inline comments
- Continuous monitoring as new commits are pushed
- Support for private and team projects

### Editor Support
- **Visual Studio Code** extension for inline analysis
- **IntelliJ** IDE integration for IDE-native analysis

### CI/CD Integration
- **SonarQube** server integration for on-premises analysis
- **Command-line interface** for automated testing
- **GitHub Marketplace** integration for billing
- **Jenkins**, **CircleCI**, and other CI/CD platforms

### Enterprise Deployment
- Infrastructure deployment for self-hosted analysis
- Custom configuration options
- Unlimited project support
- Dedicated support

## Analysis Capabilities

### Error Detection (200+ Rules)
Identifies critical issues that could cause runtime failures:
- **Null Pointer Dereference**: Accessing properties on null/undefined values
- **Type Mismatches**: Incorrect type usage and coercion errors
- **Missing Operations**: Missing returns, awaits, or required statements
- **Unreachable Code**: Dead code paths that will never execute
- **Regular Expression Issues**: Invalid or problematic regex patterns
- **Event Listener Problems**: Improper event handler registration

### Code Quality (80+ Rules)
Focuses on maintainability and best practices:
- **Dead Code**: Unused variables and unreachable statements
- **Constant Conditions**: Always-true or always-false conditions
- **Branch Duplication**: Identical logic in different branches
- **Loop Inefficiencies**: Suboptimal loop patterns
- **Unnecessary Complexity**: Over-engineered code patterns

### React-Specific Rules (50+)
Validates React-specific patterns:
- Component lifecycle usage
- Hook rules and dependencies
- JSX prop validation
- State management patterns
- Functional vs class component issues
- **Unique Execution Flow Analysis**: Detects invalid `this` binding in event handlers through execution flow tracking

### Vue.js-Specific Rules (60+)
Covers Vue-specific patterns:
- Template syntax validation
- Reactive property usage
- Lifecycle hook compliance
- Directive usage patterns
- Component composition

### Node.js Rules
Addresses Node.js-specific patterns:
- `require()` usage patterns
- CommonJS exports
- Module system issues
- Environment-specific APIs

## Standards and Compliance

### CWE Mapping
Rules map to **Common Weakness Enumeration (CWE)** standards to address:
- **CWE-476**: Null Pointer Dereference
- **CWE-628**: Incorrect Function Arguments
- **CWE-843**: Type Confusion
- And many others related to security and code quality

### Rule Management
- All rules enabled by default for comprehensive analysis
- Rules can be customized per project configuration
- Flexible enabling/disabling based on team preferences
- Default configuration optimized for catching real issues

## Data Privacy and Security

### Data Handling
- Code analysis performed securely
- Historical data retention based on plan
- Integration with GitHub's security model
- Enterprise options for self-hosted analysis

### Performance

DeepScan provides fast analysis with:
- Real-time PR feedback
- Quick issue resolution (showing fixed code)
- Efficient data-flow analysis
- Scalable infrastructure for large teams

---

**Learn More**: Visit [deepscan.io](https://deepscan.io) for feature details and examples.
