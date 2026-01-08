# Semgrep Community Edition (CE) philosophy

Source: https://semgrep.dev/docs/contributing/semgrep-philosophy

- [](/docs/)- [Support &amp; resources](/docs/trophy-case)- What&#x27;s Semgrep- Semgrep CE philosophy- [Semgrep Community Edition](/docs/tags/semgrep-community-edition)Semgrep Community Edition (CE) philosophy
[Semgrep CE](https://github.com/semgrep/semgrep/) is a lightweight static analysis tool for many languages. It can find bug variants with patterns that look like source code.

As you think about contributing to Semgrep CE, consider these design principles that have guided Semgrep CE development so far:

- 
**Free****
“If a developer has to convince their manager to spend a few million dollars on advanced security tools each time they change jobs, the future is bleak.” — see our [introductory blog post](https://semgrep.dev/blog/2020/introducing-semgrep-and-r2c/) for more. It’s important to us (and the community) that Semgrep, Inc. is able to develop a sustainable business around Semgrep to support its development, but we strongly believe the tooling itself must always be free.

- 
**Open-source software**
Semgrep is [LGPL](https://tldrlegal.com/license/gnu-lesser-general-public-license-v2.1-(lgpl-2.1)) and powered not just by [Semgrep, Inc.](https://semgrep.dev/) but also by community of brilliant external contributors. We welcome feedback and contributions and strive to be a welcoming community for new developers.

- 
**Fast**
High sloc/sec scanning speed and low startup cost. We’ll never be as fast as ripgrep but we want to get as close as we can.

- 
**Code never leaves your machine**
Semgrep by default runs entirely locally (unless you set it up yourself in a server/client mode). Code never leaves your machine to be analyzed.

- 
**Support every programming language**
“If grep supports it, we will too!” This even includes those that aren’t thought of as programming languages, like Bash or Docker.

- 
**Run anywhere**
Semgrep is small (&lt;100 MB), has minimal runtime dependencies, and should be easily installable via your programming language or operating system package manager.

- 
**Keep easy things easy, and hard things possible.**
Using Semgrep to scan your code, and writing rules with which to scan, should be easy. Semgrep also smooths the process with delightful defaults and support every step of the way. But it’s also adaptable, and we welcome you using Semgrep in your own custom way. Hey, there are even [examples of scanning cat pictures out there](https://youtu.be/ybWB2Vf2V50?t=1182).

- 
**Beginner-friendly**
You shouldn’t need a PhD in program analysis, or even to understand what an AST is, to be effective with Semgrep. A novice programmer should be able to write their first Semgrep rule in 60 seconds.

- 
**Human-readable rules**
Rules should look like code and be easy to read and reason about—hopefully easier than if they were written in grep or a native linter.

- 
**Self-contained rule files**
You shouldn’t need an additional plugin, dependency, or internet access to run a YAML rule. It should just work.

- 
**Deterministic (implies reproducible, idempotent)**
Given the same input, Semgrep gives the same output.

- 
**Runs offline**
Semgrep can run without internet access so developers can write code from airplanes or beaches.

- 
**Rules are safe to run no matter where they came from**
Rules shouldn’t have the capability to run arbitrary code on your system, only to act as a function that produces a deterministic output message.

- 
**Single-file analysis**
To stay fast and limit complexity, Semgrep CE draws a line at crossing file boundaries during analysis. It loses the ability to detect certain complex cross-function (interprocedural) issues, but that’s an explicit tradeoff it makes.
Semgrep CE&#x27;s goal is to catch what a senior engineer would catch in code review: Semgrep isn’t designed to find a crazy issue that’s 300 calls from start to finish and evaded the team for 20 years. Instead, it’s designed for enforcing best-practices and automating the code review tasks that an excellent senior engineer would be capable of. For a discussion of why expressive creativity is better than a powerful engine, [see this excellent blog post by Devdatta Akhawe](https://devd.me/log/posts/static-analysis/).
As a corollary: if you design your codebase so that code in a file is safe today, it&#x27;s still safe after a colleague makes a change twenty function calls away in another file.

- 
**Designed to run while code is being written**
Semgrep is optimized for running in the IDE, Git commit hooks, or CI—not for at the tail-end of a release process.

- 
**A platform for program analysis**
We will expose stable internals so that researchers and engineers can develop novel program analysis work off of APIs like Semgrep’s generic AST.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Community Edition](/docs/tags/semgrep-community-edition)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/contributing/philosophy.md)Last updated on **Oct 29, 2025**