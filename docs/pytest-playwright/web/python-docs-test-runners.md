# Source: https://playwright.dev/python/docs/test-runners

Title: Pytest Plugin Reference | Playwright Python

URL Source: https://playwright.dev/python/docs/test-runners

Published Time: Thu, 26 Mar 2026 01:00:24 GMT

Markdown Content:
## Introduction[​](https://playwright.dev/python/docs/test-runners#introduction "Direct link to Introduction")

Playwright provides a [Pytest](https://docs.pytest.org/en/stable/) plugin to write end-to-end tests. To get started with it, refer to the [getting started guide](https://playwright.dev/python/docs/intro).

## Usage[​](https://playwright.dev/python/docs/test-runners#usage "Direct link to Usage")

To run your tests, use [Pytest](https://docs.pytest.org/en/stable/) CLI.

`pytest --browser webkit --headed`

If you want to add the CLI arguments automatically without specifying them, you can use the [pytest.ini](https://docs.pytest.org/en/stable/reference.html#ini-options-ref) file:

`# content of pytest.ini[pytest]# Run firefox with UIaddopts = --headed --browser firefox`

## CLI arguments[​](https://playwright.dev/python/docs/test-runners#cli-arguments "Direct link to CLI arguments")

Note that CLI arguments are only applied to the default `browser`, `context` and `page` fixtures. If you create a browser, a context or a page with the API call like [browser.new_context()](https://playwright.dev/python/docs/api/class-browser#browser-new-context), the CLI arguments are not applied.

*   `--headed`: Run tests in headed mode (default: headless).
*   `--browser`: Run tests in a different browser `chromium`, `firefox`, or `webkit`. It can be specified multiple times (default: `chromium`).
*   `--browser-channel`[Browser channel](https://playwright.dev/python/docs/browsers) to be used.
*   `--slowmo` Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on (default: 0).
*   `--device`[Device](https://playwright.dev/python/docs/emulation) to be emulated.
*   `--output` Directory for artifacts produced by tests (default: `test-results`).
*   `--tracing` Whether to record a [trace](https://playwright.dev/python/docs/trace-viewer) for each test. `on`, `off`, or `retain-on-failure` (default: `off`).
*   `--video` Whether to record video for each test. `on`, `off`, or `retain-on-failure` (default: `off`).
*   `--screenshot` Whether to automatically capture a screenshot after each test. `on`, `off`, or `only-on-failure` (default: `off`).
*   `--full-page-screenshot` Whether to take a full page screenshot on failure. By default, only the viewport is captured. Requires `--screenshot` to be enabled (default: `off`).

## Fixtures[​](https://playwright.dev/python/docs/test-runners#fixtures "Direct link to Fixtures")

This plugin configures Playwright-specific [fixtures for pytest](https://docs.pytest.org/en/latest/fixture.html). To use these fixtures, use the fixture name as an argument to the test function.

`def test_my_app_is_working(fixture_name):    pass    # Test using fixture_name    # ...`

**Function scope**: These fixtures are created when requested in a test function and destroyed when the test ends.

*   `context`: New [browser context](https://playwright.dev/python/docs/browser-contexts) for a test.
*   `page`: New [browser page](https://playwright.dev/python/docs/pages) for a test.
*   `new_context`: Allows creating different [browser contexts](https://playwright.dev/python/docs/browser-contexts) for a test. Useful for multi-user scenarios. Accepts the same parameters as [browser.new_context()](https://playwright.dev/python/docs/api/class-browser#browser-new-context).

**Session scope**: These fixtures are created when requested in a test function and destroyed when all tests end.

*   `playwright`: [Playwright](https://playwright.dev/python/docs/api/class-playwright) instance.
*   `browser_type`: [BrowserType](https://playwright.dev/python/docs/api/class-browsertype) instance of the current browser.
*   `browser`: [Browser](https://playwright.dev/python/docs/api/class-browser) instance launched by Playwright.
*   `browser_name`: Browser name as string.
*   `browser_channel`: Browser channel as string.
*   `is_chromium`, `is_webkit`, `is_firefox`: Booleans for the respective browser types.

**Customizing fixture options**: For `browser` and `context` fixtures, use the following fixtures to define custom launch options.

*   `browser_type_launch_args`: Override launch arguments for [browser_type.launch()](https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch). It should return a Dict.
*   `browser_context_args`: Override the options for [browser.new_context()](https://playwright.dev/python/docs/api/class-browser#browser-new-context). It should return a Dict.
*   `connect_options`: Connect to an existing browser via WebSocket endpoint. It should return a Dict with [browser_type.connect()](https://playwright.dev/python/docs/api/class-browsertype#browser-type-connect) options.

Its also possible to override the context options ([browser.new_context()](https://playwright.dev/python/docs/api/class-browser#browser-new-context)) for a single test by using the `browser_context_args` marker:

`import pytest@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB")def test_browser_context_args(page):    assert page.evaluate("window.navigator.userAgent") == "Europe/Berlin"    assert page.evaluate("window.navigator.languages") == ["de-DE"]`

## Parallelism: Running Multiple Tests at Once[​](https://playwright.dev/python/docs/test-runners#parallelism-running-multiple-tests-at-once "Direct link to Parallelism: Running Multiple Tests at Once")

If your tests are running on a machine with a lot of CPUs, you can speed up the overall execution time of your test suite by using [`pytest-xdist`](https://pypi.org/project/pytest-xdist/) to run multiple tests at once:

`# install dependencypip install pytest-xdist# use the --numprocesses flagpytest --numprocesses auto`

Depending on the hardware and nature of your tests, you can set `numprocesses` to be anywhere from `2` to the number of CPUs on the machine. If set too high, you may notice unexpected behavior.

See [Running Tests](https://playwright.dev/python/docs/running-tests) for general information on `pytest` options.

## Examples[​](https://playwright.dev/python/docs/test-runners#examples "Direct link to Examples")

### Configure typings for auto-completion[​](https://playwright.dev/python/docs/test-runners#configure-typings-for-auto-completion "Direct link to Configure typings for auto-completion")

test_my_application.py

`from playwright.sync_api import Pagedef test_visit_admin_dashboard(page: Page):    page.goto("/admin")    # ...`

If you're using VSCode with Pylance, these types can be inferred by enabling the `python.testing.pytestEnabled` setting so you don't need the type annotation.

### Using multiple contexts[​](https://playwright.dev/python/docs/test-runners#using-multiple-contexts "Direct link to Using multiple contexts")

In order to simulate multiple users, you can create multiple [`BrowserContext`](https://playwright.dev/python/docs/browser-contexts) instances.

test_my_application.py

`from playwright.sync_api import Page, BrowserContextfrom pytest_playwright.pytest_playwright import CreateContextCallbackdef test_foo(page: Page, new_context: CreateContextCallback) -> None:    page.goto("https://example.com")    context = new_context()    page2 = context.new_page()    # page and page2 are in different contexts`

### Skip test by browser[​](https://playwright.dev/python/docs/test-runners#skip-test-by-browser "Direct link to Skip test by browser")

test_my_application.py

`import pytest@pytest.mark.skip_browser("firefox")def test_visit_example(page):    page.goto("https://example.com")    # ...`

### Run on a specific browser[​](https://playwright.dev/python/docs/test-runners#run-on-a-specific-browser "Direct link to Run on a specific browser")

conftest.py

`import pytest@pytest.mark.only_browser("chromium")def test_visit_example(page):    page.goto("https://example.com")    # ...`

### Run with a custom browser channel like Google Chrome or Microsoft Edge[​](https://playwright.dev/python/docs/test-runners#run-with-a-custom-browser-channel-like-google-chrome-or-microsoft-edge "Direct link to Run with a custom browser channel like Google Chrome or Microsoft Edge")

`pytest --browser-channel chrome`

test_my_application.py

`def test_example(page):    page.goto("https://example.com")`

### Configure base-url[​](https://playwright.dev/python/docs/test-runners#configure-base-url "Direct link to Configure base-url")

Start Pytest with the `base-url` argument. The [`pytest-base-url`](https://github.com/pytest-dev/pytest-base-url) plugin is used for that which allows you to set the base url from the config, CLI arg or as a fixture.

`pytest --base-url http://localhost:8080`

test_my_application.py

`def test_visit_example(page):    page.goto("/admin")    # -> Will result in http://localhost:8080/admin`

### Ignore HTTPS errors[​](https://playwright.dev/python/docs/test-runners#ignore-https-errors "Direct link to Ignore HTTPS errors")

conftest.py

`import pytest@pytest.fixture(scope="session")def browser_context_args(browser_context_args):    return {        **browser_context_args,        "ignore_https_errors": True    }`

### Use custom viewport size[​](https://playwright.dev/python/docs/test-runners#use-custom-viewport-size "Direct link to Use custom viewport size")

conftest.py

`import pytest@pytest.fixture(scope="session")def browser_context_args(browser_context_args):    return {        **browser_context_args,        "viewport": {            "width": 1920,            "height": 1080,        }    }`

### Device emulation / BrowserContext option overrides[​](https://playwright.dev/python/docs/test-runners#device-emulation--browsercontext-option-overrides "Direct link to Device emulation / BrowserContext option overrides")

conftest.py

`import pytest@pytest.fixture(scope="session")def browser_context_args(browser_context_args, playwright):    iphone_11 = playwright.devices['iPhone 11 Pro']    return {        **browser_context_args,        **iphone_11,    }`

Or via the CLI `--device="iPhone 11 Pro"`

### Connect to remote browsers[​](https://playwright.dev/python/docs/test-runners#connect-to-remote-browsers "Direct link to Connect to remote browsers")

conftest.py

`import pytest@pytest.fixture(scope="session")def connect_options():    return {        "wsEndpoint": "ws://localhost:8080/ws"    }`

### Using with `unittest.TestCase`[​](https://playwright.dev/python/docs/test-runners#using-with-unittesttestcase "Direct link to using-with-unittesttestcase")

See the following example for using it with `unittest.TestCase`. This has a limitation, that only a single browser can be specified and no matrix of multiple browsers gets generated when specifying multiple.

`import pytestimport unittestfrom playwright.sync_api import Pageclass MyTest(unittest.TestCase):    @pytest.fixture(autouse=True)    def setup(self, page: Page):        self.page = page    def test_foobar(self):        self.page.goto("https://microsoft.com")        self.page.locator("#foobar").click()        assert self.page.evaluate("1 + 1") == 2`

## Debugging[​](https://playwright.dev/python/docs/test-runners#debugging "Direct link to Debugging")

### Use with pdb[​](https://playwright.dev/python/docs/test-runners#use-with-pdb "Direct link to Use with pdb")

Use the `breakpoint()` statement in your test code to pause execution and get a [pdb](https://docs.python.org/3/library/pdb.html) REPL.

`def test_bing_is_working(page):    page.goto("https://bing.com")    breakpoint()    # ...`

## Deploy to CI[​](https://playwright.dev/python/docs/test-runners#deploy-to-ci "Direct link to Deploy to CI")

See the [guides for CI providers](https://playwright.dev/python/docs/ci) to deploy your tests to CI/CD.

## Async Fixtures[​](https://playwright.dev/python/docs/test-runners#async-fixtures "Direct link to Async Fixtures")

To use async fixtures, install [`pytest-playwright-asyncio`](https://pypi.org/project/pytest-playwright-asyncio/).

Ensure you are using `pytest-asyncio>=0.26.0` and set [`asyncio_default_test_loop_scope = session`](https://pytest-asyncio.readthedocs.io/en/v0.26.0/how-to-guides/change_default_test_loop.html) in your configuration (`pytest.ini/pyproject.toml/setup.cfg`).

`import pytestfrom playwright.async_api import Page@pytest.mark.asyncio(loop_scope="session")async def test_foo(page: Page):    await page.goto("https://github.com")    # ...`
