# Source: https://playwright.dev/docs/api/class-apiresponseassertions

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Assertions]
-   [APIResponseAssertions]

On this page

<div>

# APIResponseAssertions

</div>

The [APIResponseAssertions](/docs/api/class-apiresponseassertions "APIResponseAssertions") class provides assertion methods that can be used to make assertions about the [APIResponse](/docs/api/class-apiresponse "APIResponse") in the tests.

``` 
import  from '@playwright/test';

test('navigates to login', async () => );
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### toBeOK[​](#api-response-assertions-to-be-ok "Direct link to toBeOK") 

Added in: v1.18 apiResponseAssertions.toBeOK

Ensures the response status code is within `200..299` range.

**Usage**

``` 
await expect(response).toBeOK();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#api-response-assertions-to-be-ok-return)

------------------------------------------------------------------------

## Properties[​](#properties "Direct link to Properties") 

### not[​](#api-response-assertions-not "Direct link to not") 

Added in: v1.20 apiResponseAssertions.not

Makes the assertion check for the opposite condition. For example, this code tests that the response status is not successful:

``` 
await expect(response).not.toBeOK();
```

**Usage**

``` 
expect(response).not
```

**Type**

-   [APIResponseAssertions](/docs/api/class-apiresponseassertions "APIResponseAssertions")