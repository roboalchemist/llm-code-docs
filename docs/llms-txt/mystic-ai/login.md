# Source: https://docs.mystic.ai/docs/login.md

# Authentication

How to safely use the Mystic APIs

Mystic uses standard bearer tokens for all API requests. These are account specific and must be passed with every request. You can manage your API tokens on the [Developers page](https://www.mystic.ai/developers/api-tokens) on the dashboard.

You can test an API token by running the following command and replacing `YOUR_TOKEN` with a token value generated on the [Developers dashboard page](https://www.mystic.ai/developers/api-tokens) and `YOUR_USERNAME` with your dashboard username (if you get an error related to `jq` just omit the `| jq` at the end):

```shell
curl -X GET 'https://www.mystic.ai/v4/users/YOUR_USERNAME' \
	-H 'Authorization: Bearer YOUR_TOKEN' | jq
```

## Auth when using python

There are two primary ways to include this auth within requests when using the python SDK (*you'll encounter unpredictable behaviour if you do both at the same time*):

* CLI;
* or Environment Variables

You can use the Mystic CLI to authenticate and store your API credentials in your local directory `~/.pipeline/`. Any time you use the SDK to interact with the Mystic API, the SDK will then use these credentials under the hood.

> 👍 Environment variables
>
> You can either authenticate using the CLI or using environment variables, but you're likely to run into issues if you combine the two. In most cases, you'll be best off using the CLI, however, environment variables are likely to be more convenient if you're running you code on a remote server, for example in a web app.
>
> If using the CLI, check if you have previously added your `PIPELINE_API_TOKEN` to your environment, and make sure to remove it before authenticating with the CLI.
>
> On Linux/macOS, you can check whether you have set `PIPELINE_API_TOKEN`with:
>
> ```Text Shell
> echo $PIPELINE_API_TOKEN
> ```
>
> And if the output from the above command is not empty, you can remove it with:
>
> ```Text Shell
> unset PIPELINE_API_TOKEN
> ```

Simply run

```Text Shell
pipeline cluster login mystic-api API_TOKEN -u https://www.mystic.ai -a
```

with a valid API token. If you need a new token, you can create one in your [dashboard](https://www.mystic.ai/api-tokens).

You should now find a file at `~/.pipeline/config.yaml`, which looks something like:

```Text YAML
active_remote: mystic-api
remotes:
- alias: mystic-api
  token: pipeline_sk_some_random_sequence
  url: https://www.mystic.ai
```

<br>