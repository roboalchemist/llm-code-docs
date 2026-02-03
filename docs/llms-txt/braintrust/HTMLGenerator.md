# Source: https://braintrust.dev/docs/cookbook/recipes/HTMLGenerator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating beautiful HTML components

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/HTMLGenerator/HTMLGenerator.ipynb) by [Ankur Goyal](https://twitter.com/ankrgyl) on 2024-01-29</div>

In this example, we'll build an app that automatically generates HTML components, evaluates them, and captures user feedback. We'll use the feedback and evaluations to build up a dataset
that we'll use as a basis for further improvements.

## The generator

We'll start by using a very simple prompt to generate HTML components using `gpt-3.5-turbo`.

First, we'll initialize an openai client and wrap it with Braintrust's helper. This is a no-op until we start using
the client within code that is instrumented by Braintrust.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { OpenAI } from "openai";
import { wrapOpenAI } from "braintrust";

const openai = wrapOpenAI(
  new OpenAI({
    apiKey: process.env.OPENAI_API_KEY || "Your OPENAI_API_KEY",
  })
);
```

This code generates a basic prompt:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { ChatCompletionMessageParam } from "openai/resources";

function generateMessages(input: string): ChatCompletionMessageParam[] {
  return [
    {
      role: "system",
      content: `You are a skilled design engineer
who can convert ambiguously worded ideas into beautiful, crisp HTML and CSS.
Your designs value simplicity, conciseness, clarity, and functionality over
complexity.

You generate pure HTML with inline CSS, so that your designs can be rendered
directly as plain HTML. Only generate components, not full HTML pages. Do not
create background colors.

Users will send you a description of a design, and you must reply with HTML,
and nothing else. Your reply will be directly copied and rendered into a browser,
so do not include any text. If you would like to explain your reasoning, feel free
to do so in HTML comments.`,
    },
    {
      role: "user",
      content: input,
    },
  ];
}

JSON.stringify(
  generateMessages("A login form for a B2B SaaS product."),
  null,
  2
);
```

```
[
  {
    "role": "system",
    "content": "You are a skilled design engineer\nwho can convert ambiguously worded ideas into beautiful, crisp HTML and CSS.\nYour designs value simplicity, conciseness, clarity, and functionality over\ncomplexity.\n\nYou generate pure HTML with inline CSS, so that your designs can be rendered\ndirectly as plain HTML. Only generate components, not full HTML pages. Do not\ncreate background colors.\n\nUsers will send you a description of a design, and you must reply with HTML,\nand nothing else. Your reply will be directly copied and rendered into a browser,\nso do not include any text. If you would like to explain your reasoning, feel free\nto do so in HTML comments."
  },
  {
    "role": "user",
    "content": "A login form for a B2B SaaS product."
  }
]
```

Now, let's run this using `gpt-3.5-turbo`. We'll also do a few things that help us log & evaluate this function later:

* Wrap the execution in a `traced` call, which will enable Braintrust to log the inputs and outputs of the function when we run it in production or in evals
* Make its signature accept a single `input` value, which Braintrust's `Eval` function expects
* Use a `seed` so that this test is reproduceable

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { traced } from "braintrust";
async function generateComponent(input: string) {
  return traced(
    async (span) => {
      const response = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: generateMessages(input),
        seed: 101,
      });
      const output = response.choices[0].message.content;
      span.log({ input, output });
      return output;
    },
    {
      name: "generateComponent",
    }
  );
}
```

### Examples

Let's look at a few examples!

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await generateComponent("Do a reset password form inside a card.");
```

```
<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
  <div style="width: 300px; padding: 20px; border: 1px solid #ccc; border-radius: 5px;">
    <h2 style="text-align: center;">Reset Password</h2>
    <form style="display: flex; flex-direction: column;">
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" style="margin-bottom: 10px; padding: 5px;">
      <button type="submit" style="background-color: #4CAF50; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer;">Reset Password</button>
    </form>
  </div>
</div>
```

To make this easier to validate, we'll use [puppeteer](https://pptr.dev/) to render the HTML as a screenshot.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import puppeteer from "puppeteer";
import * as tslab from "tslab";

async function takeFullPageScreenshotAsUInt8Array(htmlContent) {
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  await page.setContent(htmlContent);

  const screenshotBuffer = await page.screenshot();
  const uint8Array = new Uint8Array(screenshotBuffer);

  await browser.close();
  return uint8Array;
}

async function displayComponent(input: string) {
  const html = await generateComponent(input);
  const img = await takeFullPageScreenshotAsUInt8Array(html);
  tslab.display.png(img);
  console.log(html);
}

await displayComponent("Do a reset password form inside a card.");
```

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_11.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=eaa5de0e3fd53fefe47b4356aa2a8941" alt="Cell 11" data-og-width="800" width="800" data-og-height="600" height="600" data-path="cookbook/assets/HTMLGenerator/_generated_11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_11.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=5023ca13e3ec1f5ba6e912bd49b2143c 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_11.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9b23c5fcc65f20c99e74d5d9426af8c7 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_11.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=bc57f71af83947d9253dab6e76153b6f 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_11.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=293027cbb3645870aad91ffdd7d5e552 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_11.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7213dbbd0d5e0ea21cbf9c75725dc9b5 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_11.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e707deb0016be857c6a85e04b6a41f79 2500w" />

<br />

```
<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
  <div style="width: 300px; padding: 20px; border: 1px solid #ccc; border-radius: 5px;">
    <h2 style="text-align: center;">Reset Password</h2>
    <form style="display: flex; flex-direction: column;">
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" style="margin-bottom: 10px; padding: 5px;">
      <button type="submit" style="background-color: #4CAF50; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer;">Reset Password</button>
    </form>
  </div>
</div>
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await displayComponent("Create a profile page for a social network.");
```

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_8.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3a31dd40054a751d107154cd93abd703" alt="Cell 8" data-og-width="800" width="800" data-og-height="600" height="600" data-path="cookbook/assets/HTMLGenerator/_generated_8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_8.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7d00bb1617a2fa1bb3057a1d03ad2f2f 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_8.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=93328900afa65519e1b4d729c83b5290 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_8.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=13e8c9eb47ac547614fdd4bc927e0925 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_8.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=096dbdf52c078d7ef33af310eb29ac33 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_8.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=f706f0c3c2a08c91722822908c382054 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_8.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7947dbed33c456288929bbbfe1122662 2500w" />

<br />

```
<!DOCTYPE html>
<html>

<head>
    <style>
        .profile {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-bottom: 20px;
        }

        .profile-name {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .profile-bio {
            font-size: 18px;
            text-align: center;
        }

        .profile-stats {
            display: flex;
            justify-content: space-between;
            width: 200px;
            margin-top: 20px;
        }

        .profile-stats-item {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .profile-stats-item-value {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .profile-stats-item-label {
            font-size: 16px;
        }
    </style>
</head>

<body>
    <div class="profile">
        <img class="profile-img" src="profile-picture.jpg" alt="Profile Picture">
        <div class="profile-name">John Doe</div>
        <div class="profile-bio">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ut turpis
            hendrerit, ullamcorper velit in, iaculis arcu.</div>
        <div class="profile-stats">
            <div class="profile-stats-item">
                <div class="profile-stats-item-value">500</div>
                <div class="profile-stats-item-label">Followers</div>
            </div>
            <div class="profile-stats-item">
                <div class="profile-stats-item-value">250</div>
                <div class="profile-stats-item-label">Following</div>
            </div>
            <div class="profile-stats-item">
                <div class="profile-stats-item-value">1000</div>
                <div class="profile-stats-item-label">Posts</div>
            </div>
        </div>
    </div>
</body>

</html>
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await displayComponent(
  "Logs viewer for a cloud infrastructure management tool. Heavy use of dark mode."
);
```

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_10.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3fe18370ff5949d14b6cfa84e6cc35f8" alt="Cell 10" data-og-width="800" width="800" data-og-height="600" height="600" data-path="cookbook/assets/HTMLGenerator/_generated_10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_10.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3c18c680f59bb4cd16abd76477236de8 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_10.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=226a324d37046c3cec756ad24064ee3d 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_10.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=dec80a134080e649149bf12783fc060c 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_10.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=2ad80c1962635397db662af6f67f6de6 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_10.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=53b840011ce5530cc6c08bc446c6eb0e 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_10.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b1364a6cf37f27707c22c21f36aa89a5 2500w" />

<br />

```
<!DOCTYPE html>
<html>
<head>
<style>
    /* Overall styling */
    body {
        font-family: Arial, sans-serif;
        color: #fff;
        background-color: #000;
    }

    /* Header styling */
    .header {
        background-color: #333;
        padding: 20px;
        text-align: center;
    }

    .header h1 {
        margin: 0;
        font-size: 24px;
    }

    /* Logs viewer styling */
    .logs-viewer {
        padding: 20px;
    }

    .log-entry {
        margin-bottom: 10px;
    }

    .log-entry .timestamp {
        color: #ccc;
        font-size: 14px;
        margin-right: 10px;
    }

    .log-entry .message {
        font-size: 16px;
    }
</style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <h1>Logs Viewer</h1>
    </div>

    <!-- Logs Viewer -->
    <div class="logs-viewer">
        <div class="log-entry">
            <span class="timestamp">12:30 PM</span>
            <span class="message">Info: Cloud instance created successfully</span>
        </div>
        <div class="log-entry">
            <span class="timestamp">12:45 PM</span>
            <span class="message">Warning: High CPU utilization on instance #123</span>
        </div>
        <div class="log-entry">
            <span class="timestamp">01:00 PM</span>
            <span class="message">Error: Connection lost to the database server</span>
        </div>
        <!-- Add more log entries here -->
    </div>
</body>
</html>
```

## Scoring the results

It looks like in a few of these examples, the model is generating a full HTML page, instead of a component as we requested. This is something we can evaluate, to ensure that it does not happen!

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const containsHTML = (s) => /<(html|body)>/i.test(s);
containsHTML(
  await generateComponent(
    "Logs viewer for a cloud infrastructure management tool. Heavy use of dark mode."
  )
);
```

```
true
```

Now, let's update our function to compute this score. Let's also keep track of requests and their ids, so that we can provide user feedback. Normally you would store these in a database, but for demo purposes, a global dictionary should suffice.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// Normally you would store these in a database, but for this demo we'll just use a global variable.
let requests = {};

async function generateComponent(input: string) {
  return traced(
    async (span) => {
      const response = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: generateMessages(input),
        seed: 101,
      });
      const output = response.choices[0].message.content;
      requests[input] = span.id;
      span.log({
        input,
        output,
        scores: { isComponent: containsHTML(output) ? 0 : 1 },
      });
      return output;
    },
    {
      name: "generateComponent",
    }
  );
}
```

## Logging results

To enable logging to Braintrust, we just need to initialize a logger. By default, a logger is automatically marked as the current, global logger, and once initialized will be picked up by `traced`.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { initLogger } from "braintrust";

const logger = initLogger({
  projectName: "Component generator",
  apiKey: process.env.BRAINTRUST_API_KEY || "Your BRAINTRUST_API_KEY",
});
```

Now, we'll run the `generateComponent` function on a few examples, and see what the results look like in Braintrust.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const inputs = [
  "A login form for a B2B SaaS product.",
  "Create a profile page for a social network.",
  "Logs viewer for a cloud infrastructure management tool. Heavy use of dark mode.",
];

for (const input of inputs) {
  await generateComponent(input);
}

console.log(`Logged ${inputs.length} requests to Braintrust.`);
```

```
Logged 3 requests to Braintrust.
```

### Viewing the logs in Braintrust

Once this runs, you should be able to see the raw inputs and outputs, along with their scores in the project.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/component-generator-logs.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=dcee6b8c6e741936c37dd0a6d180440d" alt="component_generator_logs.png" data-og-width="2111" width="2111" data-og-height="1315" height="1315" data-path="cookbook/assets/HTMLGenerator/component-generator-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/component-generator-logs.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=786eb43218c04d24f61c42a5e59bf2f9 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/component-generator-logs.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b8748541e3a43244171b516c1454f059 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/component-generator-logs.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e186670c50bbef274ce293e898315508 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/component-generator-logs.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=eaab57504cc2271adb4cfacd038e2009 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/component-generator-logs.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=431a4404e887ed72d7bf7038df093bd8 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/component-generator-logs.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=da620181429c0c58f8aaf5f2f9946bea 2500w" />

### Capturing user feedback

Let's also track user ratings for these components. Separate from whether or not they're formatted as HTML, it'll be useful to track whether users like the design.

To do this, [configure a new score in the project](/annotate/human-review#configuring-human-review). Let's call it "User preference" and make it a 👍/👎.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/score-config.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9e1421b5b11bf273f2288e7fc65cd372" alt="Score configuration" data-og-width="877" width="877" data-og-height="740" height="740" data-path="cookbook/assets/HTMLGenerator/score-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/score-config.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=8c683ca2e88106d5a0d18322252a73ce 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/score-config.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=fc6bd39d3365a4e150d52a0c70e27450 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/score-config.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=ab03a1dc2bce4353937359b05e4e199e 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/score-config.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=20fd479679911c2f08edbf76ccdee90d 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/score-config.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=df80ebaa06593a0641fe19f3f6b659f2 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/score-config.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=29d8d51d302e9c23877d9ed3430fd342 2500w" />

Once you create a human review score, you can evaluate results directly in the Braintrust UI, or capture end-user feedback. Here, we'll pretend to capture end-user feedback. Personally, I liked the login form and logs viewer, but not the profile page. Let's record feedback accordingly.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// Along with scores, you can optionally log user feedback as comments, for additional color.
logger.logFeedback({
  id: requests["A login form for a B2B SaaS product."],
  scores: { "User preference": 1 },
  comment: "Clean, simple",
});
logger.logFeedback({
  id: requests["Create a profile page for a social network."],
  scores: { "User preference": 0 },
});
logger.logFeedback({
  id: requests[
    "Logs viewer for a cloud infrastructure management tool. Heavy use of dark mode."
  ],
  scores: { "User preference": 1 },
  comment:
    "No frills! Would have been nice to have borders around the entries.",
});
```

As users provide feedback, you'll see the updates they make in each log entry.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/feedback-comments.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=770197749c5196c6c3829cecb042612b" alt="Feedback log" data-og-width="2117" width="2117" data-og-height="1319" height="1319" data-path="cookbook/assets/HTMLGenerator/feedback-comments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/feedback-comments.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7ce4594ac017f58d7b76e2fea025bb14 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/feedback-comments.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=d4a16f29c1cf45f3d0cbe7b50680e59b 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/feedback-comments.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7b6b8cfce93a42390b1ee56349b82eef 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/feedback-comments.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=8ffa97112fe53ac0b9f624581c9e6ff3 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/feedback-comments.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=f61698d89e5dce513384151e18e91a21 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/feedback-comments.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9fc93b9488238f757c93df9739427c19 2500w" />

## Creating a dataset

Now that we've collected some interesting examples from users, let's collect them into a dataset, and see if we can improve the `isComponent` score.

In the Braintrust UI, select the examples, and add them to a new dataset called "Interesting cases".

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/create-new-dataset.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=d953be355f16b20d37ad3990c70d4faa" alt="Interesting cases" data-og-width="928" width="928" data-og-height="538" height="538" data-path="cookbook/assets/HTMLGenerator/create-new-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/create-new-dataset.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=ab2431c9d255a03bc99ad28712d96861 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/create-new-dataset.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3b444b28a1a120d32004ad86357c4185 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/create-new-dataset.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=a0b57350c1ff6b32fb608a4df7d6e14d 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/create-new-dataset.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=957e4bfa3bb52dd2337b3eaaef0fdc1c 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/create-new-dataset.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=6f7d70f43ce7955bb948d2aa5f6d60a3 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/create-new-dataset.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=511fa45d10c7d9099a9a0f0fc9db1577 2500w" />

Once you create the dataset, it should look something like this:

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/dataset.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=ca2a6b0836f3d6ae48b31cb8f030e46c" alt="Dataset" data-og-width="2956" width="2956" data-og-height="1434" height="1434" data-path="cookbook/assets/HTMLGenerator/dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/dataset.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=a5dfa15bbf22030acc156ce5e27f7f5c 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/dataset.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=4dfd870504ece2ba09ea01e02899b862 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/dataset.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=4895f2883a37eec586db45c8aa106f85 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/dataset.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7efc15222940ec2116a7d7246df63d85 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/dataset.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=32d1ebfed4f50d9755fa5bc709515e93 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/dataset.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=41417cd797dfcfb4d5b40aebdfd2cd3c 2500w" />

## Evaluating

Now that we have a dataset, let's evaluate the `isComponent` function on it. We'll use the `Eval` function, which takes a dataset and a function, and evaluates the function on each example in the dataset.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval, initDataset } from "braintrust";

await Eval("Component generator", {
  data: async () => {
    const dataset = initDataset("Component generator", {
      dataset: "Interesting cases",
    });
    const records = [];
    for await (const { input } of dataset.fetch()) {
      records.push({ input });
    }
    return records;
  },
  task: generateComponent,
  // We do not need to add any additional scores, because our
  // generateComponent() function already computes `isComponent`
  scores: [],
});
```

Once the eval runs, you'll see a summary which includes a link to the experiment. As expected, only one of the three outputs contains HTML, so the score is 33.3%. Let's also label user preference for this experiment, so we can track aesthetic taste manually. For simplicity's sake, we'll use the same labeling as before.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/initial-experiment.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=d7e0b6ee98958d68ad3b9008028b4e40" alt="Initial experiment" data-og-width="2127" width="2127" data-og-height="1075" height="1075" data-path="cookbook/assets/HTMLGenerator/initial-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/initial-experiment.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=6812d72cc8dda92e561589b898de9728 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/initial-experiment.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=5dae56f8d734abf4aab4f7ebffcf0f94 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/initial-experiment.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b65e316c024d6affb2e23c6e21552ec3 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/initial-experiment.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=382e7c8e92752946db62edb282a3591c 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/initial-experiment.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=8261f1e479ee7586af0e53463b101448 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/initial-experiment.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=959b3889b5bd938676aadf2b002f3925 2500w" />

### Improving the prompt

Next, let's try to tweak the prompt to stop rendering full HTML pages.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
function generateMessages(input: string): ChatCompletionMessageParam[] {
  return [
    {
      role: "system",
      content: `You are a skilled design engineer
who can convert ambiguously worded ideas into beautiful, crisp HTML and CSS.
Your designs value simplicity, conciseness, clarity, and functionality over
complexity.

You generate pure HTML with inline CSS, so that your designs can be rendered
directly as plain HTML. Only generate components, not full HTML pages. If you
need to add CSS, you can use the "style" property of an HTML tag. You cannot use
global CSS in a <style> tag.

Users will send you a description of a design, and you must reply with HTML,
and nothing else. Your reply will be directly copied and rendered into a browser,
so do not include any text. If you would like to explain your reasoning, feel free
to do so in HTML comments.`,
    },
    {
      role: "user",
      content: input,
    },
  ];
}

JSON.stringify(
  generateMessages("A login form for a B2B SaaS product."),
  null,
  2
);
```

```
[
  {
    "role": "system",
    "content": "You are a skilled design engineer\nwho can convert ambiguously worded ideas into beautiful, crisp HTML and CSS.\nYour designs value simplicity, conciseness, clarity, and functionality over\ncomplexity.\n\nYou generate pure HTML with inline CSS, so that your designs can be rendered\ndirectly as plain HTML. Only generate components, not full HTML pages. If you\nneed to add CSS, you can use the \"style\" property of an HTML tag. You cannot use\nglobal CSS in a <style> tag.\n\nUsers will send you a description of a design, and you must reply with HTML,\nand nothing else. Your reply will be directly copied and rendered into a browser,\nso do not include any text. If you would like to explain your reasoning, feel free\nto do so in HTML comments."
  },
  {
    "role": "user",
    "content": "A login form for a B2B SaaS product."
  }
]
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await displayComponent(
  "Logs viewer for a cloud infrastructure management tool. Heavy use of dark mode."
);
```

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_19.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b4a4dba643562553d2111b1d135901d5" alt="Cell 19" data-og-width="800" width="800" data-og-height="600" height="600" data-path="cookbook/assets/HTMLGenerator/_generated_19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_19.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=03ae5305dc2425db0a1008952384069b 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_19.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=a4778728698b70c87f17869f6df6e3d1 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_19.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e4eeea77204428638dc35445e3942f5f 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_19.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=f2bc1775fc6e761cad581bdc2284d3df 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_19.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=05e663bc250084983dfc88ff23d189db 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/_generated_19.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e42214262081dccb77d7ba1b01826615 2500w" />

<br />

```


<div>
  <div style="background-color: #252525; color: #FFFFFF; padding: 10px;">
    <h1 style="margin: 0;">Logs Viewer</h1>
  </div>
  <div style="background-color: #343434; color: #FFFFFF; padding: 10px;">
    <pre style="margin: 0;">[Timestamp] [Service Name] [Log Level] [Message]</pre>
    <pre style="margin: 0;">[Timestamp] [Service Name] [Log Level] [Message]</pre>
    <pre style="margin: 0;">[Timestamp] [Service Name] [Log Level] [Message]</pre>
    <!-- Repeat as needed for more logs -->
  </div>
</div>
```

Nice, it looks like it no longer generates an `html` tag. Let's re-run the `Eval` (copy/pasted below for convenience).

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval, initDataset } from "braintrust";

await Eval("Component generator", {
  data: async () => {
    const dataset = initDataset("Component generator", {
      dataset: "Interesting cases",
    });
    const records = [];
    for await (const { input } of dataset.fetch()) {
      records.push({ input });
    }
    return records;
  },
  task: generateComponent,
  scores: [], // We do not need to add any additional scores, because our generateComponent() function already computes isComponent
});
console.log("Done!");
```

Nice! We are now generating components without the `<html>` tag.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/next-experiment.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=d03d7f4b5fb78ea9b10f9cab0a00da9d" alt="Next experiment" data-og-width="2129" width="2129" data-og-height="1062" height="1062" data-path="cookbook/assets/HTMLGenerator/next-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/next-experiment.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=ec45c1557773ee2cf7305a946d953f48 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/next-experiment.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=6e508921c8c842cb99092e33f0c9e938 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/next-experiment.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=cc4fb96ae71bd22c76b591f95e2356c6 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/next-experiment.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e6e000acd8861af2476ff5ffecc7484b 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/next-experiment.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3dfca02adf80c6616056412b2ce8d67b 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/HTMLGenerator/next-experiment.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=318b206bd23c05ee3556786eea344d0e 2500w" />

## Where to go from here

Now that we've run another experiment, a good next step would be to rate the new components and make sure we did not suffer a serious aesthetic regression. You can also collect more user examples, add them to the dataset, and re-evaluate to better assess how well your application works. Happy evaluating!
