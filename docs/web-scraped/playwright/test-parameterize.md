# Source: https://playwright.dev/docs/test-parameterize

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Parameterize tests]

On this page

<div>

# Parameterize tests

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

You can either parameterize tests on a test level or on a project level.

## Parameterized Tests[​](#parameterized-tests "Direct link to Parameterized Tests") 

example.spec.ts

``` 
[
  ,
  ,
  ,
].forEach(() => `, async () => `);
    await expect(page.getByRole('heading')).toHaveText(expected);
  });
});
```

### Before and after hooks[​](#before-and-after-hooks "Direct link to Before and after hooks") 

Most of the time you should put `beforeEach`, `beforeAll`, `afterEach` and `afterAll` hooks outside of `forEach`, so that hooks are executed just once:

example.spec.ts

``` 
test.beforeEach(async () => );

test.afterEach(async () => );

[
  ,
  ,
  ,
].forEach(() => `, async () => `);
    await expect(page.getByRole('heading')).toHaveText(expected);
  });
});
```

If you want to have hooks for each test, you can put them inside a `describe()` - so they are executed for each iteration / each individual test:

example.spec.ts

``` 
[
  ,
  ,
  ,
].forEach(() => ) => `);
    });
    test(`testing with $`, async () => );
  });
});
```

## Parameterized Projects[​](#parameterized-projects "Direct link to Parameterized Projects") 

Playwright Test supports running multiple test projects at the same time. In the following example, we\'ll run two projects with different options.

We declare the option `person` and set the value in the config. The first project runs with the value `Alice` and the second with the value `Bob`.

-   TypeScript
-   JavaScript

my-test.ts

``` 
import  from '@playwright/test';

export type TestOptions = ;

export const test = base.extend<TestOptions>(],
});
```

my-test.js

``` 
const base = require('@playwright/test');

exports.test = base.test.extend(],
});
```

We can use this option in the test, similarly to [fixtures](/docs/test-fixtures).

example.spec.ts

``` 
import  from './my-test';

test('test 1', async () => );
```

Now, we can run tests in multiple configurations by using projects.

-   TypeScript
-   JavaScript

playwright.config.ts

``` 
import  from '@playwright/test';
import type  from './my-test';

export default defineConfig<TestOptions>(,
    },
    ,
    },
  ]
});
```

playwright.config.ts

``` 
// @ts-check

module.exports = defineConfig(,
    },
    ,
    },
  ]
});
```

We can also use the option in a fixture. Learn more about [fixtures](/docs/test-fixtures).

-   TypeScript
-   JavaScript

my-test.ts

``` 
import  from '@playwright/test';

export type TestOptions = ;

export const test = base.extend<TestOptions>(],

  // Override default "page" fixture.
  page: async (, use) => ,
});
```

my-test.js

``` 
const base = require('@playwright/test');

exports.test = base.test.extend(],

  // Override default "page" fixture.
  page: async (, use) => ,
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Parameterized projects behavior has changed in version 1.18. [Learn more](/docs/release-notes#breaking-change-custom-config-options).

## Passing Environment Variables[​](#passing-environment-variables "Direct link to Passing Environment Variables") 

You can use environment variables to configure tests from the command line.

For example, consider the following test file that needs a username and a password. It is usually a good idea not to store your secrets in the source code, so we\'ll need a way to pass secrets from outside.

example.spec.ts

``` 
test(`example test`, async () => );
```

You can run this test with your secret username and password set in the command line.

-   Bash
-   PowerShell
-   Batch

``` 
USER_NAME=me PASSWORD=secret npx playwright test
```

``` 
$env:USER_NAME=me
$env:PASSWORD=secret
npx playwright test
```

``` 
set USER_NAME=me
set PASSWORD=secret
npx playwright test
```

Similarly, configuration file can also read environment variables passed through the command line.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(
});
```

Now, you can run tests against a staging or a production environment:

-   Bash
-   PowerShell
-   Batch

``` 
STAGING=1 npx playwright test
```

``` 
$env:STAGING=1
npx playwright test
```

``` 
set STAGING=1
npx playwright test
```

### .env files[​](#env-files "Direct link to .env files") 

To make environment variables easier to manage, consider something like `.env` files. Here is an example that uses [`dotenv`](https://www.npmjs.com/package/dotenv) package to read environment variables directly in the configuration file.

playwright.config.ts

``` 
import  from '@playwright/test';
import dotenv from 'dotenv';
import path from 'path';

// Read from ".env" file.
dotenv.config();

// Alternatively, read from "../my.env" file.
dotenv.config();

export default defineConfig(
});
```

Now, you can just edit `.env` file to set any variables you\'d like.

``` 
# .env file
STAGING=0
USER_NAME=me
PASSWORD=secret
```

Run tests as usual, your environment variables should be picked up.

``` 
npx playwright test
```

## Create tests via a CSV file[​](#create-tests-via-a-csv-file "Direct link to Create tests via a CSV file") 

The Playwright test-runner runs in Node.js, this means you can directly read files from the file system and parse them with your preferred CSV library.

See for example this CSV file, in our example `input.csv`:

``` 
"test_case","some_value","some_other_value"
"value 1","value 11","foobar1"
"value 2","value 22","foobar21"
"value 3","value 33","foobar321"
"value 4","value 44","foobar4321"
```

Based on this we\'ll generate some tests by using the [csv-parse](https://www.npmjs.com/package/csv-parse) library from NPM:

test.spec.ts

``` 
import fs from 'fs';
import path from 'path';
import  from '@playwright/test';
import  from 'csv-parse/sync';

const records = parse(fs.readFileSync(path.join(__dirname, 'input.csv')), );

for (const record of records) `, async () => );
}
```