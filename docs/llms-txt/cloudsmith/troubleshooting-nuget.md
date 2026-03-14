# Source: https://help.cloudsmith.io/docs/troubleshooting-nuget.md

# Troubleshooting NuGet

**Q. I'm unable to authenticate using HTTP Basic Authentication with a password or with an entitlement token. I'm using dotnet core SDK 2.2**

This is the error:

```
Unable to get repository signature information for source
https://nuget.cloudsmith.io/YOUR-ACCOUNT/YOUR-REPO/v3-index/repository-signatures/X.X.X/index.json
error : Response status code does not indicate success: 401 (Unauthorized)
```

***

It looks like this (not being able to use username/password directly on a source) might be an accepted bug in dotnet 2.2, possibly fixed later, as referenced in the following GitHub issues:

* [https://github.com/dotnet/cli/issues/10356](https://github.com/dotnet/cli/issues/10356)
* [https://github.com/NuGet/Home/issues/4668](https://github.com/NuGet/Home/issues/4668)

**SOLUTION**\
Add the source using `nuget sources` as follows first::

```
nuget sources add -Name NAME -source https://nuget.cloudsmith.io/YOUR-ACCOUNT/YOUR-REPO/v3/index.json -Username YOUR-USERNAME -Password YOUR-API-KEY-OR-PASSWORD -StorePasswordInClearText
```

Then do `dotnet restore` like:

```
dotnet restore -s https://nuget.cloudsmith.io/YOUR-ACCOUNT/YOUR-REPO/v3/index.json --configfile ~/config/NuGet/NuGet.Config
```

If you want to use an Entitlement Token instead of a username and password/API-Key, use "token" for the username and an Entitlement Token as the password.

## Still Need Help?

Contact us [here](https://support.cloudsmith.com). We're always happy to help!