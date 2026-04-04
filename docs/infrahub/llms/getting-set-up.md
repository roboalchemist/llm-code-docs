# Source: https://docs.infrahub.app/development/frontend/getting-set-up.md

# Getting set up with frontend

Before we start

Make sure [Infrahub Backend](/development/backend.md) is up and running. If not, in your terminal execute:

```
invoke demo.destroy demo.start demo.load-infra-schema demo.load-infra-data
```

Infrahub is built with React. Make sure you're running Node.js 22+ and npm 10+, to verify, run:

```
node --version
npm --version
```

## 1. Install dependencies[​](#1-install-dependencies "Direct link to 1. Install dependencies")

```
cd frontend/app
npm install
```

## 2. Start a local server[​](#2-start-a-local-server "Direct link to 2. Start a local server")

```
npm start
```

You can access your local server at <http://localhost:8080/>. If you are not familiar with Infrahub, follow our [Overview Guide](/overview.md).

## 3. Run all tests[​](#3-run-all-tests "Direct link to 3. Run all tests")

### Unit & integration tests[​](#unit--integration-tests "Direct link to Unit & integration tests")

```
npm run test

# same with coverage
npm run test:coverage
```

### E2E tests[​](#e2e-tests "Direct link to E2E tests")

```
npm run test:e2e
```

All tests should succeed. For more information on testing, read [Running & Writing Tests](/development/frontend/testing-guidelines.md).
