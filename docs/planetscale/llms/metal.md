# Source: https://planetscale.com/docs/metal.md

# PlanetScale Metal

> PlanetScale Metal databases are the same PlanetScale databases you know and love, powered by blazing-fast, locally-attached NVMe SSD drives instead of network-attached storage.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=6fa63babac9db310367e4ececce42342" className="block dark:hidden" alt="Metal SSD" data-og-width="1944" width="1944" data-og-height="622" height="622" data-path="docs/metal/metal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=23b7923d9634dc6ec215881a525a489f 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=66b25d4361d98825ccaab8cb3de820d5 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=88c6c30ebbab7a7c620eb6de4a00e04f 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=abc5751a04c65ae70b66ac46953a9d53 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=97c778134c92e179200133981a1d4688 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=1167f19fa5ac256ccf1d9aac70cfd4c4 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-darkmode.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=19467d0c351d6d43217647b6a80d5dc3" className="hidden dark:block" alt="Metal SSD" data-og-width="1942" width="1942" data-og-height="622" height="622" data-path="docs/metal/metal-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-darkmode.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=a3a8ccebf57d21f52be8b50a29c6253a 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-darkmode.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=063ff77e9f103f51ca3e99fcd22a6cea 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-darkmode.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=0da7b850f8b2e6653be2d408751a91d7 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-darkmode.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=89fcf7f2087b6a457dc15e8a9b72bd7a 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-darkmode.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b74b787dfd44297af0616a3f23451340 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-darkmode.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=2981b8cfe043f9beb2e2396b042c9f52 2500w" />
</Frame>

This translates to significant latency reduction, more consistent IO performance, and unlimited I/O Operations Per Second (IOPS).
Metal is an excellent choice for high-IOPS and other performance-critical workloads.
With Metal, your database now has the ability to use modern NVMe SSD technology to its full potential.

