# Source: https://exa.ai/docs/examples/demo-exa-powered-writing-assistant.md

> **Documentation Index**
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Writing Assistant

[Click here to try the Exa-powered Writing Assistant](https://demo.exa.ai/writing)

[Click here to see the relevant GitHub repo and hosting instructions](https://github.com/exa-labs/exa-writing-assist)

## What this doc covers

* Live demo link for hands-on experience (above!)
* Overview of a real-time writing assistant using Exa and Claude
* Breakdown of Exa query prompt engineering and generative AI system prompt

## Demo overview

## High-level overview

This demo showcases a real-time writing assistant that uses Exa's search capabilities to provide relevant information and citations as a user writes. The system combines Exa's neural search with Anthropic's Claude AI model to generate contextually appropriate content and citations.

<img src="https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/77dd3c1-image.png?fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=71fdb665fe05eba5ea76e04a186d52d3" alt="Conceptual block diagram of how the writing assistant works" data-og-width="1660" width="1660" data-og-height="1660" height="1660" data-path="images/77dd3c1-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/77dd3c1-image.png?w=280&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=24a55ccdac2c7c9b70ba1bba9e488d9a 280w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/77dd3c1-image.png?w=560&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=836e162e10d13bdc1bb4ec7460e65f0f 560w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/77dd3c1-image.png?w=840&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=b96e1b3389aaf96ccef1c55db47636e3 840w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/77dd3c1-image.png?w=1100&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=86f7bd243f85f23508455c31c0078c96 1100w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/77dd3c1-image.png?w=1650&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=adb93218eb741b51466df3faeae052ff 1650w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/77dd3c1-image.png?w=2500&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=d30873c8c5082d9e93845a090a78b3d6 2500w" />

Conceptual block diagram of how the writing assistant works

## Exa prompting and query style

The Exa search is performed using a unique query style that appends the user's input with a prompt for continuation. Here's the relevant code snippet:

```JavaScript JavaScript theme={null}

let exaQuery = conversationState.length > 1000
    ? (conversationState.slice(-1000))+"\n\nIf you found the above interesting, here's another useful resource to read:"
    : conversationState+"\n\nIf you found the above interesting, here's another useful resource to read:"

let exaReturnedResults = await exa.searchAndContents(
    exaQuery,
    {
        type: "neural",
        numResults: 10,
        highlights: {
            maxCharacters: 500
        }
    }
)
```

**Key aspects of this query style:**

* **Continuation prompt:** The crucial post-pend "A helpful source to read so you can continue writing the above:"
  * This prompt is designed to find sources that can logically continue the user's writing when passed to an LLM to generate content.
  * It leverages Exa's ability to understand context and find semantically relevant results.
  * By framing the query as a request for continuation, it aligns with how people naturally share helpful links.
* **Length limitation:** It caps the query at 1000 characters to maintain relevance and continue writing just based on the last section of the text.

Note this prompt is not a hard and fast rule for this use-case - we encourage experimentation with query styles to get the best results for your specific use case. For instance, you could further constrain down to just research papers.

## Prompting Claude with Exa results

The Claude AI model is prompted with a carefully crafted system message and passed the above formatted Exa results. Here is an example system prompt:

```typescript TypeScript theme={null}
const systemPrompt = `You are an essay-completion bot that continues/completes a sentence given some input stub of an essay/prose. You only complete 1-2 SHORT sentence MAX. If you get an input of a half sentence or similar, DO NOT repeat any of the preceding text of the prose. THIS MEANS DO NOT INCLUDE THE STARTS OF INCOMPLETE SENTENCES IN YOUR RESPONSE. This is also the case when there is a spelling, punctuation, capitalization or other error in the starter stub - e.g.:

USER INPUT: pokemon is a
YOUR CORRECT OUTPUT: Japanese franchise created by Satoshi Tajiri.
NEVER/INCORRECT: Pokémon is a Japanese franchise created by Satoshi Tajiri.

USER INPUT: Once upon a time there
YOUR CORRECT OUTPUT: was a princess.
NEVER/INCORRECT: Once upon a time, there was a princess.

USER INPUT: Colonial england was a
YOUR CORRECT OUTPUT: time of great change and upheaval.
NEVER/INCORRECT: Colonial England was a time of great change and upheaval.

USER INPUT: The fog in san francisco
YOUR CORRECT OUTPUT: is a defining characteristic of the city's climate.
NEVER/INCORRECT: The fog in San Francisco is a defining characteristic of the city's climate.

USER INPUT: The fog in san francisco
YOUR CORRECT OUTPUT: is a defining characteristic of the city's climate.
NEVER/INCORRECT: The fog in San Francisco is a defining characteristic of the city's climate.

 Once you have made one citation, stop generating. BE PITHY. Where there is a full sentence fed in,
 you should continue on the next sentence as a generally good flowing essay would. You have a
 specialty in including content that is cited. Given the following two items, (1) citation context and
 (2) current essay writing, continue on the essay or prose inputting in-line citations in
 parentheses with the author's name, right after that followed by the relevant URL in square brackets.
 THEN put a parentheses around all of the above. If you cannot find an author (sometimes it is empty), use the generic name 'Source'.
 ample citation for you to follow the structure of: ((AUTHOR_X, 2021)[URL_X]).
 If there are more than 3 author names to include, use the first author name plus 'et al'`

```

This prompt ensures that:

* Claude will only do completions, not parrot back the user query like in a typical chat based scenario. Note the inclusion of multiple examples that demonstrate Claude should not reply back with the stub even if there are errors, like spelling or grammar, in the input text (which we found to be a common issue)
* We define the citation style and formatting. We also tell the bot went to collapse authors into 'et al' style citations, as some webpages have many authors

Once again, experimenting with this prompt is crucial to getting best results for your particular use case.

## Conclusion

This demo illustrates the power of combining Exa's advanced search capabilities with generative AI to create a writing assistant. By leveraging Exa's neural search and content retrieval features, the system can provide relevant, up-to-date information to any AI model, resulting in contextually appropriate content generation with citations.

This approach showcases how Exa can be integrated into AI-powered applications to enhance user experiences and productivity.

[Click here to try the Exa-powered Writing Assistant](https://demo.exa.ai/writing)
