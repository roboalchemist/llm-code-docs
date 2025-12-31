# Source: https://infisical.com/docs/sdks/languages/dotnet.md

# Source: https://infisical.com/docs/integrations/frameworks/dotnet.md

# Source: https://infisical.com/docs/sdks/languages/dotnet.md

# Source: https://infisical.com/docs/integrations/frameworks/dotnet.md

# Source: https://infisical.com/docs/sdks/languages/dotnet.md

# Source: https://infisical.com/docs/integrations/frameworks/dotnet.md

# Source: https://infisical.com/docs/sdks/languages/dotnet.md

# Source: https://infisical.com/docs/integrations/frameworks/dotnet.md

# .NET

> How to use Infisical to inject environment variables and secrets into a .NET app.

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

## Initialize Infisical for your [.NET](https://dotnet.microsoft.com) app

```bash  theme={"dark"}
# navigate to the root of your of your project 
cd /path/to/project

# then initialize infisical
infisical init
```

## Start your application as usual but with Infisical

```bash  theme={"dark"}
infisical run -- <your application start command>

# Example
infisical run -- dotnet run
```
