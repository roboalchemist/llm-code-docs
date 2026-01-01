# Source: https://docs.together.ai/docs/ai-tutor.md

# How To Build An Interactive AI Tutor With Llama 3.1

> Learn we built LlamaTutor from scratch – an open source AI tutor with 90k users.

[LlamaTutor](https://llamatutor.together.ai/) is an app that creates an interactive tutoring session for a given topic using [Together AI’s](https://www.together.ai/) open-source LLMs.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=dd9838164e399ad4ba65028af3ce2793" alt="" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="images/guides/25.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=099549217905b28be8fd6fd69fc598d6 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=40bcf62887f72184a8e70f381fad6039 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9100049250fea24d344c93c4f18c5ded 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cf02317b42669234501b78e5b12c6b21 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e6fab195cda8d130488064aec01ab88e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e687740e621890360b8734aab8121b2d 2500w" />
</Frame>

It pulls multiple sources from the web with either Bing’s API or Serper's API, then uses the text from the sources to kick off an interactive tutoring session with the user.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=83d3d4d158ada52cab0ab2471f09faa2" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/26.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a009c2960b508f473deda879547a90cf 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e34dc07d84bd8fa01885111a84795382 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=72b1010a17883f6ae04cdeb91d5e18fa 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=77332c6c745f98c9118dcd22b34e1a2f 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=05a81a2cba985db4c8f03f3cdbd3cf78 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=263ad9bbf395435ccb4c3f81ec139d63 2500w" />
</Frame>

In this post, you’ll learn how to build the core parts of LlamaTutor. The app is open-source and built with Next.js and Tailwind, but Together’s API work great with any language or framework.

## Building the input prompt and education dropdown

LlamaTutor’s core interaction is a text field where the user can enter a topic, and a dropdown that lets the user choose which education level the material should be taught at:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e733787a865a226113fd4ee32bbc2564" alt="" data-og-width="1702" width="1702" data-og-height="594" height="594" data-path="images/guides/27.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=68c2c80515b7366f4e8928c4f3a12378 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6f67f53a4bb34ef494b17799e6916850 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b6b62437b9c4c20802cb3bbc9be7b9a4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=95d5812431e5f8619a9681860960ffc3 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f4d0fe1a1aa6bdd5d7bb18aaac552f1d 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0595d07bd5a1f93a153780e5a0250428 2500w" />
</Frame>

In the main page component, we’ll render an `<input>` and `<select>`, and control both using some new React state:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  return (
    <form>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Teach me about..."
      />
      <select value={grade} onChange={(e) => setGrade(e.target.value)}>
        <option>Elementary School</option>
        <option>Middle School</option>
        <option>High School</option>
        <option>College</option>
        <option>Undergrad</option>
        <option>Graduate</option>
      </select>
    </form>
  );
}
```

When the user submits our form, our submit handler ultimately needs to do three things:

1. Use the Bing API to fetch six different websites related to the topic
2. Parse the text from each website
3. Pass all the parsed text, as well as the education level, to Together AI to kick off the tutoring session

Let’s start by fetching the websites with Bing. We’ll wire up a submit handler to our form that makes a POST request to a new `/getSources` endpoint:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    let sources = await response.json();

    // This fetch() will 404 for now
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Teach me about..."
      />
      <select value={grade} onChange={(e) => setGrade(e.target.value)}>
        <option>Elementary School</option>
        <option>Middle School</option>
        <option>High School</option>
        <option>College</option>
        <option>Undergrad</option>
        <option>Graduate</option>
      </select>
    </form>
  );
}
```

If we submit the form, we see our React app makes a request to `/getSources` :

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=92e5573388f6bd84d025eb6c79eaf062" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/28.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=389685cd22e9ea862c9616ef008192e4 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=67d635e8aad971b7e176a3421ee180a7 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=98d8c6499377bc73ee90a4b7a599efb7 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e7b0f22ae781414574d25cf7387d5518 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=252aabc3fd77d01dd242684d383c0be6 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8498d782d2dde8ef09b7ee987bcf1066 2500w" />
</Frame>

Let’s go implement this API route.

## Getting web sources with Bing

To create our API route, we’ll make a new`app/api/getSources/route.js`file:

