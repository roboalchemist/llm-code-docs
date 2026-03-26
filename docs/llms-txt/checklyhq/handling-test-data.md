# Source: https://checklyhq.com/docs/learn/playwright/handling-test-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Handle Test Data with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

We define *test data* as any data we consistently use to verify properties such as a system's functionality or performance. Another popular term for the same concept is *fixture*. We will use these interchangeably.

## Avoiding duplication

It is often desirable to [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) up our scripts by factoring out test data. In the case of simple tests, it's usually not an issue to embed test data directly inside our script, but complex end-to-end scenarios might require moving this information elsewhere, like a dedicated file.

Looking at our [test webshop](https://danube-store.herokuapp.com/), we might want to verify that a specific item list is loaded on the store's front page. As this list contains several tens of elements, each with different attributes, keeping our fixtures inside our script would be impractical. Let's add this data to a JSON file instead:

```json  theme={null}
[
    { "title": "Haben oder haben", "author": "Fric Eromm", "price": "9.95" },
    { "title": "Parry Hotter", "author": "J/K Rowlin'", "price": "9.95" },
    { "title": "Laughterhouse-Five", "author": "Truk Tugennov", "price": "9.95" },
    { "title": "To Mock a Killingbird", "author": "Larper Hee", "price": "9.95" },
    { "title": "1498", "author": "Gorge Norwell", "price": "9.95" },
    { "title": "The Grand Grotsby", "author": "Gerald F. Scott", "price": "9.95" },
    { "title": "The Pickled Lynx", "author": "Ant One", "price": "9.95" },
    { "title": "Celsius 233", "author": "Bay Radbdury", "price": "9.95" },
    { "title": "The Rye in the Catcher", "author": "DJ Salinger", "price": "9.95" },
    { "title": "Of Mouse and Man", "author": "Johannes Beckstein", "price": "9.95" },
    ...
]
```

We are then able to feed this file into our test...

```js  theme={null}
const fs = require('fs')
...
let rawdata = fs.readFileSync('books.json')
const bookList = JSON.parse(rawdata)
const foundList = bookList
```

...and have each comparison executed to ensure the right elements are being shown.

```js  theme={null}
  // remove every element found from the control array...
  for  (i = 0; i < resultsNumber; i++) {
      const bookTitle = await page.$eval(`.preview:nth-child(${i+1}) > .preview-title`, e => e.innerText)
      const bookAuthor = await page.$eval(`.preview:nth-child(${i+1}) > .preview-author`, e => e.innerText)
      foundList = foundList.filter(e => (!((e.title === bookTitle) && (e.author === bookAuthor))))
  }

  // ...then assert that the control array is now empty
  assert.equal(foundList.length, 0)
```

## Retrieving test data

If the platform you are testing exposes an API endpoint to pull up-to-date test data, you could fetch the file as part of the setup phase of your test and then utilize it:

```js  theme={null}
const axios = require('axios')
...
const { data } = await axios.get('https://danube-store.herokuapp.com/api/books')
const bookList = JSON.parse(data)
const foundList = bookList
```

This approach enables testing with production data, so you don't have to maintain the test data yourself.

## Generating test data

If you test form submissions, relying on generated data might also make sense to avoid only testing the happy path. [Faker](https://fakerjs.dev/) is a library to create fake but realistic data sets.

```js  theme={null}
const { faker } = require("@faker-js/faker")
...
await page.type('#s-name', faker.name.firstName()) // Leif
await page.type('#s-surname', faker.name.lastName()) // Kirlin
await page.type('#s-address', faker.address.streetAddress(true)) // 2629 Ross Glens Suite 089
await page.type('#s-zipcode', faker.address.zipCode()) // 03651
await page.type('#s-city', faker.address.city()) // Rohanfort
await page.type('#s-company', faker.company.companyName()) // Reynolds Group
```

Faker covers a wide range of data that includes names, addresses, products, images and much more.

## Takeaways

1. Keep test data separate from your scripts.
2. REST APIs can be useful for retrieving test data.
3. Libraries such as Faker can help generate test data.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).