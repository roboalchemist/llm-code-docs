# Source: https://screenshotone.com/docs/code-examples/java/

# Java SDK and Code Examples

import Alert from "@/components/Alert.astro";

<Alert>
    If you have any questions, please, reach out at `support@screenshotone.com`.
</Alert>

It takes minutes to start taking screenshots in Java. Just [sign up](https://dash.screenshotone.com/sign-up) to get access and secret keys, import the client, and you are ready to go.

### Installation

Add dependency to your `pom.xml`:

```xml
<dependencies>
    <dependency>
        <groupId>com.screenshotone.jsdk</groupId>
        <artifactId>screenshotone-api-jsdk</artifactId>
        <version>[1.0.0,2.0.0)</version>
    </dependency>
</dependencies>
```

### Usage

Generate a screenshot URL without executing request:

```java
import com.screenshotone.jsdk.Client;
import com.screenshotone.jsdk.TakeOptions;

public class App {
    public static void main(String[] args) throws Exception {
        final Client client = Client.withKeys("IVmt2ghj9TG_jQ", "Sxt94yAj9aQSgg");
        TakeOptions takeOptions = TakeOptions.url("https://scalabledeveloper.com")
                .fullPage(true)
                .deviceScaleFactor(1)
                .viewportHeight(1200)
                .viewportWidth(1200)
                .format("png")
                .omitBackground(true);
        final String url = client.generateTakeUrl(takeOptions);

        System.out.println(url);
        // Output: https://api.screenshotone.com/take?access_key=IVmt2ghj9TG_jQ&device_scale_factor=1&format=png&full_page=true&omit_background=true&url=https%3A%2F%2Fscalabledeveloper.com&viewport_height=1200&viewport_width=1200&signature=3c0c5543599067322e8c84470702330e3687c6a08eef6b7311b71c32d04e1bd5
    }
}
```

Usually you generate URL to place it inside the image tag (<img />) or to share it.

Take a screenshot and save the image in the file:

```java
import com.screenshotone.jsdk.Client;
import com.screenshotone.jsdk.TakeOptions;

import java.io.File;
import java.nio.file.Files;

public class App {
    public static void main(String[] args) throws Exception {
        final Client client = Client.withKeys("IVmt2ghj9TG_jQ", "Sxt94yAj9aQSgg");
        TakeOptions takeOptions = TakeOptions.url("https://scalabledeveloper.com")
                .fullPage(true)
                .deviceScaleFactor(1)
                .viewportHeight(1200)
                .viewportWidth(1200)
                .format("png")
                .omitBackground(true);
        final byte[] image = client.take(takeOptions);

        Files.write(new File("./example.png").toPath(), image);
    }
}
```

Check out [other SDKs and code examples](/docs/code-examples/).