```jsx JSX theme={null}
// app/api/getSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.topic` has the user's text
}
```

The [Bing API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api) lets you make a fetch request to get back search results, so we’ll use it to build up our list of sources:

```jsx JSX theme={null}
// app/api/getSources/route.js
import { NextResponse } from 'next/server';

export async function POST(req) {
  const json = await req.json();

  const params = new URLSearchParams({
    q: json.topic,
    mkt: 'en-US',
    count: '6',
    safeSearch: 'Strict',
  });

  const response = await fetch(
    `https://api.bing.microsoft.com/v7.0/search?${params}`,
    {
      method: 'GET',
      headers: {
        'Ocp-Apim-Subscription-Key': process.env['BING_API_KEY'],
      },
    }
  );
  const { webPages } = await response.json();

  return NextResponse.json(
    webPages.value.map((result) => ({
      name: result.name,
      url: result.url,
    }))
  );
}
```

In order to make a request to Bing’s API, you’ll need to [get an API key from Microsoft](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api). Once you have it, set it in `.env.local`:

```jsx JSX theme={null}
// .env.local
BING_API_KEY=xxxxxxxxxxxx
```

and our API handler should work.

Let’s try it out from our React app! We’ll log the sources in our submit handler:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    const sources = await response.json();

    // log the response from our new endpoint
    console.log(sources);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Teach me about..."
      />
      <select value={grade} onChange={(e) => setGrade(e.target.value)}>
        <option>Elementary School</option>
        <option>Middle School</option>
        <option>High School</option>
        <option>College</option>
        <option>Undergrad</option>
        <option>Graduate</option>
      </select>
    </form>
  );
}
```

and if we try submitting a topic, we’ll see an array of pages logged in the console!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9f0c9b3b0f6228e07bea418c5353b3b5" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/29.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=71267f03b11f23ca5c4d6841380463c8 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=752048c898c16e84fc018bd6b2f8df43 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bf06784ebc7460e70694a0d3ffdd15a4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=36280e757e39d56f41f5f3aadb1902b6 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=74f1ee456b358140613075ad522a1705 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e7e90678cf50a7f622bedb40e84b804d 2500w" />
</Frame>

Let’s create some new React state to store the responses and display them in our UI:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');
  const [sources, setSources] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    const sources = await response.json();

    // Update the sources with our API response
    setSources(sources);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>{/* ... */}</form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.name}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </>
  );
}
```

If we try it out, our app is working great so far!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ce32b4be67a3087fd6e054e52b65d231" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/30.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2eb346313c648876d8ec3b728c9c9a77 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b72dba4a26148e3f28cccf1e403e6bf3 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e5e6dcce61dc11e0a27b05a00b31f8f4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=184c5642e435463d02be2001e2f27f82 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=85827f1fff733e27a87d463e2da2bbd5 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a4bfb2bca435c8251660ea11275176e9 2500w" />
</Frame>

We’re taking the user’s topic, fetching six relevant web sources from Bing, and displaying them in our UI.

Next, let’s get the text content from each website so that our AI model has some context for its first response.

## Fetching the content from each source

Let’s make a request to a second endpoint called `/api/getParsedSources`, passing along the sources in the request body:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  // ...

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the sources to a new endpoint
    const parsedSourcesRes = await fetch('/api/getParsedSources', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sources }),
    });

    // The second fetch() will 404 for now
  }

  // ...
}
```

We’ll create a file at`app/api/getParsedSources/route.js` for our new route:

