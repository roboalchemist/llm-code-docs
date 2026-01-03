# Source: https://braintrust.dev/docs/cookbook/recipes/ReleaseNotes.md

# Generating release notes and hill-climbing to improve them

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/ReleaseNotes/ReleaseNotes.ipynb) by [Ankur Goyal](https://twitter.com/ankrgyl) on 2024-02-02</div>

This tutorial walks through how to automatically generate release notes for a repository using
the Github API and an LLM. Automatically generated release notes are tough to evaluate,
and you often don't have pre-existing benchmark data to evaluate them on.

To work around this, we'll use [hill climbing](https://braintrust.dev/docs/guides/evals#hill-climbing) to iterate on our prompt, comparing new results to previous experiments to see if we're making progress.

## Installing dependencies

To see a list of dependencies, you can view the accompanying [package.json](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/Github-Issues/package.json) file. Feel free to copy/paste snippets of this code to run in your environment, or use [tslab](https://github.com/yunabe/tslab) to run the tutorial in a Jupyter notebook.

## Downloading the data

We'll start by downloading some commit data from Github using the `octokit` SDK. We'll use the [Braintrust SDK](https://github.com/braintrustdata/braintrust-sdk) from November 2023 through January 2024.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const START_DATE = "2023-11-26";
const END_DATE = "2024-01-27";
const REPO_OWNER = "braintrustdata";
const REPO_NAME = "braintrust-sdk";
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Octokit } from "@octokit/rest";
import { GetResponseTypeFromEndpointMethod } from "@octokit/types";

type CommitsResponse = GetResponseTypeFromEndpointMethod<
  typeof octokit.rest.repos.listCommits
>;
type Commit = CommitsResponse["data"][number];

// Octokit.js
// https://github.com/octokit/core.js#readme
const octokit: Octokit = new Octokit({
  auth: process.env.GITHUB_ACCESS_TOKEN || "Your Github Access Token",
});

const commits: CommitsResponse = await octokit.rest.repos.listCommits({
  owner: REPO_OWNER,
  repo: REPO_NAME,
  since: START_DATE,
  until: END_DATE,
  per_page: 1000,
});

console.log("Retrieved", commits.data.length, "commits");
```

```
Retrieved 78 commits
```

Awesome, now let's bucket the commits into weeks.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import moment from "moment";

interface CommitInfo {
  url: string;
  html_url: string;
  sha: string;
  commit: {
    author: {
      name?: string;
      email?: string;
      date?: string;
    };
    message: string;
  };
}

const weeks: Record<string, CommitInfo[]> = {};
for (const commit of commits.data) {
  const week = moment(commit.commit.author.date, "YYYY-MM-DD")
    .startOf("week")
    .format("YYYY-MM-DD");
  weeks[week] = (weeks[week] || []).concat([
    // Simplify the commit data structure
    {
      sha: commit.sha,
      url: commit.url,
      html_url: commit.html_url,
      commit: {
        author: commit.commit.author,
        message: commit.commit.message,
      },
    },
  ]);
}

const sortedWeeks = Object.keys(weeks).sort((a, b) =>
  moment(a).diff(moment(b))
);
for (const week of sortedWeeks) {
  console.log(week, weeks[week].length);
  weeks[week].sort((a, b) =>
    moment(a.commit.author.date).diff(moment(b.commit.author.date))
  );
}
```

```
2023-11-26 7
2023-12-03 14
2023-12-10 3
2023-12-17 23
2023-12-24 2
2023-12-31 8
2024-01-07 8
2024-01-14 3
2024-01-21 10
```

## Generating release notes

Awesome! It looks like we have 9 solid weeks of data to work with. Let's take a look at the first week of data.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const firstWeek = weeks[sortedWeeks[0]];
for (const commit of firstWeek) {
  console.log("-----", commit.sha, "-----");
  console.log(commit.html_url);
  console.log(commit.commit.author.date);
  console.log(commit.commit.message);
  console.log("\n");
}
```

```
----- 86316b6622c23ef4f702289b8ada30ab50417f2d -----
https://github.com/braintrustdata/braintrust-sdk/commit/86316b6622c23ef4f702289b8ada30ab50417f2d
2023-11-28T06:57:57Z
Show --verbose warning at the end of the error list (#50)

Users were reporting that the \`--verbose\` flag is lost if it's at the
beginning of the list of errors. This change simply prints the
clarification at the end (and adds it to python)


----- 1ea8e1bb3de83cf0021af6488d06710aa6835d7b -----
https://github.com/braintrustdata/braintrust-sdk/commit/1ea8e1bb3de83cf0021af6488d06710aa6835d7b
2023-11-28T18:48:56Z
Bump autoevals and version


----- 322aba85bbf0b75948cc97ef750d405710a8c9f1 -----
https://github.com/braintrustdata/braintrust-sdk/commit/322aba85bbf0b75948cc97ef750d405710a8c9f1
2023-11-29T23:04:36Z
Small fixes (#51)

* Change built-in examples to use Eval framework
* Use \`evaluator\` instead of \`_evals[evalName]\` to access metadata. The
latter is not set if you're running Evals directly in a script.


----- ad0b18fd250e8e2b0e78f8405b4323a4abb3f7ce -----
https://github.com/braintrustdata/braintrust-sdk/commit/ad0b18fd250e8e2b0e78f8405b4323a4abb3f7ce
2023-11-30T17:32:02Z
Bump autoevals


----- 98de10b6e8b44e13f65010cbf170f2b448728c46 -----
https://github.com/braintrustdata/braintrust-sdk/commit/98de10b6e8b44e13f65010cbf170f2b448728c46
2023-12-01T17:51:31Z
Python eval framework: parallelize non-async components. (#53)

Fixes BRA-661


----- a1032508521f4967a5d1cdf9d1330afce97b7a4e -----
https://github.com/braintrustdata/braintrust-sdk/commit/a1032508521f4967a5d1cdf9d1330afce97b7a4e
2023-12-01T19:59:04Z
Bump version


----- 14599fe1d9c66e058095b318cb2c8361867eff76 -----
https://github.com/braintrustdata/braintrust-sdk/commit/14599fe1d9c66e058095b318cb2c8361867eff76
2023-12-01T21:01:39Z
Bump autoevals
```

### Building the prompt

Next, we'll try to generate release notes using `gpt-3.5-turbo` and a relatively simple prompt.

We'll start by initializing an OpenAI client and wrapping it with some Braintrust instrumentation. `wrapOpenAI`
is initially a no-op, but later on when we use Braintrust, it will help us capture helpful debugging information about the model's performance.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { wrapOpenAI } from "braintrust";
import { OpenAI } from "openai";

const client = wrapOpenAI(
  new OpenAI({
    apiKey: process.env.OPENAI_API_KEY || "Your OpenAI API Key",
  })
);

const MODEL: string = "gpt-3.5-turbo";
const SEED = 123;
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { ChatCompletionMessageParam } from "openai/resources";
import { traced } from "braintrust";

function serializeCommit(info: CommitInfo): string {
  return `SHA: ${info.sha}
AUTHOR: ${info.commit.author.name} <${info.commit.author.email}>
DATE: ${info.commit.author.date}
MESSAGE: ${info.commit.message}`;
}

function generatePrompt(commits: CommitInfo[]): ChatCompletionMessageParam[] {
  return [
    {
      role: "system",
      content: `You are an expert technical writer who generates release notes for the Braintrust SDK.
You will be provided a list of commits, including their message, author, and date, and you will generate
a full list of release notes, in markdown list format, across the commits. You should include the important
details, but if a commit is not relevant to the release notes, you can skip it.`,
    },
    {
      role: "user",
      content:
        "Commits: \n" + commits.map((c) => serializeCommit(c)).join("\n\n"),
    },
  ];
}

async function generateReleaseNotes(input: CommitInfo[]) {
  return traced(
    async (span) => {
      const response = await client.chat.completions.create({
        model: MODEL,
        messages: generatePrompt(input),
        seed: SEED,
      });
      return response.choices[0].message.content;
    },
    {
      name: "generateReleaseNotes",
    }
  );
}

const releaseNotes = await generateReleaseNotes(firstWeek);
console.log(releaseNotes);
```

```
Release Notes:

- Show --verbose warning at the end of the error list (#50):
  - Users were reporting that the \`--verbose\` flag is lost if it's at the
    beginning of the list of errors. This change simply prints the
    clarification at the end (and adds it to python).

- Small fixes (#51):
  - Change built-in examples to use Eval framework
  - Use \`evaluator\` instead of \`_evals[evalName]\` to access metadata. The
    latter is not set if you're running Evals directly in a script.

- Python eval framework: parallelize non-async components. (#53):
  - Fixes BRA-661
```

## Evaluating the initial prompt

Interesting, at a glance, it looks like the model is doing a decent job, but it's missing some key details like the version updates. Before we go any further, let's benchmark its performance
by writing an eval.

### Building a scorer

Let's start by implementing a scorer that can assess how well the new release notes capture the list of commits. To make the scoring function job's easy, we'll do a few tricks:

* Use gpt-4 instead of gpt-3.5-turbo
* Only present it the commit summaries, without the SHAs or author info, to reduce noise.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { LLMClassifierFromTemplate, Scorer, Score } from "autoevals";

const GRADER: string = "gpt-4";

const promptTemplate = `You are a technical writer who helps assess how effectively a product team generates
release notes based on git commits. You will look at the commit messages and determine if the release
notes sufficiently cover the changes.

Messages:

{{input}}


Release Notes:

{{output}}

Assess the quality of the release notes by selecting one of the following options. As you think through
the changes, list out which messages are not included in the release notes or info that is made up.

a) The release notes are excellent and cover all the changes.
b) The release notes capture some, but not all, of the changes.
c) The release notes include changes that are not in the commit messages.
d) The release notes are not useful and do not cover any changes.`;

const evaluator: Scorer<any, { input: string; output: string }> =
  LLMClassifierFromTemplate<{ input: string }>({
    name: "Comprehensiveness",
    promptTemplate,
    choiceScores: { a: 1, b: 0.5, c: 0.25, d: 0 },
    useCoT: true,
    model: GRADER,
  });

async function comprehensiveness({
  input,
  output,
}: {
  input: CommitInfo[];
  output: string;
}): Promise<Score> {
  return evaluator({
    input: input.map((c) => "-----\n" + c.commit.message).join("\n\n"),
    output,
  });
}

await comprehensiveness({ input: firstWeek, output: releaseNotes });
```

```
{
  name: 'Comprehensiveness',
  score: 0.5,
  metadata: {
    rationale: "The release notes cover the changes in commits 'Show --verbose warning at the end of the error list (#50)', 'Small fixes (#51)', and 'Python eval framework: parallelize non-async components. (#53)'.\n" +
      "The release notes do not mention the changes in the commits 'Bump autoevals and version', 'Bump autoevals', 'Bump version', and 'Bump autoevals'.\n" +
      'Therefore, the release notes capture some, but not all, of the changes.',
    choice: 'b'
  },
  error: undefined
}
```

Let's also score the output's writing quality. We want to make sure the release notes are well-written, concise, and do not contain repetitive content.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const promptTemplate = `You are a technical writer who helps assess the writing quality of release notes.

Release Notes:

{{output}}

Assess the quality of the release notes by selecting one of the following options. As you think through
the changes, list out which messages are not included in the release notes or info that is made up.

a) The release notes are clear and concise.
b) The release notes are not formatted as markdown/html, but otherwise are well written.
c) The release notes contain superfluous wording, for example statements like "let me know if you have any questions".
d) The release notes contain repeated information.
e) The release notes are off-topic to Braintrust's software and do not contain relevant information.`;

