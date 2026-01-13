# Testing Tools Decision Guide & Workflow Examples

**Updated:** January 1, 2026

## Quick Decision Tree

### 1. Are you building a web application or Node.js project?

#### Web Application → Unit Testing
```
Do you use Vite?
├─ Yes → Vitest (fastest, native integration)
├─ No, React → Jest (all-in-one, widely adopted)
└─ No, Vue/Svelte/Other → Vitest or Jest
   Assertion: Built-in Jest or Chai
   Coverage: Built-in (Vitest/Jest)
   Report: Allure or built-in
```

#### Node.js Project
```
Need maximum flexibility?
├─ Yes → Mocha + Chai (customizable)
├─ No → Jest (batteries included)
└─ Async-heavy → Mocha (best async support)
   Assertion: Chai (with Mocha) or built-in Jest
   Coverage: Istanbul/NYC or built-in
   Report: Mochawesome or Allure
```

### 2. What about End-to-End Testing?

```
Which browsers do you need to support?
├─ Chrome/Electron only
│  ├─ Local development → Cypress (best DX)
│  └─ CI/CD pipeline → Playwright (faster: 4.5s vs 9.4s)
│
├─ Multiple browsers (Chrome, Firefox, Safari)
│  ├─ Need speed → Playwright (4.5s)
│  ├─ Need DX → Consider Cypress + plugins
│  └─ Enterprise → Selenium (industry standard)
│
└─ Mobile apps
   └─ Appium (iOS/Android native automation)
```

### 3. Code Coverage & Reporting

```
How do you track coverage over time?
├─ Local only → Istanbul/NYC (free, self-hosted)
├─ Cloud tracking wanted → Codecov (AI features) or Coveralls
├─ Enterprise → SonarQube (code quality + coverage)
└─ Need historical reports → Allure (beautiful interactive reports)
```

---

## Detailed Recommendation Paths

### Path A: Modern React Project (Recommended)

**Setup:**
```bash
npm install -D jest @testing-library/react @testing-library/jest-dom
```

**Configuration (jest.config.js):**
```javascript
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  collectCoverageFrom: [
    'src/**/*.{js,jsx}',
    '!src/**/*.d.ts',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```

**Test Example:**
```javascript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';

describe('App Component', () => {
  it('renders welcome message', () => {
    render(<App />);
    expect(screen.getByText(/welcome/i)).toBeInTheDocument();
  });

  it('handles user interaction', async () => {
    const user = userEvent.setup();
    render(<App />);
    await user.click(screen.getByRole('button'));
    expect(screen.getByText(/clicked/i)).toBeInTheDocument();
  });
});
```

**Run Tests:**
```bash
# Development with watch
npm test

# CI with coverage
npm test -- --coverage

# Generate coverage report
npm test -- --coverage && open coverage/lcov-report/index.html
```

**E2E Testing Addition:**
```bash
npm install -D cypress
npx cypress open
```

**Complete Stack:**
- Unit: Jest
- E2E: Cypress
- Coverage: Jest built-in
- Reports: Jest HTML + Cypress Cloud
- Trend Tracking: Optional Codecov

---

### Path B: Vite + Vue/Svelte Project (Modern Alternative)

**Setup:**
```bash
npm install -D vitest @vue/test-utils happy-dom
npm install -D @vitest/browser @vitest/ui
```

**Configuration (vitest.config.js):**
```javascript
import { defineConfig } from 'vitest/config';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'happy-dom',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'dist/'],
    },
  },
});
```

**Test Example:**
```javascript
import { describe, it, expect } from 'vitest';
import { render } from '@vue/test-utils';
import Counter from './Counter.vue';

describe('Counter.vue', () => {
  it('increments count', async () => {
    const wrapper = render(Counter);
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.count).toBe(1);
  });
});
```

**Run Tests:**
```bash
# Watch mode (development)
npm run test:watch

# UI mode (interactive)
npm run test:ui

# Coverage report
npm run test -- --coverage
```

**Advantages over Jest:**
- Much faster (Vitest 4-5x faster)
- Native ESM support
- Better TypeScript integration
- Browser Mode for real browser testing

---

### Path C: Node.js API with Mocha + Chai (Enterprise)

**Setup:**
```bash
npm install -D mocha chai @types/node
npm install -D nyc # for coverage
npm install -D chai-http # for API testing
```

**Configuration (.mocharc.json):**
```json
{
  "require": ["@babel/register"],
  "spec": ["test/**/*.test.js"],
  "timeout": 5000,
  "exit": true
}
```

