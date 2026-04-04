# Source: https://momentic.ai/docs/steps/javascript.md

# Source: https://momentic.ai/docs/javascript.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript

Momentic tests can run arbitrary JavaScript code to craft complex logic and
achieve dynamic behavior within steps.

### JavaScript step

The [JavaScript](/steps/javascript) steps allows you to execute JavaScript code.
Asynchronous code using `async` and `await` is supported.

The output of the step is set to the final return value. This value must be
[serializable](https://en.wikipedia.org/wiki/Serialization) (e.g. you cannot
return a `class` or a `function`).

### `{{ }}` expressions

<Warning>
  Do not use `{{}}` expressions within JavaScript steps. There is no need to do
  so since any variables and functions can be referenced directly.
</Warning>

String input fields in every step step can contain JavaScript expressions inside
curly brackets. At test runtime, these expressions are evaluated and the
templated value is used instead.

For example, the value of a [Type](/steps/type) step can be set to
`{{ env.USERNAME }}@gmail.com`, which might evaluate to something like
`johndoe@gmail.com`.

You should not include a `return` statement in these expressions.

## Execution context

By default, all code executes in an isolated Node.js sandbox. This ensures that
one test's code cannot access other users' data, modify the test environment, or
consume excessive resources.

You can also execute the code in the current page's JavaScript context by turn
on the **Execute in browser** option. You will have access to globals like
`window`, `document`, and other browser APIs. This is useful for interacting
with the page directly, such as manipulating the DOM or accessing
browser-specific features.

## Globals

<Info>
  These globals are **only available** in the Node.js sandbox environment.
</Info>

In addition to the Node.js built-in libraries, Momentic provides several
third-party packages, special utility functions, and global constants to
accelerate the testing experience.

### Third-party packages

* `axios`: For making HTTP/HTTPS requests. Please see the official
  [documentation](https://axios-http.com/docs/intro) for usage and examples.
* `assert`: For executing assertions based on variables and constants. Please
  see the official [Node.js documentation](https://nodejs.org/api/assert.html)
  for usage and examples.
* `faker`: For generating mock data. Please see the official
  [documentation](https://fakerjs.dev/api/) for usage and examples.
* `moment`: For creating and manipulating `Date` objects. Please see the
  official [documentation](https://momentjs.com/docs/) for usage and examples.
* `createAppAuth`: For authenticating with the GitHub API as a GitHub app.
  Please see the official
  [documentation](https://github.com/octokit/auth-app.js/?tab=readme-ov-file#createappauthoptions-or-new-octokit-auth-)
  for usage and examples.
* `Octokit`: For interacting with the GitHub API. Using this function may incur
  additional runtime. Please see the official
  [documentation](https://github.com/octokit/octokit.js)
* `pg`: For interacting with PostgreSQL databases. Please see the official
  [documentation](https://node-postgres.com/features/connecting) for usage and
  examples.

### Special utility functions

* `setVariable`: For setting a variable in the test context. Read more in
  [Variables](/variables).
* `sms`: For sending and receiving SMS messages. Read more in [SMS](/sms).
* `email`: For sending and receiving email messages. Read more in
  [Email](/email).
* `ai`: For interacting with an LLM to generate text. Read more in
  [Generating text](/generating-text).
* `extractCookiesFromResponse`: For extracting cookies from a
  [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object,
  which is the type returned from `fetch` and `axios` calls. The cookies are
  returned in a format compatible with Playwright as well as the
  [Load auth state](/steps/load-auth-state) step.

  ```javascript  theme={null}
    type CookieSetting = {
      name: string;
      value: string;
      domain: string;
      path: string;
      expires: number;
      httpOnly: boolean;
      secure: boolean;
      sameSite: "Strict" | "Lax" | "None";
    };

    async function extractCookiesFromResponse(
      response: Response,
    ): Promise<CookieSetting[]>;
  ```


Built with [Mintlify](https://mintlify.com).