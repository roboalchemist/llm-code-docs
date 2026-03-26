# Source: https://checklyhq.com/docs/communicate/status-pages/customization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Status Page Customization

> Add a custom domain and look & feel to your Status Page.

## Custom domain

<Note>
  Custom domains are available on Communicate Starter, Team and Enterprise
  plans. [View pricing](https://checklyhq.com/pricing)
</Note>

You can host your Status Page on your own domain. To set it up, add the domain in Checkly and create the required DNS records with your DNS provider.

<Steps>
  <Step title="Add a custom domain to your Status Page">
        <img src="https://mintcdn.com/checkly-422f444a/y0uv0mm_P84z_Jj5/images/docs/images/status-pages/status-pages-custom-domain-1.png?fit=max&auto=format&n=y0uv0mm_P84z_Jj5&q=85&s=a98deb431ddf04869de6c564b354664f" alt="Custom domain configuration" width="597" height="120" data-path="images/docs/images/status-pages/status-pages-custom-domain-1.png" />
  </Step>

  <Step title="Create a CNAME record that points to `custom-slug.checkly-status-page.com`">
    Create a CNAME record with your DNS provider and point it to
    `custom-domain.checkly-status-page.com` For example, in Cloudflare, the
    configuration looks like this: <img src="https://mintcdn.com/checkly-422f444a/y0uv0mm_P84z_Jj5/images/docs/images/status-pages/status-pages-custom-domain-2.png?fit=max&auto=format&n=y0uv0mm_P84z_Jj5&q=85&s=0f05307cde79d39822991fe39083bdfa" alt="Custom domain CNAME
    configuration" width="1220" height="141" data-path="images/docs/images/status-pages/status-pages-custom-domain-2.png" />
    If your provider is Cloudflare, you must disable the proxy on the CNAME, it
    should always be set to DNS only.
  </Step>

  <Step title="Add TXT record(s) to perform validation and prove domain ownership">
    After you've added your custom domain and saved the page, one or more TXT records will be displayed depending on the domain you're using.
    <img src="https://mintcdn.com/checkly-422f444a/y0uv0mm_P84z_Jj5/images/docs/images/status-pages/status-pages-custom-domain-3.png?fit=max&auto=format&n=y0uv0mm_P84z_Jj5&q=85&s=55a884a9ac24d0c061322e94d8bedec8" alt="Example custom domain TXT configuration" width="667" height="318" data-path="images/docs/images/status-pages/status-pages-custom-domain-3.png" />

    Update your DNS settings to match the TXT record(s) displayed on your Status Page to prove the ownership of the domain.

    <Note>
      Search engines require this verification to index and list your Status Page.
    </Note>
  </Step>
</Steps>

## Customize your Status Page to match your brand identity

* Upload your company logo and the link it should open
* Upload a custom favicon
* Choose the default theme: auto (system), light or dark
* Customize the color theme to match your brand

<Note>
  Theme customization is available on Communicate Team and Enterprise plans.
  [View pricing](https://checklyhq.com/pricing)
</Note>


Built with [Mintlify](https://mintlify.com).