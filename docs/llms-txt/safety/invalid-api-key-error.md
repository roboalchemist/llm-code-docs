# Source: https://docs.safetycli.com/safety-docs/support/invalid-api-key-error.md

# Invalid API Key Error

An invalid API key error means you are not using a valid Safety API key. If this API key was working previously, then the key may have been invalidated (for example, rotated) or your Safety account is no longer active.

#### How to get a Safety API key

If you already have a Safety account, once logged in you can find your API key on the [Teams and API Keys](https://manage.safetycli.com) page.

If you do not have a Safety account, you can obtain a Safety API key by [signing up ](https://manage.safetycli.com/create-account)for a free trial or a paid account.

If your team already has a Safety account and you need an API key assigned to you, please get in touch with your team's Safety admin to add you as a team member.

#### Using the Safety API key in Safety CLI

To access and utilize additional features of Safety, you will need to configure Safety to use an API key. There are two ways to do this:

* append your Safety commands with the command-line argument `--key 'your_api_key'`. For example `safety --key 'your_api_key' scan`
* save your API key as the environment variable `SAFETY_API_KEY`.\
  For example `export SAFETY_API_KEY=YOUR_API_KEY`

If you have any further questions, please don't hesitate to contact us via email at [support@s](mailto:support@pyup.io)[afetycli.com](mailto:support@safetycli.com).
