# Source: https://firebase.google.com/docs/dynamic-links/custom-domains.md.txt

<br />

| **Note:** Firebase Dynamic Links is*deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the[migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service)and see the[Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq)for more information.

You can have greater control over yourDynamic Links' branding by using your own domain instead of a`page.link`subdomain. With custom domains, you can createDynamic Linkslike the following examples:  

```
https://example.com/link-suffix
https://example.com/links/promos/link-suffix
https://links.example.com/link-suffix
https://ex.amp.le/link-suffix
```

The part of the URL before<var translate="no">link-suffix</var>is called the*URL prefix* , and contains both your customDynamic Linkdomain and a path prefix. You will need to provide a URL prefix when you createDynamic Links.

Setting up a custom domain requires Editor or Owner permission on your Firebase project.
| **Note:** To use a custom domain forDynamic Links, the domain must point toFirebase Hosting. If you have a domain you want to use withDynamic Linksand the domain points to a different host, you can either move toFirebase Hostingor create a subdomain hosted by Firebase, which you can use forDynamic Links.

## Using your web domain forDynamic Links

You can use the same domain for yourDynamic Linksand your web pages, Universal Links, and App Links, but if you do, you must take care that yourDynamic LinkURLs don't conflict with your web URLs. When you configureDynamic Linksto use a particular URL prefix, all URLs that begin with that prefix are treated asDynamic Links, so you can't use URLs with that prefix to point to ordinary hosted content.

For example, if you want to create aDynamic Linkto the resource`https://example.com/my-resource`(a web page, Universal Link, or App Link), you can't use`https://example.com/`as theDynamic LinksURL prefix, because doing so would cause`https://example.com/my-resource`to be treated as aDynamic Link. Instead, you must use a URL prefix with either a different domain or a different path prefix.

So, the following long-formDynamic Links(and equivalent short links) won't work as intended because the URLs specified by the`link`parameter start with theDynamic LinkURL prefix,`https://example.com/`:  

```
 https://example.com/?link=https://example.com/my-resource
 https://example.com/?link=https://example.com/resources/my-resource
```

But the following long-formDynamic Links(and equivalent short links) can work, because the URL prefixes don't conflict with the`link`URLs:  

```
 https://link.example.com/?link=https://example.com/my-resource
 https://example.com/links/?link=https://example.com/my-resource
 https://ex.amp.le/?link=https://example.com/my-resource
```

## Set up a custom domain in theFirebaseconsole

You can usually set up a custom domain completely in theFirebaseconsole. To do so:

1. If you haven't set upFirebase Hostingfor your project, open the[Hostingpage](https://console.firebase.google.com/project/_/hosting/)of theFirebaseconsole, click**Get Started**, and click through the setup instructions. You don't have to complete the indicated steps at this time.

