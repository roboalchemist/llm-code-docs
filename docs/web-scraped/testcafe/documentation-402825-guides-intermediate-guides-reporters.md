# Source: https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters

Title: Reporters | Intermediate Guides | Guides

URL Source: https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters

Markdown Content:
Reporter modules format and output TestCafe test run results.

[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#included-reporters)Included Reporters[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#included-reporters)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe includes the following reporters out of the box:

*   [spec](https://github.com/DevExpress/testcafe-reporter-spec) - the default reporter
*   [list](https://github.com/DevExpress/testcafe-reporter-list)
*   [minimal](https://github.com/DevExpress/testcafe-reporter-minimal)
*   [xUnit](https://github.com/DevExpress/testcafe-reporter-xunit)
*   [JSON](https://github.com/DevExpress/testcafe-reporter-json)

[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#community-reporters-and-custom-reporters)Community Reporters and Custom Reporters[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#community-reporters-and-custom-reporters)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can [install community reporters](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#install-new-reporters) or create a [custom reporter](https://testcafe.io/documentation/402810/guides/extend-testcafe/reporter-plugin) of your own.

The following community reporters are amongst the most popular:

*   [NUnit](https://github.com/DevExpress/testcafe-reporter-nunit)
*   [Tesults](https://www.npmjs.com/package/testcafe-reporter-tesults)

[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#install-new-reporters)Install New Reporters[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#install-new-reporters)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Reporter plugins are npm packages. TestCafe reporter package names start with the `testcafe-reporter-` prefix (for example, `testcafe-reporter-list`).

You can search for reporter packages on npm: [https://www.npmjs.com/search?q=testcafe-reporter](https://www.npmjs.com/search?q=testcafe-reporter).

Install reporter packages from npm as you would install any other plugin. See [Install Plugins](https://testcafe.io/documentation/402811/guides/extend-testcafe/install-plugins).

[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#specify-the-reporter)Specify the Reporter[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#specify-the-reporter)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default reporter is [spec](https://github.com/DevExpress/testcafe-reporter-spec). To use an alternative reporter, use the [-r (--reporter)](https://testcafe.io/documentation/402639/reference/command-line-interface#-r-nameoutput---reporter-nameoutput) CLI option or the [runner.reporter] Test Runner method.

```
testcafe all ./tests/sample-fixture.js -r xunit
```

```
await runner
    .browsers('all')
    .src('./tests/sample-fixture.js')
    .reporter('xunit')
    .run();
```

You can also specify which the reporter in the [configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#reporters).

[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#output-data-to-disk)Output data to disk[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#output-data-to-disk)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe reporters can write report data to disk:

```
testcafe all ./tests/sample-fixture.js -r json:report.json
```

```
await runner
    .browsers('all')
    .src('./tests/sample-fixture.js')
    .reporter('json', 'report.json')
    .run();
```

[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#use-multiple-reporters)Use Multiple Reporters[](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters#use-multiple-reporters)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use multiple reporters, provided only one of them writes to stdout. In the examples below, the `spec` reporter outputs data to `stdout`, while the `xunit` reporter writes data to disk.

```
testcafe all ./tests/sample-fixture.js -r spec,xunit:report.xml
```

```
await runner
    .browsers('all')
    .src('./tests/sample-fixture.js')
    .reporter(['spec', {
        name: 'xunit',
        output: 'report.xml'
    })
    .run();
```
