# Source: https://docs.redwoodjs.com/docs/deploy/flightcontrol

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Deployment](/docs/deployment/index)
-   [AWS via Flightcontrol]

[Version: 8.8]

On this page

<div>

# Deploy to AWS with Flightcontrol

</div>

[Flightcontrol](https://www.flightcontrol.dev?ref=redwood) enables any developer to deploy to AWS without being a wizard. It\'s extremely easy to use but lets you pop the hood and leverage the raw power of AWS when needed. It supports servers, static sites, and databases which makes it a perfect fit for hosting scalable Redwood apps.

## Flightcontrol Deploy Setup[​](#flightcontrol-deploy-setup "Direct link to Flightcontrol Deploy Setup") 

1.  In your project, run the command `yarn rw setup deploy flightcontrol --database=YOUR_DB_TYPE` where YOUR_DB_TYPE is `mysql` or `postgresql`
2.  Commit the changes and push to github.
3.  If you don\'t have an account, sign up at [app.flightcontrol.dev/signup](https://app.flightcontrol.dev/signup?ref=redwood).
4.  Create a new project.
    1.  Connect your GitHub account and select your repo.
    2.  Click the Redwood preset
    3.  Click \"Create project\" (do not add services to the UI during this step, the flightcontrol.json you added will be used for service config)
5.  After project is created, add your env vars under Environment Settings.
    1.  If using dbAuth, add the session secret key env variable in the Flightcontrol dashboard.

If you have *any* problems or questions, Flightcontrol is very responsive. [See their support options](https://www.flightcontrol.dev/docs/troubleshooting/contacting-support).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/deploy/flightcontrol.md)