**Note**: Metal nodes for Postgres now [start at \$50/month](https://planetscale.com/blog/50-dollar-planetscale-metal-is-ga-for-postgres).

## Using a Metal database

PlanetScale databases come in two main flavors: **Metal** and **network-attached storage**.
When you create a database on PlanetScale, you can choose between these two options:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=9826423b1d67d10f3d5fce0f9f14670e" className="block dark:hidden" alt="Choose between network attached storage and Metal" data-og-width="2674" width="2674" data-og-height="1428" height="1428" data-path="docs/metal/nas-and-metal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5a420ad6b359c2d601955c0f4d68b93b 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=f54e9eae31f1a1131d6c2ee16552e5d4 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=1d62414617f67cdf791ca18e0c81a539 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=6e58774fc39eb3dd31fa94ac7c152366 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=4206456b5c08db803902de8a9cb69123 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=f54d5c9b6429bcbc54067ef50c3b4a6b 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal-darkmode.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b1206c3cc112a3a66a552d17e812a05d" className="hidden dark:block" alt="Choose between network attached storage and Metal" data-og-width="2674" width="2674" data-og-height="1428" height="1428" data-path="docs/metal/nas-and-metal-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal-darkmode.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5db530e5342b965174bcbc76ec3f27ca 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal-darkmode.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=51d44ddeda2105f9a45b38844b806b40 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal-darkmode.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=e1289d6270bd558c14d0915ec4281aba 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal-darkmode.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=a939ea1001839aac12595098fcd96520 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal-darkmode.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=ef0d0c8b707179690e9ff825de06b1eb 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/nas-and-metal-darkmode.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=44a42d35d3b2cf7e8eee812ac706c07f 2500w" />
</Frame>

<Warning>
  The storage for Metal databases does not autoscale.
  It is important to keep a close eye on the storage capacity of Metal databases, and upgrade well before running out of space.
</Warning>

When you create a Metal database, you must choose a drive size up front.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=700f7bcb7ad62ff4cd8d9f3d24723867" className="block dark:hidden" alt="Select storage drive size for a Metal database" data-og-width="3788" width="3788" data-og-height="1944" height="1944" data-path="docs/metal/metal-drive-size.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=6327c6a1713e978dc728bcb7f0fbeff0 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=dec1dc601b224d275e8ef1b8eb346d80 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=313bc6ae9ca833a3a8567587b5b4b407 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=414a67e200f9663b083bac34128a01a9 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=0217a3b280b0f12b256a76757bb07a67 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=a43313432785d24726b65a3cd2de10e4 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size-darkmode.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=77e0875ce2cc316845ddd77e3f54ffd5" className="hidden dark:block" alt="Select storage drive size for a Metal database" data-og-width="3790" width="3790" data-og-height="1944" height="1944" data-path="docs/metal/metal-drive-size-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size-darkmode.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=8b67ace76e2a4ea20f55a449b46c9e7d 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size-darkmode.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=90e9d680aa707a94e76ac4b95e01d34f 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size-darkmode.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=7353dc7e0028200ccc82da15cf53d679 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size-darkmode.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=30d5e052771db5486cd7de506db2d9ca 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size-darkmode.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b20abb1ba68d7178878b1a71f04c9245 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-drive-size-darkmode.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5770bb74c4275b8e67a7fe7a2e4e6ad7 2500w" />
</Frame>

You should select a drive size that best suits your current data size, while also taking into account growth trends.
When the time comes that you need more storage, we make it easy to upgrade to larger NVMe drives with just a few clicks of a button.
You can learn more about creating and resizing Metal databases in our [creation and upgrade documentation](/docs/metal/create-a-metal-database).

## Monitoring your storage

Fixed-sized drives also means that you must closely monitor how much storage your database is using.
You can do so by looking at the storage information on the PlanetScale dashboard:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e2a6efe1aea907f77635a1e51059ef1c" className="block dark:hidden" alt="Storage indicator in PlanetScale" data-og-width="1450" width="1450" data-og-height="1290" height="1290" data-path="docs/metal/storage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=9888722ce397cc216335755e099f857b 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=aabba37339379838b3fcfdcce72e8771 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b8fd34859c301153cc7c1ab0abf9cbbf 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=66c4ee065707439a6767378f84c98dec 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7b9abb7a8ff0158e2eae04da1871decc 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a493eea4fc6feabe7e7869406198c870 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage-darkmode.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=986fd7f52435aadf1ccd83299b934fb0" className="hidden dark:block" alt="Storage indicator in PlanetScale" data-og-width="1450" width="1450" data-og-height="1290" height="1290" data-path="docs/metal/storage-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage-darkmode.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=3e50eaf82fc86bdf6b989dc8ab7fd7ec 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage-darkmode.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8293d74c8e663c23306fb1462b135ae4 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage-darkmode.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7c289f42543fa78211720be4cebbfe4d 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage-darkmode.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c3b920c4077c2a1684d9b49a4d286264 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage-darkmode.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d76e415348ad5cb56a8278b81d6b0b74 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/metal/storage-darkmode.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=9ce18ecc3d8d74035d728a1eb14fc637 2500w" />
</Frame>

We will send you email notices when your database storage reaches the following thresholds: 60%, 75%, 85%, 90%, 95%.
We will also email you when we estimate that your storage will run out in 1 week and 24 hours, based on recent usage trends.

Reaching or getting close to a drive's max capacity is dangerous and can lead to failures.
It's important to closely monitor your database's disk usage in the dashboard and check your regular storage email notifications.
We have an additional safeguard in place to protect your data: When we detect that your Metal disk has 6GiB or less of available space, we automatically switch it to read-only mode until resized.
Ideally, you should resize to a larger drive long before reaching this point.

## Workload suitability

Using Metal is a clear win for many workloads.
Many of our current Metal customers have been able to either (A) save money, (B) increase performance, or (C) do both at the same time by switching to Metal.
The per-GB cost of metal storage is more affordable than network-attached storage with high IOPS capacity, and the improved IO performance allows you to use smaller compute instances in some cases.

There are some scenarios where a network-attached storage database may be a better choice.
Here, we provide some general suggestions to help you choose the ideal type of database for your needs.
If you'd like a more personalized assessment, please [reach out to support](https://planetscale.com/contact?initial=support) with the specifics of your workload.

Generally, these types of database workloads are ideal for Metal:

* If your workload has significant I/O demands, Metal is an ideal choice.
  A network-attached storage database has limitations on how quickly it can read and write data due to the additional network hops.
  Metal databases allow you to unlock the full potential of modern NVMe technology, providing ultra-high throughput.
* If you have experience running up against the limits of AWS EBS IOPS or have a large `gp3` or `io2` `EBS` volume bill.
  Metal provides unlimited IOPS and will likely yield performance improvement, cost savings, or both.
  There is no need to pay extra for access to the I/O throughput of the local drive.
* If low-latency database performance is critical to your business needs.
* If you are concerned about long-tail p99+ performance.

However, there are some scenarios where choosing network-attached storage may still be preferable:

* Very small databases that have both low compute and low storage requirements may be better suited for network-attached storage.
* Databases where the majority of active rows fit in RAM.
  In this case, the I/O demand on the storage is probably low, and you won't see as much of a performance boost by using Metal.
* If you frequently resize your database, Metal may not be the best option.
  Metal instance resizes generally take longer than a network-attached storage resize as they require copying data between drives.

## Metal Performance

We've mentioned several times that Metal can provide you better performance.
What does that look like in practice?
Let's look at two examples.

### PlanetScale Insights

Below is a screenshot showing the p50 and p95 response times for the database that was powering PlanetScale Insights as of Q4 2024.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-insights-p50-p95.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=6246089292754f9a5e44c2ac3b61e4d9" alt="The effect of Metal on the Insights database" data-og-width="2796" width="2796" data-og-height="1906" height="1906" data-path="docs/metal/metal-insights-p50-p95.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-insights-p50-p95.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=c3d5d6435ce5d8fc3a935fe292ecf9cf 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-insights-p50-p95.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=fbc4015b39e06e8c8eb3963e3784fd27 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-insights-p50-p95.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=d574f2e7aa654b9d63e035103eb68c03 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-insights-p50-p95.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=28b4da04a3a595c5bb46e78106dc905d 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-insights-p50-p95.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=a05a186b44dfb7ca52e4a8002c7e40c5 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/metal-insights-p50-p95.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=327ac10020bbcbe188b566f4d240a40d 2500w" />
</Frame>

You can pretty clearly see when the database was switched over from network-attached storage instance types to Metal.
The p50 response times were cut in half, and the p95 had approximately a 7x improvement.

The workload was and continues to be very I/O bound.
The Insights database ingests a large amount of time-series data, and is frequently queried to pull the data that we use to generate graphs in Insights.
Metal provides a huge improvement for this type of workload.

### Large, sharded database

One of our existing customers runs several large, sharded databases.
We migrated these databases to Metal during the internal release of our product.
Below is a screenshot of the p99 latencies of a set of shards that we migrated from network-attached storage database to Metal instances.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-p99.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b014586040a54c142d7238427e2b3491" alt="The effect of Metal on a large sharded database" data-og-width="2956" width="2956" data-og-height="1390" height="1390" data-path="docs/metal/customer-p99.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-p99.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=36c2befa042b582ee8b8450d284b1074 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-p99.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=ee4dd70246f20a939962a631f4322300 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-p99.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=0233c515f1660a173cdbbb27fd7c4855 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-p99.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=9e193ee07495d7e38fb47eac48cf5361 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-p99.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=e75fb46197f08544b855b2b298b94d44 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-p99.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=ed3ac36dc16991043e735c4db96836b7 2500w" />
</Frame>

Though their p99 response times were already very good, Metal was able to further cut it in half.

### Cost and performance

We migrated yet another large customer during our internal release.
After switching to Metal, they saw a significant improvement in API call latency for one of their critical APIs.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-api-improvement.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=36e58b7cae7b9d7a1c60a001c28d573e" alt="API latency improvement" data-og-width="2854" width="2854" data-og-height="1228" height="1228" data-path="docs/metal/customer-api-improvement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-api-improvement.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=02bd5bd0b6bd0c3f75c9d53c74015b02 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-api-improvement.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=245b2c675bcf5d549a9667c03223964a 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-api-improvement.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b5c88348425602bece3e3c264ebf9050 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-api-improvement.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=51001ae24e50a89b53439755648d805d 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-api-improvement.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=98e6380eb3862ef675fc72fcae87081d 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-api-improvement.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=488299959319f1266e2efe2c11824bcd 2500w" />
</Frame>

We can clearly see that starting on Dec 20, the long tail of latency was reduced significantly.
This is due to the lower latency and improved consistency of local NVMe disk performance.

This same customer also saw some significant cost savings with their move to Metal.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-pricing-drop.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=ac730044638647cbceccbfe28200a2c9" alt="Cost savings with Metal" data-og-width="2552" width="2552" data-og-height="1728" height="1728" data-path="docs/metal/customer-pricing-drop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-pricing-drop.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=4b892ff4731ed98440ec7e3d4dba0b45 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-pricing-drop.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=bbfbf37f7dcfad0b197ab819b487668c 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-pricing-drop.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=537fecc860d51d6de35e280dafebce58 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-pricing-drop.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=87cc3be659719be54e23803d7a90ad7d 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-pricing-drop.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=17fce7faf8e35dfb64fb39c7e51d36bd 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/metal/customer-pricing-drop.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=afc6a46439ad4bee177a0b3419aa82a3 2500w" />
</Frame>

The performance of the database improved and the AWS costs to run dropped from over $100 per day to ~$30 per day.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt