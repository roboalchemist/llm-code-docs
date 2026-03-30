# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/security-kafka-consumer/using-sasl-ssl-kafka-consumer.md

# Using SASL SSL

Perform the following steps to set up SASL SSL security for PDI to connect to the Kafka broker:

1. On the **Setup** tab, select the **Direct** connection and use `${KAFKA_KERBEROS_SSL_URL}` as the URL.
2. On the **Options** tab, enter the options and values listed in the following table:

   | Option                       | Value                            |
   | ---------------------------- | -------------------------------- |
   | `auto.offset.reset`          | `latest`                         |
   | `ssl.truststore.location`    | `$[Path to Trust store]`         |
   | `ssl.truststore.password`    | `$[Trust store Password]`        |
   | `ssl.keystore.location`      | `$[Key store location]`          |
   | `ssl.keystore.password`      | `$[Key store password]`          |
   | `ssl.key.password`           | `$[ Key password]`               |
   | `security.protocol`          | `SASL_SSL`                       |
   | `sasl.mechanism`             | `PLAIN`                          |
   | `sasl.kerberos.service.name` | `${KERBEROS_KAFKA_SERVICE_NAME}` |
   | `sasl.jaas.config`           | `${SASL_JAAS_CONFIG}`            |
3. Click **OK**.

For more information on Kafka Kerberos connectivity, see <https://docs.confluent.io/platform/current/kafka/authentication_sasl/authentication_sasl_gssapi.html>
