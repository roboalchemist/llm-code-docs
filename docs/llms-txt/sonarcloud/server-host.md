# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/installation-requirements/server-host.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/installation-requirements/server-host.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/installation-requirements/server-host.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/installation-requirements/server-host.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/installation-requirements/server-host.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/installation-requirements/server-host.md

# SonarQube Server host

This section describes the general requirements, recommendations, and limitations for the machine running SonarQube Server in case of a ZIP, Docker, or Kubernetes installation. Additional requirements specific to an installation type may be mentioned in the respective installation section. For the Data Center Edition, see also [install-the-server-as-a-cluster](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server-as-a-cluster "mention").

{% hint style="info" %}
We recommend that for production installation, the database used by SonarQube Server is hosted on a machine that is physically separate from the SonarQube Server host, with low latency between both hosts.
{% endhint %}

{% hint style="info" %}
See also our reference architectures:

* [up-to-10m-loc](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/reference-architectures/up-to-10m-loc "mention")
* [up-to-50m-loc](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/reference-architectures/up-to-50m-loc "mention")
  {% endhint %}

### Limitations <a href="#limitations" id="limitations"></a>

Running SonarQube Server on environments where ElasticSearch-related Linux prerequisites can’t be met is not supported (see also [linux](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation/linux "mention")).

This concerns (the list is not exhaustive): Azure App Service, AWS App Runner, and AWS Fargate. Using these services may cause issues that will ultimately make SonarQube unreliable and unsuitable for enterprise production use.

The application models of Azure Container Instances (ACI) and Azure Container Apps (ACA) are not suitable for SonarQube, making their use not recommended.

### Supported operating systems <a href="#supported-os" id="supported-os"></a>

SonarQube Server can run on the following operating systems (note that z/OS is *not* supported):

* Linux (x64, AArch64)
* Windows (x64)
* macOS (x64, AArch64)

