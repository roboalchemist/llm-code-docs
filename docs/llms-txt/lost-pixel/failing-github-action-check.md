# Source: https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/failing-github-action-check.md

# Failing GitHub Action check

By default, Lost Pixel does not exit the action with a non-zero exit code when there is a failing lost-pixel run(**differences found** ❌), but you can easily configure it.\
\
In [lostpixel.config.js|ts|cjs|mjs](https://docs.lost-pixel.com/docs/setup/project-configuration) add the following config value:

```
...
failOnDifference: true,
...
```
