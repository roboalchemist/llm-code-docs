# Source: https://braintrust.dev/docs/guides/self-hosting/advanced.md

# Source: https://braintrust.dev/docs/core/logs/advanced.md

# Advanced logging

> Advanced logging topics

## Log multiple projects

The first logger you initialize in your program becomes the current (default) logger. Any subsequent traced function calls will use
the current logger. If you'd like to log to multiple projects, you will need to create multiple loggers, in which case setting
just one as the current leads to unexpected behavior.

When you initialize a logger, use `setCurrent: false` to set it as the current logger.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger } from "braintrust";

  async function main() {
    const logger = initLogger({
      projectName: "My Project",
      apiKey: process.env.BRAINTRUST_API_KEY,
      setCurrent: false,
    });

    // NOTE: When you `setCurrent` to false, you need to call `traced` on the logger,
    // since the global `traced` function will not pick up this logger. Within this
    // callback, however, calling globally `traced` or `wrapTraced` functions will
    // work as usual.
    await logger.traced(async (span) => {
      // Do some work
      span.log({ output: "Hello, world!" });
    });
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger

  logger = init_logger(
      project="My Project",
      api_key=os.environ["BRAINTRUST_API_KEY"],
      set_current=False,
  )

  # NOTE: When you `set_current` to False, you need to call `start_span` on the logger,
  # since the global `start_span` function will not pick up this logger. Within this context,
  # however, `@traced` decorated functions will work as usual.
  with logger.start_span("my_span") as span:
      # Do some work
      span.log(output="Hello, world!")
  ```
</CodeGroup>

### Cache loggers

When you initialize a logger, it performs some background work to (a) login to Braintrust if you haven't already, and (b)
fetch project metadata. This background work does not block your code; however, if you initialize a logger on each request,
it will slow down logging performance quite a bit. Instead, it's a best practice to cache these loggers and reuse them:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger, Logger } from "braintrust";

  // See docs below for more information on setting the async flush flag to true or false
  const loggers = new Map<string, Logger<true>>();

  function getLogger(projectName: string): Logger<true> {
    if (!loggers.has(projectName)) {
      loggers.set(
        projectName,
        initLogger({
          projectName,
          apiKey: process.env.BRAINTRUST_API_KEY,
          setCurrent: false,
          asyncFlush: true,
        }),
      );
    }
    return loggers.get(projectName)!;
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import Logger, init_logger

  loggers = {}

  def get_logger(project_name: str) -> Logger:
      global loggers
      if project_name not in loggers:
          loggers[project_name] = init_logger(
              project=project_name,
              api_key=os.environ["BRAINTRUST_API_KEY"],
              set_current=False,
          )
      return loggers[project_name]
  ```
</CodeGroup>

### Initialize login

The logger lazily authorizes against Braintrust when it is first used. This information is shared
across loggers, but you may want to explicitly call `login()` once to avoid having to pass in an API key to each logger (or
to use the `BRAINTRUST_API_KEY` environment variable).

<Note>
  There is a lower-level mechanism which can even let you use different API keys for different loggers, but it's not documented
  or officially supported. [Get in touch](mailto:support@braintrust.dev) if you need this.
</Note>

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { login } from "braintrust";

  // Run this function once at the beginning of your application
  async function init() {
    await login({
      apiKey: process.env.BRAINTRUST_API_KEY,
    });
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import login

  # Run this function once at the beginning of your application
  async def init():
      await login(api_key=os.environ["BRAINTRUST_API_KEY"])
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt