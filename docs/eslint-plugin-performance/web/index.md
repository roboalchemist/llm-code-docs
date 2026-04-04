# ESLint Plugin Performance

## Overview

**eslint-plugin-performance** is an ESLint plugin designed to detect and prevent performance anti-patterns in JavaScript code.

- **Package**: eslint-plugin-performance
- **Current Version**: 0.1.1
- **Latest Update**: 2023-03-26
- **Repository**: https://github.com/yperformance/eslint-plugin-performance (archived)
- **NPM Package**: https://www.npmjs.com/package/eslint-plugin-performance
- **Maintainer**: yperf (info@yperf.com)

## Installation

Install eslint-plugin-performance using npm or yarn:

```bash
npm install --save-dev eslint-plugin-performance
```

Or with yarn:

```bash
yarn add --dev eslint-plugin-performance
```

## Configuration

Add the plugin to your ESLint configuration file (`.eslintrc.js`, `.eslintrc.json`, or `eslintrc.yml`):

### .eslintrc.json

```json
{
  "plugins": ["performance"],
  "rules": {
    // Add performance rules here
  }
}
```

### .eslintrc.js

```javascript
module.exports = {
  plugins: ["performance"],
  rules: {
    // Add performance rules here
  }
};
```

### ESLint Configuration (ESLint 9+)

```javascript
const performancePlugin = require('eslint-plugin-performance');

module.exports = [
  {
    plugins: {
      performance: performancePlugin
    },
    rules: {
      // Add performance rules here
    }
  }
];
```

## Features

The eslint-plugin-performance plugin is designed to help developers:

- Identify code patterns that may negatively impact application performance
- Detect anti-patterns commonly associated with performance issues
- Enforce best practices for writing efficient JavaScript code
- Maintain consistent performance-conscious coding standards across teams

## Usage

Once installed and configured, ESLint will automatically check your code against the performance rules defined in the plugin:

```bash
eslint . --ext .js,.jsx,.ts,.tsx
```

## Rule Categories

The plugin provides rules focused on:

- **Code efficiency**: Detecting inefficient patterns
- **Runtime performance**: Identifying operations that may be slow at runtime
- **Memory usage**: Finding patterns that could lead to memory issues
- **DOM operations**: Detecting inefficient DOM manipulation patterns (when applicable)

## Notes

This plugin is a minimal ESLint extension for performance linting. The original GitHub repository (yperformance/eslint-plugin-performance) appears to be archived or no longer maintained.

For similar functionality, consider these alternatives:
- **eslint-plugin-sonarjs**: Detects code smells and potential bugs
- **eslint-plugin-no-floating-promise**: Catches unhandled promise rejections
- **eslint-plugin-unicorn**: Provides comprehensive JavaScript linting rules with performance considerations

## Community and Support

- **NPM Package**: https://www.npmjs.com/package/eslint-plugin-performance
- **Issue Reports**: https://github.com/yperformance/eslint-plugin-performance/issues (archived)

## License

Check the package's LICENSE file or npm page for licensing information.

---

## Source

This documentation was compiled from:
- NPM Registry: https://registry.npmjs.org/eslint-plugin-performance
- Package Information: eslint-plugin-performance@0.1.1
- GitHub Repository: https://github.com/yperformance/eslint-plugin-performance
