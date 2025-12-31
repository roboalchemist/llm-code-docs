# Source: https://upstash.com/docs/workflow/integrations/prometheus.md

# Source: https://upstash.com/docs/redis/integrations/prometheus.md

# Source: https://upstash.com/docs/qstash/integrations/prometheus.md

# Source: https://upstash.com/docs/workflow/integrations/prometheus.md

# Source: https://upstash.com/docs/redis/integrations/prometheus.md

# Source: https://upstash.com/docs/qstash/integrations/prometheus.md

# Source: https://upstash.com/docs/workflow/integrations/prometheus.md

# Source: https://upstash.com/docs/redis/integrations/prometheus.md

# Source: https://upstash.com/docs/qstash/integrations/prometheus.md

# Source: https://upstash.com/docs/workflow/integrations/prometheus.md

# Source: https://upstash.com/docs/redis/integrations/prometheus.md

# Source: https://upstash.com/docs/qstash/integrations/prometheus.md

# Source: https://upstash.com/docs/workflow/integrations/prometheus.md

# Source: https://upstash.com/docs/redis/integrations/prometheus.md

# Source: https://upstash.com/docs/qstash/integrations/prometheus.md

# Source: https://upstash.com/docs/workflow/integrations/prometheus.md

# Prometheus - Upstash QStash Integration

To monitor your QStash metrics in Prometheus and visualize in Grafana, follow these steps:

<Check>
  **Integration Scope**

  Upstash Prometheus Integration covers Prod Pack.
</Check>

## **Step 1: Enable Prometheus in Upstash Console**

1. Open the Upstash Console and navigate to QStash.
2. Go to Settings → Monitoring.
3. Enable Prometheus to allow scraping QStash metrics.

<img src="https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/configuration-qstash.png?fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=09012029cd0b26d17391faadd590d250" alt="configuration.png" data-og-width="1956" width="1956" data-og-height="680" height="680" data-path="img/prometheus/configuration-qstash.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/configuration-qstash.png?w=280&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=9a8b41e736632ca22cdb6a9c1418be24 280w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/configuration-qstash.png?w=560&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=017a60eb3cd76ca2167b565acd8cffcd 560w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/configuration-qstash.png?w=840&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=465c0808c488881e9e7b75ab2630eca4 840w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/configuration-qstash.png?w=1100&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=ad55da6d698ba3afbe35a4e2f583bfb8 1100w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/configuration-qstash.png?w=1650&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=3ca73f05137987eeac02f6f8da3f2b8f 1650w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/configuration-qstash.png?w=2500&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=096f8dd337e73b3b37232fd14646eed8 2500w" />

## **Step 2: Copy Monitoring Token**

1. After enabling, a monitoring token is generated and displayed.
2. Copy the token. It will be used to authenticate Prometheus requests.

<Check>
  **Header Format**

  Send the token as `Authorization: Bearer <MONITORING_TOKEN>`.
</Check>

<img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/monitoring-token.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2618f754b9209f28f30d27b16a652786" alt="monitoring-token.png" data-og-width="950" width="950" data-og-height="520" height="520" data-path="img/prometheus/monitoring-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/monitoring-token.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=bd809c06e4421719c1195a3542a16cfb 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/monitoring-token.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=b2721266c30939e15e371087ba8d8531 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/monitoring-token.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=dbf58ef63addcf094f3cd2ea1e4ddd2b 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/monitoring-token.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=65e3183a923ab6bfcb7c1e55cbce5a27 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/monitoring-token.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=0d9ad474b754c5a3ac37fff5155f22c0 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/monitoring-token.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=bb17a652adc3478d3b68704d29886aa4 2500w" />

## **Step 3: Configure Prometheus (via Grafana Data Source)**

1. In Grafana, add a Prometheus data source.
2. Set the address to `https://api.upstash.com/monitoring/prometheus`.
3. In HTTP headers, add the monitoring token.

<img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=3dce2b10059a2eb96d8d560bdabb7303" alt="datasource.png" data-og-width="1848" width="1848" data-og-height="464" height="464" data-path="img/prometheus/datasource.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=325217df537ca2f7269c4d38803b952f 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=9264339789011443e61167e443c0ae8a 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=c1a7c769e5b857d21a733aec149233a8 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=1e156eabf6c5c92c9ab2aa54d175667a 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=eb464cb41c5bc5d8906f09c6a70f5c2b 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=9a0c6ef2b3f5989c557a6b9d054dc0b7 2500w" />

<img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/headers.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=f32611d6c8cedb2b6a73d21e9b8a1cd5" alt="headers.png" data-og-width="1322" width="1322" data-og-height="346" height="346" data-path="img/prometheus/headers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/headers.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=613ce8cdff83bfadfbd95e40fac9548f 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/headers.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=c3edb89b53a21ffc79173c03e0c0bd7b 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/headers.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=d624ffcce430e3014319386a7de649d5 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/headers.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=4fb91d8f22449f95fc91704839fb1eb5 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/headers.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=6a5a66bed411dde641fbcf8a6111de7d 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/headers.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=1f60d9ffdf856ad140c8f470e1e9028e 2500w" />

Click <b>Test and Save</b>.

<img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource-final.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=6e3f9cc214486c59085fe036a0dd6a28" alt="datasource-final.png" data-og-width="1560" width="1560" data-og-height="412" height="412" data-path="img/prometheus/datasource-final.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource-final.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=a97d2c20d4cae7002e57524de561937b 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource-final.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=e93e44229ab80a44a9115225b65c8742 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource-final.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2d542697335e6b8e3ca346cd5371292d 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource-final.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=bde3d4b76f3d4f0f4712a307d1d90f12 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource-final.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=a15201c139e232a3ca6a6599e35a119a 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/prometheus/datasource-final.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2950933a8fb225e5ddfc04143a36a111 2500w" />

## **Step 4: Import Dashboard**

You can use the Upstash Grafana dashboard to visualize QStash metrics.

Open the import dialog and use: <a href="https://grafana.com/grafana/dashboards/24206-upstash-qstash-dashboard/">Upstash QStash Dashboard</a>

<img src="https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/grafana-qstash-dashboard.png?fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=e5deb2b23457a82d894690267e19fc7f" alt="grafana-dashboard.png" data-og-width="2978" width="2978" data-og-height="1250" height="1250" data-path="img/prometheus/grafana-qstash-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/grafana-qstash-dashboard.png?w=280&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=8604c43b9ff9932d5546baf4ae13c91f 280w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/grafana-qstash-dashboard.png?w=560&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=d9655dfabe3b43851627c919ff25a307 560w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/grafana-qstash-dashboard.png?w=840&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=d9c01c7d9cb73274aa769c592f2e32c2 840w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/grafana-qstash-dashboard.png?w=1100&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=d6326a999c61be656b3f516de281d338 1100w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/grafana-qstash-dashboard.png?w=1650&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=ff94bf6ba50c4bb30d3af1d4545c5459 1650w, https://mintcdn.com/upstash/OUAG0YZr1j5tyfjW/img/prometheus/grafana-qstash-dashboard.png?w=2500&fit=max&auto=format&n=OUAG0YZr1j5tyfjW&q=85&s=d0a6c38bf6890cc44aa95843ffc952d5 2500w" />

## **Conclusion**

You’ve integrated QStash with Prometheus. Use Grafana to explore message throughput, retries, DLQ, schedules, and Upstash Workflows.

If you encounter issues, contact support.
