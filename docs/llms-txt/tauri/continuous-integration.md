# Continuous Integration

It is possible to run [WebDriver] tests with [`tauri-driver`] on your CI. The following example uses the [WebdriverIO] example we [previously built together] and
GitHub Actions.

The WebDriver tests are executed on Linux by creating a fake display.
Some CI systems such as GitHub Actions also support running WebDriver tests on Windows.

## GitHub Actions

The following GitHub Actions assumes:

1. The Tauri application is in the `src-tauri` folder.
2. The [WebDriverIO] test runner is in the `e2e-tests` directory and runs when `yarn test` is used in that directory.

```yaml title=".github/workflows/webdriver.yml"