# Source: https://documentation.mailgun.com/docs/mailgun/sdk/java_sdk.md

# Java

a
img

    Official Mailgun Java SDK

### Installation

To run the SDK, you will need **Java 1.8+**.  The recommended way to use the **Mailgun Java SDK** in your project:

Add the following to your `pom.xml`:


```xml
<dependencies>
  ...
  <dependency>
    <groupId>com.mailgun</groupId>
    <artifactId>mailgun-java</artifactId>
    <version>1.1.x</version>
  </dependency>
  ...
</dependencies>
```

Gradle Groovy DSL


```xml
implementation 'com.mailgun:mailgun-java:1.1.3'
```

### Usage

Here's a simple example on how to send an email. As always, please consult the repository readme for full details.


```java
Message message = Message.builder()
        .from(EMAIL_FROM)
        .to(USER_EMAIL)
        .subject(SUBJECT)
        .text(TEXT)
        .build();

MessageResponse messageResponse = mailgunMessagesApi.sendMessage(DOMAIN, message);
```