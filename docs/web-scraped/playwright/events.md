# Source: https://playwright.dev/docs/events

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Events]

On this page

<div>

# Events

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright allows listening to various types of events happening on the web page, such as network requests, creation of child pages, dedicated workers etc. There are several ways to subscribe to such events, such as waiting for events or adding or removing event listeners.

## Waiting for event[​](#waiting-for-event "Direct link to Waiting for event") 

Most of the time, scripts will need to wait for a particular event to happen. Below are some of the typical event awaiting patterns.

Wait for a request with the specified url using [page.waitForRequest()](/docs/api/class-page#page-wait-for-request):

``` 
// Start waiting for request before goto. Note no await.
const requestPromise = page.waitForRequest('**/*logo*.png');
await page.goto('https://wikipedia.org');
const request = await requestPromise;
console.log(request.url());
```

Wait for popup window:

``` 
// Start waiting for popup before clicking. Note no await.
const popupPromise = page.waitForEvent('popup');
await page.getByText('open the popup').click();
const popup = await popupPromise;
await popup.goto('https://wikipedia.org');
```

## Adding/removing event listener[​](#addingremoving-event-listener "Direct link to Adding/removing event listener") 

Sometimes, events happen in random time and instead of waiting for them, they need to be handled. Playwright supports traditional language mechanisms for subscribing and unsubscribing from the events:

``` 
page.on('request', request => console.log(`Request sent: $`));
const listener = request => console.log(`Request finished: $`);
page.on('requestfinished', listener);
await page.goto('https://wikipedia.org');

page.off('requestfinished', listener);
await page.goto('https://www.openstreetmap.org/');
```

## Adding one-off listeners[​](#adding-one-off-listeners "Direct link to Adding one-off listeners") 

If a certain event needs to be handled once, there is a convenience API for that:

``` 
page.once('dialog', dialog => dialog.accept('2021'));
await page.evaluate("prompt('Enter a number:')");
```