```jsx JSX theme={null}
// app/api/getParsedSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.sources` has the websites from Bing
}
```

Now we’re ready to actually get the text from each one of our sources.

Let’s write a new `getTextFromURL` function and outline our general approach:

```jsx JSX theme={null}
async function getTextFromURL(url) {
  // 1. Use fetch() to get the HTML content
  // 2. Use the `jsdom` library to parse the HTML into a JavaScript object
  // 3. Use `@mozilla/readability` to clean the document and
  //    return only the main text of the page
}
```

Let’s implement this new function. We’ll start by installing the `jsdom` and `@mozilla/readability` libraries:

```jsx JSX theme={null}
npm i jsdom @mozilla/readability
```

Next, let’s implement the steps:

```jsx JSX theme={null}
async function getTextFromURL(url) {
  // 1. Use fetch() to get the HTML content
  const response = await fetch(url);
  const html = await response.text();

  // 2. Use the `jsdom` library to parse the HTML into a JavaScript object
  const virtualConsole = new jsdom.VirtualConsole();
  const dom = new JSDOM(html, { virtualConsole });

  // 3. Use `@mozilla/readability` to clean the document and
  //    return only the main text of the page
  const { textContent } = new Readability(doc).parse();
}
```

Looks good - let’s try it out!

We’ll run the first source through `getTextFromURL`:

```jsx JSX theme={null}
// app/api/getParsedSources/route.js
export async function POST(req) {
  let json = await req.json();

  let textContent = await getTextFromURL(json.sources[0].url);

  console.log(textContent);
}
```

If we submit our form , we’ll see the text show up in our server terminal from the first page!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aafd49af898764f983d6129e351e7f15" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/31.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ce319fc5d406d057766a14aec9e0a14c 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5df9013d584a2dda307539eaf3216341 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e64db884d0be3e1f4c34761fa73cba23 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=244ae2de9e5dfc66e052053f924139fe 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=97c39be74aae21fc58462bbcc4753044 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=472fc906cd1baf86f7e0c01c2c861887 2500w" />
</Frame>

Let’s update the code toget the text from all the sources.

Since each source is independent, we can use `Promise.all` to kick off our functions in parallel:

```jsx JSX theme={null}
// app/api/getAnswer/route.js
export async function POST(req) {
  let json = await req.json();

  let results = await Promise.all(
    json.sources.map((source) => getTextFromURL(source.url))
  );

  console.log(results);
}
```

If we try again, we’ll now see an array of each web page’s text logged to the console:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5e5eb89322d2bde318831fc0891c9ea4" alt="" data-og-width="1682" width="1682" data-og-height="1744" height="1744" data-path="images/guides/32.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c722f26797085578aa77bb485c901b42 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7ba84e41a110fd3818dcbbf2734d3ea9 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ee6a3d7776bb5b00e806a8858c69468b 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8ecbee1cf6e8ea751536fc79a6157cad 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=222c76e259759692a00cf3128e2226cd 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aa4a811bb146c0d13168c3988c90eaca 2500w" />
</Frame>

We’re ready to use the parsed sources in our React frontend!

## Using the sources for the chatbot’s initial messages

Back in our React app, we now have the text from each source in our submit handler:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  // ...

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    const parsedSourcesRes = await fetch('/api/getParsedSources', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sources }),
    });

    // The text from each source
    const parsedSources = await parsedSourcesRes.json();
  }

  // ...
}
```

We’re ready to kick off our chatbot. We’ll use the selected grade level and the parsed sources to write a system prompt, and pass in the selected topic as the user’s first message:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleSubmit(e) {
    // ...

    // The text from each source
    const parsedSources = await parsedSourcesRes.json();

    // Start our chatbot
    const systemPrompt = `
      You're an interactive personal tutor who is an expert at explaining topics. Given a topic and the information to teach, please educate the user about it at a ${grade} level.

      Here's the information to teach:

      <teaching_info>
      ${parsedSources.map(
        (result, index) =>
          `## Webpage #${index}:\\n ${result.fullContent} \\n\\n`
      )}
      </teaching_info>
    `;

    const initialMessages = [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: topic },
    ];
    setMessages(initialMessages);

    // This will 404 for now
    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: initialMessages }),
    });
  }

  // ...
}
```

We also created some new React state to store all the messages so that we can display and update the chat history as the user sends new messages.

We’re ready to implement our final API endpoint at `/chat`!

## Implementing the chatbot endpoint with Together AI’s SDK

Let’s install Together AI’s node SDK:

```jsx JSX theme={null}
npm i together-ai
```

and use it to query Llama 3.1 8B Turbo:

