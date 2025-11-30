# Source: https://docs.exa.ai/examples/exa-researcher.md

# Exa Researcher - JavaScript

> Example project using the Exa JS SDK.

***

## What this doc covers

1. Using Exa's Auto search to pick the best search setting for each query
2. Using searchAndContents() through Exa's JavaScript SDK

***

In this example, we will build Exa Researcher, a JavaScript app that, given a research topic, automatically searches for relevant sources with Exa's [**Auto search**](/changelog/auto-search-as-default) and synthesizes the information into a reliable research report.

Fastest setup: Interact with the code in your browser with this Replit [template](https://replit.com/@olafblitz/exa-researcher?v=1).

Alternatively, this [interactive notebook](https://github.com/exa-labs/exa-js/tree/master/examples/researcher/researcher.ipynb) was made with the Deno Javascript kernel for Jupyter so you can easily run it locally. Check out the [plain JS version](https://github.com/exa-labs/exa-js/tree/master/examples/researcher/researcher.mjs) if you prefer a regular Javascript file you can run with NodeJS, or want to skip to the final result. If you'd like to run this notebook locally, [Installing Deno](https://docs.deno.com/runtime/manual/getting%5Fstarted/installation) and [connecting Deno to Jupyter](https://docs.deno.com/runtime/manual/tools/jupyter) is fast and easy.

To play with this code, first we need a [Exa API key](https://dashboard.exa.ai/api-keys) and an [OpenAI API key](https://platform.openai.com/api-keys).

## Setup

Let's import the Exa and OpenAI SDKs and put in our API keys to create a client object for each. Make sure to pick the right imports for your runtime and paste or load your API keys.

```TypeScript TypeScript theme={null}
// Deno imports
import Exa from 'npm:exa-js';
import OpenAI from 'npm:openai';

// NodeJS imports
//import Exa from 'exa-js';
//import OpenAI from 'openai';

// Replit imports
//const Exa = require("exa-js").default;
//const OpenAI = require("openai");

const EXA_API_KEY = "" // insert or load your API key here
const OPENAI_API_KEY = ""// insert or load your API key here

const exa = new Exa(EXA_API_KEY);
const openai = new OpenAI({ apiKey: OPENAI_API_KEY });
```

Since we'll be making several calls to the OpenAI API to get a completion from GPT-3.5 Turbo, let's make a simple utility function so we can pass in the system and user messages directly, and get the LLM's response back as a string.

```TypeScript TypeScript theme={null}
async function getLLMResponse({system = 'You are a helpful assistant.', user = '', temperature = 1, model = 'gpt-3.5-turbo'}){
    const completion = await openai.chat.completions.create({
        model,
        temperature,
        messages: [
            {'role': 'system', 'content': system},
            {'role': 'user', 'content': user},
        ]
    });
    return completion.choices[0].message.content;
}
```

Okay, great! Now let's starting building Exa Researcher.

## Exa Auto search

The researcher should be able to automatically generate research reports for all kinds of different topics. Here's two to start:

```TypeScript TypeScript theme={null}

const SAMA_TOPIC = 'Sam Altman';
const ART_TOPIC = 'renaissance art';
```

The first thing our researcher has to do is decide what kind of search to do for the given topic.

Exa offers multiple search methods, with **neural** search being our primary approach. Neural search is preferred when the query is broad and complex because it lets us retrieve high quality, semantically relevant data. Neural search is especially suitable when a topic is well-known and popularly discussed on the Internet, allowing the machine learning model to retrieve contents which are more likely recommended by real humans.

Conveniently, Exa's autosearch feature (on by default) will automatically decide which search method to use for each query, optimizing results based on the query type.

Now, we'll create a helper function to generate search queries for our topic.

```TypeScript TypeScript theme={null}
async function generateSearchQueries(topic, n){
    const userPrompt = `I'm writing a research report on ${topic} and need help coming up with diverse search queries.
Please generate a list of ${n} search queries that would be useful for writing a research report on ${topic}. These queries can be in various formats, from simple terms to more complex phrases. Do not add any formatting or numbering to the queries.`;

    const completion = await getLLMResponse({
        system: 'The user will ask you to help generate some search queries. Respond with only the suggested queries in plain text with no extra formatting, each on its own line.',
        user: userPrompt,
        temperature: 1
    });
    return completion.split('\n').filter(s => s.trim().length > 0).slice(0, n);
}
```

Next, let's write another function that actually calls the Exa API to perform searches using Auto search.

```TypeScript TypeScript theme={null}
async function getSearchResults(queries, linksPerQuery=2){
    let results = [];
    for (const query of queries){
        const searchResponse = await exa.searchAndContents(query, {
            numResults: linksPerQuery
        });
        results.push(...searchResponse.results);
    }
    return results;
}
```

## Writing a report with GPT-4

The final step is to instruct the LLM to synthesize the content into a research report, including citations of the original links. We can do that by pairing the content and the URLs and writing them into the prompt.

```TypeScript TypeScript theme={null}
 async function synthesizeReport(topic, searchContents, contentSlice = 750){
    const inputData = searchContents.map(item => `--START ITEM--\nURL: ${item.url}\nCONTENT: ${item.text.slice(0, contentSlice)}\n--END ITEM--\n`).join('');
    return await getLLMResponse({
        system: 'You are a helpful research assistant. Write a report according to the user\'s instructions.',
        user: 'Input Data:\n' + inputData + `Write a two paragraph research report about ${topic} based on the provided information. Include as many sources as possible. Provide citations in the text using footnote notation ([#]). First provide the report, followed by a single "References" section that lists all the URLs used, in the format [#] <url>.`,
        //model: 'gpt-4' //want a better report? use gpt-4 (but it costs more)
    });
}
```

## All Together Now

Now, let's just wrap everything into one Researcher function that strings together all the functions we've written. Given a user's research topic, the Researcher will generate search queries, feed those queries to Exa Auto search, and finally use an LLM to synthesize the retrieved information. Three simple steps!

```TypeScript TypeScript theme={null}
 async function researcher(topic){
    console.log(`Starting research on topic: "${topic}"`);

    const searchQueries = await generateSearchQueries(topic, 3);
    console.log("Generated search queries:", searchQueries);

    const searchResults = await getSearchResults(searchQueries);
    console.log(`Found ${searchResults.length} search results. Here's the first one:`, searchResults[0]);

    console.log("Synthesizing report...");
    const report = await synthesizeReport(topic, searchResults);

    return report;
}
```

In just a couple lines of code, we've used Exa to go from a research topic to a valuable essay with up-to-date sources.

```TypeScript TypeScript theme={null}
async function runExamples() {
    console.log("Researching Sam Altman:");
    const samaReport = await researcher(SAMA_TOPIC);
    console.log(samaReport);

    console.log("\n\nResearching Renaissance Art:");
    const artReport = await researcher(ART_TOPIC);
    console.log(artReport);
}

// To use the researcher on the examples, simply call the runExamples() function:
runExamples();

// Or, to research a specific topic:
researcher("llama antibodies").then(console.log);
```

For a link to a complete, cleaned up version of this project that you can execute in your NodeJS environment, check out the [alternative JS-only version](https://github.com/exa-labs/exa-js/tree/master/examples/researcher/researcher.mjs).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt