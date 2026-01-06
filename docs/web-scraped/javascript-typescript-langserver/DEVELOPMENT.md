# Development Guide

Source: https://github.com/sourcegraph/javascript-typescript-langserver

Guide for developing and contributing to the JavaScript/TypeScript Language Server.

## Development Setup

### Prerequisites

- Node.js >= 6.0.0
- npm (comes with Node.js)
- Git
- A code editor or IDE

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/sourcegraph/javascript-typescript-langserver.git
cd javascript-typescript-langserver

# Install dependencies
npm install

# Verify installation
npm run build
```

## Project Structure

```
javascript-typescript-langserver/
├── src/                      # TypeScript source code
│   ├── language-server.ts   # Main server entry point
│   ├── typescript-service.ts # TypeScript API wrapper
│   ├── lsp/                 # LSP protocol implementation
│   └── test/                # Test files
├── lib/                      # Compiled JavaScript (generated)
├── package.json              # Project metadata and scripts
├── tsconfig.json             # TypeScript configuration
├── tslint.json               # Linting rules
├── README.md                 # Project documentation
└── CONTRIBUTING.md           # Contribution guidelines
```

## Build and Compilation

### Development Build

For a single compilation pass:

```bash
npm run build
```

This compiles TypeScript source files in `src/` to JavaScript in `lib/`.

### Watch Mode

For continuous compilation during development:

```bash
npm run watch
```

The build will automatically recompile whenever source files change. This is the recommended setup for active development.

### Clean Build

Remove compiled files and rebuild from scratch:

```bash
npm run clean
npm run build
```

## Running Tests

### Run All Tests

```bash
npm test
```

This runs all test files matching the pattern `lib/test/**/*.js`.

Test configuration:
- Timeout: 7000ms per test
- Slow threshold: 2000ms (tests slower than this are marked as slow)

### Run Specific Tests

```bash
# Run tests in a specific file
npm test -- lib/test/hover.test.js

# Run tests matching a pattern
npm test -- lib/test/completion*.js
```

### Test Coverage

Generate coverage report:

```bash
npm run cover
```

This creates a coverage report showing what percentage of code is tested.

## Code Quality

### Linting

The project uses TSLint for code quality checks:

```bash
npm run lint
```

This runs both TSLint and Prettier checks.

### TypeScript Linting

```bash
npm run tslint
```

TSLint configuration is in `tslint.json`. Common rules checked:
- No unused variables
- No console statements (should use logging)
- Proper semicolon usage
- Consistent naming conventions

### Code Formatting

The project uses Prettier for consistent code formatting:

```bash
npm run prettier
```

This will:
- Check which files don't match the format
- With `--write` flag (if configured), it can auto-fix formatting

Format configuration:
- 2-space indentation
- Single quotes
- Trailing commas

## Debugging

### Enable Trace Logging

Run the server with the `--trace` flag to see all requests and responses:

```bash
node lib/language-server --trace
```

Output will include:
- All incoming LSP requests
- All outgoing responses
- Diagnostic messages

### File Logging

Log to a file for easier analysis:

```bash
node lib/language-server --logfile debug.log
```

### OpenTracing with Jaeger

For performance profiling:

1. Start Jaeger locally:
```bash
docker run -d -p5775:5775/udp -p6831:6831/udp -p6832:6832/udp \
  -p5778:5778 -p16686:16686 -p14268:14268 jaegertracing/all-in-one:latest
```

2. Run server with Jaeger enabled:
```bash
node lib/language-server --enable-jaeger
```

3. Open http://localhost:16686 to view traces

Jaeger shows:
- Operation spans with timing
- Nested operation hierarchy
- Performance bottlenecks

### Debug Console Output

The server sends JSON-RPC messages to stdout. To analyze requests:

```bash
node lib/language-server 2>debug.log | jq .
```

(Requires `jq` for JSON formatting)

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation
- `test/` for test additions

### 2. Make Your Changes

Edit TypeScript files in the `src/` directory. Watch mode will automatically recompile:

```bash
npm run watch
```

### 3. Test Your Changes

```bash
npm test
npm run lint
```

All tests must pass and code must pass linting before creating a PR.

### 4. Commit with Proper Format

Commit messages should follow this format:

```
<subsystem>: <what changed>

<why this change was made>

Fixes #<issue-number>
```

Example:

```
hover: add support for const assertions

When hovering over a const assertion, display the literal type
rather than the inferred type to match TypeScript behavior.

