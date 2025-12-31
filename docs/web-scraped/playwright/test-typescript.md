# Source: https://playwright.dev/docs/test-typescript

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [TypeScript]

On this page

<div>

# TypeScript

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright supports TypeScript out of the box. You just write tests in TypeScript, and Playwright will read them, transform to JavaScript and run.

Note that Playwright does not check the types and will run tests even if there are non-critical TypeScript compilation errors. We recommend you run TypeScript compiler alongside Playwright. For example on GitHub actions:

``` 
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    ...
    - name: Run type checks
      run: npx tsc -p tsconfig.json --noEmit
    - name: Run Playwright tests
      run: npx playwright test
```

For local development, you can run `tsc` in [watch](https://www.typescriptlang.org/docs/handbook/configuring-watch.html) mode like this:

``` 
npx tsc -p tsconfig.json --noEmit -w
```

## tsconfig.json[​](#tsconfigjson "Direct link to tsconfig.json") 

Playwright will pick up `tsconfig.json` for each source file it loads. Note that Playwright **only supports** the following tsconfig options: `allowJs`, `baseUrl`, `paths` and `references`.

We recommend setting up a separate `tsconfig.json` in the tests directory so that you can change some preferences specifically for the tests. Here is an example directory structure.

``` 
src/
    source.ts

tests/
    tsconfig.json  # test-specific tsconfig
    example.spec.ts

tsconfig.json  # generic tsconfig for all typescript sources

playwright.config.ts
```

### tsconfig path mapping[​](#tsconfig-path-mapping "Direct link to tsconfig path mapping") 

Playwright supports [path mapping](https://www.typescriptlang.org/docs/handbook/module-resolution.html#path-mapping) declared in the `tsconfig.json`. Make sure that `baseUrl` is also set.

Here is an example `tsconfig.json` that works with Playwright:

tsconfig.json

``` 

  }
}
```

You can now import using the mapped paths:

example.spec.ts

``` 
import  from '@playwright/test';
import  from '@myhelper/credentials';

test('example', async () => );
```

### tsconfig resolution[​](#tsconfig-resolution "Direct link to tsconfig resolution") 

By default, Playwright will look up a closest tsconfig for each imported file by going up the directory structure and looking for `tsconfig.json` or `jsconfig.json`. This way, you can create a `tests/tsconfig.json` file that will be used only for your tests and Playwright will pick it up automatically.

``` 
# Playwright will choose tsconfig automatically
npx playwright test
```

Alternatively, you can specify a single tsconfig file to use in the command line, and Playwright will use it for all imported files, not only test files.

``` 
# Pass a specific tsconfig
npx playwright test --tsconfig=tsconfig.test.json
```

You can specify a single tsconfig file in the config file, that will be used for loading test files, reporters, etc. However, it will not be used while loading the playwright config itself or any files imported from it.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig();
```

## Manually compile tests with TypeScript[​](#manually-compile-tests-with-typescript "Direct link to Manually compile tests with TypeScript") 

Sometimes, Playwright Test will not be able to transform your TypeScript code correctly, for example when you are using experimental or very recent features of TypeScript, usually configured in `tsconfig.json`.

In this case, you can perform your own TypeScript compilation before sending the tests to Playwright.

First add a `tsconfig.json` file inside the tests directory:

``` 

}
```

In `package.json`, add two scripts:

``` 

}
```

The `pretest` script runs typescript on the tests. `test` will run the tests that have been generated to the `tests-out` directory. The `-c` argument configures the test runner to look for tests inside the `tests-out` directory.

Then `npm run test` will build the tests and run them.