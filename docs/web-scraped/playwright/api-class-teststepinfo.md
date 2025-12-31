# Source: https://playwright.dev/docs/api/class-teststepinfo

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Test Runner]
-   [TestStepInfo]

On this page

<div>

# TestStepInfo

</div>

`TestStepInfo` contains information about currently running test step. It is passed as an argument to the step function. `TestStepInfo` provides utilities to control test step execution.

``` 
import  from '@playwright/test';

test('basic test', async () => );
});
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### attach[​](#test-step-info-attach "Direct link to attach") 

Added in: v1.51 testStepInfo.attach

Attach a value or a file from disk to the current test step. Some reporters show test step attachments. Either [path](/docs/api/class-teststepinfo#test-step-info-attach-option-path) or [body](/docs/api/class-teststepinfo#test-step-info-attach-option-body) must be specified, but not both. Calling this method will attribute the attachment to the step, as opposed to [testInfo.attach()](/docs/api/class-testinfo#test-info-attach) which stores all attachments at the test level.

For example, you can attach a screenshot to the test step:

``` 
import  from '@playwright/test';

test('basic test', async () => );
  });
});
```

Or you can attach files returned by your APIs:

``` 
import  from '@playwright/test';
import  from './my-custom-helpers';

test('basic test', async () => );
  });
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

[testStepInfo.attach()](/docs/api/class-teststepinfo#test-step-info-attach) automatically takes care of copying attached files to a location that is accessible to reporters. You can safely remove the attachment after awaiting the attach call.

**Usage**

``` 
await testStepInfo.attach(name);
await testStepInfo.attach(name, options);
```

**Arguments**

-   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#test-step-info-attach-option-name)

    Attachment name. The name will also be sanitized and used as the prefix of file name when saving to disk.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `body` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") \| [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") *(optional)*[][\#](#test-step-info-attach-option-body)

        Attachment body. Mutually exclusive with [path](/docs/api/class-teststepinfo#test-step-info-attach-option-path).

    -   `contentType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#test-step-info-attach-option-content-type)

        Content type of this attachment to properly present in the report, for example `'application/json'` or `'image/png'`. If omitted, content type is inferred based on the [path](/docs/api/class-teststepinfo#test-step-info-attach-option-path), or defaults to `text/plain` for [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") attachments and `application/octet-stream` for [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") attachments.

    -   `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#test-step-info-attach-option-path)

        Path on the filesystem to the attached file. Mutually exclusive with [body](/docs/api/class-teststepinfo#test-step-info-attach-option-body).

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#test-step-info-attach-return)

------------------------------------------------------------------------

### skip()[​](#test-step-info-skip-1 "Direct link to skip()") 

Added in: v1.51 testStepInfo.skip()

Abort the currently running step and mark it as skipped. Useful for steps that are currently failing and planned for a near-term fix.

**Usage**

``` 
import  from '@playwright/test';

test('my test', async () => );
});
```

------------------------------------------------------------------------

### skip(condition)[​](#test-step-info-skip-2 "Direct link to skip(condition)") 

Added in: v1.51 testStepInfo.skip(condition)

Conditionally abort the currently running step and mark it as skipped with an optional description. Useful for steps that should not be executed in some cases.

**Usage**

``` 
import  from '@playwright/test';

test('my test', async () => );
});
```

**Arguments**

-   `condition` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[][\#](#test-step-info-skip-2-option-condition)

    A skip condition. Test step is skipped when the condition is `true`.

-   `description` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#test-step-info-skip-2-option-description)

    Optional description that will be reflected in a test report.

------------------------------------------------------------------------

## Properties[​](#properties "Direct link to Properties") 

### titlePath[​](#test-step-info-title-path "Direct link to titlePath") 

Added in: v1.55 testStepInfo.titlePath

The full title path starting with the test file name, including the step titles. See also [testInfo.titlePath](/docs/api/class-testinfo#test-info-title-path).

**Usage**

``` 
testStepInfo.titlePath
```

**Type**

-   [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")\<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\>