const evaluator: Scorer<any, { output: string }> = LLMClassifierFromTemplate({
  name: "WritingQuality",
  promptTemplate,
  choiceScores: { a: 1, b: 0.75, c: 0.5, d: 0.25, e: 0 },
  useCoT: true,
  model: GRADER,
});

async function writingQuality({ output }: { output: string }): Promise<Score> {
  return evaluator({
    output,
  });
}

await writingQuality({ output: releaseNotes });
```

```
{
  name: 'WritingQuality',
  score: 1,
  metadata: {
    rationale: 'The release notes are formatted correctly, using markdown for code and issue references.\n' +
      'There is no superfluous wording or repeated information in the release notes.\n' +
      'The content of the release notes is relevant to the software and describes changes made in the update.\n' +
      'Each change is explained clearly and concisely, making it easy for users to understand what has been updated or fixed.',
    choice: 'a'
  },
  error: undefined
}
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval } from "braintrust";

let lastExperiment = await Eval<CommitInfo[], string, unknown>(
  "Release Notes Cookbook",
  {
    data: Object.entries(weeks).map(([week, commits]) => ({
      input: commits,
      metadata: { week },
    })),
    task: generateReleaseNotes,
    scores: [comprehensiveness, writingQuality],
  }
);
```

```
{
  projectName: 'Release Notes Cookbook',
  experimentName: 'pr-hill-climbing-1707027712',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook/pr-hill-climbing-1707027712',
  comparisonExperimentName: undefined,
  scores: undefined,
  metrics: undefined
}
```

```
 ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ | Release Notes Cookbook                   |   9% | 9/100 datapoints
