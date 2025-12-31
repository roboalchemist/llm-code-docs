# Source: https://playwright.dev/docs/test-agents

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Agents]

On this page

<div>

# Playwright Test Agents

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright comes with three Playwright Test Agents out of the box: **🎭 planner**, **🎭 generator** and **🎭 healer**.

These agents can be used independently, sequentially, or as the chained calls in the agentic loop. Using them sequentially will produce test coverage for your product.

-   **🎭 planner** explores the app and produces a Markdown test plan
-   **🎭 generator** transforms the Markdown plan into the Playwright Test files
-   **🎭 healer** executes the test suite and automatically repairs failing tests