**Test Example:**
```javascript
const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../src/app');

chai.use(chaiHttp);
const { expect } = chai;

describe('User API', () => {
  it('should get users', (done) => {
    chai
      .request(app)
      .get('/api/users')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.be.an('array');
        done();
      });
  });

  it('should create user', (done) => {
    chai
      .request(app)
      .post('/api/users')
      .send({ name: 'John', email: 'john@example.com' })
      .end((err, res) => {
        expect(res).to.have.status(201);
        expect(res.body).to.have.property('id');
        done();
      });
  });
});
```

**Run Tests:**
```bash
# Basic run
npm test

# With coverage
npx nyc mocha

# With specific reporter
npx mocha --reporter spec

# With Allure reports
npm install -D mocha-allure-reporter
npx mocha --reporter mocha-allure-reporter
```

**Coverage Configuration (.nycrc.json):**
```json
{
  "all": true,
  "include": ["src/**/*.js"],
  "exclude": ["src/**/*.test.js", "src/**/*.spec.js"],
  "reporter": ["html", "text", "json"],
  "check-coverage": true,
  "lines": 80,
  "functions": 80,
  "branches": 75
}
```

---

### Path D: Full-Stack with Professional Reporting

**Setup:**
```bash
npm install -D jest @testing-library/react
npm install -D cypress
npm install -D @applitools/eyes-cypress # visual regression
npm install -D allure-commandline # for reports
```

**Package.json Scripts:**
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:e2e": "cypress open",
    "test:e2e:ci": "cypress run",
    "report:allure": "allure generate allure-results -o allure-report && open allure-report/index.html"
  }
}
```

**CI/CD Integration (GitHub Actions):**
```yaml
name: Tests

on: [push, pull_request]

jobs:
  unit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run test:coverage
      - uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json

  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: cypress-io/github-action@v5
        with:
          build: npm run build
          start: npm start
      - uses: actions/upload-artifact@v3
        if: failure()
        with:
          name: cypress-videos
          path: cypress/videos
```

---

## Tool Selection Flowchart

```
START: New Testing Setup
│
├─ What framework/ecosystem?
│  ├─ React → Use Jest
│  ├─ Vue/Svelte → Use Vitest
│  ├─ Node.js API → Use Mocha + Chai or Jest
│  └─ Bare JavaScript → Use Mocha
│
├─ Need E2E tests?
│  ├─ Yes, Chrome only → Cypress
│  ├─ Yes, multi-browser → Playwright
│  └─ Yes, enterprise → Selenium
│
├─ Coverage tracking?
│  ├─ Local only → Istanbul/NYC
│  ├─ GitHub project → Codecov
│  └─ Enterprise → SonarQube or Codecov
│
├─ Need beautiful reports?
│  ├─ Yes → Allure Report
│  ├─ Mocha only → Mochawesome
│  └─ No → Built-in reporters
│
└─ Set up CI/CD → GitHub Actions / GitLab CI / etc.
```

---

## Performance Comparison

### Test Execution Speed (Sample 100-test suite)

```
Framework          Speed      Parallelization    Notes
─────────────────────────────────────────────────────
Vitest            ~2s        Yes (native)        Fastest
Jest              ~5s        Yes                 Good
Mocha             ~6s        Yes (with plugin)   Depends on setup
Karma             ~15s       Limited             Slowest
Cypress (E2E)     ~9.4s      Limited             Browser overhead
Playwright (E2E)  ~4.5s      Yes (native)        Fastest E2E
Selenium (E2E)    ~4.6s      Limited             Protocol overhead
```

### Memory Usage

```
Framework    Memory    Notes
─────────────────────────────
Vitest      ~200MB    Lightweight
Jest        ~400MB    More overhead
Mocha       ~300MB    Depends on plugins
Cypress     ~500MB    Browser instance
Playwright  ~400MB    Per worker process
```

---

## Common Workflows

### Workflow 1: Quick Project Setup (5 minutes)

```bash
# React with Jest (recommended for speed)
npx create-react-app my-app
cd my-app
# Jest is pre-configured!
npm test

# Add E2E testing
npm install -D cypress
npx cypress open
```

### Workflow 2: Migrate Jest to Vitest (15 minutes)

```bash
# Install Vitest
npm install -D vitest @vitest/ui

# Create vitest.config.ts
cat > vitest.config.ts << 'EOF'
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
  },
})
EOF

# Update package.json
# Change "jest" → "vitest" in test scripts

# Run tests
npm test

# UI mode (interactive)
npm test -- --ui
```

### Workflow 3: Add Code Coverage Tracking

```bash
# Local coverage with threshold
npm test -- --coverage

# Upload to Codecov
npm install -D codecov
npx codecov

# Or Coveralls
npm install -D coveralls
npm test -- --coverage && npx coveralls < coverage/lcov.info
```

### Workflow 4: Professional Reporting with Allure

```bash
# Install
npm install -D mocha mocha-allure-reporter
npm install -D allure-commandline

