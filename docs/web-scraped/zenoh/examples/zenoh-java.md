# Zenoh Examples: zenoh-java

# Zenoh Java examples

----

## Start instructions

For running the examples, there are two approaches. Either you run the gradle example task with the syntax `gradle <example> --args="<arguments>"` or you can build fat JARs the examples through the task `gradle buildExamples`.

While both are valid, in this document we'll follow the second approach; when running `gradle buildExamples`, all the JARs will be located under `/examples/build/libs`, which can later be executed

```bash
java -jar <Example>.jar <arguments>
```

for instance

```bash
java -jar ZPub.jar -h
```

will return

```bash
Usage: ZPub [-hV] [--no-multicast-scouting] [-a=<attachment>] [-c=<configFile>]
            [-k=<key>] [-m=<mode>] [-v=<value>] [-e=<connect>[,
            <connect>...]]... [-l=<listen>[,<listen>...]]...
Zenoh Pub example
  -a, --attach=<attachment>
                        The attachments to add to each put. The key-value pairs
                          are &-separated, and = serves as the separator
                          between key and value.
  -c, --config=<configFile>
                        A configuration file.
  -e, --connect=<connect>[,<connect>...]
                        Endpoints to connect to.
  -h, --help            Show this help message and exit.
  -k, --key=<key>       The key expression to write to [default:
                          demo/example/zenoh-java-pub].
  -l, --listen=<listen>[,<listen>...]
                        Endpoints to listen on.
  -m, --mode=<mode>     The session mode. Default: peer. Possible values:
                          [peer, client, router].
      --no-multicast-scouting
                        Disable the multicast-based scouting mechanism.
  -v, --value=<value>   The value to write. [default: 'Pub from Java!']
  -V, --version         Print version information and exit.
```

The connect and listen parameters (that are common to all the examples) accept multiple repeated inputs.
For instance:

```bash
java -jar ZPub.jar -l tcp/localhost:7447 -l tcp/localhost:7448 -l tcp/localhost:7449
```

There is the possibility to provide a Zenoh config file as follows

```bash
java -jar ZPub.jar -c path/to/config.json5
```

In that case, any other provided configuration parameters through the command line interface will not be taken into consideration.

One last comment regarding Zenoh logging for the examples, logs from the native library can be enabled through the environment variable `RUST_LOG` as follows:

```bash
RUST_LOG=<level> java -jar ZPub.jar
```

