# Source: https://playwright.dev/docs/mock-browser-apis

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Mock browser APIs]

On this page

<div>

# Mock browser APIs

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright provides native support for most of the browser features. However, there are some experimental APIs and APIs which are not (yet) fully supported by all browsers. Playwright usually doesn\'t provide dedicated automation APIs in such cases. You can use mocks to test the behavior of your application in such cases. This guide gives a few examples.

Let\'s consider a web app that uses [battery API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/getBattery) to show your device\'s battery status. We\'ll mock the battery API and check that the page correctly displays the battery status.

## Creating mocks[​](#creating-mocks "Direct link to Creating mocks") 

Since the page may be calling the API very early while loading it\'s important to setup all the mocks before the page started loading. The easiest way to achieve that is to call [page.addInitScript()](/docs/api/class-page#page-add-init-script):

``` 
await page.addInitScript(() => 
  };
  // Override the method to always return mock battery info.
  window.navigator.getBattery = async () => mockBattery;
});
```

Once this is done you can navigate the page and check its UI state:

``` 
// Configure mock API before each test.
test.beforeEach(async () => 
    };
    // Override the method to always return mock battery info.
    window.navigator.getBattery = async () => mockBattery;
  });
});

test('show battery status', async () => );
```

## Mocking read-only APIs[​](#mocking-read-only-apis "Direct link to Mocking read-only APIs") 

Some APIs are read-only so you won\'t be able to assign to a navigator property. For example,

``` 
// Following line will have no effect.
navigator.cookieEnabled = true;
```

However, if the property is [configurable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty#configurable), you can still override it using the plain JavaScript:

``` 
await page.addInitScript(() => );
});
```

## Verifying API calls[​](#verifying-api-calls "Direct link to Verifying API calls") 

Sometimes it is useful to check if the page made all expected APIs calls. You can record all API method invocations and then compare them with golden result. [page.exposeFunction()](/docs/api/class-page#page-expose-function) may come in handy for passing message from the page back to the test code:

``` 
test('log battery calls', async () => `)
    };
    // Override the method to always return mock battery info.
    window.navigator.getBattery = async () => ;
  });

  await page.goto('/');
  await expect(page.locator('.battery-percentage')).toHaveText('75%');

  // Compare actual calls with golden.
  expect(log).toEqual([
    'getBattery',
    'addEventListener:chargingchange',
    'addEventListener:levelchange'
  ]);
});
```

## Updating mock[​](#updating-mock "Direct link to Updating mock") 

To test that the app correctly reflects battery status updates it\'s important to make sure that the mock battery object fires same events that the browser implementation would. The following test demonstrates how to achieve that:

``` 
test('update battery status (no golden)', async () => 
      // Will be called by the test.
      _setLevel(value) 
      _setCharging(value) 
    }
    const mockBattery = new BatteryMock();
    // Override the method to always return mock battery info.
    window.navigator.getBattery = async () => mockBattery;
    // Save the mock object on window for easier access.
    window.mockBattery = mockBattery;
  });

  await page.goto('/');
  await expect(page.locator('.battery-percentage')).toHaveText('10%');

  // Update level to 27.5%
  await page.evaluate(() => window.mockBattery._setLevel(0.275));
  await expect(page.locator('.battery-percentage')).toHaveText('27.5%');
  await expect(page.locator('.battery-status')).toHaveText('Battery');

  // Emulate connected adapter
  await page.evaluate(() => window.mockBattery._setCharging(true));
  await expect(page.locator('.battery-status')).toHaveText('Adapter');
  await expect(page.locator('.battery-fully')).toHaveText('00:30');
});
```