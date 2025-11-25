# Source: https://resend.com/docs/send-with-java.md

# Send emails with Java

> Learn how to send your first email using the Resend Java SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

<CodeGroup>
  ```bash Gradle theme={null}
  implementation 'com.resend:resend-java:+'
  ```

  ```xml Maven theme={null}
  <dependency>
      <groupId>com.resend</groupId>
      <artifactId>resend-java</artifactId>
      <version>LATEST</version>
  </dependency>
  ```
</CodeGroup>

## 2. Send emails using HTML

```java Main.java theme={null}
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        CreateEmailOptions params = CreateEmailOptions.builder()
                .from("Acme <onboarding@resend.dev>")
                .to("delivered@resend.dev")
                .subject("it works!")
                .html("<strong>hello world</strong>")
                .build();

         try {
            CreateEmailResponse data = resend.emails().send(params);
            System.out.println(data.getId());
        } catch (ResendException e) {
            e.printStackTrace();
        }
    }
}
```

## 3. Try it yourself

<Card title="Java Examples" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-java-example">
  See the full source code.
</Card>
