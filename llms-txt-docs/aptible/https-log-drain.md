# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/https-log-drain.md

# How to set up a self-hosted HTTPS Log Drain

[HTTPS log drains](/core-concepts/observability/logs/log-drains/https-log-drains) enable you to direct logs to HTTPS endpoints. This feature is handy for configuring Logstash and redirecting logs to another location while applying filters or adding additional information. To that end, we provide a sample Logstash app you can deploy on Aptible to do so: [aptible/docker-logstash](https://github.com/aptible/docker-logstash).

Once you've deployed this app, expose it using the [How do I expose my web app on the Internet?](/how-to-guides/app-guides/expose-web-app-to-internet)) guide and then create a new HTTPS log drain to route logs there.
