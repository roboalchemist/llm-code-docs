# Source: https://pipedream.com/docs/workflows/building-workflows/code.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

export const PIPEDREAM_NODE_VERSION = '20';

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/2mQgJbl8FMA" title="Creating a code step in your Pipedream workflows" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

Pipedream comes with thousands of prebuilt [triggers](/workflows/building-workflows/triggers/) and [actions](/components/contributing/#actions) for [hundreds of apps](https://pipedream.com/apps). Often, these will be sufficient for building simple workflows.

But sometimes you need to run your own custom logic. You may need to make an API request to fetch additional metadata about the event, transform data into a custom format, or end the execution of a workflow early under some conditions. **Code steps let you do this and more**.

Code steps let you execute [Node.js v{PIPEDREAM_NODE_VERSION}](https://nodejs.org/) (JavaScript) code, Python, Go or even Bash right in a workflow.

Choose a language to get started:

<CardGroup>
  <Card img="https://mintcdn.com/pipedream/41C9r2QWAUyQNETK/images/31501070-icons8-nodejs_aax6wn.svg?fit=max&auto=format&n=41C9r2QWAUyQNETK&q=85&s=a81c1b709d6b025e255fcde5abebf87e" href="/workflows/building-workflows/code/nodejs/" width="48" height="48" data-path="images/31501070-icons8-nodejs_aax6wn.svg" />

  <Card img="https://mintcdn.com/pipedream/D7icXfHKCcJMcQDj/images/db9e32bd-python-logo-generic_k3o5w2.svg?fit=max&auto=format&n=D7icXfHKCcJMcQDj&q=85&s=81d362bad2ca54dfa6e88b91d2bbcc83" href="/workflows/building-workflows/code/python" width="518" height="153" data-path="images/db9e32bd-python-logo-generic_k3o5w2.svg" />

  <Card img="https://mintcdn.com/pipedream/D7icXfHKCcJMcQDj/images/d62cdcaa-Go-Logo_Blue_zhkchv.svg?fit=max&auto=format&n=D7icXfHKCcJMcQDj&q=85&s=13b59e6019c3925d557b1ddb8081f583" href="/workflows/building-workflows/code/go/" width="255" height="225" data-path="images/d62cdcaa-Go-Logo_Blue_zhkchv.svg" />

  <Card img="https://mintcdn.com/pipedream/WsDr_4XP4mFeehWe/images/61fcbb48-full_colored_dark_1_-svg_vyfnv7.svg?fit=max&auto=format&n=WsDr_4XP4mFeehWe&q=85&s=994f97ac01472fb1e4a7fe8415a0c0db" href="/workflows/building-workflows/code/bash/" width="300" height="125" data-path="images/61fcbb48-full_colored_dark_1_-svg_vyfnv7.svg" />
</CardGroup>

If you’d like to see another, specific language supported, please [let us know](https://pipedream.com/community).

Built with [Mintlify](https://mintlify.com).
