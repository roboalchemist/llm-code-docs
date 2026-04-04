# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-environment-variables.md

# Get environment variables

You can get the environment variable details using **context.<\<env\_name>>** from the [context](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context) object.

Consider that you wish to get the value of an environment variable "DEV\_API\_URL" in the JS code and use it for further processing. See [Define environment variables](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-environment-variables), for more information on how to configure environment variables in your agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mcx7GfFrAnBqKQZUIuq%2F-Mcx8XFhR57ak3jKffF2%2F5.7-env-variable.png?alt=media\&token=dfc10cfd-62b0-46aa-bb5d-0aaf2f0cb776)

In the JS response node, you can use the **environment variable name** to get the value of the defined environment variable as follows:

```markup
return context.DEV_API_URL;
```

In the agent, the following response is displayed. Note that this is just an illustration to show how environment variables can be extracted from the context object:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3wtwalNgTb6RocLk7hB6%2Fimage.png?alt=media\&token=4cdec178-1a18-4237-b206-443e62925a76)

{% hint style="info" %}
**Note**: The environment variable name is case-sensitive. You must use the exact case as defined.
{% endhint %}