```

Wow! We're doing a great job with writing quality, but scored lower on comprehensiveness.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/initial-experiment.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e22445257d814442efcc49e38eb934de" alt="Initial experiment" data-og-width="1750" width="1750" data-og-height="776" height="776" data-path="cookbook/assets/ReleaseNotes/initial-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/initial-experiment.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=8180cdc79dc60a379fcc00e63c68b7e3 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/initial-experiment.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=d8f11b5dba36d431fd6e8868e2f3930d 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/initial-experiment.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=24d3e6f7cdee4b29cfab5a52a1da516a 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/initial-experiment.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6ece5f3954c619c806797ab3dda39c28 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/initial-experiment.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=543e36802c5d7c04f98cb0fc30fe40d8 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/initial-experiment.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e7b4be9c92f0c0cefa0cd8a13c0ea268 2500w" />

Braintrust makes it easy to see concrete examples of the failure cases. For example this grader mentions the new lazy login behavior is missing from the release notes:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-1.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=5fcef4a2f8360f8bfb62ed5f08756450" alt="Reason" data-og-width="2700" width="2700" data-og-height="1586" height="1586" data-path="cookbook/assets/ReleaseNotes/debug-reasons-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-1.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=dd236fd91ee8e7cfe46ab084a4fce2c0 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-1.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=d78b56f8a082e6d8d33b07b0702ab907 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-1.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=1edf1932aa22c7f2c43efcf59cfe021a 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-1.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=ea63d6e8d0da00693b446784604c5ed2 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-1.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=bd12ed3a08f4906c562637b79d05f54e 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-1.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6d0fbe56b9acc31584001098d172ed98 2500w" />

and if we click into the model's output, we can see that it's indeed missing:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-1.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e38613e6c4dfac59fadf06d3da1e8415" alt="Output" data-og-width="2684" width="2684" data-og-height="1574" height="1574" data-path="cookbook/assets/ReleaseNotes/debug-output-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-1.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b789e663c5044bedebd8cd90a40e5edd 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-1.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=96573b6aebd53e87b9a23f90754a5452 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-1.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=7c6a6218c0230c57ff77cfbba8e28fe5 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-1.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e28f306cba8bd9b11562d42447fc0cfb 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-1.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=04e4f2c2dc900ac5ce7d2466a6958665 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-1.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b79781b3f704400672417bad64694ab4 2500w" />

## Improving the prompt

Let's see if we can improve the model's performance by tweaking the prompt. Perhaps we were too eager about excluding irrelevant details in the original prompt. Let's tweak the wording to make sure it's comprehensive.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
function generatePrompt(commits: CommitInfo[]): ChatCompletionMessageParam[] {
  return [
    {
      role: "system",
      content: `You are an expert technical writer who generates release notes for the Braintrust SDK.
