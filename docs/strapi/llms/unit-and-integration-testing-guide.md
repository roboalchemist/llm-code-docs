# Unit and integration testing guide

The present guide provides a hands-on approach to configuring 

    </Tabs>

    * `Jest` provides the test runner and assertion utilities.
    * `Supertest` allows you to test all the `api` routes as they were instances of  utilities to recreate just the parts of the Strapi object and any request context that your code relies on.

### Controller example

Create a test file such as `./tests/todo-controller.test.js` that instantiates your controller with a mocked Strapi object and verifies every call the controller performs:

```js title="./tests/todo-controller.test.js"
const todoController = require('./todo-controller');

describe('Todo controller', () => {
  let strapi;

  beforeEach(() => {
    strapi = {
      plugin: jest.fn().mockReturnValue({
        service: jest.fn().mockReturnValue({
          create: jest.fn().mockReturnValue({
            data: {
              name: 'test',
              status: false,
            },
          }),
          complete: jest.fn().mockReturnValue({
            data: {
              id: 1,
              status: true,
            },
          }),
        }),
      }),
    };
  });

  it('creates a todo item', async () => {
    const ctx = {
      request: {
        body: {
          name: 'test',
        },
      },
      body: null,
    };

    await todoController({ strapi }).index(ctx);

    expect(ctx.body).toBe('created');
    expect(strapi.plugin('todo').service('create').create).toHaveBeenCalledTimes(1);
  });

  it('completes a todo item', async () => {
    const ctx = {
      request: {
        body: {
          id: 1,
        },
      },
      body: null,
    };

    await todoController({ strapi }).complete(ctx);

    expect(ctx.body).toBe('todo completed');
    expect(strapi.plugin('todo').service('complete').complete).toHaveBeenCalledTimes(1);
  });
});
```

The `beforeEach` hook rebuilds the mock so every test starts with a clean Strapi instance. Each test prepares the `ctx` request object that the controller expects, calls the controller function, and asserts both the response and the interactions with Strapi services.

### Service example

Services can be tested in the same test suite or in a dedicated file by mocking only the Strapi query layer they call into.

```js title="./tests/create-service.test.js"
const createService = require('./create-service');

describe('Create service', () => {
  let strapi;

  beforeEach(() => {
    strapi = {
      query: jest.fn().mockReturnValue({
        create: jest.fn().mockReturnValue({
          data: {
            name: 'test',
            status: false,
          },
        }),
      }),
    };
  });

  it('persists a todo item', async () => {
    const todo = await createService({ strapi }).create({ name: 'test' });

    expect(strapi.query('plugin::todo.todo').create).toHaveBeenCalledTimes(1);
    expect(todo.data.name).toBe('test');
  });
});
```

By focusing on mocking the specific Strapi APIs your code touches, you can grow these tests to cover additional branches, error cases, and services while keeping them fast and isolated.

## Set up a testing environment

For API-level testing with  that sets up and tears down Strapi instances for tests

### TypeScript compiler configuration

Create `tests/ts-compiler-options.js` with the following content:

```js title="./tests/ts-compiler-options.js"
const fs = require('fs');
const path = require('path');
const ts = require('typescript');

const projectRoot = path.resolve(__dirname, '..');
const tsconfigPath = path.join(projectRoot, 'tsconfig.json');

const baseCompilerOptions = {
  module: ts.ModuleKind.CommonJS,
  target: ts.ScriptTarget.ES2019,
  moduleResolution: ts.ModuleResolutionKind.NodeJs,
  esModuleInterop: true,
  jsx: ts.JsxEmit.React,
};

const loadCompilerOptions = () => {
  let options = { ...baseCompilerOptions };

  if (!fs.existsSync(tsconfigPath)) {
    return options;
  }

  try {
    const tsconfigContent = fs.readFileSync(tsconfigPath, 'utf8');
    const parsed = ts.parseConfigFileTextToJson(tsconfigPath, tsconfigContent);

    if (!parsed.error && parsed.config && parsed.config.compilerOptions) {
      options = {
        ...options,
        ...parsed.config.compilerOptions,
      };
    }
  } catch (error) {
    // Ignore tsconfig parsing errors and fallback to defaults
  }

  return options;
};

module.exports = {
  compilerOptions: loadCompilerOptions(),
  loadCompilerOptions,
};
```

This file loads your project's TypeScript configuration and provides sensible defaults if the config file doesn't exist.

### TypeScript runtime loader

Create `tests/ts-runtime.js` with the following content:

```js title="./tests/ts-runtime.js"
const Module = require('module');
const { compilerOptions } = require('./ts-compiler-options');
const fs = require('fs');
const ts = require('typescript');

const extensions = Module._extensions;

if (!extensions['.ts']) {
  extensions['.ts'] = function compileTS(module, filename) {
    const source = fs.readFileSync(filename, 'utf8');
    const output = ts.transpileModule(source, {
      compilerOptions,
      fileName: filename,
      reportDiagnostics: false,
    });

    return module._compile(output.outputText, filename);
  };
}

if (!extensions['.tsx']) {
  extensions['.tsx'] = extensions['.ts'];
}

module.exports = {
  compilerOptions,
};
```

This file teaches Node.js how to load `.ts` and `.tsx` files by transpiling them to JavaScript on the fly.

### Main test harness

Create `tests/strapi.js` with the following content:

What the test harness does:

1. **TypeScript Support**: Patches Strapi's configuration loader to understand TypeScript files (`.ts`, `.cts`, `.mts`) in your config directory
2. **Configuration Validation**: Ensures only valid config files are loaded and warns about common mistakes (like naming a file `middleware.js` instead of `middlewares.js`)
3. **Database Normalization**: Maps database client names to their actual driver names (e.g., `sqlite` → `sqlite3`) and handles connection pooling
4. **Environment Setup**: Sets all required environment variables for testing, including JWT secrets and database configuration
5. **Automatic Route Registration**: Automatically registers a `/api/hello` test endpoint that you can use in your tests
6. **User Permission Helper**: Patches the user service to automatically assign the "authenticated" role to newly created users, simplifying authentication tests
7. **Cleanup**: Properly closes connections and removes temporary database files after tests complete

