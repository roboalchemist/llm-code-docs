# Source: https://docs.verda.com/clusters/instant-clusters/monitoring.md

# Monitoring

Our instant clusters come with a dashboards and customizable alerts, to monitor the state of the cluster.

To access the dashboard navigate to the cluster dropdown and select **View metric dashboard**.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-684b88276f6c65e63fba34f9f678eb463615a40d%2Fcluster%20view%20metrics.png?alt=media" alt=""><figcaption></figcaption></figure>

To access the Grafana portal, follow the provided instructions to obtain the address and login details. If prompted with a certificate warning (common with self-signed certificates), select **Advanced** and then **Proceed to …** to continue. The password can be retrieved from the jump host.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-d9be180153929fe69ed7a101b91b11ef9b6c57d2%2Fhow%20to%20metrics.png?alt=media" alt=""><figcaption></figcaption></figure>

Once logged in, navigate to the **Dashboards** section in the side menu. Four pre-configured dashboards are available:

* **GPU Overview** – General GPU monitoring.
* **NVIDIA DCGM** – Metrics from the DCGM exporter.
* **Node Exporter Full** – Detailed hardware and OS-level system metrics.
* **SLURM Dashboard** – Monitoring of SLURM job activity.

The cluster is also pre-configured with several alerting rules, which can be viewed under the **Alerts** tab. Hardware-related alerts are automatically forwarded to Verda for faster resolution. Additional alerts can be created and customized to notify through Grafana’s contact points by editing the **grafana-default-email** channel. This allows customer-specific alerts to be routed to any contact point defined by the customer directly within the Grafana UI.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-7d73aebf401d4942a8634f566dced5b3b3c5f9b1%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-5a828ba129e4f492a4def5327c3e3c9ec210e5fb%2FScreenshot%202025-08-15%20at%2014.55.36.png?alt=media" alt=""><figcaption></figcaption></figure>