You will be provided a list of commits, including their message, author, and date, and you will generate
a full list of release notes, in markdown list format, across the commits. You should make sure to include
some information about each commit, without the commit sha, url, or author info.`,
    },
    {
      role: "user",
      content:
        "Commits: \n" + commits.map((c) => serializeCommit(c)).join("\n\n"),
    },
  ];
}

async function generateReleaseNotes(input: CommitInfo[]) {
  return traced(
    async (span) => {
      const response = await client.chat.completions.create({
        model: MODEL,
        messages: generatePrompt(input),
        seed: SEED,
      });
      return response.choices[0].message.content;
    },
    {
      name: "generateReleaseNotes",
    }
  );
}

await generateReleaseNotes(firstWeek);
```

```
Release Notes:

- Show --verbose warning at the end of the error list
  Users were reporting that the \`--verbose\` flag is lost if it's at the beginning of the list of errors. This change simply prints the clarification at the end (and adds it to python)

- Bump autoevals and version

- Small fixes
  - Change built-in examples to use Eval framework
  - Use \`evaluator\` instead of \`_evals[evalName]\` to access metadata. The latter is not set if you're running Evals directly in a script.

- Bump autoevals

- Python eval framework: parallelize non-async components
  Fixes BRA-661

- Bump version

- Bump autoevals
```

