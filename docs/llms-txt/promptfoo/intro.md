# Intro

`promptfoo` is an [open-source](https://github.com/promptfoo/promptfoo) CLI and library for evaluating and red-teaming LLM apps.

With promptfoo, you can:

- **Build reliable prompts, models, and RAGs** with benchmarks specific to your use-case
- **Secure your apps** with automated [red teaming](/docs/red-team/) and pentesting
- **Speed up evaluations** with caching, concurrency, and live reloading
- **Score outputs automatically** by defining [metrics](/docs/configuration/expected-outputs/)
- Use as a [CLI](/docs/usage/command-line/), [library](/docs/usage/node-package/), or in [CI/CD](/docs/integrations/github-action/)
- Use OpenAI, Anthropic, Azure, Google, HuggingFace, open-source models like Llama, or integrate custom API providers for [any LLM API](/docs/providers/)

The goal: **test-driven LLM development**, not trial-and-error.

**Get Started:**

- [**Red teaming**](/docs/red-team/quickstart/) - Scan for security vulnerabilities and compliance risks
- [**Evaluations**](/docs/getting-started/) - Test quality and accuracy of your prompts, models, and applications

promptfoo produces matrix views that let you quickly evaluate outputs across many prompts.

Here's an example of a side-by-side comparison of multiple prompts and inputs:

![Side-by-side evaluation of LLM prompt quality](https://github.com/promptfoo/promptfoo/assets/310310/ce5a7817-da82-4484-b26d-32474f1cabc5)

It works on the command line too.

![LLM prompt quality evaluation with PASS/FAIL expectations](https://user-images.githubusercontent.com/310310/236690475-b05205e8-483e-4a6d-bb84-41c2b06a1247.png)

Promptfoo also produces high-level vulnerability and risk reports:

![gen ai red team](/assets/images/riskreport-1@2x-4c0fbea80c8816901144bc951702ed91.png)

## Why choose promptfoo?

There are many different ways to evaluate prompts. Here are some reasons to consider promptfoo:

- **Developer friendly**: promptfoo is fast, with quality-of-life features like live reloads and caching.
- **Battle-tested**: Originally built for LLM apps serving over 10 million users in production. Our tooling is flexible and can be adapted to many setups.
- **Simple, declarative test cases**: Define evals without writing code or working with heavy notebooks.
- **Language agnostic**: Use Python, Javascript, or any other language.
- **Share & collaborate**: Built-in share functionality & web viewer for working with teammates.
- **Open-source**: LLM evals are a commodity and should be served by 100% open-source projects with no strings attached.
- **Private**: This software runs completely locally. The evals run on your machine and talk directly with the LLM.

## Workflow and philosophy

Test-driven prompt engineering is much more effective than trial-and-error.

[Serious LLM development requires a systematic approach to prompt engineering](https://www.ianww.com/blog/2023/05/21/prompt-engineering-framework). Promptfoo streamlines the process of evaluating and improving language model performance.

1. **Define test cases**: Identify core use cases and failure modes. Prepare a set of prompts and test cases that represent these scenarios.
2. **Configure evaluation**: Set up your evaluation by specifying prompts, test cases, and API providers.
3. **Run evaluation**: Use the command-line tool or library to execute the evaluation and record model outputs for each prompt.
4. **Analyze results**: Set up automatic requirements, or review results in a structured format/web UI. Use these results to select the best model and prompt for your use case.
5. **Feedback loop**: As you gather more examples and user feedback, continue to expand your test cases.

![llm evaluation flow](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAwIDQ1MCI+CiAgPCEtLSBCYWNrZ3JvdW5kIC0tPgogIDxyZWN0IHdpZHRoPSIxMDAwIiBoZWlnaHQ9IjQ1MCIgZmlsbD0iI2Y4ZjlmYSIvPgogIAogIDwhLS0gRGVmaW5pdGlvbnMgZm9yIHJldXNhYmxlIGVsZW1lbnRzIC0tPgogIDxkZWZzPgogICAgPCEtLSBBcnJvdyBtYXJrZXJzIC0tPgogICAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iMTAiIG1hcmtlckhlaWdodD0iNyIgcmVmWD0iOSIgcmVmWT0iMy41IiBvcmllbnQ9ImF1dG8iPgogICAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgMTAgMy41LCAwIDciIGZpbGw9IiM0YTU1NjgiLz4KICAgIDwvbWFya2VyPgogICAgPCEtLSBCb3ggc2hhZG93IC0tPgogICAgPGZpbHRlciBpZD0ic2hhZG93IiB4PSItMjAlIiB5PSItMjAlIiB3aWR0aD0iMTQwJSIgaGVpZ2h0PSIxNDAlIj4KICAgICAgPGZlR2F1c3NpYW5CbHVyIGluPSJTb3VyY2VBbHBoYSIgc3RkRGV2aWF0aW9uPSIzIi8+CiAgICAgIDxmZU9mZnNldCBkeD0iMiIgZHk9IjIiLz4KICAgICAgPGZlQ29tcG9uZW50VHJhbnNmZXI+CiAgICAgICAgPGZlRnVuY0EgdHlwZT0ibGluZWFyIiBzbG9wZT0iMC4zIi8+CiAgICAgIDwvZmVDb21wb25lbnRUcmFuc2Zlcj4KICAgICAgPGZlTWVyZ2U+CiAgICAgICAgPGZlTWVyZ2VOb2RlLz4KICAgICAgICA8ZmVNZXJnZU5vZGUgaW49IlNvdXJjZUdyYXBoaWMiLz4KICAgICAgPC9mZU1lcmdlPgogICAgPC9maWx0ZXI+CiAgPC9kZWZzPgoKICA8IS0tIFNlY3Rpb24gYmFja2dyb3VuZHMgd2l0aCBlbmhhbmNlZCBzdHlsaW5nIC0tPgogIDxyZWN0IHg9IjIwIiB5PSI0MCIgd2lkdGg9IjI2MCIgaGVpZ2h0PSIzNDAiIGZpbGw9IndoaXRlIiByeD0iOCIgc3Ryb2tlPSIjMmI2Y2IwIiBzdHJva2Utd2lkdGg9IjEiIG9wYWNpdHk9IjAuMyIvPgogIDxyZWN0IHg9IjM3MCIgeT0iNDAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMzQwIiBmaWxsPSJ3aGl0ZSIgcng9IjgiIHN0cm9rZT0iIzJiNmNiMCIgc3Ryb2tlLXdpZHRoPSIxIiBvcGFjaXR5PSIwLjMiLz4KICA8cmVjdCB4PSI3MjAiIHk9IjQwIiB3aWR0aD0iMjYwIiBoZWlnaHQ9IjM0MCIgZmlsbD0id2hpdGUiIHJ4PSI4IiBzdHJva2U9IiMyYjZjYjAiIHN0cm9rZS13aWR0aD0iMSIgb3BhY2l0eT0iMC4zIi8+CgogIDwhLS0gUGhhc2UgbGFiZWxzIHdpdGggbW9yZSBwcm9mZXNzaW9uYWwgc3R5bGluZyAtLT4KICA8cmVjdCB4PSIyMCIgeT0iNDAiIHdpZHRoPSIyNjAiIGhlaWdodD0iNDAiIGZpbGw9IiMxYTM2NWQiIHJ4PSI4Ii8+CiAgPHJlY3QgeD0iMzcwIiB5PSI0MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE2IiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0id2hpdGUiPkVWQUxVQVRJT04gUEhBU0U8L3RleHQ+CiAgPHRleHQgeD0iNTAwIiB5PSIyMjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMyYjZjYjAiPlZhbGlkYXRpb248L3RleHQ+CiAgPHRleHQgeD0iNTAwIiB5PSIyNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzRhNTU2OCI+QXV0b21hdGVkIFRlc3QgQ2FzZXM8L3RleHQ+CgogIDwhLS0gUHJvZHVjdGlvbiBib3ggLS0+CiAgPHJlY3QgeD0iNzUwIiB5PSIxODAiIHdpZHRoPSIyMDAiIGhlaWdodD0iMTAwIiByeD0iMTAiIGZpbGw9IndoaXRlIiBzdHJva2U9IiMyYjZjYjAiIHN0cm9rZS13aWR0aD0iMiIgZmlsdGVyPSJzaGFkb3ciLz4KICA8dGV4dCB4PSI4NTAiIHk9IjIyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEyIiBmaWxsPSIjNGE1NTY4Ij5JbXByb3ZlbWVudHM8L3RleHQ+CgogIDwhLS0gIEFycm93cyB3aXRoIGFkanVzdGVkIHBvc2l0aW9ucyAtLT4KICA8IS0tIEltcHJvdmVtZW50cyBhcnJvdyAtLT4KICA8cGF0aCBkPSJNMjUwIDIxMCBDMzAwIDIxMCAzNTAgMjEwIDQwMCAyMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzRhNTU2OCIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiLz4KICA8dGV4dCB4PSIzMjUiIHk9IjIwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEyIiBmaWxsPSIjNGE1NTY4Ij5GZWVkYmFjazwvdGV4dD4KICA8IS0tIEFwcGxpZWQgYmFjayAtLT4KICA8dGV4dCB4PSI1MCIgeT0iMTgwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSJ3aGl0ZSI+REVWRUxPUE1FTlQgUEhBU0U8L3RleHQ+CiAgPHRleHQgeD0iMTUwIiB5PSIyMjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMyYjZjYjAiPkRldmVsb3BtZW50PC90ZXh0PgogIDx0ZXh0IHg9IjE1MCIgeT0iMjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSJ3aGl0ZSI+QXV0b21hdGVkIFRlc3QgQ2FzZXM8L3RleHQ+CgogIDwhLS0gUGFwcGxpZWQgYmFjayAtLT4KICA8dGV4dCB4PSI4NTAiIHk9IjI0NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEyIiBmaWxsPSIjNGE1NTY4Ij5GZWVkYmFjazwvdGV4dD4KICA8IS0tIEFwcGxpZWQgYmFjayAtLT4KICA8cGF0aCBkPSJNNzUwIDI1MCBDNzAwIDI1MCA2NTAgMjUwIDYwMCAyNTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzRhNTU2OCIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiLz4KICA8dGV4dCB4PSIzMjUiIHk9IjI3MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEyIiBmaWxsPSIjNGE1NTY4Ij5SZWdyZXNzaW9uczwvdGV4dD4KPC9zdmc+Cg==) width="1000" height="450" class="img_SS3x"></p>