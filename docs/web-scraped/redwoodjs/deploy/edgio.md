# Source: https://docs.redwoodjs.com/docs/deploy/edgio

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Deployment](/docs/deployment/index)
-   [Edgio]

[Version: 8.8]

On this page

<div>

# Deploy to Edgio

</div>

> ⚠️ **Deprecated**
>
> As of Redwood v7, we are deprecating this deploy setup as an \"officially\" supported provider. This means:
>
> -   For projects already using this deploy provider, there will be NO change at this time
> -   Both the associated `setup` and `deploy` commands will remain in the framework as is; when setup is run, there will be a "deprecation" message
> -   We will no longer run CI/CD on the Edgio deployments, which means we are no longer guaranteeing this deploy works with each new version
>
> If you have concerns or questions about our decision to deprecate this deploy provider please reach out to us on our [community forum](https://community.redwoodjs.com).

[Edgio](https://edg.io) extends the capabilities of a traditional CDN by not only hosting your static content, but also providing server-side rendering for progressive web applications as well as caching both your APIs and HTML at the network edge to provide your users with the fastest browsing experience.

## Edgio Deploy Setup[​](#edgio-deploy-setup "Direct link to Edgio Deploy Setup") 

In order to deploy your RedwoodJS project to Edgio, the project must first be initialized with the Edgio CLI.

1.  In your project, run the command `yarn rw setup deploy edgio`.
2.  Verify the changes to your project, commit and push to your repository.
3.  Deploy your project to Edgio
4.  If this is your first time deploying to Edgio, the interactive CLI will prompt to authenticate using your browser. You can start the deploy by running `yarn rw deploy edgio`.
5.  If you are deploying from a **non-interactive** environment, you will need to create an account on [Edgio Developer Console](https://app.layer0.co) first and setup a [deploy token](https://docs.edg.io/guides/deploy_apps#deploy-from-ci). Once the deploy token is created, save it as a secret to your environment. You can start the deploy by running `yarn rw deploy edgio --token=XXX`.
6.  Follow the link in the output to view your site live once deployment has completed!

For more information on deploying to Edgio, check out the [documentation](https://docs.edg.io).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/deploy/edgio.md)