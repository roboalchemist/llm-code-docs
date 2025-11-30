# Source: https://dagshub.com/docs/feature_guide/project_templates/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/project_templates.md "Edit this page")

# DagsHub Templates[¶](#dagshub-templates "Permanent link")

We at DagsHub want to help you get started as painlessly as possible, so you can get to the cool data science-y parts ASAP. To make this possible, we support starting from dedicated MLOps oriented project templates. To use them, click the \"Create\" menu and select \"Create from template option\".

[![Template Options](../assets/templates/templates_option.jpeg)](../assets/templates/templates_option.jpeg)

~Repo\ Creation\ Options~

## Template Options[¶](#template-options "Permanent link")

Then select the relevant template you\'d like to use:

[![Template List](../assets/templates/templates_list.jpeg)](../assets/templates/templates_list.jpeg) You can choose from one of the following templates:

1.  **Custom** - Pick your own license, gitignores, and whether you want a basic README.md

2.  **Cookiecutter DVC** - Start your project with a general structure already established - batteries included!

    [See an example of this project structure](https://dagshub.com/DagsHub-Official/Cookiecutter-DVC).

    This template is based on the well-known [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science) template, only we modified it to give you a basic DVC pipeline right out of the box. This allows you to just start writing code and working on your data immediately. You can always modify the DVC structure to your own needs later on.

    **We especially recommend this template for first timers!**

3.  **Jupyter Notebook + DVC** - A project template based on a Jupyter Notebook.

    [See an example of this project structure](https://dagshub.com/DagsHub-Official/Jupyter-Notebook-DVC).

    Using Jupyter Notebooks might make it harder to reproduce results or create production-grade research. That said, notebooks are fun to work with, and we want to make it as easy as possible to bridge the gap.\
    This template has a basic DVC pipeline, and an example notebook that includes special cells for DVC versioning. This means you can add in your code, and version your data and models all from within the notebook. You can always modify the DVC structure to your own needs later on.

4.  **Cookiecutter MLOps** â€"Â A reasonably standardized but flexible project structure that implements sound MLOps principles for building your next machine learning project.

    [See an example of this project structure](https://dagshub.com/DagsHub/Cookiecutter-MLOps).

    This template is also based on [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science), but includes additional MLOps best practices, so you can focus on building machine learning products while having MLOps best practices applied.

## Suggestions?[¶](#suggestions "Permanent link")

**Tell us about your template ideas** - Need something, but it\'s not in the list above? Contact us via [Discord](https://discord.gg/skXZZjJd2w) and tell us what template would be great for your workflow.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).