:::note
The code example for the `tests/strapi.js` harness highlights lines 313-321 because these are optional, to be used if you [seed predictable test data](#optional-seed-predictable-test-data).
:::

Once these files are in place, the harness handles several Strapi 5 requirements automatically, letting you focus on writing actual test logic rather than configuration boilerplate.

## (optional) Seed predictable test data

Some API tests benefit from having a known set of documents preloaded. You can expose your project seeding as a reusable function and call it from the harness behind an environment flag:

1. Export a seeding function from your project script (e.g. `./scripts/seed.js`):

    ```js title="./scripts/seed.js"
    async function seedExampleApp() {
      // In test environment, skip complex seeding and just log
      if (process.env.NODE_ENV === 'test') {
        console.log('Test seeding: Skipping complex data import (not needed for basic tests)');
        return;
      }

      const shouldImportSeedData = await isFirstRun();
      if (shouldImportSeedData) {
        try {
          console.log('Setting up the template...');
          await importSeedData();
          console.log('Ready to go');
        } catch (error) {
          console.log('Could not import seed data');
          console.error(error);
        }
      }
    }

    // Allow usage both as a CLI and as a library from tests
    if (require.main === module) {
      main().catch((error) => {
        console.error(error);
        process.exit(1);
      });
    }

    module.exports = { seedExampleApp };
    ```

2. In the test harness, call the function when `TEST_SEED=true` (see lines 313-321 highlighted in the code example from the [main test harness](#main-test-harness)).

3. Run your tests with seeding enabled:

    </Tabs>

Seeding runs after Strapi starts, so services, permissions, and uploads are available.

It's recommended to keep seeds deterministic to ensure stable assertions. If you publish entries, prefer fixed timestamps or assert on structural properties rather than transient dates.

## Create smoke tests

With the harness in place you can confirm Strapi boots correctly by adding a minimal Jest suite with the following **smoke tests**  in a `tests/app.test.js` as follows:

```js title="./tests/app.test.js"
const { setupStrapi, cleanupStrapi } = require('./strapi');

/** this code is called once before any test is called */
beforeAll(async () => {
  await setupStrapi(); // Singleton so it can be called many times
});

/** this code is called once before all the tests are finished */
afterAll(async () => {
  await cleanupStrapi();
});

it('strapi is defined', () => {
  expect(strapi).toBeDefined();
});

require('./hello');
require('./user');
```

Running `yarn test` or `npm run test` should now yield:

```bash
PASS tests/create-service.test.js
PASS tests/todo-controller.test.js

Test Suites: 6 passed, 6 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        7.952 s
Ran all test suites.
✨ Done in 8.63s.
```

:::caution
If you receive a timeout error for Jest, increase the timeout by calling `jest.setTimeout(30000)` in `tests/strapi.js` or at the top of your test file.
:::

## Test a basic API endpoint

Create `tests/hello.test.js` with the following:

```js title="./tests/hello.test.js"
const { setupStrapi, cleanupStrapi } = require('./strapi');
const request = require('supertest');

beforeAll(async () => {
  await setupStrapi();
});

afterAll(async () => {
  await cleanupStrapi();
});

it('should return hello world', async () => {
  await request(strapi.server.httpServer)
    .get('/api/hello')
    .expect(200)
    .then((data) => {
      expect(data.text).toBe('Hello World!');
    });
});
```

The harness registers the `/api/hello` route automatically, so the test only has to make the request.

## Test API authentication

Strapi uses a JWT token to handle authentication. We will create one user with a known username and password, and use these credentials to authenticate and get a JWT token. The patched `user.add` helper in the harness ensures the authenticated role is applied automatically.

Create `tests/auth.test.js`:

```js title="./tests/auth.test.js"
const { setupStrapi, cleanupStrapi } = require('./strapi');
const request = require('supertest');

beforeAll(async () => {
  await setupStrapi();
});

afterAll(async () => {
  await cleanupStrapi();
});

// User mock data
const mockUserData = {
  username: 'tester',
  email: 'tester@strapi.com',
  provider: 'local',
  password: '1234abc',
  confirmed: true,
  blocked: null,
};

it('should login user and return JWT token', async () => {
  await strapi.plugins['users-permissions'].services.user.add({
    ...mockUserData,
  });

  await request(strapi.server.httpServer)
    .post('/api/auth/local')
    .set('accept', 'application/json')
    .set('Content-Type', 'application/json')
    .send({
      identifier: mockUserData.email,
      password: mockUserData.password,
    })
    .expect('Content-Type', /json/)
    .expect(200)
    .then((data) => {
      expect(data.body.jwt).toBeDefined();
    });
});
```

You can use the JWT token returned to make authenticated requests to the API. Using this example, you can add more tests to validate that the authentication and authorization are working as expected.

## Advanced API testing with user permissions

When you create API tests, you will most likely need to test endpoints that require authentication. In the following example we will implement a helper to get and use the JWT token.

Create `tests/user.test.js`:

```js title="./tests/user.test.js"
const { setupStrapi, cleanupStrapi } = require('./strapi');
const request = require('supertest');

beforeAll(async () => {
  await setupStrapi();
});

afterAll(async () => {
  await cleanupStrapi();
});

let authenticatedUser = {};

// User mock data
const mockUserData = {
  username: 'tester',
  email: 'tester@strapi.com',
  provider: 'local',
  password: '1234abc',
  confirmed: true,
  blocked: null,
};

describe('User API', () => {
  beforeAll(async () => {
    await strapi.plugins['users-permissions'].services.user.add({
      ...mockUserData,
    });

    const response = await request(strapi.server.httpServer)
      .post('/api/auth/local')
      .set('accept', 'application/json')
      .set('Content-Type', 'application/json')
      .send({
        identifier: mockUserData.email,
        password: mockUserData.password,
      });

    authenticatedUser.jwt = response.body.jwt;
    authenticatedUser.user = response.body.user;
  });

  it('should return users data for authenticated user', async () => {
    await request(strapi.server.httpServer)
      .get('/api/users/me')
      .set('accept', 'application/json')
      .set('Content-Type', 'application/json')
      .set('Authorization', 'Bearer ' + authenticatedUser.jwt)
      .expect('Content-Type', /json/)
      .expect(200)
      .then((data) => {
        expect(data.body).toBeDefined();
        expect(data.body.id).toBe(authenticatedUser.user.id);
        expect(data.body.username).toBe(authenticatedUser.user.username);
        expect(data.body.email).toBe(authenticatedUser.user.email);
      });
  });
});
```

## Automate tests with GitHub Actions

To go further, you can run your Jest test suite automatically on every push and pull request with . Create a `.github/workflows/test.yaml` file in your project and add the workflow as follows:

```yaml title="./.github/workflows/test.yaml"
name: 'Tests'

on:
  pull_request:
  push:

jobs:
  run-tests:
    name: Run Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install modules
        run: npm ci
      - name: Run Tests
        run: npm run test
```

Pairing continuous integration with your unit and API tests helps prevent regressions before they reach production.