Fixes #123
```

### 5. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a PR on GitHub with a clear description of your changes.

## Subsystem Guide

Common subsystems for commit messages:

- `hover` - Hover information display
- `definition` - Go to definition implementation
- `completion` - Code completion features
- `diagnostics` - Error and warning reporting
- `rename` - Symbol renaming
- `references` - Find references
- `symbols` - Symbol listing and search
- `lsp` - Core LSP protocol
- `typescript` - TypeScript integration
- `test` - Test additions or fixes
- `docs` - Documentation
- `ci` - Continuous integration
- `build` - Build system changes

## Common Development Tasks

### Adding a New LSP Feature

1. Implement handler in `src/lsp/`
2. Add tests in `src/test/`
3. Update capabilities in server initialization
4. Document in API_REFERENCE.md

Example: Adding `textDocument/implementation`

```typescript
// src/lsp/implementation.ts
export function handleImplementation(
  params: ImplementationParams,
  ts: TypeScriptService
): Location[] | null {
  // Implementation code
}
```

### Adding a Test

```typescript
// src/test/implementation.test.ts
import * as assert from 'assert'
import { createTestServer } from './helper'

describe('Implementation', () => {
  it('should find implementations of interface', async () => {
    const { server, files } = await createTestServer()

    const locations = await server.implementation({
      textDocument: { uri: files.interface },
      position: { line: 0, character: 0 }
    })

    assert.ok(locations)
    assert.equal(locations.length, 1)
  })
})
```

### Updating TypeScript Support

The server includes a bundled TypeScript version in `package.json`. To update:

1. Update the TypeScript version in `package.json`
2. Run `npm install`
3. Run `npm test` to ensure compatibility
4. Commit with message like: `build: update TypeScript to 5.0.0`

## Git Workflow

### Fork and Clone

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/your-username/javascript-typescript-langserver.git
cd javascript-typescript-langserver

# Add upstream remote
git remote add upstream https://github.com/sourcegraph/javascript-typescript-langserver.git
```

### Keep Your Fork Updated

```bash
# Fetch latest changes
git fetch upstream

# Rebase your branch
git rebase upstream/master
```

### Sync Before Submitting PR

```bash
git fetch upstream
git rebase upstream/master
git push origin feature/your-feature-name --force-with-lease
```

## Contributing Guidelines

### Before Starting

1. Check for existing issues/PRs
2. Create an issue for new features (unless it's a bug fix)
3. Discuss major changes in the issue first

### Code Quality Standards

- All tests must pass: `npm test`
- Code must pass linting: `npm run lint`
- Code must be formatted with Prettier: `npm run prettier`
- New features should include tests
- Documentation should be updated

### PR Review Process

1. Automated tests must pass
2. Code review by maintainers
3. Approval and merge

### Commit Message Guidelines

See the format specification in CONTRIBUTING.md:

```
<subsystem>: <what changed>

<why this change was made>

Fixes #<issue>
```

No commits over 70 characters on first line.

## Certificate of Origin

By contributing, you agree to the Developer Certificate of Origin (DCO):

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its
contributors. 1 Letterman Drive Suite D4700, San Francisco, CA,
94129

Everyone is permitted to copy and distribute verbatim copies of
this license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the
    extent I can control it, is subject to the same open source
    license as the previous work, or a lesser license as set out
    in the file (as I should be known).
```

Your commits will be checked for DCO compliance.

## Resources

- **Language Server Protocol Spec**: https://microsoft.github.io/language-server-protocol/
- **TypeScript Handbook**: https://www.typescriptlang.org/docs/
- **TSLint Documentation**: https://palantir.github.io/tslint/
- **Prettier Documentation**: https://prettier.io/docs/
- **GitHub Repository**: https://github.com/sourcegraph/javascript-typescript-langserver

## Troubleshooting

### Tests Timeout

If tests timeout (>7000ms):
- Check for async operations not awaited
- Look for infinite loops or dead code
- Use `--reporter tap` for more verbose output

### Module Resolution Issues

If you see module not found errors:
```bash
npm install
npm run build
```

### Memory Issues During Build

For large builds on low-memory systems:
```bash
node --max-old-space-size=2048 node_modules/.bin/tsc
```

### TypeScript Compilation Errors

Check TypeScript configuration:
```bash
cat tsconfig.json
npm list typescript
```

Update if needed:
```bash
npm update typescript
```
