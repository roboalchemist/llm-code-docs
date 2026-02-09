# Source: https://upstash.com/docs/common/concepts/global-replication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Global Replication

> Global Replication for Low Latency and High Availability

Upstash Redis automatically replicates your data to the regions you choose, so your application stays fast and responsive-no matter where your users are.

Add or remove regions from a database at any time with zero downtime. Each region acts as a replica, holding a copy of your data for low latency and high availability.

***

## Built for Modern Serverless Architectures

In serverless computing, performance isn't just about fast code—it's also about fast, reliable data access from anywhere in the world. Whether you're using Vercel Functions, Cloudflare Workers, Fastly Compute, or Deno Deploy, your data layer needs to be as distributed and flexible as your compute for best performance.

Upstash Global replicates your Redis data across multiple regions to:

* Minimize round-trip latency
* Guarantee high availability at scale

...even under heavy or dynamic workloads. Our HTTP-based Redis® client is optimized for serverless environments and delivers consistent performance under high concurrency or variable workloads.

As serverless platforms evolve with features like in-function concurrency (e.g. [Vercel's Fluid Compute](https://vercel.com/fluid)), you need a data layer that can keep up. Upstash Redis is a globally distributed, low-latency database that scales with your compute, wherever it runs.

***

## How Global Replication Works

To minimize latency for read operations, we use a replica model. Our tests show sub-millisecond latency for read commands in the same AWS region as the Upstash Redis® instance.

**Read commands are automatically served from the geographically closest replica**:

<Frame>
  <img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/reads.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=05494e62471be046bd28d67cf1512d76" data-og-width="1875" width="1875" data-og-height="1080" height="1080" data-path="img/global-replication/reads.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/reads.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=e1c5fa1c9318a0a61be5e03fccaed448 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/reads.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=3db4f635f9731992361c68e8df7078a4 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/reads.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=a176acbe9614747a547ce738e7d03af3 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/reads.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=a08820e00abf2150a38dd5f9d88e744c 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/reads.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=fd01b30bf0644990a6ec868ea77bc946 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/reads.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=d93bb0f07197513fa4eb58aefd9ccb2f 2500w" />
</Frame>

**Write commands go to the primary database** for consistency. After a successful write, they are replicated to all read replicas:

<Frame>
  <img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/writes.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=b31700f08a8eb664796af4d6988fc1fc" data-og-width="1875" width="1875" data-og-height="1080" height="1080" data-path="img/global-replication/writes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/writes.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=c919bf353cd650f5ca18310a4a8f96f7 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/writes.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=adb9b77e0d43d568baf7e143d825a261 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/writes.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=a37546d0af4da9b10e3612432200bf7d 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/writes.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=56173635091569ba3787e188c69218d6 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/writes.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=faa467a7ae8e72eff11753733e800a06 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/writes.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=947703a4e20b64048a6242ef2171debd 2500w" />
</Frame>

***

## Available Regions

To create a globally distributed database, select a primary region and the number of read regions:

* Select a primary region for most write operations for best performance.
* Select read regions close to your users for optimized read speeds.

Each request is then automatically served by the closest read replica for maximum performance and minimum latency:

<Frame>
  <img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/replication.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=3a5942c2dd718dcf3fccf8ddb6f46359" data-og-width="1875" width="1875" data-og-height="1080" height="1080" data-path="img/global-replication/replication.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/replication.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=89b4a8f2b9146283bdc6d409444b1faf 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/replication.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=9a8f70e543ae9ec07b2c43df05937373 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/replication.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=b1641dd97bf53fed8bd23b9323d5ac17 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/replication.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=efbac6a590f767fda4335603a87adc39 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/replication.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=1b1ee1fdf0c6150362c60dd17d880817 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/global-replication/replication.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=968984eebce41c2948e84fe6b083f35f 2500w" />
</Frame>

**You can create read replicas in the following regions:**

* AWS US-East-1 (North Virginia)
* AWS US-East-2 (Ohio)
* AWS US-West-1 (North California)
* AWS US-West-2 (Oregon)
* AWS EU-West-1 (Ireland)
* AWS EU-West-2 (London)
* AWS EU-Central-1 (Frankfurt)
* AWS AP-South-1 (Mumbai)
* AWS AP-Northeast-1 (Tokyo)
* AWS AP-Southeast-1 (Singapore)
* AWS AP-Southeast-2 (Sydney)
* AWS SA-East-1 (São Paulo)

Check out [our blog post](https://upstash.com/blog/global-database) to learn more about our global replication philosophy. You can also explore our [live benchmark](https://latency.upstash.com/) to see Upstash Redis latency from different locations around the world.