{% hint style="info" %}
SonarQube Server can run, with limitations, on Linux hosts where FIPS (Federal Information Processing Standard) is enabled. See [#fips-mode](https://docs.sonarsource.com/sonarqube-server/2025.1/pre-installation/linux#fips-mode "mention").
{% endhint %}

### Hardware requirements <a href="#hardware" id="hardware"></a>

In the table below:

* A small-scale installation is typically a SonarQube Community Build or SonarQube Server Developer Edition installation that supports up to 1M lines of code.
* A large-scale installation is typically a single-node installation of SonarQube Server Enterprise Edition that supports up to 50M lines of code, or a search or application node of a SonarQube Server Data Center Edition cluster.

{% hint style="info" %}
The requirements below should be considered a starting point for new installations. As usage patterns vary across installations, it is important that SonarQube Server instances are monitored for CPU, memory, and storage usage. Periodic adjustments may be necessary based on monitoring.
{% endhint %}

<table><thead><tr><th width="141">Category</th><th>Requirement</th></tr></thead><tbody><tr><td>RAM</td><td><p>For a small-scale installation:</p><p>• 4GB of RAM</p><p>For a large-scale installation:</p><p>• 16 GB of RAM</p></td></tr><tr><td>Processor</td><td><p>64-bit system.</p><p>For a small-scale installation:</p><p>• 2 cores</p><p>For a large-scale installation:</p><p>• 8 cores</p><p>In addition, for a server installation from a Docker image:</p><p>• amd64 architecture or arm64-based Apple Silicon</p></td></tr><tr><td>Disk space</td><td><p>Depends on how much code you analyze with SonarQube.</p><p>For a small-scale installation:</p><p>• 30 GB</p></td></tr><tr><td>Free disk space</td><td><p>10% free disk space.</p><p>Note: This requirement stems from Elasticsearch's susceptibility to crashing if disk usage exceeds its high disk watermark, which is set at 90% by default. For more information, see the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.17/fix-common-cluster-issues.html#_error_disk_usage_exceeded_flood_stage_watermark_index_has_read_only_allow_delete_block">Elasticsearch documentation</a>.</p></td></tr></tbody></table>

### Hardware configuration recommendations <a href="#hardware-recommendations" id="hardware-recommendations"></a>

[Elasticsearch](https://www.elastic.co/) is used by SonarQube Server in the background. To ensure good performance of your SonarQube Server, you need to follow these recommendations that are linked to Elasticsearch usage.

<table><thead><tr><th width="121">Category</th><th>Recommendation</th></tr></thead><tbody><tr><td>Disk</td><td><p>• Free disk space is an absolute requirement. Elasticsearch implements a safety mechanism to prevent the disk from being flooded with index data that locks all indices in read-only mode when a 95% disk usage watermark is reached.</p><p>• Disk access can easily become the bottleneck of Elasticsearch. If you can afford SSDs, they are by far superior to any spinning media. SSD-backed nodes see boosts in both query and indexing performance. If you use spinning media, try to obtain the fastest disks possible (high-performance server disks 15,000 RPM drives).</p><p>• Using RAID 0 is an effective way to increase disk speed, for both spinning disks and SSD. There is no need to use mirroring or parity variants of RAID because of Elasticsearch replicas and database primary storage.</p><p>• Do not use remote-mounted storage, such as NFS, SMB/CIFS, or network-attached storage (NAS). They are often slower, display larger latencies with a wider deviation in average latency, and are a single point of failure.</p><p>• You may put &#x3C;sonarqubeHome>/Data (where sonarqubeHome is the SonarQube Server installation directory; it is recommended to use /opt/sonarqube for this directory) into a separate partition to help alleviate the single point of failure mentioned above.</p></td></tr><tr><td>RAM</td><td><p>It is <a href="https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#_give_less_than_half_your_memory_to_lucene">recommended</a> that you give 50% of the available memory to Elasticsearch heap while leaving the other 50% free. The reason is that Lucene (used by Elasticsearch) is designed to leverage the underlying OS for caching in-memory data structures.</p><p>• Don’t allocate more than 32GB.</p><p>See the following Elasticsearch articles for more details:</p><p>• Elasticsearch Guide: Heap Sizing</p><p>• A Heap of Trouble</p><p>• Elasticsearch Reference: JVM heap size</p></td></tr><tr><td>CPU</td><td><p>If you need to choose between faster CPUs or more cores, then choose more cores. The extra concurrency that multiple cores offer will far outweigh a slightly faster clock speed.</p><p>By nature, data is distributed on multiple nodes, so execution time depends on the slowest node. It’s better to have multiple medium boxes than one fast and one slow.</p></td></tr><tr><td>I/O scheduler for SSD</td><td><p>If you use SSD, do not use the CFQ (Completely Fair Queuing) I/O scheduler (this is the defaul I/O scheduler under most Unix distributions). Use either the deadline or the NOOP scheduler instead.</p><p>When you write data to disk, the I/O Scheduler decides when that data is actually sent to the disk. The CFQ allocates "time slices" to each process, and then optimizes the delivery of these various queues to the disk. It is optimized for spinning media: the nature of rotating platters means it is more efficient to write data to disk based on physical layout. The deadline scheduler optimizes based on how long writes have been pending, while NOOP is just a simple FIFO queue.</p></td></tr><tr><td>Hard drives</td><td><p>They should have excellent read and write performance.</p><p>Most importantly, the "data" folder houses the Elasticsearch indices on which a huge amount of I/O will be done when the server is up and running. Read and write hard drive performance will therefore have a big impact on the overall SonarQube Server host performance.</p></td></tr></tbody></table>

### Software requirements <a href="#software-requirements" id="software-requirements"></a>

<table><thead><tr><th width="183">Category</th><th>Requirement</th></tr></thead><tbody><tr><td>Client web browser</td><td><p>• Microsoft Edge: latest version</p><p>• Mozilla Firefox: latest version</p><p>• Google Chrome: latest version</p><p>• Safari: latest version</p></td></tr><tr><td>Java</td><td><p>Applies only to a server installation from the ZIP file.</p><p>• Oracle JRE or OpenJDK</p><p>• Java version 17 or 21</p><p>• Recommendation: Use Java CPU (critical patch update) releases.</p><p>Note: SonarQube Server is able to analyze any kind of Java source files regardless of the version of Java they comply with.</p></td></tr></tbody></table>
