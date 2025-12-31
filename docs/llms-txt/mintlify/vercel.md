# Source: https://mintlify.com/docs/deploy/vercel.md

# Vercel

> Deploy documentation on Vercel with automatic builds and custom domains.

export const VercelJsonGenerator = () => {
  const [subdomain, setSubdomain] = useState('[SUBDOMAIN]');
  const [subpath, setSubpath] = useState('[SUBPATH]');
  const vercelConfig = {
    rewrites: [{
      source: "/_mintlify/:path*",
      destination: `https://${subdomain}.mintlify.app/_mintlify/:path*`
    }, {
      source: "/api/request",
      destination: `https://${subdomain}.mintlify.app/_mintlify/api/request`
    }, {
      source: `/${subpath}`,
      destination: `https://${subdomain}.mintlify.app/${subpath}`
    }, {
      source: `/${subpath}/llms.txt`,
      destination: `https://${subdomain}.mintlify.app/llms.txt`
    }, {
      source: `/${subpath}/llms-full.txt`,
      destination: `https://${subdomain}.mintlify.app/llms-full.txt`
    }, {
      source: `/${subpath}/sitemap.xml`,
      destination: `https://${subdomain}.mintlify.app/sitemap.xml`
    }, {
      source: `/${subpath}/robots.txt`,
      destination: `https://${subdomain}.mintlify.app/robots.txt`
    }, {
      source: `/${subpath}/:path*`,
      destination: `https://${subdomain}.mintlify.app/${subpath}/:path*`
    }, {
      source: "/mintlify-assets/:path+",
      destination: `https://${subdomain}.mintlify.app/mintlify-assets/:path+`
    }]
  };
  const copyToClipboard = () => {
    navigator.clipboard.writeText(JSON.stringify(vercelConfig, null, 2)).then(() => {
      console.log('Copied config to clipboard!');
    }).catch(err => {
      console.error("Failed to copy: ", err);
    });
  };
  return <div className="p-4 border dark:border-white/10 rounded-2xl not-prose space-y-4">
      <div className="space-y-4">
        <div>
          <label className="block text-sm text-zinc-950/70 dark:text-white/70 mb-1">
            Subdomain
          </label>
          <input type="text" value={subdomain} onChange={e => setSubdomain(e.target.value)} placeholder="your-subdomain" className="w-full p-1 text-sm rounded border dark:border-white/10 bg-transparent" />
        </div>
        <div>
          <label className="block text-sm text-zinc-950/70 dark:text-white/70 mb-1">
            Subpath
          </label>
          <input type="text" value={subpath} onChange={e => setSubpath(e.target.value)} placeholder="docs" className="w-full p-1 text-sm rounded border dark:border-white/10 bg-transparent" />
        </div>
      </div>
      <div className="relative">
        <button onClick={copyToClipboard} className="absolute top-2 right-2 p-2 rounded-lg transition-all duration-200 group">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-4 h-4 dark:text-white/60 text-gray-400 group-hover:text-gray-500 dark:group-hover:text-white/60 transition-colors">
            <path d="M14.25 5.25H7.25C6.14543 5.25 5.25 6.14543 5.25 7.25V14.25C5.25 15.3546 6.14543 16.25 7.25 16.25H14.25C15.3546 16.25 16.25 15.3546 16.25 14.25V7.25C16.25 6.14543 15.3546 5.25 14.25 5.25Z" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"></path>
            <path d="M2.80103 11.998L1.77203 5.07397C1.61003 3.98097 2.36403 2.96397 3.45603 2.80197L10.38 1.77297C11.313 1.63397 12.19 2.16297 12.528 3.00097" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"></path>
          </svg>
          <span className="absolute top-9 left-1/2 transform -translate-x-1/2 bg-primary text-white text-xs px-1.5 py-0.5 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-200 whitespace-nowrap">
            Copy
          </span>
        </button>
        <pre className="p-4 rounded-lg overflow-auto text-xs border dark:border-white/10">
          <code>{JSON.stringify(vercelConfig, null, 2)}</code>
        </pre>
      </div>
    </div>;
};

## vercel.json file

The `vercel.json` file configures how your project is built and deployed. It sits in your project's root directory and controls various aspects of your deployment, including routing, redirects, headers, and build settings.

We use the `rewrites` configuration to proxy requests from your main domain to your documentation.

Rewrites map incoming requests to different destinations without changing the URL in the browser. When someone visits `yoursite.com/docs`, Vercel internally fetches content from `your-subdomain.mintlify.dev/docs`, but the user still sees `yoursite.com/docs` in their browser. This is different from redirects, which send users to another URL entirely.

You can customize the subpath to any value you prefer, such as `/docs`, `/help`, or `/guides`. Additionally, you can use deeply nested subpaths like `/product/docs`.

