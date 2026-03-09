# Source: https://nitro.build/raw/deploy/providers/flightcontrol.md

# Flightcontrol

> Deploy Nitro apps to AWS via Flightcontrol.

**Preset:** `flightcontrol`

<read-more to="https://flightcontrol.dev?ref=nitro" title="flightcontrol.dev">

</read-more>

<note>

Flightcontrol has zero config support for [Nuxt](https://nuxt.com/) projects.

</note>

## Set Up your flightcontrol account

On a high level, the steps you will need to follow to deploy a project for the first time are:

<steps level="4">

#### Create an account at [Flightcontrol](https://app.flightcontrol.dev/signup?ref=nitro)

#### Create an account at [AWS](https://portal.aws.amazon.com/billing/signup) (if you don't already have one)

#### Link your AWS account to the Flightcontrol

#### Authorize the Flightcontrol GitHub App to access your chosen repositories, public or private

#### Create a Flightcontrol project with configuration via the Dashboard or with configuration via `flightcontrol.json`

</steps>

### Create a project with configuration via the dashboard

<steps level="4">

#### Create a Flightcontrol project from the Dashboard. Select a repository for the source

#### Select the `GUI` config type

#### Select the Nuxt preset. This preset will also work for any Nitro-based applications

#### Select your preferred AWS server size

#### Submit the new project form

</steps>

### Create a project with configuration via `flightcontrol.json`

<steps level="4">

#### Create a Flightcontrol project from your dashboard. Select a repository for the source

#### Select the `flightcontrol.json` config type

#### Add a new file at the root of your repository called `flightcontrol.json`. Here is an example configuration that creates an AWS fargate service for your app

</steps>

```json [flightcontrol.json]
{
  "$schema": "https://app.flightcontrol.dev/schema.json",
  "environments": [
    {
      "id": "production",
      "name": "Production",
      "region": "us-west-2",
      "source": {
        "branch": "main"
      },
      "services": [
        {
          "id": "nitro",
          "buildType": "nixpacks",
          "name": "My Nitro site",
          "type": "fargate",
          "domain": "www.yourdomain.com",
          "outputDirectory": ".output",
          "startCommand": "node .output/server/index.mjs",
          "cpu": 0.25,
          "memory": 0.5
        }
      ]
    }
  ]
}
```

1. Submit the new project form.

<read-more to="https://www.flightcontrol.dev/docs?ref=nitro">

Learn more about Flightcontrol's [configuration](https://www.flightcontrol.dev/docs?ref=nitro).

</read-more>
