# Source: https://docs.readthedocs.com/platform/latest/reference/cdn.html

# Content Delivery Network (CDN) and caching[](#content-delivery-network-cdn-and-caching "Link to this heading")

A CDN is used for making documentation pages *fast* for your users. CDNs increase speed by caching documentation content in multiple data centers around the world, and then serving docs from the data center closest to the user.

We support CDNs on both of our sites:

-   

    On Read the Docs Community,

    :   we are able to provide a CDN to all the projects that we host. This service is graciously sponsored by [Cloudflare](https://www.cloudflare.com/).

-   

    On Read the Docs for Business,

    :   the CDN is included as part of all of our plans. We use [Cloudflare](https://www.cloudflare.com/) for this as well.

## CDN benefits[](#cdn-benefits "Link to this heading")

Having a CDN in front of your documentation has many benefits:

-   **Improved reliability**: Since docs are served from multiple places, one can go down and the docs are still accessible.

-   **Improved performance**: Data takes time to travel across space, so connecting to a server closer to the user makes documentation load faster.