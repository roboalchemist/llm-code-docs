# Source: https://buildkite.com/docs/apis/webhooks/test-engine.md

# Source: https://buildkite.com/docs/test-engine.md

# Buildkite Test Engine

Scale out your testing across any framework with _Buildkite Test Engine_. Speed up builds with real-time flaky test management and intelligent test splitting. Drive accountability and get more out of your existing CI compute with performance insights and analytics.

Where [Buildkite Pipelines](/docs/pipelines) helps you automate your CI/CD pipelines, Test Engine helps you track and analyze the steps in these pipelines, by:

- Shipping code to production faster through test optimization.
- Working directly with Buildkite Pipelines, as well as other CI/CD applications.
- Identifying, fixing, and monitoring test performance.
- Tracking, improving, and monitoring test reliability.

<div style="max-width: 2594px"><div class="responsive-image-container"><img alt="Screenshot of test suite trend showing six metrics over the last day" src="/docs/assets/overview-CCO132lw.png" /></div></div>

## Get started

Run through the [Getting started](/docs/test-engine/getting-started) tutorial for a step-by-step guide on how to use Buildkite Test Engine.

If you're familiar with the basics, understand how to run your tests within your development project, and analyze and report on them through a Test Engine [_test suite_](/docs/test-engine/test-suites).

As part of configuring a test suite, you'll need to configure [test collection](/docs/test-engine/test-collection) for your development project. Do this by setting it up with the required Buildkite _test collectors_ for your project's testing frameworks (also known as _test runners_), which sends the required test data information to Test Engine:

<div class="ButtonGroup">
  <a class="Button Button--default" href="/docs/test-engine/test-collection/ruby-collectors#rspec-collector">:rspec: RSpec</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/ruby-collectors#minitest-collector">:ruby: minitest</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-jest">:jest: Jest</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-mocha">:mocha: Mocha</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-cypress">:cypress: Cypress</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-jasmine">:jasmine: Jasmine</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-playwright">:playwright: Playwright</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/javascript-collectors#configure-the-test-framework-vitest">:vitest: Vitest</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/swift-collectors">:swift: Swift</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/android-collectors">:android: Android</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/python-collectors">:pytest: pytest</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/golang-collectors">:golang: Go</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/importing-junit-xml">:junit: JUnit</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/dotnet-collectors">:dotnet: .NET</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/elixir-collectors">:elixir: Elixir</a>
  <a class="Button Button--default" href="/docs/test-engine/test-collection/rust-collectors">:rust: Rust</a>
</div>

If a Buildkite test collector is not available for one of these test runners, you can use [other test collection](/docs/test-engine/other-collectors) mechanisms instead.

## Core features

<section class="Tiles"><article class="TileItem"><h2 class="TileItem__title"><a class="TileItem__title-link" href="/docs/test-engine/test-suites#trends-and-analysis">Deep performance analysis</a></h2><p class="TileItem__desc">Automatic tracing across your test suite, deeply integrated with your programming language and test framework.</p><a class="TileItem__learn-more" href="/docs/test-engine/test-suites#trends-and-analysis">Learn more</a></article><article class="TileItem"><h2 class="TileItem__title"><a class="TileItem__title-link" href="/docs/test-engine/reduce-flaky-tests">Find and fix flaky tests</a></h2><p class="TileItem__desc">Quickly identify which tests are the most disruptive for your team, and get a head-start on fixing them.</p><a class="TileItem__learn-more" href="/docs/test-engine/reduce-flaky-tests">Learn more</a></article><article class="TileItem"><h2 class="TileItem__title"><a class="TileItem__title-link" href="/docs/test-engine/speed-up-builds-with-bktec">Reduce build times with bktec</a></h2><p class="TileItem__desc">Split tests evenly across agents to reduce overall pipeline build times, and skip and mute flaky tests.</p><a class="TileItem__learn-more" href="/docs/test-engine/speed-up-builds-with-bktec">Learn more</a></article></section>

> 📘 Data retention
> The execution data uploaded to Test Engine is stored in S3 and deleted after 120 days.

## API & references

Learn more about:

- Test Engine's APIs through the [REST API documentation](/docs/apis/rest-api), and related endpoints, starting with [test suites](/docs/apis/rest-api/test-engine/suites).
- The [Buildkite MCP server](/docs/apis/mcp-server) and its Test Engine-specific MCP [tools](/docs/apis/mcp-server/tools#available-mcp-tools-test-engine) and [toolsets](/docs/apis/mcp-server/tools/toolsets#available-toolsets).
- Test Engine's [webhooks](/docs/apis/webhooks/test-engine).
- Test Engine [glossary](/docs/test-engine/glossary) of important terms.
