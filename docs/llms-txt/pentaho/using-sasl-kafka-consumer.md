# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/security-kafka-consumer/using-sasl-kafka-consumer.md

# Using SASL

SASL security requires the Kerberos configuration file `krb5.conf` and a Kerberos principal. You must obtain these from your Kerberos administrator.

Perform the following steps to set up SASL security for PDI to connect to the Kafka broker:

1. Copy the `krb5.conf` file to the `${JAVA_HOME}/conf/security` directory.
2. Run the kinit command `${KERBEROS_PRINCIPAL_KAFKA}` to initiate the authentication process to obtain a Kerberos ticket-granting ticket (TGT).
3. Copy the `${KERBEROS_PRINCIPAL_KAFKA}`.keytab from the server to the workstation where PDI is installed.
4. On the **Setup** tab, select the **Direct** connection and enter `${KAFKA_SASL_PLAINTEXT_URL}` as the **Bootstrap servers** URL.
5. On the **Options** tab, enter the options and values listed in the following table:

   | Option                       | Value                            |
   | ---------------------------- | -------------------------------- |
   | `auto.offset.reset`          | `latest`                         |
   | `security.protocol`          | `SASL_PLAINTEXT`                 |
   | `sasl.mechanism`             | `GSSAPI`                         |
   | `sasl.kerberos.service.name` | `${KERBEROS_KAFKA_SERVICE_NAME}` |
   | `sasl.jaas.config`           | `${SASL_JAAS_CONFIG}`            |
6. Click **OK**.

**Note:** The following is a sample format of `${SASL_JAAS_CONFIG}`

```
com.sun.security.auth.module.Krb5LoginModule required useKeyTab=true storeKey=true  debug=true doNotPrompt=true keyTab="Path to ${KERBEROS_PRINCIPAL_KAFKA}.keytab" principal="${Pricipal created in Kerberos for Kafka}";
```