2. Open the[Dynamic Linkspage](https://console.firebase.google.com/project/_/durablelinks/)of theFirebaseconsole.

3. If you haven't usedDynamic Linksbefore, click**Get Started** . Otherwise, click**Add URL prefix**from the drop-down menu.

   Then, complete the setup wizard, specifying the domain and path prefix you want to use when prompted.
   | **Note:** You can't use the same URL prefix for bothDynamic Linksand regular hosting. If you want to use the same branding for both, consider using a path prefix (for example, example.com/links) or subdomain (links.example.com/) in yourDynamic LinksURL prefix.
4. **iOS only** : In your Xcode project's`Info.plist`file, create a key called`FirebaseDynamicLinksCustomDomains`and set it to your app'sDynamic LinksURL prefixes. For example:

       <key>FirebaseDynamicLinksCustomDomains</key>
       <array>
         <string>https://example.com/link</string>
         <string>https://example.com/promos</string>
       </array>

## Set up a custom domain manually

In some situations, such as when you already have a custom domain set up forDynamic Linksand want to add another domain, or when you are adding a domain already connected to aHostingsite, you have to set up your custom domain manually.

To do so:

1. [Connect your domain toFirebase Hosting](https://firebase.google.com/docs/hosting/custom-domain)if you haven't already done so.

   Setting up your domain withFirebase Hostingincludes creating the configuration file[`firebase.json`](https://firebase.google.com/docs/cli#the_firebasejson_file)in your local project directory.
2. [Update to the latest version of theFirebaseCLI](https://firebase.google.com/docs/cli#update-cli)(v6.5.0 or later).

3. Configure yourHostingsite forDynamic Linksin your project's`firebase.json`file. If your project has multiple sites, be sure to configure the site connected to the domain you want to use.

   - Set`appAssociation`to`AUTO`. With this setting,Hostingdynamically generates`assetlinks.json`and`apple-app-site-association`files when they are requested.

   - Specify the path prefixes you want to use forDynamic Linksby setting rewrite rules with`dynamicLinks`set to`true`. Requests to these paths get proxied toDynamic Links.

     Unlike rules that rewrite paths to URLs,Dynamic Linkrewrite rules can't contain regular expressions.

     If you have multiple rewrite rules for your site, be aware thatHostingexecutes the first rewrite rule that matches the request.

   For example:  

       "hosting": {
         // ...
         "appAssociation": "AUTO",
         "rewrites": [
           {
             "source": "/promos/**",
             "dynamicLinks": true
           },
           {
             "source": "/links/share/**",
             "dynamicLinks": true
           }
         ]
       }

   With the above configuration, you can createDynamic Linkswith URL prefixes like the following examples:  

   ```
   https://your-domain/promos/link-suffix
   https://your-domain/links/share/link-suffix
   ```

   <br />

   | **Note:** You can't use the same URL prefix for bothDynamic Linksand regular hosting. If you want to use the same branding for both, consider using a path prefix (for example, example.com/links) or subdomain (links.example.com/) in yourDynamic LinksURL prefix.

   If you use this domain only forDynamic Links, you can use a source path of`/**`to createDynamic Linkswith no path prefix:  

       {
         "source": "/**",
         "dynamicLinks": true
       }

   With the above rule, you can createDynamic Linkslike the following example:  

   ```
   https://your-domain/link-suffix
   ```

   <br />

4. Deploy yourHostingconfiguration changes:

   ```
   firebase deploy --only hosting
   ```

   <br />

   *(optional)* You can check the deployed`firebase.json`content using the[HostingREST API](https://firebase.google.com/docs/hosting/reference/rest/v1beta1/sites.releases/list?apix_params=%7B%22parent%22:%22sites/%3Cyour-site-name%3E%22,%22pageSize%22:1%7D).
5. **iOS only** : In your Xcode project's`Info.plist`file, create a key called`FirebaseDynamicLinksCustomDomains`and set it to your app'sDynamic LinksURL prefixes. For example:

       <key>FirebaseDynamicLinksCustomDomains</key>
       <array>
         <string>https://example.com/promos</string>
         <string>https://example.com/links/share</string>
       </array>

### Priority order forDynamic LinksandHosting

ForDynamic Links, be particularly aware of[hosting priority order](https://firebase.google.com/docs/hosting/full-config#hosting_priority_order).

- Ensure that yourDynamic LinksURL prefix doesn't conflict with higher priority hosting configurations (for example, hosted static content always has priority over rewrites).
- Within the`rewrites`attribute, theHostingresponse will obey the rule specified by the*first`source`glob that captures the requested path*.

For example, if you set up aDynamic Linkfor<var translate="no">your-domain</var>`/`<var translate="no">source-path</var>`/`<var translate="no">link-suffix</var>but you also have static content at<var translate="no">your-domain</var>`/`<var translate="no">source-path</var>`/index.html`, the static content takes precedence. An end-user will see`index.html`rather than theDynamic Link. Similarly, if you have static content at<var translate="no">your-domain</var>`/`<var translate="no">source-path</var>`/`<var translate="no">link-suffix</var>, the end-user will see the static content rather than theDynamic Link.

If you want to use the same branding for bothDynamic LinksandHosting, consider one of the following options for yourDynamic LinksURL prefix:

- Set your`source`attribute to match a path prefix. For example, if you have a custom domain of`example.com`, your rewrite rule could be:

      // Domain is example.com
      "rewrites": [ {
        "source": "/links/**",  // Dynamic Links start with "https://example.com/links/"
        "dynamicLinks": true
      } ]

- Set up a subdomain to use forDynamic Links, then set your`source`attribute to match that subdomain. For example, if you have a subdomain of`links.example.com`, your rewrite rule could be:

      // Domain is links.example.com
      "rewrites": [ {
        "source": "/**",  // Dynamic Links start with "https://links.example.com/"
        "dynamicLinks": true
      } ]

| **Note:** You can check the deployed`firebase.json`content using the[HostingREST API](https://firebase.google.com/docs/hosting/reference/rest/v1beta1/sites.releases/list?apix_params=%7B%22parent%22:%22sites/%3Cyour-site-name%3E%22,%22pageSize%22:1%7D).