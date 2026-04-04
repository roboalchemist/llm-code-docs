# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/jms-consumer/options-jms-consumer/security-tab-jms-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-consumer/options-jms-consumer/security-tab-jms-consumer.md

# Security tab

![Security tab in JMS Consumer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-19ac7c9a3ec9a9f722bff8e3780e5186b45193c9%2FPDITransStep_JMSConsumer_SecurityTab.png?alt=media)

The **Security** tab includes the following authentication options and values:

| Option                  | Description                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Username**            | Specify the user name required to access the Active MQ or IBM MQ server.                                                                                       |
| **Password**            | Specify the password associated with the user name.                                                                                                            |
| **Use secure protocol** | Select to secure the message stream with the Secure Socket Layer (SSL) protocol. You can adjust the settings of the protocol through the SSL properties table. |

The following SSL values are available, depending on whether you use ActiveMQ or IBM MQ as the connection method for the step:

| Name                     | Value                                                                                                                                                                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ciphersuite**          | Specify a CipherSuite name. Values depend on the provider. For more details, see: <https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html>                                                                                                                    |
| **Context Algorithm**    | Specify the name of the secure protocol you are using.                                                                                                                                                                                                                                   |
| **FIPS required**        | IBM MQ only: Specify `True` to enable support for the Federal Information Processing Standard (FIPS). Specify `False` if FIPS is not required.                                                                                                                                           |
| **Key Store Password**   | Specify the password for the key store object you want this secure connection to use.                                                                                                                                                                                                    |
| **Key Store Path**       | Specify the file path location of the key store you want this secure connection to use.                                                                                                                                                                                                  |
| **Key Store Type**       | IBM MQ only: Specify the format of the key store.                                                                                                                                                                                                                                        |
| **SSL Provider**         | Active MQ only: Specify the SSL implementation you want to use, either JDK or OpenSSL.If you specify OpenSSL, you will need to provide the OpenSSL libraries. For details, see the ActiveMQ documentation: <https://activemq.apache.org/artemis/docs/latest/configuring-transports.html> |
| **Trust Store Password** | IBM MQ only: Specify the password for the trust store object you want this secure connection to use.                                                                                                                                                                                     |
| **Trust All**            | Active MQ only: Specify either `True` or `False`. `False` is recommended. Specify `True` if you want this connection to trust all certificates without validation. `True` is not recommended for production use.                                                                         |
| **Trust Store Path**     | Specify the file path location of the trust store certificates you want this secure connection to use.                                                                                                                                                                                   |
| **Trust Store Type**     | IBM MQ only: Specify the format of the trust store.                                                                                                                                                                                                                                      |
| **Verify Host**          | Active MQ only: Specify `True` if you want this secure connection to verify that the host server name matches its certificate. Specify `False` to omit host verification.                                                                                                                |
