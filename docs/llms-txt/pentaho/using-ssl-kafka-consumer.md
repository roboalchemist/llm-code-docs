# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/security-kafka-consumer/using-ssl-kafka-consumer.md

# Using SSL

Perform the following steps to set up SSL security to connect to the Kafka broker:

1. On the **Setup**tab, select the **Direct** connection and enter `${KAFKA_ssl_url}` as the **Bootstrap servers** URL.
2. On the **Options** tab, enter the options and values listed in the following table:

   | Option                    | Value                     |
   | ------------------------- | ------------------------- |
   | `auto.offset.reset`       | `latest`                  |
   | `ssl.key.password`        | `$[Key password]`         |
   | `ssl.keystore.location`   | `$[Path to Key store]`    |
   | `ssl.keystore.password`   | `$[Key store password]`   |
   | `ssl.truststore.location` | `$[Path to Trust store]`  |
   | `ssl.truststore.password` | `$[Trust store Password]` |
   | `ssl.protocol`            | `TLS 1.2`                 |
   | `security.protocol`       | `SSL`                     |
3. Click **OK**.
