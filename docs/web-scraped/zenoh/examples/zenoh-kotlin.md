# Zenoh Examples: zenoh-kotlin

# Zenoh Kotlin examples

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
Usage: zpub [<options>]

  Zenoh Pub example

Options:
  -k, --key=<key>          The key expression to write to [default: demo/example/zenoh-kotlin-pub]
  -c, --config=<config>    A configuration file.
  -e, --connect=<connect>  Endpoints to connect to.
  -l, --listen=<listen>    Endpoints to listen on.
  -m, --mode=<mode>        The session mode. Default: peer. Possible values: [peer, client, router]
  -v, --value=<value>      The value to write. [Default: "Pub from Kotlin!"]
  -a, --attach=<attach>    The attachments to add to each put. The key-value pairs are &-separated, and = serves as the separator between key and value.
  --no-multicast-scouting  Disable the multicast-based scouting mechanism.
  -h, --help               Show this message and exit
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
java -jar ZPut.jar -k demo/example/put -v 'Put from Kotlin!'
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

The ZLiveliness example, it just announces itself to the Zenoh network by default to the key expression `group1/zenoh-kotlin`.

Usage:

```bash
java -jar ZLiveliness
```

It can be used along with the following liveliness examples:

#### ZGetLiveliness

Gets the liveliness tokens, by default to `group1/zenoh-kotlin`.

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

# Example: examples--src--main--kotlin--io.zenoh--Config.kt

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
    connectEndpoints: List<String>,
    listenEndpoints: List<String>,
    noMulticastScouting: Boolean,
    mode: String?
): Config {
    return if (emptyArgs) {
        Config.default()
    } else {
        configFile?.let {
            Config.fromFile(path = Path(it)).getOrThrow()
        } ?: run {
            val connect = Connect(connectEndpoints)
            val listen = Listen(listenEndpoints)
            val scouting = Scouting(Multicast(!noMulticastScouting))
            val configData = ConfigData(connect, listen, mode, scouting)
            val jsonConfig = Json.encodeToJsonElement(configData)
            Config.fromJsonElement(jsonConfig).getOrThrow()
        }
    }
}
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZAdvancedPublisher.kt

```kt
//
// Copyright (c) 2025 ZettaScale Technology
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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.bytes.ZBytes
import io.zenoh.ext.CacheConfig
import io.zenoh.ext.HeartbeatMode
import io.zenoh.ext.MissDetectionConfig
import io.zenoh.keyexpr.intoKeyExpr

class ZAdvancedPublisher(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Advanced Publisher example"
) {
    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()

        val maxSamples = history.toLong()
        val cacheConfig = CacheConfig(maxSamples)

        val sampleMissDetection = MissDetectionConfig(HeartbeatMode.PeriodicHeartbeat(500))

        println("Declaring AdvancedPublisher on '$keyExpr'...")
        val publisher = session.declareAdvancedPublisher(
            keyExpr,
            cacheConfig = cacheConfig,
            sampleMissDetection = sampleMissDetection,
            publisherDetection = true
        ).getOrThrow()

        println("Press CTRL-C to quit...")
        val attachment = attachment?.toByteArray()

        var idx = 0
        while (true) {
            Thread.sleep(1000)
            val payload = "[${
                idx.toString().padStart(4, ' ')
            }] $value"
            println(
                "Putting Data ('$keyExpr': '$payload')..."
            )
            attachment?.let {
                publisher.put(ZBytes.from(payload), attachment = ZBytes.from(it))
            } ?: let { publisher.put(ZBytes.from(payload)) }
            idx++
        }
    }


    private val key by option(
        "-k", "--key", help = "The key expression to write to [default: demo/example/zenoh-kotlin-pub]", metavar = "key"
    ).default("demo/example/zenoh-kotlin-pub")
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val value by option(
        "-v", "--value", help = "The value to write. [Default: \"Pub from Kotlin!\"]", metavar = "value"
    ).default("Pub from Kotlin!")
    private val history by option(
        "-i", help = "The number of publications to keep in cache. [Default: 1]", metavar = "history"
    ).default("1")
    private val attachment by option(
        "-a",
        "--attach",
        help = "The attachments to add to each put. The key-value pairs are &-separated, and = serves as the separator between key and value.",
        metavar = "attach"
    )
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZAdvancedPublisher(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZAdvancedSubscriber.kt

```kt
//
// Copyright (c) 2025 ZettaScale Technology
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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.ext.HistoryConfig
import io.zenoh.ext.RecoveryConfig
import io.zenoh.ext.RecoveryMode
import io.zenoh.handlers.Handler
import io.zenoh.keyexpr.KeyExpr
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.sample.Sample
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking
import java.util.concurrent.CountDownLatch