```jsx JSX theme={null}
// api/chat/route.js
import { Together } from 'togetherai';

const together = new Together();

export async function POST(req) {
  const json = await req.json();

  const res = await together.chat.completions.create({
    model: 'meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
    messages: json.messages,
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

Since we’re passing the array of messages directly from our React app, and the format is the same as what Together’s `chat.completions.create` method expects, our API handler is mostly acting as a simple passthrough.

We’re also using the `stream: true` option so our frontend will be able to show partial updates as soon as the LLM starts its response.

We’re read to display our chatbot’s first message in our React app!

## Displaying the chatbot’s response in the UI

Back in our page, we’ll use the `ChatCompletionStream` helper from Together’s SDK to update our `messages` state as our API endpoint streams in text:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleSubmit(e) {
    // ...

    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: initialMessages }),
    });

    ChatCompletionStream.fromReadableStream(chatRes.body).on(
      'content',
      (delta) => {
        setMessages((prev) => {
          const lastMessage = prev[prev.length - 1];

          if (lastMessage.role === 'assistant') {
            return [
              ...prev.slice(0, -1),
              { ...lastMessage, content: lastMessage.content + delta },
            ];
          } else {
            return [...prev, { role: 'assistant', content: delta }];
          }
        });
      }
    );
  }

  // ...
}
```

Note that because we’re storing the entire history of messages as an array, we check the last message’s `role` to determine whether to append the streamed text to it, or push a new object with the assistant’s initial text.

Now that our `messages` React state is ready, let’s update our UI to display it:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');
  const [sources, setSources] = useState([]);
  const [messages, setMessages] = useState([]);

  async function handleSubmit(e) {
    // ...
  }

  return (
    <>
      <form onSubmit={handleSubmit}>{/* ... */}</form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.name}</a>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Display the messages */}
      {messages.map((message, i) => (
        <p key={i}>{message.content}</p>
      ))}
    </>
  );
}
```

If we try it out, we’ll see the sources come in, and once our `chat` endpoint responds with the first chunk, we’ll see the answer text start streaming into our UI!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6524178a639503751c16dc713afb81a4" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/33.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=497d7dcf0114276fee30e72bad9272be 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b78e411455f4ccec95e2c5b2cf5362a8 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a6e08df04098a6feb2187b9a05969bed 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8b07f9b488780f752c4020c30f858a01 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ae918a63013689621da6d989ce6108ab 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ac70bc939926bb197f99e86effe6b7bc 2500w" />
</Frame>

## Letting the user ask follow-up questions

To let the user ask our tutor follow-up questions, let’s make a new form that only shows up once we have some messages in our React state:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  // ...
  const [newMessageText, setNewMessageText] = useState('');

  return (
    <>
      {/* Form for initial messages */}
      {messages.length === 0 && (
        <form onSubmit={handleSubmit}>{/* ... */}</form>
      )}

      {sources.length > 0 && <>{/* ... */}</>}

      {messages.map((message, i) => (
        <p key={i}>{message.content}</p>
      ))}

      {/* Form for follow-up messages */}
      {messages.length > 0 && (
        <form>
          <input
            value={newMessageText}
            onChange={(e) => setNewMessageText(e.target.value)}
            type="text"
          />
        </form>
      )}
    </>
  );
}
```

We’ll make a new submit handler called `handleMessage` that will look a lot like the end of our first `handleSubmit` function:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleMessage(e) {
    e.preventDefault();

    const newMessages = [
      ...messages,
      {
        role: 'user',
        content: newMessageText,
      },
    ];

    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: newMessages }),
    });
    setMessages(newMessages);

    ChatCompletionStream.fromReadableStream(chatRes.body).on(
      'content',
      (delta) => {
        setMessages((prev) => {
          const lastMessage = prev[prev.length - 1];

          if (lastMessage.role === 'assistant') {
            return [
              ...prev.slice(0, -1),
              { ...lastMessage, content: lastMessage.content + delta },
            ];
          } else {
            return [...prev, { role: 'assistant', content: delta }];
          }
        });
      }
    );
  }

  // ...
}
```

Because we have all the messages in React state, we can just create a new object for the user’s latest message, send it over to our existing `chat` endpoint, and reuse the same logic to update our app’s state as the latest response streams in.

The core features of our app are working great!

## Digging deeper

React and Together AI are a perfect match for building powerful chatbots like LlamaTutor.

The app is fully open-source, so if you want to keep working on the code from this tutorial, be sure to check it out on GitHub:

[https://github.com/Nutlope/llamatutor](https://github.com/Nutlope/llamatutor)

And if you’re ready to start building your own chatbots, [sign up for Together AI today](https://www.together.ai/) and make your first query in minutes!

***


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt