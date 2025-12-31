# Source: https://playwright.dev/docs/clock

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Clock]

On this page

<div>

# Clock

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Accurately simulating time-dependent behavior is essential for verifying the correctness of applications. Utilizing [Clock](/docs/api/class-clock "Clock") functionality allows developers to manipulate and control time within tests, enabling the precise validation of features such as rendering time, timeouts, scheduled tasks without the delays and variability of real-time execution.

The [Clock](/docs/api/class-clock "Clock") API provides the following methods to control time:

-   `setFixedTime`: Sets the fixed time for `Date.now()` and `new Date()`.
-   `install`: initializes the clock and allows you to:
    -   `pauseAt`: Pauses the time at a specific time.
    -   `fastForward`: Fast forwards the time.
    -   `runFor`: Runs the time for a specific duration.
    -   `resume`: Resumes the time.
-   `setSystemTime`: Sets the current system time.

The recommended approach is to use `setFixedTime` to set the time to a specific value. If that doesn\'t work for your use case, you can use `install` which allows you to pause time later on, fast forward it, tick it, etc. `setSystemTime` is only recommended for advanced use cases.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

[page.clock](/docs/api/class-page#page-clock) overrides native global classes and functions related to time allowing them to be manually controlled:

-   `Date`
-   `setTimeout`
-   `clearTimeout`
-   `setInterval`
-   `clearInterval`
-   `requestAnimationFrame`
-   `cancelAnimationFrame`
-   `requestIdleCallback`
-   `cancelIdleCallback`
-   `performance`
-   `Event.timeStamp`

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

If you call `install` at any point in your test, the call *MUST* occur before any other clock related calls (see note above for list). Calling these methods out of order will result in undefined behavior. For example, you cannot call `setInterval`, followed by `install`, then `clearInterval`, as `install` overrides the native definition of the clock functions.

## Test with predefined time[​](#test-with-predefined-time "Direct link to Test with predefined time") 

Often you only need to fake `Date.now` while keeping the timers going. That way the time flows naturally, but `Date.now` always returns a fixed value.

``` 
<div id="current-time" data-testid="current-time"></div>
<script>
  const renderTime = () => ;
  setInterval(renderTime, 1000);
</script>
```

``` 
await page.clock.setFixedTime(new Date('2024-02-02T10:00:00'));
await page.goto('http://localhost:3333');
await expect(page.getByTestId('current-time')).toHaveText('2/2/2024, 10:00:00 AM');

await page.clock.setFixedTime(new Date('2024-02-02T10:30:00'));
// We know that the page has a timer that updates the time every second.
await expect(page.getByTestId('current-time')).toHaveText('2/2/2024, 10:30:00 AM');
```

## Consistent time and timers[​](#consistent-time-and-timers "Direct link to Consistent time and timers") 

Sometimes your timers depend on `Date.now` and are confused when the `Date.now` value does not change over time. In this case, you can install the clock and fast forward to the time of interest when testing.

``` 
<div id="current-time" data-testid="current-time"></div>
<script>
  const renderTime = () => ;
  setInterval(renderTime, 1000);
</script>
```

``` 
// Initialize clock with some time before the test time and let the page load
// naturally. `Date.now` will progress as the timers fire.
await page.clock.install();
await page.goto('http://localhost:3333');

// Pretend that the user closed the laptop lid and opened it again at 10am,
// Pause the time once reached that point.
await page.clock.pauseAt(new Date('2024-02-02T10:00:00'));

// Assert the page state.
await expect(page.getByTestId('current-time')).toHaveText('2/2/2024, 10:00:00 AM');

// Close the laptop lid again and open it at 10:30am.
await page.clock.fastForward('30:00');
await expect(page.getByTestId('current-time')).toHaveText('2/2/2024, 10:30:00 AM');
```

## Test inactivity monitoring[​](#test-inactivity-monitoring "Direct link to Test inactivity monitoring") 

Inactivity monitoring is a common feature in web applications that logs out users after a period of inactivity. Testing this feature can be tricky because you need to wait for a long time to see the effect. With the help of the clock, you can speed up time and test this feature quickly.

``` 
<div id="remaining-time" data-testid="remaining-time"></div>
<script>
  const endTime = Date.now() + 5 * 60_000;
  const renderTime = () =>  else  seconds.`;
    }
    setTimeout(renderTime, 1000);
  };
  renderTime();
</script>
<button type="button">Interaction</button>
```

``` 
// Initial time does not matter for the test, so we can pick current time.
await page.clock.install();
await page.goto('http://localhost:3333');
// Interact with the page
await page.getByRole('button').click();

// Fast forward time 5 minutes as if the user did not do anything.
// Fast forward is like closing the laptop lid and opening it after 5 minutes.
// All the timers due will fire once immediately, as in the real browser.
await page.clock.fastForward('05:00');

// Check that the user was logged out automatically.
await expect(page.getByText('You have been logged out due to inactivity.')).toBeVisible();
```

## Tick through time manually, firing all the timers consistently[​](#tick-through-time-manually-firing-all-the-timers-consistently "Direct link to Tick through time manually, firing all the timers consistently") 

In rare cases, you may want to tick through time manually, firing all timers and animation frames in the process to achieve a fine-grained control over the passage of time.

``` 
<div id="current-time" data-testid="current-time"></div>
<script>
  const renderTime = () => ;
  setInterval(renderTime, 1000);
</script>
```

``` 
// Initialize clock with a specific time, let the page load naturally.
await page.clock.install();
await page.goto('http://localhost:3333');

// Pause the time flow, stop the timers, you now have manual control
// over the page time.
await page.clock.pauseAt(new Date('2024-02-02T10:00:00'));
await expect(page.getByTestId('current-time')).toHaveText('2/2/2024, 10:00:00 AM');

// Tick through time manually, firing all timers in the process.
// In this case, time will be updated in the screen 2 times.
await page.clock.runFor(2000);
await expect(page.getByTestId('current-time')).toHaveText('2/2/2024, 10:00:02 AM');
```

## Related Videos[​](#related-videos "Direct link to Related Videos")