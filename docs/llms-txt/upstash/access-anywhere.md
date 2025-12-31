# Source: https://upstash.com/docs/common/concepts/access-anywhere.md

# Access Anywhere

Upstash has integrated REST APIs into all its products to facilitate access from various runtime environments. This integration is particularly beneficial for edge runtimes like Cloudflare Workers and Vercel Edge, which do not permit TCP connections, and for serverless functions such as AWS Lambda, which are stateless and do not retain connection information between invocations.

### Rationale

The absence of TCP connection support in edge runtimes and the stateless nature of serverless functions necessitate a different approach for persistent connections typically used in traditional server setups. The stateless REST API provided by Upstash addresses this gap, enabling consistent and reliable communication with data stores from these platforms.

### REST API Design

The REST APIs for Upstash services are thoughtfully designed to align closely with the conventions of each product. This ensures that users who are already familiar with these services will find the interactions intuitive and familiar. Our API endpoints are self-explanatory, following standard REST practices to guarantee ease of use and seamless integration.

<img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/access-anywhere/restclient.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=f43d16d28819cb7fcfc638d0ff3f1bcd" data-og-width="1794" width="1794" data-og-height="1068" height="1068" data-path="img/access-anywhere/restclient.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/access-anywhere/restclient.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=95619248d2e0708920b3bea3dd63b708 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/access-anywhere/restclient.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=de7b8b47d89984545fdf6ba920d0051a 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/access-anywhere/restclient.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=126149df464792fdcb207bbeb754e762 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/access-anywhere/restclient.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=53fca51a6018d81c20597422924dc19e 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/access-anywhere/restclient.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=6a6d36def36560186aa9ce2261f78d2d 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/access-anywhere/restclient.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=859e252db002c24c77e77f1470f0f180 2500w" />

### SDKs for Popular Languages

To enhance the developer experience, Upstash is developing SDKs in various popular programming languages. These SDKs simplify the process of integrating Upstash services with your applications by providing straightforward methods and functions that abstract the underlying REST API calls.

### Resources

[Redis REST API Docs](/redis/features/restapi)

[QStash REST API Docs](/qstash/api/authentication)

[Redis SDK - Typescript](https://github.com/upstash/upstash-redis)

[Redis SDK - Python](https://github.com/upstash/redis-python)

[QStash SDK - Typescript](https://github.com/upstash/sdk-qstash-ts)
