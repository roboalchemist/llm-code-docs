# Source: https://playwright.dev/docs/touch-events

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Touch events (legacy)]

On this page

<div>

# Touch events (legacy)

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Web applications that handle legacy [touch events](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events) to respond to gestures like swipe, pinch, and tap can be tested by manually dispatching [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)s to the page. The examples below demonstrate how to use [locator.dispatchEvent()](/docs/api/class-locator#locator-dispatch-event) and pass [Touch](https://developer.mozilla.org/en-US/docs/Web/API/Touch) points as arguments.

Note that [locator.dispatchEvent()](/docs/api/class-locator#locator-dispatch-event) does not set [`Event.isTrusted`](https://developer.mozilla.org/en-US/docs/Web/API/Event/isTrusted) property. If your web page relies on it, make sure to disable `isTrusted` check during the test.

### Emulating pan gesture[​](#emulating-pan-gesture "Direct link to Emulating pan gesture") 

In the example below, we emulate pan gesture that is expected to move the map. The app under test only uses `clientX/clientY` coordinates of the touch point, so we initialize just that. In a more complex scenario you may need to also set `pageX/pageY/screenX/screenY`, if your app needs them.

``` 
import  from '@playwright/test';

test.use();

async function pan(locator: Locator, deltaX?: number, deltaY?: number, steps?: number)  = await locator.evaluate((target: HTMLElement) => ;
  });

  // Providing only clientX and clientY as the app only cares about those.
  const touches = [];
  await locator.dispatchEvent('touchstart',
      );

  steps = steps ?? 5;
  deltaX = deltaX ?? 0;
  deltaY = deltaY ?? 0;
  for (let i = 1; i <= steps; i++) ];
    await locator.dispatchEvent('touchmove',
        );
  }

  await locator.dispatchEvent('touchend');
}

test(`pan gesture to move the map`, async () => );
  await page.getByRole('button', ).click();
  await expect(page.getByRole('button', )).not.toBeVisible();
  // Get the map element.
  const met = page.locator('[data-test-id="met"]');
  for (let i = 0; i < 5; i++)
    await pan(met, 200, 100);
  // Ensure the map has been moved.
  await expect(met).toHaveScreenshot();
});
```

### Emulating pinch gesture[​](#emulating-pinch-gesture "Direct link to Emulating pinch gesture") 

In the example below, we emulate pinch gesture, i.e. two touch points moving closer to each other. It is expected to zoom out the map. The app under test only uses `clientX/clientY` coordinates of touch points, so we initialize just that. In a more complex scenario you may need to also set `pageX/pageY/screenX/screenY`, if your app needs them.

``` 
import  from '@playwright/test';

test.use();

async function pinch(locator: Locator,
  arg: )  = await locator.evaluate((target: HTMLElement) => ;
  });

  const deltaX = arg.deltaX ?? 50;
  const steps = arg.steps ?? 5;
  const stepDeltaX = deltaX / (steps + 1);

  // Two touch points equally distant from the center of the element.
  const touches = [
    ,
    ,
  ];
  await locator.dispatchEvent('touchstart',
      );

  // Move the touch points towards or away from each other.
  for (let i = 1; i <= steps; i++) ,
      ,
    ];
    await locator.dispatchEvent('touchmove',
        );
  }

  await locator.dispatchEvent('touchend', );
}

test(`pinch in gesture to zoom out the map`, async () => );
  await page.getByRole('button', ).click();
  await expect(page.getByRole('button', )).not.toBeVisible();
  // Get the map element.
  const met = page.locator('[data-test-id="met"]');
  for (let i = 0; i < 5; i++)
    await pinch(met, );
  // Ensure the map has been zoomed out.
  await expect(met).toHaveScreenshot();
});
```