## Configuration

### Host from `/docs`

1. Navigate to [Custom domain setup](https://dashboard.mintlify.com/settings/deployment/custom-domain) in your dashboard.
2. Click the **Host at `/docs`** toggle to the on position.

<Frame>
  <img alt="Screenshot of the Custom domain setup page. The Host at `/docs` toggle is on and highlighted by an orange rectangle." src="https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-light.png?fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=7e32943b9dd517e21030678381a60b40" className="block dark:hidden" data-og-width="1438" width="1438" data-og-height="298" height="298" data-path="images/subpath/toggle-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-light.png?w=280&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=33d489126d09988d19d008d6a7f4a297 280w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-light.png?w=560&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=b21fa8cf8a97621570dfafbf58adc664 560w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-light.png?w=840&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=4148864540f914d5cd5fd9da362f4bf8 840w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-light.png?w=1100&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=47fd61f2209bd3d69e84eb3504f44758 1100w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-light.png?w=1650&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=e6452903ad163a01396dc9dbda4b0dc0 1650w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-light.png?w=2500&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=705655c35ceb3f569262b45500a53706 2500w" />

  <img alt="Screenshot of the Custom domain setup page. The Host at `/docs` toggle is on and highlighted by an orange rectangle." src="https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-dark.png?fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=9e0fd7047a7937d5a6d9cfc2c55acb09" className="hidden dark:block" data-og-width="1440" width="1440" data-og-height="300" height="300" data-path="images/subpath/toggle-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-dark.png?w=280&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=0d91795ad4a995f2f38870b1e1dcdf42 280w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-dark.png?w=560&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=06032a7cb5cd4ef88ec6ff7d43a59936 560w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-dark.png?w=840&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=836eef4347e6e17b30dac1b38c41c951 840w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-dark.png?w=1100&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=43c8f66298e7820cffe6d544663ca9a7 1100w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-dark.png?w=1650&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=f2b3176eb3af0ac276f8255973ae57ab 1650w, https://mintcdn.com/mintlify/y0I2fgo5Rzv873ju/images/subpath/toggle-dark.png?w=2500&fit=max&auto=format&n=y0I2fgo5Rzv873ju&q=85&s=19e3818409019c5e6136b61861b01f89 2500w" />
</Frame>

3. Enter your domain.
4. Select **Add domain**.
5. Add the following rewrites to your `vercel.json` file. Replace `[subdomain]` with your subdomain:

```json  theme={null}
{
  "rewrites": [
    {
      "source": "/docs",
      "destination": "https://[subdomain].mintlify.dev/docs"
    },
    {
      "source": "/docs/:match*",
      "destination": "https://[subdomain].mintlify.dev/docs/:match*"
    }
  ]
}
```

* **`source`**: The path pattern on your domain that triggers the rewrite.
* **`destination`**: Where the request should be proxied to.
* **`:match*`**: A wildcard that captures any path segments after your subpath.

For more information, see [Configuring projects with vercel.json: Rewrites](https://vercel.com/docs/projects/project-configuration#rewrites) in the Vercel documentation.

### Host from custom path

To use a custom subpath (any path other than `/docs`), you must organize your documentation files within your repository to match your subpath structure. For example, if your documentation is hosted at `yoursite.com/help`, your documentation files must be in a `help/` directory.

Use the generator below to create your rewrites configuration. Add the rewrites to your `vercel.json` file.

<VercelJsonGenerator />

## Using external proxies with Vercel

If you're using an external proxy (like Cloudflare or AWS CloudFront) in front of your Vercel deployment, you must configure it properly to avoid conflicts with Vercel's domain verification and SSL certificate provisioning.

Improper proxy configuration can prevent Vercel from provisioning Let's Encrypt SSL certificates and cause domain verification failures.

See the [supported providers](https://vercel.com/guides/how-to-setup-verified-proxy#supported-providers-verified-proxy-lite) in the Vercel documentation.

### Required path allowlist

Your external proxy must allow traffic to these specific paths without blocking, redirecting, or heavily caching:

* `/.well-known/acme-challenge/*` - Required for Let's Encrypt certificate verification
* `/.well-known/vercel/*` - Required for Vercel domain verification
* `/mintlify-assets/_next/static/*` - Required for static assets

These paths should pass through directly to your Vercel deployment without modification.

### Header forwarding requirements

Ensure that your proxy correctly forwards the `HOST` header. Without proper header forwarding, verification requests will fail.

### Testing your proxy setup

To verify your proxy is correctly configured:

1. Test that `https://[yourdomain].com/.well-known/vercel/` returns a response.
2. Ensure SSL certificates are provisioning correctly in your Vercel dashboard.
3. Check that domain verification completes successfully.