### Hill climbing

We'll use [hill climbing](https://www.braintrust.dev/docs/guides/evals#hill-climbing) to automatically use data from the previous experiment to compare to this one. Hill climbing is inspired by, but not exactly the same as, the term used in [numerical optimization](https://en.wikipedia.org/wiki/Hill_climbing). In the context of Braintrust, hill climbing is a way to iteratively improve a model's performance by comparing new experiments to previous ones. This is especially useful when you don't have a pre-existing benchmark to evaluate against.

Both the `Comprehensiveness` and `WritingQuality` scores evaluate the `output` against the `input`, without considering a comparison point. To take advantage of hill climbing, we'll add another scorer, `Summary`, which will compare the `output` against the `data` from the previous experiment. To learn more about the `Summary` scorer, check out its [prompt](https://github.com/braintrustdata/autoevals/blob/main/templates/summary.yaml).

To enable hill climbing, we just need to use `BaseExperiment()` as the `data` argument to `Eval()`. The `name` argument is optional, but since we know the exact experiment to compare to, we'll specify it. If you don't specify a name, Braintrust will automatically use the most recent ancestor on your main branch or the last experiment by timestamp as the comparison point.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { BaseExperiment } from "braintrust";
import { Summary } from "autoevals";

async function releaseSummary({
  input,
  output,
  expected,
}: {
  input: CommitInfo[];
  output: string;
  expected: string;
}): Promise<Score> {
  return Summary({
    input: input.map((c) => "-----\n" + c.commit.message).join("\n\n"),
    output,
    expected,
    model: GRADER,
    useCoT: true,
  });
}

lastExperiment = await Eval<CommitInfo[], string, unknown>(
  "Release Notes Cookbook",
  {
    data: BaseExperiment({ name: lastExperiment.experimentName }),
    task: generateReleaseNotes,
    scores: [comprehensiveness, writingQuality, releaseSummary],
  }
);
```

```
{
  projectName: 'Release Notes Cookbook',
  experimentName: 'pr-hill-climbing-1707027732',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook/pr-hill-climbing-1707027732',
  comparisonExperimentName: 'pr-hill-climbing-1707027712',
  scores: {
    WritingQuality: {
      name: 'WritingQuality',
      score: 0.75,
      diff: -0.25,
      improvements: 0,
      regressions: 3
    },
    Comprehensiveness: {
      name: 'Comprehensiveness',
      score: 0.8611111111111112,
      diff: 0.13888888888888895,
      improvements: 4,
      regressions: 2
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 0.3663333257039388,
      unit: 's',
      diff: -0.006666713290744364,
      improvements: 7,
      regressions: 2
    }
  }
}
```

```
 ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ | Release Notes Cookbook                   |   9% | 9/100 datapoints
