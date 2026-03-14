# Source: https://docs.envzero.com/guides/integrations/oidc-integrations/oidc-retrieving-your-subject-identifier.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve OIDC Subject Identification

> Retrieve your env zero OIDC subject identifier using credentials, app UI, or deployment methods

env zero OIDC token contains a unique Subject Identifier per env zero Organization.

There are three methods for retrieving your subject identifier.

A. From the Credential Form\
B. From the App\
C. Use Run Task\
D. Use env zero OIDC script template\
E. Manually from env zero deployment

## A. From the Credential Form

When creating an OIDC credential in the organization credentials page you can see the sub value in the last disabled form input:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/8647f03-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=337e3d4268695e9a4de62c34dca3637f" alt="Interface screenshot showing configuration options" width="1132" height="1298" data-path="images/guides/integrations/oidc-integrations/8647f03-image.png" />
</Frame>

## B. From the App

Go to Organization Settings -> Policies\
Next to the "Enable OIDC" checkbox, click "show" ( the "show" button will only appear if OIDC is enabled )

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/375e089-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=45fef7347581f23712511a1138d65416" alt="" width="1915" height="972" data-path="images/guides/integrations/oidc-integrations/375e089-image.png" />

## C. Use Run Task

This simple node script will help decode the OIDC Token.

1. “Enable OIDC”
   1. Under Organization > Settings > Policy - Check “Enable OIDC during deployments”\
      <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/15ff313-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=7a4119e7d7e647626f120b819693832a" alt="" width="854" height="678" data-path="images/guides/integrations/oidc-integrations/15ff313-image.png" />
2. Run a Task - under any existing env zero environment, select "Run a Task" from the env zero environment menu.  Note: You will need administrative access to see this option.
3. Copy and Paste this script:

```shell  theme={null}
node -e "console.log(JSON.parse(Buffer.from(process.env.ENV0_OIDC_TOKEN.split('.')[1], 'base64')));"
```

1. Hit Run a Task and open the console outputs under "Task Commands" step.

## D. Using env zero OIDC Script Template

This [env zero template](https://github.com/env0/customer-tools/tree/main/iam/oidc/decode-oidc), will run a decode script to help you view the contents of the OIDC token.

1. “Enable OIDC”
   1. Under Organization > Settings > Policy - Check “Enable OIDC during deployments”\
      <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/15ff313-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=7a4119e7d7e647626f120b819693832a" alt="" width="854" height="678" data-path="images/guides/integrations/oidc-integrations/15ff313-image.png" />

2. Clone or Fork the Repo: [https://github.com/env0/customer-tools](https://github.com/env0/customer-tools)

3. Run an Environment - from VCS, and configure it with the repo you've cloned/forked to, and the folder path: `iam/oidc/decode-oidc`

4. This will generate a step in the deployment that outputs the OIDC contents similar to this screenshot:

## E. Manually from env zero deployment

To retrieve your organization’s unique Subject Identifier:

1. “Enable OIDC”
   1. Under Organization > Settings > Policy - Check “Enable OIDC during deployments”\
      <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/15ff313-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=7a4119e7d7e647626f120b819693832a" alt="" width="854" height="678" data-path="images/guides/integrations/oidc-integrations/15ff313-image.png" />

2. Go to an existing environment and “Run a Task”\
   <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/b06384f-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=fde3d0c7f631e0d6c4016d2ce91f33f8" alt="" width="845" height="338" data-path="images/guides/integrations/oidc-integrations/b06384f-image.png" />

3. Run the following command: `echo $ENV0_OIDC_TOKEN | base64`\
   <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/43c7ad2-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=7d2c75aa54568981b735f5a68b7a0c56" alt="" width="771" height="552" data-path="images/guides/integrations/oidc-integrations/43c7ad2-image.png" />

   <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/812c2d9-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=e0f643ce23e30360604ca9c82e87a501" alt="" width="847" height="637" data-path="images/guides/integrations/oidc-integrations/812c2d9-image.png" />

4. Copy and Base64 Decode the Token: `echo “ZVXMU5pSXNJblI1Y0NJNklrcFhWQ0lzSW10cFpDSTZJazETmEwWkdU…” | base64 -d`

   <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/c1d4936-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=5a065acbee20ae3af8df9228b92cee04" alt="" width="816" height="388" data-path="images/guides/integrations/oidc-integrations/c1d4936-image.png" />

5. Copy the Token and Inspect the decoded token using [jwt.io](https://jwt.io/)\
   <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/6fbcc4a-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=cc2647f9b8dd046492a04e3312c20b79" alt="" width="959" height="855" data-path="images/guides/integrations/oidc-integrations/6fbcc4a-image.png" />

6. Copy the Subject Identifier ”sub” (In this example: `auth0|632b8219674bde0224a96141`)

Built with [Mintlify](https://mintlify.com).
