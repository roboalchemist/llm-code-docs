orphan

:

nosearch

:

[Elasticsearch](https://www.elastic.co) provides enterprise-scale
deployments with optimized search performance and prevents performance
degradation and timeouts. Elasticsearch allows you to search large
volumes of data quickly, in near real-time, by creating and managing an
index of post data. Mattermost's implementation uses
[Elasticsearch](https://www.elastic.co) as a distributed, RESTful search
engine supporting highly efficient database searches in a
`cluster environment </administration-guide/scale/high-availability-cluster-based-deployment>`{.interpreted-text
role="doc"}. Visit the
`Mattermost Elasticsearch product documentation </administration-guide/scale/elasticsearch-setup>`{.interpreted-text
role="doc"} for deployment and configuration details.

Performance monitoring support enables a Mattermost server to track
system health for large Enterprise deployments through integrations with
[Prometheus](https://prometheus.io/) and
[Grafana](https://grafana.com/). These integrations support data
collection from several Mattermost servers, which is particularly useful
if you're running Mattermost
`in high availability mode </administration-guide/scale/high-availability-cluster-based-deployment>`{.interpreted-text
role="doc"}. Once you're tracking system health, you can
`set up performance alerts </administration-guide/scale/performance-alerting>`{.interpreted-text
role="doc"} on your Grafana dashboard. Visit the
`Mattermost Performance Monitoring product documentation </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`{.interpreted-text
role="doc"} for installation details.
