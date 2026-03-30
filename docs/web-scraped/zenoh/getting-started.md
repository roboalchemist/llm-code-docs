# Getting Started with Zenoh

# https://zenoh.io/docs/getting-started/deployment/

Source: https://zenoh.io/docs/getting-started/deployment/

* [Home](../../../)
* [Documentation](../../../docs/getting-started/first-app/)
* [Use Cases](../../../usecases/)
* [Community](../../../community/)
* [Adopters](../../../adopters/)
* [Media](../../../media/)
* [Blog](../../../blog/2025-12-11-zenoh-jiaolong/)

# Deployment

[Edit on GitHub](https://github.com/atolab/zenoh-web/tree/master/content/docs/getting-started/deployment.md)

## Overview

## Peer to peer

By default Zenoh applications are configured to communicate peer to peer (`peer` mode). All applications in the local network directly communicate with each other.

**Configuration**

```
{ mode: "peer", } 
```

### Scouting

Zenoh applications in `peer` mode run both `multicast` and `gossip` scouting to discover other applications or Zenoh routers and connect them.

**Multicast scouting**

Zenoh applications in `peer` mode join multicast group `224.0.0.224` on UDP port `7446` and send scout messages on this address to discover local applications and routers. They automatically connect to all accessible `peer` mode applications and routers they discover. The scouting address and behavior can be configured.

**Configuration**

```
{ mode: "peer", scouting: { multicast: { enabled: true, address: "224.0.0.224:7446", interface: "auto", autoconnect: { router: [], peer: ["router", "peer"] }, listen: true, }, }, } 
```

**Gossip scouting**

Zenoh applications in `peer` mode forward all local applications and routers that they already discovered to newly scouted applications. This is useful when multicast communications are not available. But applications need to connect first to an entry point to discover the rest of the system. This entry point is typically one or several Zenoh routers but can also be one or several other peers. Those entry points are configured through the `connect` section of the configuration.

**Configuration**

```
{ mode: "peer", connect: { endpoints: ["tcp/192.168.1.1:7447", "tcp/192.168.1.2:7447"], }, scouting: { gossip: { enabled: true, multihop: false, autoconnect: { router: [], peer: ["router", "peer"] }, }, }, } 
```

## Client

Communicating peer to peer implies establishing multiple sessions with multiple other peers and maintaining a state for those sessions. Maintaining such states can be undesirable for scalability reasons or because the application runs on a constrained device. In this case the Zenoh application can be configured to operate in client mode. In this mode, the application will maintain, at any given time, a single session with another process (typically a Zenoh router) that will grant it connectivity with the rest of the system.

**Configuration**

```
{ mode: "client", } 
```

### Scouting

Zenoh applications in `client` mode run `multicast` scouting to discover Zenoh routers and connect to them. In addition, the endpoints of one or several routers can be configured in the `connect` section.

**Configuration**

```
{ mode: "client", connect: { endpoints: ["tcp/192.168.1.1:7447", "tcp/192.168.1.2:7447"], }, } 
```

## Peers mesh

In a mesh network, applications cannot directly connect to each other. Peer to peer and brokered communications may be impossible or undesirable. Zenoh applications in `peer` mode can run a linkstate protocol that allow them to communicate in a mesh network.

**Configuration**

```
{ mode: "peer", routing: { peer: { mode: "linkstate", }, }, } 
```

Note: if a Zenoh router is used to connect a local mesh of Zenoh peers to a wider network, this router also needs to be configured with the same `routing` section.

## Zenoh router

Zenoh routers route data between clients and local subnetworks of peers. They can be deployed using any topology. They, by default, never try to interconnect themself automatically and must be configured with the endpoints of the other routers they are supposed to connect to.

```
{ connect: { endpoints: ["tcp/192.168.1.1:7447", "tcp/192.168.1.2:7447"], }, } 
```

**Next up**: [For a quick test using Docker](/docs/getting-started/quick-test/)

---

# https://zenoh.io/docs/getting-started/first-app/

Source: https://zenoh.io/docs/getting-started/first-app/

* [Home](../../../)
* [Documentation](../../../docs/getting-started/first-app/)
* [Use Cases](../../../usecases/)
* [Community](../../../community/)
* [Adopters](../../../adopters/)
* [Media](../../../media/)
* [Blog](../../../blog/2025-12-11-zenoh-jiaolong/)

# Your first Zenoh app

[Edit on GitHub](https://github.com/atolab/zenoh-web/tree/master/content/docs/getting-started/first-app.md)

Let us take a step-by-step approach in putting together your first Zenoh application in Python. As the first step, let us see how we get some data from a temperature sensor in our kitchen. Then we see how we can route this data to store and perform some analytics.

Before cranking some code, let’s define some terminology.

Zenoh deals with keys/values where each key is a path and is associated to a value. A key looks like just a Unix file system path, such as `myhome/kitchen/temp`. The value can be defined with different encodings (string, JSON, raw bytes buffer…).

Let’s get started!

## Pub/sub in Zenoh

First thing first, we need to install the [zenoh Python library](https://github.com/eclipse-zenoh/zenoh-python).

```
pip install eclipse-zenoh pip install eclipse-zenoh 
```

*The examples are updated to use the 1.0 version currently in rc, which is why version must be specified in the installation command. You can find more information about the 1.0 changes in the [migration guides](https://zenoh.io/docs/migration_1.0/concepts/).*

Then, let’s write an application, `z_sensor.py` that will produce temperature measurements at each second:

```
import zenoh, random, time import zenoh, random, time import zenoh, random, time   random.seed() random.seed() .   def read_temp(): def read_temp(): def read_temp return random.randint(15, 30)  return random.randint(15, 30) return. 15 30   if __name__ == "__main__": if __name__ == "__main__": if == "__main__" with zenoh.open(zenoh.Config()) as session:  with zenoh.open(zenoh.Config()) as session: with.. as key = 'myhome/kitchen/temp'  key = 'myhome/kitchen/temp' ='myhome/kitchen/temp' pub = session.declare_publisher(key)  pub = session.declare_publisher(key) =. while True:  while True: while True t = read_temp()  t = read_temp() = buf = f"{t}"  buf = f"{t}" = f "{} " print(f"Putting Data ('{key}': '{buf}')...")  print(f"Putting Data ('{key}': '{buf}')...") print f"Putting Data ('{}': '{}')..." pub.put(buf)  pub.put(buf) . time.sleep(1)  time.sleep(1) . 1
```

Now we need a subscriber, `z_subscriber.py` that can receive the measurements:

```
import zenoh, time import zenoh, time import zenoh, time   def listener(sample): def listener(sample): def listener print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')")  print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')") print f "Received {.} ('{.}': '{..}')"   if __name__ == "__main__": if __name__ == "__main__": if == "__main__" with zenoh.open(zenoh.Config()) as session:  with zenoh.open(zenoh.Config()) as session: with.. as sub = session.declare_subscriber('myhome/kitchen/temp', listener)  sub = session.declare_subscriber('myhome/kitchen/temp', listener) =.'myhome/kitchen/temp' time.sleep(60)  time.sleep(60) . 60
```

Start the subscriber:

```
python3 z_subscriber.py python3 z_subscriber.py 
```

The subscriber waits for an update on `myhome/kitchen/temp`.

Now start `z_sensor.py` as follows

```
python3 z_sensor.py python3 z_sensor.py 
```

You can see the values produced by the sensor being consumed by the subscriber.

## Store and Query in Zenoh

As the next step, let’s see how the value generated by a publisher can be stored in Zenoh. For this, we use [Zenoh router](../installation) (`zenohd`). By default, a Zenoh router starts without any storage. In order to store the temperature, we need to configure one. Create a `zenoh-myhome.json5` configuration file for Zenoh with this content:

```
{ plugins: { rest: { // activate and configure the REST plugin http_port: 8000 // with HTTP server listening on port 8000 }, storage_manager: { // activate and configure the storage_manager plugin storages: { myhome: { // configure a "myhome" storage key_expr: "myhome/**", // which subscribes and replies to query on myhome/** volume: { // and using the "memory" volume (always present by default) id: "memory" } } } } } } 
```

[Install](../installation) and start the Zenoh router with this configuration file:

```
zenohd -c zenoh-myhome.json5 zenohd -c zenoh-myhome.json5 
```

Now the data generated by our temperature sensor is stored in memory. We can retrieve the latest temperature value stored in Zenoh:

```
import zenoh import zenoh import zenoh   if __name__ == "__main__": if __name__ == "__main__": if == "__main__" with zenoh.open(zenoh.Config()) as session:  with zenoh.open(zenoh.Config()) as session: with.. as replies = session.get('myhome/kitchen/temp')  replies = session.get('myhome/kitchen/temp') =.'myhome/kitchen/temp' for reply in replies:  for reply in replies: for in try:  try: try print("Received ('{}': '{}')"  print("Received ('{}': '{}')" print"Received ('{}': '{}')" .format(reply.ok.key_expr, reply.ok.payload.to_string()))  .format(reply.ok.key_expr, reply.ok.payload.to_string())) ...... except:  except: except print("Received (ERROR: '{}')"  print("Received (ERROR: '{}')" print"Received (ERROR: '{}')" .format(reply.err.payload.to_string()))  .format(reply.err.payload.to_string())) ....
```

## Other examples

You can also have a look at the examples provided with each client API:

* **Rust**: <https://github.com/eclipse-zenoh/zenoh/tree/main/examples>
* **Python**: <https://github.com/eclipse-zenoh/zenoh-python/tree/main/examples>
* **C**: <https://github.com/eclipse-zenoh/zenoh-c/tree/main/examples>

**Next up**: [Installation](/docs/getting-started/installation/)

---

# https://zenoh.io/docs/getting-started/installation/

Source: https://zenoh.io/docs/getting-started/installation/

![](../../../img/zenoh-dragon-bg-150x163.png)

# Installation

To start playing with Zenoh we need the Zenoh router and/or the Zenoh client library.

## Installing client library

To develop your application Zenoh, you need to install a Zenoh client library.
Depending on your programming language, pick one of the following API and refer to the installation and usage instructions in here:

Note that if you wish to always have access to all of Zenoh’s latest features, Rust is Zenoh’s original language, and will therefore always be the most feature-complete version.

## Installing the Zenoh router

The Zenoh router (a.k.a. `zenohd`) and its plugins are currently available as pre-built binaries for various platforms. All release packages can be downloaded from:

`zenohd`

Each subdirectory has the name of the Rust target. See the platforms each target corresponds to on <https://doc.rust-lang.org/stable/rustc/platform-support.html>

You can also install it via a package manager on macOS (homebrew) or Linux Debian (apt). See instructions below.

For other platforms, you can use the [Docker image](../quick-test#run-zenoh-in-docker) or [build it](https://github.com/eclipse-zenoh/zenoh#how-to-build-it) directly on your platform.

### MacOS

Tap our brew package repository:

`$ brew tap eclipse-zenoh/homebrew-zenoh`

Install Zenoh:

`$ brew install zenoh`

Then you can start the Zenoh router with this command:

`$ zenohd`

### Ubuntu or any Debian

Add Eclipse Zenoh public key to apt keyring

`$ curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg`

Add Eclipse Zenoh private repository to the sources list:

`$ echo "deb [signed-by=/etc/apt/keyrings/zenoh-public-key.gpg] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list > /dev/null
$ sudo apt update`

Install Zenoh:

`$ sudo apt install zenoh`

Then you can start the Zenoh router with this command:

`$ zenohd`

### Windows

Download the Zenoh archive from <https://download.eclipse.org/zenoh/zenoh/latest/> :

`x86_64-pc-windows-msvc/zenoh-<version>-x86_64-pc-windows-msvc.zip`

Unzip the archive.

Go to Zenoh directory and start Zenoh router:

`> cd C:\path\to\zenoh\dir
> zenohd.exe`

## Testing Your Installation

To test the installation, try to see the Zenoh man page by executing the following command:

`$ zenohd --help`

You should see the following output on your console:

`2024-08-12T13:27:29.724708Z INFO main ThreadId(01) zenohd: zenohd v0.11.0-dev-965-g764be602d built with rustc 1.75.0 (82e1608df 2023-12-21)
The zenoh router
Usage: zenohd [OPTIONS]
Options:
 -c, --config <PATH>
 The configuration file. Currently, this file must be a valid JSON5 or YAML file
 -l, --listen <ENDPOINT>
 Locators on which this router will listen for incoming sessions. Repeat this option to open several listeners
 -e, --connect <ENDPOINT>
 A peer locator this router will try to connect to. Repeat this option to connect to several peers
 -i, --id <ID>
 The identifier (as an hexadecimal string, with odd number of chars - e.g.: A0B23...) that zenohd must use. If not set, a random unsigned 128bit integer will be used. WARNING: this identifier must be unique in the system and must be 16 bytes maximum (32 chars)!
 -P, --plugin <PLUGIN>
 A plugin that MUST be loaded. You can give just the name of the plugin, zenohd will search for a library named 'libzenoh_plugin_\<name\>.so' (exact name depending the OS). Or you can give such a string: "\<plugin_name\>:\<library_path\>" Repeat this option to load several plugins. If loading failed, zenohd will exit
 --plugin-search-dir <PATH>
 Directory where to search for plugins libraries to load. Repeat this option to specify several search directories
 --no-timestamp
 By default zenohd adds a HLC-generated Timestamp to each routed Data if there isn't already one. This option disables this feature
 --no-multicast-scouting
 By default zenohd replies to multicast scouting messages for being discovered by peers and clients. This option disables this feature
 --rest-http-port <SOCKET>
 Configures HTTP interface for the REST API (enabled by default on port 8000). Accepted values: - a port number - a string with format `<local_ip>:<port_number>` (to bind the HTTP server to a specific interface) - `none` to disable the REST API
 --cfg <CFG>
 Allows arbitrary configuration changes as column-separated KEY:VALUE pairs, where: - KEY must be a valid config path. - VALUE must be a valid JSON5 string that can be deserialized to the expected type for the KEY field.
 Examples: - `--cfg='startup/subscribe:["demo/**"]'` - `--cfg='plugins/storage_manager/storages/demo:{key_expr:"demo/example/**",volume:"memory"}'`
 --adminspace-permissions <[r|w|rw|none]>
 Configure the read and/or write permissions on the admin space. Default is read only
 -h, --help
 Print help (see a summary with '-h')
 -V, --version
 Print version`

##### Eclipse Incubation

![](../../../img/eclipse-incubation.png)

![](../../../img/eclipse-incubation.png)

Eclipse zenoh ™ is an incubating project under the Eclipse Foundation.

##### More Information

[Legal](https://www.eclipse.org/legal)

[Privacy policy](https://www.eclipse.org/legal/privacy.php)

[Terms of use](https://www.eclipse.org/legal/termsofuse.php)

[Copyright](https://www.eclipse.org/legal/copyright.php)

[Report a security issue](https://www.eclipse.org/security/)

[Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/)

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

[Eclipse Foundation](https://www.eclipse.org/)

##### Sponsored by:

[![](../../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../../img/eclipse-foundation.svg)

[![](../../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../../docs/overview/what-is-zenoh)

![](../../../img/zenoh-dragon-150x163.png)

![](../../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/docs/getting-started/first-app/

Source: https://zenoh.io/docs/getting-started/first-app/

* [Home](../../../)
* [Documentation](../../../docs/getting-started/first-app/)
* [Use Cases](../../../usecases/)
* [Community](../../../community/)
* [Adopters](../../../adopters/)
* [Media](../../../media/)
* [Blog](../../../blog/2025-12-11-zenoh-jiaolong/)

# Your first Zenoh app

[Edit on GitHub](https://github.com/atolab/zenoh-web/tree/master/content/docs/getting-started/first-app.md)

Let us take a step-by-step approach in putting together your first Zenoh application in Python. As the first step, let us see how we get some data from a temperature sensor in our kitchen. Then we see how we can route this data to store and perform some analytics.

Before cranking some code, let’s define some terminology.

Zenoh deals with keys/values where each key is a path and is associated to a value. A key looks like just a Unix file system path, such as `myhome/kitchen/temp`. The value can be defined with different encodings (string, JSON, raw bytes buffer…).

Let’s get started!

## Pub/sub in Zenoh

First thing first, we need to install the [zenoh Python library](https://github.com/eclipse-zenoh/zenoh-python).

```
pip install eclipse-zenoh pip install eclipse-zenoh 
```

*The examples are updated to use the 1.0 version currently in rc, which is why version must be specified in the installation command. You can find more information about the 1.0 changes in the [migration guides](https://zenoh.io/docs/migration_1.0/concepts/).*

Then, let’s write an application, `z_sensor.py` that will produce temperature measurements at each second:

```
import zenoh, random, time import zenoh, random, time import zenoh, random, time   random.seed() random.seed() .   def read_temp(): def read_temp(): def read_temp return random.randint(15, 30)  return random.randint(15, 30) return. 15 30   if __name__ == "__main__": if __name__ == "__main__": if == "__main__" with zenoh.open(zenoh.Config()) as session:  with zenoh.open(zenoh.Config()) as session: with.. as key = 'myhome/kitchen/temp'  key = 'myhome/kitchen/temp' ='myhome/kitchen/temp' pub = session.declare_publisher(key)  pub = session.declare_publisher(key) =. while True:  while True: while True t = read_temp()  t = read_temp() = buf = f"{t}"  buf = f"{t}" = f "{} " print(f"Putting Data ('{key}': '{buf}')...")  print(f"Putting Data ('{key}': '{buf}')...") print f"Putting Data ('{}': '{}')..." pub.put(buf)  pub.put(buf) . time.sleep(1)  time.sleep(1) . 1
```

Now we need a subscriber, `z_subscriber.py` that can receive the measurements:

```
import zenoh, time import zenoh, time import zenoh, time   def listener(sample): def listener(sample): def listener print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')")  print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')") print f "Received {.} ('{.}': '{..}')"   if __name__ == "__main__": if __name__ == "__main__": if == "__main__" with zenoh.open(zenoh.Config()) as session:  with zenoh.open(zenoh.Config()) as session: with.. as sub = session.declare_subscriber('myhome/kitchen/temp', listener)  sub = session.declare_subscriber('myhome/kitchen/temp', listener) =.'myhome/kitchen/temp' time.sleep(60)  time.sleep(60) . 60
```

Start the subscriber:

```
python3 z_subscriber.py python3 z_subscriber.py 
```

The subscriber waits for an update on `myhome/kitchen/temp`.

Now start `z_sensor.py` as follows

```
python3 z_sensor.py python3 z_sensor.py 
```

You can see the values produced by the sensor being consumed by the subscriber.

## Store and Query in Zenoh

As the next step, let’s see how the value generated by a publisher can be stored in Zenoh. For this, we use [Zenoh router](../installation) (`zenohd`). By default, a Zenoh router starts without any storage. In order to store the temperature, we need to configure one. Create a `zenoh-myhome.json5` configuration file for Zenoh with this content:

```
{ plugins: { rest: { // activate and configure the REST plugin http_port: 8000 // with HTTP server listening on port 8000 }, storage_manager: { // activate and configure the storage_manager plugin storages: { myhome: { // configure a "myhome" storage key_expr: "myhome/**", // which subscribes and replies to query on myhome/** volume: { // and using the "memory" volume (always present by default) id: "memory" } } } } } } 
```

[Install](../installation) and start the Zenoh router with this configuration file:

```
zenohd -c zenoh-myhome.json5 zenohd -c zenoh-myhome.json5 
```

Now the data generated by our temperature sensor is stored in memory. We can retrieve the latest temperature value stored in Zenoh:

```
import zenoh import zenoh import zenoh   if __name__ == "__main__": if __name__ == "__main__": if == "__main__" with zenoh.open(zenoh.Config()) as session:  with zenoh.open(zenoh.Config()) as session: with.. as replies = session.get('myhome/kitchen/temp')  replies = session.get('myhome/kitchen/temp') =.'myhome/kitchen/temp' for reply in replies:  for reply in replies: for in try:  try: try print("Received ('{}': '{}')"  print("Received ('{}': '{}')" print"Received ('{}': '{}')" .format(reply.ok.key_expr, reply.ok.payload.to_string()))  .format(reply.ok.key_expr, reply.ok.payload.to_string())) ...... except:  except: except print("Received (ERROR: '{}')"  print("Received (ERROR: '{}')" print"Received (ERROR: '{}')" .format(reply.err.payload.to_string()))  .format(reply.err.payload.to_string())) ....
```

## Other examples

You can also have a look at the examples provided with each client API:

* **Rust**: <https://github.com/eclipse-zenoh/zenoh/tree/main/examples>
* **Python**: <https://github.com/eclipse-zenoh/zenoh-python/tree/main/examples>
* **C**: <https://github.com/eclipse-zenoh/zenoh-c/tree/main/examples>

**Next up**: [Installation](/docs/getting-started/installation/)

---

# https://zenoh.io/docs/getting-started/installation/

Source: https://zenoh.io/docs/getting-started/installation/

![](../../../img/zenoh-dragon-bg-150x163.png)

# Installation

To start playing with Zenoh we need the Zenoh router and/or the Zenoh client library.

## Installing client library

To develop your application Zenoh, you need to install a Zenoh client library.
Depending on your programming language, pick one of the following API and refer to the installation and usage instructions in here:

Note that if you wish to always have access to all of Zenoh’s latest features, Rust is Zenoh’s original language, and will therefore always be the most feature-complete version.

## Installing the Zenoh router

The Zenoh router (a.k.a. `zenohd`) and its plugins are currently available as pre-built binaries for various platforms. All release packages can be downloaded from:

`zenohd`

Each subdirectory has the name of the Rust target. See the platforms each target corresponds to on <https://doc.rust-lang.org/stable/rustc/platform-support.html>

You can also install it via a package manager on macOS (homebrew) or Linux Debian (apt). See instructions below.

For other platforms, you can use the [Docker image](../quick-test#run-zenoh-in-docker) or [build it](https://github.com/eclipse-zenoh/zenoh#how-to-build-it) directly on your platform.

### MacOS

Tap our brew package repository:

`$ brew tap eclipse-zenoh/homebrew-zenoh`

Install Zenoh:

`$ brew install zenoh`

Then you can start the Zenoh router with this command:

`$ zenohd`

### Ubuntu or any Debian

Add Eclipse Zenoh public key to apt keyring

`$ curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg`

Add Eclipse Zenoh private repository to the sources list:

`$ echo "deb [signed-by=/etc/apt/keyrings/zenoh-public-key.gpg] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list > /dev/null
$ sudo apt update`

Install Zenoh:

`$ sudo apt install zenoh`

Then you can start the Zenoh router with this command:

`$ zenohd`

### Windows

Download the Zenoh archive from <https://download.eclipse.org/zenoh/zenoh/latest/> :

`x86_64-pc-windows-msvc/zenoh-<version>-x86_64-pc-windows-msvc.zip`

Unzip the archive.

Go to Zenoh directory and start Zenoh router:

`> cd C:\path\to\zenoh\dir
> zenohd.exe`

## Testing Your Installation

To test the installation, try to see the Zenoh man page by executing the following command:

`$ zenohd --help`

You should see the following output on your console:

`2024-08-12T13:27:29.724708Z INFO main ThreadId(01) zenohd: zenohd v0.11.0-dev-965-g764be602d built with rustc 1.75.0 (82e1608df 2023-12-21)
The zenoh router
Usage: zenohd [OPTIONS]
Options:
 -c, --config <PATH>
 The configuration file. Currently, this file must be a valid JSON5 or YAML file
 -l, --listen <ENDPOINT>
 Locators on which this router will listen for incoming sessions. Repeat this option to open several listeners
 -e, --connect <ENDPOINT>
 A peer locator this router will try to connect to. Repeat this option to connect to several peers
 -i, --id <ID>
 The identifier (as an hexadecimal string, with odd number of chars - e.g.: A0B23...) that zenohd must use. If not set, a random unsigned 128bit integer will be used. WARNING: this identifier must be unique in the system and must be 16 bytes maximum (32 chars)!
 -P, --plugin <PLUGIN>
 A plugin that MUST be loaded. You can give just the name of the plugin, zenohd will search for a library named 'libzenoh_plugin_\<name\>.so' (exact name depending the OS). Or you can give such a string: "\<plugin_name\>:\<library_path\>" Repeat this option to load several plugins. If loading failed, zenohd will exit
 --plugin-search-dir <PATH>
 Directory where to search for plugins libraries to load. Repeat this option to specify several search directories
 --no-timestamp
 By default zenohd adds a HLC-generated Timestamp to each routed Data if there isn't already one. This option disables this feature
 --no-multicast-scouting
 By default zenohd replies to multicast scouting messages for being discovered by peers and clients. This option disables this feature
 --rest-http-port <SOCKET>
 Configures HTTP interface for the REST API (enabled by default on port 8000). Accepted values: - a port number - a string with format `<local_ip>:<port_number>` (to bind the HTTP server to a specific interface) - `none` to disable the REST API
 --cfg <CFG>
 Allows arbitrary configuration changes as column-separated KEY:VALUE pairs, where: - KEY must be a valid config path. - VALUE must be a valid JSON5 string that can be deserialized to the expected type for the KEY field.
 Examples: - `--cfg='startup/subscribe:["demo/**"]'` - `--cfg='plugins/storage_manager/storages/demo:{key_expr:"demo/example/**",volume:"memory"}'`
 --adminspace-permissions <[r|w|rw|none]>
 Configure the read and/or write permissions on the admin space. Default is read only
 -h, --help
 Print help (see a summary with '-h')
 -V, --version
 Print version`

##### Eclipse Incubation

![](../../../img/eclipse-incubation.png)

![](../../../img/eclipse-incubation.png)

Eclipse zenoh ™ is an incubating project under the Eclipse Foundation.

##### More Information

[Legal](https://www.eclipse.org/legal)

[Privacy policy](https://www.eclipse.org/legal/privacy.php)

[Terms of use](https://www.eclipse.org/legal/termsofuse.php)

[Copyright](https://www.eclipse.org/legal/copyright.php)

[Report a security issue](https://www.eclipse.org/security/)

[Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/)

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

[Eclipse Foundation](https://www.eclipse.org/)

##### Sponsored by:

[![](../../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../../img/eclipse-foundation.svg)

[![](../../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../../docs/overview/what-is-zenoh)

![](../../../img/zenoh-dragon-150x163.png)

![](../../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/docs/getting-started/deployment/

Source: https://zenoh.io/docs/getting-started/deployment/

* [Home](../../../)
* [Documentation](../../../docs/getting-started/first-app/)
* [Use Cases](../../../usecases/)
* [Community](../../../community/)
* [Adopters](../../../adopters/)
* [Media](../../../media/)
* [Blog](../../../blog/2025-12-11-zenoh-jiaolong/)

# Deployment

[Edit on GitHub](https://github.com/atolab/zenoh-web/tree/master/content/docs/getting-started/deployment.md)

## Overview

## Peer to peer

By default Zenoh applications are configured to communicate peer to peer (`peer` mode). All applications in the local network directly communicate with each other.

**Configuration**

```
{ mode: "peer", } 
```

### Scouting

Zenoh applications in `peer` mode run both `multicast` and `gossip` scouting to discover other applications or Zenoh routers and connect them.

**Multicast scouting**

Zenoh applications in `peer` mode join multicast group `224.0.0.224` on UDP port `7446` and send scout messages on this address to discover local applications and routers. They automatically connect to all accessible `peer` mode applications and routers they discover. The scouting address and behavior can be configured.

**Configuration**

```
{ mode: "peer", scouting: { multicast: { enabled: true, address: "224.0.0.224:7446", interface: "auto", autoconnect: { router: [], peer: ["router", "peer"] }, listen: true, }, }, } 
```

**Gossip scouting**

Zenoh applications in `peer` mode forward all local applications and routers that they already discovered to newly scouted applications. This is useful when multicast communications are not available. But applications need to connect first to an entry point to discover the rest of the system. This entry point is typically one or several Zenoh routers but can also be one or several other peers. Those entry points are configured through the `connect` section of the configuration.

**Configuration**

```
{ mode: "peer", connect: { endpoints: ["tcp/192.168.1.1:7447", "tcp/192.168.1.2:7447"], }, scouting: { gossip: { enabled: true, multihop: false, autoconnect: { router: [], peer: ["router", "peer"] }, }, }, } 
```

## Client

Communicating peer to peer implies establishing multiple sessions with multiple other peers and maintaining a state for those sessions. Maintaining such states can be undesirable for scalability reasons or because the application runs on a constrained device. In this case the Zenoh application can be configured to operate in client mode. In this mode, the application will maintain, at any given time, a single session with another process (typically a Zenoh router) that will grant it connectivity with the rest of the system.

**Configuration**

```
{ mode: "client", } 
```

### Scouting

Zenoh applications in `client` mode run `multicast` scouting to discover Zenoh routers and connect to them. In addition, the endpoints of one or several routers can be configured in the `connect` section.

**Configuration**

```
{ mode: "client", connect: { endpoints: ["tcp/192.168.1.1:7447", "tcp/192.168.1.2:7447"], }, } 
```

## Peers mesh

In a mesh network, applications cannot directly connect to each other. Peer to peer and brokered communications may be impossible or undesirable. Zenoh applications in `peer` mode can run a linkstate protocol that allow them to communicate in a mesh network.

**Configuration**

```
{ mode: "peer", routing: { peer: { mode: "linkstate", }, }, } 
```

Note: if a Zenoh router is used to connect a local mesh of Zenoh peers to a wider network, this router also needs to be configured with the same `routing` section.

## Zenoh router

Zenoh routers route data between clients and local subnetworks of peers. They can be deployed using any topology. They, by default, never try to interconnect themself automatically and must be configured with the endpoints of the other routers they are supposed to connect to.

```
{ connect: { endpoints: ["tcp/192.168.1.1:7447", "tcp/192.168.1.2:7447"], }, } 
```

**Next up**: [For a quick test using Docker](/docs/getting-started/quick-test/)

---