```

```
{
  projectName: 'Release Notes Cookbook',
  experimentName: 'pr-hill-climbing-1707027732',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook/pr-hill-climbing-1707027732',
  comparisonExperimentName: 'pr-hill-climbing-1707027712',
  scores: {
    WritingQuality: {
      name: 'WritingQuality',
      score: 0.75,
      diff: -0.25,
      improvements: 0,
      regressions: 3
    },
    Comprehensiveness: {
      name: 'Comprehensiveness',
      score: 0.8611111111111112,
      diff: 0.13888888888888895,
      improvements: 4,
      regressions: 2
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 0.3663333257039388,
      unit: 's',
      diff: -0.006666713290744364,
      improvements: 7,
      regressions: 2
    }
  }
}
```

While we were able to boost the comprehensiveness score to 86%, it looks like we dropped the writing quality score by 25%.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/second-experiment.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=502c654da0c6b7139907c928c8fbe6ec" alt="Hill climbing experiment" data-og-width="2158" width="2158" data-og-height="1314" height="1314" data-path="cookbook/assets/ReleaseNotes/second-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/second-experiment.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=706c06ce491cb58663eeb3cbf3d78f00 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/second-experiment.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=101a0418f00c5df63da62b0c1b9ab064 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/second-experiment.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=5dbf4da1d6c0580e10af00133cb10dcc 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/second-experiment.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6645644ca62968ae839d351deeb6e5a3 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/second-experiment.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=15997a13856bcffe2ac49ae0fe628950 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/second-experiment.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=34bf89e50854633e4293469df8ccb778 2500w" />

Digging into a few examples, it appears that we're mentioning version bumps multiple times.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-2.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=36f40c2c2e195581334a2c9b83b417a2" alt="Reason" data-og-width="2702" width="2702" data-og-height="1946" height="1946" data-path="cookbook/assets/ReleaseNotes/debug-reasons-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-2.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=598eb1c123c73fdde8172f3cd51ea01f 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-2.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=155b3ec03fb7ac5c76dadef581177961 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-2.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b6765001f5e170b91f0b849783bcc7c8 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-2.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=3b714c98a2262d2421345b7405c9e1b2 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-2.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=8faf7b85db2250e28c4caa624068e3eb 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-reasons-2.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4296027290df646458d0c15477688d60 2500w" />

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-2.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=9d8fcb790186e04852a87f3c656a0673" alt="Output" data-og-width="2696" width="2696" data-og-height="1986" height="1986" data-path="cookbook/assets/ReleaseNotes/debug-output-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-2.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=df2e02c4015d03804b61e95fd24ea7cd 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-2.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=a35046c4b185a46ec9658c4e4eb7ead3 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-2.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=a728f94a61aed4daa3af4cfa4f845ae9 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-2.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f3d8321b411cb49d979b2ba358d240d4 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-2.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=109cced8214959c3220ac3978eafccef 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/debug-output-2.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=8c5b1090ada6229a480ad3b9a60c4382 2500w" />

## Iterating further on the prompt

Let's try to address this explicitly by tweaking the prompt. We'll continue to hill climb.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { ChatCompletionMessageParam } from "openai/resources";
import { traced } from "braintrust";

function generatePrompt(commits: CommitInfo[]): ChatCompletionMessageParam[] {
  return [
    {
      role: "system",
      content: `You are an expert technical writer who generates release notes for the Braintrust SDK.
You will be provided a list of commits, including their message, author, and date, and you will generate
a full list of release notes, in markdown list format, across the commits. You should make sure to include
some information about each commit, without the commit sha, url, or author info. However, do not mention
version bumps multiple times. If there are multiple version bumps, only mention the latest one.`,
    },
    {
      role: "user",
      content:
        "Commits: \n" + commits.map((c) => serializeCommit(c)).join("\n\n"),
    },
  ];
}

async function generateReleaseNotes(input: CommitInfo[]) {
  return traced(
    async (span) => {
      const response = await client.chat.completions.create({
        model: MODEL,
        messages: generatePrompt(input),
        seed: SEED,
      });
      return response.choices[0].message.content;
    },
    {
      name: "generateReleaseNotes",
    }
  );
}

const releaseNotes = await generateReleaseNotes(firstWeek);
console.log(releaseNotes);
```

