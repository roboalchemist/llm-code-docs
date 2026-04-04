# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-producer/security-kafka-producer/using-ssl-kafka-producer.md

# Using SSL

Perform the following steps to set up SSL security to connect to the Kafka broker:

1. On the **Setup**tab, select the **Direct** connection and enter `${KAFKA_ssl_url}` as the **Bootstrap servers** URL.
2. On the **Options** tab, enter the options and values listed in the following table:

   | Option                    | Value                    |
   | ------------------------- | ------------------------ |
   | `compression.type`        | `none`                   |
   | `ssl.truststore.location` | `$[Path to Trust store]` |
   | `ssl.truststore.password` | `$[Password]`            |
   | `ssl.keystore.location`   | `$[Path to Key store]`   |
   | `ssl.keystore.password`   | `$[ Key store password]` |
   | `ssl.key.password`        | `$[ Key password]`       |
   | `security.protocol`       | `SSL`                    |
   | `ssl.protocol`            | `TLS 1.2`                |
3. Click **OK**.
