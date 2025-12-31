# Source: https://playwright.dev/docs/api/class-testinfoerror

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Test Runner]
-   [TestInfoError]

On this page

<div>

# TestInfoError

</div>

Information about an error thrown during test execution.

------------------------------------------------------------------------

## Properties[​](#properties "Direct link to Properties") 

### cause[​](#test-info-error-cause "Direct link to cause") 

Added in: v1.49 testInfoError.cause

Error cause. Set when there is a [cause](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) for the error. Will be `undefined` if there is no cause or if the cause is not an instance of [Error](https://nodejs.org/api/errors.html#errors_class_error "Error").

**Usage**

``` 
testInfoError.cause
```

**Type**

-   [TestInfoError](/docs/api/class-testinfoerror "TestInfoError")

------------------------------------------------------------------------

### message[​](#test-info-error-message "Direct link to message") 

Added in: v1.10 testInfoError.message

Error message. Set when [Error](https://nodejs.org/api/errors.html#errors_class_error "Error") (or its subclass) has been thrown.

**Usage**

``` 
testInfoError.message
```

**Type**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

------------------------------------------------------------------------

### stack[​](#test-info-error-stack "Direct link to stack") 

Added in: v1.10 testInfoError.stack

Error stack. Set when [Error](https://nodejs.org/api/errors.html#errors_class_error "Error") (or its subclass) has been thrown.

**Usage**

``` 
testInfoError.stack
```

**Type**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

------------------------------------------------------------------------

### value[​](#test-info-error-value "Direct link to value") 

Added in: v1.10 testInfoError.value

The value that was thrown. Set when anything except the [Error](https://nodejs.org/api/errors.html#errors_class_error "Error") (or its subclass) has been thrown.

**Usage**

``` 
testInfoError.value
```

**Type**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")