where `<level>` is the log filter (for instance `debug`, `warn`, `error`... (see the [Rust documentation](https://docs.rs/env_logger/latest/env_logger/#enabling-logging))).

----

## Examples description

### ZPub

Declares a resource with a path and a publisher on this resource. Then puts a value using the numerical resource id.
The path/value will be received by all matching subscribers, for instance the [ZSub](#zsub) example.

Usage:

```bash
java -jar ZPub.jar
```

or

```bash
java -jar ZPub.jar -k demo/example/test -v "hello world"
```

### ZSub

Creates a subscriber with a key expression.
The subscriber will be notified of each put made on any key expression matching
the subscriber's key expression, and will print this notification.

Usage:

```bash
java -jar ZSub.jar
```

or

```bash
java -jar ZSub.jar -k demo/example/test
```

### ZGet

Sends a query message for a selector.
The queryables with a matching path or selector (for instance [ZQueryable](#zqueryable))
will receive this query and reply with paths/values that will be received by the query callback.

```bash
java -jar ZGet.jar
```

or

```bash
java -jar ZGet.jar -s demo/example/get
```

### ZPut

Puts a path/value into Zenoh.
The path/value will be received by all matching subscribers, for instance the [ZSub](#zsub).

Usage:

```bash
java -jar ZPut.jar
```

or

```bash
java -jar ZPut.jar -k demo/example/put -v 'Put from Java!'
```

### ZDelete

Performs a Delete operation into a path/value into Zenoh.

Usage:

```bash
java -jar ZDelete.jar
```

or

```bash
java -jar ZDelete.jar -k demo/example/delete
```

### ZQueryable

Creates a queryable function with a key expression.
This queryable function will be triggered by each call to a get operation on zenoh
with a selector that matches the key expression, and will return a value to the querier.

Usage:

```bash
java -jar ZQueryable.jar
```

or

```bash
java -jar ZQueryable.jar -k demo/example/query
```

### ZPubThr & ZSubThr

Pub/Sub throughput test.
This example allows to perform throughput measurements between a publisher performing
put operations and a subscriber receiving notifications of those puts.

Subscriber usage:

```bash
java -jar ZSubThr.jar
```

Publisher usage:

```bash
java -jar ZPubThr.jar <payload_size>
```

### ZPing & ZPong

Latency tests

```bash
java -jar ZPing.jar
```

```bash
java -jar ZPong.jar
```

### ZScout

A scouting example. Will show information from other nodes in the Zenoh network.

```bash
java -jar ZScout.jar
```

### Liveliness examples

#### ZLiveliness

The ZLiveliness example, it just announces itself to the Zenoh network by default to the key expression `group1/zenoh-java`.

Usage:

```bash
java -jar ZLiveliness
```

It can be used along with the following liveliness examples:

#### ZGetLiveliness

Gets the liveliness tokens, by default to `group1/zenoh-java`.

Usage:

```bash
java -jar ZGetLiveliness
```

#### ZSubLiveliness

Subscribes to liveliness events:

```bash
java -jar ZSubLiveliness
```

---

# Example: examples--src--main--java--io--zenoh--Config.kt

```kt
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh

import kotlinx.serialization.Serializable
import kotlinx.serialization.SerialName
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.encodeToJsonElement
import kotlin.io.path.Path

@Serializable
data class ConfigData(
    @SerialName("connect") var connect: Connect? = null,
    @SerialName("listen") var listen: Listen? = null,
    @SerialName("mode") var mode: String? = null,
    @SerialName("scouting") var scouting: Scouting? = null,
)

@Serializable
data class Connect(
    @SerialName("endpoints") var endpoints: List<String>
)

@Serializable
data class Listen(
    @SerialName("endpoints") var endpoints: List<String>
)

@Serializable
data class Scouting(
    @SerialName("multicast") var multicast: Multicast,
)

@Serializable
data class Multicast(
    @SerialName("enabled") var enabled: Boolean,
)

internal fun loadConfig(
    emptyArgs: Boolean,
    configFile: String?,
    connectEndpoints: List<String>?,
    listenEndpoints: List<String>?,
    noMulticastScouting: Boolean?,
    mode: String?
): Config {
    return if (emptyArgs) {
        Config.loadDefault()
    } else {
        configFile?.let {
            Config.fromFile(path = Path(it))
        } ?: run {
            val connect = connectEndpoints?.let {Connect(it)}
            val listen = listenEndpoints?.let {Listen(it)}
            val scouting = noMulticastScouting?.let { Scouting(Multicast(!it)) }
            val configData = ConfigData(connect, listen, mode, scouting)
            val jsonConfig = Json.encodeToJsonElement(configData).toString()
            println(jsonConfig)
            Config.fromJson(jsonConfig)
        }
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--QueueHandler.java

```java
package io.zenoh;

import io.zenoh.handlers.Handler;

import java.util.ArrayDeque;

/**
 * Sample handler for the sake of the examples.
 *
 * A custom handler can be implemented to handle incoming samples, queries or replies for
 * subscribers, get operations, query operations or queryables.
 *
 * The example below shows a queue handler, in which an ArrayDeque is specified as the receiver type.
 * The function handle will be called everytime an element of type T is received and in our example
 * implementation, elements are simply enqueued into the queue, which can later be retrieved.
 */
class QueueHandler<T extends ZenohType> implements Handler<T, ArrayDeque<T>> {

    final ArrayDeque<T> queue = new ArrayDeque<>();

    @Override
    public void handle(T t) {
        queue.add(t);
    }

    @Override
    public ArrayDeque<T> receiver() {
        return queue;
    }

    @Override
    public void onClose() {}
}
```

---

# Example: examples--src--main--java--io--zenoh--ZBytesExamples.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.bytes.ZBytes;
import io.zenoh.ext.ZDeserializer;
import io.zenoh.ext.ZSerializer;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class ZBytesExamples {

    public static void main(String[] args) {

        /*
         * ZBytes
         *
         * A ZBytes instance can be created from a String and from a Byte Array with the `ZBytes.from(string: String)`
         * and `ZBytes.from(bytes: byte[])` functions.
         *
         * A ZBytes can be converted back into a [String] with the functions [ZBytes.toString] and [ZBytes.tryToString].
         * Similarly, with [ZBytes.toBytes] you can get the inner byte representation.
         */

        var exampleString = "example string";
        var zbytesA = ZBytes.from(exampleString);
        var outputA = zbytesA.toString();
        assert exampleString.equals(outputA);

        var exampleBytes = new byte[]{1, 2, 3, 4, 5};
        var zbytesB = ZBytes.from(exampleBytes);
        var outputB = zbytesB.toBytes();
        assert Arrays.equals(exampleBytes, outputB);

        /*
         * Serialization and deserialization.
         *
         * Additionally, the Zenoh API provides a series of serialization and deserialization utilities for processing
         * the received payloads.
         *
         * Serialization and deserialization supports the following types:
         * - Boolean
         * - Byte
         * - Byte Array
         * - Short
         * - Int
         * - Long
         * - Float
         * - Double
         * - String
         * - List
         * - Map
         *
         * For List and Map, the inner types can be a combination of the above types, including themselves.
         *
         * These serialization and deserialization utilities can be used across the Zenoh ecosystem with Zenoh
         * versions based on other supported languages such as Rust, Python, C and C++.
         * This works when the types are equivalent (a `Byte` corresponds to an `i8` in Rust, a `Short` to an `i16`, etc).
         */

        // Boolean example
        Boolean input1 = true;
        ZSerializer<Boolean> serializer1 = new ZSerializer<>() {};
        ZBytes zbytes1 = serializer1.serialize(input1);

        ZDeserializer<Boolean> deserializer1 = new ZDeserializer<>() {};
        Boolean output1 = deserializer1.deserialize(zbytes1);
        assert input1.equals(output1);

        // Byte example
        Byte input2 = 126;
        ZSerializer<Byte> serializer2 = new ZSerializer<>() {};
        ZBytes zbytes2 = serializer2.serialize(input2);

        ZDeserializer<Byte> deserializer2 = new ZDeserializer<>() {};
        Byte output2 = deserializer2.deserialize(zbytes2);
        assert input2.equals(output2);

        // Short example
        Short input3 = 256;
        ZSerializer<Short> serializer3 = new ZSerializer<>() {};
        ZBytes zbytes3 = serializer3.serialize(input3);

        ZDeserializer<Short> deserializer3 = new ZDeserializer<>() {};
        Short output3 = deserializer3.deserialize(zbytes3);
        assert input3.equals(output3);

        // Int example
        Integer input4 = 123456;
        ZSerializer<Integer> serializer4 = new ZSerializer<>() {};
        ZBytes zbytes4 = serializer4.serialize(input4);

        ZDeserializer<Integer> deserializer4 = new ZDeserializer<>() {};
        Integer output4 = deserializer4.deserialize(zbytes4);
        assert input4.equals(output4);

        // Long example
        Long input5 = 123456789L;
        ZSerializer<Long> serializer5 = new ZSerializer<>() {};
        ZBytes zbytes5 = serializer5.serialize(input5);

        ZDeserializer<Long> deserializer5 = new ZDeserializer<>() {};
        Long output5 = deserializer5.deserialize(zbytes5);
        assert input5.equals(output5);

        // Float example
        Float input6 = 123.45f;
        ZSerializer<Float> serializer6 = new ZSerializer<>() {};
        ZBytes zbytes6 = serializer6.serialize(input6);

        ZDeserializer<Float> deserializer6 = new ZDeserializer<>() {};
        Float output6 = deserializer6.deserialize(zbytes6);
        assert input6.equals(output6);

        // Double example
        Double input7 = 12345.6789;
        ZSerializer<Double> serializer7 = new ZSerializer<>() {};
        ZBytes zbytes7 = serializer7.serialize(input7);

        ZDeserializer<Double> deserializer7 = new ZDeserializer<>() {};
        Double output7 = deserializer7.deserialize(zbytes7);
        assert input7.equals(output7);

        // List example
        List<Integer> input12 = List.of(1, 2, 3, 4, 5);
        ZSerializer<List<Integer>> serializer12 = new ZSerializer<>() {};
        ZBytes zbytes12 = serializer12.serialize(input12);

        ZDeserializer<List<Integer>> deserializer12 = new ZDeserializer<>() {};
        List<Integer> output12 = deserializer12.deserialize(zbytes12);
        assert input12.equals(output12);

        // String example
        String input13 = "Hello, World!";
        ZSerializer<String> serializer13 = new ZSerializer<>() {};
        ZBytes zbytes13 = serializer13.serialize(input13);

        ZDeserializer<String> deserializer13 = new ZDeserializer<>() {};
        String output13 = deserializer13.deserialize(zbytes13);
        assert input13.equals(output13);

        // ByteArray example
        byte[] input14 = new byte[]{1, 2, 3, 4, 5};
        ZSerializer<byte[]> serializer14 = new ZSerializer<>() {};
        ZBytes zbytes14 = serializer14.serialize(input14);

        ZDeserializer<byte[]> deserializer14 = new ZDeserializer<>() {};
        byte[] output14 = deserializer14.deserialize(zbytes14);
        assert Arrays.equals(input14, output14);

        // Map example
        Map<String, Integer> input15 = Map.of("one", 1, "two", 2, "three", 3);
        ZSerializer<Map<String, Integer>> serializer15 = new ZSerializer<>() {};
        ZBytes zbytes15 = serializer15.serialize(input15);

        ZDeserializer<Map<String, Integer>> deserializer15 = new ZDeserializer<>() {};
        Map<String, Integer> output15 = deserializer15.deserialize(zbytes15);
        assert input15.equals(output15);

        // Nested List example
        List<List<Integer>> input18 = List.of(List.of(1, 2, 3));
        ZSerializer<List<List<Integer>>> serializer18 = new ZSerializer<>() {};
        ZBytes zbytes18 = serializer18.serialize(input18);

        ZDeserializer<List<List<Integer>>> deserializer18 = new ZDeserializer<>() {};
        List<List<Integer>> output18 = deserializer18.deserialize(zbytes18);
        assert input18.equals(output18);

        // Combined types example
        List<Map<String, Integer>> input19 = List.of(Map.of("a", 1, "b", 2));
        ZSerializer<List<Map<String, Integer>>> serializer19 = new ZSerializer<>() {};
        ZBytes zbytes19 = serializer19.serialize(input19);

        ZDeserializer<List<Map<String, Integer>>> deserializer19 = new ZDeserializer<>() {};
        List<Map<String, Integer>> output19 = deserializer19.deserialize(zbytes19);
        assert input19.equals(output19);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZDelete.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZDelete",
        mixinStandardHelpOptions = true,
        description = "Zenoh Delete example"
)
public class ZDelete implements Callable<Integer> {

    @Override
    public Integer call() throws ZError {
        Zenoh.initLogFromEnvOr("error");
        System.out.println("Opening session...");
        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);
        try (Session session = Zenoh.open(config)) {
            KeyExpr keyExpr = KeyExpr.tryFrom(key);
            System.out.println("Deleting resources matching '" + keyExpr + "'...");
            session.delete(keyExpr);
        }
        return 0;
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZDelete(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression to delete [default: demo/example/zenoh-java-delete].",
            defaultValue = "demo/example/zenoh-java-delete"
    )
    private String key;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZDelete(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZGet.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.bytes.ZBytes;
import io.zenoh.exceptions.ZError;
import io.zenoh.query.GetOptions;
import io.zenoh.query.QueryTarget;
import io.zenoh.query.Selector;
import io.zenoh.query.Reply;
import io.zenoh.sample.SampleKind;
import picocli.CommandLine;

import java.time.Duration;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZGet",
        mixinStandardHelpOptions = true,
        description = "Zenoh Get example"
)
public class ZGet implements Callable<Integer> {

    @Override
    public Integer call() throws ZError, InterruptedException {
        Zenoh.initLogFromEnvOr("error");
        System.out.println("Opening session...");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);
        Selector selector = Selector.tryFrom(this.selectorOpt);

        ZBytes payload = Optional.ofNullable(this.payload)
                .map(ZBytes::from)
                .orElse(null);
        ZBytes attachment = Optional.ofNullable(this.attachment)
                .map(ZBytes::from)
                .orElse(null);

        // Load GET options
        GetOptions options = new GetOptions();

        options.setPayload(payload);
        options.setTarget(QueryTarget.valueOf(this.target));
        options.setTimeout(Duration.ofMillis(this.timeout));
        options.setAttachment(attachment);


        // A GET query can be performed in different ways, by default (using a blocking queue), using a callback
        // or providing a handler. Uncomment one of the function calls below to try out different implementations:
        // Implementation with a blocking queue
        getExampleDefault(config, selector, options);
        // getExampleWithCallback(config, selector, options);
        // getExampleWithHandler(config, selector, options);

        return 0;
    }

    private void getExampleDefault(Config config, Selector selector, GetOptions options) throws ZError, InterruptedException {
        try (Session session = Zenoh.open(config)) {
            System.out.println("Performing Get on '" + selector + "'...");

            BlockingQueue<Optional<Reply>> receiver = session.get(selector, options);

            while (true) {
                Optional<Reply> wrapper = receiver.take();
                if (wrapper.isEmpty()) {
                    break;
                }
                Reply reply = wrapper.get();
                handleReply(reply);
            }
        }
    }

    /**
     * Example using a simple callback for handling the replies.
     * @see io.zenoh.handlers.Callback
     */
    private void getExampleWithCallback(Config config, Selector selector, GetOptions options) throws ZError {
        try (Session session = Zenoh.open(config)) {
            System.out.println("Performing Get on '" + selector + "'...");
            session.get(selector, this::handleReply, options);
        }
    }

    /**
     * Example using a custom implementation of a Handler.
     * @see QueueHandler
     * @see io.zenoh.handlers.Handler
     */
    private void getExampleWithHandler(Config config, Selector selector, GetOptions options) throws ZError {
        try (Session session = Zenoh.open(config)) {
            System.out.println("Performing Get on '" + selector + "'...");
            QueueHandler<Reply> queueHandler = new QueueHandler<>();
            session.get(selector, queueHandler, options);
        }
    }

    private void handleReply(Reply reply) {
        if (reply instanceof Reply.Success) {
            Reply.Success successReply = (Reply.Success) reply;
            if (successReply.getSample().getKind() == SampleKind.PUT) {
                System.out.println("Received ('" + successReply.getSample().getKeyExpr() + "': '" + successReply.getSample().getPayload() + "')");
            } else if (successReply.getSample().getKind() == SampleKind.DELETE) {
                System.out.println("Received (DELETE '" + successReply.getSample().getKeyExpr() + "')");
            }
        } else {
            Reply.Error errorReply = (Reply.Error) reply;
            System.out.println("Received (ERROR: '" + errorReply.getError() + "')");
        }
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZGet(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-s", "--selector"},
            description = "The selection of resources to query [default: demo/example/**].",
            defaultValue = "demo/example/**"
    )
    private String selectorOpt;

    @CommandLine.Option(
            names = {"-p", "--payload"},
            description = "An optional payload to put in the query."
    )
    private String payload;

    @CommandLine.Option(
            names = {"-t", "--target"},
            description = "The target queryables of the query. Default: BEST_MATCHING. " +
                    "[possible values: BEST_MATCHING, ALL, ALL_COMPLETE]",
            defaultValue = "BEST_MATCHING"
    )
    private String target;

    @CommandLine.Option(
            names = {"-o", "--timeout"},
            description = "The query timeout in milliseconds [default: 10000].",
            defaultValue = "10000"
    )
    private long timeout;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-a", "--attach"},
            description = "The attachment to add to the get. The key-value pairs are &-separated, and = serves as the separator between key and value."
    )
    private String attachment;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZGet(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZGetLiveliness.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.query.Reply;
import picocli.CommandLine;

import java.time.Duration;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZGetLiveliness",
        mixinStandardHelpOptions = true,
        description = "Zenoh Get Liveliness example"
)
public class ZGetLiveliness implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);
        KeyExpr keyExpr = KeyExpr.tryFrom(this.key);

        Session session = Zenoh.open(config);

        // Uncomment one of the lines below to try out different implementations:
        getLivelinessWithBlockingQueue(session, keyExpr);
        // getLivelinessWithCallback(session, keyExpr);
        // getLivelinessWithHandler(session, keyExpr);

        return 0;
    }

    /**
     * Default implementation using a blocking queue to handle replies.
     */
    private void getLivelinessWithBlockingQueue(Session session, KeyExpr keyExpr) throws ZError, InterruptedException {
        System.out.println("Sending Liveliness Query '" + keyExpr + "'.");
        BlockingQueue<Optional<Reply>> replyQueue = session.liveliness().get(keyExpr, Duration.ofMillis(timeout));

        while (true) {
            Optional<Reply> wrapper = replyQueue.take();
            if (wrapper.isEmpty()) {
                break;
            }
            handleReply(wrapper.get());
        }
    }

    /**
     * Example using a callback to handle liveliness replies asynchronously.
     * @see io.zenoh.handlers.Callback
     */
    private void getLivelinessWithCallback(Session session, KeyExpr keyExpr) throws ZError {
        System.out.println("Sending Liveliness Query '" + keyExpr + "'.");
        session.liveliness().get(keyExpr, this::handleReply, Duration.ofMillis(timeout));
    }

    /**
     * Example using a custom handler to process liveliness replies.
     * @see QueueHandler
     * @see io.zenoh.handlers.Handler
     */
    private void getLivelinessWithHandler(Session session, KeyExpr keyExpr) throws ZError {
        System.out.println("Sending Liveliness Query '" + keyExpr + "'.");
        QueueHandler<Reply> queueHandler = new QueueHandler<>();
        session.liveliness().get(keyExpr, queueHandler, Duration.ofMillis(timeout));
    }

    private void handleReply(Reply reply) {
        if (reply instanceof Reply.Success) {
            Reply.Success successReply = (Reply.Success) reply;
            System.out.println(">> Alive token ('" + successReply.getSample().getKeyExpr() + "')");
        } else if (reply instanceof Reply.Error) {
            Reply.Error errorReply = (Reply.Error) reply;
            System.out.println(">> Received (ERROR: '" + errorReply.getError() + "')");
        }
    }

    /**
     * ----- Example arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZGetLiveliness(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression matching liveliness tokens to query. [default: group1/**].",
            defaultValue = "group1/**"
    )
    private String key;

    @CommandLine.Option(
            names = {"-o", "--timeout"},
            description = "The query timeout in milliseconds [default: 10000].",
            defaultValue = "10000"
    )
    private long timeout;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZGetLiveliness(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZInfo.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.session.SessionInfo;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZInfo",
        mixinStandardHelpOptions = true,
        description = "Zenoh Info example"
)
public class ZInfo implements Callable<Integer> {


    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);

        System.out.println("Opening session...");
        try (Session session = Zenoh.open(config)) {
            SessionInfo info = session.info();
            System.out.println("zid: " + info.zid());
            System.out.println("routers zid: " + info.routersZid());
            System.out.println("peers zid: " + info.peersZid());
        }
        return 0;
    }

    /**
     * ----- Example CLI arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZInfo(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZInfo(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZLiveliness.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.keyexpr.KeyExpr;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZLiveliness",
        mixinStandardHelpOptions = true,
        description = "Zenoh Liveliness example"
)
public class ZLiveliness implements Callable<Integer> {


    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);

        System.out.println("Opening session...");
        try (Session session = Zenoh.open(config)) {
            KeyExpr keyExpr = KeyExpr.tryFrom(key);
            session.liveliness().declareToken(keyExpr);
            System.out.println("Liveliness token declared for key: " + key);

            while (true) {
                Thread.sleep(1000);
            }
        }
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZLiveliness(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression to declare liveliness tokens for [default: group1/zenoh-java].",
            defaultValue = "group1/zenoh-java"
    )
    private String key;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;


    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZLiveliness(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZPing.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.bytes.ZBytes;
import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.pubsub.Publisher;
import io.zenoh.pubsub.PublisherOptions;
import io.zenoh.qos.CongestionControl;
import io.zenoh.sample.Sample;
import picocli.CommandLine;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZPing",
        mixinStandardHelpOptions = true,
        description = "Zenoh Ping example"
)
public class ZPing implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(true, configFile, connect, listen, noMulticastScouting, mode);

        System.out.println("Opening session...");
        try (Session session = Zenoh.open(config)) {
            KeyExpr keyExprPing = KeyExpr.tryFrom("test/ping");
            KeyExpr keyExprPong = KeyExpr.tryFrom("test/pong");

            BlockingQueue<Optional<Sample>> receiverQueue =
                    session.declareSubscriber(keyExprPong).getReceiver();

            var publisherOptions = new PublisherOptions();
            publisherOptions.setCongestionControl(CongestionControl.BLOCK);
            publisherOptions.setExpress(!noExpress);
            Publisher publisher = session.declarePublisher(keyExprPing, publisherOptions);

            byte[] data = new byte[payloadSize];
            for (int i = 0; i < payloadSize; i++) {
                data[i] = (byte) (i % 10);
            }
            ZBytes payload = ZBytes.from(data);

            // Warm-up
            System.out.println("Warming up for " + warmup + " seconds...");
            long warmupEnd = System.currentTimeMillis() + (long) (warmup * 1000);
            while (System.currentTimeMillis() < warmupEnd) {
                publisher.put(payload);
                receiverQueue.take();
            }

            List<Long> samples = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                long startTime = System.nanoTime();
                publisher.put(payload);
                receiverQueue.take();
                long elapsedTime = (System.nanoTime() - startTime) / 1000; // Convert to microseconds
                samples.add(elapsedTime);
            }

            for (int i = 0; i < samples.size(); i++) {
                long rtt = samples.get(i);
                System.out.printf("%d bytes: seq=%d rtt=%dµs lat=%dµs%n", payloadSize, i, rtt, rtt / 2);
            }
        }
        return 0;
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    @CommandLine.Parameters(
            paramLabel = "payload_size",
            description = "Sets the size of the payload to publish [default: 8].",
            defaultValue = "8"
    )
    private int payloadSize;

    @CommandLine.Option(
            names = "--no-express",
            description = "Express for sending data.",
            defaultValue = "false"
    )
    private boolean noExpress;

    @CommandLine.Option(
            names = {"-w", "--warmup"},
            description = "The number of seconds to warm up [default: 1.0].",
            defaultValue = "1.0"
    )
    private double warmup;

    @CommandLine.Option(
            names = {"-n", "--samples"},
            description = "The number of round-trips to measure [default: 100].",
            defaultValue = "100"
    )
    private int n;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZPing()).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZPong.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.pubsub.Publisher;
import io.zenoh.pubsub.PublisherOptions;
import io.zenoh.qos.CongestionControl;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.CountDownLatch;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZPong",
        mixinStandardHelpOptions = true,
        description = "Zenoh ZPong example"
)
public class ZPong implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(true, configFile, connect, listen, noMulticastScouting, mode);

        System.out.println("Opening session...");
        try (Session session = Zenoh.open(config)) {
            KeyExpr keyExprPing = KeyExpr.tryFrom("test/ping");
            KeyExpr keyExprPong = KeyExpr.tryFrom("test/pong");

            var publisherOptions = new PublisherOptions();
            publisherOptions.setCongestionControl(CongestionControl.BLOCK);
            publisherOptions.setExpress(!noExpress);

            Publisher publisher = session.declarePublisher(keyExprPong, publisherOptions);

            session.declareSubscriber(keyExprPing, sample -> {
                try {
                    publisher.put(sample.getPayload());
                } catch (ZError e) {
                    System.err.println("Error responding to ping: " + e.getMessage());
                }
            });

            latch.await();
        }
        return 0;
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    @CommandLine.Option(
            names = "--no-express",
            description = "Express for sending data.",
            defaultValue = "false"
    )
    private boolean noExpress;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    private static final CountDownLatch latch = new CountDownLatch(1);

    public static void main(String[] args) {
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("Shutting down...");
            latch.countDown();
        }));

        int exitCode = new CommandLine(new ZPong()).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZPub.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.bytes.Encoding;
import io.zenoh.bytes.ZBytes;
import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.pubsub.Publisher;
import io.zenoh.pubsub.PublisherOptions;
import io.zenoh.pubsub.PutOptions;
import io.zenoh.qos.CongestionControl;
import io.zenoh.qos.Reliability;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZPub",
        mixinStandardHelpOptions = true,
        description = "Zenoh Pub example"
)
public class ZPub implements Callable<Integer> {

    @Override
    public Integer call() throws ZError, InterruptedException {
        Zenoh.initLogFromEnvOr("error");
        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);

        System.out.println("Opening session...");
        try (Session session = Zenoh.open(config)) {
            KeyExpr keyExpr = KeyExpr.tryFrom(key);
            System.out.println("Declaring publisher on '" + keyExpr + "'...");

            // A publisher config can optionally be provided.
            PublisherOptions publisherOptions = new PublisherOptions();
            publisherOptions.setEncoding(Encoding.ZENOH_STRING);
            publisherOptions.setCongestionControl(CongestionControl.BLOCK);
            publisherOptions.setReliability(Reliability.RELIABLE);

            // Declare the publisher
            Publisher publisher = session.declarePublisher(keyExpr, publisherOptions);

            System.out.println("Press CTRL-C to quit...");
            int idx = 0;
            while (true) {
                Thread.sleep(1000);
                String payload = String.format("[%4d] %s", idx, value);
                System.out.println("Putting Data ('" + keyExpr + "': '" + payload + "')...");
                if (attachment != null) {
                    PutOptions putOptions = new PutOptions();
                    putOptions.setAttachment(attachment);
                    publisher.put(payload, putOptions);
                } else {
                    publisher.put(payload);
                }
                idx++;
            }
        }
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZPub(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression to write to [default: demo/example/zenoh-java-pub].",
            defaultValue = "demo/example/zenoh-java-pub"
    )
    private String key;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"-v", "--value"},
            description = "The value to write. [default: 'Pub from Java!']",
            defaultValue = "Pub from Java!"
    )
    private String value;

    @CommandLine.Option(
            names = {"-a", "--attach"},
            description = "The attachments to add to each put. The key-value pairs are &-separated, and = serves as the separator between key and value."
    )
    private String attachment;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZPub(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZPubThr.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.bytes.ZBytes;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.pubsub.Publisher;
import io.zenoh.pubsub.PublisherOptions;
import io.zenoh.qos.CongestionControl;
import io.zenoh.qos.Priority;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZPubThr",
        mixinStandardHelpOptions = true,
        description = "Zenoh Throughput example"
)
public class ZPubThr implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        byte[] data = new byte[payloadSize];
        for (int i = 0; i < payloadSize; i++) {
            data[i] = (byte) (i % 10);
        }
        ZBytes payload = ZBytes.from(data);

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);

        try (Session session = Zenoh.open(config)) {
            KeyExpr keyExpr = KeyExpr.tryFrom("test/thr");
            var publisherOptions = new PublisherOptions();
            publisherOptions.setCongestionControl(CongestionControl.BLOCK);
            publisherOptions.setPriority(priorityInput != null ? Priority.getEntries().get(priorityInput) : Priority.DATA);
            try (Publisher publisher = session.declarePublisher(keyExpr, publisherOptions)) {
                System.out.println("Publisher declared on test/thr.");
                long count = 0;
                long start = System.currentTimeMillis();
                System.out.println("Press CTRL-C to quit...");

                while (true) {
                    publisher.put(payload);

                    if (statsPrint) {
                        if (count < number) {
                            count++;
                        } else {
                            long elapsedTime = System.currentTimeMillis() - start;
                            long throughput = (count * 1000) / elapsedTime;
                            System.out.println(throughput + " msgs/s");
                            count = 0;
                            start = System.currentTimeMillis();
                        }
                    }
                }
            }
        }
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZPubThr(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Parameters(
            index = "0",
            description = "Sets the size of the payload to publish [default: 8].",
            defaultValue = "8"
    )
    private int payloadSize;

    @CommandLine.Option(
            names = {"-p", "--priority"},
            description = "Priority for sending data."
    )
    private Integer priorityInput;

    @CommandLine.Option(
            names = {"-n", "--number"},
            description = "Number of messages in each throughput measurement [default: 100000].",
            defaultValue = "100000"
    )
    private long number;

    @CommandLine.Option(
            names = {"-t", "--print"},
            description = "Print the statistics.",
            defaultValue = "true"
    )
    private boolean statsPrint;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZPubThr(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZPut.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.pubsub.PutOptions;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZPut",
        mixinStandardHelpOptions = true,
        description = "Zenoh Put example"
)
public class ZPut implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);

        System.out.println("Opening session...");
        try (Session session = Zenoh.open(config)) {
            KeyExpr keyExpr = KeyExpr.tryFrom(key);
            System.out.println("Putting Data ('" + keyExpr + "': '" + value + "')...");
            if (attachment != null) {
                var putOptions = new PutOptions();
                putOptions.setAttachment(attachment);
                session.put(keyExpr, value, putOptions);
            } else {
                session.put(keyExpr, value);
            }
        }
        return 0;
    }


    /**
     * ----- Example CLI arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZPut(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression to write to [default: demo/example/zenoh-java-put].",
            defaultValue = "demo/example/zenoh-java-put"
    )
    private String key;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"-v", "--value"},
            description = "The value to write. [default: 'Put from Java!'].",
            defaultValue = "Put from Java!"
    )
    private String value;

    @CommandLine.Option(
            names = {"-a", "--attach"},
            description = "The attachment to add to the put. The key-value pairs are &-separated, and = serves as the separator between key and value."
    )
    private String attachment;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZPut(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZQuerier.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.query.*;
import picocli.CommandLine;

import java.time.Duration;
import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZQuerier",
        mixinStandardHelpOptions = true,
        description = "Zenoh Querier example"
)
public class ZQuerier implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);
        Selector selector = Selector.tryFrom(this.selectorOpt);

        QueryTarget queryTarget = target != null ? QueryTarget.valueOf(target.toUpperCase()) : QueryTarget.BEST_MATCHING;
        Duration queryTimeout = Duration.ofMillis(timeout);

        System.out.println("Opening session...");
        Session session = Zenoh.open(config);
        QuerierOptions options = new QuerierOptions();
        options.setTarget(queryTarget);
        options.setTimeout(queryTimeout);

        System.out.println("Declaring querier on '" + selector + "'...");
        Querier querier = session.declareQuerier(selector.getKeyExpr(), options);

        performQueries(querier, selector);
        return 0;
    }

    /**
     * Performs queries in an infinite loop, printing responses.
     */
    private void performQueries(Querier querier, Selector selector) throws ZError, InterruptedException {
        for (int idx = 0; idx < Integer.MAX_VALUE; idx++) {
            Thread.sleep(1000);

            String queryPayload = String.format("[%04d] %s", idx, payload != null ? payload : "");
            System.out.println("Querying '" + selector + "' with payload: '" + queryPayload + "'...");

            Querier.GetOptions options = new Querier.GetOptions();
            options.setPayload(queryPayload);
            options.setParameters(selector.getParameters());

            querier.get(this::handleReply, options);
        }
    }

    /**
     * Handles replies received from the query.
     */
    private void handleReply(Reply reply) {
        if (reply instanceof Reply.Success) {
            Reply.Success successReply = (Reply.Success) reply;
            System.out.println(">> Received ('" + successReply.getSample().getKeyExpr() +
                    "': '" + successReply.getSample().getPayload() + "')");
        } else if (reply instanceof Reply.Error) {
            Reply.Error errorReply = (Reply.Error) reply;
            System.out.println(">> Received (ERROR: '" + errorReply.getError() + "')");
        }
    }

    /**
     * ----- Example arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZQuerier(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-s", "--selector"},
            description = "The selection of resources to query [default: demo/example/**].",
            defaultValue = "demo/example/**"
    )
    private String selectorOpt;

    @CommandLine.Option(
            names = {"-p", "--payload"},
            description = "An optional payload to put in the query."
    )
    private String payload;

    @CommandLine.Option(
            names = {"-t", "--target"},
            description = "The target queryables of the query. Default: BEST_MATCHING. " +
                    "[possible values: BEST_MATCHING, ALL, ALL_COMPLETE]"
    )
    private String target;

    @CommandLine.Option(
            names = {"-o", "--timeout"},
            description = "The query timeout in milliseconds [default: 10000].",
            defaultValue = "10000"
    )
    private long timeout;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZQuerier(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZQueryable.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.query.Query;
import io.zenoh.query.QueryableOptions;
import io.zenoh.query.ReplyOptions;
import org.apache.commons.net.ntp.TimeStamp;
import picocli.CommandLine;

import java.util.List;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZQueryable",
        mixinStandardHelpOptions = true,
        description = "Zenoh Queryable example"
)
public class ZQueryable implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);
        KeyExpr keyExpr = KeyExpr.tryFrom(this.key);

        System.out.println("Opening session...");
        Session session = Zenoh.open(config);

        // A Queryable can be implemented in multiple ways. Uncomment one to try:
        declareQueryableWithBlockingQueue(session, keyExpr);
        // declareQueryableWithCallback(session, keyExpr);
        // declareQueryableProvidingConfig(session, keyExpr);

        return 0;
    }

    /**
     * Default implementation using a blocking queue to handle incoming queries.
     */
    private void declareQueryableWithBlockingQueue(Session session, KeyExpr keyExpr) throws ZError, InterruptedException {
        System.out.println("Declaring Queryable on '" + keyExpr + "'...");
        var queryable = session.declareQueryable(keyExpr);
        BlockingQueue<Optional<Query>> receiver = queryable.getReceiver();
        while (true) {
            Optional<Query> wrapper = receiver.take();
            if (wrapper.isEmpty()) {
                break;
            }
            Query query = wrapper.get();
            handleQuery(query);
        }
    }

    /**
     * Example using a callback to handle incoming queries asynchronously.
     *
     * @see io.zenoh.handlers.Callback
     */
    private void declareQueryableWithCallback(Session session, KeyExpr keyExpr) throws ZError {
        System.out.println("Declaring Queryable on '" + keyExpr + "'...");
        session.declareQueryable(keyExpr, this::handleQuery);
    }

    /**
     * Example demonstrating the use of QueryableConfig to declare a Queryable.
     *
     * @see QueryableOptions
     */
    private void declareQueryableProvidingConfig(Session session, KeyExpr keyExpr) throws ZError {
        System.out.println("Declaring Queryable on '" + keyExpr + "'...");
        QueryableOptions queryableOptions = new QueryableOptions();
        queryableOptions.setComplete(true);
        session.declareQueryable(keyExpr, this::handleQuery, queryableOptions);
    }

    private void handleQuery(Query query) {
        try {
            String valueInfo = query.getPayload() != null ? " with value '" + query.getPayload() + "'" : "";
            System.out.println(">> [Queryable] Received Query '" + query.getSelector() + "'" + valueInfo);
            var options = new ReplyOptions();
            options.setTimeStamp(TimeStamp.getCurrentTime());
            query.reply(query.getKeyExpr(), value, options);
        } catch (Exception e) {
            System.err.println(">> [Queryable] Error sending reply: " + e.getMessage());
        }
    }

    /**
     * ----- Example arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZQueryable(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression to write to [default: demo/example/zenoh-java-queryable].",
            defaultValue = "demo/example/zenoh-java-queryable"
    )
    private String key;

    @CommandLine.Option(
            names = {"-v", "--value"},
            description = "The value to reply to queries [default: 'Queryable from Java!'].",
            defaultValue = "Queryable from Java!"
    )
    private String value;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZQueryable(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZScout.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.config.WhatAmI;
import io.zenoh.scouting.Hello;
import io.zenoh.scouting.ScoutOptions;
import picocli.CommandLine;

import java.util.Optional;
import java.util.Set;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;

@CommandLine.Command(
        name = "ZScout",
        mixinStandardHelpOptions = true,
        description = "Zenoh Scouting example"
)
public class ZScout implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        System.out.println("Scouting...");

        var scoutOptions = new ScoutOptions();
        scoutOptions.setWhatAmI(Set.of(WhatAmI.Peer, WhatAmI.Router));
        var scout = Zenoh.scout(scoutOptions);
        BlockingQueue<Optional<Hello>> receiver = scout.getReceiver();
        assert receiver != null;

        try {
            while (true) {
                Optional<Hello> wrapper = receiver.take();
                if (wrapper.isEmpty()) {
                    break;
                }

                Hello hello = wrapper.get();
                System.out.println(hello);
            }
        } finally {
            scout.stop();
        }

        return 0;
    }

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZScout()).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZSub.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.handlers.Handler;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.pubsub.HandlerSubscriber;
import io.zenoh.sample.Sample;
import picocli.CommandLine;

import java.util.List;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZSub",
        mixinStandardHelpOptions = true,
        description = "Zenoh Sub example"
)
public class ZSub implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);
        KeyExpr keyExpr = KeyExpr.tryFrom(this.key);

        System.out.println("Opening session...");
        Session session = Zenoh.open(config);

        // Subscribers can be declared in different ways.
        // Uncomment one of the lines below to try out different implementations:
        subscribeWithBlockingQueue(session, keyExpr);
        // subscribeWithCallback(session, keyExpr);
        // subscribeWithHandler(session, keyExpr);

        return 0;
    }

    /**
     * Default implementation using a blocking queue to handle incoming samples.
     */
    private void subscribeWithBlockingQueue(Session session, KeyExpr keyExpr) throws ZError, InterruptedException {
        System.out.println("Declaring Subscriber on '" + keyExpr + "'...");
        try (HandlerSubscriber<BlockingQueue<Optional<Sample>>> subscriber = session.declareSubscriber(keyExpr)) {
            BlockingQueue<Optional<Sample>> receiver = subscriber.getReceiver();
            assert receiver != null;
            while (true) {
                Optional<Sample> wrapper = receiver.take();
                if (wrapper.isEmpty()) {
                    break;
                }
                handleSample(wrapper.get());
            }
        }
    }

    /**
     * Example using a callback to handle incoming samples asynchronously.
     * @see io.zenoh.handlers.Callback
     */
    private void subscribeWithCallback(Session session, KeyExpr keyExpr) throws ZError {
        System.out.println("Declaring Subscriber on '" + keyExpr + "'...");
        session.declareSubscriber(keyExpr, this::handleSample);
    }

    /**
     * Example using a custom implementation of the Handler.
     * @see QueueHandler
     * @see Handler
     */
    private void subscribeWithHandler(Session session, KeyExpr keyExpr) throws ZError {
        System.out.println("Declaring Subscriber on '" + keyExpr + "'...");
        QueueHandler<Sample> queueHandler = new QueueHandler<>();
        var subscriber = session.declareSubscriber(keyExpr, queueHandler);
        for (Sample sample : subscriber.getReceiver()) {
            System.out.println(sample);
        }
    }

    /**
     * Handles a single Sample and prints relevant information.
     */
    private void handleSample(Sample sample) {
        String attachment = sample.getAttachment() != null ? ", with attachment: " + sample.getAttachment() : "";
        System.out.println(">> [Subscriber] Received " + sample.getKind() +
                " ('" + sample.getKeyExpr() + "': '" + sample.getPayload() + "'" + attachment + ")");
    }

    /**
     * ----- Example arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZSub(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression to subscribe to [default: demo/example/**].",
            defaultValue = "demo/example/**"
    )
    private String key;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZSub(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZSubLiveliness.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.liveliness.LivelinessSubscriberOptions;
import io.zenoh.sample.Sample;
import io.zenoh.sample.SampleKind;
import picocli.CommandLine;

import java.util.List;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZSubLiveliness",
        mixinStandardHelpOptions = true,
        description = "Zenoh Sub Liveliness example"
)
public class ZSubLiveliness implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);
        KeyExpr keyExpr = KeyExpr.tryFrom(this.key);

        System.out.println("Opening session...");
        Session session = Zenoh.open(config);

        // Subscribing to liveliness tokens can be implemented in multiple ways.
        // Uncomment the desired implementation:
        subscribeToLivelinessWithBlockingQueue(session, keyExpr);
        // subscribeToLivelinessWithCallback(session, keyExpr);
        // subscribeToLivelinessWithHandler(session, keyExpr);

        return 0;
    }

    /**
     * Default implementation using a blocking queue to handle incoming liveliness tokens.
     */
    private void subscribeToLivelinessWithBlockingQueue(Session session, KeyExpr keyExpr) throws ZError, InterruptedException {
        var options = new LivelinessSubscriberOptions(history);
        var subscriber = session.liveliness().declareSubscriber(keyExpr, options);

        BlockingQueue<Optional<Sample>> receiver = subscriber.getReceiver();
        System.out.println("Listening for liveliness tokens...");
        while (true) {
            Optional<Sample> wrapper = receiver.take();
            if (wrapper.isEmpty()) {
                break;
            }
            handleLivelinessSample(wrapper.get());
        }
    }

    /**
     * Example using a callback to handle incoming liveliness tokens asynchronously.
     *
     * @see io.zenoh.handlers.Callback
     */
    private void subscribeToLivelinessWithCallback(Session session, KeyExpr keyExpr) throws ZError {
        var options = new LivelinessSubscriberOptions(history);
        session.liveliness().declareSubscriber(
                keyExpr,
                this::handleLivelinessSample,
                options
        );
    }

    /**
     * Example using a handler to handle incoming liveliness tokens asynchronously.
     *
     * @see io.zenoh.handlers.Handler
     * @see QueueHandler
     */
    private void subscribeToLivelinessWithHandler(Session session, KeyExpr keyExpr) throws ZError {
        QueueHandler<Sample> queueHandler = new QueueHandler<>();
        var options = new LivelinessSubscriberOptions(history);
        session.liveliness().declareSubscriber(
                keyExpr,
                queueHandler,
                options
        );
    }

    /**
     * Handles a single liveliness token sample.
     */
    private void handleLivelinessSample(Sample sample) {
        if (sample.getKind() == SampleKind.PUT) {
            System.out.println(">> [LivelinessSubscriber] New alive token ('" + sample.getKeyExpr() + "')");
        } else if (sample.getKind() == SampleKind.DELETE) {
            System.out.println(">> [LivelinessSubscriber] Dropped token ('" + sample.getKeyExpr() + "')");
        }
    }

    /**
     * ----- Example arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZSubLiveliness(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-k", "--key"},
            description = "The key expression to subscribe to [default: group1/**].",
            defaultValue = "group1/**"
    )
    private String key;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--history"},
            description = "Get historical liveliness tokens.",
            defaultValue = "false"
    )
    private boolean history;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZSubLiveliness(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

# Example: examples--src--main--java--io--zenoh--ZSubThr.java

```java
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

package io.zenoh;

import io.zenoh.exceptions.ZError;
import io.zenoh.keyexpr.KeyExpr;
import io.zenoh.pubsub.Subscriber;
import picocli.CommandLine;

import java.util.List;
import java.util.concurrent.Callable;

import static io.zenoh.ConfigKt.loadConfig;

@CommandLine.Command(
        name = "ZSubThr",
        mixinStandardHelpOptions = true,
        description = "Zenoh Subscriber Throughput test"
)
public class ZSubThr implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        Zenoh.initLogFromEnvOr("error");

        Config config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode);

        System.out.println("Opening Session");
        try (Session session = Zenoh.open(config)) {
            try (KeyExpr keyExpr = KeyExpr.tryFrom("test/thr")) {
                subscriber = session.declareSubscriber(keyExpr, sample -> listener(number));
                System.out.println("Press CTRL-C to quit...");

                while (subscriber.isValid()) {
                    Thread.sleep(1000);
                }
            }
        }
        return 0;
    }

    private void listener(long number) {
        if (batchCount > samples) {
            closeSubscriber();
            report();
            return;
        }

        if (count == 0) {
            startTimestampNs = System.nanoTime();
            if (globalStartTimestampNs == 0) {
                globalStartTimestampNs = startTimestampNs;
            }
            count++;
            return;
        }

        if (count < number) {
            count++;
            return;
        }

        long stop = System.nanoTime();
        double elapsedTimeSecs = (double) (stop - startTimestampNs) / NANOS_TO_SEC;
        double messagesPerSec = number / elapsedTimeSecs;
        System.out.printf("%.2f msgs/sec%n", messagesPerSec);
        batchCount++;
        count = 0;
    }

    private void report() {
        long end = System.nanoTime();
        long totalMessages = batchCount * number + count;
        double elapsedTimeSecs = (double) (end - globalStartTimestampNs) / NANOS_TO_SEC;
        double averageMessagesPerSec = totalMessages / elapsedTimeSecs;

        System.out.printf("Received %d messages in %.2f seconds: averaged %.2f msgs/sec%n",
                totalMessages, elapsedTimeSecs, averageMessagesPerSec);
    }

    private void closeSubscriber() {
        if (subscriber != null && subscriber.isValid()) {
            try {
                subscriber.close();
            } catch (Exception e) {
                System.err.println("Error closing subscriber: " + e.getMessage());
            }
        }
    }

    
    /**
     * ----- Example arguments and private fields -----
     */

    private final Boolean emptyArgs;

    ZSubThr(Boolean emptyArgs) {
        this.emptyArgs = emptyArgs;
    }

    private static final long NANOS_TO_SEC = 1_000_000_000L;
    private long batchCount = 0;
    private long count = 0;
    private long startTimestampNs = 0;
    private long globalStartTimestampNs = 0;

    @CommandLine.Option(
            names = {"-s", "--samples"},
            description = "Number of throughput measurements [default: 10].",
            defaultValue = "10"
    )
    private long samples;

    @CommandLine.Option(
            names = {"-n", "--number"},
            description = "Number of messages in each throughput measurement [default: 100000].",
            defaultValue = "100000"
    )
    private long number;

    @CommandLine.Option(
            names = {"-c", "--config"},
            description = "A configuration file."
    )
    private String configFile;

    @CommandLine.Option(
            names = {"-e", "--connect"},
            description = "Endpoints to connect to.",
            split = ","
    )
    private List<String> connect;

    @CommandLine.Option(
            names = {"-l", "--listen"},
            description = "Endpoints to listen on.",
            split = ","
    )
    private List<String> listen;

    @CommandLine.Option(
            names = {"-m", "--mode"},
            description = "The session mode. Default: peer. Possible values: [peer, client, router].",
            defaultValue = "peer"
    )
    private String mode;

    @CommandLine.Option(
            names = {"--no-multicast-scouting"},
            description = "Disable the multicast-based scouting mechanism.",
            defaultValue = "false"
    )
    private boolean noMulticastScouting;

    private Subscriber subscriber;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new ZSubThr(args.length == 0)).execute(args);
        System.exit(exitCode);
    }
}
```

---