class ZAdvancedSubscriber(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Advanced Subscriber example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()

        println("Declaring Advanced Subscriber on '$keyExpr'...")

        runChannelExample(session, keyExpr)
    }

    private fun runChannelExample(session: Session, keyExpr: KeyExpr) {
        val historyConfig = HistoryConfig(true)
        val recoveryConfig = RecoveryConfig(RecoveryMode.Heartbeat)

        val subscriber = session.declareAdvancedSubscriber(
            keyExpr, historyConfig, recoveryConfig, true, Channel()).getOrThrow()

        runBlocking {
            for (sample in subscriber.receiver) {
                println(">> [Advanced Subscriber] Received ${sample.kind} ('${sample.keyExpr}': '${sample.payload}'" + "${
                    sample.attachment?.let {
                        ", with attachment: $it"
                    } ?: ""
                })")
            }
        }

        subscriber.close()
    }

    private fun runCallbackExample(session: Session, keyExpr: KeyExpr) {
        val historyConfig = HistoryConfig(true)
        val recoveryConfig = RecoveryConfig(RecoveryMode.Heartbeat)

        val subscriber = session.declareAdvancedSubscriber(
            keyExpr, historyConfig, recoveryConfig, true, callback = { sample ->
                println(">> [Advanced Subscriber] Received ${sample.kind} ('${sample.keyExpr}': '${sample.payload}'" + "${
                    sample.attachment?.let {
                        ", with attachment: $it"
                    } ?: ""
                })")
        }).getOrThrow()


        CountDownLatch(1).await() // A countdown latch is used here to block execution while samples are received.
                                         // Typically, this wouldn't be needed.
        subscriber.close()
    }

    private fun runHandlerExample(session: Session, keyExpr: KeyExpr) {
        class ExampleHandler: Handler<Sample, Unit> {
            override fun handle(t: Sample) {
                println(">> [Advanced Subscriber] Received ${t.kind} ('${t.keyExpr}': '${t.payload}'" + "${
                    t.attachment?.let {
                        ", with attachment: $it"
                    } ?: ""
                })")
            }

            override fun receiver() {}
            override fun onClose() {}
        }

        val historyConfig = HistoryConfig(true)
        val recoveryConfig = RecoveryConfig(RecoveryMode.Heartbeat)

        val subscriber = session.declareAdvancedSubscriber(
            keyExpr, historyConfig, recoveryConfig, true, handler = ExampleHandler()).getOrThrow()

        CountDownLatch(1).await() // A countdown latch is used here to block execution while samples are received.
                                         // Typically, this wouldn't be needed.
        subscriber.close()
    }

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val key by option(
        "-k", "--key", help = "The key expression to subscribe to [default: demo/example/**]", metavar = "key"
    ).default("demo/example/**")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZAdvancedSubscriber(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZBytes.kt

```kt
package io.zenoh

import io.zenoh.ext.zDeserialize
import io.zenoh.ext.zSerialize
import io.zenoh.bytes.ZBytes

fun main() {

    /**
     * # ZBytes
     *
     * A ZBytes instance can be created from a [String] and from a [ByteArray] with the `ZBytes.from(string: String)`
     * and `ZBytes.from(bytes: ByteArray)` functions.
     *
     * A ZBytes can be converted back into a [String] with the functions [ZBytes.toString] and [ZBytes.tryToString].
     * Similarly, with [ZBytes.toBytes] you can get the inner byte representation.
     */

    // String examples
    val inputA = "Example"
    val zbytesA = ZBytes.from(inputA)

    val outputA = zbytesA.toString()
    check(inputA == outputA)

    zbytesA.tryToString().onSuccess {
        check(inputA == it)
    }.onFailure { error ->
        throw error
    }

    // Bytes example
    val inputC = "Example2".toByteArray()
    val zbytesC = ZBytes.from(inputC)
    val outputC = zbytesC.toBytes()
    check(inputC.contentEquals(outputC))

    /**
     * # Serialization and deserialization.
     *
     * Additionally, the Zenoh API provides a series of serialization and deserialization utilities for processing
     * the received payloads.
     *
     * Serialization and deserialization supports the following types:
     * - [Boolean]
     * - [Byte]
     * - [Short]
     * - [Int]
     * - [Long]
     * - [Float]
     * - [Double]
     * - [UByte]
     * - [UShort]
     * - [UInt]
     * - [ULong]
     * - [List]
     * - [String]
     * - [ByteArray]
     * - [Map]
     * - [Pair]
     * - [Triple]
     *
     * For `List`, `Pair` and `Triple`, the inner types can be a combination of the above types, including themselves.
     *
     * These serialization and deserialization utilities can be used across the Zenoh ecosystem with Zenoh
     * versions based on other supported languages such as Rust, Python, C and C++.
     * This works when the types are equivalent (a `Byte` corresponds to an `i8` in Rust, a `Short` to an `i16`, etc).
     *
     */

    /** Boolean example */
    val input1: Boolean = true
    val zbytes1 = zSerialize(input1).getOrThrow()
    val output1 = zDeserialize<Boolean>(zbytes1).getOrThrow()
    check(input1 == output1)

    /** Byte example */
    val input2: Byte = 126.toByte()
    val zbytes2 = zSerialize(input2).getOrThrow()
    val output2 = zDeserialize<Byte>(zbytes2).getOrThrow()
    check(input2 == output2)

    /** Short example */
    val input3: Short = 256.toShort()
    val zbytes3 = zSerialize(input3).getOrThrow()
    val output3 = zDeserialize<Short>(zbytes3).getOrThrow()
    check(input3 == output3)

    /** Int example */
    val input4: Int = 123456
    val zbytes4 = zSerialize(input4).getOrThrow()
    val output4 = zDeserialize<Int>(zbytes4).getOrThrow()
    check(input4 == output4)

    /** Long example */
    val input5: Long = 123456789L
    val zbytes5 = zSerialize(input5).getOrThrow()
    val output5 = zDeserialize<Long>(zbytes5).getOrThrow()
    check(input5 == output5)

    /** Float example */
    val input6: Float = 123.45f
    val zbytes6 = zSerialize(input6).getOrThrow()
    val output6 = zDeserialize<Float>(zbytes6).getOrThrow()
    check(input6 == output6)

    /** Double example */
    val input7: Double = 12345.6789
    val zbytes7 = zSerialize(input7).getOrThrow()
    val output7 = zDeserialize<Double>(zbytes7).getOrThrow()
    check(input7 == output7)

    /** UByte example */
    val input8: UByte = 255.toUByte()
    val zbytes8 = zSerialize(input8).getOrThrow()
    val output8 = zDeserialize<UByte>(zbytes8).getOrThrow()
    check(input8 == output8)

    /** UShort example */
    val input9: UShort = 65535.toUShort()
    val zbytes9 = zSerialize(input9).getOrThrow()
    val output9 = zDeserialize<UShort>(zbytes9).getOrThrow()
    check(input9 == output9)

    /** UInt example */
    val input10: UInt = 123456789u
    val zbytes10 = zSerialize(input10).getOrThrow()
    val output10 = zDeserialize<UInt>(zbytes10).getOrThrow()
    check(input10 == output10)

    /** ULong example */
    val input11: ULong = 1234567890123456789uL
    val zbytes11 = zSerialize(input11).getOrThrow()
    val output11 = zDeserialize<ULong>(zbytes11).getOrThrow()
    check(input11 == output11)

    /** List example */
    val input12: List<Int> = listOf(1, 2, 3, 4, 5)
    val zbytes12 = zSerialize(input12).getOrThrow()
    val output12 = zDeserialize<List<Int>>(zbytes12).getOrThrow()
    check(input12 == output12)

    /** String example */
    val input13: String = "Hello, World!"
    val zbytes13 = zSerialize(input13).getOrThrow()
    val output13 = zDeserialize<String>(zbytes13).getOrThrow()
    check(input13 == output13)

    /** ByteArray example */
    val input14: ByteArray = byteArrayOf(1, 2, 3, 4, 5)
    val zbytes14 = zSerialize(input14).getOrThrow()
    val output14 = zDeserialize<ByteArray>(zbytes14).getOrThrow()
    check(input14.contentEquals(output14))

    /** Map example */
    val input15: Map<String, Int> = mapOf("one" to 1, "two" to 2, "three" to 3)
    val zbytes15 = zSerialize(input15).getOrThrow()
    val output15 = zDeserialize<Map<String, Int>>(zbytes15).getOrThrow()
    check(input15 == output15)

    /** Pair example */
    val input16: Pair<String, Int> = Pair("one", 1)
    val zbytes16 = zSerialize(input16).getOrThrow()
    val output16 = zDeserialize<Pair<String, Int>>(zbytes16).getOrThrow()
    check(input16 == output16)

    /** Triple example */
    val input17: Triple<String, Int, Boolean> = Triple("one", 1, true)
    val zbytes17 = zSerialize(input17).getOrThrow()
    val output17 = zDeserialize<Triple<String, Int, Boolean>>(zbytes17).getOrThrow()
    check(input17 == output17)

    /** Nested List example */
    val input18: List<List<Int>> = listOf(listOf(1, 2, 3))
    val zbytes18 = zSerialize(input18).getOrThrow()
    val output18 = zDeserialize<List<List<Int>>>(zbytes18).getOrThrow()
    check(input18 == output18)

    /** Combined types example */
    val input19: List<Map<String, Int>> = listOf(mapOf("a" to 1, "b" to 2))
    val zbytes19 = zSerialize(input19).getOrThrow()
    val output19 = zDeserialize<List<Map<String, Int>>>(zbytes19).getOrThrow()
    check(input19 == output19)

}
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZDelete.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.keyexpr.intoKeyExpr

class ZDelete(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Delete example"
) {
    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        session.use {
            key.intoKeyExpr().onSuccess { keyExpr ->
                println("Deleting resources matching '$keyExpr'...")
                session.delete(keyExpr)
            }
        }
    }

    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val key by option(
        "-k", "--key", help = "The key expression to write to [default: demo/example/zenoh-kotlin-put]", metavar = "key"
    ).default("demo/example/zenoh-kotlin-put")
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZDelete(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZGet.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import com.github.ajalt.clikt.parameters.types.long
import io.zenoh.bytes.ZBytes
import io.zenoh.handlers.Handler
import io.zenoh.sample.SampleKind
import io.zenoh.query.QueryTarget
import io.zenoh.query.Reply
import io.zenoh.query.Selector
import io.zenoh.query.intoSelector
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking
import java.time.Duration

class ZGet(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Get example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        val session = Zenoh.open(config).getOrThrow()
        val selector = selector.intoSelector().getOrThrow()

        // Run the Get query through one of the examples below:
        runChannelExample(session, selector)
        // runCallbackExample(session, selector)
        // runHandlerExample(session, selector)

        session.close()
    }

    private fun runChannelExample(session: Session, selector: Selector) {
        val channelReceiver = session.get(selector,
            channel = Channel(),
            payload = payload?.let { ZBytes.from(it) },
            target = target?.let { QueryTarget.valueOf(it.uppercase()) } ?: QueryTarget.BEST_MATCHING,
            attachment = attachment?.let { ZBytes.from(it) },
            timeout = Duration.ofMillis(timeout)
        ).getOrThrow()
        runBlocking {
            for (reply in channelReceiver) {
                reply.result.onSuccess { sample ->
                    when (sample.kind) {
                        SampleKind.PUT -> println("Received ('${sample.keyExpr}': '${sample.payload}')")
                        SampleKind.DELETE -> println("Received (DELETE '${sample.keyExpr}')")
                    }
                }.onFailure { error ->
                    println("Received (ERROR: '${error.message}')")
                }
            }
        }
    }

    private fun runCallbackExample(session: Session, selector: Selector) {
        session.get(selector,
            payload = payload?.let { ZBytes.from(it) },
            target = target?.let { QueryTarget.valueOf(it.uppercase()) } ?: QueryTarget.BEST_MATCHING,
            attachment = attachment?.let { ZBytes.from(it) },
            timeout = Duration.ofMillis(timeout),
            callback = { reply ->
                reply.result.onSuccess { sample ->
                    when (sample.kind) {
                        SampleKind.PUT -> println("Received ('${sample.keyExpr}': '${sample.payload}')")
                        SampleKind.DELETE -> println("Received (DELETE '${sample.keyExpr}')")
                    }
                }.onFailure { error ->
                    println("Received (ERROR: '${error.message}')")
                }
            },
        ).getOrThrow()
    }

    private fun runHandlerExample(session: Session, selector: Selector) {
        // Create your own handler implementation
        class ExampleHandler : Handler<Reply, Unit> {
            override fun handle(t: Reply) {
                t.result.onSuccess { sample ->
                    when (sample.kind) {
                        SampleKind.PUT -> println("Received ('${sample.keyExpr}': '${sample.payload}')")
                        SampleKind.DELETE -> println("Received (DELETE '${sample.keyExpr}')")
                    }
                }.onFailure { error ->
                    println("Received (ERROR: '${error.message}')")
                }
            }

            override fun receiver() {}
            override fun onClose() {}
        }

        session.get(selector,
            payload = payload?.let { ZBytes.from(it) },
            target = target?.let { QueryTarget.valueOf(it.uppercase()) } ?: QueryTarget.BEST_MATCHING,
            attachment = attachment?.let { ZBytes.from(it) },
            timeout = Duration.ofMillis(timeout),
            handler = ExampleHandler(), // Provide a handler instance
        ).getOrThrow()
    }

    private val selector by option(
        "-s",
        "--selector",
        help = "The selection of resources to query [default: demo/example/**]",
        metavar = "selector"
    ).default("demo/example/**")
    private val payload by option(
        "-p", "--payload", help = "An optional payload to put in the query.", metavar = "payload"
    )
    private val target by option(
        "-t",
        "--target",
        help = "The target queryables of the query. Default: BEST_MATCHING. " + "[possible values: BEST_MATCHING, ALL, ALL_COMPLETE]",
        metavar = "target"
    )
    private val timeout by option(
        "-o", "--timeout", help = "The query timeout in milliseconds [default: 10000]", metavar = "timeout"
    ).long().default(10000)
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val attachment by option(
        "-a",
        "--attach",
        help = "The attachment to add to the get. The key-value pairs are &-separated, and = serves as the separator between key and value.",
        metavar = "attach"
    )
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZGet(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZGetLiveliness.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import com.github.ajalt.clikt.parameters.types.long
import io.zenoh.handlers.Handler
import io.zenoh.keyexpr.KeyExpr
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.query.Reply
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking
import java.time.Duration

class ZGetLiveliness(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Get Liveliness example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()

        runChannelExample(session, keyExpr)

        session.close()
    }

    private fun runChannelExample(session: Session, keyExpr: KeyExpr) {
        val channel =
            session.liveliness().get(keyExpr, channel = Channel(), timeout = Duration.ofMillis(timeout)).getOrThrow()
        runBlocking {
            for (reply in channel) {
                reply.result.onSuccess {
                    println(">> Alive token ('${it.keyExpr}')")
                }.onFailure {
                    println(">> Received (ERROR: '${it.message}')")
                }
            }
        }
    }

    private fun runCallbackExample(session: Session, keyExpr: KeyExpr) {
        session.liveliness().get(keyExpr, timeout = Duration.ofMillis(timeout), callback = { reply ->
            reply.result.onSuccess {
                println(">> Alive token ('${it.keyExpr}')")
            }.onFailure {
                println(">> Received (ERROR: '${it.message}')")
            }
        }).getOrThrow()
    }

    private fun runHandlerExample(session: Session, keyExpr: KeyExpr) {
        // Create your own handler implementation
        class ExampleHandler : Handler<Reply, Unit> {
            override fun handle(t: Reply) {
                t.result.onSuccess {
                    println(">> Alive token ('${it.keyExpr}')")
                }.onFailure {
                    println(">> Received (ERROR: '${it.message}')")
                }
            }

            override fun receiver() {}
            override fun onClose() {}
        }

        session.liveliness().get(keyExpr, timeout = Duration.ofMillis(timeout), handler = ExampleHandler()).getOrThrow()
    }

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val key by option(
        "-k",
        "--key",
        help = "The key expression matching liveliness tokens to query. [default: group1/**]",
        metavar = "key"
    ).default("group1/**")
    private val timeout by option(
        "-o", "--timeout", help = "The query timeout in milliseconds [default: 10000]", metavar = "timeout"
    ).long().default(10000)
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZGetLiveliness(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZInfo.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*

class ZInfo(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Info example"
) {
    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val info = session.info()
        println("zid: ${info.zid().getOrThrow()}")
        println("routers zid: ${info.routersZid().getOrThrow()}")
        println("peers zid: ${info.peersZid().getOrThrow()}")
        session.close()
    }


    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZInfo(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZLiveliness.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.keyexpr.intoKeyExpr
import java.util.concurrent.CountDownLatch

class ZLiveliness(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Liveliness example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()
        session.liveliness().declareToken(keyExpr)

        CountDownLatch(1).await() // A countdown latch is used here to block execution while the liveliness token
                                         // is declared. Typically, this wouldn't be needed.
        session.close()
    }

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val key by option(
        "-k", "--key", help = "The key expression to subscribe to [default: group1/zenoh-kotlin]", metavar = "key"
    ).default("group1/zenoh-kotlin")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZLiveliness(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZPing.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.arguments.argument
import com.github.ajalt.clikt.parameters.arguments.default
import com.github.ajalt.clikt.parameters.options.*
import com.github.ajalt.clikt.parameters.types.double
import com.github.ajalt.clikt.parameters.types.int
import io.zenoh.bytes.ZBytes
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.qos.CongestionControl
import io.zenoh.qos.QoS
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking

class ZPing(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Ping example"
) {
    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExprPing = "test/ping".intoKeyExpr().getOrThrow()
        val keyExprPong = "test/pong".intoKeyExpr().getOrThrow()

        val sub = session.declareSubscriber(keyExprPong, Channel()).getOrThrow()
        val publisher = session.declarePublisher(keyExprPing, qos = QoS(CongestionControl.BLOCK, express = !noExpress)).getOrThrow()

        val data = ByteArray(payloadSize)
        for (i in 0..<payloadSize) {
            data[i] = (i % 10).toByte()
        }
        val payload = ZBytes.from(data)
        val samples = arrayListOf<Long>()

        // -- warmup --
        println("Warming up for $warmup...")
        val startTime = System.currentTimeMillis()
        while (System.currentTimeMillis() - startTime < warmup) {
            publisher.put(payload).getOrThrow()
            runBlocking { sub.receiver.receive() }
        }

        for (x in 0..n ) {
            val writeTime = System.nanoTime()
            publisher.put(payload).getOrThrow()
            runBlocking { sub.receiver.receive() }
            val ts = (System.nanoTime() - writeTime) / 1_000 //convert to microseconds
            samples.add(ts)
        }

        for (x in samples.withIndex()) {
            println("$payloadSize bytes: seq=${x.index} rtt=${x.value}µs lat=${x.value / 2}µs")
        }
    }


    private val payloadSize by argument(
        "payload_size",
        help = "Sets the size of the payload to publish [Default: 8]"
    ).int().default(8)
    private val noExpress: Boolean by option(
        "--no-express", help = "Express for sending data."
    ).flag(default = false)
    private val warmup: Double by option(
        "-w",
        "--warmup",
        metavar = "warmup",
        help = "The number of seconds to warm up (double) [default: 1]"
    ).double().default(1.0)
    private val n: Int by option(
        "-n",
        "--samples",
        metavar = "samples",
        help = "The number of round-trips to measure [default: 100]"
    ).int().default(100)

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZPing(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZPong.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.qos.CongestionControl
import io.zenoh.qos.QoS
import io.zenoh.sample.Sample
import java.util.concurrent.CountDownLatch

class ZPong(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh ZPong example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")
        val latch = CountDownLatch(1)

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExprPing = "test/ping".intoKeyExpr().getOrThrow()
        val keyExprPong = "test/pong".intoKeyExpr().getOrThrow()

        val publisher = session.declarePublisher(keyExprPong, qos = QoS(CongestionControl.BLOCK, express = !noExpress)).getOrThrow()
        session.declareSubscriber(keyExprPing, callback = { sample: Sample -> publisher.put(sample.payload).getOrThrow() }).getOrThrow()

        latch.await()
    }


    private val noExpress: Boolean by option(
        "--no-express", help = "Express for sending data."
    ).flag(default = false)

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) {
    val zPong = ZPong(args.isEmpty())
    zPong.main(args)
}
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZPub.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.bytes.ZBytes
import io.zenoh.keyexpr.intoKeyExpr

class ZPub(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Pub example"
) {
    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()

        println("Declaring publisher on '$keyExpr'...")
        val publisher = session.declarePublisher(keyExpr).getOrThrow()

        println("Press CTRL-C to quit...")
        val attachment = attachment?.toByteArray()

        var idx = 0
        while (true) {
            Thread.sleep(1000)
            val payload = "[${
                idx.toString().padStart(4, ' ')
            }] $value"
            println(
                "Putting Data ('$keyExpr': '$payload')..."
            )
            attachment?.let {
                publisher.put(ZBytes.from(payload), attachment = ZBytes.from(it))
            } ?: let { publisher.put(ZBytes.from(payload)) }
            idx++
        }
    }


    private val key by option(
        "-k", "--key", help = "The key expression to write to [default: demo/example/zenoh-kotlin-pub]", metavar = "key"
    ).default("demo/example/zenoh-kotlin-pub")
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val value by option(
        "-v", "--value", help = "The value to write. [Default: \"Pub from Kotlin!\"]", metavar = "value"
    ).default("Pub from Kotlin!")
    private val attachment by option(
        "-a",
        "--attach",
        help = "The attachments to add to each put. The key-value pairs are &-separated, and = serves as the separator between key and value.",
        metavar = "attach"
    )
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZPub(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZPubThr.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.arguments.argument
import com.github.ajalt.clikt.parameters.arguments.default
import com.github.ajalt.clikt.parameters.options.*
import com.github.ajalt.clikt.parameters.types.boolean
import com.github.ajalt.clikt.parameters.types.int
import com.github.ajalt.clikt.parameters.types.ulong
import io.zenoh.bytes.ZBytes
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.qos.CongestionControl
import io.zenoh.qos.Priority
import io.zenoh.qos.QoS

class ZPubThr(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Throughput example"
) {

    override fun run() {
        Zenoh.initLogFromEnvOr("error")

        val data = ByteArray(payloadSize)
        for (i in 0..<payloadSize) {
            data[i] = (i % 10).toByte()
        }
        val payload = ZBytes.from(data)

        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        val qos = QoS(
            congestionControl = CongestionControl.BLOCK,
            priority = priorityInput?.let { Priority.entries[it] } ?: Priority.DATA,
        )

        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = "test/thr".intoKeyExpr().getOrThrow()
        val publisher = session.declarePublisher(keyExpr, qos = qos).getOrThrow()

        println("Publisher declared on test/thr.")
        var count: Long = 0
        var start = System.currentTimeMillis()
        val number = number.toLong()

        println("Press CTRL-C to quit...")
        while (true) {
            publisher.put(payload).getOrThrow()
            if (statsPrint) {
                if (count < number) {
                    count++
                } else {
                    val throughput = count * 1000 / (System.currentTimeMillis() - start)
                    println("$throughput msgs/s")
                    count = 0
                    start = System.currentTimeMillis()
                }
            }
        }
    }

    private val payloadSize by argument(
        "payload_size",
        help = "Sets the size of the payload to publish [Default: 8]"
    ).int().default(8)

    private val priorityInput by option(
        "-p",
        "--priority",
        help = "Priority for sending data",
        metavar = "priority"
    ).int()
    private val number by option(
        "-n",
        "--number",
        help = "Number of messages in each throughput measurements [default: 100000]",
        metavar = "number"
    ).ulong().default(100000u)
    private val statsPrint by option("-t", "--print", help = "Print the statistics").boolean().default(true)
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZPubThr(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZPut.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.bytes.ZBytes
import io.zenoh.keyexpr.intoKeyExpr

class ZPut(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Put example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening Session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()

        session.put(keyExpr, ZBytes.from(value), attachment = attachment?.let { ZBytes.from(it) })
            .onSuccess { println("Putting Data ('$keyExpr': '$value')...") }.getOrThrow()

        session.close()
    }

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val key by option(
        "-k", "--key", help = "The key expression to write to [default: demo/example/zenoh-kotlin-put]", metavar = "key"
    ).default("demo/example/zenoh-kotlin-put")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val value by option(
        "-v", "--value", help = "The value to write. [Default: \"Put from Kotlin!\"]", metavar = "value"
    ).default("Put from Kotlin!")
    private val attachment by option(
        "-a",
        "--attach",
        help = "The attachment to add to the put. The key-value pairs are &-separated, and = serves as the separator between key and value.",
        metavar = "attach"
    )
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZPut(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZQuerier.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import com.github.ajalt.clikt.parameters.types.long
import io.zenoh.annotations.Unstable
import io.zenoh.bytes.ZBytes
import io.zenoh.query.QueryTarget
import io.zenoh.query.intoSelector
import java.time.Duration

class ZQuerier(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Querier example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        val session = Zenoh.open(config).getOrThrow()
        val selector = selector.intoSelector().getOrThrow()

        val target = target ?.let{ QueryTarget.valueOf(it.uppercase()) } ?: QueryTarget.BEST_MATCHING
        val timeout = Duration.ofMillis(timeout)
        val querier = session.declareQuerier(selector.keyExpr, target, timeout = timeout).getOrThrow()

        for (idx in 0..Int.MAX_VALUE) {
            Thread.sleep(1000)
            val payload = "[${idx.toString().padStart(4, ' ')}] ${payload ?: ""}"
            println("Querying '$selector' with payload: '$payload'...")
            querier.get(callback = {
                it.result.onSuccess { sample ->
                    println(">> Received ('${sample.keyExpr}': '${sample.payload}')")
                }.onFailure { error ->
                    println(">> Received (ERROR: '${error.message}')")
                }
            }, payload = ZBytes.from(payload), parameters = selector.parameters)
        }

        session.close()
    }

    private val selector by option(
        "-s",
        "--selector",
        help = "The selection of resources to query [default: demo/example/**]",
        metavar = "selector"
    ).default("demo/example/**")
    private val payload by option(
        "-p", "--payload", help = "An optional payload to put in the queries.", metavar = "payload"
    )
    private val target by option(
        "-t",
        "--target",
        help = "The target queryables of the querier. Default: BEST_MATCHING. " + "[possible values: BEST_MATCHING, ALL, ALL_COMPLETE]",
        metavar = "target"
    )
    private val timeout by option(
        "-o", "--timeout", help = "The query timeout in milliseconds [default: 10000]", metavar = "timeout"
    ).long().default(10000)
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZQuerier(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZQueryable.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.bytes.ZBytes
import io.zenoh.handlers.Handler
import io.zenoh.keyexpr.KeyExpr
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.query.Query
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking
import org.apache.commons.net.ntp.TimeStamp
import java.util.concurrent.CountDownLatch

class ZQueryable(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Queryable example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()

        // Run the queryable example through one of the examples below:
        runChannelExample(session, keyExpr)
        // runCallbackExample(session, keyExpr)
        // runHandlerExample(session, keyExpr)

        session.close()
    }

    private fun runChannelExample(session: Session, keyExpr: KeyExpr) {
        println("Declaring Queryable on $key...")
        val queryable = session.declareQueryable(keyExpr, Channel()).getOrThrow()
        runBlocking {
            for (query in queryable.receiver) {
                val valueInfo = query.payload?.let { value -> " with value '$value'" } ?: ""
                println(">> [Queryable] Received Query '${query.selector}' $valueInfo")
                query.reply(
                    keyExpr,
                    payload = ZBytes.from(value),
                    timestamp = TimeStamp.getCurrentTime()
                ).onFailure { println(">> [Queryable ] Error sending reply: $it") }
            }
        }
        queryable.close()
    }

    private fun runCallbackExample(session: Session, keyExpr: KeyExpr) {
        println("Declaring Queryable on $key...")
        val queryable = session.declareQueryable(keyExpr, callback = { query ->
            val valueInfo = query.payload?.let { value -> " with value '$value'" } ?: ""
            println(">> [Queryable] Received Query '${query.selector}' $valueInfo")
            query.reply(
                keyExpr,
                payload = ZBytes.from(value),
                timestamp = TimeStamp.getCurrentTime()
            ).onFailure { println(">> [Queryable ] Error sending reply: $it") }
        }).getOrThrow()

        CountDownLatch(1).await() // A countdown latch is used here to block execution while queries are received.
                                         // Typically, this wouldn't be needed.

        queryable.close()
    }

    private fun runHandlerExample(session: Session, keyExpr: KeyExpr) {

        // Create your own handler implementation
        class ExampleHandler : Handler<Query, Unit> {
            override fun handle(t: Query) {
                val valueInfo = t.payload?.let { value -> " with value '$value'" } ?: ""
                println(">> [Queryable] Received Query '${t.selector}' $valueInfo")
                t.reply(
                    keyExpr,
                    payload = ZBytes.from(value),
                    timestamp = TimeStamp.getCurrentTime()
                ).onFailure { println(">> [Queryable ] Error sending reply: $it") }
            }

            override fun receiver() {}
            override fun onClose() {}
        }

        // Declare the queryable, providing an instance of the handler
        println("Declaring Queryable on $key...")
        val queryable = session.declareQueryable(keyExpr, handler = ExampleHandler()).getOrThrow()

        CountDownLatch(1).await() // A countdown latch is used here to block execution while queries are received.
                                         // Typically, this wouldn't be needed.

        queryable.close()
    }

    private val key by option(
        "-k",
        "--key",
        help = "The key expression to write to [default: demo/example/zenoh-kotlin-queryable]",
        metavar = "key"
    ).default("demo/example/zenoh-kotlin-queryable")
    private val value by option(
        "-v", "--value", help = "The value to reply to queries [default: \"Queryable from Kotlin!\"]", metavar = "value"
    ).default("Queryable from Kotlin!")
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZQueryable(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZScout.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import io.zenoh.config.WhatAmI
import io.zenoh.handlers.Handler
import io.zenoh.scouting.Hello
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking
import java.util.concurrent.CountDownLatch

class ZScout : CliktCommand(
    help = "Zenoh Scouting example"
) {
    override fun run() {

        Zenoh.initLogFromEnvOr("error")

        // Run the scout example with one of the implementations below:
        runChannelExample()
        // runCallbackExample()
        // runHandlerExample()
    }

    private fun runChannelExample() {
        println("Scouting...")

        val scout = Zenoh.scout(channel = Channel(), whatAmI = setOf(WhatAmI.Peer, WhatAmI.Router)).getOrThrow()
        runBlocking {
            for (hello in scout.receiver) {
                println(hello)
            }
        }

        scout.stop()
    }

    private fun runCallbackExample() {
        println("Scouting...")

        val scout = Zenoh.scout(whatAmI = setOf(WhatAmI.Peer, WhatAmI.Router), callback = ::println).getOrThrow()

        CountDownLatch(1).await() // A countdown latch is used here to block execution while queries are received.
                                         // Typically, this wouldn't be needed.
        scout.stop()
    }

    private fun runHandlerExample() {

        // Create your own Handler implementation:
        class ExampleHandler: Handler<Hello, Unit> {
            override fun handle(t: Hello) = println(t)

            override fun receiver() {}

            override fun onClose() {}
        }

        println("Scouting...")

        // Declare the scout with the handler
        val scout = Zenoh.scout(whatAmI = setOf(WhatAmI.Peer, WhatAmI.Router), handler = ExampleHandler()).getOrThrow()

        CountDownLatch(1).await() // A countdown latch is used here to block execution while queries are received.
                                  // Typically, this wouldn't be needed.
        scout.stop()
    }
}

fun main(args: Array<String>) = ZScout().main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZSub.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.handlers.Handler
import io.zenoh.keyexpr.KeyExpr
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.sample.Sample
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking
import java.util.concurrent.CountDownLatch

class ZSub(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Sub example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()

        println("Declaring Subscriber on '$keyExpr'...")

        runChannelExample(session, keyExpr)
    }

    private fun runChannelExample(session: Session, keyExpr: KeyExpr) {
        val subscriber = session.declareSubscriber(keyExpr, Channel()).getOrThrow()
        runBlocking {
            for (sample in subscriber.receiver) {
                println(">> [Subscriber] Received ${sample.kind} ('${sample.keyExpr}': '${sample.payload}'" + "${
                    sample.attachment?.let {
                        ", with attachment: $it"
                    } ?: ""
                })")
            }
        }

        subscriber.close()
    }

    private fun runCallbackExample(session: Session, keyExpr: KeyExpr) {
        val subscriber = session.declareSubscriber(keyExpr, callback = { sample ->
                println(">> [Subscriber] Received ${sample.kind} ('${sample.keyExpr}': '${sample.payload}'" + "${
                    sample.attachment?.let {
                        ", with attachment: $it"
                    } ?: ""
                })")
        }).getOrThrow()


        CountDownLatch(1).await() // A countdown latch is used here to block execution while samples are received.
                                         // Typically, this wouldn't be needed.
        subscriber.close()
    }

    private fun runHandlerExample(session: Session, keyExpr: KeyExpr) {
        class ExampleHandler: Handler<Sample, Unit> {
            override fun handle(t: Sample) {
                println(">> [Subscriber] Received ${t.kind} ('${t.keyExpr}': '${t.payload}'" + "${
                    t.attachment?.let {
                        ", with attachment: $it"
                    } ?: ""
                })")
            }

            override fun receiver() {}
            override fun onClose() {}
        }

        val subscriber = session.declareSubscriber(keyExpr, handler = ExampleHandler()).getOrThrow()

        CountDownLatch(1).await() // A countdown latch is used here to block execution while samples are received.
                                         // Typically, this wouldn't be needed.
        subscriber.close()
    }

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val key by option(
        "-k", "--key", help = "The key expression to subscribe to [default: demo/example/**]", metavar = "key"
    ).default("demo/example/**")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZSub(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZSubLiveliness.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.sample.SampleKind
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.runBlocking

class ZSubLiveliness(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Sub Liveliness example"
) {

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        println("Opening session...")
        val session = Zenoh.open(config).getOrThrow()
        val keyExpr = key.intoKeyExpr().getOrThrow()
        val subscriber =
            session.liveliness().declareSubscriber(keyExpr, channel = Channel(), history = history).getOrThrow()

        runBlocking {
            for (sample in subscriber.receiver) {
                when (sample.kind) {
                    SampleKind.PUT -> println(">> [LivelinessSubscriber] New alive token ('${sample.keyExpr}')")
                    SampleKind.DELETE -> println(">> [LivelinessSubscriber] Dropped token ('${sample.keyExpr}')")
                }
            }
        }

        session.close()
    }

    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val key by option(
        "-k", "--key", help = "The key expression to subscribe to [default: group1/**]", metavar = "key"
    ).default("group1/**")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val history: Boolean by option(
        "--history",
        help = "Get historical liveliness tokens."
    ).flag(default = false)
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)
}

fun main(args: Array<String>) = ZSubLiveliness(args.isEmpty()).main(args)
```

---

# Example: examples--src--main--kotlin--io.zenoh--ZSubThr.kt

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

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.*
import com.github.ajalt.clikt.parameters.types.ulong
import io.zenoh.keyexpr.intoKeyExpr
import io.zenoh.pubsub.Subscriber
import kotlin.system.exitProcess

class ZSubThr(private val emptyArgs: Boolean) : CliktCommand(
    help = "Zenoh Subscriber Throughput test"
) {
    companion object {
        private const val NANOS_TO_SEC = 1_000_000_000L
    }

    private var batchCount = 0u
    private var count = 0u
    private var startTimestampNs: Long = 0
    private var globalStartTimestampNs: Long = 0

    private fun listener(number: ULong) {
        if (batchCount > samples) {
            subscriber.close()
            report()
        }
        if (count == 0u) {
            startTimestampNs = System.nanoTime()
            if (globalStartTimestampNs == 0L) {
                globalStartTimestampNs = startTimestampNs
            }
            count++
            return
        }
        if (count < number) {
            count++
            return
        }
        val stop = System.nanoTime()
        val elapsedTimeSecs = (stop - startTimestampNs).toDouble() / NANOS_TO_SEC
        val messagesPerSec = number.toLong() / elapsedTimeSecs
        println("$messagesPerSec msgs/sec")
        batchCount++
        count = 0u
    }

    private fun report() {
        val end = System.nanoTime()
        val total = batchCount * number + count
        val elapsedTimeSecs = (end - globalStartTimestampNs).toDouble() / NANOS_TO_SEC
        val globalMessagesPerSec = total.toLong() / elapsedTimeSecs
        print("Received $total messages in $elapsedTimeSecs seconds: averaged $globalMessagesPerSec msgs/sec")
        exitProcess(0)
    }

    private lateinit var subscriber: Subscriber<Unit>

    override fun run() {
        val config = loadConfig(emptyArgs, configFile, connect, listen, noMulticastScouting, mode)

        Zenoh.initLogFromEnvOr("error")

        "test/thr".intoKeyExpr().onSuccess { keyExpr ->
            keyExpr.use {
                println("Opening Session")
                Zenoh.open(config).onSuccess { session ->
                    session.use {
                        println("Press CTRL-C to quit...")
                        subscriber =
                            session.declareSubscriber(
                                keyExpr,
                                callback = { listener(number) },
                            ).getOrThrow()
                        while (subscriber.isValid()) {/* Keep alive the subscriber until the test is done. */
                            Thread.sleep(1000)
                        }
                    }
                }
            }
        }
    }

    private val samples by option(
        "-s", "--samples", help = "Number of throughput measurements [default: 10]", metavar = "number"
    ).ulong().default(10u)
    private val number by option(
        "-n",
        "--number",
        help = "Number of messages in each throughput measurements [default: 100000]",
        metavar = "number"
    ).ulong().default(10000u)
    private val configFile by option("-c", "--config", help = "A configuration file.", metavar = "config")
    private val connect: List<String> by option(
        "-e", "--connect", help = "Endpoints to connect to.", metavar = "connect"
    ).multiple()
    private val listen: List<String> by option(
        "-l", "--listen", help = "Endpoints to listen on.", metavar = "listen"
    ).multiple()
    private val mode by option(
        "-m",
        "--mode",
        help = "The session mode. Default: peer. Possible values: [peer, client, router]",
        metavar = "mode"
    ).default("peer")
    private val noMulticastScouting: Boolean by option(
        "--no-multicast-scouting", help = "Disable the multicast-based scouting mechanism."
    ).flag(default = false)

}

fun main(args: Array<String>) = ZSubThr(args.isEmpty()).main(args)
```

---