```
Release Notes:

- Show --verbose warning at the end of the error list (#50): Users were reporting that the \`--verbose\` flag is lost if it's at the beginning of the list of errors. This change simply prints the clarification at the end (and adds it to python).

- Small fixes (#51):
  - Change built-in examples to use Eval framework.
  - Use \`evaluator\` instead of \`_evals[evalName]\` to access metadata. The latter is not set if you're running Evals directly in a script.

- Python eval framework: parallelize non-async components. (#53): Fixes BRA-661.

Please note that there were multiple version bumps and autoevals bumps.
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
lastExperiment = await Eval<CommitInfo[], string, unknown>(
  "Release Notes Cookbook",
  {
    data: BaseExperiment({ name: lastExperiment.experimentName }),
    task: generateReleaseNotes,
    scores: [comprehensiveness, writingQuality, releaseSummary],
  }
);
```

```
{
  projectName: 'Release Notes Cookbook',
  experimentName: 'pr-hill-climbing-1707027750',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook/pr-hill-climbing-1707027750',
  comparisonExperimentName: 'pr-hill-climbing-1707027732',
  scores: {
    Summary: {
      name: 'Summary',
      score: 0.4444444444444444,
      diff: -0.2222222222222222,
      improvements: 0,
      regressions: 2
    },
    WritingQuality: {
      name: 'WritingQuality',
      score: 0.9166666666666666,
      diff: 0.16666666666666663,
      improvements: 2,
      regressions: 0
    },
    Comprehensiveness: {
      name: 'Comprehensiveness',
      score: 0.7222222222222222,
      diff: -0.13888888888888895,
      improvements: 1,
      regressions: 3
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 0.3829999499850803,
      unit: 's',
      diff: 0.016666624281141518,
      improvements: 6,
      regressions: 3
    }
  }
}
```

```
 ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ | Release Notes Cookbook                   |   9% | 9/100 datapoints
```

```
{
  projectName: 'Release Notes Cookbook',
  experimentName: 'pr-hill-climbing-1707027750',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook/pr-hill-climbing-1707027750',
  comparisonExperimentName: 'pr-hill-climbing-1707027732',
  scores: {
    Summary: {
      name: 'Summary',
      score: 0.4444444444444444,
      diff: -0.2222222222222222,
      improvements: 0,
      regressions: 2
    },
    WritingQuality: {
      name: 'WritingQuality',
      score: 0.9166666666666666,
      diff: 0.16666666666666663,
      improvements: 2,
      regressions: 0
    },
    Comprehensiveness: {
      name: 'Comprehensiveness',
      score: 0.7222222222222222,
      diff: -0.13888888888888895,
      improvements: 1,
      regressions: 3
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 0.3829999499850803,
      unit: 's',
      diff: 0.016666624281141518,
      improvements: 6,
      regressions: 3
    }
  }
}
```

Sometimes hill climbing is not a linear process. It looks like while we've improved the writing quality, we've now dropped the comprehensiveness score as well as
overall summary quality.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/third-experiment.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4e05d84a61dcf677be8dcc300c5ce59e" alt="Hill climbing experiment" data-og-width="2082" width="2082" data-og-height="1076" height="1076" data-path="cookbook/assets/ReleaseNotes/third-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/third-experiment.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=a06ce3f06d0e3d227ce9b695aa68ed06 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/third-experiment.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=666875a85efe6584c037b842b840e70d 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/third-experiment.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=9916138de7ba2dc86653e8de5e68b3b6 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/third-experiment.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=33c1dac6617a34686afa5a5b8eb343aa 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/third-experiment.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=daefe7c1159e8adcd5ce07c78698ece5 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/third-experiment.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=7f509643bbb6ef0b51cb8f9bc33673e6 2500w" />

## Upgrading the model