# Configure in package.json
"test": "mocha --reporter mocha-allure-reporter",
"report": "allure generate allure-results -o allure-report && open allure-report/index.html"

# Run
npm test
npm run report
```

### Workflow 5: Full Test Suite with CI/CD

```bash
# Local
npm test              # Unit tests
npm run test:e2e:ci  # E2E tests
npm run coverage     # Coverage report

# Deployed to GitHub Actions (see CI/CD template above)
# Automatically runs on push/PR
# Uploads coverage to Codecov
# Comments on PR with results
```

---

## Troubleshooting Common Issues

### Issue: Tests are too slow
**Solutions:**
1. Switch to Vitest (if not already using it)
2. Enable parallel execution: `jest --maxWorkers=4`
3. Use test sharding in CI
4. Profile with `node --prof` to find bottlenecks

### Issue: Coverage thresholds not enforcing
**Solutions:**
```bash
# Jest: Ensure collectCoverage is true
jest --coverage

# NYC: Add to .nycrc.json
"check-coverage": true,
"lines": 80

# Verify thresholds
npm test -- --coverage && npm run coverage:check
```

### Issue: E2E tests flaky in CI
**Solutions:**
1. Increase timeouts for CI: `CYPRESS_DEFAULT_COMMAND_TIMEOUT=10000`
2. Disable parallel execution in CI
3. Use Playwright (more stable than Cypress)
4. Record videos to debug: `cypress run --record`

### Issue: Can't migrate from Karma
**Solutions:**
1. Switch to Vitest Browser Mode (similar to Karma)
2. Migrate incrementally: Run both during transition
3. Use Vitest's Jest API compatibility
4. Check Vitest migration guide for your framework

---

## Best Practices

### 1. Test Organization
```javascript
// Good: Organized by feature
describe('User Authentication', () => {
  describe('Login', () => {
    it('should log in with valid credentials');
    it('should reject invalid credentials');
  });

  describe('Logout', () => {
    it('should clear user session');
    it('should redirect to home');
  });
});

// Avoid: Disorganized
describe('User', () => {
  it('login');
  it('logout');
  it('signup');
  it('delete');
  // ...many more
});
```

### 2. Test Independence
```javascript
// Good: Each test is independent
describe('Counter', () => {
  let counter;

  beforeEach(() => {
    counter = new Counter();
  });

  it('starts at 0', () => {
    expect(counter.value).toBe(0);
  });

  it('increments', () => {
    counter.increment();
    expect(counter.value).toBe(1);
  });
});

// Avoid: Tests depending on execution order
let counter = new Counter();
it('starts at 0', () => expect(counter.value).toBe(0));
it('increments', () => {
  counter.increment();
  expect(counter.value).toBe(1); // Depends on previous test
});
```

### 3. Coverage Meaningfulness
```javascript
// Good: Test behavior, not just coverage
it('should validate email format', () => {
  expect(validateEmail('invalid')).toBe(false);
  expect(validateEmail('valid@example.com')).toBe(true);
});

// Avoid: Meaningless coverage
it('should call function', () => {
  expect(typeof validateEmail).toBe('function'); // Not testing behavior
});
```

### 4. CI/CD Integration
```yaml
# Good: Multiple stages with clear purposes
test:unit:
  script: npm test -- --coverage
  coverage: '/Coverage: \d+\.\d+/'

test:e2e:
  script: npm run test:e2e:ci
  artifacts:
    paths: [cypress/videos]
    when: on_failure

coverage:
  script: npm run coverage:check
  allow_failure: false  # Enforce thresholds
```

---

## Summary Table

| Scenario | Test Runner | Assertion | Coverage | Reports | E2E | Status |
|----------|------------|-----------|----------|---------|-----|--------|
| React Quick Start | Jest | Built-in | Built-in | Built-in | Cypress | Use |
| Vite Modern | Vitest | Chai | Built-in | Allure | Playwright | Recommended |
| Node.js API | Mocha | Chai | Istanbul | Allure | N/A | Use |
| Enterprise | Jest | Built-in | Codecov | Allure | Selenium | Use |
| Performance | Vitest | Built-in | Built-in | Built-in | Playwright | New Standard |
| Legacy Browser | Karma | Chai | Istanbul | Karma reporter | Selenium | Deprecating |

---

## Resources

- **Jest Documentation:** https://jestjs.io/docs/getting-started
- **Vitest Migration:** https://vitest.dev/guide/migration.html
- **Mocha Best Practices:** https://mochajs.org/#run-cycle-overview
- **Cypress Docs:** https://docs.cypress.io/
- **Playwright Best Practices:** https://playwright.dev/docs/best-practices
- **Coverage Guide:** https://istanbul.js.org/
- **Allure Documentation:** https://docs.qameta.io/allure/

