# Source: https://dagshub.com/docs/api/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/api.md "Edit this page")

# Welcome to the DagsHub API Docs[¶](#welcome-to-the-dagshub-api-docs "Permanent link")

- ***Click [here](#swagger-ui) to jump to the API documentation***

**Use this API to automate, integrate and create new things with DagsHub.**

You can experiment with the API right from here using the **\"Try it out\"** button under each endpoint. [Create a repository](https://dagshub.com/repo/create) for expirmentation and make sure to [authorize](https://dagshub.com/user/settings/tokens) for endpoints that require that.

**Having trouble? Something doesn\'t work properly?** Please [get help on our discord](https://discord.com/invite/9gU36Y6) or [open an issue](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).

## Authentication[¶](#authentication "Permanent link")

**To use the \'Try it out\' button, just sign in to the website.** No need to use the \'Authorize\' button.

### Access Token[¶](#access-token "Permanent link")

You can find your access token [here](http://dagshub.com/user/settings/tokens). To make API requests, use the token with **Basic Authentication**, along with your username.

## Client Library[¶](#client-library "Permanent link")

You can find **auto-generated** client libraries for various languages here: <https://github.com/DagsHub/api-clients>. They\'re supposed to work, but haven\'t been fully tested yet. If you find problems, please open an issue on GitHub.

## Direct Data Access[¶](#direct-data-access "Permanent link")

Read more about how to use this API as part of the DagsHub client to let you [download & stream your data from](https://dagshub.com/docs/client/reference/file_downloading.html), and [upload it to](https://dagshub.com/docs/client/reference/file_uploading.html), any DagsHub project.

## Integrations[¶](#integrations "Permanent link")

**TL;DR: We offer full support for the MLflow & Label Studio APIs for projects hosted on DagsHub!**

### MLflow[¶](#mlflow "Permanent link")

Check out the **[MLflow documentation](https://www.mlflow.org/docs/latest/rest-api.html)** for the complete API documentation. In short, to use the MLflow Rest API with DagsHub, treat the mlflow remote address (`https://dagshub.com/<user-name>/<repository-name>.mlflow`) as the base url for all the API endpoints.

*For example*, to list experiments from the DagsHub repository [nirbarazida/CheXNet](https://dagshub.com/nirbarazida/CheXNet/experiments), you can run:

    curl https://dagshub.com/nirbarazida/CheXNet.mlflow/api/2.0/mlflow/experiments/list

### Label Studio[¶](#label-studio "Permanent link")

Check out the **[Label Studio documentation](https://labelstud.io/api)** for the complete API documentation. Use the DagsHub repository address with the addition of **`/annotations/de`** as the base url for all the API endpoints.

Info

Instead of using `Authorization: Token` as specified in the Label Studio documentation, use `Authorization: Bearer`.

*For example*, to list your annotation projects in the DagsHub repository [nirbarazida/CheXNet](https://dagshub.com/nirbaraz/CheXNet), you can run:

    curl -X GET https://dagshub.com/nirbarazida/CheXNet/annotations/de/api/projects -H 'Authorization: Bearer <your_dagshub_token>'

Important Note

**Label Studio workspaces shut down when not in use.** This means, your requests may initially fail but after 2-3 minutes the workspace will wake up and the API will work again. **If you need an always-running workspace, please contact us through our [plans page](https://dagshub.com/pricing) and we\'ll be happy to help.**

## API Reference[¶](#api-reference "Permanent link")

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).