Let's try upgrading the model to `gpt-4-1106-turbo` and see if that helps. Perhaps we're hitting the limits of `gpt-3.5-turbo`.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
async function generateReleaseNotes(input: CommitInfo[]) {
  return traced(
    async (span) => {
      const response = await client.chat.completions.create({
        model: "gpt-4-1106-preview",
        messages: generatePrompt(input),
        seed: SEED,
      });
      return response.choices[0].message.content;
    },
    {
      name: "generateReleaseNotes",
    }
  );
}
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
lastExperiment = await Eval<CommitInfo[], string, unknown>(
  "Release Notes Cookbook",
  {
    data: BaseExperiment({ name: lastExperiment.experimentName }),
    task: generateReleaseNotes,
    scores: [comprehensiveness, writingQuality, releaseSummary],
  }
);
```

```
{
  projectName: 'Release Notes Cookbook',
  experimentName: 'pr-hill-climbing-1707027779',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook/pr-hill-climbing-1707027779',
  comparisonExperimentName: 'pr-hill-climbing-1707027750',
  scores: {
    WritingQuality: {
      name: 'WritingQuality',
      score: 1,
      diff: 0.08333333333333337,
      improvements: 1,
      regressions: 0
    },
    Summary: {
      name: 'Summary',
      score: 0.7777777777777778,
      diff: 0.33333333333333337,
      improvements: 4,
      regressions: 1
    },
    Comprehensiveness: {
      name: 'Comprehensiveness',
      score: 0.8333333333333334,
      diff: 0.11111111111111116,
      improvements: 5,
      regressions: 2
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 0.3962223529815674,
      unit: 's',
      diff: 0.013222402996487082,
      improvements: 3,
      regressions: 6
    }
  }
}
```

```
 ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ | Release Notes Cookbook                   |   9% | 9/100 datapoints
```

```
{
  projectName: 'Release Notes Cookbook',
  experimentName: 'pr-hill-climbing-1707027779',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Release%20Notes%20Cookbook/pr-hill-climbing-1707027779',
  comparisonExperimentName: 'pr-hill-climbing-1707027750',
  scores: {
    WritingQuality: {
      name: 'WritingQuality',
      score: 1,
      diff: 0.08333333333333337,
      improvements: 1,
      regressions: 0
    },
    Summary: {
      name: 'Summary',
      score: 0.7777777777777778,
      diff: 0.33333333333333337,
      improvements: 4,
      regressions: 1
    },
    Comprehensiveness: {
      name: 'Comprehensiveness',
      score: 0.8333333333333334,
      diff: 0.11111111111111116,
      improvements: 5,
      regressions: 2
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 0.3962223529815674,
      unit: 's',
      diff: 0.013222402996487082,
      improvements: 3,
      regressions: 6
    }
  }
}
```

Wow, nice! It looks like we've made an improvement across the board.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/fourth-experiment.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c79ee722982907f132abc064a9d6f835" alt="Hill climbing experiment" data-og-width="2126" width="2126" data-og-height="1206" height="1206" data-path="cookbook/assets/ReleaseNotes/fourth-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/fourth-experiment.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=09030c7056f5efcbe2ba3e4b1ece2039 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/fourth-experiment.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=277d2191776c521bb0b66ecf60adbc2c 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/fourth-experiment.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=5bd68cb8aafbc5aaa64fd57b06b0957d 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/fourth-experiment.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=21e03840695850b2793297c031c76ef4 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/fourth-experiment.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f056a01d43fb621604abdf74a86cf2f2 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/fourth-experiment.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=874e7c4808610698e532df09e444ed0f 2500w" />

As a next step, we should dig into the example where we produced a worse summary than before, and hypothesize how to improve it.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/output_v_expected.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=306ccecfcbd543507e29f500c480e759" alt="Output vs Expected" data-og-width="1942" width="1942" data-og-height="962" height="962" data-path="cookbook/assets/ReleaseNotes/output_v_expected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/output_v_expected.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=105a828de46e0902bc20ee897f22ad20 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/output_v_expected.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c44f67a315412ca5556759224e49675c 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/output_v_expected.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=72bcfa9f798520698428ec9c33d5f1a8 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/output_v_expected.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=76d234214ddaf26b78639a8bb9eb48b0 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/output_v_expected.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e6a344a38ed6015c8ae9aabecc0a60cb 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ReleaseNotes/output_v_expected.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=d399feb783557d9fac773403110ad923 2500w" />

Happy evaluating!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt