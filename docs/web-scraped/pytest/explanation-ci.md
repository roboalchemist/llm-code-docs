# Source: https://docs.pytest.org/en/stable/explanation/ci.html

[]

# CI Pipelines[¶](#ci-pipelines "Link to this heading")

## Rationale[¶](#rationale "Link to this heading")

The goal of testing in a CI pipeline is different from testing locally. Indeed, you can quickly edit some code and run your tests again on your computer, but it is not possible with CI pipeline. They run on a separate server and are triggered by specific actions.

From that observation, pytest can detect when it is in a CI environment and adapt some of its behaviours.

## How CI is detected[¶](#how-ci-is-detected "Link to this heading")

Pytest knows it is in a CI environment when either one of these environment variables are set to a non-empty value:

-   [`CI`]: used by many CI systems.

-   [`BUILD_NUMBER`]: used by Jenkins.

## Effects on CI[¶](#effects-on-ci "Link to this heading")

For now, the effects on pytest of being in a CI environment are limited.

When a CI environment is detected, the output of the short test summary info is no longer truncated to the terminal size i.e. the entire message will be shown.

> <div>
>
> ::: 
> ::: highlight
>     # content of test_ci.py
>     import pytest
>
>
>     def test_db_initialized():
>         pytest.fail(
>             "deliberately failing for demo purpose, Lorem ipsum dolor sit amet, "
>             "consectetur adipiscing elit. Cras facilisis, massa in suscipit "
>             "dignissim, mauris lacus molestie nisi, quis varius metus nulla ut ipsum."
>         )
> :::
> :::
>
> </div>

Running this locally, without any extra options, will output:

> <div>
>
> ::: 
> ::: highlight
>     $ pytest test_ci.py
>     ...
>     ========================= short test summary info ==========================
>     FAILED test_backends.py::test_db_initialized[d2] - Failed: deliberately f...
> :::
> :::
>
> </div>

*(Note the truncated text)*

While running this on CI will output:

> <div>
>
> ::: 
> ::: highlight
>     $ export CI=true
>     $ pytest test_ci.py
>     ...
>     ========================= short test summary info ==========================
>     FAILED test_backends.py::test_db_initialized[d2] - Failed: deliberately failing
>     for demo purpose, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras
>     facilisis, massa in suscipit dignissim, mauris lacus molestie nisi, quis varius
>     metus nulla ut ipsum.
> :::
> :::
>
> </div>