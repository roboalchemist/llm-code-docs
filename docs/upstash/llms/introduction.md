# Source: https://upstash.com/docs/introduction.md

# Source: https://upstash.com/docs/devops/developer-api/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started

Using Upstash API, you can develop applications that can create and manage
Upstash products and resources. You can automate everything that
you can do in the console. To use developer API, you need to create an API key
in the console.

<Note>
  The Developer API is only available to native Upstash accounts. Accounts created via third-party platforms like Vercel or Fly.io are not supported.
</Note>

### Create an API key

1. Log in to the console then in the left menu click the
   `Account > Management API` link.

2. Click the `Create API Key` button.

<Frame>
  <img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-list.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=0ee4011eb149892c533eecbd904e2934" data-og-width="2068" width="2068" data-og-height="1102" height="1102" data-path="img/developerapi/api-key-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-list.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=660c631a8f49489a3ff8948dd6db41c3 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-list.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=8e561d91ca284d7c7819a8ad74dcea65 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-list.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=9e19189fe974b4c4179a70ea8282fdca 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-list.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=2029bc6f2d13a1d7854a795f272c2c1f 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-list.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=287f08f34a7857d56af29a6c0c3ad26f 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-list.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=5af51a63b067e72e902977c040bc8864 2500w" />
</Frame>

3. Enter a name for your key. You can not use the same name for multiple keys.

<Frame>
  <img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-create.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=db586a9d35310683c8537cca2fce7d50" data-og-width="1040" width="1040" data-og-height="484" height="484" data-path="img/developerapi/api-key-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-create.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=463a076f8898851266fc937cdc661ca0 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-create.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=5f96cb6172a2670f5b5a8f450a71b7d7 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-create.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=4cb381cdd6e18a43ddde322bd06286bc 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-create.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=13b331fc613dd29cfa0a427ad33b93e4 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-create.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=2ef3c3b3232336133c710e078386d2b8 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-create.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=2e0928223a4eea7b19677222be91d184 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-secret.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=1295912b886ea491e71da0c6c0675d87" data-og-width="1040" width="1040" data-og-height="608" height="608" data-path="img/developerapi/api-key-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-secret.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=c9c20a789894acb2b466be8cfb85b5f1 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-secret.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=6f15c1a8c536e0a1c85505d4487abaec 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-secret.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=76fd28466dfc601b999b31da9d40d3b2 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-secret.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=4d7039e531cbf706acbdc3fb62083d4e 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-secret.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=5d65db7ea62cfc1a988bcc91c0b3ba97 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/developerapi/api-key-secret.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=9f653bc215ca2eb53aad4c07a8ca0f2b 2500w" />
</Frame>

You need to download or copy/save your API key. Upstash does not remember or
keep your API for security reasons. So if you forget your API key, it becomes
useless; you need to create a new one.

<br />

You can create multiple keys. It is recommended to use different keys in
different applications. By default one user can create up to 37 API keys. If you
need more than that, please send us an email at
[support@upstash.com](mailto:support@upstash.com)

### Deleting an API key

When an API key is exposed (e.g. accidentally shared in a public repository) or
not being used anymore; you should delete it. You can delete the API keys in
`Account > API Keys` screen.

### Roadmap

**Role based access:** You will be able to create API keys with specific
privileges. For example you will be able to create a key with read-only access.

**Stats:** We will provide reports based on usage of your API keys.
