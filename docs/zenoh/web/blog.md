# Zenoh Blog Posts

# https://zenoh.io/blog/2020-06-29-zenoh-tidings/

Source: https://zenoh.io/blog/2020-06-29-zenoh-tidings/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh Tidings

Blog Posts

# Zenoh Tidings

30 June 2020 -- Paris.

In our last blog we had announced a rewrite of [**zenoh**](http://zenoh.io) in [Rust](http://rust-lang.org). The wrote the first version of zenoh in [OCaml](http://ocaml.org), a super-neat ML-derived functional programming language. [OCaml](http://ocaml.org) allowed us to experiment very quickly and have good performances. Yet, one of the major feedback we were receiving from the community was that few people knew this programming language and this was limiting contributions. Beside, we had the desire to make zenoh even faster and smaller. One obvious choice would have been to write the new version in C/C++, yet something we did not want to loose were the safety properties we enjoyed with [OCaml](http://ocaml.org). Additionally, if we had to leave our beloved [OCaml](http://ocaml.org), we did not want to completely give away high level abstractions. We also wanted to avoid languages that had a heavy runtime and a garbage collector. We had already looked at [Rust](http://rust-lang.org) back in 2015, but at the point we did not feel it was the right choice for us. The improvements introduced in the programming language with the 2018 edition along with the introduction at a language level **async** make [Rust](http://rust-lang.org) a perfect choice for zenoh.

## Zenoh: A New Era

As we were going for a rewrite, we took this opportunity to leverage the experience, user feedback and lesson learned from the first version of zenoh. We did some improvements at the protocol level as well as some reorganisation. The resulting stack is represented in the diagram below.

![zenoh-stack](../../img/zenoh-stack.png)

![zenoh-stack](../../img/zenoh-stack.png)

As you can see from this diagram, now zenoh is organised as two layers.

### zenoh-net

Implements a networking layer capable of running above a Data Link, Network or Transport Layer. **zenoh-net** provides primitives for efficient pub/sub and distributed queries. It supports fragmentation and ordered reliable delivery and provides a pluggable scouting abstraction for discovery. **zenoh-net** defines and builds upon a session protocol that provides abstractions for ordered best effort and reliable channels with unlimited MTU that are independent of the underlying layer.

**zenoh-net** supports peer-to-peer and routed communication as well as push and pull pub/sub along.

### zenoh

The **zenoh** layer provides a high level API for pub/sub and distributed queries. It deals with data representation encoding and transcoding and provides an implementation of geo-distributed storage and distributed computed values. **zenoh** natively supports a series of data encoding, such as JSON, Properties, Relational, Raw, etc., along with transcoding across supported formats. It also defines a canonical query syntax based on URIs syntax.
The **zenoh** layer also provides a storage back-end plug-in API to ease the integration of third parties storage technologies. Currently supported storage back-ends are Memory, MySQL, MariaDB, PostgreSQL, SQLite and InfluxDB
By default the Geo-Distributed Storages work under eventual consistency. Stronger consistency can be implemented by user leveraging Quorum Mechanism

## Improvements and New Features

The upcoming version of **zenoh** comes with a few improvements and some new features. Specifically, you will see:

**Major performance improvements**. These performance improvements are a consequence of both using Rust and of some changes on packet scheduling.

**Protocols improvements**. We have reorganised the protocol to make it even simpler to port **zenoh** to different kinds of networks while exploiting network specific features. We have also added the ability to carry user provided attachments with both data and queries. These attachments can be used by zenoh applications to either extend the protocol, or for instance add user level security.

**Generalised Peer-to-Peer and Client Communication**. In the upcoming version of **zenoh** an application can decide at runtime to behave like a peer or a client. Peers route information between themselves and can also route on behalf of clients – in other terms peers can behave like routers. Peers-to-peer communication is supported for arbitrary connectivity graphs and supports cliques as a special case.

**Closure-based Discovery**. Discovery in **zenoh** is supported by the **scouting** protocol, in order to ease the deployment of system that wants to leverage a clique connectivity, for cases in which multicast is not avaiable, or desirable, we support now a clousure-based discovery. In other terms starting from a single peer, we can discover its closure, or in other terms the peers that can be reached directly or indirectly from this starting point.

**Region-Based Routing**
The new version of **zenoh** supports region-based routing. As depicted in the diagram below, this really means two things, (1) routing information required to build and maintain our routing tables scales with the size of the region, and (2) each region can decide wether to route over an arbitrary connectivity graph of assume a clique. This approach to routing will greatly improve scalability and performance by allowing to use the most appropriate routing technique within a region.
![zenoh-routing](../../img/routing.png)

![zenoh-routing](../../img/routing.png)

## Performances

The Zenoh distribution includes simple tests to check the performance. To build and run these tests just follow the instruction below:

`$ git clone git@github.com:eclipse-zenoh/zenoh.git
$ cd zenoh
$ git checkout rust-master
$ cargo build --release
$ cargo build --release --examples
# then run the throughput benchmark
# run the subscriber
$ ./target/release/examples/zn_sub_thr
# run the publisher with <payload size> (1024 below) and locator
# the locator will become optional once the rust version will also support zenoh scouting
$ ./target/release/examples/zn_pub_thr 1024`

When running these tests on a Linux Laptop with an Intel Core i7 we get the results displayed below. As you can read from the graph the 1Gbps mark is reached already for messages with a payload of just 128 bytes.

![msg-sec](../../img/perf/2020.05.24-mgs-sec.png)

![msg-sec](../../img/perf/2020.05.24-mgs-sec.png)

![mps](../../img/perf/2020.05.24-mbps.png)

![mps](../../img/perf/2020.05.24-mbps.png)

## Schedule

We have made good progress toward making the [Rust](http://rust-lang) of **zenoh** available. You can already start experimenting with the [rust-master branch](https://github.com/eclipse-zenoh/zenoh/tree/rust-master), but the good news is that by the end of July we should have the bulk of features in place.
You can check-out the [roadmap](https://github.com/eclipse-zenoh/zenoh/wiki/Roadmap) to see our progress as well as comment on which features you’d like to see next.

Finally, do not hesitate to reach us out on the [Zenoh Discord Server](https://discord.gg/cY4nVjUd)

[**A+**](https://github.com/kydos/)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2020-10-08-aithusa/

Source: https://zenoh.io/blog/2020-10-08-aithusa/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh Aithusa Hatched Out!

Blog Posts

# Zenoh Aithusa Hatched Out!

8 October 2020 -- Paris.

We have been waiting this very moment for several months. Months of patient
dedication, months of hard and creative work. Months in which each and every
member of the **zenoh** team has made his and her best to give our little dragon all
it needed to succed in the complicated world of Internet Scale Protocols.

Today, at about 11.00 Paris Time **Zenoh Aithusa** Hatched Out!

Aithusa is the code-name for the first release of our Rust-based zenoh infrastructure,
A supercharged of new features and improvements, including better performance,
improved network scheduling, ROS2 integration, and DDS Plugin.

Let’s find out together what are the main news and what’s next.

## Protocol Updates

Zenoh Aithusa has several changes at the protocol level, most notably,
we have reorganised the messages to neatly separate the transport session
abstraction and the messages that are used by the protocol implementing
zenoh’s primitives.

This protocol-level reorganisation has the advantage of clearly decoupling
the portion of zenoh-net that deals with the underlying network and the portion
of the protocol that buils upon the zenoh-channel abstraction. This reorganisation
makes it eaier to port zenoh to disparate networks and also giges a better
architecture for traffic scheduling.

Additional changes include the consolidation of data messages, now reduced to a
single one, along with the addition of a generic message attachment decorator.
The attachment decorator can be used by the application layer to attach arbitrary
data to zenoh messages.

Finally, we have extended the representation of resources keys on the wire to allow
us to represent effectively prefixes. In other terms, the previous version of zenoh
could represent on the wire either a numerical resource identifier or a full
resource key (meaning the string, such as “/org/eclipse/zenoh/demo/hello”).
Now the protocol is able to represent resource keys made by resource identifier
representing the prefix and a suffix. Thus we could represent the previous resource
key as (42, “demo/hello).

This makes it possible for our runtime to play more optimisation tricks when
deciding when, how and which portion of a key to map to a small integer.
What has not changed is that these integer are invisible to you and completely
managed by our runtime. You can just relax and enjoy their benefits in terms
of reducing the wire-overhead.

## Peers, Clients and Routers

Zenoh Aithusa supports peer-to-peer communication, as well as routed communication.
Additionally, clients can leverage peers and routing nodes to communicate between
each others. Likewise, group peers across separate networks can leverage routers
to communicate with each other.

The routing protocol has also been updated to improve path selection
while still maintaining the routing state under control.

## Performance

Zenoh Aithusa gives major performance improvement when compared with the last release
– the OCaml version of zenoh.

As rust async-std-1.6.4 has introduced some performance regression, while we work
with the async team try go back to the level of performances of async-std-1.6.2,
you should try performance with 1.6.2. The SED command below does precisely that.

`$ git clone git@github.com:eclipse-zenoh/zenoh.git
$ cd zenoh
$ find . -name "*.toml" -exec sed -i s/=1.6.4/=1.6.2/ {} \;
$ export RUSTFLAGS="-C target-cpu=native"
$ cargo build --release
$ cargo build --release --examples
# then run the throughput benchmark
# run the subscriber asking to collect 30 measurement, each measurement uses 100K messages.
$ ./target/release/examples/zn_sub_thr -s 30
# run the publisher with <payload size> (1024 below). The subscriber is discovered via UDP multicast.
$ ./target/release/examples/zn_pub_thr 1024`

When running these tests on a testbed made by Linux Workstations with an AMD Ryzen 7 3800X and 10GbE network. As you can read from the graph the 1Gbps mark is reached for messages of 128 bytes and the 10Gbps mark is reached for messages with a payload of just 1024 bytes.

![msg-sec](../../img/perf/2020.10.08-mgs-sec.png)

![msg-sec](../../img/perf/2020.10.08-mgs-sec.png)

![mps](../../img/perf/2020.10.08-mbps.png)

![mps](../../img/perf/2020.10.08-mbps.png)

## DDS Plugin and ROS2 Integration

Another goody coming with Zenoh Aithusa is the [DDS plugin](https://github.com/eclipse-zenoh/zenoh-plugin-dds). This allows to route transparently data from [Cyclone DDS](http://github.com/eclipse-cyclonedds/cyclonedds), any other DDS implementation, and ROS2. As a consequence ROS2 based robot can be teamed, monitored and managed from anywhere across the Internet!

## What’s Next

In the weeks to come we will be releasing:

**Zenoh-pico**. A C-based [client stack for zenoh](https://github.com/eclipse-zenoh/zenoh/wiki/Zenoh--For-Microcontrollers) targeting the most constrained environemnts.

**Language Bindings**. More bindings are coming up including Go-Lang and Java APIs.

**Storages Backends**. Supporting addintional storage backends for time-series and
relational DBs.

**Micro-ROS RMW**. Adding support for zenoh in MicroROS2.

Finally, do not hesitate to reach us out on the [Zenoh Discord Server](https://discord.gg/cY4nVjUd)

[**A+**](https://github.com/kydos/)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2021-03-23-discovery/

Source: https://zenoh.io/blog/2021-03-23-discovery/

![](../../img/zenoh-dragon-bg-150x163.png)

# Minimizing Discovery Overhead in ROS2

Blog Posts

# Minimizing Discovery Overhead in ROS2

23 March 2021 -- Paris.

The amount of discovery traffic generated by ROS2 is a problem that has
received an increasing attention in the community. The discovery overhead
issue becomes extremely severe when running over wireless technologies,
such as WiFi, and in particular in combination with more complex robots, robot
swarms and tele-operation. The [ROS2 Discovery Service](https://docs.ros.org/en/foxy/Tutorials/Discovery-Server/Discovery-Server.html) has been proposed
as a way to alleviate the problem, not necessarily to solve it.

In the reminder of this post I’ll explain the essence of problem,
remind what was tried in the past and unveils a [**Zenoh**](https://github.com/eclipse-zenoh/zenoh) based solution that
(1) drastically reduces DDS discovery overhead – from 97% to 99,9% in tested scenarios,
(2) allows for peer-to-peer communication when useful,
(3) enables efficient Internet-scale routing when necessary, and
(3) does not require any changes to your existing ROS2 systems.

Ready, let’s go!

# Understanding the Problem

As many of you should know, ROS2 uses the [Data Distribution Service (DDS)](https://www.omg.org/omg-dds-portal/) as the mean to communicate and share data
across ROS2 nodes. Thus, when people discuss about ROS2 discovery,
they really mean DDS discovery – in any case, this is what is used
under-the-hood.

The problem of DDS discovery has been known for quite some time. The oldest
trace I can find of a public reference to the issue goes back to this
[presentation](https://www.slideshare.net/Angelo.Corsaro/scaling-the-data-distribution-service-to-global-networks) I gave back in 2009.
As a team we did work hard to address this problem and already in 2012 we
had products, such as [Vortex Cloud](https://www.slideshare.net/Angelo.Corsaro/building-and-scaling-internet-of-things-applications-with-vortex-cloud-37188676) (now Vortex Link), used by our customers to either scale DDS over a wired WAN or to reduce discovery traffic. One notable user of Vortex Cloud was
[NASA SMART NAS](https://www.adlinktech.com/en/News_18100302503788216.aspx). Thus I can humbly claim that, in a way, we’ve been there and we’ve done that long time back. The experience gathered during those years, was one of the main drivers for coming up with [**Zenoh**](https://github.com/eclipse-zenoh/zenoh). But before we get there, let me try to explain what the DDS discovery problem is and why it is inevitably entangled with the very nature of DDS.

## DDS Discovery Fundamentals

DDS has two discovery protocols, one called the SPDP (Simple Participant Discovery Protocol) and one called SEDP (Simple Entity Discovery Protocol).
The SPDP essentially takes care of finding out who is around, in DDS jargon
it finds domain participants. Once discovered a new domain participant the
SEPD kicks-in to mutually exchange the full list of data-readers, data-writers and optionally topics. As a consequence the amount of discovery data generated by real-world applications grows quadratically in the number of nodes. More precisely, assuming we have a system with **n** domain participants each of which has
**r** readers and **w** writers, then the amount of discovery traffic scales with **n\*(n-1)\*(r+w)**.

Additionally to the generated traffic, the DDS discovery model forces every domain participant to retain all discovery information. In other terms, every participant
has to keep track of every single reader and writer available on any other participant within the same domain – all of this in spite of whether
that is of interest or not.

As we did in [Vortex Cloud](https://www.slideshare.net/Angelo.Corsaro/building-and-scaling-internet-of-things-applications-with-vortex-cloud-37188676) some of this can be alleviated, yet the bulk of the problem is tied to design decisions that are at the very heart of DDS. Its end-points matching and reliability model is probably the main one, not to mention that DDS was designed with wired network in mind, networks in which bandwidth is plentiful and packet losses are relatively rare.

These are the reasons for the known challenges on WiFi and the hard truth about how far can we get with DDS because
of its inherent model and assumptions.

As I mentioned above, our efforts trying to scale DDS made it evident that Discovery was one of the elephants in the room,
but not the only one. This led us to look at things differently, it led us into designing [**Zenoh**](https://github.com/eclipse-zenoh/zenoh).

## Zenoh

When designing [**Zenoh**](https://github.com/eclipse-zenoh/zenoh), discovery overhead was one of the issues we wanted to
tackle along with the ability to support Internet-scale applications, constrained devices and networks.

Another problem we wanted to solve, that is interesting per-se but not relevant for this blog, was the unification of data
in motion an data at rest. This makes it much easier to support robot swarms, tele-operation and in general any kind of
applications in where you have to deal with data in motion as well geographically dispersed data at rest.
Will provide some coverage on later instalment of this blog series, for now let’s get back to the protocol aspects.

Zenoh manages to drastically lower discovery traffic because (1) it only advertises resource interests, in other terms
does not need to advertise publishers, (2) resource interests can be generalized to “compress” discovery data,
(3) discovery messages are extremely wire efficient, and (4) the reliability protocol is between run-times as opposed
to every couple of reader and writers as in DDS.

In this blog we will see how the design decisions summarized above significantly impact discovery traffic and more importantly how
you can leverage **zenoh** along with your favorite DDS – which I hope is
[**Eclipse Cyclone DDS**](http://github.com/eclipse-cyclonedds/cyclonedds) – in order to massively reduce the discovery traffic,
and take advantage of the many super-cool features zenoh has to provide, including Internet-scale routing, geo-distributed storages, distributed queries, etc.

## Real World Use Case

Instead of crafting a synthetic benchmark, we decided to run a real-world **ROS2** application and measure the
discovery overhead induced by **DDS** and **zenoh** in the context of this application. As shown below, we run
[RVIZ2](https://www.stereolabs.com/docs/ros2/rviz2/) in combination with the [turtlebot burger](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#overview)
[SLAM](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/) application and measured the discovery traffic generated
by each of the two technologies.

![msg-sec](../../img/2021.03.18-disco-scenario.png)

![msg-sec](../../img/2021.03.18-disco-scenario.png)

The [turtlebot burger](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#overview) was running
[ROS2 Foxy](https://docs.ros.org/en/foxy/Installation.html) and was connected to a WiFi network powered by a
[NetGear NightHawk](https://www.netgear.com/home/wifi/routers/r6020/) router. [RVIZ2](https://www.stereolabs.com/docs/ros2/rviz2/) for [ROS2 Foxy](https://docs.ros.org/en/foxy/Installation.html) was running on a [System76 Galago](https://system76.com/laptops/galago) Linux laptop.

## DDS Scenario

To measure the discovery traffic, we started the SLAM application on the turtlebot and awaited for it to be ready. Only then, we started, simultaneously, Wireshark and RVIZ2 on the laptop and captured DDS packets until RVIZ2 was showing the map created by the robot – the setup is depicted in the diagram below.

![msg-sec](../../img/2021.03.18-dds-scenario.png)

![msg-sec](../../img/2021.03.18-dds-scenario.png)

The command used on the turtlebot was:

`$ ros2 launch turtlebot3_bringup robot.launch.py`

The command used on the laptop to start RVIZ2 was:

`$ ros2 launch turtlebot3_cartographer cartographer.launch.py`

## Zenoh Scenario

The first question you may have, is how can you use zenoh to transparently bridge ROS2/DDS communication?
The [Eclipse Zenoh Project](https://github.com/eclipse-zenoh) makes available the [zenoh-plugin-dds](https://github.com/eclipse-zenoh/zenoh-plugin-dds) to transparently bridge DDS communication over zenoh and vice-versa. You can use this service to route DDS traffic over zenoh, for instance to tele-operate a robot over the internet, or to interact with a DDS or a ROS2 application through the zenoh ecosystem – will show how to do that on our next blog.

To measure the discovery overhead introduced by zenoh, we configured ROS on the robot and the laptop to use
different domains – to ensure that they could not discover each other via DDS – then we deployed an instance of [zenoh-plugin-dds](https://github.com/eclipse-zenoh/zenoh-plugin-dds) respectively on the robot and on the laptop. As a consequence all data flowing through the network was going over zenoh. Locally, to the robot and to the laptop, we had the [zenoh-plugin-dds](https://github.com/eclipse-zenoh/zenoh-plugin-dds) bridging from DDS to zenoh and zenoh to DDS.

To ensure that the scenario was as close as possible to that using DDS, we configured the [zenoh-plugin-dds](https://github.com/eclipse-zenoh/zenoh-plugin-dds) to operate as a peer. Thus from a functional perspective it is important to understand the peer-to-peer communication model supported by ROS2 was maintained without any functional degradation. It is also important to say that the RVIZ2 application was running without no limitations or degradations.

The scenario used to measure zenoh discovery overhead is depicted below.

![msg-sec](../../img/2021.03.18-zenoh-scenario.png)

![msg-sec](../../img/2021.03.18-zenoh-scenario.png)

The application we ran on the robot were:

 `$ cargo run --release -- dzd -m peer -d 21
$ ROS_DOMAIN_ID=21 ros2 launch turtlebot3_bringup robot.launch.py`

and on the laptop:

 `$ cargo run --release -- dzd -m peer -d 42
$ ROS_DOMAIN_ID=42 ros2 launch turtlebot3_cartographer cartographer.launch.py`

### Zenoh’s Discovery and Resource Generalisation

As de briefly mentioned earlier in this post, zenoh has a very different approach to discovery when compared to DDS. In a way we could say that
DDS is very detail oriented to the level of becoming pedantic. What do I mean with this?
DDS exchanges the tiny nitty gritty details of every single writers and readers available for a given topic (an optionally the topic info too), and by the way it exchanges it even if I do not care about the majority of it.

Zenoh operates very differently. This was a conscious choice, because when designing zenoh we wanted to
make sure that we could predict the resource used by an application in spite of the number of *“matching”* reader/writers.
In other terms, having a writer matching one or one million readers makes a huge difference in DDS in terms of discovery traffic generated, reliability protocol overhead, and discovery data to keep in memory. When designing **zenoh** we did not want to have this undesirable side-effect.

This lead toward a design geared toward sharing only resource interests as opposed to sharing interest as well as those who are interested, *i.e.*, readers and writers. This is a big difference and one of the areas where zenoh has much better scalability. The other trick we play in zenoh is that, our protocol may decide
to make generalizations – to make a parallel with what I was mentioning above, it raises the level of abstraction and tries to detach itself from the details. What do I mean with that? This is best explained with an example, suppose that your robot publishes data for `/mybot/sensor/lidar`,
`/mybot/sensor/camera`, `/mybot/dynamics/odometry`, etc. Zenoh, when looking at these resources may decide that the only thing the rest of the world needs to know is that they have to come to this robot when looking for anything that matches`/mybot/**`. This is in simple terms what we mean by resource generalization. This is an important mechanism to compress discovery information and to ensure that the discovery information can withstand Internet scale applications. As a result, in zenoh all routing and matching is performed using set-theoretic operations and set-coverage – for instance to figure out the minimal set of storages that can answer a query.
The zenoh protocol performs resource generalization automatically whenever it makes sense but it also exposes an API for the user to give hints.

`/mybot/sensor/lidar`
`/mybot/sensor/camera`
`/mybot/dynamics/odometry`
`/mybot/**`

### Leveraging Resource Generalisation

To demonstrate the effectiveness of zenoh’s resource generalization we ran an additional scenario whereby using an option
of our [zenoh-plugin-dds](https://github.com/eclipse-zenoh/zenoh-plugin-dds) we made the resource space for the robot
rooted by simply prefixing it with `/bot`. Then we also gave hint to aggressively generalize resources matching this
prefix.

`/bot`

Thus to measure zenoh’s discovery overhead when leveraging resource generalization, we ran the same scenario as above, with the following arguments:

`# On the Turtlebot
$ cargo run --release -- dzd -m peer -d 21 -s /bot -r /bot/** -w /bot/**
$ ROS_DOMAIN_ID=21 ros2 launch turtlebot3_bringup robot.launch.py
# On the Laptop
$ cargo run --release -- dzd -m peer -d 21 -s /bot -r /bot/** -w /bot/**
$ ROS_DOMAIN_ID=42 ros2 launch turtlebot3_cartographer cartographer.launch.py`

For your reference these are the options supported by our **dzd** bridge:

 `$ dzd --help
 dzd zenoh router for DDS
 USAGE:
 dzd [OPTIONS]
 FLAGS:
 -h, --help Prints help information
 -V, --version Prints version information
 OPTIONS:
 -a, --allow <String> The regular expression describing set of /partition/topic-name that should be
 bridged, everything is forwarded by default.'
 -c, --config <FILE> A configuration file.'
 -d, --domain <ID> The DDS Domain ID (if using with ROS this should be the same as ROS_DOMAIN_ID).'
 -w, --generalise-pub <String>... A comma separated list of key expression to use for generalising pubblications.'
 -r, --generalise-sub <String>... A comma separated list of key expression to use for generalising subscriptions.'
 -l, --listener <LOCATOR>... Locators to listen on.'
 -m, --mode <MODE> The zenoh session mode.' [default: client] [possible values: peer, client]
 -e, --peer <LOCATOR>... Peer locator used to initiate the zenoh session.'
 -s, --scope <String>... A string used as prefix to scope DDS traffic.'`

### Cold and Warm Start

Another aspect that we need to consider when using zenoh in this configuration is whether we measure the discovery traffic assuming that nothing is running on the laptop, in other terms we start `dzd` after we start capturing zenoh packets, or else we assume that the zenoh infrastructure is already up and running and we only start `RVIZ2`. We call **cold start** the case in which nothing is running on the laptop before we start measuring zenoh discovery data and **warm start** the case in which `dzd` is already running. On a real-world scenario you would have dzd running, but we prefer to measure the two cases to show the worst case scenario.

`dzd`
`RVIZ2`
`dzd`

## Measuring Discovery Data

### DDS

To evaluate the traffic generated by DDS discovery data we take into account the SPDP (Single Participant Discovery Protocol) and SEDP (Simple Entity Discovery Protocol) generated from the start of RVIZ2 to the last SEDP – which is the last reader or writer declaration. After the last SEPD message nothing else is taken into account. We think this is a fair measure since it represents the amount of discovery data necessary to establish proper communication between the two DDS applications.

### Zenoh

To evaluate the traffic generated by zenoh we measure the overhead coming from the session opening and the link-state algorithm along with all the packets containing resource declarations. You may wonder why zenoh peers run a link-state algorithm, well they do it to be able to support communication on [arbitrary mesh topologies](http://zenoh.io/docs/getting-started/key-concepts/), we’ll share more details on some later blog post.

## Experimental Results

The experiments described above were run five times each and for each run we measured discovery data. While for zenoh the measured data was stable across experiment, on DDS we saw a fluctuation of roughly 50Kbytes. To make the comparison even more compelling, we decided to take the best measure for DDS. Once again for zenoh we did not see variability across experiments.

The table below shows, for DDS, zenoh and for each of the scenarios described above, the number of discovery packets, their average size in bytes and more importantly the total number of bytes exchanged. The last column shows the percentage of discovery traffic reduction measured for zenoh.

|  | Packets | Avg Size (Bytes) | Total Bytes | Zenoh Discovery Reduction % |
| --- | --- | --- | --- | --- |
| DDS | 686 | 366.73 | 251576 |  |
| Zenoh | 31 | 213.45 | 6617 | 97.37% |
| Zenoh RG | 13 | 136,54 | 1775 | 99.29% |
| Zenoh WS | 17 | 276,41 | 4699 | 98.13% |
| Zenoh RGWS | 1 | 82 | 82 | 99.97% |

Where:

By looking at the table it is clear how much zenoh can drastically reduce the discovery overhead. In the measured scenarios,
zenoh is already able to reduce discovery by **97.37%** in the worst case. It gets to **99.29%** reduction in discovery traffic as soon as
we add some structure to the turtlebot ROS2 topics by prefixing them with `/bot` and gets to the incredible **99.97%** reduction in discovery traffic when combining resource generalization with warm start.

`/bot`

We think these results are extremely encouraging and in a way explain why those who have moved to zenoh for Robot to Everything (R2X) communication have
experienced huge improvements over wireless networks and in particular WiFi. The other good news is that to leverage zenoh you do not have to change anything to your application.
Just drop-in the [zenoh-plugin-dds](https://github.com/eclipse-zenoh/zenoh-plugin-dds) and have fun!

But there is even more that you can do, such as writing native zenoh applications and have them seamlessly interact with ROS2. We’ll cover these and other cool matters in upcoming posts.

Good Hacking!

[**A+**](https://github.com/kydos/)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2021-04-28-ros2-integration/

Source: https://zenoh.io/blog/2021-04-28-ros2-integration/

* [Home](../../)
* [Documentation](../../docs/getting-started/first-app/)
* [Use Cases](../../usecases/)
* [Community](../../community/)
* [Adopters](../../adopters/)
* [Media](../../media/)
* [Blog](../../blog/2025-12-11-zenoh-jiaolong/)

# Integrating ROS2 with Eclipse zenoh

# Integrating ROS2 with Eclipse zenoh

28 April 2021 -- Paris.

In our [previous blog](./2021-03-23-discovery/) we demonstrated how the [zenoh bridge for DDS](https://github.com/eclipse-zenoh/zenoh-plugin-dds) allows to (1) bridge DDS communications through zenoh, and (2) reduce by up to 99.97% the discovery traffic between the nodes.

The previous blog was focusing on demonstrating the advantages of using zenoh as the mean for ROS2-to-ROS2 communication over wireless technologies. In this blog, we’ll go one step further and will demonstrate how you can easily write native zenoh applications —meaning that has no dependencies on ROS2 — and seamlessly interact with [ROS2](https://docs.ros.org/en/foxy/index.html) applications. Finally, we will show how you can extend your communication to Internet scale, allowing to cover all the typical cases for Robot-to-anything (R2X) communication.

---

## What does the zenoh/DDS bridge do ?

The zenoh/DDS bridge is leveraging [CycloneDDS](https://github.com/eclipse-cyclonedds/cyclonedds) to discover the DDS readers and writers declared by the ROS2 application. For each discovered DDS entity the bridge creates a mirror DDS-entity — in other terms it creates a reader when discovering a writer and vice-versa. Additionally, the bridge maps the DDS topics read and written by the discovered DDS entities on zenoh resources and performs the proper declarations.

As example, let’s consider the [turtlesim](http://docs.ros.org/en/foxy/Tutorials/Turtlesim/Introducing-Turtlesim.html) package used in the ROS2 Tutorial:

* By default the turtlesim node has a ROS2 Publisher on topic `/rosout`. As per [ROS2 conventions](https://design.ros2.org/articles/topic_and_service_names.html#ros-specific-namespace-prefix) this maps to a DDS Writer on topic `rt/rosout`. Consequently, the zenoh/DDS bridge declares a DDS Reader on the same topic with matching QoS. This DDS Reader will receive all publications from the turtlesim on this topic and re-publish those on a zenoh resource having `/rt/rosout` as a key.
* The turtlesim also has a ROS2 Subscriber on topic `/turtle1/cmd_vel` that maps as a DDS Reader on `rt/turtle1/cmd_vel`. The zenoh/DDS bridge declares a DDS Writer on the same topic, and a zenoh subscriber for the key `/rt/turtle1/cmd_vel`. This zenoh subscriber will receive all publications with this key from any zenoh application and re-publish those to DDS on topic `rt/turtle1/cmd_vel` to be received by the ROS2 subscriber on `/turtle1/cmd_vel`.

---

## How to encode/decode ROS2 messages ?

You may have noticed that the zenoh/DDS bridge doesn’t need to be compiled with any ROS2 message definition. That is because the bridge doesn’t need to interpret the ROS2 messages. It just forwards the data payload as is. As a consequence a zenoh application that needs to publish/subscribe to ROS2 will need to encode/decode those messages.

For those who are curious about the details, the ROS2 messages are encoded for DDS following the OMG DDSI-RTPS specification (see §10) in [CDR format (see §9.3)](https://www.omg.org/spec/CORBA/3.4/Interoperability/PDF). But fortunately, you usually don’t need to implement a CDR encoder/decoder, since there are libraries for this in most languages ([Python](https://pypi.org/project/pycdr/), [Rust](https://crates.io/crates/cdr), [C#](https://www.nuget.org/packages/CSCDR), [Javascript](https://www.npmjs.com/package/jscdr)…)

---

## Show me some code

OK, let’s do a zenoh “teleop” app in Python for a start. It will publish Twist messages to the turtlesim’s `/turtle1/cmd_vel` Subscriber and subscribe to Log messages published by the turtlesim’s `/rosout` Publisher.

All that you need is:

* A host with ROS2 environment and:
  + the [turtlesim](http://docs.ros.org/en/foxy/Tutorials/Turtlesim/Introducing-Turtlesim.html) package
  + the [zenoh/DDS bridge](https://github.com/eclipse-zenoh/zenoh-plugin-dds/#trying-it-out)
* Another host in the same LAN with (or you can use the same host, but that’s less fun…):
  + the [zenoh Python API](https://github.com/eclipse-zenoh/zenoh-python#how-to-install-it) and pycdr installed -  
    just do: `pip install eclipse-zenoh pycdr`

***Note**: currently you need to build the zenoh/DDS bridge yourself. But we will provide pre-built binaries for main platforms soon. Once built, the `zenoh-bridge-dds` executable is generated in the `zenoh-plugin-dds/target/release` subdirectory.*

Now:

1. **Start the turtlesim** on host 1:

   ```
   ros2 run turtlesim turtlesim_node ros2 run turtlesim turtlesim_node 
   ```
2. **Start the zenoh/DDS bridge** on host 1:

   ```
   RUST_LOG=info zenoh-bridge-dds -m peer RUST_LOG=info zenoh-bridge-dds -m peer RUST_LOG =
   ```

   The `RUST_LOG=info` environment variable is to activate the logs at “info” level. You should see such logs proving that the bridge discovered the turtlesim’s Publishers and Subscribers:

   ```
   [2021-04-13T13:11:58Z INFO zenoh_bridge_dds] New route: [2021-04-13T13:11:58Z INFO zenoh_bridge_dds] New route: [] DDS 'rt/rosout' => zenoh '/rt/rosout' (rid=19) with type'rcl_interfaces::msg::dds_::Log_'  DDS 'rt/rosout' => zenoh '/rt/rosout' (rid=19) with type'rcl_interfaces::msg::dds_::Log_' 'rt/rosout' ='/rt/rosout'(rid =)'rcl_interfaces::msg::dds_::Log_'[2021-04-13T13:11:58Z INFO zenoh_bridge_dds] New route: [2021-04-13T13:11:58Z INFO zenoh_bridge_dds] New route: [] zenoh '/rt/turtle1/cmd_vel' => DDS 'rt/turtle1/cmd_vel' with type'geometry_msgs::msg::dds_::Twist_'  zenoh '/rt/turtle1/cmd_vel' => DDS 'rt/turtle1/cmd_vel' with type'geometry_msgs::msg::dds_::Twist_' '/rt/turtle1/cmd_vel' ='rt/turtle1/cmd_vel''geometry_msgs::msg::dds_::Twist_'
   ```
3. On host 2, run the following **Python** script:

   ```
   # Some required imports # Some required imports # Some required imports import zenoh import zenoh import zenoh from pycdr import cdr from pycdr import cdr from pycdr importfrom pycdr.types import int8, int32, uint32, float64 from pycdr.types import int8, int32, uint32, float64 frompycdr.types import   # Declare the types of Twist message to be encoded and published via zenoh # Declare the types of Twist message to be encoded and published via zenoh # Declare the types of Twist message to be encoded and published via zenoh @cdr @cdr @cdrclass Vector3: class Vector3: class Vector3 x: float64  x: float64  y: float64  y: float64  z: float64  z: float64   @cdr @cdr @cdrclass Twist: class Twist: class Twist linear: Vector3  linear: Vector3  angular: Vector3  angular: Vector3   # Declare the types of Log message to be decoded and subscribed to via zenoh # Declare the types of Log message to be decoded and subscribed to via zenoh # Declare the types of Log message to be decoded and subscribed to via zenoh @cdr @cdr @cdrclass Time: class Time: class Time sec: int32  sec: int32  nanosec: uint32  nanosec: uint32   @cdr @cdr @cdrclass Log: class Log: class Log stamp: Time  stamp: Time  level: int8  level: int8  name: str  name: str str msg: str  msg: str str file: str  file: str str function: str  function: str str line: uint32  line: uint32   # Initiate the zenoh-net API # Initiate the zenoh-net API # Initiate the zenoh-net APIsession = zenoh.open() session = zenoh.open() =.   # Declare the callback and the subscriber for Log messages with key 'rt/rosout' # Declare the callback and the subscriber for Log messages with key 'rt/rosout' # Declare the callback and the subscriber for Log messages with key 'rt/rosout'def rosout_callback(sample): def rosout_callback(sample): def rosout_callback log = Log.deserialize(sample.payload)  log = Log.deserialize(sample.payload) =.. print('[{}.{}] [{}]: {}'.format(  print('[{}.{}] [{}]: {}'.format( print'[{}.{}] [{}]: {} '. log.stamp.sec, log.stamp.nanosec, log.name, log.msg))  log.stamp.sec, log.stamp.nanosec, log.name, log.msg)) ......   sub = session.declare_subscriber('rt/rosout', rosout_callback, reliability=zenoh.Reliability.RELIABLE()) sub = session.declare_subscriber('rt/rosout', rosout_callback, reliability=zenoh.Reliability.RELIABLE()) =.'rt/rosout' =..   # Publish a Twist message with key 'rt/turtle1/cmd_vel' to make the turtlesim to move forward # Publish a Twist message with key 'rt/turtle1/cmd_vel' to make the turtlesim to move forward # Publish a Twist message with key 'rt/turtle1/cmd_vel' to make the turtlesim to move forwardt = Twist(linear=Vector3(x=2.0, y=0.0, z=0.0), t = Twist(linear=Vector3(x=2.0, y=0.0, z=0.0), = = =2.0 =0.0 =0.0 angular=Vector3(x=0.0, y=0.0, z=0.0)).serialize()  angular=Vector3(x=0.0, y=0.0, z=0.0)).serialize() = =0.0 =0.0 =0.0.session.put('rt/turtle1/cmd_vel', t) session.put('rt/turtle1/cmd_vel', t) .'rt/turtle1/cmd_vel'   # Make it move forward until it hits the wall!! # Make it move forward until it hits the wall!! # Make it move forward until it hits the wall!!session.put('rt/turtle1/cmd_vel', t) session.put('rt/turtle1/cmd_vel', t) .'rt/turtle1/cmd_vel'session.put('rt/turtle1/cmd_vel', t) session.put('rt/turtle1/cmd_vel', t) .'rt/turtle1/cmd_vel'
   ```

You can see more complete versions of a “teleop” code with various options and arrows key-pressed listener here:

* in Python: <https://github.com/eclipse-zenoh/zenoh-demos/tree/main/ROS2/zenoh-python-teleop>
* in Rust: <https://github.com/eclipse-zenoh/zenoh-demos/tree/main/ROS2/zenoh-rust-teleop>

---

## How do I use zenoh to operate my robot from anywhere in the world ?

In the scenario described above, the zenoh application discovers the zenoh/DDS bridge via its scouting protocol that leverages UDP multicast - when available. Once discovered, a TCP connection is established between the app and the bridge

But the zenoh application can also be configured to directly establish a TCP connection with a known host, without relying on scouting protocol. Thus, it can connect directly to the bridge (if reachable) or to 1 or more zenoh routers that will route the zenoh communications between the application and the bridge.

Let’s see the different use cases:

### 1. Opening a TCP port and redirecting it to the zenoh/DDS bridge

Assuming you can configure your internet connection to open a public TCP port (e.g. 7447) and redirect it to the host running the zenoh/DDS bridge, you can do the following deployment:

Where:

* the zenoh/DDS bridge is started with this command:

  ```
  zenoh-bridge-dds -m peer -l tcp/0.0.0.0:7447 zenoh-bridge-dds -m peer -l tcp/0.0.0.0:7447 
  ```

  The `-l` option makes the bridge to listen for TCP connection on port 7447.
* Our zenoh teleop application must be configured to connect to the public IP and port of the bridge.  
  In Python, this is done adding a `"peer"` configuration when initializing the API:

  ```
  # note: replace "123.4.5.6" with your public IP in here: # note: replace "123.4.5.6" with your public IP in here: # note: replace "123.4.5.6" with your public IP in here:session = zenoh.net.open({"peer": "tcp/123.4.5.6:7447"}) session = zenoh.net.open({"peer": "tcp/123.4.5.6:7447"}) =.. "peer""tcp/123.4.5.6:7447"
  ```

  With the “teleop” demos provided [here](https://github.com/atolab/zenoh-demo/tree/main/ROS2), you can use the `-e tcp/123.4.5.6:7447` program argument.

### 2. Behind a NAT? Leverage a zenoh router in the cloud!

If you can’t open a public TCP port in your LAN, let’s use a zenoh router in a public cloud instance that will intermediate the communications between the bridge and the zenoh application:

To deploy this:

1. Pick your favorite cloud provider and provision a 64-bit Ubuntu VM with a public IP.
2. Install the zenoh router in this VM following those instructions: <http://zenoh.io/docs/getting-started/installation/#ubuntu-or-any-debian-x86-64>
3. Run the zenoh router in your vm staring:

   ```
   zenohd zenohd 
   ```

   Now the zenoh router is reachable on via the public IP of your VM on port **7447** by default.
4. Run the zenoh/DDS bridge as a router client, making it to connect the zenoh router:

   ```
   # note: replace "123.4.5.6" with your cloud VM's public IP in here: # note: replace "123.4.5.6" with your cloud VM's public IP in here: # note: replace "123.4.5.6" with your cloud VM's public IP in here:zenoh-bridge-dds -m client -e tcp/123.4.5.6:7447 zenoh-bridge-dds -m client -e tcp/123.4.5.6:7447 
   ```
5. our zenoh teleop application must be also configured as a router client to connect the zenoh router:

   ```
   # note: replace "123.4.5.6" with your cloud VM's public IP in here: # note: replace "123.4.5.6" with your cloud VM's public IP in here: # note: replace "123.4.5.6" with your cloud VM's public IP in here:session = zenoh.net.open({"mode": "client" , "peer": "tcp/123.4.5.6:7447"}) session = zenoh.net.open({"mode": "client" , "peer": "tcp/123.4.5.6:7447"}) =.. "mode" "client" "peer""tcp/123.4.5.6:7447"
   ```

   With the “teleop” demos provided [here](https://github.com/atolab/zenoh-demo/tree/main/ROS2), you can use the `-m client -e tcp/123.4.5.6:7447` program arguments.

### 3. What if my cloud instance crashes or reboot ?

Just deploy several interconnected zenoh routers in different cloud instances:

1. Run a first zenoh router in 1st cloud:

   ```
   zenohd zenohd 
   ```
2. Run another zenoh router in 2nd cloud, connected to zenoh router in 1st cloud:

   ```
   zenohd -e tcp/123.4.5.6:7447 zenohd -e tcp/123.4.5.6:7447 
   ```
3. Run the zenoh/DDS bridge as a router client, configured with the 2 zenoh routers’ locators:

   ```
   # note: replace "123.4.5.6" and "123.7.8.9" with your cloud VMs' public IPs in here: # note: replace "123.4.5.6" and "123.7.8.9" with your cloud VMs' public IPs in here: # note: replace "123.4.5.6" and "123.7.8.9" with your cloud VMs' public IPs in here:zenoh-bridge-dds -m client -e tcp/123.4.5.6:7447 -e tcp/123.7.8.9:7447 zenoh-bridge-dds -m client -e tcp/123.4.5.6:7447 -e tcp/123.7.8.9:7447 
   ```
4. our zenoh teleop application must be also configured as a router client and with the 2 zenoh routers’ locators:

   ```
   # note: replace "123.4.5.6" and "123.7.8.9" with your cloud VMs' public IPs in here: # note: replace "123.4.5.6" and "123.7.8.9" with your cloud VMs' public IPs in here: # note: replace "123.4.5.6" and "123.7.8.9" with your cloud VMs' public IPs in here:session = zenoh.net.open({"mode": "client" , "peer": "tcp/123.4.5.6:7447,tcp/123.7.8.9:7447"}) session = zenoh.net.open({"mode": "client" , "peer": "tcp/123.4.5.6:7447,tcp/123.7.8.9:7447"}) =.. "mode" "client" "peer""tcp/123.4.5.6:7447,tcp/123.7.8.9:7447"
   ```

   With the “teleop” demos provided [here](https://github.com/atolab/zenoh-demo/tree/main/ROS2), you can use the `-m client -e tcp/123.4.5.6:7447 -e tcp/123.7.8.9:7447` program arguments.

Now, both bridge and zenoh application will connect to the 1st configured locator (i.e. router in 1st cloud). If this one fails, they will both failover to the router in 2nd cloud.

### 4. Other deployments (e.g. mesh network)

Notice that in the previous use case, as the 2 zenoh routers are interconnected, the zenoh/DDS bridge and the zenoh application don’t need to be connected to the same router to communicate with each other. If they are connected to distinct routers, they will route the zenoh traffic between them, and the bridge and the application will still communicate with each other.

Actually, you can deploy the zenoh/DDS bridge, your teleop application and one or more interconnected zenoh router in all the ways described in the [zenoh documentation](./../docs/getting-started/key-concepts/#deployment-units). Just use the `-m peer` or `-m client` argument for the `zenoh-bridge-dds` to configure it as a peer or a client. And similarly for your zenoh teleop application.

---

## One more thing…

Did I mention that you can easily communicate with more than 1 robot using Eclipse zenoh? Let’s make several independent turtlesims move in a synchronous way!

Start as many turtlesim you want, each using its own ROS domain[1](#fn:1):

```
ROS_DOMAIN_ID=1 ros2 run turtlesim turtlesim_node ROS_DOMAIN_ID=1 ros2 run turtlesim turtlesim_node ROS_DOMAIN_ID = 1ROS_DOMAIN_ID=2 ros2 run turtlesim turtlesim_node ROS_DOMAIN_ID=2 ros2 run turtlesim turtlesim_node ROS_DOMAIN_ID = 2ROS_DOMAIN_ID=3 ros2 run turtlesim turtlesim_node ROS_DOMAIN_ID=3 ros2 run turtlesim turtlesim_node ROS_DOMAIN_ID = 3... ... 
```

For each turtlesim, run a zenoh/DDS bridge using the same ROS domain (via `-d` argument) and specifying a prefix that will be added to each zenoh key (via `-s` argument):

```
zenoh-bridge-dds -d 1 -m peer -s /bot-1 zenoh-bridge-dds -d 1 -m peer -s /bot-1 1zenoh-bridge-dds -d 2 -m peer -s /bot-2 zenoh-bridge-dds -d 2 -m peer -s /bot-2 2zenoh-bridge-dds -d 3 -m peer -s /bot-3 zenoh-bridge-dds -d 3 -m peer -s /bot-3 3... ... 
```

Now for turtlesim on domain 1, the `/rosout` and `/turtle1/cmd_vel` ROS2 topics are mapped respectively to `/bot-1/rt/rosout` and `/bot-1/rt/turtle1/cmd_vel` zenoh keys. And similarly but with a different prefix for each turtlesim.

The zenoh trick to rule them all is to just subscribe and publish via [path expressions](http://zenoh.io/docs/manual/abstractions/#key-expressions). In the Python code shown above:

* subscribe to `'/**/rosout'` instead of `'/rt/rosout'`
* publish Twist messages to `'/**/cmd_vel'` instead of `'/rt/turtle1/cmd_vel'`

You can also test this with the “teleop” demos provided [here](https://github.com/atolab/zenoh-demo/tree/main/ROS2), using the `--rosout='/**/rosout' --cmd_vel='/**/cmd_vel'` program arguments.

[**–JE**](https://github.com/JEnoch)

---

1. **Why 1 domain per robot ?**  
   In most of the cases, you don’t need the robots to communicate with each other. But if you let them use the same `ROS_DOMAIN_ID`, their DDS entities in the robots will anyway exchange discovery information with each other leading to a lot of unecessary traffic that could be problematic over wireless communications (as seen in our previous blog). The simplest way to avoid such traffic is to use distinct domains. Other solutions could be specific network configuration, or specific DDS configuration. [↩︎](#fnref:1)

**Next up**: [Minimizing Discovery Overhead in ROS2](../../blog/2021-03-23-discovery/)

---

# https://zenoh.io/blog/2021-07-13-zenoh-performance-async/

Source: https://zenoh.io/blog/2021-07-13-zenoh-performance-async/

* [Home](../../)
* [Documentation](../../docs/getting-started/first-app/)
* [Use Cases](../../usecases/)
* [Community](../../community/)
* [Adopters](../../adopters/)
* [Media](../../media/)
* [Blog](../../blog/2025-12-11-zenoh-jiaolong/)

# Zenoh performance: a stroll in Rust async wonderland

# Zenoh performance: a stroll in Rust async wonderland

13 July 2021 -- Paris.

Since its very first public release, zenoh provided impressive and easily accessible performances (see **[here](https://zenoh.io/blog/2020-06-29-zenoh-tidings/)**). But instead of resting on laurels, the zenoh team has been relentlessly working on further improving them.

As a result of this work, we are happy to announce that zenoh delivers at least twice the performances than before:

* more than **3.5M msg/s** with 8 bytes payload,
* more than **45 Gb/s** with 1 Megabyte payload,
* a latency as little as **35 µsec** in backlogged scenarios.

The reminder of this post will take you through the journey of zenoh profiling along with the nuts and bolts of Rust async programming. If you are unfamiliar with Rust and you are just interested in the results, you can jump directly **[here](#looking-at-the-results)**.

---

## Getting ready

As we previously wrote in this **[blog post](https://zenoh.io/blog/2020-06-29-zenoh-tidings/)**, zenoh is purely written in **[Rust](https://www.rust-lang.org/)** and leverages the **[async](https://async.rs/)** features to achieve high performance and scalability.

Even though initial zenoh performances were already quite good, we weren’t completely happy about them. Some numbers didn’t sum up as expected and we were very puzzled about it: we knew that zenoh could deliver more. We had only to discover what was preventing us from getting there. So, during the last few months we have been relentlessly profiling zenoh and looking into its most deep and intimate internals.

The very first thing we did was to properly prepare our testing environment in such a way to get reproducible results. This is very important when profiling your code otherwise you risk to walk down the wrong path: there are plenty of external factors that may impact the performance of the code. If you are about to profile your code, we highly recommend you to follow this **[guide](https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux)** that summarizes very well how to properly setup a Linux environment and how to get consistent results out of it.

The second thing was to have a thorough read of **[The Rust Performance Book](https://nnethercote.github.io/perf-book/title-page.html)**. If you are developing in Rust like us, we recommend you to go through it since we found it really insightful for what concerns performance tips and tricks along with profiling techniques in Rust. Another nice reference on how to write performant code in Rust can be found **[here](http://likebike.com/posts/How_To_Write_Fast_Rust_Code.html)**.

## Finding the hotspots

We started with identifying the hotspots in zenoh by generating flame-graphs with this **[tool](https://github.com/flamegraph-rs/flamegraph)**. We were confident that flame-graphs were a good way to visualize which part of the code takes most of the time in zenoh. We were wrong.

We couldn’t see any function taking a substantial amount of time to justify the performance mismatch we were observing. In addition, async was making the flame-graph quite difficult to read because of the async scheduler and future executor appearing almost everywhere in the graph. So, we changed the profiling tool and we started using **[perf](https://perf.wiki.kernel.org/index.php/Main_Page)** which provided, at least for us, a more clear view on the hotspots: notably on serialization and deserialization.

We improved our serializer and deserializer implementation and the synthetic benchmarks immediately improved by roughly 100%. However, that improvement didn’t reflect in the throughput tests. Nothing had changed. We were more puzzled than before.

## Heap or not to heap? Stack is the problem

Then we started looking into memory allocations. Since the beginning of zenoh, we have been very careful to avoid heap allocations in the critical path. We used **[Valgrind](https://www.valgrind.org/)** to double check if that was still the case and yes, it was: we didn’t observe unnecessary allocations nor suspicious high cache miss rates.

So, if it’s not the heap, it might be the stack. But how to see how deep the stack is? Especially when operating with async? Luckily for us, there is a very useful Rust compilation flag (available only in Rust nightly) to verify how big a data structure is and its cache alignment. It is sufficient to build zenoh (or any Rust code) with:

```
$ RUSTFLAGS=-Zprint-type-sizes cargo build --release $ RUSTFLAGS=-Zprint-type-sizes cargo build --release RUSTFLAGS =
```

In addition to the usual Cargo output, each data structure including async futures is printed out with the corresponding size and cache alignment. An examples of the generated output for the zenoh data message Rust struct is:

```
print-type-size type: `net::protocol::proto::msg::Data`: 304 bytes, alignment: 8 bytes print-type-size type: `net::protocol::proto::msg::Data`: 304 bytes, alignment: 8 bytes ` ` 304 8print-type-size field `.key`: 40 bytes print-type-size field `.key`: 40 bytes ` ` 40print-type-size field `.data_info`: 168 bytes print-type-size field `.data_info`: 168 bytes ` ` 168print-type-size field `.payload`: 96 bytes print-type-size field `.payload`: 96 bytes ` ` 96
```

And here comes the bitter discovery. These async futures, once compiled, were taking a few tens of KBs on the stack. These futures are called every time a message needs to be sent over the network. Unsurprisingly at this stage, we realized that we were putting too much pressure on the memory due to a stack too deep and large. Async libraries and runtime were doing their job correctly, they were putting on the stack everything that was needed in order to have a proper asynchronous environment. The problem was that we used async code too extensively in zenoh, mainly driven by its great simplicity and superb ergonomics.

So, we started a deep dive into zenoh internals and did some introspection on how to tackle the problem. We like async, it provides great flexibility and scalability properties to zenoh and we didn’t want to let it go. The final solution was to isolate the async code in specific parts of the code, especially the one interacting with the network, and to move some other parts to the standard sync library. As a result, zenoh has now a very balanced mix of sync and async code that takes the best of both worlds. This allowed us to drastically reduce the stack size of some critical async futures which immediately reflected in a massive performance boost as described below.

---

## Looking at the results

Throughput and latency tests are provided as examples in the main zenoh distribution. So, you can check what we actually used to get our throughput and latency results and replicate it yourself!

In the following we are going to show the throughput and latency results for both peer-to-peer and routed communications. To see the communication models supported by zenoh, please refer to the **[documentation](https://zenoh.io/docs/getting-started/key-concepts/)**.

All the tests below are run on three of our workstations equipped with an AMD Ryzen 5800x, 32 GB of RAM, connected through a 100Gb Ethernet connection, and configured according to this **[guide](https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux)**.

### Peer-to-peer communication

In the peer-to-peer communication test, we consider two peers that directly communicate with each other, that is without passing through an intermediate node.

#### Throughput

To build and run the p2p throughput tests just follow the instruction below:

```
$ git clone https://github.com/eclipse-zenoh/zenoh.git $ git clone https://github.com/eclipse-zenoh/zenoh.git $ cd zenoh $ cd zenoh cd$ cargo build --release --all-targets $ cargo build --release --all-targets   # ---- zenoh-net test ---- # ---- zenoh-net test ---- # ---- zenoh-net test ----# run the zenoh-net subscriber # run the zenoh-net subscriber # run the zenoh-net subscriber$ ./target/release/examples/zn_sub_thr $ ./target/release/examples/zn_sub_thr   # run the zenoh-net publisher with  (1024 below) # run the zenoh-net publisher with  (1024 below) # run the zenoh-net publisher with  (1024 below)$ ./target/release/examples/zn_pub_thr 1024 $ ./target/release/examples/zn_pub_thr 1024 1024   # ---- zenoh test ---- # ---- zenoh test ---- # ---- zenoh test ---- # run the zenoh subscriber # run the zenoh subscriber # run the zenoh subscriber$ ./target/release/examples/z_sub_thr $ ./target/release/examples/z_sub_thr   # run the zenoh publisher with  (1024 below) # run the zenoh publisher with  (1024 below) # run the zenoh publisher with  (1024 below)$ ./target/release/examples/z_put_thr 1024 $ ./target/release/examples/z_put_thr 1024 1024
```

In this test, one workstation runs the publisher while a separate one runs the subscriber. The figure below shows (in log scale) the number of messages per second for different payloads: from **8 bytes** to **1 GiB**.

As you can see, **zenoh-net API** delivers more than **3.5M msg/s** with a **8 bytes payload**. At the same time, **zenoh API** delivers **2M msg/s**.

The figure below shows (in log scale) the results in terms of throughput (bit/s) delivered at API level. We also report the throughput obtained with iperf on the same 100GbE connection as reference baseline: **60 Gb/s**.

As it can be noticed, a **100 Mb/s** connection is already saturated by zenoh-net and zenoh with a payload as little as **8 bytes**. A **1 Gb/s** connection is then saturated with a payload of **32** and **64 bytes** for zenoh-net and zenoh, respectively. A payload of **512** and **1024 bytes** is then sufficient for zenoh-net and zenoh to saturate a **10 Gb/s** connection. Finally, payloads larger than **128 KB** suffice to saturate a **40 Gb/s** connection.

#### Latency

Throughput figures are very nice, but about latency? To run the p2p latency tests just follow the instructions below:

```
# ---- zenoh-net test ---- # ---- zenoh-net test ---- # ---- zenoh-net test ----# run the zenoh-net pong # run the zenoh-net pong # run the zenoh-net pong$ ./target/release/examples/zn_pong $ ./target/release/examples/zn_pong   # run the zenoh-net ping # run the zenoh-net ping # run the zenoh-net ping$ ./target/release/examples/zn_ping $ ./target/release/examples/zn_ping   # ---- zenoh test ---- # ---- zenoh test ---- # ---- zenoh test ---- # run the zenoh pong # run the zenoh pong # run the zenoh pong$ ./target/release/examples/z_pong $ ./target/release/examples/z_pong   # run the zenoh ping # run the zenoh ping # run the zenoh ping$ ./target/release/examples/z_ping $ ./target/release/examples/z_ping 
```

With latency is necessary to clarify one very important aspect: latency depends on the load of the system. As you can see from the figure below, as the number of messages per second increases, latency actually decreases. This is due to the fact that when messages are sent at a low rate, the processes are more likely to be descheduled by the operating system. This operation adds additional latency since the processes need to be rescheduled when messages are sent and received. This is true for both zenoh and the classical ping, which is reported as a reference baseline for latency.

The x axis of the figure below shows the number of messages that we configured to be sent in one second, from 1 to 1 million and beyond. The inf case represents the scenario where messages are sent back-to-back as fast as possible. In such a backlogged scenario, we can see that zenoh latency is as little as **35 µsec** for both zenoh-net and zenoh APIs. The payload size is **64 bytes**, the same as standard ICMP.

### Routed communication

In the router communication test, we consider two clients that communicate with each other through an intermediate node: the zenoh router.

#### Throughput

To run the routed throughput tests just follow the instruction below:

```
# ---- zenoh-net test ---- # ---- zenoh-net test ---- # ---- zenoh-net test ---- # run the zenoh router # run the zenoh router # run the zenoh router$ ./target/release/zenohd $ ./target/release/zenohd   # run the zenoh-net subscriber # run the zenoh-net subscriber # run the zenoh-net subscriber$ ./target/release/examples/zn_sub_thr -m client $ ./target/release/examples/zn_sub_thr -m client   # run the zenoh-net publisher with  (1024 below) # run the zenoh-net publisher with  (1024 below) # run the zenoh-net publisher with  (1024 below)$ ./target/release/examples/zn_pub_thr 1024 -m client $ ./target/release/examples/zn_pub_thr 1024 -m client 1024   # ---- zenoh test ---- # ---- zenoh test ---- # ---- zenoh test ---- # run the zenoh router # run the zenoh router # run the zenoh router$ ./target/release/zenohd $ ./target/release/zenohd   # run the zenoh subscriber # run the zenoh subscriber # run the zenoh subscriber$ ./target/release/examples/z_sub_thr -m client $ ./target/release/examples/z_sub_thr -m client   # run the zenoh publisher with  (1024 below) # run the zenoh publisher with  (1024 below) # run the zenoh publisher with  (1024 below)$ ./target/release/examples/z_put_thr 1024 -m client $ ./target/release/examples/z_put_thr 1024 -m client 1024
```

In this test, one workstation runs the publisher, one runs the router and a third one runs the subscriber. The figure below shows (in log scale) the number of messages per second for different payloads: from **8 bytes** to **1GiB**.

As you can see, zenoh-net API delivers **3M msg/s** with a **8 bytes** payload. At the same time, zenoh API delivers **1.8M msg/s**. The figure below shows (in log scale) the same results in terms of throughput (bit/s) delivered at API level.

As it can be noticed, a **100 Mb/s** connection is still saturated by zenoh-net and zenoh with a payload as little as **8 bytes**. A **1 Gb/s** connection is then saturated with a payload of **64 bytes** for zenoh-net and zenoh. A payload of **1024 bytes** is then sufficient for both zenoh-net and zenoh to saturate a **10 Gb/s** connection. Finally, larger payloads are forwarded at **20-30 Gb/s**.

#### Latency

To run the routed latency tests just follow the instructions below:

```
# ---- zenoh-net test ---- # ---- zenoh-net test ---- # ---- zenoh-net test ---- # run the zenoh router # run the zenoh router # run the zenoh router$ ./target/release/zenohd $ ./target/release/zenohd   # run the zenoh-net subscriber # run the zenoh-net subscriber # run the zenoh-net subscriber$ ./target/release/examples/zn_pong -m client $ ./target/release/examples/zn_pong -m client   # run the zenoh-net publisher with  (1024 below) # run the zenoh-net publisher with  (1024 below) # run the zenoh-net publisher with  (1024 below)$ ./target/release/examples/zn_ping -m client $ ./target/release/examples/zn_ping -m client   # ---- zenoh test ---- # ---- zenoh test ---- # ---- zenoh test ---- # run the zenoh router # run the zenoh router # run the zenoh router$ ./target/release/zenohd $ ./target/release/zenohd   # run the zenoh subscriber # run the zenoh subscriber # run the zenoh subscriber$ ./target/release/examples/z_pong -m client $ ./target/release/examples/z_pong -m client   # run the zenoh publisher with  (1024 below) # run the zenoh publisher with  (1024 below) # run the zenoh publisher with  (1024 below)$ ./target/release/examples/z_ping -m client $ ./target/release/examples/z_ping -m client 
```

In the routed test, latency is double than the p2p test: **70 µs**. This is due to the fact that an additional network hop, i.e. the router, has been introduced between the two clients. Nevertheless, it can be noticed that the router does not add any noticeable latency to the overall communication, being the latency driven mainly by the number of hops. The payload size is still **64 bytes**.

---

## Conclusions

Summarizing, recent work makes zenoh capable to deliver over **3.5M msg/s** for small messages, over **45 Gb/s** for large messages, and a latency as little as **35 µsec**.

This has been possible thanks to the careful redesign of some core parts of zenoh that led to a more balanced mix of synchronous and asynchronous code. Although the results are already very remarkable, rest assured, our journey towards better performance doesn’t end here!

This blog post is just a very important milestone for zenoh, not the finishing line.

[**–LC**](https://github.com/Mallets/)

**Next up**: [Zenoh overhead: a story from our community](../../blog/2021-07-05-zenoh-overhead/)

---

# https://zenoh.io/blog/2021-10-04-zenoh-pico-guide/

Source: https://zenoh.io/blog/2021-10-04-zenoh-pico-guide/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh goes embedded with zenoh-pico

Blog Posts

# Zenoh goes embedded with zenoh-pico

04 October 2021 -- Paris.

In this post, we will introduce [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico), **a lightweight implementation of Zenoh APIs in C, fully compatible with its Rust counterpart**.

As a result of this work, we are happy to announce that we successfully deployed and tested Zenoh in [Zephyr](https://www.zephyrproject.org) (reel\_board and nucleo-f767zi) and [Arduino](https://www.arduino.cc) (ESP32) compatible boards, with initial results showcasing a quite remarkable performance within the microcontrollers landscape:

The reminder of this post will get you started with the environment setup, library installation, and project creation for your microcontrollers.

# A bit of context for zenoh-pico

[Zenoh](https://zenoh.io) has been natively designed to introduce minimal wire overhead (check our [previous blog post](https://zenoh.io/blog/2021-07-05-zenoh-overhead/)) and run across extremely constrained transports such as LPWAN and LowPAN, or directly over OSI Layer 2 (Data Link Layer) as well as to accommodate the resource constraints of embedded systems. However, since its very first public release, Zenoh Rust-based implementations have been focusing on providing high performance in widely used operating systems and platforms (check our [previous blog post](https://zenoh.io/blog/2021-07-13-zenoh-performance-async/)). As a side note, Arduino was supported in the [very first proof-of-concept for Zenoh](https://github.com/atolab/zhe). But what about other constraints devices and microcontrollers?

Fear not more because [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico) has come a long way to provide such support. **Zenoh-pico is a lightweight implementation of Zenoh APIs in C, fully compatible with its Rust counterpart.**

Internet of Things (IoT), home automation, and robotic systems appear among a set of use cases where Zenoh capabilities and features are a clear fit, paving the way for several benefits: support for push and pull communication models, geo distributed storage, and minimal wire overhead. However, most of these use cases rely on a variety of heterogeneous, low-powered, and resource constrained devices, making it a challenging environment to be supported. Just as an example, many IoT and smart home appliances being available in the market today (like smart plugs, motion sensors, door sensors, among others) are embedded with a ESP8266/ESP32 devices: the ESP32 is a dual-core 160MHz to 240MHz CPU with 320 KiB SRAM and 4MiB of built-in flash, whereas the ESP8266 is a single-core processor that runs at 80MHz with 80 KiB SRAM and 1 MiB of built-in flash. Similarly, many robotic systems are integrated with microcontrollers to control specific parts of the hardware as a complement to a more powerful device (e.g., Raspberry Pi) where all the logic is running.

**But is the Rust-based implementation of Zenoh supported by microcontrollers?**
Not yet, but **zenoh-pico comes to rescue**. Zenoh-pico is a lightweight implementation of the Zenoh protocol in C, fully compatible with its Rust counterpart. Its goal is three-fold: (i) provide a library implementation optimized for microcontrollers; (ii) provide a native C-based implementation (around 80% of embedded systems use C programming language); and (iii) keep the Rust-based implementation abstracted from the constraints imposed by microcontrollers.

**Being a lightweight implementation, what is it missing?**
Currently, zenoh-pico does offer all the functionalities for you to implement a Zenoh [client mode](./../docs/getting-started/key-concepts/#client-application) in microcontrollers. The support for peer-to-peer communication is still under planning and it does not feature the same level of message scheduling of the Rust stack.

**Which frameworks, platforms, or boards are currently supported?**
So far, we have successfully tested zenoh-pico in [Zephyr](https://www.zephyrproject.org) ([reel\_board](https://docs.zephyrproject.org/latest/boards/arm/reel_board/doc/index.html) and [nucleo-f767zi](https://docs.zephyrproject.org/2.6.0/boards/arm/nucleo_f767zi/doc/index.html) boards) and [Arduino](https://www.arduino.cc) ([ESP32](https://www.espressif.com/en/products/socs/esp32)). No changes have been made in the core of zenoh-pico, requiring only the implementation of the system calls for your specific framework / platform.

![msg-sec](../../img/blog-zenoh-pico-guide/boards.png)

![msg-sec](../../img/blog-zenoh-pico-guide/boards.png)

Well…enough talk, let’s see how to do it!!

# Step by step guide

In the following, we provide a step by step guide to build a Zenoh publisher.

## Prepare your environment

In order to manage and ease the process of building and deploying into a variety of microcontrollers, we suggest that PlatformIO is used as a supporting platform. Among other things, [PlatformIO](https://platformio.org) provides a multi-platform and multi-architecture build system, supporting ~48 different platforms, ~26 frameworks, and ~1035 boards, without any external dependencies to the operating system.

You can check the super-quick installation instructions (as they call it) [here](https://docs.platformio.org/en/latest//core/installation.html).

## Setup your project folder

Different platforms, frameworks, and boards require different project structures. But do not worry because you do not need to do it manually yourself. PlatformIO will give you a hand with that.

A typical PlatformIO project for must have the following structure:

### Zephyr

`project_dir
├── include
├── src
│ └── main.c
├── zephyr
│ ├── prj.conf
│ └── CMakeLists.txt
└── platformio.ini`

### Arduino

`project_dir
├── include
├── src
│ └── main.ino
└── platformio.ini`

To setup this project structure, execute the following commands:

`$ cd /path/to/project_dir
$ platformio init -b <board_name> #check board id by running platformio boards
$ platformio run`

For the Zephyr framework, additional configurations must be provided. These are included in both prj.conf and CMakeLists.txt files. Example files for reel\_board and nucleo\_f767zi boards are provided in the documentation files of zenoh-pico. We will be keeping this list updated as we test zenoh-pico support on other boards.

`$ cp /path/to/zenoh_pico/docs/zephyr/<board>/CMakelists.txt /path/to/project_dir/zephyr/
$ cp /path/to/zenoh_pico/docs/zephyr/<board>/prj.conf /path/to/project_dir/zephyr/`

## Set zenoh-pico as an external library in your project

This is as simple as doing a symlink. Easy right?

`$ ln -s /path/to/zenoh_pico/ /path/to/project_dir/lib/zenoh-pico`

## Implement your logic using zenoh-pico libraries

Your code goes inside /path/to/project\_dir/src/ folder. Note that some platforms/frameworks/boards do not follow the usual int main() for the programs’ entry point (e.g., ESP32).

Below you can find examples on how to implement a Zenoh publisher, publishing a message every 5 seconds.

### Zephyr

Examples provided with zenoh-pico work out of the box with Zephyr. However, note that in some boards, the board is still setting up the network when it starts running your program. In the following example, we solve this problem by sleeping for a couple of seconds.

`#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <zenoh-pico.h>
int main(int argc, char **argv)
{
 sleep(5);
 zn_properties_t *config = zn_config_default();
 zn_properties_insert(config, ZN_CONFIG_PEER_KEY, z_string_make("tcp/10.0.0.1:7447"));
 zn_session_t *s = zn_open(config);
 if (s == 0)
 {
 printf("Unable to open session!\n");
 exit(-1);
 }
 // Start the read session session lease loops
 znp_start_read_task(s);
 znp_start_lease_task(s);
 char *data = "Publishing from Zephyr";
 zn_reskey_t reskey = zn_rid(zn_declare_resource(s, zn_rname("/demo/example/zenoh-pico-zephyr")));
 zn_publisher_t *pub = zn_declare_publisher(s, reskey);
 if (pub == 0)
 {
 printf("Unable to declare publisher.\n");
 exit(-1);
 }
 while (1)
 {
 zn_write_ext(s, reskey, (const uint8_t *)data, strlen(data), Z_ENCODING_DEFAULT, Z_DATA_KIND_DEFAULT, zn_congestion_control_t_BLOCK);
 sleep(5);
 }
 return 0;
}`

### Arduino

`#include <Arduino.h>
#include <WiFi.h>
extern "C" {
 #include "zenoh-pico.h"
}
#define SSID "SSID"
#define PASS "PASSWORD"
// Zenoh-specific parameters
#define MODE "client"
#define PEER "tcp/10.0.0.1:7447"
#define URI "/demo/example/zenoh-pico-esp32"
zn_session_t *s = NULL;
zn_reskey_t *reskey = NULL;
void setup()
{
 // Set WiFi in STA mode and trigger attachment
 WiFi.mode(WIFI_STA);
 WiFi.begin(SSID, PASS);
 // Keep trying until connected
 while (WiFi.status() != WL_CONNECTED)
 { }
 delay(1000);
 zn_properties_t *config = zn_config_default();
 zn_properties_insert(config, ZN_CONFIG_MODE_KEY, z_string_make(MODE));
 zn_properties_insert(config, ZN_CONFIG_PEER_KEY, z_string_make(PEER));
 s = zn_open(config);
 if (s == NULL)
 {
 return;
 }
 znp_start_read_task(s);
 znp_start_lease_task(s);
 unsigned long rid = zn_declare_resource(s, zn_rname(URI));
 reskey = (zn_reskey_t*)malloc(sizeof(zn_reskey_t));
 *reskey = zn_rid(rid);
 zn_publisher_t *pub = zn_declare_publisher(s, *reskey);
 if (pub == NULL) {
 return;
 }
}
void loop()
{
 delay(5000);
 if (s == NULL)
 return;
 if (reskey == NULL)
 return;
 char *buf = "Publishing data from ESP-32";
 zn_write(s, *reskey, (const uint8_t *)buf, strlen(buf));
}`

## Build and upload

To build and upload the code into the board, run the following command:

`platformio run
platformio run -t upload`

# First look on memory footprint and performance results

The scarce memory and flash resources in microcontrollers stresses out the importance of the memory footprint of zenoh-pico. In the following table, you will find that zenoh-pico is introducing a memory footprint of only ~2.8% (nucleo-f767zi), ~9.2% (reel\_board), and ~0.9% (ESP32).

|  |  |  | **reel\_board (Zephyr)** |  |  | **nucleo-f767zi (Zephyr)** |  |  | **ESP32-D0WDQ6 (Arduino)** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Build-in Flash** |  |  | 1MiB |  |  | 2MiB |  |  | 4MiB |
| **Empty Binary (Zephyr-only)** |  |  | 68166 bytes |  |  | 127344 bytes |  |  | 385859 bytes |
| **Zenoh Publisher** |  |  | 164654 bytes |  |  | 186942 bytes |  |  | 423161 bytes |

In terms of application-level throughput (i.e., goodput), ESP32 board was able to deliver more than 5.2k msg/s with a 8 bytes payload, while for a payload of 4096 bytes nucleo-f767zi board the link gets up to 9.2 Mbps (thus, saturating the 10 Mbps Ethernet link).

![msg-sec](../../img/blog-zenoh-pico-guide/preliminary-benchmark.png)

![msg-sec](../../img/blog-zenoh-pico-guide/preliminary-benchmark.png)

\*Note: reel\_board and nucleo-f767zi are using Ethernet while ESP32 WiFi.

# Conclusion

As developers, we know how important it is to keep things efficient and optimized, especially when it comes to microcontrollers, while providing as transparent support as possible (no one likes to be setting up or significantly changing their projects).

Summarizing:

Help us increase the number of supported platforms, frameworks, and boards. We will provide all the support you need either in [GitHub](https://github.com/eclipse-zenoh) or [Discord](https://discord.gg/cY4nVjUd).

[**–CG**](https://github.com/cguimaraes/)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2021-11-09-ros2-zenoh-pico/

Source: https://zenoh.io/blog/2021-11-09-ros2-zenoh-pico/

![](../../img/zenoh-dragon-bg-150x163.png)

# ROS 2 and microcontrollers integration via Zenoh-pico

Blog Posts

# ROS 2 and microcontrollers integration via Zenoh-pico

09 November 2021 -- Paris.

In a [previous blog](https://zenoh.io/blog/2021-04-28-ros2-integration/), we showed how you can easily write native Zenoh applications and seamlessly interact with ROS 2 applications. This was exemplified by developing a native Zenoh teleoperation application to control a ROS 2 powered robot, namely a [turtlebot](https://www.robot-advance.com/EN/actualite-turtlebot3-burger-by-robotis-149.htm) or its simulation counterpart [turtlesim](http://wiki.ros.org/turtlesim), from anywhere in the world. In this blog, we will go one step further by trying to make it cool and fun – together with a bit of nostalgia.

As a result of this work, we are unveiling the capabilities of Zenoh to bridge the gap between ROS 2 and microcontroller environments by providing a lightweight and unified data-centric protocol coupled with its own implementation Zenoh middleware solution and DDS bridge. In other words, ROS 2 users can extend their application towards microcontrollers via Zenoh.

The reminder of this blog will recap the main concepts of our previous blog and guide you towards its extension to use [Zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico) and microcontrollers.

# Rewinding time

In the scenario described below, the Zenoh teleoperation application discovers the Zenoh/DDS bridge via its scouting protocol that leverages UDP multicast - when available. Once discovered, a TCP connection is established between the app and the bridge. But the Zenoh application can also be configured to directly establish a TCP connection with a known host, without relying on scouting protocol. Thus it can connect directly to the bridge (if reachable) or to 1 or more Zenoh routers that will route the Zenoh communications between the application and the bridge.

![msg-sec](../../img/blog-ros2-zenoh-pico/scenario-zenoh-dds.png)

![msg-sec](../../img/blog-ros2-zenoh-pico/scenario-zenoh-dds.png)

At this stage, the user can make use of its keyboard to control the robot (just like in a game).

# It seems like the 80s…can we fast forward in time?

Remember that it is a proof-of-concept demo to show the capabilities of Zenoh. Still, we have to agree that the turtlesim and teleoperation via keyboard is too much 80s.
So, how to forward this demo in time…

At this point, you might have guessed already that we are going for an immersive experience.

## Zenoh-powered Immersive Controller

As announced in a [previous blog](https://zenoh.io/blog/2021-10-04-zenoh-pico-guide/), Zenoh-pico is available as a lightweight implementation of Zenoh APIs in C, fully compatible with its Rust counterpart. It mainly targets embedded systems and, in particular, microcontrollers.

Thanks to the combination of Zenoh-pico, microcontrollers and a couple of sensors, we extended our initial teleoperation controller and embedded it anywhere. In doing so, we are going to show you how to control a turtlebot and its simulation counterpart turtlesim by means of hand gestures. For example, the small size of the microcontroller and sensors make them almost imperceptible to the eye and touch, and can be easily embedded in a regular glove for a truly immersive experience.

Wouldn’t it be cool and fun to have the power in your hand? How many of you have ever tried to use the force as a Jedi or telekinetic powers as an X-Men?

Here is a short video of our Zenoh-powered Immersive Controller prototype being used to control the turtlebot.

![msg-sec](../../img/blog-ros2-zenoh-pico/turtlebot-real-demo.gif)

![msg-sec](../../img/blog-ros2-zenoh-pico/turtlebot-real-demo.gif)

# Show me how to do it myself

All you need is an [ESP32](https://www.espressif.com/en/products/socs/esp32), a MPU-6050 accelerometer and gyroscope module and, of course, [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico). Note that, even if you decide to use other microcontrollers or sensors, all Zenoh-related code and components remain unchanged.

By providing a set of abstractions for pub/sub, geo distributed storage, query, and evals, Zenoh really simplifies the development of distributed applications. In other words, Zenoh internally handles all the inherent complexities of a distributed system and data distribution, keeping your life as a developer much simpler.

## 1. Pinout and Connections

The first step is to wire the ESP32 with the MPU-6050 sensor. Here are some guidelines:

| **MPU-6050** |  |  | **ESP32** |
| --- | --- | --- | --- |
| VCC |  |  | 3V3 |
| GND |  |  | GND |
| SCL |  |  | GPIO22 |
| SDA |  |  | GPIO21 |

|  |  |  |  |
| --- | --- | --- | --- |
| msg-sec |  |  | msg-sec |

![msg-sec](../../img/blog-ros2-zenoh-pico/diagram-pinout.png)
![msg-sec](../../img/blog-ros2-zenoh-pico/real-pinout.png)

## 2. Code

You can find the steps on how to set up your project in our [previous blog](https://zenoh.io/blog/2021-10-04-zenoh-pico-guide/). Then, you just need this little snippet of code to make it work. Note that, Zenoh-related code is only around 12 lines, while the remaining code is related to reading the values of the sensor, pre-processing them, and creating the Twist message.

`#include <Arduino.h>
#include <WiFi.h>
#include <Wire.h>
#include <MPU6050_tockn.h>
extern "C" {
 #include "zenoh-pico.h"
}
// WiFi-specific parameters
#define SSID "SSID"
#define PASS "PASSWORD"
// Zenoh-specific parameters
#define MODE "client"
#define URI "/rt/cmd_vel"
// Measurement specific parameters
#define X_SCALING_FACTOR 100.0
#define X_MAX_VALUE 0.20
#define X_MIN_VALUE -0.20
#define Y_SCALING_FACTOR 10.0
#define Y_MAX_VALUE 2.80
#define Y_MIN_VALUE -2.80
MPU6050 mpu(Wire);
double offset_x = 0.0;
double offset_y = 0.0;
zn_session_t *s = NULL;
zn_reskey_t *reskey = NULL;
void setup(void)
{
 // Set WiFi in STA mode and trigger attachment
 WiFi.mode(WIFI_STA);
 WiFi.begin(SSID, PASS);
 while (WiFi.status() != WL_CONNECTED)
 delay(1000);
 // Initialize MPU6050
 Wire.begin();
 mpu.begin();
 mpu.calcGyroOffsets(true);
 mpu.update();
 offset_x = mpu.getAccAngleX();
 offset_y = mpu.getAccAngleY();
 // Initialize Zenoh Session and other parameters
 zn_properties_t *config = zn_config_default();
 zn_properties_insert(config, ZN_CONFIG_MODE_KEY, z_string_make(MODE));
 s = zn_open(config);
 if (s == NULL)
 return;
 znp_start_read_task(s);
 znp_start_lease_task(s);
 unsigned long rid = zn_declare_resource(s, zn_rname(URI));
 reskey = (zn_reskey_t*)malloc(sizeof(zn_reskey_t));
 *reskey = zn_rid(rid);
 delay(1000);
}
void loop()
{
 delay(20);
 mpu.update();
 double linear_x = (mpu.getAccAngleX() - offset_x) / X_SCALING_FACTOR;
 linear_x = min(max(linear_x, X_MIN_VALUE), X_MAX_VALUE);
 if (linear_x < 0.10 && linear_x > -0.10)
 linear_x = 0;
 double linear_y = (mpu.getAccAngleY() - offset_y) / Y_SCALING_FACTOR;
 linear_y = min(max(linear_y, Y_MIN_VALUE), Y_MAX_VALUE);
 if (linear_y < 0.5 && linear_y > -0.5)
 linear_y = 0;
 Twist measure;
 measure.linear.x = linear_x;
 measure.linear.y = 0.0;
 measure.linear.z = 0.0;
 measure.angular.x = 0.0;
 measure.angular.y = 0.0;
 measure.angular.z = linear_y;
 uint8_t twist_serialized_size = 4 + sizeof(double) * 6;
 char buf[twist_serialized_size];
 serialize_twist(&measure, buf);
 if (s == NULL || reskey == NULL)
 return;
 zn_write(s, *reskey, (const uint8_t *)buf, twist_serialized_size);
}`

**Note:** auxiliary structs and serialization functions are missing in the previous snippet. For the full code, including the adaptations for the turtlesim, please check the code under <https://github.com/eclipse-zenoh/zenoh-demos/tree/main/ROS2/zenoh-pico-teleop-gyro>

## 3. Setting up the infrastructure and the turtlebot / turtlesim

In order to set up the infrastructure and the turtlebot / turtle in different configurations, follow the steps described in our [previous blog](https://zenoh.io/blog/2021-04-28-ros2-integration/). However, note that Zenoh-pico currently supports client mode only (a lightweight peer mode is coming soon). As such, you might need to deploy at least one Zenoh router to which your microcontroller application will need to connect to. The minimum steps are shown below:

## 4. Demonstration

If everything goes well, you might be able to control the robot just like in the video below.

| Turtlebot3 Burger |  |  | Turtlesim |
| --- | --- | --- | --- |
| msg-sec |  |  | msg-sec |

![msg-sec](../../img/blog-ros2-zenoh-pico/turtlebot-test-demo.gif)
![msg-sec](../../img/blog-ros2-zenoh-pico/turtlesim-test-demo.gif)

Really cool, isn’t it?!

# Conclusion

Although it seems a very simple demonstration, it is supported by several state-of-the-art technologies and protocols that are running under the hood. For you as a developer, being abstracted from all of them means that you can focus on the core business of your application.

Moreover, Zenoh and Zenoh-pico are bridging the gap between ROS 2 and microcontroller environments, allowing ROS 2 users to make use of all its capabilities within their applications. Summarizing some key points:

Tell us about your ideas on how to unlock the power of microcontrollers. We will provide all the support you need either in [GitHub](https://github.com/eclipse-zenoh) or [Discord](https://discord.gg/cY4nVjUd).

[**–CG**](https://github.com/cguimaraes/)
[**–GB**](https://github.com/gabrik/)
[**–JE**](https://github.com/JEnoch/)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2022-02-08-dragonbot/

Source: https://zenoh.io/blog/2022-02-08-dragonbot/

![](../../img/zenoh-dragon-bg-150x163.png)

# DragonBotOne Egg Hatching with Zenoh and Zenoh-Pico

Blog Posts

# DragonBotOne Egg Hatching with Zenoh and Zenoh-Pico

08 February 2022 -- Paris.

In previous blogs [(1)](https://zenoh.io/blog/2021-04-28-ros2-integration/)[(2)](https://zenoh.io/blog/2021-11-09-ros2-zenoh-pico/), we showed how you can easily develop native Zenoh applications and seamlessly integrate them with ROS2 applications by using Zenoh bridge for DDS. In particular, this was successfully exemplified by using a TurtleBot, a well-known, low-cost, personal robot kit with open-source software and hardware.

In this blog, we go one step further to show how you can bring Zenoh down to the TurtleBot’s microcontroller and control it from a different geographic location via a Zenoh infrastructure. By following a native Zenoh approach, you can rely on better decentralization concepts where no translation semantics are required.

Such approach allows the same technology to be used across all components from your application, from the microcontrollers to the cloud robotic platform, as well as bringing peer-to-peer capabilities to the microcontroller. To showcase it, we started working on the first demonstration of a TurtleBot look-a-like, fully Zenoh-powered personal robot that we will call from now on **DragonBotOne**.

![dragonbot-diagram](../../img/blog-dragonbot/DragonBotOne-diagram.png)

![dragonbot-diagram](../../img/blog-dragonbot/DragonBotOne-diagram.png)

Note that, although ROS2 is not used in this example, we still rely on ROS2 data type definitions as a way to leverage robot abstractions and to ease any migration towards Zenoh. As a consequence, leveraging the Zenoh-to-ROS2 connectivity any ROS2 application, anywhere on the Zenoh network, could interact with the robot.

Check out the final result!!!

![dragonbotone-demo](../../img/blog-dragonbot/DragonBotOne.gif)

![dragonbotone-demo](../../img/blog-dragonbot/DragonBotOne.gif)

The remainder of this blog will take you through the journey towards the hatching of our DragonBotOne egg.

# Checking behind the scenes

DragonBotOne is brought to life under the wings of Zenoh. Namely, both Zenoh and Zenoh-Pico implementation are on its genesis:

## DragonBotOne: OpenCR with WiFi connectivity

OpenCR consists of an open-source control module developed for ROS embedded systems. Given its completely open-source hardware and software and the fact it is widely used in several robotic applications, it quickly becomes our preferred choice for the development of DragonBotOne.

Still, we had to move some rocks along the way:

![dragonbotone](../../img/blog-dragonbot/DragonBotOne.png)

![dragonbotone](../../img/blog-dragonbot/DragonBotOne.png)

Finally, DragonBotOne made it all the way to hatch.

All source-code and step-by-step guides can be found in our [GitHub repositories](https://github.com/eclipse-zenoh/zenoh-demos/tree/main/zenoh-dragonbot).

## Remote Controller: ESP32 with a MPU-6050 accelerometer and gyroscope module

Born in a time where immersive experiences are becoming the mainstream, it is only natural if the controlling interfaces of DragonBotOne also follow such a paradigm. Thus, you can not only control DragonBotOne with a keyboard or a joypad but also by means of hand gestures.

For the development of this remote controller, we used an ESP32 with a MPU-6050 accelerometer and gyroscope module. By tilting the controller, you can make DragonBotOne to move forward and backward as well as to turn left and right. Moreover, you can control the velocity according to the inclination of the remote controller.

![remotecontroller](../../img/blog-dragonbot/RemoteController.png)

![remotecontroller](../../img/blog-dragonbot/RemoteController.png)

For additional implementation details, check our previous [blog](https://zenoh.io/blog/2021-11-09-ros2-zenoh-pico/).

# Conclusion

The simplicity and efficiency of Zenoh allied to the lightweightness of Zenoh-Pico is paving the way for a complete ecosystem in the whole cloud-to-things continuum, without impacting its high-performance or set of features and capabilities.

Summarizing the main takeaways:

Nevertheless, Zenoh is completely interoperable with already existing solutions that rely on ROS2+DDS. It is up to you to decide how high will our dragon fly or how deep will it swim.

We will provide all the support you need either in [GitHub](https://github.com/eclipse-zenoh) or [Gitter](https://gitter.im/atolab/zenoh).

[**–CG**](https://github.com/cguimaraes/)
[**–GB**](https://github.com/gabrik/)

# Additional Notes:

PlatformIO is a great tool when it comes to working with embedded development. Since OpenCR was not listed as one of the supported boards in PlatformIO, we decided to do it ourselves and share it with the community.

`$PLATFORMIO_DIR/platforms/ststm32`
`.piopm`
`$PLATFORMIO_DIR/platforms/ststm32`
`{"type": "platform", "name": "ststm32", "version": "15.2.0", "spec": {"owner": "platformio", "id": 8020, "name": "ststm32", "requirements": null, "url": null}}`
`$PLATFORMIO_DIR/packages/framework-arduinoststm32-opencr`
`.piopm`
`$PLATFORMIO_DIR/packages/framework-arduinoststm32-opencr`
`{"type": "tool", "name": "framework-arduinoststm32-opencr", "version": "1.4.18", "spec": {"owner": "platformio", "id": 8080, "name": "framework-arduinoststm32-opencr", "requirements": null, "url": null}}`
`platformio init -b opencr`

Now you can easily build and upload your own applications into OpenCR boards, but we would love them to be Zenoh-powered 😜

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2022-03-30-zenoh-mobility/

Source: https://zenoh.io/blog/2022-03-30-zenoh-mobility/

![](../../img/zenoh-dragon-bg-150x163.png)

# Mobility, Latency and Energy saving

Blog Posts

# Mobility, Latency and Energy saving

30 March 2022 -- Paris.

Connected cars, smart factories, swarms of robots… More and more applications need device mobility and require low latency for local device to device communications. With the increases in energy costs and its constrained availability, there is an increasing necessity to optimize data paths and to avoid unnecessary data transmissions – as just for clarity, communications takes the lion share in energy consumption when compared to computation.

Cloud centric architectures are energetically greedy and offer poor latency. Decentralization becomes an increasingly pressing necessity. In this blog post we will see why mobility raises complex challenges in decentralized deployments and how zenoh, with its efficient discovery and dynamic routing, can offer seamless session migration and overcome those obstacles.

## Cloud Architectures

Cloud architectures promote centralisation toward a cloud hosted instance of a service, such as storage, compute or messaging. If we consider cloud messaging, then devices connect to an instance deployed on a cloud data center that acts as a broker to provide connectivity to all other devices – as shown in the figure below. This approach is convenient in several aspects, since there is a single instance of the service sitting on the cloud. Yet it leads to a centralized, hub-and-spoke architecture that introduces several challenges with respect to latency, connectivity requirements, energy consumption, security, mobility and the ability to exploit locality.

![mobility1_crop_540x405.png](../../img/blog-zenoh-mobility/mobility1_crop_540x405.png)

![mobility1_crop_540x405.png](../../img/blog-zenoh-mobility/mobility1_crop_540x405.png)

## Decentralization with Zenoh

Zenoh has been designed to support decentralized architectures. As such, it supports different communication topologies, including peer-to-peer, routed and brokered, over which it provides high performance publish/subscribe and queries for geo-distributed storages. In peer-to-peer deployments, all devices communicate directly with each other without any infrastructure components involved. When direct communication is not possible, Zenoh routers act as mediation points for devices to get connectivity with the rest of the system and across the Internet. Thanks to its data-centric paradigm, zenoh can transparently allow devices to connect to the nearest zenoh router to get optimal routing paths to other points in the system and optimal latency for local communications, thus avoiding many of the issues faced by host-centric and End-to-End solutions.

![mobility2_crop_540x405.png](../../img/blog-zenoh-mobility/mobility2_crop_540x405.png)

![mobility2_crop_540x405.png](../../img/blog-zenoh-mobility/mobility2_crop_540x405.png)

## Decentralization and mobility

When mobility gets into the party, things get more complicated. As a device is moving and the handover occurs in the physical layer (5G roaming, WiFi handover, …), if the device remains connected to the same zenoh router, the data path becomes less and less optimal as the distance between them grows. This is a well-known issue in traditional mobility solutions as anchor points lead to suboptimal and longer data paths.

![mobility3_crop_540x405.gif](../../img/blog-zenoh-mobility/mobility3_crop_540x405.gif)

![mobility3_crop_540x405.gif](../../img/blog-zenoh-mobility/mobility3_crop_540x405.gif)

## zenoh session migration

As shown in this [previous experiment](https://zenoh.io/blog/2021-03-23-discovery/), the zenoh wire protocol is very lightweight and its discovery very efficient. The zenoh infrastructure and its several routing algorithms support high dynamicity. This allows zenoh devices to migrate their sessions from one zenoh router to another in a smooth and seamless manner. Devices can then connect to the nearest router after the mobility occurs and maintain optimal latency by migrating from zenoh router to zenoh router while moving.

![mobility4_crop_540x405.gif](../../img/blog-zenoh-mobility/mobility4_crop_540x405.gif)

![mobility4_crop_540x405.gif](../../img/blog-zenoh-mobility/mobility4_crop_540x405.gif)

## Demo

The following demo demonstrates zenoh session migration in a WiFi environment.

![mobility5_crop_720x540.png](../../img/blog-zenoh-mobility/mobility5_crop_720x540.png)

![mobility5_crop_720x540.png](../../img/blog-zenoh-mobility/mobility5_crop_720x540.png)

Hardware deployment:

Software deployment:

The application deployed in the robots constantly monitors the currently associated WiFi access point. Each time the WiFi access point changes, the robot application reconnects to the closest zenoh router (details discussed below).

To perform such zenoh session migrations it is needed that the device:

**Detects that it moved.** More precisely, detect that handover occurred and that a closer router may be available. Such detection is highly dependent on the kind of wireless communication involved (5G, WiFi, …) and it would be detected by the zenoh scouting sub-protocol. In this demo, the detection is performed by periodically looking at the BSSID of the currently associated WiFi access point.

**Finds the new closest zenoh router.** Again, this is dependent on the underlying infrastructure and would leverage an implementation of Zenoh’s scouting that is specific to the network. For instance, a DNS-based scouting implementation would probably be the most portable, or a DHCP-based scouting implementation might allow zenoh router discovery during IP bootstrap. For this particular demo, the robots are configured with a json file containing a WiFi BSSID to zenoh endpoints mapping.

Example :

`{
 "default": "[\"tcp/10.10.10.10:7447\"]",
 "00:00:00:00:00:00": "[\"tcp/10.10.10.11:7447\"]",
 "11:11:11:11:11:11": "[\"tcp/10.10.10.12:7447\"]"
}`

For this experiment, the mapping is deployed as a json file in each robot. But in a more advanced version, the mapping could be stored in several zenoh storages deployed at strategic places in the system. It could even be served by one or several zenoh queryables and computed on demand according to some algorithms.

## Conclusion

Mobility in decentralized environments is a notorious challenge. Zenoh provides a very efficient wire protocol, a light discovery and adaptive routing algorithms that demonstrates to be highly responsive in dynamic environments and topology changes and provides seamless session migration. This ensures optimal latency and resource consumption to devices in decentralized systems in spite of mobility.

[**–OH**](https://github.com/OlivierHecart)

*Special thanks to:*

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2022-04-14-rust-async-eval/

Source: https://zenoh.io/blog/2022-04-14-rust-async-eval/

![](../../img/zenoh-dragon-bg-150x163.png)

# A Performance Evaluation on Rust Asynchronous Frameworks

Blog Posts

# A Performance Evaluation on Rust Asynchronous Frameworks

14 April 2022 -- Paris.

As we previously mentioned in [this blog post](https://zenoh.io/blog/2021-07-13-zenoh-performance-async/), Zenoh is written in **Rust** and leverages the **async** features to achieve high performance and scalability. At the present stage, we rely on the [async\_std](https://async.rs/) framework – a decision that we took after a careful performance evaluation of the frameworks available in late 2019. This framework has proven to be quite effective, allowing Zenoh to reach more than **4M** msg/s with 8 bytes payload and over **45Gb/s** with 1MiB payload while keeping latency of **~30µsS**.

However, **async\_std** development seems to be stalling and the community appears to be moving towards other async frameworks, such as **Tokio**. As such, we decided to re-evaluate the major Rust async frameworks in order to assess the possibility to move to another framework without compromising our performances.

In this post, we will go through the evaluation of three asynchronous frameworks with respect to how they perform on asynchronous networking. Each of them will be evaluated and compared with the baseline performances provided by the equivalent synchronous primitives provided by the Rust standard library. Namely, we are targeting the following frameworks:

## Preparation of the testing environment

The first step toward reproducible results and fair evaluation is a stable and dedicated environment. In other terms, in any benchmarking effort, it is essential to reduce the number of factors that may influence the results of our performance evaluation. [This guide](https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux) effectively summarizes how to properly setup a Linux environment and how to get consistent results. The second recommendation is to have a thorough read of *“[The Rust Performance Book](https://nnethercote.github.io/perf-book/title-page.html)”* If you, like us, are developing in Rust, we recommend you to go through it since we found it really insightful for what concerns performance tips and tricks along with profiling techniques in Rust. Another nice reference on how to write performant code in Rust is [this one](http://likebike.com/posts/How_To_Write_Fast_Rust_Code.html%5D).

All the tests below are run on two of our workstations equipped with an AMD Ryzen 5800X @ 4.0GHz, 32 GB of RAM, running Ubuntu 20.04.3 LTS with Kernel 5.4.0-96-generic, connected through a 100Gb Ethernet connection (Mellaxon ConnectX-6 Dx).

## Experiment Description

For such evaluation, we concentrate on Round Trip Time (RTT) by building a ping-pong application for each framework. This synthetic benchmark is essential for us as it gives a lower bound on the achievable latency as well as its behavior under “async contention”. The **Round Trip Time (RTT)** is the amount of time it takes for a message to be sent plus the amount of time it takes for the acknowledgment of that message being received.

The picture below illustrates the ping-pong application, and how the RTT is computed.

![rtt](../../img/blog-rust-async-eval/rtt.png)

![rtt](../../img/blog-rust-async-eval/rtt.png)

Our RTT tests are provided [here](https://github.com/ZettaScaleLabs/rust-async-net-eval). So, you can check what we actually used to get the RTT results and replicate it yourself!

## Looking at the results

In the following, we are presenting the RTT results for all the frameworks under two different scenarios: over localhost and over the network.

### Localhost

In our first series of tests, the ping-pong application is executed on a single machine, leveraging only localhost communication.

#### RTT

To replicate these experiments, you can build and run the RTT test by following these instructions:

`$ git clone https://github.com/ZettaScaleLabs/rust-async-net-eval.git
$ cd rust-async-net-eval.git
$ make
# ---- RTT in localhost ----
# run all the tests in localhost
$ ./run-localhost.sh -asStP
# parse the results
$ python3 parse.py -d latency-logs -k rtt -o localhost-latency.pdf -l 0`

One very important aspect to mention is that RTT depends on the load of the system. As you can see from the figure below, as the number of messages per second increases, RTT decreases. This is due to the fact that when messages are sent at a low rate, the processes are more likely to be de-scheduled by the operating system. This operation adds additional latency since the processes need to be rescheduled when messages are sent and received. This is true for both the Rust code and the classical ping, which is reported as a reference baseline for RTT.

The x-axis of the figure below shows the number of messages that we configured to be sent in one second, from a single message to 1 million and beyond. The *inf* case represents the scenario where messages are sent back-to-back as fast as possible. In such a backlogged scenario, we can see that Rust latency is as little as 5 µs for the standard library. The payload size of each message is 64 bytes, the same as standard ICMP.

![localhost](../../img/blog-rust-async-eval/local-0.png)

![localhost](../../img/blog-rust-async-eval/local-0.png)

### Over the network

It is also interesting to see the behavior over a real physical network, as the asynchronous frameworks should take advantage of real blocking I/O operations, such as sending messages over the network. In this case, we used two workstations, one running the ping and the other one running the pong.

![net-100gbe](../../img/blog-rust-async-eval/100gbe-0.png)

![net-100gbe](../../img/blog-rust-async-eval/100gbe-0.png)

### Adding CPU bounded computing

But Zenoh does not only send data, but it also has a set of CPU-bound tasks, like looking up a forwarding table, de/serializing messages, and so on. To this extent, it is interesting to validate how such frameworks perform when interleaving the I/O tasks with come computing-intensive tasks.

A Zenoh peer runs two separate tasks for each session with other Zenoh peers, so we modified the ping-pong applications to spawn a number of tasks that mimics those compute-intensive tasks.
In our tests we range from 10 to 1000 tasks, mimicking from 5 to 500 “zenoh sessions”, figures below illustrate the different results.

#### Localhost

##### 10 tasks

![local-10](../../img/blog-rust-async-eval/local-10.png)

![local-10](../../img/blog-rust-async-eval/local-10.png)

##### 1000 tasks

![local-1000](../../img/blog-rust-async-eval/local-1000.png)

![local-1000](../../img/blog-rust-async-eval/local-1000.png)

#### Over a 100GbE network

In this series of tests the ping and the pong applications are running on two different machines, leveraging the 100GbE network connectivity, varying the number of computing tasks.

##### 10 tasks

![100gbe-10](../../img/blog-rust-async-eval/100gbe-10.png)

![100gbe-10](../../img/blog-rust-async-eval/100gbe-10.png)

##### 100 tasks

![100gbe-100](../../img/blog-rust-async-eval/100gbe-100.png)

![100gbe-100](../../img/blog-rust-async-eval/100gbe-100.png)

##### 1000 tasks

![100gbe-1000](../../img/blog-rust-async-eval/100gbe-1000.png)

![100gbe-1000](../../img/blog-rust-async-eval/100gbe-1000.png)

## Conclusions

Our evaluation shows **async\_std** and **smol** are quite close to the standard library and outperform it on some workloads. On the other hand, **Tokio** seems to reach very soon its limit ~18µs with 100 msg/s and it shows no differences between TCP and UDP. Additionally, Tokio seems to be adversely impacted by the CPU-bound (Rust) asynchronous tasks.
Based on these results, we believe that we have no choice but remain on **async-std**. That said, it would be interesting to understand why **Tokio** exposes such behavior under contention and also to improve its raw performance to close the gap with **async\_std**. As it stands, **Tokio** introduces 8µs additional latency in localhost and 10µs over the network.

Ideally, we would like to see one async framework becoming the “standard”, but to do so we can’t ignore raw performance. We look forward to engaging and working with the rest of the community to help make this happen.

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2022-06-09-zenoh-pico-above-and-beyond/

Source: https://zenoh.io/blog/2022-06-09-zenoh-pico-above-and-beyond/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh-Pico: Above and Beyond

Blog Posts

# Zenoh-Pico: Above and Beyond

09 June 2022 -- Paris.

In a [previous blog post](https://zenoh.io/blog/2021-10-04-zenoh-pico-guide/), we introduced Zenoh-Pico, an implementation of Zenoh for microcontrollers and embedded devices, along with a preliminary performance results and its integration on off-the-shelf robots (by bridging both legacy ROS2+DDS and Zenoh systems or by making it a full-fledged Zenoh system).

In this post, we will dive deeper on Zenoh-Pico, show, how Zenoh-Pico is capable of:

The remainder of this post will compare Zenoh-Pico against technologies currently used in embedded devices, and more specifically with DDS-XRCE, MQTT, and OPC-UA. We will depart from higher layers analyzing the ergonomics and simplicity of the APIs, we will then look into performances and compare throughput, latency, wire overhead, and flash memory footprint.

# Why constrained devices?

With digitalization spreading across industries and the growing adoption of Cyber Physical Systems (CPS) new applications, services, and use cases are emerging that require scalable, and extremely performant,i.e. , high throughput and low latency, data-management technologies. Connected cars, smart factories, swarms of robots are some examples that impose such requirements over device-to-device and/or device-to-Edge-to-Cloud communications.

This means that your applications can operate beyond standalone systems limited to onboard capabilities, and start exploiting the ubiquitous computing, storage, and networking capabilities available anywhere in the network and at any time. Data distribution and storage became paramount in such vision, thus data exchange protocols face new needs with respect to vertical and horizontal scalability, support for constrained networks and devices with low duty cycle – in other terms devices that are disconnected/sleeping most of the time as well as ability to deal with both data in motion and data at rest.

Protocols used today to build these systems, such as MQTT, DDS, CoAP and even HTTP were not designed with these needs in mind nor considering the whole Cloud-to-Things continuum. As a result, architects and developers are forced into patchwork design in which multiple protocols are stitched together to provide some meaningful end-to-end semantics.

**Zenoh** provides a stack that unifies data in motion data at rest and computations, by carefully blending traditional pub/sub with geo-distributed storages, queries and computations while retaining a level of time and space efficiency that is well beyond any of the mainstream stacks. And beyond all that, your entire system can leverage on Zenoh as the single solution, no matter if your applications are running on a microcontroller and/or in a powerful resource in the Cloud.

# Zenoh API for constrained devices

APIs should provide a minimal set of well defined and composable primitives. That’s easily said but takes a deep understanding of the problem space and the patience necessary to refine the solution. In Zenoh, we went through a careful thought process in order to understand the abstractions and primitives that must or must not be provided to the users, hiding irrelevant details while not reducing its expressiveness. As a result, Zenoh-Pico provides exactly the same set of primitives as provided by the Zenoh Rust-implementation and its binding, making in fact 99% of Zenoh-C source-code copyable into Zenoh-Pico code.

“(Software design is) a craft…and it has a lot to do with valuing simplicity over complexity. Many people do have a tendency to make things more complicated than they need to be.”

— Barbara Liskov

But let’s look at some code!! In the following, we compare the minimal source code required to implement a publisher of data in constrained devices, whenever done with Zenoh or with other widely used solutions for robotics (i.e., DDS-XRCE), industrial environments (i.e., OPC-UA), and IoT (i.e., MQTT).

## Zenoh API

`int main(int argc, char **argv)
{
 zn_properties_t *config = zn_config_default();
 zn_session_t *s = zn_open(config);
 if (s == NULL)
 exit(EXIT_FAILURE);
 znp_start_read_task(s);
 znp_start_lease_task(s);
 zn_reskey_t reskey = zn_rid(zn_declare_resource(s, zn_rname("/demo/example/topic")));
 // ...
 zn_write(s, reskey, (const uint8_t *)buf, buflen);
 znp_stop_read_task(s);
 znp_stop_lease_task(s);
 zn_close(s);
}`

## XRCE-DDS API

`typedef struct
{
 char *buf;
} MyDataType;
bool MyDataType_serialize_topic(ucdrBuffer* writer, const MyDataType* data)
{
 ucdr_serialize_array_uint8_t(writer, data->buf, buflen + 1);
 return !writer->error;
}
uint32_t MyDataType_size_of_topic(const MyDataType* data, uint32_t size)
{
 uint32_t previousSize = size;
 size += (uint32_t)(ucdr_alignment(size, 4) + 4 + buflen + 1);
 return size - previousSize;
}
int main(int argc, char** argv)
{
 uxrUDPTransport transport;
 if (!uxr_init_udp_transport(&transport, UXR_IPv4, DDS_IP, DDS_PORT))
 exit(EXIT_FAILURE);
 uxrSession session;
 uxr_init_session(&session, &transport.comm, 0x11111111);
 if (!uxr_create_session(&session))
 exit(EXIT_FAILURE);
 uint8_t output_reliable_stream_buffer[BUFFER_SIZE];
 uxrStreamId reliable_out = uxr_create_output_reliable_stream(&session, output_reliable_stream_buffer, BUFFER_SIZE, STREAM_HISTORY);
 uint8_t input_reliable_stream_buffer[BUFFER_SIZE];
 uxr_create_input_reliable_stream(&session, input_reliable_stream_buffer, BUFFER_SIZE, STREAM_HISTORY);
 uint8_t output_besteffort_stream_buffer[BUFFER_SIZE];
 uxrStreamId besteffort_out = uxr_create_output_best_effort_stream(&session, output_besteffort_stream_buffer, BUFFER_SIZE);
 // Create entities
 uxrObjectId participant_id = uxr_object_id(0x01, UXR_PARTICIPANT_ID);
 const char* participant_xml = "<dds><participant><rtps><name>default_xrce_participant</name></rtps></participant></dds>";
 uint16_t participant_req = uxr_buffer_create_participant_xml(&session, reliable_out, participant_id, 0, participant_xml, UXR_REPLACE);
 uxrObjectId topic_id = uxr_object_id(0x01, UXR_TOPIC_ID);
 const char* topic_xml = "<dds><topic><name>/demo/example/topic</name><dataType>MyDataType</dataType></topic></dds>";
 uint16_t topic_req = uxr_buffer_create_topic_xml(&session, reliable_out, topic_id, participant_id, topic_xml, UXR_REPLACE);
 uxrObjectId publisher_id = uxr_object_id(0x01, UXR_PUBLISHER_ID);
 const char* publisher_xml = "";
 uint16_t publisher_req = uxr_buffer_create_publisher_xml(&session, reliable_out, publisher_id, participant_id, publisher_xml, UXR_REPLACE);
 uxrObjectId datawriter_id = uxr_object_id(0x01, UXR_DATAWRITER_ID);
 const char* datawriter_xml = "<dds><data_writer><topic><kind>NO_KEY</kind><name>/demo/example/topic</name><dataType>MyDataType</dataType></topic></data_writer></dds>";
 uint16_t datawriter_req = uxr_buffer_create_datawriter_xml(&session, reliable_out, datawriter_id, publisher_id, datawriter_xml, UXR_REPLACE);
 uint8_t status[4];
 uint16_t requests[4] = { participant_req, topic_req, publisher_req, datawriter_req};
 if (!uxr_run_session_until_all_status(&session, 1000, requests, status, 4))
 exit(EXIT_FAILURE);
 // ...
 ucdrBuffer ub;
 MyDataType topic = { buf };
 uint32_t topic_size = MyDataType_size_of_topic(&topic, 0);
 uxr_prepare_output_stream(&session, besteffort_out, datawriter_id, &ub, topic_size);
 MyDataType_serialize_topic(&ub, &topic);
 connected = uxr_run_session_time(&session, 1000);
 uxr_delete_session(&session);
 uxr_close_udp_transport(&transport);
 return 0;
}`

## MQTT API

`void on_connect_failure(void* context, MQTTAsync_failureData5* response)
{
 printf("Connect failed, rc %d\n", response->code);
 exit(EXIT_FAILURE);
}
void on_connect(void* context, MQTTAsync_successData5* response)
{
 ready = 1;
}
int main(int argc, char** argv)
{
 MQTTAsync client;
 MQTTAsync_createOptions create_opts = MQTTAsync_createOptions_initializer;
 create_opts.MQTTVersion = MQTTVERSION_5;
 int rc = MQTTAsync_createWithOptions(&client, MQTT_BROKER, MQTT_CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL, &create_opts);
 if (rc != MQTTASYNC_SUCCESS)
 exit(EXIT_FAILURE);
 MQTTAsync_connectOptions conn_opts = MQTTAsync_connectOptions_initializer5;
 conn_opts.keepAliveInterval = 3;
 conn_opts.onSuccess5 = on_connect;
 conn_opts.onFailure5 = on_connect_failure;
 conn_opts.context = client;
 conn_opts.MQTTVersion = MQTTVERSION_5;
 conn_opts.cleanstart = 1;
 rc = MQTTAsync_connect(client, &conn_opts);
 if (rc != MQTTASYNC_SUCCESS)
 {
 MQTTAsync_destroy(&client);
 exit(EXIT_FAILURE);
 }
 while (!ready);
 // ...
 MQTTAsync_message pubmsg = MQTTAsync_message_initializer;
 pubmsg.payload = buf;
 pubmsg.payloadlen = buflen;
 pubmsg.qos = MQTT_QOS;
 pubmsg.retained = 0;
 MQTTAsync_sendMessage(client, "/demo/example/topic", &pubmsg, NULL);
 MQTTAsync_disconnectOptions disc_opts = MQTTAsync_disconnectOptions_initializer;
 rc = MQTTAsync_disconnect(client, &disc_opts);
 MQTTAsync_destroy(&client);
 exit(EXIT_SUCCESS);
}`

# OPC-UA API

`int main(int argc, char **argv)
{
 UA_Client *client = UA_Client_new();
 UA_ClientConfig_setDefault(UA_Client_getConfig(client));
 UA_StatusCode status = UA_Client_connect(client, "opc.tcp://localhost:4840");
 if(status != UA_STATUSCODE_GOOD)
 {
 UA_Client_delete(client);
 return status;
 }
 // ...
 UA_String val = UA_STRING(buf);
 UA_Variant value;
 UA_Variant_init(&value);
 UA_Variant_setScalarCopy(&value, &val, &UA_TYPES[UA_TYPES_STRING]);
 status = UA_Client_writeValueAttribute(client, UA_NODEID_STRING(1, "/demo/example/topic"), &value);
 UA_Variant_clear(&value);
 UA_Client_delete(client);
 return status;
}`

All the previous examples are doing exactly the same – publish a string of data under a given topic. That is the basic primitive that the developer should care about, circumscribing all the complexity only to the required, without ‘nice to have’ features that are not relevant from the user point of view. But be aware, that just because you do not see these ‘nice to have’ features does not mean that the user cannot exploit them.

# Performance comparison on Linux environment

Although Zenoh APIs are simple to understand and use, it still gives the user the proper handles to extract the best performance from Zenoh. Below you can check a set of tests comparing different solutions and performed under the same set of conditions, as explained in a [previous blog post](https://zenoh.io/blog/2022-04-14-rust-async-eval/).

Note that, for the sake of fairness, Zenoh is evaluated under a brokered model since it is the same model provided by all the other solutions. In such a model, Zenoh clients connect the nearest Zenoh node in the infrastructure node to exchange communications. Still, Zenoh allows peer-to-peer models to be in-place peers that allows Zenoh nodes to directly communicate with one another, without passing through an intermediate node.

![setup-demo](../../img/blog-pico-performance/setup-demo.png)

![setup-demo](../../img/blog-pico-performance/setup-demo.png)

All the tests below are run on two of our workstations equipped with an AMD Ryzen 5800X @ 4.0GHz, 32 GB of RAM, running Ubuntu 20.04.3 LTS with Kernel 5.4.0-96-generic, connected through a 100Gb Ethernet connection (Mellaxon ConnectX-6 Dx).

Let’s check the numbers!!

## Throughput

![throughput](../../img/blog-pico-performance/zenoh_pico_throughput.png)

![throughput](../../img/blog-pico-performance/zenoh_pico_throughput.png)

As you can see, Zenoh-Pico operating over a unicast transport is able to exchange data messages at a rate of **~2.5M msg/s** with a 8 bytes payload. As it can be noticed, a 100 Mb/s connection is already saturated by Zenoh-Pico with a payload as little as 8 bytes. For payloads of 8 bytes, 64 bytes and 1024 bytes, Zenoh-Pico is already saturating, respectively, a 100Mbps, 1Gbps and 10Gbps connection. Payloads larger than 8 KB are sufficient to achieve **>25Gbps** of application throughput.

In turn, when operating over a multicast transport, although both pub and sub are directly exchanging multicast messages without the need for a broker, Zenoh-Pico has a lower performance when compared to the unicast scenario. The reason lies solely in the fact that data messages are not being batched.

When comparing against the remaining solutions, Zenoh-Pico is able to achieve significantly better throughput performance, almost **10x better than XRCE-DDS, 40x better than MQTT and 55x better than OPC-UA**.

Finally, Zenoh-Pico and MQTT were the only solutions that were able to send payloads up to 8192 bytes, while XRCE-DDS was not able to send payloads bigger than 256 bytes and OPC-UA bigger than 4096 bytes.

## Latency

Throughput figures are looking nice, but about latency?

With latency is necessary to clarify one very important aspect: latency depends on the load of the system. As you can see from the figure below, as the number of messages per second increases, latency actually decreases. This is due to the fact that when messages are sent at a low rate, the processes are more likely to be descheduled by the operating system. This operation adds additional latency since the processes need to be rescheduled when messages are sent and received.

![throughput](../../img/blog-pico-performance/zenoh_pico_latency.png)

![throughput](../../img/blog-pico-performance/zenoh_pico_latency.png)

The x axis of the figure below shows the number of messages (payload size of 16 bytes) that are sent in one second. In such a backlogged scenario, we can see that Zenoh-Pico latency (one way delay) is as little as **45 µsec** for the unicast transport, being on par with the remaining solutions. Note that OPC-UA already achieves such a latency for lower message loads because it follows a polling approach, thus its processes are less likely to be descheduled by the operating system.

In addition, if we consider that Zenoh-Pico is in peer mode and making use of the multicast transport, its latency can be as small as **15 µsec**.

## Overhead

One might think that having high throughput and low latency is all that matters right? Not quite true. It might be that you need to optimize your power consumption and the link budget as is the case of [Low Throughput Networks](https://www.etsi.org/deliver/etsi_gs/ltn/001_099/002/01.01.01_60/gs_ltn002v010101p.pdf), where you would be allowed to send as low as 200 bytes per day (5KB maximum), payloads as low as 12 bytes (255 bytes maximum) and throughput as low as 10 bps (1kbps maximum).

Where do you think Zenoh stands? Let me give you a hint: Zenoh has been designed to run across extremely constrained networks, including on OSI Layer 2, and it has a **minimal wire overhead of 5 bytes.**

Let’s look at the numbers!

![overhead](../../img/blog-pico-performance/zenoh_pico_overhead.png)

![overhead](../../img/blog-pico-performance/zenoh_pico_overhead.png)

Except for the session opening and closing, Zenoh offers the lowest overhead in the wire for the remaining operations. However, data is the recurrent operation for publishing data, making the others a one-time operation for the whole lifetime of a session. Even though, Zenoh only sends 71 bytes more in the wire, during the opening and closing operations, when compared to the less expensive solution.

Still, the most important operation is publishing data, and **Zenoh overhead in the wire is 98%, 75% and 64% smaller when compared to OPC-UA, XRCE-DDS and MQTT**. In doing so, Zenoh is considerably less expensive if we consider long-lived sessions that periodically publish information (e.g., IoT sensoring systems making use of Low Throughput Networks).

As for the keep-alives, in Zenoh they are not sent if any message is transmitted between the session peers in the corresponding lease window, making its overhead non-existent for periodic publishers.

## Flash Memory Overhead

Flash memory might be an extremely restrictive element in constrained devices like IoT devices, not comprising more than 1MB of flash memory. This means that all the compiled software (including the user code and libraries), firmware and any other data the device can download needs to fit in such a small amount of space.

It becomes quite important that Zenoh footprint is as small as possible. Check in the following table, the footprint of Zenoh w.r.t. different RTOSs and different networking configurations.

|  | **Arduino** | **Zephyr** | **MBedOS** |
| --- | --- | --- | --- |
| **Empty App (wo/ Zenoh-Pico)** | 17796 bytes | 160400 bytes | 49552 bytes |
| **Zenoh-Pico core (wo/ networking stacks)** | 62844 bytes | 202980 bytes | 99568 bytes |
| **Zenoh-Pico w/ UDP stack** | 98176 bytes | 209410 bytes | 158008 bytes |
| **Zenoh-Pico w/ TCP stack** | 104140 bytes | 209434 bytes | 158144 bytes |
| **Zenoh-Pico w/ UDP and TCP stacks** | 104916 bytes | 211988 bytes | 160008 bytes |
| **Zenoh-Pico w/ Serial Stack** | Not supported yet | Not supported yet | 122472 bytes |

Note that, most of the additional footprint required to include a networking stack does not come from Zenoh-Pico itself but from the RTOS (Arduino / Zephyr / MBedOS) implementations.

Out of the box, Zenoh-Pico allows you to incorporate all capabilities provided by Zenoh in less than **~50KB** within your microcontroller applications. Still, the set of supported features can be stripped down at compilation time. This provides you the flexibility to define the set of Zenoh features that you require at your application, allowing you to reduce Zenoh-Pico footprint to the minimum w.r.t. your application.

Taking the example of a Zenoh publisher, Zenoh-Pico core can be reduced to only **~15KB** of footprint in the flash memory, enabling Zenoh capabilities to be included in applications running on Atmel-based 8-bits MCUs with 32KB of flash memory like Arduino Uno or similar.

# Conclusion

Zenoh-Pico is a lightweight implementation of Zenoh targeted for microcontroller and embedded systems. This blog has shown how it delivers better performance than alternative technologies and has less overhead.

In summary, Zenoh-Pico capable of:

This blog post is just a very important milestone for Zenoh-Pico, but we will not rest here. We aim to use it as the baseline comparison for all developments in the future, making sure that our compass is calibrated towards the right direction. As short-term evaluations, we will target a performance assessment on different **RTOS already supported by Zenoh-Pico**, namely **Arduino**, **Zephyr**, **MBedOS** and **ESP-IDF**.

And remember…while most of us demand more and more powerful computers, the future of our technological world will greatly depend on the smallest things.

[**–CG**](https://github.com/cguimaraes/)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2022-08-12-zenoh-serial/

Source: https://zenoh.io/blog/2022-08-12-zenoh-serial/

![](../../img/zenoh-dragon-bg-150x163.png)

# There is Land Besides IP: How to Cross It with Zenoh

Blog Posts

# There is Land Besides IP: How to Cross It with Zenoh

12 August 2022 -- Paris.

Since the early 2000s the transition towards All-IP networks had been pushed as a natural evolutionary path. Today, IP is the dominant stack for packet-based integrated networks deployed worldwide. However, there is land beyond the ocean…in other words, **there is an entire and growing non-IP universe that cannot be ignored**. This universe expands at the outskirts of ordinary IP networks, where other protocols shine brighter because of more stringent requirements on **overhead, energy-efficienciency, latency / real-time, and cost**.

In this post, we will show how **Zenoh can simultaneously operate over multiple layers of the OSI model**, accommodating IP and non-IP networks. By the end of this post, you will be able to use **Zenoh over Serial** for some of your applications and have them transparently communicate with applications running over IP networks.

# Zenoh runs where you need it

Simply put, **Zenoh is capable of running above a Data Link, Network, or Transport Layer**.
Such capability is available by protocol design, which defines and builds upon a Zenoh Session Protocol that provides abstractions for ordered best effort and reliable channels, different priorities and unlimited MTU.

Zenoh has minimal overhead, introducing only 4-6 bytes of overhead per data exchange. This is once again the result of careful design and protocol behavior as demonstrated in our previous blog post [1](https://zenoh.io/blog/2021-07-13-zenoh-performance-async/) [2](https://zenoh.io/blog/2022-06-09-zenoh-pico-above-and-beyond/).

Below, you can find the protocols currently supported by Zenoh. The modularity of our implementations allow us to easily add new underlying protocols. Check-out our [roadmap](https://github.com/eclipse-zenoh/roadmap) to see what is planned, and let us know if you have any transport you would like to see supported.

![stack](../../img/blog-zenoh-serial/stack.png)

![stack](../../img/blog-zenoh-serial/stack.png)

# Zenoh over Serial

Our latest addition to **Zenoh is the Serial Transport**. As you can imagine, by supporting serial we are unleashing the potential of Zenoh into a new set of devices that lack any other kind of networking interfaces (e.g., WiFi, Bluetooth, Ethernet). This is a common scenario, especially in robotics, vehicles, bus, and maritime/agricultural/industrial devices, where conventional computer network technologies are rarely used.

In the following, we present a quick how-to on Zenoh over Serial, where Serial-only devices are able to exchange data with other devices in the IP domain.

## Zenoh over Serial

For this how-to, you will need: a unix-based machine, a MbedOS device with serial capabilities, and a serial cable.

![setup](../../img/blog-zenoh-serial/setup.png)

![setup](../../img/blog-zenoh-serial/setup.png)

### Unix-based machine

`$ git clone -b api-changes https://github.com/eclipse-zenoh/zenoh
$ cd zenoh
$ cargo build --bin zenohd --example z_sub --no-default-features --features transport_tcp --features transport_serial`
`zenohd`
`$ RUST_LOG=debug ./target/debug/zenohd --no-multicast-scouting -l "serial//dev/tty.usbserial-0001#baudrate=115200" -l “tcp/127.0.0.1:7447”`
`/dev/tty.usbserial-0001`
`Zenoh Subscriber`
`$ ./target/debug/examples/z_sub -m client -e "tcp/127.0.0.1:7447"`

### MbedOS device (nucleo-f767zi)

`$ platformio init -b nucleo_f767zi --project-option "framework=mbed" --project-option "lib_deps=https://github.com/eclipse-zenoh/zenoh-pico#api-changes"`

Include the following code as your `src/main.cpp`:

`src/main.cpp`
`#include <mbed.h>
#include <EthernetInterface.h>
#include <randLIB.h>
extern "C" {
 #include <zenoh-pico.h>
}
#define MODE "client"
#define PEER "serial/110.105#baudrate=115200"
#define KEYEXPR "demo/example/zenoh-pico-pub"
#define VALUE "[MBedOS]{nucleo-F767ZI} Pub from Zenoh-Pico via Serial!"
int main(int argc, char **argv)
{
 randLIB_seed_random();
 // Initialize Zenoh Session and other parameters
 z_owned_config_t config = zp_config_default();
 zp_config_insert(z_config_loan(&config), Z_CONFIG_MODE_KEY, z_string_make(MODE));
zp_config_insert(z_config_loan(&config), Z_CONFIG_PEER_KEY, z_string_make(PEER));
 // Open Zenoh session
 printf("Open session!\n");
 z_owned_session_t s = z_open(z_config_move(&config));
 if (!z_session_check(&s)) {
 printf("Unable to open session!\n");
 while(1);
 }
 printf("OK\n");
 // Start the receive and the session lease loop for zenoh-pico
 zp_start_read_task(z_session_loan(&s));
 zp_start_lease_task(z_session_loan(&s));
 printf("Declaring publisher for '%s'...", KEYEXPR);
 z_owned_publisher_t pub = z_declare_publisher(z_session_loan(&s), z_keyexpr(KEYEXPR), NULL);
 if (!z_publisher_check(&pub)) {
 printf("Unable to declare publisher for key expression!\n");
 exit(-1);
 }
 printf("OK\n");
 char buf[6];
 for (int idx = 0; idx < 5; ++idx) {
 z_sleep_s(1);
 sprintf(buf, "[%4d]", idx);
 printf("Putting Data ('%s': '%s')...\n", KEYEXPR, buf);
 z_publisher_put_options_t options = z_publisher_put_options_default();
 options.encoding.prefix = Z_ENCODING_PREFIX_TEXT_PLAIN;
 z_publisher_put(z_publisher_loan(&pub), (const uint8_t *)buf, strlen(buf), &options);
 }
 printf("\nPreparing to send burst of 1000 messages. Start in 2 seconds...\n");
 z_sleep_s(2);
 for (int idx = 0; idx < 1000; ++idx) {
 sprintf(buf, "[%4d]", idx);
 printf(".");
 fflush(stdout);
 z_publisher_put_options_t options = z_publisher_put_options_default();
 options.encoding.prefix = Z_ENCODING_PREFIX_TEXT_PLAIN;
 z_publisher_put(z_publisher_loan(&pub), (const uint8_t *)buf, strlen(buf), &options);
 }
 printf("\n");
 printf("Closing Zenoh Session...");
 z_undeclare_publisher(z_publisher_move(&pub));
 // Stop the receive and the session lease loop for zenoh-pico
 zp_stop_read_task(z_session_loan(&s));
 zp_stop_lease_task(z_session_loan(&s));
 z_close(z_session_move(&s));
 printf("OK!\n");
 return 0;
}`

Build and upload your application to the board. Remember to set `Z_LINK_SERIAL=1` in `zenoh-pico/config.h`

`Z_LINK_SERIAL=1`
`zenoh-pico/config.h`
`$ platformio run -t upload`

Connect your serial cable to the board: `TX` and `RX` as pins `D1 (110)` and `D0 (105)`, respectively.
If you prefer to use a different pair of pins or to change the baud rate, you can do it by changing the Zenoh locator: `serial/110.105#baudrate=115200`

`TX`
`RX`
`D1 (110)`
`D0 (105)`
`serial/110.105#baudrate=115200`

### Demo

If everything goes well, you should have a similar output to the one below.

![zenoh-serial-demo](../../img/blog-zenoh-serial/zenoh-serial-demo.gif)

![zenoh-serial-demo](../../img/blog-zenoh-serial/zenoh-serial-demo.gif)

# Conclusion

**Zenoh is the most flexible stack available for decentralized data management** capable of supporting not only serial but able to run across several layers of the OSI model.

In summary, Zenoh paves the way for:

The support for Serial communication in Zenoh is an important milestone, as yet another and concrete proof of how Zenoh can operate across several layers of the OSI model. Thus, Zenoh meets the expectations of today’s applications and systems w.r.t. Robotic, embedded, and vehicular applications, where alternative buses are used instead of conventional computer network technologies.

In conclusion, this is yet another example of how **Zenoh makes available a holistic data management solution** for the whole Cloud-to-Things continuum.

[**–CG**](https://github.com/cguimaraes/)
[**–GB**](https://github.com/gabrik/)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2023-02-10-zenoh-flow/

Source: https://zenoh.io/blog/2023-02-10-zenoh-flow/

![](../../img/zenoh-dragon-bg-150x163.png)

# Data Flow programming with Zenoh-Flow

Blog Posts

# Data Flow programming with Zenoh-Flow

10 February 2023 -- Paris.

[Zenoh-Flow](https://github.com/eclipse-zenoh/zenoh-flow) was the concluding episode of Zenoh’s webinar series “Taming the Dragon” released recently and available on ZettaScale’s Youtube channel. In case you haven’t watched the webinar (which you should definitely do!), click [here](https://www.youtube.com/playlist?list=PLZDEtJusUvAY04pwmpY8uqCG5iQ7NgSrR)!
This blog provides additional insights about Zenoh-Flow: its origin, motivating use-cases, and upcoming features.

## Data Flow Programming

As we explained in our webinar, Zenoh-Flow is Zenoh’s native Data Flow Programming framework, offering a common abstraction applicable from the Data Center down to the microcontroller.

Data Flow Programming is not a new concept. The term was first coined by Jack B. Dennis and David P. Misunas in 1961 ([pdf](https://courses.cs.washington.edu/courses/cse548/11au/Dennis-Dataflow.pdf)) when they designed their data-flow processor. Gilles Kahn made another substantial contribution to the field in 1973 ([pdf](http://www1.cs.columbia.edu/~sedwards/papers/kahn1974semantics.pdf)) by formalizing the concept for parallel programming in general.

To summarize, Data Flow Programming is a programming paradigm in which applications are organized as a directed graph of nodes, where each node represents a computational unit and each arc a stream of data.

This programming model is at the foundation of many application domains, such as Analytics, Autonomous Driving and Robotics. For instance in these latter cases, we can find multiple sensors sending data to an object detection unit, which in turn sends its results to a path planning unit, which eventually sends commands to the engine of the robot or the autonomous car. There is a clear flow of data that goes from the sensors to the motors.

![Example of Data Flow inside a Robot](../../img/20230209-Blog-Zenoh-Flow/Data-flow_robot_camera_path-planning_engine.png)

Example of Data Flow inside a Robot

A complementary consideration is that applications are no longer contained to a single host or device, they span across the whole Cloud-to-Thing spectrum. We thus need to interconnect their different parts and preferably do so as transparently and efficiently as possible. Two properties where Zenoh really shines!

## Zenoh-Flow overview

Hence, based on this previous analysis, when designing Zenoh-Flow we wanted for it to:

To achieve these requirements, we center the development of a Zenoh-Flow application around two axis:

![Data Flow descriptor](../../img/20230209-Blog-Zenoh-Flow/Zenoh-Flow_Data-flow-descriptor.png)

Data Flow descriptor

![Zenoh-Flow Rust API](../../img/20230209-Blog-Zenoh-Flow/Zenoh-Flow_Rust-API.png)

Zenoh-Flow Rust API

![Zenoh-Flow Python API](../../img/20230209-Blog-Zenoh-Flow/Zenoh-Flow_Python-API.png)

Zenoh-Flow Python API

As illustrated above, Zenoh-Flow currently supports nodes written in Rust and Python.

Once in possession of the descriptors and the node implementations, our command line tool `zfctl` will allow you to deploy your application in one simple line:

`zfctl`
`$ zfctl launch my-flow.yaml`

That’s it!

Under the hood, a Zenoh-Flow runtime will parse this data flow descriptor and, together with all the runtimes involved, create the required connections as well as fire up the different nodes. All without requiring any (additional[1](#fn:1)) intervention from the user on the target devices.

As we mentioned performance earlier, let’s take a quick look at an optimisation Zenoh-Flow does transparently. Depending on the localisation of the nodes, different streams will be used to exchange data: if two nodes are located on the same runtime, a channel will be used instead of a Zenoh publisher / subscriber pair. This allows for lower latency as well as zero-copy.

Another noteworthy property of Zenoh-Flow is data isolation: a unique identifier is generated for each instance of a data flow which is then used to separate the publishers and subscribers. Each data flow will only receive the data it is supposed to. Notice that a lack of isolation, as is the case with some mainstream robotic frameworks, can induce unwanted communications which can then disrupt your application.

This illustrates how Zenoh-Flow allows users to focus on what matters most to them, their business logic. All the nitty gritty details, which are often a source of mistakes and frustrations, are handled by Zenoh-Flow.

## Example applications

If you want to try out Zenoh-Flow, we provide simple data flows in our example repository: a [Hello, world!](https://github.com/ZettaScaleLabs/zenoh-flow-examples/tree/0.4.x/getting-started) and a [Period miss detector](https://github.com/ZettaScaleLabs/zenoh-flow-examples/tree/0.4.x/period-miss-detector) that directly interact with Zenoh.

We also provide an implementation of the [Montblanc](https://github.com/ZettaScaleLabs/zenoh-flow-examples/tree/0.4.x/montblanc) testbed for robotics:

![Montblanc robotics testbed](../../img/20230209-Blog-Zenoh-Flow/Montblanc.png)

Montblanc robotics testbed

As one can see, Zenoh-Flow handles complex graphs. It also already provides several benefits:

Our main test application is a port of UC Berkeley’s [ERDOS - Pylot](https://github.com/erdos-project/pylot) autonomous driving pipeline, called [STUNT](https://github.com/ZettaScaleLabs/stunt). As it stands, STUNT uses the perfect perception: we receive the exact information of the car and its environment from the simulator and, based on these, we compute how much steering and acceleration to give. The data flow is as follow:

![STUNT Data Flow](../../img/20230209-Blog-Zenoh-Flow/Autonomous-driving-pipeline.png)

STUNT Data Flow

We then deployed it on our infrastructure and obtained the following recording:

![STUNT Perfect Perception recording](../../img/20230209-Blog-Zenoh-Flow/STUNT-short.gif)

Our first measurements show notable improvements in the execution time of the pipeline. A concrete consequence was that, to obtain the above video, we did not need to stop the simulator between each frame and wait for a command for the car. The pipeline was running in “real simulated time”.

The following figures show the execution time needed to perform different scenarios (pedestrian avoidance, slow car overtake, lane change) in their entirety. As one can see, the execution time with Zenoh-Flow is noticeably reduced. We want to slightly nuance these last results as they were obtained with earlier versions of both ERDOS and Zenoh-Flow.

![Evaluation of the Pedestrian avoidance scenario](../../img/20230209-Blog-Zenoh-Flow/Evaluation_Pedestrian-avoidance.png)

Pedestrian avoidance

![Evaluation of the Slow car overtake scenario](../../img/20230209-Blog-Zenoh-Flow/Evaluation_Slow-car-overtake.png)

Slow car overtake

![Evaluation of the Lane change scenario](../../img/20230209-Blog-Zenoh-Flow/Evaluation_Lane-change.png)

Lane change

## What is next for Zenoh-Flow?

Building on these promising results, here is what we have planned for Zenoh-Flow.

Our next step will be to further the integration with Zenoh. As shown in the examples, in order to subscribe (resp. publish) on a key expression a Source (resp. Sink) must be implemented. This tighter integration will provide a builtin implementation of a Source / Sink directly derived from the data flow descriptor.

Next, we plan to improve the developer experience: the ability to test nodes in isolation, better logging and error messages.

In the mid term, we want to (i) provide a marketplace API to favor the reuse of nodes and (ii) explore how to better orchestrate the execution of nodes to further improve the performance of Zenoh-Flow (but not only…!).

Having a marketplace would yield two main benefits: facilitating the reuse of nodes and removing the need to upload the nodes implementation where they should be deployed.

Better orchestrating the execution of the nodes is possible because Zenoh-Flow knows the flow of data in the application, before it is instantiated. Armed with this knowledge, we can leverage known scientific results to optimize the execution. What makes this even more interesting is that we believe it would unlock other uses: behavior trees are a field we are looking into!

We are also planning on having a graphical user interface to facilitate the creation of data flows. That’s however on a more long term plan and will be the object of a dedicated blog post!

We hope that this introduction to Zenoh-Flow has proven to be interesting and, as usual, if you want to give some feedback or interact with us, please use the links in the footer.

[**–The Zenoh Team**](https://github.com/orgs/eclipse-zenoh/people)

The current version of Zenoh-Flow requires you to upload, beforehand and on each device, the implementation of the nodes they will run. As we explain later, this is a constraint we are working on removing! [↩︎](#fnref:1)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2023-03-21-zenoh-vs-mqtt-kafka-dds/

Source: https://zenoh.io/blog/2023-03-21-zenoh-vs-mqtt-kafka-dds/

* [Home](../../)
* [Documentation](../../docs/getting-started/first-app/)
* [Use Cases](../../usecases/)
* [Community](../../community/)
* [Adopters](../../adopters/)
* [Media](../../media/)
* [Blog](../../blog/2025-12-11-zenoh-jiaolong/)

# Comparing the Performance of Zenoh, MQTT, Kafka, and DDS

# Comparing the Performance of Zenoh, MQTT, Kafka, and DDS

21 March 2023 -- Taipei.

### Prologue

This instalment features a blog contributed by a team of researchers from the prestigious [National Taiwan University (NTU)](https://www.ntu.edu.tw/english/). This team has been using Zenoh for some time in R2X and V2X R&D projects and recently did an interesting performance comparison between our blue dragon protocol, MQTT, Kafka and DDS. I’d like to thank the NTU team on behalf of the Zenoh community as this evaluation answers a couple of questions we are asked quite often.

– [kydos](https://github.com/kydos)

## Introduction

High performance has always been one of the main goals of Zenoh. While Zenoh's performance is provided for each release (see [here](https://zenoh.io/blog/2022-09-30-zenoh-bahamut/#improved-performance), [here](https://zenoh.io/blog/2022-04-14-rust-async-eval/), and [here](https://zenoh.io/blog/2021-07-13-zenoh-performance-async/)), so far there were no peformance evaluations that compared Zenoh with other technologies. Yet, this was a question commonly asked on Zenoh’s discord server and on github. In this blog, we’ll present an evaluation conducted by the [National Taiwan University](https://www.ntu.edu.tw/english/) where Zenoh's performance is compared with MQTT, Kafka, and DDS. A comprehensive version of this blog is available on [arXiv](https://arxiv.org/abs/2303.09419) to provide a detailed description and analysis for further study [1](#fn:1).

## Communication models

MQTT and Kafka adopt a brokered communication model where every message must go through a broker. Differently, DDS adopts a peer-to-peer communication model where messages are directly exchanged between publishers and subscribers without any middleman. Zenoh supports both the brokered and the peer-to-peer communication models, as well as a routed infrastructure mode. Fig. 1 illustrates the models with mixed topology, in which Mesh and Clique are peer-to-peer models. See the various [deployment models](https://zenoh.io/docs/getting-started/deployment/) for more insights. For a fair comparison with MQTT, Kafka, and DDS, both brokered and peer-to-peer modes are used in Zenoh.

![Topology offered by Zenoh](../../img/20230321-performance-comparison/topology.png)

Fig. 1 Topology offered by Zenoh

## Tested Performance Indicators

For this performance evaluation, we were interested in evaluating two key performance indicators, namely throughput and latency. Fig. 2 shows the communication diagram for the throughput measurements. For the comparison between Zenoh, MQTT, and Kafka, all the data flows through the “Broker” or the “Zenoh Router” to the subscriber. For the Zenoh peer mode and DDS tests, the data pass directly from the publisher to the subscriber.

![The configuration diagram for throughput tests](../../img/20230321-performance-comparison/throughput-configuration.png)

Fig. 2 The configuration diagram for throughput tests

Fig. 3 shows the communication diagram for the latency measurement. Similar to the throughput test, the message will be forwarded by the broker or the router for MQTT, Kafka, and the Zenoh client mode, and for the Zenoh peer mode and DDS, the data will be passed between the ping and pong nodes directly.

![The configuration diagram for latency tests](../../img/20230321-performance-comparison/latency-configuration.png)

Fig. 2 The configuration diagram for latency tests

## Testbed configuration

Two scenarios were prepared for the experiments: on a single machine and on multiple machines connected through Ethernet. For the multiple-machine scenario, the tested programs and the broker (or the Zenoh Router) will be run on different machines. Tab. 1 shows the configuration for each of the used machines.

Tab. 1 The configuration of the testing machines

| Type | Specification |
| --- | --- |
| OS | Ubuntu 20.04.3 LTS |
| CPU | AMD Ryzen 7 5800X running at a fixed frequency of 4.0 GHz 8-Core Processor, 16 threads |
| RAM | 32 GiB DDR4 3200MHz |
| Network | 100Gb Ethernet (for the multiple-machine scenario) |

The testing procedures are the same for all of Zenoh, DDS, MQTT, and Kafka. Their versions and settings are described below. The procedures were designed according to the suggestions from [the guide for accurate measurement](https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux). All the benchmark programs can be found under the [Zenoh performance test project](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison).

For Zenoh, the [test programs](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison/zenoh) use [version 0.7.0-rc](https://github.com/eclipse-zenoh/zenoh/tree/0.7.0-rc) and the Zenoh router `zenohd` can be built by following this [guide](https://github.com/eclipse-zenoh/zenoh#how-to-install-it). Its reliability was set to “reliable” and the congestion control option was set to “Block” on the publisher side. For the latency measurements, its reliability was set to “BestEffort” to align with the behavior of Kafka and MQTT.

For MQTT, the [test programs](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison/mqtt) use [Eclipse Mosquitto version 2.0.15](https://github.com/eclipse/mosquitto/archive/refs/tags/v2.0.15.tar.gz). The MQTT clients were implemented with the [Eclipse Paho MQTT C client library v.1.3.11](https://github.com/eclipse/paho.mqtt.c/releases/tag/v1.3.11). For all MQTT clients, the communication QoS level was set to 0 to achieve its best performance.

For Kafka, the [test programs](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison/kafka) use the [official broker 3.2.1](https://archive.apache.org/dist/kafka/3.2.1/kafka_2.13-3.2.1.tgz) and the

[rdkafka client library 0.28.0](https://github.com/fede1024/rust-rdkafka/tree/v0.28.0). The following parameters were chosen according to the suggestions from the [online documents](https://docs.confluent.io/cloud/current/client-apps/optimizing/index.html) and real experiments in order to get better results: linger.ms=0 and batch.size=400KB for throughput, 1 for latency; compression.type=none, acks=0 and fetch.min.bytes=1 (only for latency tests).

For DDS, the [test programs](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison/cyclonedds) use [Eclipse Cyclone DDS](https://github.com/eclipse-cyclonedds/cyclonedds) as the target implementation. They are based on the [official DDS examples](https://github.com/eclipse-cyclonedds/cyclonedds/tree/master/examples/roundtrip). For the reliability QoS, RELIABLE was employed. For the history QoS, while KEEP\_LAST was used in latency tests, KEEP\_ALL was selected for throughput tests.

## Throughput Comparison

In the throughput tests, the publisher program publishes messages back-to-back. The consumer program subscribed to the same topic collects a set of messages and calculates the message rate (msg/s). The procedure will be repeated multiple times for each payload size and the median number is selected from the samples as the result [1](#fn:1), in which outliers are excluded from the samples beyond 1st and 99th percentiles. The same procedure is applied to Zenoh, Cyclone DDS (briefly represented as DDS below), MQTT, and Kafka. The bitrates (bit/s) were also calculated based on the message rate and the payload size. In addition, the `iperf` utility was also used to measure the ideal data rate from the application layer between two peers. Various payload sizes from 8 bytes to 512 MB were tested to see the trend of the throughput. Note that in the charts below, the Y-axis is shown in the log scale for both the message rate and bitrate. The statistics data can be found [here](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison#numerical-results). Some of the numbers will be reported in the following paragraphs for discussion purposes.

![Throughput data in msg/s for the single-machine scenario](../../img/20230321-performance-comparison/plots/single/message_per_second.png)

Fig. 4 Throughput data in msg/s for the single-machine scenario

Fig. 4 shows the results for the single-machine scenario. From the figure, we can see that Zenoh can reach up to more than 4M msg/s for small payload sizes. Among the two lines for Zenoh, the peer mode (indicated by `Zenoh P2P`) provides better results than that of the client mode (marked by `Zenoh brokered`), because the data transmission doesn’t need to be relayed by the Zenoh router. DDS, although slower, is relatively close to Zenoh and can still reach up to 2M msg/s. Note that in the charts, the Y-axis is in the log scale.

As for Kafka, it maintains a stable message rate between 56K to 63K msg/s for payload sizes less than 2 KB and starts to decrease until the last data that was successfully measured at the payload size of 512 KB. On the other hand, MQTT has a slightly lower throughput between 33K to 38K msg/s before 32 KB of the payload size. However, it then starts to reduce drastically and shows the worst performance number, although it supports larger payload sizes compared to Kafka. However, Kafka in principle should be able to support more payload sizes. The reason behind the observed limitation is that the Kafka bindings we used failed on extending the message size over 1 MB.

![Throughput data in bit/s for the single-machine scenario](../../img/20230321-performance-comparison/plots/single/bit_per_second.png)

Fig. 5 Throughput data in bit/s for the single-machine scenario

Fig. 5 provides the throughput in bits-per-second (bit/s or bps). It shows that Zenoh starts to saturate toward the ideal throughput measured by `iperf` (at 76 Gpbs) for the payload size equal to or larger than 4 KB. The peer mode `Zenoh P2P` can reach up to 67 Gbps. For DDS, the highest throughput achieved is about 26 Gpbs. Kafka appears to saturate at about 4~5 Gbps when the payload size is larger than 16 KB. For MQTT, it reaches up to ~9 Gbps at the payload size of 32 KB. The performance degradation phenomenon of MQTT appeared in the tests consistently. The reason behind this is still unknown and will be worth further study in the future.

Overall, in this single-machine scenario, taking bitrate numbers for the throughput comparison, considering the best numbers obtained from Zenoh, DDS, Kafka, and MQTT, Zenoh peer mode achieves ~2x higher performance compared to that of DDS and 65x and 130x for Kafka and MQTT at the payload size of 8 bytes. Zenoh achieves peak performances at 8KB, achieving more than 4x throughput than DDS, 24x than Kafka, and 27x than MQTT. Finally, for a payload of 32 KB, Zenoh achieves more than 2x higher throughput than DDS, 5x than MQTT, and 10x than Kafka.

The throughput across multiple machines over a 100 Gb Ethernet is shown in Fig. 6 and Fig. 7. We will mainly focus on the bitrate results here.

![Throughput data in msg/s for the multiple-machine scenario](../../img/20230321-performance-comparison/plots/multi/message_per_second.png)

Fig. 6 Throughput data in msg/s for the multiple-machine scenario

![Throughput data in bit/s for the multiple-machine scenario](../../img/20230321-performance-comparison/plots/multi/bit_per_second.png)

Fig. 7 Throughput data in bit/s for the multiple-machine scenario

In the figure, `iperf` shows that the ideal throughput of the target network is 44 Gpbs. The maximal bitrate is about 34 Gbps for `Zenoh brokered` and 50 Gbps for `Zenoh P2P`, respectively. For Cyclone DDS, its throughput ranking remains at number three in the charts at 14 Gbps. On the other hand, MQTT's bitrates can reach up to ~9 Gbps at the payload size of 32 KB and then goes down, similar to the single-machine scenario. For Kafka, its best bitrate number is 5 Gbps, also at the payload size of 32 KB.

As a summary of the comparison, the results observed from the multiple-machine scenario maintain a similar performance trend to the single-machine results, showing that Zenoh outperforms DDS, Kafka, and MQTT by several to tens of performance improvements.

## Latency Comparison

In the latency tests, the `ping` program publishes the ping message, and the `pong` program replies with the same message upon receiving the ping. The tested payload size is fixed at 64 bytes (aligned with ICMP echo/reply), and the testing is performed in a back-to-back manner to reduce the impact of the process scheduling and the context switches induced by the underlying operating system. The latency is defined as half of the median round-trip time covering the ping and pong operations [1](#fn:1). Similarly, we remove the outliers beyond 1st and 99th percentiles. The statistics data can also be found [here](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison#numerical-results). Tab. 2 shows the results of the tests. The Linux `ping` utility was included as a baseline of the minimum latency that can be achieved.

Tab. 2 Latency data in µs (microseconds) for the single-machine and multiple-machine scenario

| Target | Single-machine | Multiple-machine |
| --- | --- | --- |
| Kafka | 73 | 81 |
| MQTT | 27 | 45 |
| Cyclone DDS | 8 | 37 |
| Zenoh brokered | 21 | 41 |
| Zenoh P2P | 10 | 16 |
| Zenoh-pico | 5 | 13 |
| ping | 1 | 7 |

For the single-machine environment, the ideal latency value obtained from `ping` is 1 µs. MQTT and Kafka have a latency of 73 µs and 27 µs, respectively. As for Zenoh, while the client mode `Zenoh brokered` has a latency of 21 µs, mainly due to routing data through a middleman, `Zenoh P2P` shows that it can be further reduced to 10 µs. For Cyclone DDS, the latency is even lower than Zenoh, achieving down to 8 µs. The reason is that it’s using UDP Multicast. Although Zenoh currently hasn’t implemented the same data transport yet, the microcontroller implementation of Zenoh – `Zenoh-pico` – has already realized this. As a result, we’ve also tested its latency and the result is 5 µs, as indicated by `Zenoh-pico`, which is even lower than that of Cyclone DDS, mainly because the Zenoh protocol and its implementation can be more lightweight and efficient than the OMG DDSI-RTPS protocol (implemented by all DDS-compliant implementations).

For the multiple-machine scenario over a real network with 100 Gb Ethernet, the latency for the `Zenoh brokered` is about 41 µs, and the number of `Zenoh P2P` for the peer mode is 16 µs, which is lower than that for Kafka at 81 µs, MQTT at 45 µs, and Cyclone DDS at 37 µs. For `Zenoh-pico`, it remains the best one at 13 µs, closest to the baseline obtained by the `ping` utility at 7 µs.

In general, the latency of Zenoh is low. Zenoh with the default peer-to-peer mode has the shortest latency compared to MQTT and Kafka (and DDS for the multiple-machine scenario). When the UDP Multicast transport is supported by Zenoh, as the result indicated by Zenoh-pico, it is expected that Zenoh can achieve the lowest number among all the software.

## Conclusion

In this blog, we compared the performance of Zenoh, MQTT, Kafka, and DDS. Zenoh consistently outperformed MQTT and Kafka. The results show that Zenoh is relatively closer to the ideal numbers obtained by the classic baseline tools `iperf` and `ping` for throughput and latency evaluation from the application layer, thanks to the low overhead design and multiple optimization techniques embedded in Zenoh’s implementation.

In our evaluation, Zenoh achieved up to **67** Gbps throughput on single-machine tests and **51** Gbps on multiple-machine tests with a 100 GbE network when the default peer mode was used. It can reach up to 1~2 orders of magnitude improvement on MQTT and Kafka and could double the throughput of DDS. One noticeable thing is that Cyclone DDS performed the best in the latency tests of the single-machine scenario, due to its use of the UDP multicast transport mechanism. However, when Zenoh-pico, the microcontroller implementation of Zenoh which has also realized the UDP multicast transport, is added to the comparison, it attains the lowest latency in all cases. This capability will later be supported by all Zenoh implementations.

Zenoh’s goal is to provide a next-generation communication framework with unparalleled performance and scalability. Besides being incredibly performant, Zenoh was also the technology featuring the simplest API and the shortest learning curve. We believe that Zenoh is the best choice for industrial, IoT, robotics, and automotive applications that can seamlessly support the cloud-to-edge and to-things continuum.

Hope you enjoyed it,

– [**William**](https://github.com/william-wyliang), [**Circle**](https://github.com/YuanYuYuan), and [**Jerry**](https://github.com/jerry73204)

---

1. Instead of displaying averaged numbers (with standard deviations) in the [arXiv](https://arxiv.org/abs/2303.09419) version, median values are used in this blog to increase the fairness of the comparison. [↩︎](#fnref:1) [↩︎](#fnref1:1) [↩︎](#fnref2:1)

**Next up**: [Data Flow programming with Zenoh-Flow](../../blog/2023-02-10-zenoh-flow/)

---

# https://zenoh.io/blog/2023-06-05-charmander2/

Source: https://zenoh.io/blog/2023-06-05-charmander2/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh Charmander Grows Stronger

Blog Posts

# Zenoh Charmander Grows Stronger

June 7th, 2023 -- Paris

The new [Zenoh](https://zenoh.io) Charmander 0.7.2-rc is out and comes with some aces up the sleeve! This patch release marks as stable the following APIs:

It introduces some new features:

It brings to life these experimental features:

And it also comes with a load of various bug fixes and improvements.

## C++ API

[Zenoh Charmander 0.7.0-rc](https://zenoh.io/blog/2023-01-10-zenoh-charmander/#c-bindings) introduced experimental support for [C++ bindings](https://zenoh.io/blog/2023-01-10-zenoh-charmander/#c-bindings), which are built on top of the Zenoh C API. This release introduces the support of [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico) in addition to the already supported [zenoh-c](https://github.com/eclipse-zenoh/zenoh-c). This means you can now write your Zenoh C++ application and run it on any embedded platform supported by [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico#zenoh-pico-native-c-library-for-constrained-devices)! You can check [here](https://github.com/eclipse-zenoh/zenoh-cpp#library-usage) how to set up zenoh-cpp as a library and switch between zenoh-c and zenoh-pico.

Moreover, this release finally provides the full coverage of the Zenoh stable API, including shared memory support (see [C](https://github.com/eclipse-zenoh/zenoh-c/blob/main/examples/z_pub_shm.c) and [C++](https://github.com/eclipse-zenoh/zenoh-cpp/blob/main/examples/zenohc/z_pub_shm.cxx) examples). The build for zenoh C/C++ projects was also made simpler and more flexible. Now zenoh-c, zenoh-pico and zenoh-cpp can be directly included into the parent CMake project without installation - see examples [here](https://github.com/eclipse-zenoh/zenoh-cpp/tree/main/examples/simple). The full set of C++ examples is available [here](https://github.com/eclipse-zenoh/zenoh-cpp/tree/main/examples/).

Stay tuned for an upcoming, detailed blog post on the C++ API that will be published shortly.

## Query payload

The [query payload API](https://zenoh.io/blog/2023-01-10-zenoh-charmander/#query-payload) has been marked stable and added to all Zenoh examples: in Rust ([get](https://github.com/eclipse-zenoh/zenoh/blob/eca888b410a0afb1df939393d4a304b7f926cd5e/examples/examples/z_get.rs#L32) and [queryable](https://github.com/eclipse-zenoh/zenoh/blob/eca888b410a0afb1df939393d4a304b7f926cd5e/examples/examples/z_queryable.rs#L49)), C ([get](https://github.com/eclipse-zenoh/zenoh-c/blob/2779f7ac470b1557e6fd8fd0ebfd04002ee8db2c/examples/z_get.c#L60) and [queryable](https://github.com/eclipse-zenoh/zenoh-c/blob/2779f7ac470b1557e6fd8fd0ebfd04002ee8db2c/examples/z_queryable.c#L32)), C++ ([get](https://github.com/eclipse-zenoh/zenoh-cpp/blob/81e1a69693bb45d4f23236d769ff4f4ad74ddddb/examples/universal/z_get.cxx#L62) and [queryable](https://github.com/eclipse-zenoh/zenoh-cpp/blob/81e1a69693bb45d4f23236d769ff4f4ad74ddddb/examples/universal/z_queryable.cxx#L75)), Python ([get](https://github.com/eclipse-zenoh/zenoh-python/blob/78a3902316f0e99d593ff7a2013ef920e637fa60/examples/z_get.py#L82) and [queryable](https://github.com/eclipse-zenoh/zenoh-python/blob/78a3902316f0e99d593ff7a2013ef920e637fa60/examples/z_queryable.py#L73)), and Zenoh-Pico ([get](https://github.com/eclipse-zenoh/zenoh-pico/blob/main/examples/unix/c11/z_get.c) and [queryable](https://github.com/eclipse-zenoh/zenoh-pico/blob/main/examples/unix/c11/z_queryable.c)). As a reminder, a query has now gained the possibility to carry some user payload that can be received and interpreted by the matching queryables. For example, you can now attach a picture to a query that is analyzed by a queryable running an object detection algorithm as shown in the figure below.

![Query payload](../../img/20230605-blog-zenoh-charmander2/zenoh-queryable-example.png)

## TLS updates

This release adds the support for [Let’s Encrypt](https://letsencrypt.org/) TLS certificates in Zenoh. More information on how to use it, for example to set up a Zenoh router in the cloud with TLS support can be found in this [dedicated blog post](https://zenoh.io/blog/2023-04-04-letsencrypt/).

Moreover, the TLS library used by Zenoh ([Rustls](https://www.memorysafety.org/blog/rustls-new-features/)) has finally added the support for TLS certificates based on IP addresses instead of DNS names. To test it out, it is enough to generate the TLS certificates according to [these instructions](https://zenoh.io/docs/manual/tls/#appendix-tls-certificates-creation).

![Letsencrypt validation](../../img/20230605-blog-zenoh-charmander2/zenoh-letsencrypt.png)

## S3 Backend updates

This release also includes some updates for the S3 backend. The first version of the plugin already provided many functionalities, such as the communication between Zenoh and AWS S3 servers, compatibility with MinIO S3 instances, and TLS communication. However we were missing timestamp handling on our side, which could lead to some edge case concurrency issues. In this release we handle this problem.

## Key Expression Trees and Formatters

With Zenoh 0.6, we introduced a new definition for Key Expressions (KE) to make them both faster and more predictable. Now introducing KeTrees and KeFormatters (Rust exclusive for now). A full blog post on both of these is coming soon, but in the meantime, here’s a quick sum-up.

KeTrees: it may be tempting to just put KE-value pairs into a hashmap and be done with it, but the reality is that you’re likely to lose the intersection/inclusion semantics of KEs when doing that. KeTrees are built to let you iterate on intersections between KEs as fast as possible.

`let mut tree = KeBoxTree::new();
tree.insert(keyexpr::new("a/b").unwrap(), 1);
tree.insert(keyexpr::new("a/c").unwrap(), 2);
tree.insert(keyexpr::new("b/c").unwrap(), 3);
let intersection = tree.intersection(keyexpr::new("a/**").unwrap());
// intersection is an iterator which will yield the nodes for "a",
// "a/b" and "a/c", which will have weights `None`, `Some(1)` and `Some(2)`
// respectively. The order isn't guaranteed.`

KeFormatters: because KEs are Zenoh’s address-space, they’re a fairly important thing for your team to manage correctly. You’re likely to end up defining your address space in a manner similar to REST APIs. KeFormatters are here to help you manage this in 3 steps:

`zenoh::kedefine!(pub temperatures: "factory/temperature/sensor/-/${factory:*}/${sensor:*}");`
`factory = “5/42”`
`let mut formatter = temperatures::formatter();
let ke = zenoh::keformat!(formatter, factory = 5, sensor = 42).unwrap();`
`let parsed = temperatures::parse(ke).unwrap();
assert_eq!(parsed.factory(), Ok("5"));
assert_eq!(parsed.sensor(), Ok("42"));`

## Transport protocol whitelisting

A new configuration option has been added in zenoh to allow only certain network protocols to be used by Zenoh. In order to understand what that means, we need to take a step back and see how Zenoh operates. Zenoh can work on various network protocols as shown in the figure below.

![Zenoh stack](../../img/20230605-blog-zenoh-charmander2/zenoh-stack.png)

Depending on the use case and requirements, certain protocols may be preferred to others. E.g., we would like to force all the Zenoh communication to happen on TLS, which provides encryption, and not on TCP, which is less secure. In normal operation, Zenoh will try to connect via any available means to the other Zenoh nodes (e.g. peer or router). I.e., if a node supports multiple protocols (e.g. TCP, UDP, TLS), it will try any of those until it succeeds. However, in some cases it would be nice to limit the protocols to be used.

Until this release, the only way to disable certain protocols was to build Zenoh and disable them at compile time. This is clearly a tedious and long process that force the user to multiple builds just to support different combinations of required protocols. What about this release then? The newly introduced transport protocol whitelisting is now possible to configure at deployment time which protocols to enable via the Zenoh configuration. No more rebuilds needed! The figure below shows an example of a Zenoh peer who has configured only TLS as protocol whitelist and it will fail to connect to a Zenoh peer only offering TCP connectivity.

![IP whitelisting](../../img/20230605-blog-zenoh-charmander2/zenoh-whitelist-ip.png)

Here below is an example of the configuration for the transport whitelisting.

`transport: {
link: {
/// An optional whitelist of protocols to be used for accepting and opening sessions.
/// If not configured, all the supported protocols are automatically whitelisted.
/// The supported protocols are: ["tcp" , "udp", "tls", "quic", "ws", "unixsock-stream"]
/// For example, to only enable "tls" and "quic":
protocols: ["tls", "quic"],
}
}`

## ROS1 bridge

[ROS1](https://wiki.ros.org) is a very popular meta-operating system for robotics. It consists of the main core (peer-to-peer message exchange primitives, environment, broker - “rosmaster”, interface definition tools, package system) and numerous packages and tools providing extra capabilities built on top of the core: HAL, device drivers, components and algorithms collection etc.

A typical ROS1 system is a set of services communicating through some closed network and performing on different levels: from low-level hardware control (servo motors, sensors) and up to some high-level functionality (autopiloting, telemetry collection, parameter tuning, remote control etc).

Despite the fact that ROS1 operates on a peer-to-peer network, it is not designed to be ultimately scalable and leaves a lot of scalability problems to be solved by the user. In this condition, we believe that bridging ROS1 systems to Zenoh could do the trick, allowing ROS1 users to utilize all power of Zenoh in their solutions.

[An alpha version of ROS1 to Zenoh bridge](https://github.com/eclipse-zenoh/zenoh-plugin-ros1) is introduced in this release. This bridge is quite similar to the ROS2 bridge, but it offers some limited functionality for ROS1 systems. An example integration is shown on the following schema:

![Zenoh & Ros1](../../img/20230605-blog-zenoh-charmander2/zenoh-ros1.png)

Capabilities:

ROS1 bridge has some limitations which, however, are planned to be completely eliminated in the nearest future:

## Liveliness support

This release introduces the *liveliness* feature. It allows any Zenoh application to assert and monitor the liveliness of any other Zenoh application in the network. Zenoh applications can declare liveliness tokens associated with some key expressions. Liveliness tokens will be seen as *alive* by other Zenoh applications while the Zenoh application that declared it is *alive*.

Zenoh applications can query alive tokens with the `get_liveliness` function and subscribe to liveliness changes (apparition/disappearance of liveliness tokens) with the `declare_liveliness_subscriber` function.
This feature is only available in the Rust API and is marked *unstable*: it works as intended but the API may change in the future. More details can be found [here](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Liveliness.md). Examples can be found [here](https://github.com/eclipse-zenoh/zenoh/blob/main/examples/examples/z_liveliness.rs), [here](https://github.com/eclipse-zenoh/zenoh/blob/main/examples/examples/z_get_liveliness.rs) and [here](https://github.com/eclipse-zenoh/zenoh/blob/main/examples/examples/z_sub_liveliness.rs).

`get_liveliness`
`declare_liveliness_subscriber`

## Compression (experimental)

An experimental transparent compression feature is added within this release, so far with promising results. The compression is performed hop to hop in the network, meaning that messages are compressed by the sending node and decompressed by the receiving node (a node being either a router, a client or a peer).

In order to enable the compression feature, Zenoh needs to be built enabling the “transparent\_compression” and the “unstable” feature. Beware that for the moment, every node on the network needs to be built with those features if we want to have compressed communication even on a single link of the network. In the future we plan to add automatic negotiation for compression to support different configurations.

In the configuration file we can enable or disable the compression as shown below:

`{
transport: {
link: {
compression: {
enabled: true,
},
},
},
}`

So far the metrics collected on a local environment show promising results. By running the [z\_pub\_thr & z\_sub\_thr tests](https://github.com/eclipse-zenoh/zenoh/tree/main/examples#z_pub_thr--z_sub_thr) (which allow us to measure the amount of messages sent per second through Zenoh) on a local environment composed of a Mac with an M2 processor, we see that even for a worst case scenario with batches containing high entropy payloads (resulting in a low compression rate), the amount of messages per second sent through the Zenoh network behaves as well as in the case compression is disabled.

![Average messages per second depending on their size with and without compression. (Apple M2 CPU)](../../img/20230605-blog-zenoh-charmander2/compressions_2.png)

However, it’s in terms of size that we notice the biggest difference. In the worst case scenario we end up sending batches with the same size as the original batch, while for a best case scenario (for low entropy batches with high compression rate) then the gain in size is huge! A 64KB batch is reduced to a couple hundred bytes.

![Sizes of compressed messages in bytes with high and low entropies, compared to non compressed ones.](../../img/20230605-blog-zenoh-charmander2/compressions_1.png)

Of course, in terms of entropy for the batches, in real life most of the time we will deal with something in between the best and worst case scenario. We can expect that the gain in size will not be as optimal as in the best case scenario but the transparent compression feature will cause a considerable gain anyway, reducing the bandwidth needed to send messages through the network.

# **What’s next?**

Are you ready to keep rocking with Zenoh?

![Zenoh rocks](../../img/20220930-blog-zenoh-bahamut/zenoh-on-fire.gif)

![Zenoh rocks](../../img/20220930-blog-zenoh-bahamut/zenoh-on-fire.gif)

These are the cool features you can expect for the months to come:

And many other cool things…

And don’t forget to stay in touch with the Zenoh team on [Discord](https://discord.gg/vSDSpqnbkm) and to propose new features on the [roadmap](https://github.com/eclipse-zenoh/roadmap/discussions).

[–The Zenoh Team](https://github.com/orgs/eclipse-zenoh/people)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2023-07-17-s3-backend/

Source: https://zenoh.io/blog/2023-07-17-s3-backend/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh Storage Gets a Boost: Empowering Storage with S3 Integration

Blog Posts

# Zenoh Storage Gets a Boost: Empowering Storage with S3 Integration

July 17th, 2023 -- Paris

As we happily announced on the blog post for the Zenoh 0.7.0-rc release ([Zenoh Charmander is coming to town](https://zenoh.io/blog/2023-01-10-zenoh-charmander/)), we now provide enhanced backend storage capabilities with the new AmazonS3/MinIO backend implementation.

This was a requested feature that originated within [our community on Discord](https://discord.gg/2GJ958VuHs) which soon made its way into the [roadmap](https://github.com/eclipse-zenoh/roadmap).

The S3 backend can be installed by downloading the package from ​​<https://download.eclipse.org/zenoh/zenoh-backend-s3/latest/>. The source code can be found in our eclipse-zenoh repository: <https://github.com/eclipse-zenoh/zenoh-backend-s3>. Inside you will find a README with detailed instructions on how to set up this backend for both Amazon S3 and MinIO.

### Contents

In this blog post we’ll go through the S3 backend, explaining what’s the conception behind a backend, how the S3 backend fits into it, how to configure it and what are some of its limits and considerations to take when using this backend.

**Table of contents:**

## Zenoh Backends

You may ask yourself “what is a backend?”. Well, in Zenoh a backend is a storage technology allowing to store the key/values publications made via Zenoh and return them on queries. Different storage technologies allow storing key/values based on different use cases.

At the moment we had three backend systems:

AmazonS3 joins this list with the capability of storing the data on a cloud storage service.

It will boost our storage capabilities, especially when it comes to object oriented storage. So far the only way to work with object storages was using the FileSystem backend which was designed to be a simple storage option constrained into the host’s filesystem. It is a backend that also lacks many of the mechanisms a cloud storage provides regarding security, data availability and performance, and is not very scalable either.

Our users needed the possibility to interact with an object storage technology that could easily be set up on the cloud, that would already provide performance, security and data availability and that could be scalable. Amazon S3 reunited all of these conditions and was immediately proposed, as up to today it’s been a proven technology with a broad adoption in the systems industry.

## Features

### S3 storage

[Amazon S3](https://aws.amazon.com/s3/) (which stands for Simple Storage Service) provides object storage capabilities through Amazon Web Services, offering “industry-leading scalability, data availability, security, and performance”.

This backend allows us to:

`\*`
`\*\*`
![S3 storage backend](../../img/20220922-blog-zenoh-charmander/s3.png)

### Compatibility with MinIO

[MinIO](http://min.io) is an open source multi-cloud object storage that offers high-performance and is an S3 compatible object storage. We developed the backend in order for you to be able to either choose AmazonS3 or MinIO depending on your use cases. There may be many factors for you to decide on one over the other. One to consider is the amount of interactions with the storage, as with Zenoh, you can receive thousands of requests to put or retrieve data from a storage, which can have an impact on the pricing of your storage in case of using Amazon S3.

### TLS support

AmazonS3 provides HTTPS support per se, but if you set up your own S3 instances using MinIO, you’ll probably want to secure the connection using TLS. For that you need to specify the certificates that will allow you to authenticate your servers. That certificate from the certificate authority can be specified in the configuration file.

## Configuration

The example configuration file below can also be found in [our repository](https://github.com/eclipse-zenoh/zenoh-backend-s3/blob/main/zenoh.json5). In it we have parameters for ‘volumes’ and ‘storages’.

`{
 "plugins": {
 "storage_manager": {
 "volumes": {
 "s3": {
 // This field is mandatory if you are going to communicate with an AWS S3 server and
 // optional in case you are working with a MinIO S3 server.
 "region": "eu-west-1",
 // Endpoint where the S3 server is located.
 // This parameter allows you to specify a custom endpoint when working with a MinIO S3
 // server.
 // This field is mandatory if you are working with a MinIO server and optional in case
 // you are working with an AWS S3 server as long as you specified the region, in which
 // case the endpoint will be resolved automatically.
 "url": "https://s3.eu-west-1.amazonaws.com",
 // Optional TLS specific parameters to enable HTTPS with MinIO. Configuration shared by
 // all the associated storages.
 "tls": {
 // Certificate authority to authenticate the server.
 "root_ca_certificate": "./certificates/minio/ca.pem"
 }
 }
 },
 "storages": {
 // Configuration of a "demo" storage using the S3 volume. Each storage is associated to a
 // single S3 bucket.
 "s3_storage": {
 // The key expression this storage will subscribes to
 "key_expr": "s3/example/*",
 // this prefix will be stripped from the received key when converting to database key.
 // i.e.: "demo/example/a/b" will be stored as "a/b"
 "strip_prefix": "s3/example",
 "volume": {
 // Id of the volume this storage is associated to
 "id": "s3",
 // Bucket to which this storage is associated to
 "bucket": "zenoh-bucket",
 // The storage attempts to create the bucket, but if the bucket already exists and is
 // owned by you, then with 'reuse_bucket' you can associate that preexisting bucket to
 // the storage, otherwise it will fail.
 "reuse_bucket": true,
 // If the storage is read only, it will only handle GET requests
 "read_only": false,
 // strategy on storage closure, either `destroy_bucket` or `do_nothing`
 "on_closure": "destroy_bucket",
 "private": {
 // Credentials for interacting with the S3 bucket
 "access_key": "AKIAIOSFODNN7EXAMPLE",
 "secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
 }
 }
 }
 }
 },
 // Optionally, add the REST plugin
 "rest": { "http_port": 8000 }
 }
}`

In our conception of what an S3 storage is, each storage is associated with an S3 bucket, while a volume is associated with a server. A volume can be associated with many storages, which means that all the s3 buckets are going to be stored on the same server.

The volume configuration required is limited to specifying where the server is going to be located (if you are using Amazon S3 you need to specify only the region, while when using MinIO you need to provide an url) and eventually the TLS certificate path. All the storages associated with it will share the same configuration.

Within the storage configuration, we specify the key expression, the name of the bucket, the credentials needed to access it, some policies related to the creation of the storage and its read-write permissions, etc… More detail is provided in the example config file.

## Considerations

Keep in mind that this S3 backend is still a work in progress and some extra work on it is to be expected.

There are a couple things to consider when using this backend at this stage, some related to how MinIO and AmazonS3 work and some related to the status of the development of this backend.

### Same name files and directories

Regarding the differences between MinIO and AmazonS3, MinIO is “S3 compatible”, which doesn’t mean it works identically.

One difference we noted during the development emerged from the question: what if we put a value under the key ‘a/b’ and later another one under `a/b/c`. With Zenoh one may expect this to be possible; Zenoh allows you to publish a value under `a/b/c` or under `a/b`, receivers subscribed to `a/\*\*` for instance should be able to receive both events, independently if the listener is a storage or not.

`a/b/c`
`a/b/c`
`a/b`
`a/\*\*`

So how does the system behave when dealing with this situation?

`└── a
├── b
│ └── c
└── b`

Performing a publication under `a/b` and later under `a/b/c` (or inversely) means we’ll have a directory with the same name as a file under the same location, under `/a`!  
MinIO doesn’t permit such a behavior and will throw an error message when attempting to perform such a thing. However, Amazon S3 doesn’t complain at all! That is because Amazon S3 uses a flat namespace to organize its files and directories, while MinIO uses the file system hierarchy for storing (see [this discussion](https://github.com/minio/minio/issues/7335) for more info). With file systems we can not have a file with the same name as a directory at the same place. We had in fact stumbled with this issue when developing the file system backend some time ago, and had to develop a mechanism to allow this behavior and store the values for both events. However on this new S3 backend, a mechanism for this is not implemented for the moment, so you need to keep that into consideration when using this backend alongside MinIO at this stage.

`a/b`
`a/b/c`
`/a`

### Sample timestamps

We are not yet taking into consideration the timestamps of the samples, this may cause problems in some edge cases, for instance in the case we send a PUT immediately followed by a DELETE on the same key expression, it may happen that the DELETE operation gets to the storage earlier than the PUT, which would cause a file to be kept stored instead of being removed as intended, due to order issues. Taking the timestamps into account would have allowed us in this example case to discard the PUT operation, avoiding to corrupt the storage. This is yet to be implemented and an [issue](https://github.com/eclipse-zenoh/zenoh-backend-s3/issues/5) is already opened for it.

### Replicas support

Replication is not yet supported from the Zenoh side. If we have two S3 backends subscribed to the same key expression and one goes momentarily down, when respawning it needs to fetch the data it missed from the other backend to synchronize. This is not yet implemented. We can, however, profit from the replication mechanisms both Amazon S3 and MinIO provide.

Another replication problem comes in when we want to have multiple but with different backends, for instance S3 and RocksDB. There is no workaround for this at the moment and it’s up to the user to manually take care of synchronization.

### Aws-sdk-s3 library

Finally, this implementation relies on Amazon’s [aws-sdk-s3 Rust crate](https://crates.io/crates/aws-sdk-s3), which is itself under development and clearly states: “*Please Note: The SDK is currently in Developer Preview and is intended strictly for feedback purposes only. Do not use this SDK for production workloads.*” So, you need to take that into strong consideration before making a production release.

As of today, the amazon’s engineering team that’s developing this crate is regularly publishing new versions of it. As a consequence, new versions of this backend are to be expected in the future in order to update the dependency versions.

# What’s next!

This concludes our post on how to use S3 as a storage for Zenoh thanks to our recent implementation of the S3 backend.

Although it’s a work in progress, this first version of it already provides us with many functionalities. We can:

There are nevertheless limitations we aim to tackle in the near future.

Stay tuned for updates and don’t forget to stay in touch with the Zenoh team on [Discord](https://discord.gg/vSDSpqnbkm) and to propose new features on the [roadmap](https://github.com/eclipse-zenoh/roadmap/discussions).

![Zenoh rocks](../../img/20220930-blog-zenoh-bahamut/zenoh-on-fire.gif)

![Zenoh rocks](../../img/20220930-blog-zenoh-bahamut/zenoh-on-fire.gif)

[–The Zenoh Team](https://github.com/orgs/eclipse-zenoh/people)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2023-10-03-zenoh-dragonite/

Source: https://zenoh.io/blog/2023-10-03-zenoh-dragonite/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh Dragonite Took Off!

Blog Posts

# Zenoh Dragonite Took Off!

October 3rd, 2023 -- Paris

We are happy to announce the release of Zenoh 0.10.0-rc **Dragonite**.

This version introduces new important features and improvements we have been working on the last couple of months. Specifically, this release introduces:

# The Best Pub/Sub/Query Protocol Gets Better!

![Zenoh Comic](../../img/20231003-blog-zenoh-dragonite/comic_august_2023.jpg)

With this release, Zenoh gets a series of protocol improvements and extensions, such as improved support for multicast and constrained devices. Additionally, some new mechanisms have been introduced to make it easier to add protocol extensions in the future without compromising backward compatibility.

These were the first batch of changes that will break wire-compatibility. We plan to have the second and final batch on the next release and then seal the protocol with a shiny 1.0 stamp !

# New Zenoh WireShark Plugin

![Zenoh Dissector](../../img/20231003-blog-zenoh-dragonite/zenoh-dissector.png)

Those of you that, like us, love dissecting protocols, will be pleased to learn that we have a new WireShark plugin for Zenoh – this new dissector is written in Rust!

The new [zenoh-dissector](https://github.com/ZettaScaleLabs/zenoh-dissector) makes it easier to spoof Zenoh packets and display them as human-readable messages. We also decided to change the implementation of the Wireshark plugin from Lua to Rust to reuse the codec defined in the Zenoh source code. Now, the parsing of Zenoh messages will be smoothly synchronized with any newer version of the Zenoh protocol! Moreover, the change gives us better performance and brings the potential to visualize more information in cooperation with Zenoh Rust library. Please give it a try, and any feedback is welcome!

# Zenoh Kotlin API

![Zenoh Kotlin](../../img/20231003-blog-zenoh-dragonite/zenoh-kotlin.png)

This release introduces Zenoh to the world of Kotlin, and viceversa ;-). The [Zenoh Kotlin API](https://github.com/eclipse-zenoh/zenoh-kotlin) targets the JVM environment and essentially opens the use of Zenoh to all the JVM-based programming languages.
In this alpha version, you’ll find most of Zenoh’s features. You’ll be able to publish, subscribe and query data.
Next we will be working on platform independent packaging and Android support.

Below is the [ZSub.kt example](https://github.com/eclipse-zenoh/zenoh-kotlin/blob/main/examples/src/main/kotlin/io.zenoh/ZSub.kt) that will be useful to briefly take a look at the Zenoh’s Kotlin API.
Here, we illustrate how to open a session, create a key expression, declare a subscriber (specifying some configuration parameters) and handle incoming samples – using the default channel handler with a coroutine.

`println("Opening session...")
Session.open().onSuccess { session -> session.use {
 "demo/example/**".intoKeyExpr().onSuccess { keyExpr ->
 println("Declaring Subscriber on '$keyExpr'...")
 session.declareSubscriber(keyExpr)
 .bestEffort()
 .res()
 .onSuccess { subscriber ->
 subscriber.use {
 runBlocking {
 val receiver = subscriber.receiver!!
 val iterator = receiver.iterator()
 while (iterator.hasNext()) {
 val sample = iterator.next()
 println(">> [Subscriber] Received ${sample.kind} ('${sample.keyExpr}': '${sample.value}')")
 }
 }
 }
 }
 }
 }
}`

For more information, checkout the [Kotlin API documentation](https://eclipse-zenoh.github.io/zenoh-kotlin/index.html).

# Support for Ultra Low-Latency

Although Zenoh is already capable of delivering very low latency – as low as 10 us (see [here](../../blog/2023-03-21-zenoh-vs-mqtt-kafka-dds/#latency-comparison)). We believe that we can do even better! This release introduces the experimental support for **ultra low latency** communication to address those applications that care about every single microsecond. For example, applications communicating over shared-memory will greatly benefit from it… and it will also be required for a new Zenoh’s high-performance SHM API we are cooking up.

The two experimental features we are introducing in Zenoh 0.10.0-rc to get to ultra low latency communication are:

In order to test it out, you need to compile Zenoh with `transport_unixpipe` feature and enable the `lowlatency profile`. For example, you can create a Zenoh configuration file (called `lowlatency.json5`) with the content below:

`transport_unixpipe`
`lowlatency profile`
`lowlatency.json5`
`// lowlatency.json5 Zenoh config file
{
transport: {
unicast: {
lowlatency: true, // enable low latency unicast transport
},
qos: {
enabled: false, // disable qos
},
},
}`

You can then build and run our latency examples (`z_ping` and `z_pong`) as follows:

`z_ping` 
 `z_pong`
`# build examples with 'transport_unixpipe' feature
cargo build --release -F transport_unixpipe --examples
cd target/release/examples
…
# run z_pong example
./z_pong --no-multicast-scouting -c lowlatency.json5 -l unixpipe/example_endpoint.pipe
…
# run z_ping example
./z_ping 64 --no-multicast-scouting -c lowlatency.json5 -e unixpipe/example_endpoint.pipe`

On our testing machine (AMD Ryzen 7 5800X with 32 GB of RAM), the newly introduced experimental features for ultra low latency support reduce latency of ~30% as shown in the table below.

| Protocol | 5th Percentile | Median | 95th Percentile |
| --- | --- | --- | --- |
| P2P, Y LowLat, Pipe | 6.0 | 7.0 | 9.0 |
| P2P, N LowLat, TCP | 10.0 | 10.0 | 11.0 |

Clearly, this is a first step for Zenoh and more is to be expected in the future!

# 

# ROS1 bridge

We are happy to announce that the ROS1 bridge, introduced in [Zenoh Charmander](../../blog/2023-06-05-charmander2/#ros1-bridge), has been released! To better understand how the ROS1 bridge works, let’s recall that any ROS1 system is centralized and contains one ROS1 Master service and a set of services called ROS1 Nodes. Each Node is capable of publishing, subscribing or querying some topics. ROS Master aggregates information about Nodes and their topics and provides a nameservice for Nodes to help them discover each other and establish direct connections when necessary. Those direct connections are used by Nodes to transport the actual topic data.

![Zenoh & Ros1](../../img/20231003-blog-zenoh-dragonite/zenoh-ros1.png)

Compared to the alpha version, we significantly improved algorithms that utilize ROS1 standard ROSXMLRPC APIs of ROS1 Master and Nodes to collect information on the local ROS1 system. This gives the bridge the capability to also preserve topic data types and md5 signatures. Now ROS1 Bridge carefully probes all entities of the local ROS1 system to keep the information up-to-date, trying to apply caching when possible to reduce the costs of its operation.

Another significant change is the new fine-grained bridging mode config. Now users can specify bridging policy (Auto\Lazy\Disabled) both globally and for specific ROS1 topics.

As a result, the bridge is capable to expose ROS1 topics for publishers, subscribers, services and clients into Zenoh network as a set of Zenoh publishers, subscribers, queryables and queries, providing ROS1 system all set of Zenoh features, like highly-efficient and flexible network operation, storage-based data caching, etc. Moreover, multiple ROS1 systems bridged into one Zenoh network are capable of seeing each other and interact seamlessly.

ROS1 to Zenoh Bridge aims to be completely transparent, making interaction with remote ROS1 topics as if they were local. The integration to any existing ROS1 system does not require its tuning, recompilation etc (of course, if its application logic won’t get mad of seeing remote ROS1 topics in its environment :) ).

To test a new bridge, please try the following:

`# To run this example, you should have ROS1 locally installed….
# build the bridge from source
cargo build
cd target/debug/
# terminal 1:
rosmaster -p 10000
# terminal 2:
rosmaster -p 10001
# terminal 3:
./zenoh-bridge-ros1 --ros_master_uri http://localhost:10000
# terminal 4:
./zenoh-bridge-ros1 --ros_master_uri http://localhost:10001
# terminal 5:
ROS_MASTER_URI=http://localhost:10000 rostopic pub /topic std_msgs/String -r 1 test_message
# terminal 6:
ROS_MASTER_URI=http://localhost:10001 rostopic echo /topic`

As the result, you will see the topic `/topic` bridged from one ROS1 system to another:

`/topic`
![Ros1 Topics](../../img/20231003-blog-zenoh-dragonite/ros-topics.png)

# C++ Documentation & API changes

An important step has been taken for the Zenoh C++ library with the publishing of the documentation, now available at [https://zenoh-cpp.readthedocs.io](https://zenoh-cpp.readthedocs.io/).

Several API changes have been made in the C++ API. The most significant change is related to closures. They now accept parameters by reference instead of pointers:

`session.declare_subscriber("foo/bar", [](const Sample& sample) {
 // No need to check for nullptr anymore; the code is safe
 std::cout << sample.get_payload().as_string_view() << std::endl;
});`

The use of `nullptr` had a special meaning before; it signaled that the data stream is closed. This can now be handled with an optional drop handler:

`nullptr`
`auto on_reply = [](Reply &&reply) {
 // Process the data
};
auto on_done = []() {
 // Finish data processing
};
GetOptions opts;
opts.set_target(Z_QUERY_TARGET_ALL);
session.get("foo/bar", "", {on_reply, on_done}, opts);`

Another change is related to the handling of key expressions, which differs between Zenoh-C and Zenoh-Pico. In the case of Zenoh-Pico, the `KeyExpr` object is unaware of its string representation if it is declared with `Session::declare_keyexpr`. So a perfectly valid `KeyExpr` object returns incorrect results from its `equals`, `includes`, and `intersects` operations. To avoid such unexpected errors, these operations without explicit error handling have been disabled for Zenoh-Pico. Instead, `Session::keyexp_equals`, `Session::keyexpr_intersects`, and `Session::keyexpr_includes` have been added. For more details, checkout the [KeyExpr documentation](https://zenoh-cpp.readthedocs.io/en/latest/keyexpr.html).

`KeyExpr`
`Session::declare_keyexpr`
`KeyExpr`
`equals`
`includes`
`intersects`
`Session::keyexp_equals`
`Session::keyexpr_intersects`
`Session::keyexpr_includes`

Large cleanup of warnings was performed: now Zenoh C++ can be compiled with the strictest warning level (see the related [issue](https://github.com/eclipse-zenoh/zenoh-cpp/issues/71)).

# What’s next?

Developing Zenoh is an amazing part of our journey on this beautifully blue planet. This release represents another step forward in our goal to provide the community with a blazingly fast, decentralized and scalable Pub/Sub/Query protocol, with an ecosystem allowing us to have Zenoh running on a multitude of environments that span from robotics to autonomous driving vehicles and more!

Many more things are yet to come!

You can take part in this process by joining our community on [Discord](https://discord.com/invite/vSDSpqnbkm). There you will be able to chat with us as well as with other members of the community, discuss features on the roadmap, and more.

![Guitar](../../img/20231003-blog-zenoh-dragonite/zenoh-on-fire.gif)

![Guitar](../../img/20231003-blog-zenoh-dragonite/zenoh-on-fire.gif)

—

The Zenoh Team

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2024-01-31-zenoh-flow-getting-started/

Source: https://zenoh.io/blog/2024-01-31-zenoh-flow-getting-started/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh-Flow 0.6.0-rc: Getting Started

Blog Posts

# Zenoh-Flow 0.6.0-rc: Getting Started

31 January 2024 -- Paris.

At ZettaScale, we are developing a next-generation middleware called [Zenoh](https://zenoh.io/docs/getting-started/first-app/). Zenoh gained a lot of traction with very positive feedback from diverse industries, including Robotics, Industrial Automation, Automotive and more. If you haven’t tried it yet and you think it could help you, don’t hesitate, we guarantee it’s easy and worth your time!

This blog post will focus on another exciting project we are building: Zenoh-Flow. As its name indicates, Zenoh-Flow brings together the control of data flow programming and the power of Zenoh. Think of distributed applications where you don’t have to know the exact location of your computing units, but simply agree on the name (and type) of the resources they are going to exchange, how they are connected and, if needed, the properties of the host(s) on which they are going to run. Add to this list a validation step, uniquely named resources, great performance and you would start to have a good idea of what Zenoh-Flow has to offer!

Let us dive in!

![Data Flow descriptor](../../img/20240131-Zenoh-Flow-Getting-Started/zf-getting-started.png)

# Zenoh-Flow 0.6.0-rc: Getting Started

`blog-post-31-01-2024`
`git clone https://github.com/eclipse-zenoh/zenoh-flow --branch blog-post-31-01-2024 --depth 1`

To facilitate the discovery of Zenoh-Flow we have included in the repository an example data flow called “getting started”. Similar to the very first program you write in every programming language, its purpose is to print a sentence akin to “Hello, world!”. However, as we are building a data flow and using Zenoh, we have to introduce slightly more logic and we have to make our flow interact via Zenoh.

Hence, our getting started will subscribe to the resource `zf/getting-started/hello` — a Source — in the hope of receiving names, then it will forward this name to a node that will generate a greeting — an Operator — and finally forward the generated greeting to be both published on Zenoh, on the resource `zf/getting-started/greeting`, and written to a file — two Sinks.

`zf/getting-started/hello`
`zf/getting-started/greeting`

This flow is already written in the file: `zenoh-flow/examples/flows/getting-started.yaml`.

`zenoh-flow/examples/flows/getting-started.yaml`

## Data Flow Descriptor

`name: getting-started`

**[Required]** We start with the name of the data flow. It is a human-readable summary of what your data flow will do. Zenoh-Flow will use it when displaying information regarding its status.

`vars:
 TARGET_DIR: "/home/zettascale/zenoh-flow/target"
 BUILD: "debug"
 DLL_EXTENSION: "so"`

**[Optional]** The “variables” section. They allow performing text replacements inside a descriptor and any of its nested descriptor(s) before your data flow is processed by Zenoh-Flow. This is useful if, for instance, you regularly switch between machines with different paths, operating system and build.

To indicate that you are using one such variable in your descriptor, you have to escape it between “moustaches” like so: `{{ TARGET_DIR }}`.

`{{ TARGET_DIR }}`

The standalone Zenoh-Flow runtime and daemon allow to change these variables through a command line argument if you want to manipulate them in scripts.

`sources:
 - id: zenoh-sub
 description: The Source receiving the names
 zenoh-subscribers:
 hello: "zf/getting-started/hello"`

**[Required]** The sources section lists all the nodes that feed data to your data flow. Sensors or “events” (e.g. a publication on a Zenoh resource) are good examples. Without sources a data flow can never process data as it will never receive any.

The `id` has to be unique within your data flow. The same applies to other nodes.

`id`

This source is a specific built-in Zenoh-Flow provides, it is a Zenoh subscriber. It is ready to be used inside any data flow and simply expects a `description` and an association list `port-id: key-expression`.

`description`
`port-id: key-expression`

The `port-id` has to be unique within the `zenoh-subscribers` subsection. More specifically, a `port-id` has to be unique per node and per port type (i.e. input or output). Which means the same `port-id` can be repeated between different nodes and within the same node as long as it applies to different port types. Here the zenoh-subscribers map to outputs.

`port-id`
`zenoh-subscribers`
`port-id`
`port-id`

Regular Zenoh-Flow sources (i.e. where you have to provide an implementation) follow the same structure as operators with the only exception that a source does not have an `inputs` subsection.

`inputs`
`operators:
 - id: greetings-maker
 description: "This node will create the greeting, transforming for instance 'John' to: 'Hello, John!'"
 library: "file://{{ TARGET_DIR }}/{{ BUILD }}/examples/libgreetings_maker.{{ DLL_EXTENSION }}"
 inputs:
 - name
 outputs:
 - greeting`

**[Required]** The operators section lists all the nodes that manipulate data. They receive data in their `inputs`, manipulate them, and send the results in their `outputs`.

`inputs`
`outputs`

The `library` subsection points to the shared library where the implementation resides. For now, only the `file://` schema is supported which means that the path has to be valid *on the machine where the operator will run*.

`library`
`file://`
`sinks:
 - id: file-writer
 configuration:
 file: "/tmp/greetings.txt"
 library: "file://{{ TARGET_DIR }}/{{ BUILD }}/examples/libfile_writer.{{ DLL_EXTENSION }}"
 description: "This Sink will write the greetings in a temporary file."
 inputs:
 - in
 - id: zenoh-writer
 description: The Sink publishing the result of the processing
 zenoh-publishers:
 greeting: "zf/getting-started/greeting"`

**[Required]** The sinks section lists all the nodes that will send the results of the data flow processing to the outside. In this particular example we have two sinks: the sink `file-writer` writes the result in the file
`/tmp/greetings.txt` and the sink zenoh-writer publishes it on Zenoh on the resource `zf/getting-started/greeting`.

`file-writer`
`/tmp/greetings.txt`
`zf/getting-started/greeting`

Note that the sink `file-writer` has a `configuration` subsection. This subsection allows passing the values declared there to your node when Zenoh-Flow creates it. This is useful if you want to change the behaviour of your node without having to recompile it or if you want to reuse the same node several times with just a tweak in its parameters.

`file-writer`
`configuration`

Any node can have this subsection (expect builtin Zenoh nodes). It can also appear at the data flow level if all your nodes share a common configuration subset, such that you do not have to repeat it. Similar to the `vars` sections, a global `configuration` section is propagated to nested descriptors.

`vars`
`configuration`
`links:
 - from:
 node: zenoh-sub
 output: hello
 to:
 node: greetings-maker
 input: name
 - from:
 node: greetings-maker
 output: greeting
 to:
 node: file-writer
 input: in
 - from:
 node: greetings-maker
 output: greeting
 to:
 node: zenoh-writer
 input: greeting`

**[Required]** The links section details how your nodes are connected. Its verbose format is there to ensure that your links are *valid*.

Zenoh-Flow will guarantee several crucial properties regarding these links and your data flow:

There is a last optional section, the `mapping`, that we did not include in this descriptor. We will detail why and its contents when we will explain how to launch this data flow.

`mapping`

At this point you should have a better grasp of how a data flow in Zenoh-Flow is structured. One point that should be clarified before we can launch it is how to write the logic of a node.

## Node Implementation

We are going to detail the code located in the `greetings-maker` operator as an Operator is the only node that has both inputs and outputs. We will point out the small differences, when compared to a Source or a Sink, throughout the explanation.

`greetings-maker`

The code we describe is located in: `zenoh-flow/examples/examples/greetings-maker/src/lib.rs`.

`zenoh-flow/examples/examples/greetings-maker/src/lib.rs`
`use prost::Message as pMessage;
use zenoh_flow_nodes::prelude::*;`

The first line imports the `Message` trait from the Rust implementation of Protobuf. Protobuf is a serialization / deserialization library that works across programming languages. This will allow us to tell Zenoh-Flow how to deserialize / serialize the data we receive / send — if needed!

`Message`

On a technical note, we have to rename it as we are also defining a `Message` structure in Zenoh-Flow.

`Message`

The second line imports everything you need to write an Operator from the `zenoh-flow-nodes` crate.

`zenoh-flow-nodes`
`#[export_operator]
pub struct GreetingsMaker {
 input: Input<String>,
 output: Output<String>,
}`

This snippet creates a structure called `GreetingsMaker` that has one input and one output, both of type `String`. Inputs and Outputs in Zenoh-Flow can be typed to facilitate data manipulation: once you tell Zenoh-Flow how to perform the deserialisation / serialisation, it will do it automatically when needed.

`GreetingsMaker`
`String`

The `#[export_operator]` procedural macro on top of the structure is to expose the correct symbols such that Zenoh-Flow can dynamically load your shared library. This is a required step and we feel leveraging a macro is the easiest way to get it right for developers.

`#[export_operator]`
`#[export_sink]`
`#[export_source]`
`#[async_trait::async_trait]
impl Operator for GreetingsMaker {
 async fn new(
 _context: Context,
 _configuration: Configuration,
 mut inputs: Inputs,
 mut outputs: Outputs,
 ) -> Result<Self> {
 Ok(GreetingsMaker {
 input: inputs
 .take("name")
 .expect("No input 'name' found")
 // NOTE: the method `take` returns an `InputBuilder` and the method `typed`
 // creates a typed Input.
 .typed(|bytes| String::from_utf8(bytes.into()).map_err(|e| anyhow!(e))),
 output: outputs
 .take("greeting")
 .expect("No output 'greeting' found")
 // NOTE: similarly, the method `take` returns an `OutputBuilder` and the
 // method `typed` creates a typed Output.
 .typed(|buffer, data: &String| data.encode(buffer).map_err(|e| anyhow!(e))),
 })
 }
}`

This snippet tells how Zenoh-Flow can create an instance of your Operator. We require you to implement the `Operator` trait that consists of a single asynchronous function: `new`.

`Operator`
`new`

It’s arguments are:

`_context`
`_configuration`
`key`
`value`
`serde_json::Value`
`inputs`
`typed`
`outputs`
`inputs`

The procedural macro `#[async_trait::async_trait]` is to allow for the definition and usage of asynchronous method in traits.

`#[async_trait::async_trait]`
`#[async_trait::async_trait]
impl Node for GreetingsMaker {
 async fn iteration(&self) -> Result<()> {
 let (message, _) = self.input.recv().await?;
 if let Message::Data(characters) = message {
 let name = characters.trim_end();
 let greetings = match name {
 "Sofia" | "Leonardo" => format!("Ciao, {}!\n", name),
 "Lucia" | "Martin" => format!("¡Hola, {}!\n", name),
 "Jade" | "Gabriel" => format!("Bonjour, {} !\n", name),
 _ => format!("Hello, {}!\n", name),
 };
 return self.output.send(greetings, None).await;
 }
 Ok(())
 }
}`

The last part of the implementation of our Operator is the `Node` trait and its method `iteration`. This method is what Zenoh-Flow will call, in a loop, until you decide to stop your data flow (or if an unfortunate event happens).

`Node`
`iteration`

As the signature of the method indicates, this method takes an immutable reference to your operator’s instance. If you want to persist state, then you need to leverage the [interior mutability pattern](https://doc.rust-lang.org/reference/interior-mutability.html). This is a design choice of Zenoh-Flow: providing a mutable reference would hinder the performance of all nodes, even those that do not need to mutate it.

If an iteration returns an error, Zenoh-Flow will log it and resume the execution of your operator. Speaking of execution, let us briefly explain how Zenoh-Flow drives the execution of a data flow.

## Execution Model: Data-Driven

In version `0.6.0-rc` and the previous ones, Zenoh-Flow supports a single execution model: data-driven. This model is relatively simple: each node runs in its own task and is driven by its I/O operations. If there is no available input then the node will be parked by the executor, only to be woken up when data has been received.

`0.6.0-rc`

The following line from the Operator implementation is a perfect example:

`let (message, _) = self.input.recv().await?;`

The `await` keyword in Rust indicates asynchronous events where the executor can park the node.

`await`

We already have implemented another execution model and are working on a second one that we keep for the following minor release of Zenoh-Flow, stay tuned! As a form of teaser, these other execution models offer more control than the data-driven one which in turn leads to (much) better performance.

Now that we have seen how to define a data flow, how to implement an Operator and how Zenoh-Flow drives the execution of the nodes, the next step is to launch your first flow!

## Launching a Data Flow

Zenoh-Flow provides two ways of starting a data flow: via a standalone runtime or via a daemon (and its associated command line tool `zfctl`).

`zfctl`

The standalone runtime will only run a single data flow and will only deploy nodes on the machine on which it is started. We believe it is beneficial for prototyping or realising benchmarks.

We offer two flavours of the daemon: a standalone daemon and a plugin for Zenoh. Both offer the exact same functionalities with the difference that the standalone daemon does not require you to start and configure a Zenoh router. We recommend using the daemon when you need to deploy a data flow on several Zenoh-Flow runtimes. Our daemon and command line tool have been designed to help you in this specific scenario, automating the deployment as much as possible.

Running the example requires first to compile the example we want to run:

`# We are assuming that you are at the root of the Zenoh-Flow directory.
cargo build --examples`

### With the Standalone Runtime

Compile the executable (if you want a release profile, add `--release`) to the command below:

`--release`
`cargo build -p zenoh-flow-standalone-runtime`

Simply launch the following command and you are set:

`./target/debug/zenoh-flow-standalone-runtime ./examples/flows/getting-started.yaml`

If you want to modify some of the variables in the vars section of the data flow you can execute instead:

`./target/debug/zenoh-flow-standalone-runtime \
 # macOS
 --vars DLL=dylib \
 # release build instead of debug
 --vars BUILD=release \
 ./examples/flows/getting-started.yaml`

Fire up a Zenoh subscriber and / or launch `tail` on the file /tmp/greetings.txt to see the results:

`tail`
`# In a first shell
z_sub -k "zf/getting-started/greeting"
# (optional) In a second shell
tail -f /tmp/greetings.txt
# In another shell
z_put -k "zf/getting-started/hello" -v "Alice"
# You should see "Hello, Alice!".`

### With the Standalone Daemon

Running a data flow on a daemon requires slightly more preparatory work.

First we need to compile the executable we need:

`cargo build -p zenoh-flow-standalone-daemon -p zfctl`

We then need to start the standalone daemon:

`./target/debug/zenoh-flow-standalone-daemon my-first-daemon`

You should see something along the lines of:

The id is the unique identifier of the Zenoh-Flow runtime contained within your daemon called “my-first-daemon”. This id is important if you want to control where the different nodes composing your data flow will run. As we mentioned earlier when we described the different sections of a data flow descriptor, there is an optional section `mapping`.

`mapping`

The section `mapping` allows defining on which Zenoh-Flow runtime a node should run. For instance, the snippet below tells Zenoh-Flow to launch all nodes on the runtime of our daemon “my-first-daemon”.

`mapping`
`mapping:
 92af6ef5bdab227a95993f3f73cb9f6e:
 - zenoh-sub
 - greetings-maker
 - zenoh-writer
 - file-writer`

If a node is omitted, Zenoh-Flow will default to launching it on the runtime that was contacted. How to choose which Zenoh-Flow runtime to contact? Our command line tool `zfctl` lets you specify the unique identifier of a runtime or selects one randomly for you if you don’t specify one.

`zfctl`

If you want to list all the available Zenoh-Flow daemon on your network you can use zfctl `like` so:

`like`
`./target/debug/zfctl runtime list`

Hence, assuming there is only one Zenoh-Flow daemon running on your network, the two commands below are equivalent and both create an instance of the data flow “getting-started”:

`./target/debug/zfctl instance create ./examples/flows/getting-started.yaml
# is equivalent to:
./target/debug/zfctl instance --runtime 92af6ef5bdab227a95993f3f73cb9f6e create ./examples/flows/getting-started.yaml`

You should then see the *unique identifier* of the instance of this data flow echoed in the logs. Note it down, as if the creation is successful, this is through this identifier that you can manage it.

We have to make two comments regarding this last sentence:

If we assume that the data flow was successfully created and its unique identifier is `d392a6b5-b284-4d26-96c4-35372d860978` then to start it, on all runtimes, one should enter:

`d392a6b5-b284-4d26-96c4-35372d860978`
`./target/debug/zfctl instance start d392a6b5-b284-4d26-96c4-35372d860978`

Just like with the standalone runtime, enter the following commands on different shells to confirm that the data flow is executed correctly:

`# In a first shell
z_sub -k "zf/getting-started/greeting"
# (optional) In a second shell
tail -f /tmp/greetings.txt
# In another shell
z_put -k "zf/getting-started/hello" -v "Bob"
# You should see "Hello, Bob!".`

## Conclusion

This blog gave you an overview of how to write your first data flow using the Zenoh-Flow framework. We have seen the different sections that compose a data flow descriptor, we have seen what is required to write an Operator, how Zenoh-Flow is (for now!) a data-driven framework and, lastly, how to start your data flow with either the standalone runtime or via a daemon.

As we have indicated at few occasions, we are still in the process of polishing minor aspects and will update the blog post as soon as the `0.6.0-rc` version is released. We are also working (among other exciting features!) on other execution models that we will progressively unroll with other minor releases of Zenoh-Flow. The first one, *guided execution*, will come with version `0.6.1-rc` and will be the object of a dedicated blog!

`0.6.0-rc`
`0.6.1-rc`

Until then, happy coding!

[**– Julien Loudet for the Zenoh team**](https://github.com/orgs/eclipse-zenoh/people)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2024-04-17-datadog-zenoh-router-integration/

Source: https://zenoh.io/blog/2024-04-17-datadog-zenoh-router-integration/

![](../../img/zenoh-dragon-bg-150x163.png)

# Streamlining Zenoh router Monitoring with Datadog Integration

Blog Posts

# Streamlining Zenoh router Monitoring with Datadog Integration

April 17th, 2024 -- Paris.

![Integration Dashboard](../../img/20240417-Datadog-Zenoh-Router-Integration/1-dashboard.png)

## Unlocking Insights, Enhancing Efficiency

Today, we’re excited to introduce a powerful integration that greatly improves the monitoring experience for [Zenoh](https://zenoh.io/) users. While Zenoh has always prioritized efficiency and performance, our [Datadog integration](https://docs.datadoghq.com/integrations/zenoh_router/) brings a new dimension of visibility and insight to Zenoh deployments. By seamlessly integrating with Datadog, users can now monitor the state of their Zenoh routers with unprecedented ease and efficiency.

## Empowering Zenoh Users

The Zenoh Team understands the importance of providing users with the tools they need to manage their distributed systems effectively. With this integration, we’re empowering Zenoh users to gain valuable insights into router performance, network dynamics, and system health without sacrificing efficiency. By leveraging the robust monitoring capabilities of Datadog, users can optimize their Zenoh deployments with confidence.

## A Tailored Solution for Cloud Environments

For users operating in cloud environments, the Zenoh router Datadog integration offers tailored monitoring solutions that streamline operations and enhance visibility. By seamlessly integrating with Datadog’s cloud monitoring platform, users can easily monitor the state of their Zenoh routers in real time, allowing for proactive management and optimization of cloud-based deployments.

## Key Features of the Integration:

## How It Works

The Zenoh router integration for Datadog is implemented as an agent plugin that collects relevant metrics and status information from Zenoh routers and sends them to the Datadog platform. Users can then visualize and analyze this data using Datadog’s intuitive dashboarding and querying capabilities.

![Datadog Agent Overview](../../img/20240417-Datadog-Zenoh-Router-Integration/2-agent.png)

## Getting Started

To start monitoring Zenoh routers with Datadog, simply install the [Zenoh router integration plugin](https://docs.datadoghq.com/integrations/zenoh_router/) on your Datadog agent, configure it with the necessary connection details, and start exploring the metrics and status information available in Datadog.

![Integration Tile](../../img/20240417-Datadog-Zenoh-Router-Integration/3-integration-tile.png)
`> datadog-agent integration install -t datadog-zenoh_router==1.0.0`
`/etc/datadog-agent/conf.d/zenoh_router.d/conf.yaml`
`init_config:
instances:
 -
 min_collection_interval: 30
 url: http://your_zenoh_router_address:8000`
`> sudo systemctl restart datadog-agent`
![Dashboards](../../img/20240417-Datadog-Zenoh-Router-Integration/4-dashboards.png)
![Monitors](../../img/20240417-Datadog-Zenoh-Router-Integration/5-monitors.png)

## Conclusion

By integrating Zenoh routers with Datadog, we can enhance observability and gain valuable insights into the performance and status of our distributed Zenoh system. This integration empowers teams to monitor, troubleshoot, and optimize Zenoh deployments effectively, ensuring the reliability and efficiency of their applications.

**– [Alexander Bushnev](https://github.com/sashacmc) for the [Zenoh team](https://github.com/orgs/eclipse-zenoh/people)**

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2024-04-30-zenoh-electrode/

Source: https://zenoh.io/blog/2024-04-30-zenoh-electrode/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh 0.11.0 "Electrode" release is out!

Blog Posts

# Zenoh 0.11.0 "Electrode" release is out!

13th May 2024

During the summer of 2023, we rolled out Zenoh v0.7.0 ‘Charmander,’ which brought significant enhancements to the Zenoh ecosystem. This was followed by the release of v0.10.0-rc ‘Dragonite’ in autumn, and a winter update with v0.10.1-rc.
This spring, we are pleased to announce Zenoh v0.11.0 “Electrode”. This release introduces several new features, some key improvements. Next will come the much-anticipated version 1.0.0, planned for June 2024🎉!

But let’s see what comes with Zenoh Electrode.

![Zenoh comic April 2024](../../img/20240430-blog-zenoh-electrode/comic-april-2024.png)

# Android, Kotlin and Java

![Zenoh kotlin header](../../img/20240430-blog-zenoh-electrode/zenoh-kotlin-header.png)

Back in September we announced that after C, C++ and Python, you could now use Zenoh with Kotlin (checkout the [repository](https://github.com/eclipse-zenoh/zenoh-kotlin)).

However there were some important aspects to tackle.

To begin with, the 0.10.0-rc Zenoh-Kotlin release target was limited to JVM. But you may have asked yourself “what about Android?”… Indeed, on this release we got your back covered ;-). We have refactored the build scripts in order to integrate the [Kotlin Multiplatform Plugin](https://kotlinlang.org/docs/multiplatform-plugin-releases.html), which allows us to have a common codebase to be reused across multiple targets, with some specificity for each. Therefore, we now can build Zenoh-Kotlin for both Android and JVM targets.

Additionally, we now provide packaging, which is key to ease the importing of Zenoh on Kotlin projects. Find them out here on [Github Packages](https://github.com/orgs/eclipse-zenoh/packages?repo_name=zenoh-kotlin), for both JVM and Android targets!

The third important item is that Java joined the party! Indeed, we have forked the Kotlin bindings, making the necessary adjustments to make the bindings fully Java compatible. Checkout the examples! <https://github.com/eclipse-zenoh/zenoh-java/tree/main/examples>

Because Zenoh-Kotlin (and now Zenoh-Java) relies on the Zenoh-JNI native library, we need to take into consideration the platforms on top of which the library is going to run.

For Android, we support the following architectures:

While for JVM we support:

Take a look at the [Zenoh demo app](https://github.com/eclipse-zenoh/zenoh-demos/tree/main/zenoh-android/ZenohApp) we have published to see how to use the package:

*In this example we communicate from an Android phone using the Zenoh Kotlin bindings to a computer using the Zenoh Rust implementation, reproducing a publisher/subscriber example.*

You can also see a live demo we did during the Zenoh User Meeting of an android application using the kotlin bindings to control a turtlebot: <https://youtu.be/oaRe2bkIyIo?feature=shared&t=15268>

# ROS 2 Plug-in

<https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds>

We have had a Zenoh Bridge/Plug-in for DDS for some time. This plug-in has been heavily used by numerous robotic applications in overcoming [wireless connectivity](https://zenoh.io/blog/2021-03-23-discovery/), [bandwidth](https://zenoh.io/blog/2021-09-28-iac-experiences-from-the-trenches/), and [integration](https://zenoh.io/blog/2021-11-09-ros2-zenoh-pico/) challenges. Yet, this plugin was for generic DDS applications and was not leveraging some of the semantics that are specific to ROS2. This is why we decided to do a new plugin/bridge optimized for ROS2, which provides the following features:

`ros2`
`rviz2`

# InfluxDB v2.x Plug-in

<https://github.com/eclipse-zenoh/zenoh-backend-influxdb>

The release extends the support to InfluxDB v2.x. Our plugin maintains support v1.x for our users that are still on the old version of the database. For InfluxDB 2.x backend we have implemented the following features:

# Tokio Porting

Back to April 2022, we conducted a [performance evaluation on Rust asynchronous runtimes](https://zenoh.io/blog/2022-04-14-rust-async-eval/) and chose [async-std](https://async.rs/) as the Rust async framework for Zenoh. Fast forward two years, [Tokio](https://tokio.rs/) has grown to become the most extensive asynchronous framework in Rust. As more users adopt Tokio, the ecosystem has expanded with valuable tools and innovative features. We began another thorough performance study a few months ago and the results were enough to prompt us to switch to Tokio. The change of asynchronous runtime is internal and does not affect the user API. Moreover, it offers us cool features like,

**Controllability.** You can adjust the runtime settings through the environmental variable. For instance, controlling the number of worker threads and the maximal blocking threads for the specific zenoh runtimes.

`export ZENOH_RUNTIME='(
 app: (worker_threads: 2),
 tx: (max_blocking_threads: 1)
 )'`

The configuration syntax follows [RON](https://github.com/ron-rs/ron) and the available parameters are listed [here](https://docs.rs/zenoh-runtime/latest/zenoh_runtime/struct.RuntimeParam.html). We plan to enhance our runtime and add more parameters in the future!

**Debugging**

Developers can leverage the tokio-console to monitor the detailed status of each async task. Taking the z\_sub as the example,

![Tokio](../../img/20240430-blog-zenoh-electrode/tokio.png)

To learn how to enable it, please refer to this [tutorial](https://github.com/tokio-rs/console?tab=readme-ov-file#using-it).

# Attachments

Sometimes, you just want to attach some meta-information to your payload, and you really don’t want to add a layer of serialization in order to do so. Well now, you can use the new `attachment` API! Available in the Rust, C, C++, Kotlin and Java APIs, coming to zenoh-pico and other bindings soon; this API lets you attach a list of key-value pairs to your publications, queries and replies.

`attachment`

For instance, this is how you can use attachments with a publisher using Zenoh’s Rust API:

`// Declaring a publisher
let publisher = session.declare_publisher(&key_expr).res().await?;
// Create an attachment by specifying key value pairs to an attachment builder
let attachmentBuilder = AttachmentBuilder::new();
attachmentBuilder.insert("key1", "value1");
attachmentBuilder.insert("key2", "value2");
// Build the attachment
let attachment = attachmentBuilder.build();
// Perform a put using the with_attachment function.
publisher.put("value").with_attachment(attachment).res();`

The other bindings follow a similar approach, for instance on Kotlin we’d do:

`// …
publisher.put(payload).withAttachment(
 Attachment.Builder()
 .add("key1", "value1")
 .add("key2", "value2")
 .res()
).res()`

# Typescript Bindings

![Zenoh TypeScript header](../../img/20240430-blog-zenoh-electrode/zenoh-ts-header.png)

Many of you have asked for the ability to run Zenoh in your browser… Well, that’s coming up!

We have a Typescript API providing the core set of Zenoh features working in the browser, with Node.js support becoming a priority once enough features are stable in the browser.

For now we can offer only a taste of the API that will be presented to developers, but keep in mind this is still in the experimental stage and changes are likely to happen as we continue to develop the bindings.

In its current state it is structured as a Callback API.

Here is a brief example of how Zenoh currently works in a Typescript program:

`import * as zenoh from "zenoh"
function sleep(ms: number) {
 return new Promise(resolve => setTimeout(resolve, ms));
}
async function main() {
 const session = await zenoh.Session.open(zenoh.Config.new("ws/127.0.0.1:10000"))
 // Subscriber Example
 const key_expr: zenoh.KeyExpr = await session.declare_ke("demo/send/to/ts");
 var subscriber = await session.declare_subscriber_handler_async(key_expr,
 async (sample: zenoh.Sample) => {
 const decoder = new TextDecoder();
 let text = decoder.decode(sample.value.payload)
 console.debug("sample: " + sample.keyexpr + "': '" + text);
 }
 );
 // Publisher Example
 const key_expr2 = await session.declare_ke("demo/send/from/ts");
 const publisher : zenoh.Publisher = await session.declare_publisher(key_expr2);
 let enc: TextEncoder = new TextEncoder(); // always utf-8
 let i : number = 0;
 while ( i < 100) {
 let currentTime = new Date().toTimeString();
 let uint8arr: Uint8Array = enc.encode(My Message : ${currentTime} );
 let value: zenoh.Value = new zenoh.Value(uint8arr);
 (publisher).put(value);
 await sleep(1000);
 }
 // Loop to spin and keep Subscriber alive
 var count = 0;
 while (true) {
 var seconds = 10;
 await sleep(1000 * seconds);
 console.log("Main Loop ? ", count)
 count = count + 1;
 }
}`

# Access Control

As a part of the 0.11.0 release, Zenoh has added the option of access control via network interfaces. It works by restricting actions (eg: put) on key-expressions (eg: test/demo) based on network interface values (eg: lo). The access control is managed by filtering messages (where message types are denoted as actions in the access\_control config): `put`, `get`, `declare_subscriber` and `declare_queryable`. The filter can be applied on both incoming (ingress) and outgoing messages (egress).

`put`
`get`
`declare_subscriber`
`declare_queryable`

Enabling access control for the network is a straightforward process: the rules for the access control can be directly provided in the configuration file.

**Access Control Config**

A typical access control configuration in the config file looks as follows:

`access_control: {
 "enabled": true,
 "default_permission": "deny",
 "rules":
 [
 {
 "actions": ["put", "declare_subscriber"],
 "flows":["egress", "ingress"],
 "permission": "allow",
 "key_exprs": ["test/demo"],
 "interfaces": ["lo0"]
 }
 ]
}`

The configuration has three primary fields:

The *enabled* field sets the access control status. If it is set to false, no filtering of messages takes place and everything that follows in the access control config is ignored.

The *default\_permission* field provides the implicit permission for filtering messages, i.e., this rule applies if no other matching rule is found for an action. It therefore always has lower priority than explicit rules provided in the *rules* field.

The *rules* field itself has sub-fields: *actions*, *flows*, *permission*, *key\_exprs* and *interfaces*. The values provided in these fields set the explicit rules for the access control:

For example, in the above config, the *default\_permission* is set to *deny*, and then a rule is added to explicitly allow certain behavior. Here, a node connecting via the “lo0” interface will be allowed to `put` and `declare_subscriber` on the `test/demo` key expression for both incoming and outgoing messages. However, if there is a node connected via another interface or trying to perform another action (eg: `get`), it will be denied. This provides a granular access control over permissions, ensuring that only authorized devices or networks can perform allowed behavior. More details on this can be found in our [Access Control RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Access%20Control%20Rules.md).

`put`
`declare_subscriber`
`test/demo`
`get`

# Downsampling

Downsampling is a feature in Zenoh that allows users to control the flow of data messages by reducing their frequency based on specified rules. This feature is particularly useful in scenarios where high-frequency data transmission is not necessary or desired, such as conserving network bandwidth or reducing processing overhead.

The downsampling configuration in Zenoh is defined using a structured declaration, as shown below:

`downsampling: [
 {
 // A list of network interfaces messages will be processed on, the rest will be passed as is.
 interfaces: [ "wlan0" ],
 // Data flow messages will be processed on. ("egress" or "ingress")
 flow: "egress",
 // A list of downsampling rules: key_expression and the maximum frequency in Hertz
 rules: [
 {
 key_expr: "demo/example/zenoh-rs-pub",
 freq: 0.1
 },
 ],
 },
],`

Let’s break down each component of the downsampling configuration:

`key_expression`
`freq`
`key_expression`
`freq`

In the provided example, the downsampling rule targets messages published under the key expression `demo/example/zenoh-rs-pub` for interface wlan0 and restricts their transmission frequency to 0.1 Hz. This means that data messages matching this key expression will be transmitted at a maximum rate of 0.1 Hz, effectively reducing the data flow to the specified frequency.

`demo/example/zenoh-rs-pub`

By configuring downsampling rules, users can effectively manage data transmission rates, optimize resource utilization, and tailor data delivery to meet specific application requirements.

# Ability to bind on an interface

Zenoh introduces advanced capabilities for binding network interfaces in TCP/UDP communication on Linux systems, enabling users to fine-tune network connectivity and optimize resource utilization. This feature facilitates precise control over both outgoing connections and incoming connections, enhancing network security, reliability, and performance in diverse deployment environments.

#### Outgoing Connections

Users can specify the interface to be connected to when establishing TCP/UDP connections, ensuring that connections are established only if the target IP address is reachable via the designated interface. This capability enhances network reliability and efficiency by directing outgoing connections through the most appropriate network path.

For instance:

`// connect only if the address 192.168.0.1 is reachable via
// the interface eth0
connect: {
 endpoints: [
 "tcp/192.168.0.1:7447#iface=eth0"
 ],
}`

#### Incoming Connections

Furthermore, Zenoh allows users to bind connections to specific interfaces for listening purposes, even if the interface is not available at the time of launching Zenoh. By specifying the interface to be listened to when accepting incoming TCP/UDP connections, users can ensure that Zenoh binds to the designated interface when it becomes available.

For instance:

`// listen for connections only on interface eth0
// (even if not yet available)
listen: {
 endpoints: [
 "tcp/0.0.0.0:7447#iface=eth0"
 ],
}`

# Transparent network compression

Transparent compression is now available in Zenoh. This allows two Zenoh nodes to perform transparent hop-to-hop compression at network level when communicating. This can be pretty useful when sending large data over constrained networks like WiFi, 5G, etc.

The following configuration enables hop-to-hop compression:

`{
 transport: {
 unicast: {
 /// Enables compression on unicast communications.
 /// Compression capabilities are negotiated during session establishment.
 /// If both Zenoh nodes support compression, then compression is activated.
 compression: {
 enabled: false,
 },
 },
 },
},`

Upon session establishment, Zenoh nodes performs a handshake to verify whether transparent compression should be activated or not. If both agree, then hop-to-hop compression is transparently used as illustrated in the figure below.

![Zenoh transparent compression](../../img/20240430-blog-zenoh-electrode/compression.png)

It’s worth highlighting that Zenoh applications don’t need to be modified to use this feature since, from their perspective, they will send and receive uncompressed data. All the compression happens under the hood, making it completely transparent.

# Plugins support in applications

Plugins have been available only on Zenoh routers, *i.e.*, [zenohd](https://github.com/eclipse-zenoh/zenoh/tree/main/zenohd). Starting from the 0.11.0 release, plugins can be loaded and started by any application written in any supported language, e.g. Rust, C, C++, Python. To enable it it’s sufficient to pass the following configuration upon zenoh session open:

`{
 "plugins_loading": {
 // Enable plugins loading.
 "enabled": true
 /// Directories where plugins configured by name should be looked for. Plugins configured by __path__ are not subject to lookup.
 /// If enabled: true and search_dirs is not specified then search_dirs falls back to the default value: ".:~/.zenoh/lib:/opt/homebrew/lib:/usr/local/lib:/usr/lib"
 // search_dirs: [],
 },
 /// Plugins are only loaded if plugins_loading: { enabled: true } and present in the configuration when starting.
 /// Once loaded, they may react to changes in the configuration made through the zenoh instance's adminspace.
 "plugins": {
 "my_plugin": {
 // my_plugin specific configuration
 }
 }
}`

More configuration details on plugins are available [here](https://github.com/eclipse-zenoh/zenoh/blob/9a9832a407300763af6e30652ac33bcaab2c94e4/DEFAULT_CONFIG.json5#L387).

# Verbatim chunks

A Zenoh key-expression is defined as a `/`-separated list of chunks, where each chunk is a non-empty UTF-8 string that can’t contain the following characters: `*$?#`. E.g.: The key expression `home/kitchen/temp` is composed of 3 chunks: `home`, `kitchen`, and `temp`.

`/`
`*$?#`
`home/kitchen/temp`
`home`
`kitchen`
`temp`

Wild chunks `*` and `**` then allow addressing multiple keys at once. For instance, the key expression `home/*/temp` addresses the `temp` for any value of the second chunk, such as bedroom, livingroom, etc.

`*`
`**`
`home/*/temp` 
`temp`

This release introduces a new type of chunk: the verbatim chunk. The goal of these chunks is to allow some key spaces to be *hermetically sealed* from each other. Any chunk that starts with `@` is treated as a verbatim chunk, and can only be matched by an identical chunk.

`@`

For instance, the key expression `my-api/@v1/**` does not intersect any of the following key expressions:

`my-api/@v1/**` 
`my-api/@v2/**`
`my-api/*/**`
`my-api/@$*/**`
`my-api/**`

because the verbatim chunk `@v1` prohibits it.

`@v1`

In general, verbatim chunks are useful in ensuring that `*` and `**` accidentally match chunks that are not supposed to be matched. A common case is API versioning where `@v1` and `@v2` should not be mixed or at least explicitly selected. The full RFC on key expressions is available [here](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Key%20Expressions.md#verbatim-chunks-behavioural-breaking-change-in-zenoh-0110).

`*`
`**` 
`@v1`
`@v2`

# Vsock links

Zenoh now offers support for Vsock connections, facilitating seamless communication between virtual machines and their host operating systems. [Vsock](https://man7.org/linux/man-pages/man7/vsock.7.html), or Virtual Socket, is a communication protocol designed for efficient communication between virtual machines and their host operating systems in virtualized environments. It enables high-performance communication with low latency and overhead.

Users can specify endpoints using both numeric and string-based addressing formats, allowing for flexible configuration. Numeric addresses such as `"vsock/-1:1234"` and string constant addresses like `"vsock/VMADDR_CID_ANY:VMADDR_PORT_ANY"` and `"vsock/VMADDR_CID_LOCAL:2345"` are supported. This enhancement expands Zenoh’s communication capabilities within virtualized environments, fostering improved integration and interoperability.

 `"vsock/-1:1234"`
`"vsock/VMADDR_CID_ANY:VMADDR_PORT_ANY"`
`"vsock/VMADDR_CID_LOCAL:2345"`

# Connection timeouts and retries

Zenoh’s configuration has been improved to fine tune how Zenoh connects to configured remote endpoints and tries to open listening endpoints.

In both [connect](https://github.com/eclipse-zenoh/zenoh/blob/ac6bbf4676949677887e96e9bb38519cab69ad28/DEFAULT_CONFIG.json5#L24) and [listen](https://github.com/eclipse-zenoh/zenoh/blob/ac6bbf4676949677887e96e9bb38519cab69ad28/DEFAULT_CONFIG.json5#L57) sections of the configuration, the following entries have been added:

`timeout_ms`
`0`
`-1`
`exit_on_failure`
`timeout_ms`
`true`
`open()`
`false`
`open()`
`Ok`
`retry`
`period_init_ms`
`period_increase_factor`
`period_max_ms`

For example, the following configuration:

`retry {
 period_init_ms: 1000,
 period_increase_factor: 4000,
 period_increase_factor: 2
}`

will lead to the following periods between successive attempts (in milliseconds): 1000, 2000, 4000, 4000, 4000, …

It is also possible to define different configurations for different endpoints by setting different values directly in the endpoints strings. Typically if you want your `peer` to imperatively connect to an endpoint (and fail if unable) and optionally connect to another, you can configure your `connect/endpoints` like this: `["tcp/192.168.0.1:7447#exit_on_failure=true", "tcp/192.168.0.2:7447#exit_on_failure=false"]`.

`peer`
`connect/endpoints`
`["tcp/192.168.0.1:7447#exit_on_failure=true", "tcp/192.168.0.2:7447#exit_on_failure=false"]`

# Improved congestion control

Congestion control has been improved in this release and made both less aggressive and configurable. For the sake of understanding this change, it’s important to know that Zenoh uses an internal queue for transmission. Until now, messages published with `CongestionControl::Drop` were dropped as soon as the internal queue was full. However, this led to an aggressive dropping strategy since short bursts couldn’t be accommodated unless the size of the queue was increased, at the cost of additional memory consumption.

`CongestionControl::Drop`

Now, messages are dropped not when the queue is full but when the queue has been full for at least a given amount of time. By default, messages are dropped if the queue is full for \_1ms. \_Congestion control timeout can be configured as follows:

`{
 "transport": {
 "link": {
 "tx": {
 /// Each zenoh link has a transmission queue that can be configured
 "queue": {
 /// Congestion occurs when the queue is empty (no available batch).
 /// Using CongestionControl::Block the caller is blocked until a batch is available and re-insterted into the queue.
 /// Using CongestionControl::Drop the message might be dropped, depending on conditions configured here.
 "congestion_control": {
 /// The maximum time in microseconds to wait for an available batch before dropping the message if still no batch is available.
 "wait_before_drop": 1000
 }
 }
 }
 }
 }
}`

# Mutual TLS authentication in QUIC

Although Zenoh supported QUIC from the very beginning, a recently added feature is the support of mutual authentication with TLS (mTLS) also for QUIC.

mTLS allows to verify the identity of the server as well as the client, this means that only a client having the right certificate can access the Zenoh infrastructure.

Supporting mTLS in QUIC allows for new use-cases where mobility and security are key.

Configuration of mTLS in QUIC is done via the same parameters currently used for [mTLS configuration on TCP](https://zenoh.io/docs/manual/tls/#mutual-authentication-mtls), thus facilitating the migration (or adoption) for users currently using mTLS over TCP. It is sufficient to add a new locator with QUIC to start using mTLS over QUIC!

An example configuration of QUIC with mTLS is:

`{
 // ...
 // your usual zenoh configuration
 "connect": {
 "endpoints": ["quic/<ip address or dnsname>:<port>"]
 },
 "transport": {
 "link": {
 "tls": {
 "client_auth": true,
 "client_certificate": "/cert.pem",
 "client_private_key": "/cert-key.pem",
 "root_ca_certificate": "/root.pem"
 }
 }
 }
 // ...
}`

# New features for Zenoh-Pico

In addition to addressing numerous bugs, the upcoming release of zenoh-pico 0.11 introduces several new features:

# Bugfixes

`**`
`*`

And more. Checkout the [release changelog](https://github.com/eclipse-zenoh/zenoh/releases/tag/0.11.0-rc.1) to check all the new features and bug fixes with their associated PR’s!

# What’s next?

The big news is that in June 2024 we are going to release v1.0.0. This version, along with several innovations, will provide users and the community a first stable version for which we’ll guarantee API and protocol backward compatibility. This is an important milestone as more and more projects and products on the market rely on our beloved Blue Dragon Protocol ;-)

Happy Hacking,

– The Zenoh Team

P.S. You can reach us out on Zenoh’s [Discord server](https://discord.com/invite/vSDSpqnbkm)!

![Guitar](../../img/20231003-blog-zenoh-dragonite/zenoh-on-fire.gif)

![Guitar](../../img/20231003-blog-zenoh-dragonite/zenoh-on-fire.gif)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2024-10-21-zenoh-firesong/

Source: https://zenoh.io/blog/2024-10-21-zenoh-firesong/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh 1.0.0 "Firesong" is ready to rock!

Blog Posts

# Zenoh 1.0.0 "Firesong" is ready to rock!

21st October 2024

As a result of an incredible effort from the whole Zenoh team and Zenoh community, we can finally announce that Zenoh 1.0.0 *Firesong* is out!

![Zenoh comic October 2024](../../img/20241021-blog-zenoh-firesong/comic-october-2024.png)

This release marks an incredible milestone for Zenoh and comes with a lot of features and improvements:

Let us take a closer look at what Zenoh 1.0.0 brings to the table.

## Improved API approach

Zenoh’s API has been improved in terms of ergonomics, clarity, and composability for future extensibility!
The following sections highlight the main changes of the API in the various language bindings.
The full migration guide of each language is available [here](https://zenoh.io/docs/migration_1.0/concepts/).

### Accessors

To better separate the public API from the internal implementation, we have introduced the accessor pattern in the Zenoh API across all language bindings.
See an example in Rust below.
Please note that the same approach would apply to all Zenoh APIs.

Zenoh 0.11.0:

`while let Ok(sample) = subscriber.recv_async().await {
 println!(
 ">> [Subscriber] Received {} ('{}': '{}')",
 sample.kind,
 sample.key_expr.as_str(),
 );
}`

Zenoh 1.0.0:

`while let Ok(sample) = subscriber.recv_async().await {
 println!(
 ">> [Subscriber] Received {} ('{}': '{}')",
 sample.kind(),
 sample.key_expr().as_str(),
 );
}`

### ZBytes

`Value` was a type that contained a payload (`ZBuf`) and some metadata about the `Encoding`. It was generally accepted in functions like `put()` and `reply()`.
Zenoh 1.0.0 deprecates `Value` in favour of explicitly separating `ZBytes` and `Encoding` in the API. This has the benefit of improving API and network overhead.

`Value`
`ZBuf`
`Encoding`
`put()`
`reply()`
`Value`
`ZBytes`
`Encoding`

`ZBytes` is the core type for raw data representation in Zenoh.
All API has been reworked to accept `ZBytes` or a type that can be transparantely converted into a `ZBytes`, such as a string.
Sample’s payloads are now `ZBytes`. `Publisher`, `Queryable` and `Subscriber` now expect `ZBytes` for all their interfaces.
The Attachment API also now accepts `ZBytes`.

`ZBytes`
`ZBytes`
`ZBytes`
`ZBytes`
`Publisher`
`Queryable`
`Subscriber`
`ZBytes`
`ZBytes`

Zenoh 0.11.0:

`// Publisher
// “My Value” is converted in bytes and the “string” encoding was automatically set
session.put(“test/foo”, “My Value”).res().await.unwrap();
// Subscriber
// Data can be accessed directly and encoding metadata is not required to be checked
// Some bandwidth was wasted for nothing
let string = String::from_utf8_lossy(sample.value.contiguous());`

Zenoh 1.0.0:

`// Publisher
// “My Value” is a string that can be diretly converted in bytes, no encoding is automatically set
session.put(“test/foo”, “My Value”).attachment(“My attachment”).await.unwrap();
// Subscriber
// Convert data type using
let string = String::from_utf8_lossy(&sample.payload().to_bytes());
let value = sample.payload().try_to_string().unwrap();
let attach = sample.attachment().try_to_string().unwrap();`

It is worth highlighting that Zenoh semantics and protocol take care of sending and receiving bytes without restricting the actual data types.
Nonetheless, in the spirit of always improving user’s life with a simple out-of-the-box experience, we have added a number of optional serializer/deserializer to deal with language primitive types (e.g., integeres, floats, tuples, etc.).
This serializer/deserializer is NOT by any means the only serializer/deserializer users can use nor a limitation to the types supported by Zenoh.
Users are free and encouraged to use any serializer/deserializer of their choice like JSON, protobuf, bincode, flatbuffers, etc.

`use zenoh_ext::{z_deserialize, z_serialize};
// Numeric types: u8, u16, u32, u128, i8, i16, i32, i128, f32, f64
let input = 1234_u32;
let payload = z_serialize(&input);
let output: u32 = z_deserialize(&payload).unwrap();
assert_eq!(input, output);
// Vec
let input = vec![0.0f32, 1.5, 42.0];
let payload = z_serialize(&input);
let output: Vec<f32> = z_deserialize(&payload).unwrap();
assert_eq!(input, output);
// HashMap
let mut input: HashMap<u32, String> = HashMap::new();
input.insert(0, String::from("abc"));
input.insert(1, String::from("def"));
let payload = z_serialize(&input);
let output: HashMap<u32, String> = z_deserialize(&payload).unwrap();
assert_eq!(input, output);
// Tuple
let input = (0.42f64, "string".to_string());
let payload = z_serialize(&input);
let output: (f64, String) = z_deserialize(&payload).unwrap();
assert_eq!(input, output);
// Array (handled as variable-length sequence, not as tuple)
let input = [0.0f32, 1.5, 42.0];
let payload = z_serialize(&input);
let output: [f32; 3] = z_deserialize(&payload).unwrap();
assert_eq!(input, output);
// can also be deserialized as a vec
let output: Vec<f32> = z_deserialize(&payload).unwrap();
assert_eq!(input.as_slice(), output);`

You can have a look at the [z\_bytes example](https://github.com/eclipse-zenoh/zenoh/blob/main/examples/examples/z_bytes.rs) for additional examples.

### Encoding

`Encoding` has been reworked, moving away from enumerables to now accepting strings.
While Zenoh does not impose any `Encoding` requirement on the user, providing an `Encoding` can offer automatic wire-level optimization for known types.  
For the user defined `Encoding`, it can be thought of as optional metadata, carried over by Zenoh in such a way that the end user’s application may perform different operations based on `Encoding`.  
We have expanded our list of predefined encoding types from Zenoh 0.11.0 to include variants for numerous IANA standard encodings, including but not limited to `video/x` , `application/x`, `text/x`, `image/x` and `audio/x` encoding families, as well as an encoding family specific to Zenoh defined by the prefix `zenoh/x` .  
Users can also define their own encoding scheme that does not need to be based on the predefined IANA variants.

`Encoding`
`Encoding`
`Encoding`
`Encoding`
`Encoding`
`video/x`
`application/x`
`text/x`
`image/x`
`audio/x`
`zenoh/x`
`// Publisher
// Encoding::TEXT_PLAIN is a convenience constant equivalent to “text/plain”
session.put(“test/foo”, “My Value”).encoding(Encoding::TEXT_PLAIN).await.unwrap();
// Subscriber
if sample.encoding() == Encoding::TEXT_PLAIN {
 let s = sample.payload().try_to_string().unwrap()
}`

Example of using custom encoding:

`// Publisher
// Encoding::TEXT_PLAIN is a convenience constant equivalent to “text/plain”
session.put(“test/foo”, vec![0u8; 64]).encoding(“my_encoding”).await.unwrap();
// Subscriber
if &sample.encoding().to_string() == “my_encoding” {
 let reader = sample.payload().reader();
 // Deserialize the type according to the encoding
}`

### Query & Queryable

The `reply` method of a `Queryable` has gained two variants:

`reply`
`Queryable`
`reply_del`
`reply_err`

Additionally, these variants behave similarly to `put` and `del`, providing improved ergonomics.

`put`
`del`

We have added the ability to get the underlying `Handler` of a Queryable as well.

`Handler`
`// Queryable
while let Ok(query) = queryable.recv_async().await {
 query
 .reply(key_expr.clone(), payload.clone())
 // Or reply with a delete
 // .reply_del(key_expr.clone())
 // Or reply with an error
 // .reply_err(“My error”)
 .await
 .unwrap();
}
// Querier
let replies = session.get(“test/foo”).await.unwrap();
while let Ok(reply) = replies.recv_async().await {
 match reply.result() {
 Ok(sample) => match sample.kind() {
 SampleKind::Put => { /* Handle .reply() */ },
 SampleKind::Del => { /* Handle .reply_del() */ },
 },
 Err(err) => { /* Handle .reply_err() and any infrastructure error */ }
 }
}`

### Timestamps

Zenoh timestamps are based on an [Unique Hybrid Logical Clock](https://github.com/atolab/uhlc-rs), which is largely used in the Zenoh Storage Alignment protocol. One of the requirements for the alignment protocol is to be able to uniquely identify who published the data and consequently who generated the timestamp. Zenoh 0.11.0 exposed a function to generate timestamps outside of a session, which could be used in a Zenoh system. Due to our efforts to improve the storage replication logic, now timestamps are generated from a session, with the timestamp inheriting the `ZenohID` of the session. Users are not expected to generate timestamps by themselves but rather to rely on the [timestamping functionality](https://github.com/eclipse-zenoh/zenoh/blob/6b7ec55911ce85a243c6eae857cbddd7ab1d0021/DEFAULT_CONFIG.json5#L133) of Zenoh.

`ZenohID`

### Ring channel

A pull subscriber was mainly used to pull the latest data available for a given subscriber.
In Zenoh 1.0.0, we have removed the pull subscriber as part of some rework to streamline the API and the protocol.
This leads to the fact that only one type of subscriber exists.
However, to keep the functionality of being able to pull the last data, we have added a `RingChannel` for the subscriber (as well as for the queryable and get) that can be used to get a similar behaviour.
Once full, the `RingChannel` will replace older data with most recent ones. This contrasts with the `FIFOChannel`, the default channel type used by Subscribers, which blocks once its buffer is full.

`RingChannel`
`RingChannel`
`FIFOChannel`

Publisher example:

`#[tokio::main]
async fn main() {
 let session = zenoh::open(Config::default()).await.unwrap();
 let publisher = session.declare_publisher(“test/foo”).await.unwrap();
 // Publish a message every second
 for idx in 0..10 {
 tokio::time::sleep(Duration::from_secs(1)).await;
 let buf = format!("[{idx:4}] Pub from Rust!");
 println!("{}", buf);
 publisher
 .put(buf)
 .await
 .unwrap();
 }
}`

Subscriber example with FifoChannel (default):

`#[tokio::main]
async fn main() {
 let session = zenoh::open(Config::default()).await.unwrap();
 let subscriber = session.declare_subscriber(“test/foo”).await.unwrap();
 while let Ok(sample) = subscriber.recv_async().await {
 let payload = sample
 .payload()
 .try_to_string()
 .unwrap_or_else(|e| format!("{}", e));
 println!(“{}”, payload); // No long computation
 }
}`

Subscriber example with RingChannel:

`#[tokio::main]
async fn main() {
 let session = zenoh::open(Config::default()).await.unwrap();
 let subscriber = session
 .declare_subscriber(“test/foo”)
 .with(RingChannel::new(5))
 .await
 .unwrap();
 while let Ok(sample) = subscriber.recv_async().await {
 let payload = sample
 .payload()
 .try_to_string()
 .unwrap_or_else(|e| format!("{}", e));
 println!(“{} Sleeping for 5s.”, payload);
 tokio::time::sleep(Duration::from_secs(5)).await; // Long computation
 }
}`

You can take a look at examples of usage in any language’s *examples/z\_pull.x*.
The output of the publisher will look like this with a publication made every second.

`$ ./z_pub
[ 0] Pub from Rust!
[ 1] Pub from Rust!
[ 2] Pub from Rust!
[ 3] Pub from Rust!
[ 4] Pub from Rust!
[ 5] Pub from Rust!
[ 6] Pub from Rust!
[ 7] Pub from Rust!
[ 8] Pub from Rust!
[ 9] Pub from Rust!
[ 10] Pub from Rust!`

Since *z\_sub* uses a `FifoChannel` then it will receive all samples. Please note that in the case of having a slow subscriber, back pressure could reach back the publisher.

`FifoChannel`
`$ ./z_sub
[ 0] Pub from Rust!
[ 1] Pub from Rust!
[ 2] Pub from Rust!
[ 3] Pub from Rust!
[ 4] Pub from Rust!
[ 5] Pub from Rust!
[ 6] Pub from Rust!
[ 7] Pub from Rust!
[ 8] Pub from Rust!
[ 9] Pub from Rust!
[ 10] Pub from Rust!`

If you want the subscriber to receive and process the most recent samples, use the `RingChannel`. In this case, the subscriber will take 5 seconds to process a sample, not being able to keep up with the publication rate. Using the `RingChannel` will then allow you to drop old samples and get a more recent one.
E.g. if you want to always process the most recent sample, you can set the size of the `RingChannel` to 1.

`RingChannel`
`RingChannel`
`RingChannel`
`$ ./z_pull
[ 0] Pub from Rust! Sleeping for 5s.
[ 2] Pub from Rust! Sleeping for 5s. # Missed sample 1
[ 7] Pub from Rust! Sleeping for 5s. # Missed sample 3, 4, 5, 6
[ 12] Pub from Rust! Sleeping for 5s. # Missed sample 8, 9, 10, 11`

## C API

Zenoh 1.0.0 underwent a major rework of the C API with the goal of better clarifying data ownership via a well-defined naming semantics of types.

#### Owned types

Owned types are types that are allocated by the user and it is their responsibility to drop them using `z_drop` (or `z_close` for sessions).

`z_drop`
`z_close`

Previously, we were returning Zenoh structures by value.
In Zenoh 1.0.0, a reference to memory must be provided. This allows initializing user allocated structures and frees return value for error codes.

#### Moved types

Moved types are obtained when using `z_move` on an owned type object. They are consumed on use when passed to relevant functions. Any non-constructor function accepting a moved object (i.e. an object passed by owned pointer) becomes responsible for calling drop on it. The object is guaranteed to be in the null state upon such function return, even if it fails.

`z_move`

#### Loaned types

Each owned type now has a corresponding `z_loaned_xxx_t` type, which is obtained by calling `z_loan` or `z_loan_mut` on it, or eventually received from Zenoh functions / callbacks. It is no longer possible to directly access the fields of an owned object, the accessor functions on the loaned objects should instead be used.

`z_loaned_xxx_t`
`z_loan`
`z_loan_mut`

#### View types

View types are only wrappers to user allocated data, like `z_view_keyexpr_t.` These types can be loaned in the same way as owned types but they don’t need to be dropped explicitly (user is fully responsible for deallocation of wrapped data).

`z_view_keyexpr_t.`

Here is a quick example of all the above changes:

Zenoh 0.11.0:

`int main(int argc, char** argv) {
 z_owned_config_t config = z_config_default();
 z_owned_session_t s = z_open(z_move(config));
 if (!z_check(s)) {
 exit(-1);
 }
 z_put_options_t options = z_put_options_default();
 options.encoding = z_encoding(Z_ENCODING_PREFIX_TEXT_PLAIN, NULL);
 const char *payload = "My payload";
 int res = z_put(z_loan(s), z_keyexpr(args.keyexpr), (const uint8_t*)payload, strlen(payload), &options);
 if (res < 0) {
 printf("Put failed...\n");
 }
 z_close(z_move(s));
 z_drop(z_move(attachment));
 return 0;
}`

Zenoh 1.0.0:

`int main(int argc, char** argv) {
 z_owned_config_t config;
 z_config_default(&config);
 z_owned_session_t s;
 if (z_open(&s, z_move(config)) < 0) {
 exit(-1);
 }
 z_view_keyexpr_t ke;
 z_view_keyexpr_from_str(&ke, args.keyexpr);
 z_owned_bytes_t payload;
 z_bytes_from_static_str(&payload, "My payload");
 z_put_options_t options;
 z_put_options_default(&options);
 int res = z_put(z_loan(s), z_loan(ke), z_move(payload), &options);
 if (res < 0) {
 printf("Put failed...\n");
 }
 z_close(z_move(s));
 return 0;
}`

For more information on the C API, please see the [migration guide](https://zenoh.io/docs/migration_1.0/c_pico/).

## C++ API

Zenoh 1.0.0 brings a number of changes to the API, with a concentrated effort to make the C++ API usage close to the Rust API.

The improvements include:

#### Error Handling

In Zenoh 0.11.0, all Zenoh call failures were handled by either returning a bool value indicating success or failure (and probably returning an error code) or returning an `std::variant<ReturnType, ErrorMessage>`. For instance:

`std::variant<ReturnType, ErrorMessage>`
`std::variant<z::Config, ErrorMessage> config_client(const z::StrArrayView& peers);
bool put(const z::BytesView& payload, const z::PublisherPutOptions& options, ErrNo& error);`

In Zenoh 1.0.0, all functions that can fail on the Zenoh side now offer 2 options for error handling:

Any function that can fail now accepts an optional parameter ZError\* err pointer to the error code. If it is not provided (or set to nullptr), an instance of ZException will be thrown, otherwise the error code will be written into the err pointer.

`static Config client(const std::vector<std::string>& peers, ZError* err = nullptr);`

This also applies to constructors: if a failure occurs, either an exception is thrown or the error code is written to the provided pointer.
In the latter case, the returned object will be in an *empty* state (i.e. converting it to a boolean returns false).

`Config config = Config::create_default();
// Receiving an error code
Zerror err = Z_OK;
auto session = Session::open(std::move(config), &err);
if (err != Z_OK) { // or alternatively if (!session)
 // handle failure
}
// Catching exception
Zenoh::session s(nullptr); // Empty session object
try {
 s = Session::open(std::move(config), &err);
} catch (const ZException& e) {
 // handle failure
}`

All returned and `std::move`’d-in objects are guaranteed to be left in an *empty* state in case of function call failure.

`std::move`

#### Stream Handlers and Callbacks

In Zenoh 1.0.0, Subscriber, Queryable and get can now use either a callable object or a stream handler.
Currently, Zenoh provides 2 types of handlers:

`// callback
session.get(
 keyexpr, "", on_reply, on_done,
 {.target = Z_QUERY_TARGET_ALL}
);
// stream handlers interface
auto replies = session.get(
 keyexpr, "", channels::FifoChannel(16), // Or channels::RingChannel(16),
 {.target = QueryTarget::Z_QUERY_TARGET_ALL}
);
// blocking
for (auto res = replies.recv(); std::has_alternative<Reply>(res); res = replies.recv()) {
 const auto& sample = std::get<Reply>(res).get_ok();
 std::cout << "Received ('" << sample.get_keyexpr().as_string_view() << "' : '"
 << sample.get_payload().as_string() << "')\n";
}`

For more information on the C++ API, please see the [migration guide](https://zenoh.io/docs/migration_1.0/c++/).

## Python API

In Zenoh 1.0.0, Python API introduces context managers for the Zenoh session and the various entities like subscriber, queryable and publisher.
Using the context manager ensures the proper cleanup is called.

For example, to close the Zenoh session after use with context manager:

`import Zenoh
with zenoh.open(zenoh.Config()) as session:
 # `session.close()` will be called at the end of the block`

Session-managed objects like subscribers or queryables can also be managed using context managers:

`with session.declare_subscriber("my/keyexpr") as subscriber:
 # `subscriber.undeclare()` will be called at the end of the block``

However, these objects can also be used without a context manager, and without calling undeclare. In that case, they will run in “background” mode, meaning that their lifetime will end when the session closes.

`import Zenoh
with zenoh.open(zenoh.Config()) as session:
 subscriber = session.declare_subscriber("my/keyepxr")
 for sample in subscriber:
 ...
 # `session.close()` will be called at the end of the block, and it will undeclare the subscriber`

In Zenoh 0.11.0, it was necessary to keep a variable in the scope for declared *subscribers/queryables/etc*.
This restriction no longer exists, as objects not bound to a variable will still run in *background* mode, until the session is closed.

Please refer to the [migration guide](https://zenoh.io/docs/migration_1.0/python/) for the complete list of changes on the Python API.

## Kotlin API

Finally, after many ‘alpha’ releases, the time has come to provide a first stable release on the Kotlin API, bringing the possibility of using Zenoh on JVM and Android targets!
The Kotlin API comes with an extensive rework on the API, along with bug fixes, and new implementations.
The changes come with the following goals in mind:

New features and improvements:

For more information on the Kotlin API, please see the [migration guide](https://zenoh.io/docs/migration_1.0/kotlin/).

## Java API

The Java API is still a work in progress, and future extensive rework on the API is to be expected. The beta releases of the Java API are fully compatible with Zenoh 1.0.0. Feel free to use it, but keep in mind that changes are coming to fully align the API with all the other bindings.
When that will happen, we will provide a corresponding migration guide.

## TypeScript API

The TypeScript API is in its alpha stage with the focus being put towards browser support, as majority of the requests from users have been to use Zenoh for UI and visualisation applications, and due to the numerous languages already supported for backend development.
The Typescript API comes with the requirement of using a remote API plugin attached to a Zenoh router running on the backend.
The remote API plugin works by starting a native Zenoh session inside the plugin and communicating over websockets with the browser instance, passing control and data messages between the browser instance and the plugin backend. All state exists inside the plugin and the Typescript API just keeps references to the state stored in the plugin.
It is advised for users to account for the general performance characteristics of a JavaScript runtime environment when designing their applications.

Below is an example of a *subscriber* taking a callback:

`const session = await Session.open(new Config("ws/127.0.0.1:10000"));
 const callback = async function (sample: Sample): Promise<void> {
 console.log!(
 ">> [Subscriber] Received " +
 sample.kind() + " ('" +
 sample.keyexpr() + "': '" +
 sample.payload().deserialize(deserialize_string) + "')",
 );
 };
 let callback_subscriber: Subscriber = await session.declare_subscriber(
 "demo/pub",
 callback,
 );
 await sleep(1000 * 3);
 callback_subscriber.undeclare();`

Below is an example of a *publisher*:

 `const session = await Session.open(new Config("ws/127.0.0.1:10000"));
 let key_expr = new KeyExpr("demo/example/zenoh-ts-pub");
 let publisher: Publisher = session.declare_publisher(
 key_expr,
 {
 encoding: Encoding.default(),
 congestion_control: CongestionControl.BLOCK,
 priority: Priority.DATA,
 express: true,
 reliability: Reliability.RELIABLE
 }
 );
 const payload = [122, 101, 110, 111, 104];
 for (let idx = 0; idx < Number.MAX_VALUE; idx++) {
 let buf = `[${idx}] ${payload}`;
 console.log("Block statement execution no : " + idx);
 console.log(`Putting Data ('${key_expr}': '${buf}')...`);
 publisher.put(buf, Encoding.TEXT_PLAIN, "attachment");
 await sleep(1000);
 }`

## Shared Memory

Zenoh 1.0.0 adds comprehensive shared memory support with a rich yet unstable API to perform specific SHM actions.
The SHM subsystem is heavily reworked both on the API and implementation side.
Shared memory API is currently available in Rust, C and C++ API.

Some key featuers that have been introduced are:

`// create an SHM backend…
let backend = PosixShmProviderBackend::builder()
 .with_size(65536)
 .unwrap()
 .wait()
 .unwrap();
// ...and an SHM provider
let provider = ShmProviderBuilder::builder()
 .protocol_id::<POSIX_PROTOCOL_ID>()
 .backend(backend)
 .wait();
// There are two API-defined ways of making shm buffer allocations: direct and through the layout...
// Direct allocation
// The direct allocation calculates all layouting checks on each allocation. It is good for
// uniquely-layouted allocations. For making series of similar allocations, please refer to
// layout allocation API which is shown later in this example...
let _direct_allocation = {
 // OPTION: Simple allocation
 let simple = provider.alloc(512).wait().unwrap();
 // OPTION: Allocation with custom alignment and alloc policy customization
 let _comprehensive = provider
 .alloc(512)
 .with_alignment(AllocAlignment::new(2).unwrap())
 .with_policy::<GarbageCollect>()
 .wait()
 .unwrap();
 // OPTION: Allocation with custom alignment and async alloc policy
 let _async = provider
 .alloc(512)
 .with_alignment(AllocAlignment::new(2).unwrap())
 .with_policy::<BlockOn<Defragment<GarbageCollect>>>()
 .await
 .unwrap();
 simple
};
// Create a layout for particular allocation arguments and particular SHM provider
// The layout is validated for argument correctness and also is checked
// against particular SHM provider's layouting capabilities.
// This layout is reusable and can handle series of similar allocations
let buffer_layout = {
 // OPTION: Simple configuration:
 let simple_layout = provider.alloc(512).into_layout().unwrap();
 // OPTION: Comprehensive configuration:
 let _comprehensive_layout = provider
 .alloc(512)
 .with_alignment(AllocAlignment::new(2).unwrap())
 .into_layout()
 .unwrap();
 simple_layout
};
// Allocate ShmBufInner
// Policy is a generics-based API to describe necessary allocation behaviour
// that will be highly optimized at compile-time.
// Policy resolvable can be sync and async.
// The basic policies are:
// -JustAlloc (sync)
// -GarbageCollect (sync)
// -Deallocate (sync)
// --contains own set of dealloc policy generics:
// ---DeallocateYoungest
// ---DeallocateEldest
// ---DeallocateOptimal
// -BlockOn (sync and async)
let mut sbuf = async {
 // Some examples on how to use layout interface:
 // OPTION: The default allocation with default JustAlloc policy
 let default_alloc = buffer_layout.alloc().wait().unwrap();
 // OPTION: The async allocation
 let _async_alloc = buffer_layout
 .alloc()
 .with_policy::<BlockOn>()
 .await
 .unwrap();
 // OPTION: The comprehensive allocation policy that blocks if provider is not able to allocate
 let _comprehensive_alloc = buffer_layout
 .alloc()
 .with_policy::<BlockOn<Defragment<GarbageCollect>>>()
 .wait()
 .unwrap();
 // OPTION: The comprehensive allocation policy that deallocates up to 1000 buffers if provider is not able to allocate
 let _comprehensive_alloc = buffer_layout
 .alloc()
 .with_policy::<Deallocate<1000, Defragment<GarbageCollect>>>()
 .wait()
 .unwrap();
 default_alloc
}
.await;`

For more information, please see the [migration guide](https://zenoh.io/docs/migration_1.0/rust/#shared-memory).

## Plugins

In Zenoh 1.0.0 we finished porting the Zenoh ecosystem from async-std to Tokio. All plugins and storage backends now use Tokio.

As a reminder, Zenoh 0.11.0 added the ability for user-applications to load compiled plugins written in Rust, regardless of which language bindings you are using. See the configuration example on how to load the plugins.

When loading a plugin, it must have been built with the same version of the Rust compiler as the bindings loading it, and the `Cargo.lock` of the plugin must be synced with the same commit of Zenoh.

`Cargo.lock`

This means that if the language bindings are using `rustc` version `1.75`:

`rustc`
`1.75`
`1.75`
`Cargo.lock`
`Cargo.lock`

The reason behind this strict set of requirements is due to Rust making no guarantees regarding data layout in memory. This means between compiler versions, the representation may change based on optimizations. More on this topic here: [Rust:Type-Layout](https://doc.rust-lang.org/reference/type-layout.html#representations)

## Interest protocol

Zenoh 1.0.0 introduces a major change in the routing protocol that brings a great scalability improvement and a major discovery traffic consumption reduction.

Up to version 0.11.0, all subscribers, queryables and liveliness tokens declarations were propagated to all nodes of the system.
In a large system, this could be problematic for small devices. In version 1.0.0, subscribers, queryables and liveliness tokens declarations are not propagated any more to clients and peers subsystems.
This implies that writer side filtering cannot be performed any more in clients and peers subsystems.
All publications, queries and liveliness queries are sent to the nearest router.
Writer side filtering can be reactivated for publications on some key expressions by simply declaring a *publisher*.

## Access Control

For Zenoh 1.0.0, we are happy to share that we have added support for TLS and user/password authentication methods as means to identify access control subjects, as relying solely on interface names to identify subjects quickly reaches its limits.
This addition introduced the need for a way to describe subjects as combinations of multiple attributes of different types (interface, certificate common name, and/or username).
We have addressed this need by reworking the ACL configuration format, making it modular by isolating the `rules` from the `subjects`.
This allows the combination of subject attributes, while also avoiding the need to duplicate subject or rule configurations by adding the `policies` list.

`rules`
`subjects`
`policies`

On another note, we have shifted the focus of ACL from `actions` to `messages` to make it easier for users to associate the ACL rules to their respective operations exposed via the Zenoh API.
The `get` action has been replaced by the `Query` message, and we completed the array of supported message types in ACL with the addition of publisher `Delete` and queryable `Reply` messages. Filters for liveliness messages are added later on in Zenoh v1.0.3.

`actions`
`messages`
`get`
`Query`
`Delete`
`Reply`

Following this release, a guide on how to configure ACL is available on the [Zenoh reference manual](https://zenoh.io/docs/manual/access-control/), and the [Access Control Rules RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Access%20Control%20Rules.md) has been updated.

## Batching and jitter

The porting of Zenoh to Tokio in 0.11.0 had as a side effect a change in the batching behaviour as reported by some users.
The issue has been thoroughly investigated resulting in a rework of the batching mechanism in Zenoh 1.0.0.
This rework accounts for Tokio peculiarities in timing management and improves the overall jitter performance when publishing at high frequency.

## Link selection

Link selection refers to the process of choosing a network Link when transmitting messages.
This is done in the Zenoh Transport layer when two Zenoh nodes are operating in multilink mode (i.e. more than one Link has been established).

In Zenoh 0.11.x, the Link selection implementation picks any Link that matches the Reliability of the transmitted message.
In Zenoh 1.0.0, Links can be tagged with Reliability and Priority range information through Endpoint metadata:

`{ listen: { endpoints: ["tcp/localhost:7447?prio=0-3;rel=1"] } }`

Thus Link selection takes in account both Reliability and Priority of the transmitted message by picking the Link that best matches the given Reliability-Priority pair.

E.g., let’s consider the following configuration:

`{ listen: { endpoints: ["tcp/localhost:7447?rel=0", "tcp/localhost:7448?rel=1"] } }`

Will result in listening on two different TCP ports: *7447* that will be used for *best effort* traffic and *7448* that will be used for *reliable traffic*.

## Storage Alignment Protocol

In Zenoh 1.0.0 we have completely rewritten the *storage replication* feature to provide a more robust and configurable implementation.
Users leveraging this functionality will have to update their configuration as this release includes non-backward compatible changes.
The following configuration illustrates the changes:

`"plugins": {
 "storage_manager": {
 "storages": {
 "replication-test": {
 "key_expr": "test/replication/*",
 "strip_prefix": "test/replication",
 "volume": "memory",
 // This field was named replica_config.
 "replication": {
 // This field was named publication_interval.
 "interval": 10,
 // This field was named delta.
 "sub_intervals": 5,
 "propagation_delay": 250,
 // These fields did not exist before.
 "hot": 6,
 "warm": 30,
 }
 }
 }
 }
}`

As shown above, in addition to renaming some fields, we expose two new ones: hot and warm.
They expose to some extent the algorithm we use in order to keep *storage* aligned and have a direct impact on the quantity of information sent over the network.

As with most things in computer science, tweaking these values comes down to making a trade-off: the higher they are, the more information will be regularly sent but, in turn, the alignment process will be faster, requiring less exchanges.
Conversely, the lower they are, the less information will be regularly sent but the alignment process could take longer, requiring more message exchanges.
Choosing appropriate values depends on your system: if it is unstable only exceptionally and you do not expect your *storage* to diverge a lot, you can keep these values at their default.

Another important remark, and a difference compared to the previous implementation, is that *storage* will align only if their configurations are identical. This includes: (i) all the fields of the replication section, (ii) the key\_expr field of the *storage* and (iii) the strip\_prefix field of the *storage*.
The rationale is to avoid comparing information that, in fact, cannot be compared eventually leading to a significant overload: the full alignment algorithm would be triggered at every alignment interval, maybe to no avail if the *storage* are actually aligned.

## TLS/mTLS/QUIC Configuration

In Zenoh 1.0.0 we have changed the configuration parameters for TLS/mTLS/QUIC to faciliate the configuration.

The following configuration illustrates the changes:

`"transport": {
 "link": {
 "tls": {
 "root_ca_certificate": "/home/user/tls/minica.pem",
 "enable_mtls": true,
 "listen_private_key": "/home/user/tls/localhost/key.pem",
 "listen_certificate": "/home/user/tls/localhost/cert.pem",
 "connect_private_key": "/home/user/client/localhost/key.pem",
 "connect_certificate": "/home/user/client/localhost/cert.pem",
 "verify_name_on_connect":false,
 }
 }
 }`

For users already using a TLS configuration, it is sufficient to change the configuration parametes accoring to the following table:

| Old | New |
| --- | --- |
| client\_auth | enable\_mtls |
| server\_name\_verification | verify\_name\_on\_connect |
| server\_private\_key | listen\_private\_key |
| server\_certificate | listen\_certificate |
| client\_private\_key | connect\_private\_key |
| client\_certificate | connect\_certificate |

## Zenoh-Pico

Zenoh-Pico implementes now the new [C API](#c-api) as well the new [interest protocol](#interest-protocol) when operating in client mode.
Therefore, Zenoh-Pico publishers will now start sending messages on the network only once at least one subscriber is detected, saving energy and bandwidth in case of nodody is interested in the actual data.
The interest feature will be implemented also for peer mode in the future.

## Changelog

The effort behind Zenoh 1.0.0 resulted in a large number of bugfixes and improvements.
The full changelog for every Zenoh repository is available at the following links: [Rust](https://github.com/eclipse-zenoh/zenoh/releases), [C](https://github.com/eclipse-zenoh/zenoh-c/releases), [C++](https://github.com/eclipse-zenoh/zenoh-cpp/releases), [Python](https://github.com/eclipse-zenoh/zenoh-python/releases), [Kotlin](https://github.com/eclipse-zenoh/zenoh-kotlin/releases), [Pico](https://github.com/eclipse-zenoh/zenoh-pico/releases), [DDS plugin](https://github.com/eclipse-zenoh/zenoh-plugin-dds/releases), [ROS2 plugin](https://github.com/eclipse-zenoh/zenoh-plugin-ros2/releases), [MQTT plugin](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt/releases), [WebServer plugin](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt/releases), [Filesystem backend](https://github.com/eclipse-zenoh/zenoh-backend-filesystem/releases), [RocksDB backend](https://github.com/eclipse-zenoh/zenoh-backend-rocksdb/releases), [S3 backend](https://github.com/eclipse-zenoh/zenoh-backend-s3/releases), [InfluxDB backend](https://github.com/eclipse-zenoh/zenoh-backend-influxdb/releases).

## What’s next?

This has been quite a long blog post but the amount of new features introduced in Zenoh 1.0.0 deserved some space! And now what could you expect from Zenoh in the future?

Happy Hacking,

– The Zenoh Team

P.S. You can reach us out on Zenoh’s [Discord server](https://discord.com/invite/vSDSpqnbkm)!

![Guitar](../../img/20231003-blog-zenoh-dragonite/zenoh-on-fire.gif)

![Guitar](../../img/20231003-blog-zenoh-dragonite/zenoh-on-fire.gif)

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2024-12-12-zenoh-firesong-1.1.0/

Source: https://zenoh.io/blog/2024-12-12-zenoh-firesong-1.1.0/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh 1.1.0: Firesong Keeps Rocking 🎸

Blog Posts

# Zenoh 1.1.0: Firesong Keeps Rocking 🎸

12th December 2024

This latest release of Zenoh 1.1.0 brings exciting new features, some of them were already introduced in the 1.0.1, 1.0.2, 1.0.3, and 1.0.4 releases. The key features are:

### API

### Zenoh-Pico

### ROS 2 Bridge

### Protocol Updates

### Commercial Support and Tools

## Querier

The querier has been added to Zenoh to serve a similar purpose of the publisher but for queries. For example, a publisher allows Zenoh to perform some optimization for continuous publications like [write-side filtering](https://www.google.com/url?q=https://zenoh.io/blog/2024-10-21-zenoh-firesong/%23interest-protocol&sa=D&source=docs&ust=1733925165202597&usg=AOvVaw1piF0-TzhbWXLP5chS1fKO) and [matching status](https://docs.rs/zenoh/latest/zenoh/pubsub/struct.Publisher.html#method.matching_status). These kinds of optimizations are now also available for queries through the new querier API. A Rust example is provided below and [here](https://github.com/eclipse-zenoh/zenoh/blob/main/examples/examples/z_querier.rs). The same example is also available in [C](https://github.com/eclipse-zenoh/zenoh-c/blob/main/examples/z_querier.c), [C++](https://github.com/eclipse-zenoh/zenoh-cpp/blob/main/examples/zenohc/z_querier.cxx), and [Python](https://github.com/eclipse-zenoh/zenoh-python/blob/main/examples/z_querier.py).

`#[tokio::main]
async fn main() {
 let session = zenoh::open(Config::default()).await.unwrap();
 let querier = session
 .declare_querier(selector.key_expr())
 .target(target)
 .timeout(timeout)
 .await
 .unwrap();
 querier
 .matching_listener()
 .callback(|matching_status| {
 if matching_status.matching() {
 println!("Querier has matching query tables.");
 } else {
 println!("Querier has NO MORE matching queryables.");
 }
 })
 .background()
 .await
 .unwrap();
 for idx in 0..u32::MAX {
 tokio::time::sleep(Duration::from_secs(1)).await;
 let replies = querier
 .get()
 .await
 .unwrap();
 while let Ok(reply) = replies.recv_async().await {
 let _ = reply.result().unwrap()
 }
 }
}`

## Zenoh-Pico

### Manual Batching

Rust-based implementation APIs (i.e. C, C++, Python, Kotlin, Java) offer automatic message batching. In other words, Zenoh automatically batches messages based on the network backpressure to both increase throughput and reduce latency.

This wonderful automatic magic comes with some complexity that was considered too high for fitting in microcontrollers targeted by Zenoh-Pico (memory is quite expensive…). But does it mean we cannot have batching in Zenoh-Pico? Not at all! In this release we have introduced a simple API that allows users to explicitly control message batching. Please note that manual batching will make Zenoh-Pico to batch messages until the sending batch is full (the maximum batch size is 64KB and it can be configured to a smaller value). When the batch is full, Zenoh-Pico will automatically send the batch on the network.

`int main(int argc, char **argv) {
 z_view_keyexpr_t ke;
 z_view_keyexpr_from_str(&ke, "example/batching");
 uint8_t value = 0x55;
 z_owned_bytes_t payload;
 z_bytes_from_buf(&payload, &value, 1, NULL, NULL);
 z_owned_config_t config;
 z_config_default(&config);
 z_owned_session_t s;
 z_open(&s, z_move(config), NULL);
 zp_start_lease_task(z_loan_mut(s), NULL);
 zp_start_read_task(z_loan_mut(s), NULL);
 zp_batch_start(z_loan(s)); // Start batching
 for (int i = 0; i < 1000000; i++) {
 z_owned_bytes_t p;
 z_bytes_clone(&p, z_loan(payload));
 z_put(z_loan(s), z_loan(ke), z_move(p), NULL);
 }
 zp_batch_stop(z_loan(s)); // Stop batching
 z_drop(z_move(s));
 z_drop(z_move(payload));
 return 0;
}`

### Rasberry Pi Pico

We are excited to announce support for the Raspberry Pi Pico series in Zenoh-Pico! This addition makes it possible to leverage Zenoh-Pico’s lightweight and efficient communication capabilities on `RP2040/RP2350`-based devices.
To get started, check out the new Raspberry Pi Pico section in the [README](https://github.com/eclipse-zenoh/zenoh-pico?tab=readme-ov-file#226-raspberry-pi-pico). This includes detailed instructions for building and running Zenoh-Pico on Pico devices, enabling seamless integration into your IoT projects.

`RP2040/RP2350`

### Performance

A lot of effort has been devoted to improving throughput and latency performance in Zenoh-Pico. A big improvement has been brought by:

Notably, the latency has been reduced to up to 1/50th (i.e. 5000% better) for large fragmented messages and up to 35% for non-fragmented messages. Moreover, the throughput has increased up to 60% for non-fragmented messages and up to 10x (i.e. 1000% better) for large fragmented messages in peer-to-peer over UDP multicast (§). In client mode, the throughput has been increased up to 10x (i.e. 1000% better) for large messages.
Enabling manual batching can increase throughput of non-fragmented packets, with up to 20x (i.e. 2000% better) msg/s for 8 byte payloads.

(§) Zenoh-Pico only supports UDP multicast in peer mode.

## ROS 2 Bridge

ROS 2 Iron and Jazzy introduced some changes that the `zenoh-plugin-ros2dds` and `zenoh-bridge-ros2dds` now support.

`zenoh-plugin-ros2dds`
`zenoh-bridge-ros2dds`

The **Type Description Distribution**, a.k.a. [REP-2016](https://github.com/ros-infrastructure/rep/pull/381) or type hash: The bridge re-transmit the type hashes exposed by the ROS Nodes to the remote bridges, so they re-expose them in the same way to remote ROS Nodes.

`ROS_AUTOMATIC_DISCOVERY_RANGE` and `ROS_STATIC_PEERS`: The bridge supports those new environment variables starting from Iron, and still supports the `ROS_LOCALHOST_ONLY` environment variables with ROS distributions prior to Iron.

`ROS_AUTOMATIC_DISCOVERY_RANGE`
`ROS_STATIC_PEERS`
`ROS_LOCALHOST_ONLY`

The `zenoh-bridge-ros2dds` now also leverages the new Querier and its matching status. This means that implementing a Zenoh Queryable which is able to act as a ROS Service Server no longer requires the declaration of a Liveliness Token to be discovered by the bridge.

`zenoh-bridge-ros2dds`

## Advanced Pub/Sub

This version introduces:

Examples:

`// Advanced Publisher
use zenoh_ext::{AdvancedPublisherBuilderExt, CacheConfig};
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let publisher = session
 .declare_publisher("key/expression")
 .cache(CacheConfig::default().max_samples(10))
 .sample_miss_detection()
 .publisher_detection()
 .await
 .unwrap();
publisher.put("Value").await.unwrap();`
`// Advanced Subscriber
use zenoh_ext::{AdvancedSubscriberBuilderExt, HistoryConfig, RecoveryConfig};
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let subscriber = session
 .declare_subscriber("key/expression")
 .history(HistoryConfig::default().detect_late_publishers())
 .recovery(RecoveryConfig::default())
 .await
 .unwrap();
let miss_listener = subscriber.sample_miss_listener().await.unwrap();
loop {
 tokio::select! {
 sample = subscriber.recv_async() => {
 if let Ok(sample) = sample {
 // ...
 }
 },
 miss = miss_listener.recv_async() => {
 if let Ok(miss) = miss {
 // ...
 }
 },
 }
}`

Connectivity Status and Events have been updated to be retrievable through an AdvancedSubscriber (see [Connectivity Status and Events](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Connectivity%20Status%20and%20Events.md#using-the-advancedsubscriber)).
The FetchingSubscriber and PublicationCache have been marked as deprecated.

## Miscellaneous

**TCP buffers**: TCP and TLS links got more tuning options with the introduction of TCP buffers configuration. Users can now configure read/write TCP buffer sizes with custom values, independently for each endpoint via endpoint configuration (ex: `tcp/[::]:7447#so_sndbuf=65000;so_rcvbuf=65000`) or per protocol basis via the Zenoh config file, respectively in the `transport/link/tcp` and `transport/link/tls` sections.

`tcp/[::]:7447#so_sndbuf=65000;so_rcvbuf=65000`
`transport/link/tcp`
`transport/link/tls`

**QUIC/TLS Interface Binding**: Interface binding for Zenoh links has been available on Linux for TCP and UDP for some time now. In this release, we have extended the support of interface binding to TLS and QUIC links, via the same endpoint configuration format (ex: `tls/[::]:7447#iface=wlan0`).

`tls/[::]:7447#iface=wlan0`

**Publisher QoS Overwrites**: A new performance-tuning feature introduced in this release is the capability of overwriting QoS configuration of publishers, namely: priority, reliability, congestion control, and express. All the configuration happens via the newly added `qos/publications` section of the Zenoh config file.
A publisher configuration can be passed per key-expression, which will overwrite any publisher or `put` operation with a key-expression that it includes (see more about key-expression inclusion in the [Key Expressions RFC](https://github.com/eclipse-zenoh/roadmap/blob/73b2d4bad44bf35638f97d449907da6f79ec6f9b/rfcs/ALL/Key%20Expressions.md#the-basics)).
As the name implies, QoS overwrites take priority over the publishers and `put` builders API, which makes them quite handy when using a library that uses Zenoh but does not expose the publisher QoS API, or when debugging or tuning a black-box Zenoh application.

`qos/publications`
`put`
`put`

## Changelogs

The effort behind Zenoh 1.1.0 resulted in a large number of bug fixes and improvements. The full changelog for every Zenoh repository is available at the following links: [Rust](https://github.com/eclipse-zenoh/zenoh/releases) | [C](https://github.com/eclipse-zenoh/zenoh-c/releases) | [C++](https://github.com/eclipse-zenoh/zenoh-cpp/releases) | [Python](https://github.com/eclipse-zenoh/zenoh-python/releases) | [Kotlin](https://github.com/eclipse-zenoh/zenoh-kotlin/releases) | [Pico](https://github.com/eclipse-zenoh/zenoh-pico/releases) | [DDS plugin](https://github.com/eclipse-zenoh/zenoh-plugin-dds/releases) | [ROS2 plugin](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds/releases) | [MQTT plugin](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt/releases) | [WebServer plugin](https://github.com/eclipse-zenoh/zenoh-plugin-webserver/releases/tag/1.0.4) | [Filesystem backend](https://github.com/eclipse-zenoh/zenoh-backend-filesystem/releases) | [RocksDB backend](https://github.com/eclipse-zenoh/zenoh-backend-rocksdb/releases) | [S3 backend](https://github.com/eclipse-zenoh/zenoh-backend-s3/releases) | [InfluxDB backend](https://github.com/eclipse-zenoh/zenoh-backend-influxdb/releases)

## What’s next?

Whether you are working with Rust, C, C++, Python, or other supported languages, this update addresses the feedback we received from the community and empowers Zenoh developers with new tools. Make sure to explore all these updates by trying out Zenoh Firesong 1.1.0. Thanks to all contributors and users!

Happy Hacking,
– The Zenoh Team

P.S. You can reach us out on [Zenoh’s Discord server](https://discord.com/invite/vSDSpqnbkm)!

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2025-01-08-introducing-raspberry-pi-pico-support-in-zenoh-pico/

Source: https://zenoh.io/blog/2025-01-08-introducing-raspberry-pi-pico-support-in-zenoh-pico/

![](../../img/zenoh-dragon-bg-150x163.png)

# Introducing Raspberry Pi Pico Support in Zenoh-Pico

Blog Posts

# Introducing Raspberry Pi Pico Support in Zenoh-Pico

January 8th, 2025 -- Paris.

# Introducing Raspberry Pi Pico Support in Zenoh-Pico

We’re excited to announce that Zenoh-Pico now supports the Raspberry Pi Pico series, including the Pico W and Pico 2 W variants! Zenoh already runs seamlessly on platforms like the Raspberry Pi Zero, providing robust communication solutions for IoT. Now, with the addition of Raspberry Pi Pico support, we’ve expanded the Zenoh ecosystem to even smaller and more constrained devices.

![Raspberry Pi Pico Family](../../img/20250108-Introducing-Raspberry-Pi-Pico-Support-in-Zenoh-Pico/pico-family.jpg)

## What is Zenoh-Pico?

Zenoh-Pico is the lightweight, native C implementation of the [Eclipse Zenoh](http://zenoh.io) protocol, designed specifically for constrained devices. It provides a streamlined, low-resource API while maintaining compatibility with the main [Rust Zenoh implementation](https://github.com/eclipse-zenoh/zenoh). Zenoh-Pico already supports a broad range of platforms and protocols, making it a versatile choice for embedded systems development.

## Why Raspberry Pi Pico?

The [Raspberry Pi Pico family](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) is a cost-effective, feature-rich microcontroller platform based on the [RP2040](https://www.raspberrypi.com/documentation/microcontrollers/silicon.html#rp2040)/[RP2350](https://www.raspberrypi.com/documentation/microcontrollers/silicon.html#rp2350) chips. With its dual-core Arm Cortex-M0+ processor (or more advanced processors in the Pico 2 series), low power consumption, and extensive GPIO options, it’s a favorite among hobbyists and professionals alike. The addition of integrated Wi-Fi in the Pico W and Pico 2 W variants makes the platform even more suitable for IoT applications.

With Zenoh-Pico’s support, developers can now leverage the Raspberry Pi Pico family for reliable and efficient data communication over:

## Technical Architecture

Zenoh-Pico for Raspberry Pi Pico uses the **Raspberry Pi Pico SDK** for hardware interfacing and communication protocols. It also integrates **FreeRTOS** to manage tasks and scheduling, providing a robust framework for real-time operations. This combination ensures efficient and reliable performance even under constrained conditions.

## Getting Started

Here’s how you can set up Zenoh-Pico examples on your Raspberry Pi Pico using Ubuntu 24.04:

### 1. Installation Prerequisites

Ensure your system has the required tools and libraries:

`sudo apt update
sudo apt install -y cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential g++ libstdc++-arm-none-eabi-newlib`

### 2. Set Up the Pico SDK

Clone and initialize the Raspberry Pi Pico SDK:

`export PICO_SDK_PATH=$HOME/src/pico-sdk
mkdir -p $PICO_SDK_PATH
cd $PICO_SDK_PATH
git clone https://github.com/raspberrypi/pico-sdk.git .
git submodule update --init`

### 3. Prepare the FreeRTOS Kernel

Clone the FreeRTOS Kernel repository:

`export FREERTOS_KERNEL_PATH=$HOME/src/FreeRTOS-Kernel/
mkdir -p $FREERTOS_KERNEL_PATH
cd $FREERTOS_KERNEL_PATH
git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git .
git submodule update --init`

### 4. Build the Examples

Navigate to the example directory and build them:

`git clone //github.com/eclipse-zenoh/zenoh-pico.git .
cd zenoh-pico/examples/rpi_pico
cmake -Bbuild -DPICO_BOARD="pico_w" -DWIFI_SSID=wifi_network_ssid -DWIFI_PASSWORD=wifi_network_password -DZENOH_CONFIG_MODE=client -DZENOH_CONFIG_CONNECT="tcp/router_address:7447"
cmake --build ./build`

### 5. Flash Your Raspberry Pi Pico device

Connect the Raspberry Pi Pico in bootloader mode and copy one of the generated `.uf2` files onto the device.

`.uf2`

## Connectivity Options

### Serial Connection

To connect via UART, specify pins or predefined device name and baud rate:

e.g.

`-DZENOH_CONFIG_CONNECT="serial/0.1#baudrate=38400"
-DZENOH_CONFIG_CONNECT="serial/uart1_0#baudrate=38400"`

Valid PIN combinations and associated device names for Raspberry Pi Pico:

### USB Serial Connection (Experimental)

Enable this feature by compiling Zenoh-Pico with:

`-DZ_FEATURE_LINK_SERIAL_USB -DZ_FEATURE_UNSTABLE_API`

To connect via USB CDC, use:

`-DZENOH_CONFIG_CONNECT="serial/usb#baudrate=112500"`

On the host side, run:

`zenohd -l serial//dev/ttyACM0#baudrate=112500`

## Let’s Run the Zenoh Family on the Raspberry Pi Family

The flexibility of Zenoh allows for powerful and efficient IoT deployments across the Raspberry Pi ecosystem. Here’s an example scenario.

### Set Up the Zenoh Router

Install the Zenoh Router on a Raspberry Pi Zero:

`wget https://github.com/eclipse-zenoh/zenoh/releases/download/1.1.0/zenoh-1.1.0-armv7-unknown-linux-gnueabi-standalone.zip
unzip zenoh-1.1.0-armv7-unknown-linux-gnueabihf-standalone.zip`

Start the Zenoh router:

`./zenohd`

Find the locator in the router output:

`2025-01-03T16:24:17.204829Z INFO main ThreadId(01) zenoh::net::runtime::orchestrator: Zenoh can be reached at: tcp/192.168.0.207:7447`

### Build Pico W Clients

Configure Zenoh-Pico Raspberry Pi Pico examples as it was shown above, but specify to use our router IP and build it:

`cmake -Bbuild -DPICO_BOARD="pico_w" -DWIFI_SSID=WIFI_SSID -DWIFI_PASSWORD=********* -DZENOH_CONFIG_MODE=client -DZENOH_CONFIG_CONNECT="tcp/192.168.0.207:7447"
cmake --build ./build`

### Deploy Pico W Clients

Hold the BOOTSEL button on Raspberry Pi Pico W and attach it to the USB port.

Copy compiled z\_pub firmware image:

`cp ./build/z_pub.uf2 /media/${USER}/RPI-RP2`

Do the same with the z\_sub and second Raspberry Pi Pico W device:

`cp ./build/z_sub.uf2 /media/${USER}/RPI-RP2`

### Check output

Connect to the Pico W Subscriber to check output:

`❯ sudo tio /dev/ttyACM0 -e -m INLCRNL,ONLCRNL -b 115200
[18:12:42.639] Press ctrl-t q to quit
[18:12:46.643] Connected to /dev/ttyACM0
Wi-Fi connected.
IP Address: 192.168.0.249
Netmask: 255.255.255.0
Gateway: 192.168.0.3
Connect endpoint: tcp/192.168.0.207:7447
Opening client session ...
Declaring Subscriber on 'demo/example/**'...
>> [Subscriber] Received ('demo/example/zenoh-pico-pub': '[ 0] [RPI] Pub from Zenoh-Pico!')
>> [Subscriber] Received ('demo/example/zenoh-pico-pub': '[ 1] [RPI] Pub from Zenoh-Pico!')
>> [Subscriber] Received ('demo/example/zenoh-pico-pub': '[ 2] [RPI] Pub from Zenoh-Pico!')
>> [Subscriber] Received ('demo/example/zenoh-pico-pub': '[ 3] [RPI] Pub from Zenoh-Pico!')
>> [Subscriber] Received ('demo/example/zenoh-pico-pub': '[ 4] [RPI] Pub from Zenoh-Pico!')`

This setup showcases the seamless integration of Zenoh-Pico on Raspberry Pi Pico devices with a Zenoh router running on Raspberry Pi Zero, creating a scalable and efficient IoT ecosystem.

## Memory Usage Insights

Running Zenoh-Pico on the Raspberry Pi Pico W provides impressive efficiency. Here’s a brief summary of memory usage:

**Flash Usage**: A basic configuration provided above consumes approximately 80 KB of flash memory.

It is around 20% for Raspberry Pi Pico or 10 % for Raspberry Pi Pico 2 !

**RAM Usage**: Zenoh typically uses around 12 KB of RAM for this configuration.

It is around 5% for Raspberry Pi Pico or 2% for Raspberry Pi Pico 2 !

## Future-Proofing IoT Applications

With support for the Raspberry Pi Pico, Zenoh-Pico continues to lead in providing robust, scalable, and efficient communication solutions for constrained devices. Whether you’re building home automation systems, industrial IoT solutions, or experimenting with new ideas, Zenoh-Pico and Raspberry Pi Pico make a powerful combination.

Additionally, the main Rust-based Zenoh implementation is fully compatible with the Raspberry Pi Zero, making it an excellent choice for edge routers in distributed systems.

We’re eager to see what the community builds with this new capability! For more details, check out the [Zenoh-Pico repository](https://github.com/eclipse-zenoh/zenoh-pico) and join the discussion on our [community channels](http://zenoh.io/community/).

Let’s build the future of IoT together!

**– [Alexander Bushnev](https://github.com/sashacmc)**

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2025-04-09-zenoh-pico-performance/

Source: https://zenoh.io/blog/2025-04-09-zenoh-pico-performance/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh-Pico performance improvements

Blog Posts

# Zenoh-Pico performance improvements

April 30th, 2025 -- Paris.

# Improving Zenoh-Pico performance

Last year, after the long-awaited release of Zenoh 1.0 which included a unified C API with Zenoh-C and Zenoh-Pico, we decided to dedicate some time to measure and improve the performance and efficiency of Zenoh-Pico. These modifications were released with Zenoh 1.1 earlier this year and we present the results to you with this blog post.

## What is Zenoh-Pico?

Zenoh-Pico is the lightweight, native C implementation of the [Eclipse Zenoh](http://zenoh.io) protocol, designed specifically for constrained devices. It provides a streamlined, low-resource API while maintaining compatibility with the main [Rust Zenoh implementation](https://github.com/eclipse-zenoh/zenoh). Zenoh-Pico already supports a broad range of platforms and protocols, making it a versatile choice for embedded systems development.

## The results

To measure performance, we have a standardized throughput test and a latency test which we run on a standardized machine (Intel Xeon E3-1275 @3.6GHz, 32GB DDR4, Ubuntu 22.04). For embedded measurements, we ran those tests on an ESP32-WROOM-32 dev board.

These tests produce a thousand measurements or so per payload size that we use to calculate the median value to then get the following graphs (note that the y-axis is log scale):

### PC throughput client, TCP:

![Client throughput](../../img/20250430-Zenoh-Pico-Performance/zpperf1.png)

We see a massive (up to 100x) improvement in throughput for payloads over 32KiB, this is because packets of these sizes are fragmented on the network and we had an issue where their data was serialized byte-by-byte.

We also see a >10x improvement in throughput for smaller payloads when using manual batching (more info below) introduced in 1.1 as well.

Other than that there are no significant changes because client performance is limited by the router.

### PC throughput peer to peer, UDP multicast:

![Peer throughput](../../img/20250430-Zenoh-Pico-Performance/zpperf2.png)

Peer to peer being not limited by router performance, we observe a bigger improvement on smaller payloads with batching (>20x), but a smaller one (>10x) for fragmented packets (>2KiB) because of UDP’s smaller packet size.

In addition, we observe a 60% throughput increase for the other payload sizes, that results from the general library optimization.

### PC latency:

![PC latency](../../img/20250430-Zenoh-Pico-Performance/zpperf3.png)

This plot shows a >50x enhancement on fragmented packets latency, again due to data copy improvement, but also a 35% boost across the board from the general library optimization.

Note that a big chunk of the latency value is due to the router (node to router hop + time to route the packet + router to node hop), and this value could be much lower using peer to peer TCP unicast.

### Performance limitations/regime:

Before going into embedded results, let’s spend some time in understanding what are the limiting factors of performance.

![Throughput limitations](../../img/20250430-Zenoh-Pico-Performance/zpperf6.png)

For throughput there are 3 distinctive regions:

`send`
`recv`
`memcpy`
![Latency limitations](../../img/20250430-Zenoh-Pico-Performance/zpperf7.png)

For latency there are 2 regions:

### Embedded throughput:

Embedded systems being limited memory-wise, we limited payload sizes to 4KiB maximum which is still enough to observe fragmented packets behavior for 2KiB and 4KiB sizes.

![Peer throughput](../../img/20250430-Zenoh-Pico-Performance/zpperf4.png)

The ESP32 really benefits from batching with a >50x increase in throughput, which seems fair since we’re going through a much slower Wi-Fi interface compared to loopback that uses unix pipe.

### Embedded latency:

![Peer throughput](../../img/20250430-Zenoh-Pico-Performance/zpperf5.png)

Latency values are in the ~10ms range mostly because Wi-Fi itself is slow as demonstrated by the ~4ms value observed on Zenoh-Pico PC latency measured on the same Wi-Fi network.

We do observe a big impact on latency when trying to send fragmented packets which should come from both Wi-Fi and ESP32 bandwidth limitation.

## How performance was improved

To improve Zenoh-Pico performance, we traced it on PC using [samply](https://github.com/mstange/samply) and the Firefox debugger to visualize the traces. That allowed us to detect choke points and parts of the code that could be improved.

As stated earlier, the most impactful changes were solving the byte-by-byte copy issue for fragmented packets and the introduction of the manual batching mechanism.

Besides that, we also streamlined a lot how the stack created, used and destroyed data to avoid redundant operations or unnecessary data copies. We also rationalized heap memory usage and fragmentation although these changes were not quantified.

## Manual Batching

If you want to use Zenoh-Pico recently introduced manual batching you only have 3 things to know about:

`zp_batch_start`
`z_put`
`z_get`
`zp_batch_stop`
`zp_batch_flush`

Note that there are also cases where a batch will be sent if a message needs to be sent immediately, like when sending keep-alive messages or if the API pushes a message with the `is_express` QOS.

`is_express`

### Examples:

In this example we will batch all the messages and send them in bulk to improve throughput. Every time the batch is full, it will be sent and the last one will be sent with the `zp_batch_stop` call:

`zp_batch_stop`
 `zp_batch_start(z_loan(session));
 z_owned_bytes_t p;
 while (cnt < n) {
 // Clone payload
 z_bytes_clone(&p, z_loan(payload));
 z_publisher_put(z_loan(pub), z_move(p), NULL);
 cnt++;
 }
 zp_batch_stop(z_loan(session));`

In this second example, another thread is responsible for sending messages and we want to batch them to avoid too many packets on the network, but we might want to limit latency, so we add a loop that will flush the batch periodically.

 `zp_batch_start(z_loan(session));
 // Wait for other thread to add messages
 while(is_running){
 elapsed_us = z_clock_elapsed_us(&time_start);
 // Flush buffer periodically
 if (elapsed_us > 10000) {
 zp_batch_flush(z_loan(session));
 time_start = z_clock_now();
 }
 z_sleep_ms(1);
 }
 zp_batch_stop(z_loan(session));`

## Wrapping up

As you saw, we improved throughput and latency across the board, in some cases reaching a 100x increase.

We also introduced manual batching which, beside improving throughput of small messages, can be used to reduce power consumption in embedded devices by reducing network transmissions.

Now let’s talk briefly of our next big feature. As we hinted above, we are limited in client mode by the router both in throughput and latency, but client mode is currently the only way to use TCP links in Zenoh-Pico…

That was true until the newly introduced peer-to-peer unicast mode that we will present in a future blog post!

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2025-04-14-zenoh-gozuryu/

Source: https://zenoh.io/blog/2025-04-14-zenoh-gozuryu/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh Gozuryū is Here!

Blog Posts

# Zenoh Gozuryū is Here!

14th April, 2025 -- Paris.

We are thrilled to announce the release of Zenoh 1.3.3 – **Gozuryū**!

Named after the legendary “Five-Headed Dragon”, this release brings a powerful set of new capabilities across the entire Zenoh ecosystem, with improvements touching everything from core routing and shared memory to the language bindings and Zenoh-Pico for constrained devices.

Let’s dive into the highlights of this release.

**Namespace Prefix Support**: Isolate Zenoh sessions with namespace prefixes — ideal for multi-robot and multi-instance setups.

**Peer-to-Peer Unicast in Zenoh-Pico**: Zenoh-Pico now supports direct unicast communication, enabling router-less setups in constrained environments.

**Automatic Reconnect (Zenoh-Pico)**: Sessions can now automatically recover from disconnections, including declaration restoration.

**Shared Memory Performance Boost**: Up to **35% throughput improvements**, with new mutation examples and memory control options.

**Advanced Pub/Sub Enhancements**: Heartbeat support and zero-copy buffer management now available in Zenoh-C and Zenoh-Cpp.

**QoS Rewrite & Filtering Interceptors**: New routing interceptors allow message filtering and QoS adjustments at runtime.

**Resource Usage Optimizations**: Significant reductions in memory and CPU usage, especially on multi-interface systems.

These are just the highlights — Zenoh 1.3.3 comes packed with enhancements across the entire ecosystem, from core protocol upgrades to binding-specific improvements in C, C++, TypeScript, Java/Kotlin, and Zenoh-Pico. In the sections below, we’ll take a closer look at what’s new, what’s faster, and what’s now possible with **Gozuryū**.

## Zenoh

### Namespace prefix support

In the latest release we introduced the concept of session namespaces. A namespace can be viewed as a prefix that is automatically prepended to key expressions of all messages that are sent outside of the session. This includes publications, queries, replies, \ subscriber, queryable and liveliness token declarations.

If we declare a session to have a namespace `"my_namespace"` and call `session.put("my_keyexpr", my_data)` then for everyone *outside* the namespace,i.e., all subscribers declared on sessions without any namespace, this will look like a put on `"my_namespace/my_keyexpr"`, while subscribers declared for the sessions with same namespace will see it as a put on `"my_keyexpr"`.

`"my_namespace"`
`session.put("my_keyexpr", my_data)`
`"my_namespace/my_keyexpr"`
`"my_keyexpr"`

Let us illustrate this with an example:

put.rs

`#[tokio::main]
async fn main() {
 let mut config = Config::default();
 config.insert_json5("namespace", "\"my_namespace\"").unwrap();
 let session = zenoh::open(config).await.unwrap();
 session.put("my_keyexpr","my_data".to_string()).await.unwrap();
}`

sub\_in\_namespace.rs

`#[tokio::main]
async fn main() {
 let mut config = Config::default();
 config.insert_json5("namespace", "\"my_namespace\"").unwrap();
 let session = zenoh::open(config).await.unwrap();
 let subscriber = session.declare_subscriber("my_keyexpr").await.unwrap();
 while let Ok(sample) = subscriber.recv_async().await {
 println!(
 ">> [Subscriber] Received ('{}': '{}')",
 sample.key_expr().as_str(),
 sample.payload().try_to_string().unwrap(),
 );
 }
}`

sub\_outside\_of\_namespace.rs

`#[tokio::main]
async fn main() {
 let mut config = Config::default();
 let session = zenoh::open(config).await.unwrap();
 let subscriber = session.declare_subscriber("my_namespace/my_keyexpr").await.unwrap();
 while let Ok(sample) = subscriber.recv_async().await {
 println!(
 ">> [Subscriber] Received ('{}': '{}')",
 sample.key_expr().as_str(),
 sample.payload().try_to_string().unwrap(),
 );
 }
}`

Both `sub_in_namespace.rs` and `sub_outside_of_namespace.rs` will receive the message of `put.rs`. The former will output:

`sub_in_namespace.rs`
`sub_outside_of_namespace.rs`
`put.rs`

`>> [Subscriber] Received (‘my_keyexpr': ‘my_data’)`, while the latter will output:
`>> [Subscriber] Received (‘my_namespace/my_keyexpr’: ‘my_data’)`.

`>> [Subscriber] Received (‘my_keyexpr': ‘my_data’)`
`>> [Subscriber] Received (‘my_namespace/my_keyexpr’: ‘my_data’)`

Namespaces can be useful when one needs to avoid name collisions when running the same code on different instances, in multi-robot scenarios for example. Additionally they can be used if isolation between different instances is required, since non-intersecting namespaces will never receive each other’s messages, since they will start with different prefixes. It is a feature that comes handy when integrating systems too.

Any string satisfying key expression constraints and not including wildcard chunks (i.e. `"*"`, `"**"`, or `"$*"`) can be used as a namespace.

`"*"`
`"**"`
`"$*"`

### Multicast TTL Configuration

Multicast communication now supports a configurable TTL (Time-To-Live) parameter. Previously, multicast packets were restricted to a TTL of 1, preventing them from traversing routers. With this update, users can specify a TTL value when establishing a multicast connection, ensuring that traffic can reach beyond a local network. For example:

`./z_pub -m peer -l 'udp/239.1.3.37:9001#iface=myinterface;ttl=32' -k 'testkey' -p 'Hello beyond the router'`

### Configurable Interests Timeout

The interests protocol timeout, previously hardcoded to 10 seconds, is now configurable via `routing.interests.timeout`. This allows users to fine-tune interest tracking behavior based on network conditions and application requirements. The default remains 10 seconds, but adjusting this parameter can help optimize message delivery in dynamic environments.

`routing.interests.timeout`

### Improved Link Establishment Timeout

A default timeout for new link establishment has been introduced. While link acceptance already had a 10-second timeout, establishing a new link lacked a similar safeguard. This update ensures that connections do not fail prematurely due to incorrect timeout handling, improving connection stability and retry mechanisms. Default value can be changed via `transport.unicast.open_timeout` parameter.

`transport.unicast.open_timeout`

### Advanced Pub/Sub Heartbeat

Advanced Pub/Sub was introduced in [Zenoh v1.1.0](https://zenoh.io/blog/2024-12-12-zenoh-firesong-1.1.0/#advanced-pubsub) to provide end-to-end reliability even in presence of router crashes and networks reconfiguration. In the initial implementation, when using samples sequencing, if the last sent sample was lost and no other samples were published, the AdvancedSubscriber would not detect the miss. One way to address this issue was to enable periodic queries, but those are costly.

Zenoh version 1.3.3 introduces a `heartbeat` message that can optionally be sent by the AdvancedPublishers and indicates to the AdvancedSubscribers what are the available samples for recovery. This message can be sent periodically (version 1.3.0) or sporadically (only when new samples are available) with `CongestionControl::Block` to ensure its reception (version 1.3.2).

`heartbeat`
`CongestionControl::Block`

### Improved locator metadata syntax

Link locators support a priority range metadata value (i.e. `prio`) that instructs Zenoh to use the link in question to transmit messages whose priority falls within the given range. For single-value ranges, you can now write `tcp/localhost:0?prio=1` instead of `tcp/localhost:0?prio=1-1` — something that proved confusing and unnatural for users.

`prio`
`tcp/localhost:0?prio=1`
`tcp/localhost:0?prio=1-1`

### New Interceptors and general interceptor framework improvements

In this release we introduce 2 new interceptor types:

Low-pass filter (configurable through low\_pass\_filter field in the config) which limits the maximum size of incoming or outgoing messages.

QoS Overwrite (configurable through qos/network field in the config) which allows the router (or peer) to overwrite QoS settings of the messages it propagates.

In addition existing interceptor framework received some substantial improvements:

Whenever possible, interceptors now cache the data necessary to process the messages for the given key-expression, which significantly improves their performance.

Downsampling interceptor now works with **query** and **reply** message types.

All interceptor rules can now be restricted to specific link protocols (i.e. one can define rules which are only applied to TCP or TLS links for example).

### Shared Memory Just Got Better

The shared memory subsystem, first introduced in [Zenoh v1.0.0](https://zenoh.io/blog/2024-10-21-zenoh-firesong/), continues to evolve with new improvements and optimizations aimed at performance and flexibility.

#### Mutation Examples in Rust, C, and C++

First up: we’ve added mutation examples for shared memory buffers in [Rust](https://github.com/eclipse-zenoh/zenoh/blob/94e917948914af093eae340ee52118b19fb1671f/examples/examples/z_sub_shm.rs#L91), [C](https://github.com/eclipse-zenoh/zenoh-c/blob/18eed6fecf2c52e8c822b3b8c77d92f620b6e120/examples/z_sub_shm.c#L50), and [C++](https://github.com/eclipse-zenoh/zenoh-cpp/blob/e3f9bfc977a72a03668537eca6f03e4bbbe130c7/examples/zenohc/z_sub_shm.cxx#L58).
These examples extend our common `z_sub_shm` demo, adding a mutation attempt to show whether the received buffer is actually mutable. This gives developers more insight into how to handle SHM buffer mutation functionality.

`z_sub_shm`

#### Performance Boosts

We’ve also done a lot of under-the-hood optimization. By reducing computational complexity and memory footprint in the SHM internals, we’ve managed to boost message-per-second performance by a solid **35%**.

#### New Configuration Option for Initialization Behavior

Previously, SHM internal resources were always initialized lazily—the first time your application touched shared memory (typically on the first buffer allocation or reception). This approach worked well for most use cases, keeping memory usage and startup time low. But it introduced a one-time latency spike that wasn’t ideal in latency-sensitive scenarios.

Now, we’ve introduced a [new configuration option](https://github.com/eclipse-zenoh/zenoh/blob/94e917948914af093eae340ee52118b19fb1671f/DEFAULT_CONFIG.json5#L681) to give you control over SHM initialization behavior. You can choose between lazy or eager initialization, depending on what best fits your application.

### Resources consumption improvements

Some major reduction of CPU and memory consumption have been introduced that allow for better scalability.

Network interface scanning to compute locators is a very CPU expensive task that is now only performed once at startup.

Various improvements have been made in the routing to decrease CPU and memory consumption.

Changes have been made in the default size and allocation policies of the Zenoh internal queues that significantly decrease memory consumption.

Here is a graph of CPU and memory consumption running a Zenoh router and 100 ROS2 nodes (50 publishers and 50 subscribers) on a same host (4 cores 8GB RAM):

![CPU and memory consumption](../../img/20250414-zenoh-gozuryu/zenoh_perf.png)

![CPU and memory consumption](../../img/20250414-zenoh-gozuryu/zenoh_perf.png)

## Zenoh-Pico

### Add p2p unicast support

In the latest release, we have introduced peer-to-peer (P2P) unicast support in Zenoh-Pico, allowing applications to establish unicast links without the need for a central router – thus far, peer-to-peer was only available in combination with the use of UDP multicast.

This is particularly beneficial in scenarios where reliability, low-latency and high-throughput communication are crucial.

This addition aligns with Zenoh-Pico’s goal of providing robust communication solutions for constrained devices, further expanding its use cases in IoT and embedded.

A blog post will go into more detail about the feature and its limitations but if you want to try it right now:

First, run a Zenoh-pico example on your machine as a tcp server:

`./build/examples/z_sub -m peer -l tcp/127.0.0.1:7447`

`./build/examples/z_sub -m peer -l tcp/127.0.0.1:7447`

And run a few other examples as clients:

`./build/examples/z_pub -m peer -e tcp/127.0.0.1:7447`

`./build/examples/z_pub -m peer -e tcp/127.0.0.1:7447`

### Connection restoring

When network disruptions occur, whether due to temporary connectivity issues or router restarts, Zenoh-Pico now automatically attempts to restore its connection. This new functionality, introduced under the `Z_FEATURE_AUTO_RECONNECT` flag (enabled by default), enhances reliability by detecting lost connections and seamlessly reestablishing them. Additionally, it caches declarations and restores them after reconnection, ensuring a smooth recovery without manual intervention. With this improvement, applications using Zenoh-Pico can handle transient failures more gracefully, reducing the risk of silent data loss and aligning Zenoh-Pico’s resilience more closely with Zenoh. For memory-constrained environments, the feature can be disabled to optimize resource usage.

`Z_FEATURE_AUTO_RECONNECT`

### Querier

Zenoh-Pico now supports queriers, bringing query-side optimizations similar to those available for publishers. Just as publishers enable Zenoh to optimize continuous data dissemination, queriers allow for efficient, stateful querying with features like write-side filtering and matching status. This addition enhances Zenoh-Pico’s ability to interact with distributed systems while maintaining minimal resource usage.

#### Declaring a Querier

A querier can be declared on a specific key expression, allowing queries to be issued dynamically:

`z_owned_querier_t querier;
if (z_declare_querier(z_loan(s), &querier, z_loan(keyexpr), NULL) < 0) {
 printf("Unable to declare Querier for key expression!\n");
 exit(-1);
}`

#### Sending a Query

Once declared, a querier can retrieve data from matching queryables in the system. Replies are handled asynchronously through a callback:

`void reply_handler(z_loaned_reply_t *reply, void *ctx) {
 if (z_reply_is_ok(reply)) {
 const z_loaned_sample_t *sample = z_reply_ok(reply);
 z_view_string_t keystr;
 z_keyexpr_as_view_string(z_sample_keyexpr(sample), &keystr);
 printf(">> Received '%.*s'\n",
 z_string_len(z_loan(keystr)),
 z_string_data(z_loan(keystr)));
 }
}
z_owned_closure_reply_t callback;
z_closure(&callback, reply_handler, NULL, NULL);
z_querier_get(z_loan(querier), params, z_move(closure), NULL);`

#### Cleaning Up

When no longer needed, the querier should be undeclared to release resources:

`z_drop(z_move(querier));`

A full example as well as working with the channel can be found [there](https://github.com/eclipse-zenoh/zenoh-pico/blob/main/examples/unix/c11/z_querier.c).

### Matching listeners

Zenoh-Pico now supports matching listeners, allowing publishers and queriers to detect when there are active subscribers or queriable matching their key expression. This feature provides applications with greater awareness of their communication state, optimizing resource usage and enabling more responsive behavior. The same functionality is also available in Zenoh-Cpp, ensuring consistency across implementations.

A matching listener can be declared using `z_publisher_declare_background_matching_listener`, which registers a callback that is triggered when the first subscriber connects or when the last subscriber disconnects:

`z_publisher_declare_background_matching_listener`
`void matching_status_handler(const z_matching_status_t *matching_status, void *arg) {
 (void)arg;
 if (matching_status->matching) {
 printf("Publisher has matching subscribers.\n");
 } else {
 printf("Publisher has NO MORE matching subscribers.\n");
 }
}
z_owned_closure_matching_status_t callback;
z_closure(&callback, matching_status_handler, NULL, NULL);
z_publisher_declare_background_matching_listener(z_loan(pub), z_move(callback));`

Alternatively, for more control, `z_publisher_declare_matching_listener` can be used, which allows explicit management of the listener’s lifecycle.

`z_publisher_declare_matching_listener`

### “Take from loaned” operation for callbacks

See the same-named section for Zenoh-C, the Zenoh-Pico API was updated in the same way.

## Zenoh-C

### Advanced Pub Sub

We are happy to share that Zenoh-C now supports [Advanced Pub/Sub API](%5Bhttps://zenoh.io/blog/2024-12-12-zenoh-firesong-1.1.0/#advanced-pubsub%5D(https://zenoh.io/blog/2024-12-12-zenoh-firesong-1.1.0/#advanced-pubsub)) introduced in Zenoh 1.1.0.

z\_advanced\_pub.c

`z_owned_config_t config;
z_config_default(&config);
zc_config_insert_json5(
 z_loan_mut(config), Z_CONFIG_ADD_TIMESTAMP_KEY, "true");
z_owned_session_t s;
z_open(&s, z_move(config), NULL);
z_view_keyexpr_t ke;
z_view_keyexpr_from_str(&ke, "key/expression");
ze_advanced_publisher_options_t pub_opts;
ze_advanced_publisher_options_default(&pub_opts);
pub_opts.cache.is_enabled = true;
pub_opts.cache.max_samples = 10;
pub_opts.publisher_detection = true;
pub_opts.sample_miss_detection.is_enabled = true
pub_opts.sample_miss_detection.heartbeat_period_ms = 500;
pub_opts.sample_miss_detection.heartbeat_mode = ZE_ADVANCED_PUBLISHER_HEARTBEAT_MODE_PERIODIC;
// if not set, publisher will retransmit samples based on periodic queries from advanced subscriber
ze_owned_advanced_publisher_t pub;
ze_declare_advanced_publisher(z_loan(s), &pub, z_loan(ke), &pub_opts);
z_owned_bytes_t payload;
z_bytes_copy_from_str(&payload, "some_data");
ze_advanced_publisher_put(z_loan(pub), z_move(payload), NULL);`

z\_advanced\_sub.c

`void data_handler(z_loaned_sample_t* sample, void* arg) {
 z_view_string_t key_string;
 z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_string);
 z_owned_string_t payload_string;
 z_bytes_to_string(z_sample_payload(sample), &payload_string);
 printf(">> [Subscriber] Received ('%.*s': '%.*s')\n",
 (int)z_string_len(z_loan(key_string)),
 z_string_data(z_loan(key_string)),
 (int)z_string_len(z_loan(payload_string)),
 z_string_data(z_loan(payload_string)));
 z_drop(z_move(payload_string));
}
void miss_handler(const ze_miss_t* miss, void* arg) {
 z_id_t id = z_entity_global_id_zid(&miss->source);
 z_owned_string_t id_string;
 z_id_to_string(&id, &id_string);
 printf(">> [Subscriber] Missed %d samples from '%.*s' !!!",
 miss->nb, (int)z_string_len(z_loan(id_string)),
 z_string_data(z_loan(id_string)));
 z_drop(z_move(id_string));
}
...
z_owned_config_t config;
z_config_default(&config);
z_owned_session_t session;
z_open(&session, z_move(config), NULL);
z_view_keyexpr_t ke;
z_view_keyexpr_from_str(&ke, "key/expression");
ze_advanced_subscriber_options_t sub_opts;
ze_advanced_subscriber_options_default(&sub_opts);
sub_opts.history.is_enabled = true;
sub_opts.history.detect_late_publishers = true;
sub_opts.recovery.is_enabled = true;
sub_opts.recovery.last_sample_miss_detection.is_enabled = true;
// use publisher heartbeats by default, otherwise enable periodic queries as follows:
// sub_opts.recovery.last_sample_miss_detection.periodic_queries_period_ms = 1000;
sub_opts.subscriber_detection = true;
z_owned_closure_sample_t callback;
z_closure(&callback, data_handler, NULL, NULL);
ze_owned_advanced_subscriber_t sub;
ze_declare_advanced_subscriber(
 z_loan(session), &sub, z_loan(ke),
 z_move(callback), &sub_opts);
ze_owned_closure_miss_t miss_callback;
z_closure(&miss_callback, miss_handler, NULL, NULL);
ze_advanced_subscriber_declare_background_sample_miss_listener(
 z_loan(sub), z_move(miss_callback));`

Complete examples can be found at [z\_advanced\_pub.c](https://github.com/eclipse-zenoh/zenoh-c/blob/main/examples/z_advanced_pub.c) and [z\_advanced\_sub.c](https://github.com/eclipse-zenoh/zenoh-c/blob/main/examples/z_advanced_sub.c).

**ze\_querying\_subscriber** and **ze\_publication\_cache** APIs are now marked as deprecated.

### “Take from loaned” operation for callbacks

The Zenoh-C API makes a strong distinction between “moved” and “loaned” arguments of functions inspired by Rust and introduced to increase code safety. Assume that we define the structure

`z_owned_foo_t foo;`

Below are the variants of how this structure is processed depending on function parameter type:

| Function declaration | How to call | Meaning |
| --- | --- | --- |
| void new\_foo(z\_owned\_foo\_t\* foo); | new\_foo(&foo); | Construct a new “foo” object; assumes that the structure foo is undefined |
| bool read\_foo(const z\_loaned\_foo\_t\* foo); | read\_foo(z\_loan(foo)); | Reads data from “foo”, never changes it |
| void update\_foo(z\_loaned\_foo\_t\* foo); | update\_foo(z\_loan\_mut(foo)); | May modify “foo”, but guarantees that “foo” is valid after the call |
| void take\_foo(z\_moved\_foo\_t\* foo); | take\_foo(z\_move(foo)); | Takes ownership of data contained in foo. Guarantees that after calling this function the foo is left in the empty state and should not be accessed anymore (but z\_drop on it is allowed, i.e., the API is double-drop safe) |

See the Zenoh-C “Concepts” section of documentation for more detailed explanations: <https://zenoh-c.readthedocs.io/en/1.3.2/concepts.html>.

It happened that this approach doesn’t work well with parameters of callback functions. Ideally the callback functions should have accepted the `z_moved_foo_t *` type. E.g., callback receives a sample and the user is allowed to take this sample and place it to some queue for further processing.

`z_moved_foo_t *`

The problem is that `z_moved_foo_t *` type obliges function to take ownership of the parameter. But sometimes users just want to read and analyze data in place, they don’t want to care about the lifetime of the passed data.

`z_moved_foo_t *`

So, it was decided that callback functions accepts parameter of `z_loaned_foo_t *` type and in this release the new operation `z_take_from_loaned` was introduced. Here is the example of its usage:

`z_loaned_foo_t *`
`z_take_from_loaned`
`void sub_callback(z_loaned_sample_t* sample, void* arg) {
 z_owned_sample_t s;
 z_take_from_loaned(&s, sample);
 // Now we can save `s` for further processing, e.g. send it to another thread
}
...
z_owned_closure_sample_t callback;
z_closure(&callback, sub_callback, NULL, NULL);
z_owned_subscriber_t sub;
if (z_declare_subscriber(z_loan(session), &sub, z_loan(keyexpr), z_move(callback), NULL) < 0) {
 printf("Unable to declare subscriber.\n");
 exit(-1);
}`

It’s important to notice that the `z_take_from_loaned` function breaks the condition *“function, accepting z\_loaned\_foo\_t* type guarantees that “foo” is valid after the call”\* . That’s why this operation is reserved to be used only by developers and it’s strongly discouraged to use it outside of callbacks. The functions of Zenoh-C API itself never perform this operation.

`z_take_from_loaned`

### Other API improvements

We introduced the `z_bytes_get_contiguous_view` function allowing to get a view (i.e. a pointer and length) of the payload bytes, for contiguous payloads. This function will return an error if payload is not contiguous (most likely due to fragmentation if payload size is too big) - in this case to access payload data without copy one can continue to use either **z\_bytes\_reader** API or **z\_bytes\_slice\_iterator** API.

`z_bytes_get_contiguous_view`

get\_contiguous\_view.c

`z_view_slice_t view;
if (z_bytes_get_contiguous_view(z_loan(payload), &view) == Z_OK) {
 const uint8_t* ptr = z_slice_data(z_loan(view));
 size_t len = z_slice_len(z_loan(view));
 // do something with ptr and len
}`

## Zenoh-Cpp

### Advanced Pub Sub

[Advanced Pub/Sub API](https://zenoh.io/blog/2024-12-12-zenoh-firesong-1.1.0/#advanced-pubsub) introduced in Zenoh 1.1.0 is now also available in Zenoh-Cpp, but for the time being only with **Zenoh-C** backend:

z\_advanced\_pub.cpp

`auto config = Config::create_default();
config.insert_json5(Z_CONFIG_ADD_TIMESTAMP_KEY, "true");
auto session = Session::open(std::move(config));
ext::SessionExt::AdvancedPublisherOptions opts;
opts.cache.emplace().max_samples = 10;
opts.publisher_detection = true;
opts.sample_miss_detection.emplace().heartbeat =
ext::SessionExt::AdvancedPublisherOptions::SampleMissDetectionOptions::HeartbeatPeriodic{1000};
// alternatively sample miss detection can be done in response to subscriber's periodic queries
auto pub = session.ext().declare_advanced_publisher(
 "key/expression", std::move(opts));
pub.put("some_data");`

z\_advanced\_sub.cpp

`auto config = Config::create_default();
auto session = Session::open(std::move(config));
ext::SessionExt::AdvancedSubscriberOptions opts;
opts.history.emplace().detect_late_publishers = true;
opts.history->detect_late_publishers = true;
// enable recovery based on received heartbeats from ext::AdvancedPublisher
opts.recovery.emplace().last_sample_miss_detection =
ext::SessionExt::AdvancedSubscriberOptions::RecoveryOptions::Heartbeat{};
// alternatively recovery can be triggered based on missed sample detection via periodic queries:
// opts.recovery.emplace().last_sample_miss_detection =
// ext::SessionExt::AdvancedSubscriberOptions::RecoveryOptions::PeriodicQueriesOptions{1000};
opts.subscriber_detection = true;
auto data_handler = [](const Sample &sample) {
 std::cout << ">> [Subscriber] Received ('"
 << sample.get_keyexpr().as_string_view() << "' : '"
 << sample.get_payload().as_string() << "')"
 << std::endl;
};
auto missed_sample_handler = [](const ext::Miss &miss) {
 std::cout << ">> [Subscriber] Missed " << miss.nb
 << " samples from '" << miss.source.id() << "' !!!"
 << std::endl;
};
auto advanced_subscriber =
session.ext().declare_advanced_subscriber(
 "key/expression", data_handler, closures::none, std::move(opts));
advanced_subscriber.declare_background_sample_miss_listener(
 missed_sample_handler, closures::none);`

Complete examples can be found at [z\_advanced\_pub.cpp](https://github.com/eclipse-zenoh/zenoh-cpp/blob/main/examples/zenohc/z_advanced_pub.cxx) and [z\_advanced\_sub.cpp](https://github.com/eclipse-zenoh/zenoh-cpp/blob/main/examples/zenohc/z_advanced_sub.cxx).

**ext::QueryingSubscriber** and **ext::PublicationCache** APIs are now marked as deprecated.

### Custom deleter for external buffer

Sometimes it’s necessary to send a large amount of data, which can be inefficient to copy. However, the exact moment when Zenoh deletes the `Buffer` object is unknown: after being sent, the buffer is queued and only deleted once it has actually been transmitted.

`Buffer`

It is possible to create a `Bytes` object by moving a `std::vector` into it, thereby avoiding a copy of the vector. However, this approach does not cover all use cases.

`Bytes`
`std::vector`

Now, it is possible to create a `Buffer` object that points to external data and uses a custom deleter for that data. When Zenoh finishes sending the buffer, it destroys the `Buffer` object, and its destructor invokes the custom deleter. See the example below:

`Buffer`
`Buffer`
`uint8_t* ptr = new uint8_t[10];
auto deleter = [&deleted](uint8_t* data) {
 delete[] data;
};
Bytes bytes(ptr, 10, deleter);
session.put("foo/bar", std::move(bytes));`

### Other API improvements

We introduced `Bytes::get_contiguous_view()` method allowing to get a view (i.e. a pointer and length) of the payload bytes, for contiguous payloads. This function will return an empty `std::optional` if payload is not contiguous (most likely due to fragmentation, if payload size is too big) - in this case to access payload data without copy one can continue to use either **Bytes::Reader** or **Bytes::SliceIterator**.

`Bytes::get_contiguous_view()`
`std::optional`

get\_contiguous\_view.cpp

`auto view = payload.get_contiguous_view();
if (view.has_value()) {
 const uint8_t* ptr = view.data;
 size_t len = view.len;
 // do something with ptr and len
}`

## Zenoh-Python

### Query context manager

When using queryable with a channel handler, query objects need to be finalized in order to acknowledge the query response on the querier side. The proper way to do this in Python is by using a context manager, that’s why Query objects can now be used as context managers.

`with zenoh.open(conf) as session:
 print(f"Declaring Queryable on '{key}'...")
 queryable = session.declare_queryable(key, complete=complete)

 print("Press CTRL-C to quit...")
 while True:
 with queryable.recv() as query: # use the context manager here
 # do something with query`

## Zenoh-TS

### API Polish and alignments

In version 1.3.3 we have made some upgrades to the inner workings of the Typescript API, specifically we have added a **KeyExpr** API based on the Rust Zenoh-KeyExpr library, compiling a subset of the KeyExpr library to WASM. This is a first step on the path of integration and code reuse between main Zenoh and Zenoh typescript binding.

We have also exposed the ability to get session info in a poll-based fashion.
Note that due to the TS implementation being based on a remote API, every time a user requires the most up to date version of the session info, a new call to session info will have to be made, producing a new `SessionInfo` class instance.

`SessionInfo`
`console.log!("Opening session...");
const session = await Session.open(new Config("ws/127.0.0.1:10000"));
console.log!("Get Info...");
const info: SessionInfo = await session.info();
console.log!("zid: {}", info.zid());
console.log!("routers zid: {:?}",info.routers_zid() );
console.log!("peers zid: {:?}",info.peers_zid() );
// New SessionInfo object will need to be created here for updated state`

Multiple minor changes in the Typescript API have been made in order to cover main Zenoh functionality and to make Typescript API better matching with other language bindings as well as to make it internally consistent:

The `callback` field was renamed to `handler` as it was supposed to contain a callback function or channel. This field now is always passed in corresponding “options” structure for API uniformity

`callback`
`handler`

`options` structures with additional parameters like `encoding`, `attachment`, `priority`, etc were added to `reply()`, `reply_err()` and `reply_del()` operations of `Query`

`options`
`encoding`
`attachment`
`priority`
`reply()`
`reply_err()`
`reply_del()`
`Query`

Channels’ fields `size` were renamed to `capacity`

`size`
`capacity`

Encoding’s `from_str` renamed to `from_string`,

`from_str`
`from_string`

`with_schema()` method added to Encoding

`with_schema()`

Binary data serialization compatible with the zenoh-ext library was implemented. Now it’s possible to exchange data between Zenoh applications on typescript and other languages. The example of using serialization/deserialization API:

`let input = new Map<bigint, string>()
input.set(0n, "abc")
input.set(1n, "def")
let payload = zserialize(input, ZS.map(ZS.bigint(BigIntFormat.Uint64), ZS.string()))
let output = zdeserialize(ZD.map(ZD.bigint(BigIntFormat.Uint64), ZD.string()), payload)`

### Example chat application

An example browser application demonstrating the key parts of Zenoh Typescript API functionality was added. This is a multiuser chat application which sends/receives chat messages using **pub/sub** API, allows to restore chat history for new connected users using **queryable/get** API and shows list of online users using **liveliness** API.

See [“Build and run examples”](https://github.com/eclipse-zenoh/zenoh-ts?tab=readme-ov-file#build-and-run-examples) section in the github readme for instructions how to run this example

## Zenoh-Java / Zenoh-Kotlin

### API Polish and alignments

For this release we have mostly worked on Zenoh-Java on aligning the API whose migration guide is now available on <https://zenoh.io/docs/migration_1.0/java/>. We now provide the same features as on the other bindings.

Besides that, some changes on both projects include:

Providing string overloads to functions requiring ZBytes instances, reducing the verbosity of the code when working with string messages.

Implementing the Querier feature

Fix missing QoS (quality of service) configuration options on session get operations.

Regarding architectures, we’ve now added support for the aarch64 architecture on Windows.

On both Zenoh-Kotlin and Zenoh-Java we have provided a further utility to run the examples, by allowing users to now build them as executable fat JARs.

### Maven Publications

A big improvement was achieved with regards to the packages publication of these libraries which is that we are now publishing to Maven Central! Checkout

<https://central.sonatype.com/artifact/org.eclipse.zenoh/zenoh-kotlin/overview>

<https://central.sonatype.com/artifact/org.eclipse.zenoh/zenoh-kotlin-android/overview>

<https://central.sonatype.com/artifact/org.eclipse.zenoh/zenoh-java/overview>

<https://central.sonatype.com/artifact/org.eclipse.zenoh/zenoh-java-android/overview>

Now it’s simpler to import the projects into your own projects by adding the MavenCentral repository and importing the appropriate library.

That’s a wrap for Zenoh 1.3.3 — **Gozuryū**! This release brings significant improvements in performance, flexibility, and feature completeness across the stack. Whether you’re building on constrained devices, working in highly dynamic environments, or scaling across complex networks, Zenoh now gives you more tools to do it right and while having fun ;-).

As always, we’d love to hear your feedback, ideas, and contributions. Check out the [Zenoh repository](https://github.com/eclipse-zenoh/zenoh), join the conversation on [Zenoh’s Discord](https://discord.com/invite/vSDSpqnbkm), and let us know what you’re building!

Until next time — stay fast, stay flexible, and keep streaming.

**– The Zenoh Team**

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2025-07-11-zenoh-pico-peer-to-peer-unicast/

Source: https://zenoh.io/blog/2025-07-11-zenoh-pico-peer-to-peer-unicast/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh-Pico Peer to Peer Improvements

Blog Posts

# Zenoh-Pico Peer to Peer Improvements

July 9th, 2025 -- Paris.

As hinted at in our [previous blog](http://localhost:1313/blog/2025-04-09-zenoh-pico-performance/) post on Zenoh-Pico performance improvements, we’ve now introduced a long-requested peer-to-peer unicast mode for Zenoh-Pico! Let’s dive into how it works.

## What is Zenoh-Pico?

Zenoh-Pico is the lightweight, native C implementation of the [Zenoh](http://github.com/eclipse-zenoh/zenoh) protocol, designed specifically for constrained devices. It provides a streamlined, low-resource API while supporting all abstractions from [Rust Zenoh](https://github.com/eclipse-zenoh/zenoh): pub, sub and query, advanced pub/sub and so on. Zenoh-Pico already supports a broad range of platforms and protocols, making it a versatile choice for embedded systems development.

## Peer-to-Peer Unicast

Until now, if you didn’t want to run a router with Zenoh-Pico nodes, you had to rely on multicast transport—an option that isn’t always feasible. Additionally, this method was limited to UDP, which lacks reliability.

Now, you can use TCP links to enable unicast peer-to-peer communication and enhance reliability in scenarios without a router. This advancement also improves throughput and latency, which we’ll discuss below.

This feature is supported and has been tested on all platforms, including FreeRTOS, ESP-IDF, Raspberry Pi Pico, Zephyr, Linux, and Windows. It is currently limited to TCP links, but may be extended to include UDP or Serial if there’s demand.

Architecture-wise, we use non-blocking sockets and I/O multiplexing to handle all connections on a single RX thread, plus an additional thread that listens on a socket and accepts incoming connections. For resource-efficiency reasons, peer-unicast nodes do not route traffic: every message received from a connected peer triggers our API, and every message created via our API is sent to all connected peers. This design allows for a single TX and a single RX buffer.

### Examples:

Here is an example showing how to implement a 1:N (or N:1) communication graph:

![1:N diagram](../../img/20250711-Zenoh-Pico-peer-to-peer-unicast/1-n.png)

If we assume a single publisher connected to 3 subscribers, here’s how we could configure it:

`./build/example/z_pub -l tcp/127.0.0.1:7447
./build/example/z_sub -e tcp/127.0.0.1:7447
./build/example/z_sub -e tcp/127.0.0.1:7447
./build/example/z_sub -e tcp/127.0.0.1:7447`

To implement an N:N graph:

![N:N diagram](../../img/20250711-Zenoh-Pico-peer-to-peer-unicast/n-n.png)
`./build/example/z_pub -l tcp/127.0.0.1:7447
./build/example/z_sub -l tcp/127.0.0.1:7448 -e tcp/127.0.0.1:7447
./build/example/z_sub -l tcp/127.0.0.1:7449 -e tcp/127.0.0.1:7447 -e tcp/127.0.0.1:7448
./build/example/z_sub -e tcp/127.0.0.1:7447 -e tcp/127.0.0.1:7448 -e tcp/127.0.0.1:7449`

## Performances

### Test Details

In addition to enabling peer-to-peer unicast, we improved general library CPU utilization, further boosting throughput and latency by approximately 10%. The tests were run on an Ubuntu 22.04 laptop equipped with an AMD Ryzen 7735U and 32 GB of RAM.

### Configuration

Note that the Zenoh-Pico configuration used for testing deviates from the default. Here are the changes:

`Z_FEATURE_SESSION_CHECK`
`Z_FEATURE_BATCH_TX_MUTEX`
`Z_FEATURE_RX_CACHE`

### Results

![P2p latency](../../img/20250711-Zenoh-Pico-peer-to-peer-unicast/perf_lat.png)

The round-trip time for packets below 16 KiB is under 20 µs—meaning a one-way latency of under 10 µs. Peer-to-peer unicast delivers up to **70% lower latency** compared to client mode.

![P2p throughput](../../img/20250711-Zenoh-Pico-peer-to-peer-unicast/perf_thr.png)

With up to 20 million messages per second for 8-byte messages, peer-to-peer unicast achieves over **4x the throughput** of client mode for small payloads, and still improves performance by **30% for larger payloads**.

## Multicast Declarations

Alongside peer-to-peer unicast, we’ve implemented a multicast declaration feature. This allows multicast transport to:

This feature is disabled by default and can be enabled by setting `Z_FEATURE_MULTICAST_DECLARATIONS`to 1. It’s off by default because, for it to work correctly, all existing nodes must redeclare all key expressions and subscriptions whenever a new node joins the network—which can lead to congestion.

`Z_FEATURE_MULTICAST_DECLARATIONS`

## Memory Allocation Improvements

Previously, we discussed reducing dynamic memory allocations without providing measurements. We’ve measured allocations using [heaptrack](https://github.com/KDE/heaptrack), and below you can see the results for the latest version:

![current heaptrack](../../img/20250711-Zenoh-Pico-peer-to-peer-unicast/malloc_current.png)

### Memory Breakdown:

The latest version of Zenoh-Pico includes some major performance and memory utilisation improvements, here are the latest numbers:

Since this test involved a single subscriber, no message copies were needed. With multiple subscribers, data copies would be required—but only for auxiliary data (like key expressions), as payloads are reference-counted.

## Final Thoughts

This release brings substantial improvements to Zenoh-Pico’s flexibility and performance. Peer-to-peer unicast opens the door to more robust, scalable topologies without requiring a central router. And the combined enhancements in memory use, throughput, and latency make it a strong choice for high-performance embedded applications.

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2025-07-28-zenoh-hong/

Source: https://zenoh.io/blog/2025-07-28-zenoh-hong/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh 1.5.0: Hong, the Red Dragon's Power

Blog Posts

# Zenoh 1.5.0: Hong, the Red Dragon's Power

28th July, 2025 -- Paris.

Named after the Red Dragon, a symbol of power, protection, and passion, this release delivers significant improvements across the entire Zenoh ecosystem. Hong brings substantial performance enhancements—we’ve broken the 10M msg/sec barrier—and our shared memory implementation has 25% performance throughput gains along with a simplified API and improved safety mechanisms. Configuration management has been streamlined with better validation and the ability to provide full configurations via command line. The installation process has been modernized with signed Debian repositories for enhanced security.

This release also includes major updates to language bindings: Zenoh-TS now features binary serialization for improved performance and a camelCase API, Zenoh-Pico adds STM32 ThreadX support and peer-to-peer multicast improvements, and Advanced Pub/Sub functionality has been expanded across multiple bindings.

Let’s dive into the highlights of this release.

## Zenoh

### Throughput

This release of Zenoh has further improved its performance by breaking the 10M msg/sec barrier, as measured on our MacBook laptops. We have almost doubled the throughput for small messages (8 bytes) since the release of 1.0.0.

If you want to check out the performance on your hardware, just do:

`$ cargo run --release --example z_sub_thr -- --no-multicast-scouting -l tcp/127.0.0.1:7447 -s 30
$ cargo run --release --example z_pub_thr -- --no-multicast-scouting -e tcp/127.0.0.1:7447 8
10648918.469217971 msg/s
10751147.174281364 msg/s
10658802.460094243 msg/s
10605109.520556785 msg/s
10769720.542983461 msg/s
10690899.371909663 msg/s
10758472.296933835 msg/s`

### SHM: Performance, Safety and Simplicity

In this release, Zenoh’s shared memory has become more performant, safer, and easier to use—both for newcomers and power users alike. Here are the important changes:

**SHM API Simplification & Examples**

**Hidden ProtocolID**: The low-level `ProtocolID` is now internal to the SHM API, slimming down public types and reducing noise for most users.

`ProtocolID`

**Streamlined Builders**: `ShmProviderBuilder` APIs have been overhauled for consistency and ease of use—defaults are smarter and method chains are shorter.

`ShmProviderBuilder`

**Improved Examples**: A brand-new minimal SHM example has been added, and existing examples have been refactored to use the simplified API patterns.

More details can be found in this [PR](https://github.com/eclipse-zenoh/zenoh/pull/1975).

**Watchdog Storage & Performance Tuning**

**≈25% Throughput Gain**: Internal SHM watchdog confirmator storage was re-architected—metadata cells now grow on demand and Arc-based ownership was tightened—yielding an extra ~600 K msgs/sec (from 2.4 M to ~3 M msgs/sec).

**Arena Utilization Fix**: The metadata segment now properly expands when cell exhaustion occurs, preventing stalls when the arena still has free memory but no metadata slots.

**Lifetime Safety**: Shared memory buffers now own their underlying segment handle to guarantee correct cleanup.

More details can be found in this [PR](https://github.com/eclipse-zenoh/zenoh/pull/1869).

**SHM Buffer Layout & Alignment**

**Relayout & Resize Operations**: Buffers can now be resized in place, improving flexibility for dynamic data workloads.

**Owned vs. Borrowed Buffers**: The relationship between owned and borrowed SHM buffers was clarified, fixing several edge-case bugs in buffer/session tests.

**Alignment Constants**: Alignment parameters are exposed via new constants (default = 1)

More details can be found in this [PR](https://github.com/eclipse-zenoh/zenoh/pull/1950).

**Consistent Re-exports & API Sync**

**Pruned Client Storage**: ProtocolID usage has been fully removed from the Rust client-storage module to match the new hidden-ID approach.

**Docs & Safety Notes**: The safety-critical portions of the SHM API documentation have been reformatted for clarity.

More details can be found in this [PR](https://github.com/eclipse-zenoh/zenoh/pull/2003).

**SHM Polish & Ergonomic Tweaks**

**Infallible POSIX Builder**: `with_size()` on the POSIX `ShmProviderBuilder` is now guaranteed to succeed, removing the need for error handling in most cases.

`with_size()`
`ShmProviderBuilder`

**Unchecked Mutability Helpers**: New `as_mut_unchecked()` methods across all SHM buffer types simplify scenarios where unchecked raw access is safe. Please check the [ZSHM](https://github.com/kydos/zshm/tree/shm_typed_api) repo to see the examples of unchecked mutability power usage.

`as_mut_unchecked()`

**Alignment Builders**: Added `for_type()` and `for_val()` constructors for alignment helpers, plus a new default alignment setter on the SHM provider builder.

`for_type()`
`for_val()`

**Cross-Platform Fixes**: Windows support has been hardened, and a round of `rustfmt`/`clippy` adjustments keep the codebase idiomatic.

`rustfmt`
`clippy`

More details can be found in this [PR](https://github.com/eclipse-zenoh/zenoh/pull/2023).

Following the Zenoh SHM API changes, full support for the API and example updates have been implemented for both Zenoh-C and Zenoh-Cpp. You can find the relevant updates in the following pull requests:

### Configuration improvements

#### Improved configuration validation

The following parts of the configuration are now properly validated at load time:

`access_control`
`downsampling`
`low_pass_filter`
`qos/network`

#### Providing a full configuration through –cfg command line argument

It is now possible to provide a full configuration through the command line with the `--cfg` argument.
Example:

`--cfg`
`zenohd --cfg=':{id:"aa",listen:{timeout_ms:10}}'`

#### Optional ID in the configuration

The `id` field of the configuration was a non-optional field that was automatically set up at configuration creation or at configuration load if not explicitly provided. Because of this, it was impossible to clone and reuse a configuration as-is because this would result in two configurations with the same `id`.
This field has been made optional and the `id` is automatically generated at configuration application (not at configuration creation/load) if not explicitly provided.

`id`
`id`
`id`

For example, the following code now works properly:

`import time
import zenoh
conf = zenoh.Config()
session1 = zenoh.open(conf)
session1.declare_subscriber("key/expression", lambda sample:
 print(f"Received {sample.payload.to_string()}"))
session2 = zenoh.open(conf)
session2.put("key/expression", "value")`

#### DSCP link configuration support

Endpoints now support DSCP configuration, which can be specified in the endpoint string as follows: `"tcp/192.168.0.1:7447#dscp=0x08"`

`"tcp/192.168.0.1:7447#dscp=0x08"`

This means you can now control the type of service that your routers and switches will apply to Zenoh traffic, making it possible for them to differentiate real-time traffic.

#### Link weight support

We have added support for weighted routing graphs. In other words, you can now assign weights to any of the links in the communication graph to express routing cost. At any given point in time, the routing algorithm will choose the path with minimal cost to route data from A to B.

Example:

`zenohd --cfg='routing:router:linkstate:transport_weights:[{"dst_zid": "zid1", "weight": 10}, {"dst_zid": "zid2", "weight": 42}]'`

### Breaking change: Reply::replier\_id

The unstable `replier_id` API, which used to return a `ZenohId`, is now aligned with other `SourceInfo` implementations, returning an `EntityGlobalId` which allows it to globally identify the queryable that generated the reply in question. This is a breaking change that has been propagated to all affected APIs: Rust, C, C++, Python, Kotlin, and Java. The `replier_id` API remains marked as unstable for now.

`replier_id`
`ZenohId`
`SourceInfo`
`EntityGlobalId`
`replier_id`

Example in Rust:

`if let Some(replier_id) = reply.replier_id() {
 let replier_zid: ZenohId = replier_id.zid();
 let replier_eid: u32 = replier_id.eid();
}`

### QUIC Datagram support

As of Zenoh 1.5.0, it is now possible to use unreliable datagrams in QUIC by setting `rel=0` in QUIC endpoints/locators. Both the initial MTU value and the MTU discovery interval are configurable via endpoint configuration:

`rel=0`

`quic/127.0.0.1:9000?rel=0#initial_mtu=2000;mtu_discovery_interval_secs=300`

`quic/127.0.0.1:9000?rel=0#initial_mtu=2000;mtu_discovery_interval_secs=300`

By default, the initial MTU value is 1200 bytes with an MTU discovery interval of 600 seconds (note that MTU discovery is a binary search algorithm). Therefore, if network conditions allow for higher MTUs, manual configuration of `initial_mtu` is desirable.

`initial_mtu`

Note that QUIC streamed and datagram modes are not currently compatible in Zenoh: both the listener and connect endpoints need to use the same mode.

See [RFC 9221](https://datatracker.ietf.org/doc/rfc9221/) for more information on the QUIC protocol.

## Advanced Pub/Sub

You’ve been asking for it and we did it 🙂 The Advanced Pub/Sub API is now available in both Python and Kotlin! You can check out the implementations and examples at the following links:

## Zenoh-TS

The Zenoh TypeScript API has witnessed several major improvements:

**Data Exchange Protocol**: Binary serialization is now used between the TypeScript library and remote-API plugin. This update has significantly reduced bandwidth and improved performance.
Given highly optimized JSON serialization in JavaScript, the throughput improvement might be negligible for smaller payloads (around 10% more compared to the older version for 8-byte messages), but becomes significant as message size increases (almost doubled for >1KB payload).

**From snake\_case to camelCase**: This is a breaking change, but it was necessary to make the library conform to commonly accepted style and to avoid confusion between, for example, “toString” and “to\_string”.

**Async**: API functions relying on WebSocket usage have migrated to async.

In this release, we introduce the [“bridge”](https://github.com/eclipse-zenoh/zenoh-ts/tree/main/zenoh-bridge-remote-api) variant of the remote-API plugin (the plugin to which the zenoh-ts library connects through WebSocket). The bridge is a standalone application with a statically linked plugin and command-line options specific to the plugin. This makes configuration easier, allowing users to simply run the application instead of error-prone dynamic plugin loading.

A [Nuxt](https://nuxt.com/) [example application](https://github.com/eclipse-zenoh/zenoh-ts/tree/main/zenoh-ts/examples/browser/nuxt) was added to demonstrate how to use Zenoh in this popular framework. This example demonstrates how to work around some of the issues caused by Server-Side Rendering (SSR).

Feel free to use this example to interactively explore basic Zenoh functionality and API!

![Nuxt example](../../img/20250414-zenoh-gozuryu/zenoh_ts_nuxt.png)

![Nuxt example](../../img/20250414-zenoh-gozuryu/zenoh_ts_nuxt.png)

## Zenoh-Pico

### STM32 ThreadX Support

Thanks to g4sp3r from Ubiquity Robotics, we have added support for ThreadX on STM32 with serial transport, providing more options for real-time operating system integration.

### Peer-to-Peer Multicast Improvements

We have added the new `Z_FEATURE_MULTICAST_DECLARATIONS` compile-time option with the following features:

`Z_FEATURE_MULTICAST_DECLARATIONS`

This option comes with a cost: every joining node will trigger the previous nodes to push all their declarations at once. As such, the option is disabled by default. Be sure to activate it if you think the benefits outweigh the drawbacks.

### Performance Optimization

Various performance optimizations were implemented in this release, resulting in lower latency overall and increased small packet throughput. We also reduced the number of memory allocations required for standard operations. If you want to delve deeper into these changes, you can read our corresponding blog post: [Zenoh Blog](https://zenoh.io/blog/2025-07-11-zenoh-pico-peer-to-peer-unicast/).

### New Logging System

With this release, we changed how logging is handled at compile time. The previous `ZENOH_DEBUG=<value>` system still works, but now if you want to set the log level, you can use `ZENOH_LOG=debug`.

`ZENOH_DEBUG=<value>`
`ZENOH_LOG=debug`

More details can be found [here](https://github.com/eclipse-zenoh/zenoh-pico/pull/934).

## Installation Process Changes

The Debian repository is now [signed](https://github.com/eclipse-zenoh/ci/issues/316), which requires changes to the sources.list of already installed systems and downloading the public key. The [instructions](https://zenoh.io/docs/getting-started/installation/#ubuntu-or-any-debian) to install on a new system are now:

Add Eclipse Zenoh public key to apt keyring:

`$ curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg`

Add Eclipse Zenoh private repository to the sources list:

`$ echo "deb [signed-by=/etc/apt/keyrings/zenoh-public-key.gpg] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list > /dev/null
$ sudo apt update`

For existing systems, replace `[trusted=yes]` with `[signed-by=/etc/apt/keyrings/zenoh-public-key.gpg]`.

`[trusted=yes]`
`[signed-by=/etc/apt/keyrings/zenoh-public-key.gpg]`

## Changelogs

The effort behind Zenoh 1.5.0 has resulted in a large number of bug fixes and improvements. The full changelog for every Zenoh repository is available at the following links: [Rust](https://github.com/eclipse-zenoh/zenoh/releases) | [C](https://github.com/eclipse-zenoh/zenoh-c/releases) | [C++](https://github.com/eclipse-zenoh/zenoh-cpp/releases) | [Python](https://github.com/eclipse-zenoh/zenoh-python/releases) | [Java](https://github.com/eclipse-zenoh/zenoh-java/releases) | [Kotlin](https://github.com/eclipse-zenoh/zenoh-kotlin/releases) | [TypeScript](https://github.com/eclipse-zenoh/zenoh-ts/releases) | [Pico](https://github.com/eclipse-zenoh/zenoh-pico/releases) | [DDS plugin](https://github.com/eclipse-zenoh/zenoh-plugin-dds/releases) | [ROS2 plugin](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds/releases) | [MQTT plugin](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt/releases) | [WebServer plugin](https://github.com/eclipse-zenoh/zenoh-plugin-webserver/releases/tag/1.0.4) | [Filesystem backend](https://github.com/eclipse-zenoh/zenoh-backend-filesystem/releases) | [RocksDB backend](https://github.com/eclipse-zenoh/zenoh-backend-rocksdb/releases) | [S3 backend](https://github.com/eclipse-zenoh/zenoh-backend-s3/releases) | [InfluxDB backend](https://github.com/eclipse-zenoh/zenoh-backend-influxdb/releases)

That’s a wrap for Zenoh 1.5.0 — **Hong**! This release demonstrates our continued commitment to performance, safety, and developer experience across the entire Zenoh ecosystem. Whether you’re building cloud-to-microcontroller systems, high-performance shared memory applications, deploying on constrained devices, or developing modern web applications, Hong provides the tools and improvements to power your next-generation data-centric systems.

We are eager to hear what you’ll build with these new capabilities. As always, we welcome your feedback and contributions to help shape the future of Zenoh.
You can reach us on [Zenoh’s Discord server](https://discord.com/invite/vSDSpqnbkm)!

May the power of the Red Dragon fuel your innovations,

**– The Zenoh Team**

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2025-10-20-zenoh-imoogi/

Source: https://zenoh.io/blog/2025-10-20-zenoh-imoogi/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh 1.6.x: Imoogi

Blog Posts

# Zenoh 1.6.x: Imoogi

20th October, 2025 -- Paris.

We are thrilled to announce the release of Zenoh 1.6.x – **Imoogi**!

Named after the Korean dragon that ascends to greatness, this release elevates the Zenoh ecosystem with powerful refinements and critical improvements. Imoogi focuses on stabilizing and extending the groundbreaking features introduced in version 1.5.0, bringing enhanced shared memory capabilities, improved configuration management, better scalability, and expanded language binding support.

Key highlights of this release include:

`congestion_control`

Let’s explore what Imoogi brings to the Zenoh ecosystem!

## Zenoh

### SHM Improvements

#### Typed SHM Buffers

Zenoh 1.5 introduced a fully **generic, typed** shared-memory API. All SHM buffer traits are now generic over the data type, and a new `Typed<T, …>` wrapper provides a high-level, type-safe view over the raw SHM buffer [(PR)](https://github.com/eclipse-zenoh/zenoh/pull/2034). In other words, you can treat a shared buffer almost like a Rust struct. For example, if you have a C-compatible struct:

`Typed<T, …>`
`#[repr(C)]
struct MyData { x: u32, y: u16 }`

you can build a layout and allocate a buffer for it, then wrap it in `Typed<MyData, …>` to access fields safely:

`Typed<MyData, …>`
`let layout = TypedLayout::<MyData>::new();
let mut typed_buf: Typed<MyData, ZShmMut> = provider
 .alloc(layout)
 .wait()
 .unwrap()
 .assume_init();
typed_buf.as_mut().x = 42; // safe, typed access`

Under the hood, this enforces the correct alignment and size for `MyData`, avoiding manual casting.

`MyData`

#### Improved Allocator

The SHM allocator is now based on the [talc](https://crates.io/crates/talc) allocator and performs much more efficiently in real-world workload scenarios, addressing performance and fragmentation issues.

#### Improved Allocation Builder Ergonomics

Allocation builders are now much simpler and more robust. The provider’s `alloc` method is generic and accepts different layout descriptions such as `usize`, `(usize, AllocAlignment)`, and `MemoryLayout`.

`alloc`
`usize`
`(usize, AllocAlignment)`
`MemoryLayout`
`// Option 1: Simple allocation
let _shm_buf = provider.alloc(512).wait()?;
// Option 2: Allocation with custom alignment
let _shm_buf = provider
 .alloc((512, AllocAlignment::ALIGN_2_BYTES))
 .wait()?;
/// Layout allocation:
let layout = provider.alloc_layout(512)?;
let _shm_buf = layout.alloc().wait()?;`

#### Buffer Layout, Resize and Safety

The SHM API rework also clarified *owned vs. borrowed* buffers and added dynamic operations. Notably, you can now **resize a shared buffer in place**, which wasn’t previously possible. For example, after allocating a buffer you can:

`shm_buf.try_resize(new_len)?;`

to grow or shrink it (within its segment’s limits).

We also expose alignment defaults and constants (`ALIGN_N_BYTE(S)`) and have tightened lifetime management: SHM buffers now own their segment handle to ensure proper cleanup. New unchecked mutability methods (`as_mut_unchecked()`) were added for cases where you *know* a mutable borrow is safe. Overall, these API changes make working with SHM buffers more predictable and idiomatic to Rust.

`ALIGN_N_BYTE(S)`
`as_mut_unchecked()`

#### Implicit SHM Optimization

Perhaps the most thrilling change is that Zenoh now **automatically uses shared memory for large data**. In practice, this means you don’t have to do anything special: if you publish a large payload, Zenoh will “implicitly pack” it into SHM and transmit just a reference locally. For example:

`let large_data = vec![0u8; 1_000_000]; // 1 MB payload
publisher.put(large_data).await.unwrap();
// Zenoh will use SHM under the hood for this large message.`

This implicit SHM transport applies in all modes (even when using a router), vastly improving throughput for local messages.

#### Precommit SHM pages

**What changed:** the SHM provider now pre-commits newly-created shared-memory buffers and locks their pages into physical RAM before handing them to consumers. Concretely, pages that previously could be allocated lazily (and thus incur a page fault on first touch) are committed and locked so the memory backing the SHM buffer is resident and won’t trigger major page faults later [(PR)](https://github.com/eclipse-zenoh/zenoh/pull/2175).

**Observable runtime effect:** previously a large zero-copy handoff could incur an unpredictable latency spike when the OS needed to fault in pages; after this change those first-access page fault penalties are removed (at the cost of doing the work up front). That makes SHM handoffs much more deterministic and stable for real-time/edge use cases where a router or local consumer must forward large buffers with tight latency requirements.

**Performance & resource tradeoffs:** precommitting shifts the cost from the consumer’s first access to SHM segment creation time — it takes slightly longer and the process’ resident memory increases immediately. It also prevents lazy swapping for those pages, so overall resident memory can be higher. These are intentional tradeoffs: you trade a small, predictable allocation cost and higher resident footprint for removing rare but large, unpredictable page fault latency spikes.

**Failure modes & safeguards:** the PR adds more careful logging around the SHM provider (e.g., logging errors in `LazyShmProvider`) and CI/test adjustments to cope with platform limits. Integrators should expect to see error logs if the OS refuses to lock pages and should verify system limits (e.g., `RLIMIT_MEMLOCK` on Linux).

`LazyShmProvider`
`RLIMIT_MEMLOCK`

**Actionable implications:**

#### SHM monitoring

##### TransportSession SHM indicator

A boolean field has been added to the `session` object of the AdminSpace report indicating whether SHM is enabled for the relevant TransportSession.

`session`
`[
 {
 "key": "@/aaaaaaaaaaaaaaaa/router",
 "value": {
 "sessions": [
 {
 "peer": "bbbbbbbbbbbbbbbb",
 "shm": "true",
 "whatami": "client",
 ...
 }
 ],
 ...
 },
 ...
 }
]`

##### SHM related statistics

The statistics reports have been updated to distinguish between network messages sent and received through SHM and those sent and received through the network.

In the JSON report:

`"stats": {
 "rx_n_msgs": {
 "net": 4,
 "shm": 12
 },
 "tx_n_msgs": {
 "net": 20,
 "shm": 45
 },
 ...
}`

In the OpenMetrics report:

`# HELP rx_n_msgs Counter of received network messages.
# TYPE rx_n_msgs counter
rx_n_msgs 16
rx_n_msgs{media="net"} 4
rx_n_msgs{media="shm"} 12
# HELP tx_n_msgs Counter of sent network messages.
# TYPE tx_n_msgs counter
tx_n_msgs 65
tx_n_msgs{media="net"} 20
tx_n_msgs{media="shm"} 45`

Note: to enable statistics, Zenoh has to be built with the [`stats` feature](https://docs.rs/crate/zenoh/1.6.2/features).

`stats`

### Configuration changes

In version 1.6.x, we introduced minor modifications to the Zenoh configuration to improve its overall consistency:

`congestion_control`

### Scalability improvements

In version 1.6.x, we fixed a bug that was causing an infinite loop of messages across multiple processes in a peer-to-peer topology [(PR)](https://github.com/eclipse-zenoh/zenoh/pull/214). We also applied various optimizations that reduce CPU consumption for discovery message processing [(PR)](https://github.com/eclipse-zenoh/zenoh/pull/2174).

Overall, these changes drastically reduced CPU consumption and significantly improved Zenoh scalability, especially in peer-to-peer scenarios and the rmw\_zenoh use case.

### Rust 1.75 compatibility improvement

The **zenoh** crate is declared to be compatible with Rust 1.75. This compatibility is maintained to support ROS2 Humble users on Ubuntu 22.04 LTS, which ships with Rust 1.75 as the official package version—essential for building rmw\_zenoh on that platform.

Unfortunately, the Rust version compatibility checker ignores the fact that dependent crates evolve, and a crate that worked with Rust 1.75 at one point may later fail to compile because some of its dependencies have bumped their minimum supported versions.

One possible solution would be to use pinned dependencies (e.g., `"=0.1.2"`) in zenoh itself, but this approach can cause compatibility issues.

`"=0.1.2"`

The solution is to include an additional crate, [zenoh-pinned-deps-1-75](https://crates.io/crates/zenoh-pinned-deps-1-75), which pins all failing dependencies (as of the time of release 😭) to versions compatible with Rust 1.75.

### Documentation improvements

The [Rust documentation](https://docs.rs/zenoh/latest/zenoh/) has been significantly extended. Introductory paragraphs with usage examples were added to the main page and each module. Features were documented, and functions and types were cross-linked to ensure that users would not get lost when encountering a type without knowing its purpose or how to use it.

The project’s [README](https://github.com/eclipse-zenoh/zenoh/blob/main/README.md) was also improved and systematized. Each component now has its own README, with the root README linking to all of them.

## Zenoh-Pico

### Advanced Pub/Sub

Zenoh-Pico now includes support for the Advanced Publisher and Subscriber, bringing it in line with core Zenoh, where this functionality was first introduced in version [1.1.0](https://zenoh.io/blog/2024-12-12-zenoh-firesong-1.1.0/).

These features enable reliable communication even when using best-effort links such as UDP/IP.

This version introduces:

The API is consistent with the Zenoh-C implementation first introduced in [Zenoh Gozuryū](https://zenoh.io/blog/2025-04-14-zenoh-gozuryu/). Note that in addition to starting the read and lease tasks, you must also start the periodic scheduler task when using the Advanced Publisher or Subscriber:

`z_result_t res = zp_start_periodic_scheduler_task(z_loan_mut(s), NULL);`

Complete examples can be found at [z\_advanced\_pub.c](https://github.com/eclipse-zenoh/zenoh-pico/blob/main/examples/unix/c11/z_advanced_pub.c) and [z\_advanced\_sub.c](https://github.com/eclipse-zenoh/zenoh-pico/blob/main/examples/unix/c11/z_advanced_sub.c).

### Mbed TLS Support

Secure communication is essential for IoT deployments, especially when connecting devices to cloud platforms or transmitting sensitive data. With this release, Zenoh-Pico brings enterprise-grade security to constrained devices through TLS and mutual TLS (mTLS) support via Mbed TLS.

TLS provides encryption and server authentication, ensuring that your devices communicate securely over untrusted networks. Mutual TLS goes further by requiring both client and server to authenticate each other with certificates, providing strong device identity verification—a critical requirement for production IoT deployments and cloud platforms like the Zetta Platform PaaS.

Zenoh-Pico now supports TLS via Mbed TLS in both client and peer modes. Enable it at build time with `Z_FEATURE_LINK_TLS=1` and use `tls/<host>:<port>` locators. This feature is currently available for Unix platforms.

`Z_FEATURE_LINK_TLS=1`
`tls/<host>:<port>`

#### Certificate Validation and Security

The TLS implementation includes robust security features:

`Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_KEY`
`*_BASE64_KEY`
`Z_CONFIG_TLS_VERIFY_NAME_ON_CONNECT_KEY`
`Z_CONFIG_TLS_ENABLE_MTLS_KEY=true`

#### Configuration Options

**For peer mode (listening)**:

Configure your server certificate and private key with `Z_CONFIG_TLS_LISTEN_CERTIFICATE_{KEY,BASE64_KEY}` and `Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_{KEY,BASE64_KEY}`.

`Z_CONFIG_TLS_LISTEN_CERTIFICATE_{KEY,BASE64_KEY}`
`Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_{KEY,BASE64_KEY}`

**For client mode with mTLS**:

Configure your client certificate and private key with `Z_CONFIG_TLS_CONNECT_CERTIFICATE_{KEY,BASE64_KEY}` and `Z_CONFIG_TLS_CONNECT_PRIVATE_KEY_{KEY,BASE64_KEY}`.

`Z_CONFIG_TLS_CONNECT_CERTIFICATE_{KEY,BASE64_KEY}`
`Z_CONFIG_TLS_CONNECT_PRIVATE_KEY_{KEY,BASE64_KEY}`

All configuration options are fully documented in `docs/config.rst`.

`docs/config.rst`

#### Example Configuration

Here’s a complete example showing client-side mTLS with inline base64-encoded certificates:

`z_owned_config_t cfg;
z_config_default(&cfg);
// Connect to TLS endpoint
zp_config_insert(z_loan_mut(cfg), Z_CONFIG_CONNECT_KEY, "tls/127.0.0.1:7447");
// Set CA certificate for server validation
zp_config_insert(z_loan_mut(cfg), Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_KEY, "/home/user/client/minica.pem");
// Enable mutual TLS
zp_config_insert(z_loan_mut(cfg), Z_CONFIG_TLS_ENABLE_MTLS_KEY, "true");
// Set client credentials
zp_config_insert(z_loan_mut(cfg), Z_CONFIG_TLS_CONNECT_PRIVATE_KEY_BASE64_KEY, client_key_base64);
zp_config_insert(z_loan_mut(cfg), Z_CONFIG_TLS_CONNECT_CERTIFICATE_BASE64_KEY, client_cert_base64);
// Disable hostname verification (testing only)
zp_config_insert(z_loan_mut(cfg), Z_CONFIG_TLS_VERIFY_NAME_ON_CONNECT_KEY, "false");`

Complete working examples for publishing and subscribing over TLS can be found in `examples/unix/c11/z_pub_tls.c` and `examples/unix/c11/z_sub_tls.c`.

`examples/unix/c11/z_pub_tls.c`
`examples/unix/c11/z_sub_tls.c`

### zp\_read Optimization

The `zp_read` function has undergone significant optimization in this release, addressing critical performance and reliability issues that affected applications processing high message throughput. These improvements come from two complementary enhancements that transform how Zenoh-Pico handles network data.

`zp_read`

#### Batch Processing for Improved Throughput

The original `zp_read` implementation processed only a single message per call, creating a significant performance bottleneck. Applications had to repeatedly call `zp_read` to drain the network buffer, and when messages arrived faster than they could be processed one-by-one, TCP buffers would overflow, causing data corruption.

`zp_read`
`zp_read`

The new default behavior processes all available messages in the buffer in a single `zp_read` call. This batch processing approach:

`zp_read`
`single_read = true`

**API Changes:**

`typedef struct {
 bool single_read; // Read a single packet instead of the whole buffer
} zp_read_options_t;
// Default is batch processing (single_read = false)
void zp_read_options_default(zp_read_options_t *options) {
 options->single_read = false;
}`

The implementation now efficiently processes all messages in both unicast and multicast transport modes.

More details can be found in this [PR](https://github.com/eclipse-zenoh/zenoh-pico/pull/1004).

#### No-Data Notification

After changing `zp_read` to batch processing, applications needed a way to distinguish between successful operations that processed data and calls where no data was available. Previously, both scenarios returned `Z_OK`, making it impossible to implement efficient polling strategies or detect when the network buffer was empty.

`zp_read`
`Z_OK`

A new result code `Z_NO_DATA_PROCESSED` was introduced specifically for this scenario.

`Z_NO_DATA_PROCESSED`

This enhancement enables applications to implement smarter polling strategies and optimize resource usage:

`z_result_t result = zp_read(session, NULL);
if (result == Z_NO_DATA_PROCESSED) {
 // No data available, can back off or sleep
 // Perfect for power-constrained devices
} else if (result == Z_OK) {
 // Data was processed, might want to read again immediately
} else {
 // Handle error (result < 0)
}`

**Benefits:**

More details can be found in this [PR](https://github.com/eclipse-zenoh/zenoh-pico/pull/1022).

#### Impact

Together, these optimizations provide:

These changes are particularly impactful for:

## Zenoh-Python

### Introduce SHM API

A shared memory API has been added to zenoh-python, allowing you to allocate and write to shared-memory segments before sending them through Zenoh.

`# Create a provider with 1 MB buffer
provider = zenoh.shm.ShmProvider.default_backend(1024 * 1024)
payload = b"shared memory payload"
# Allocate buffer with garbage collection policy
sbuf = provider.alloc(
 len(payload), policy=zenoh.shm.BlockOn(zenoh.shm.GarbageCollect())
)
# Write data to shared buffer
sbuf[:] = payload
# Publish - subscribers in the same host will access via shared memory
session.put(sbuf)`

## Zenoh-C

The SHM API has been updated to align with recent changes in the Rust API, specifically the renaming of `alloc_layout` to `precomputed_layout`. While the renamed items are deprecated, they remain accessible to facilitate a smoother migration process for developers.

`alloc_layout`
`precomputed_layout`

For example:

`// Old API (deprecated but still available)
z_owned_alloc_layout_t alloc_layout;
z_alloc_layout_with_alignment_new(&alloc_layout, z_loan(*provider), buf_ok_size, alignment));
// New API (recommended)
z_owned_precomputed_layout_t precomputed_layout;
z_shm_provider_alloc_layout_aligned(&precomputed_layout, z_loan(*provider), buf_ok_size, alignment));`

## Zenoh-TS

### Introduce Matching API

We added the last missing part of core Zenoh functionality - matching listener and matching status for Publisher and Querier in Zenoh-TS 1.6.x. Similarly to other languages, the new API can be used as follows:

`const publisher: Publisher = await session.declarePublisher(keyExpr);
const listenerCallback = function (status: MatchingStatus) {
 if (status.matching()) {
 console.warn("Publisher has matching subscribers.")
 } else {
 console.warn("Publisher has NO MORE matching subscribers")
 }
};
let matchingListener = await publisher.matchingListener({handler: listenerCallback });
// Now every time matching status of publisher changes (i.e. first subscriber connects, or last one disconnects) a listenerCallback will be triggered
// Alternatively it is also possible to access matching status of publisher at any moment of time using
let matchingStatus = publisher.matchingStatus().await;`

## Plugin API Update

Prior to 1.6.x, due to the absence of a stable ABI in Rust, it was necessary to ensure that plugins and zenohd were built with the same version of Rust, the same Zenoh version and features, and additionally that all common dependency crates of plugins and Zenoh (such as ***serde*** or ***tokio***) had the same version and contained exactly the same features. The last requirement was especially difficult to satisfy.

In the new version, we reworked the plugin interface, and it should no longer be necessary to satisfy the last constraint.

The requirement for the same version of Rust and the same Zenoh version and features still remains, but the diagnostics for such mismatches have also been improved.

## NuZe: Nu meets Zenoh

Nu is the powerful scripting language underlying [Nushell](https://www.nushell.sh/). In Nu, everything is *structured* data in the form of [tables](https://www.nushell.sh/lang-guide/chapters/types/basic_types/table.html). This allows commands to pipeline in a natural, robust, and consistent way. Tables are a particularly great fit for Zenoh data: sample streams are tables where each column represents a sample property (e.g., key-expression, timestamp, encoding, etc.).

NuZe (/nuz/) embeds the upstream Nu engine and extends it with Zenoh commands through the Rust bindings. The result is a single standalone executable that combines Nushell functionality with an extensive collection of custom Zenoh commands. The Asciinema recording below illustrates the use of NuZe to declare a queryable and send a query to it:

[![asciicast](https://asciinema.org/a/Uy6yvpT86vWzYW5DmWBfLcc8V.svg)](https://asciinema.org/a/Uy6yvpT86vWzYW5DmWBfLcc8V)

![asciicast](https://asciinema.org/a/Uy6yvpT86vWzYW5DmWBfLcc8V.svg)

NuZe was conceived to facilitate testing and debugging of Zenoh applications: it is a convenient tool to write end-to-end tests and quickly poke into a Zenoh network. It also (unsurprisingly) serves as a powerful building block for interactive Zenoh applications in a given domain.

NuZe currently lives in <https://github.com/ZettaScaleLabs/nu-zenoh> and is based on [Nushell 0.106.1](https://www.nushell.sh/blog/2025-07-30-nushell_0_106_1.html) as of commit `578316b`; see the repository [README](https://github.com/ZettaScaleLabs/nu-zenoh?tab=readme-ov-file#nuze-zenoh-nu-shell) for installation and usage instructions.

`578316b`

## Changelogs

The effort behind Zenoh 1.6.x **Imoogi** has resulted in numerous bug fixes and improvements across the ecosystem. The full changelog for every Zenoh repository is available at the following links:

[Rust](https://github.com/eclipse-zenoh/zenoh/releases) | [C](https://github.com/eclipse-zenoh/zenoh-c/releases) | [C++](https://github.com/eclipse-zenoh/zenoh-cpp/releases) | [Python](https://github.com/eclipse-zenoh/zenoh-python/releases) | [Java](https://github.com/eclipse-zenoh/zenoh-java/releases) | [Kotlin](https://github.com/eclipse-zenoh/zenoh-kotlin/releases) | [TypeScript](https://github.com/eclipse-zenoh/zenoh-ts/releases) | [Pico](https://github.com/eclipse-zenoh/zenoh-pico/releases) | [DDS plugin](https://github.com/eclipse-zenoh/zenoh-plugin-dds/releases) | [ROS2 plugin](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds/releases) | [MQTT plugin](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt/releases) | [WebServer plugin](https://github.com/eclipse-zenoh/zenoh-plugin-webserver/releases) | [Filesystem backend](https://github.com/eclipse-zenoh/zenoh-backend-filesystem/releases) | [RocksDB backend](https://github.com/eclipse-zenoh/zenoh-backend-rocksdb/releases) | [S3 backend](https://github.com/eclipse-zenoh/zenoh-backend-s3/releases) | [InfluxDB backend](https://github.com/eclipse-zenoh/zenoh-backend-influxdb/releases)

We’re thrilled to see what you’ll build with these enhancements. As always, your feedback, contributions, and success stories help shape the future of Zenoh. Join the conversation, share your experiences, and help us continue making Zenoh better for everyone.

You can reach us on [Zenoh’s Discord server](https://discord.com/invite/vSDSpqnbkm)!

Like the Imoogi ascending to become a true dragon, may your systems rise to new heights,

**– The Zenoh Team**

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

# https://zenoh.io/blog/2025-12-11-zenoh-jiaolong/

Source: https://zenoh.io/blog/2025-12-11-zenoh-jiaolong/

![](../../img/zenoh-dragon-bg-150x163.png)

# Zenoh 1.7.x: Jiāolóng

Blog Posts

# Zenoh 1.7.x: Jiāolóng

11th December, 2025 -- Paris.

We are happy to announce the release of Zenoh 1.7.x **Jiāolóng**

Named after the Chinese flood dragon, Jiāolóng represents transformation and the mastery of powerful forces. Like its namesake navigating between realms, this release bridges the gap between simplicity and power, bringing sophisticated capabilities within easy reach of developers across all platforms.

This release focuses on developer productivity and system reliability with powerful new APIs and optimizations across the Zenoh ecosystem. Query cancellation arrives across all language bindings, giving developers fine-grained control over long-running operations. Zenoh-Pico introduces zero-copy co-localization optimization and automatic task management, making embedded development simpler and more efficient. The shared memory subsystem becomes even more accessible with the transport SHM provider now available through public APIs in Rust, C, and C++.

On the plugin front, the DDS bridge adds DDS-Security support for authenticated and encrypted communication, while the Wireshark dissector has been updated for Wireshark 4.6 compatibility. API refinements across the board — including the improved SourceInfo API and locality configuration — make Zenoh 1.7.x more consistent and easier to use.

Key highlights of this release include:

`z_open()`

Let’s break down the enhancements in Jiāolóng!

## Query cancellation

We introduced cancellation tokens that allow interrupting ongoing queries – get operations.

Cancelling a token unregisters the associated query callback. If the callback is currently being executed, the cancel operation will blocks until execution terminates. Thus, after cancel returns, it is guaranteed that the callback will no longer be called.

Here’s a simple example that cancels a query after a 5-second delay:

`let ct = zenoh::cancellation::CancellationToken::default();
let query = session
 .get(key_expression)
 .callback(|reply| {println!("Received {:?}", reply.result());})
 .cancellation_token(ct.clone())
 .await
 .unwrap();
tokio::task::spawn(async move {
 tokio::time::sleep(std::time::Duration::from_secs(5)).await;
 ct.cancel().await.unwrap();
});
let reply = query.recv();`

This functionality is also available in Zenoh-C and Zenoh-Pico:

`z_owned_closure_reply_t reply_callback;
z_owned_fifo_handler_reply_t reply_handler;
z_fifo_channel_reply_new(&reply_callback, &reply_handler, 16);
z_get_options_t opts;
z_get_options_default(&opts);
z_owned_cancellation_token_t ct, ct_clone;
z_cancellation_token_new(&ct);
z_cancellation_token_clone(&ct_clone, z_loan(ct));
opts.cancellation_token = z_move(ct_clone);
z_get(z_session_loan(&session), z_loan(&key_expression), "", z_closure_reply_move(&reply_callback), &opts);
z_owned_reply_t reply;
z_result_t res = z_recv(z_loan(&reply_handler), &reply);
// in another thread ...
z_sleep_s(5);
z_cancellation_token_cancel(z_loan_mut(ct));`

Zenoh-CPP

`CancellationToken ct;
Session::GetOptions opt;
opt.cancellation_token = ct;
auto replies = session.get(key_expression, "", channels::FifoChannel(16), std::move(opt));
std::thread t([ct]() {
 std::this_thread::sleep_for(5s);
 ct.cancel();
});
auto reply = replies.recv();`

Zenoh-Python

`cancellation_token = CancellationToken()
replies = session.get(key_expression, cancellation_token=cancellation_token)
def cancel_after_5s(ct: CancellationToken):
 time.sleep(5)
 ct.cancel()
threading.Thread(target=cancel_after_5s, args=(cancellation_token,)).start()
try:
 reply = replies.recv()
except:
 reply = None`

Zenoh-TS

`let ct = new CancellationToken();
let replies = await session.get(key_expression, { cancellationToken: ct });
setTimeout(() => ct.cancel(), 5000);
let reply: Reply | undefined;
try {
 reply = await replies!.receive();
} catch (error) {
 reply = undefined;
}`

## Source info API change

The `SourceInfo` API went through some changes. Now both source id and sequence number need to be specified to construct a `SourceInfo` struct. In addition `Sample::source_info` and `Query::source_info` getters return an `Option<SourceInfo>` which contains a `None` value if it was not set by the sender side.

`SourceInfo`
`SourceInfo`
`Sample::source_info`
`Query::source_info`
`Option<SourceInfo>`
`None`
`let publisher = session1.declare_publisher("key/expression").await.unwrap();
let subscriber = session2.declare_subscriber("key/expression").await.unwrap();
publisher.put("data").source_info(SourceInfo::new(id, sn)).unwrap();
// ...
let sample = subscriber.recv_async().await.unwrap();
if let Some(source_info) = sample.source_info() {
 println!("Received sample sn: {} from {}:{}", source_info.source_sn(), source_info.source_id().zid(), source_info.source_id().eid());
}`

We also simplified SourceInfo struct in Zenoh-C and Zenoh-Pico making it no longer owned, but a trivial POD type:

`z_entity_global_id_t egid = z_session_id(z_loan(session));
uint32_t sn = z_random_u32();
z_source_info_t source_info = z_source_info_new(&egid, sn);
z_put_options_t opts;
z_put_options_default(&opts);
opts.source_info = &source_info;
z_session_put(z_loan(key_expression), z_move(payload), &opts);
// Upon sample reception ...
z_source_info_t* sample_source_info = z_sample_source_info(z_loan(sample));
if (sample_source_info != NULL) {
 z_entity_global_id_t source_id = z_source_info_id(sample_source_info);
 uint32_t source_sn = z_source_info_sn(sample_source_info);
 z_id_t zid = z_entity_global_id_zid(&source_id);
 uint32_t eid = z_entity_global_id_eid(&source_id);
 z_owned_string_t id_string;
 z_id_to_string(&zid, &id_string);
 printf("Received sample %lu from %.*s : %lu\n", source_sn, (int)z_string_len(z_loan(id_string)), z_string_data(z_loan(id_string)), eid);
 z_drop(z_move(id_string));
}`

## SHM Improvements

**Making SHM Easier: Transport Provider Now Public**

Zenoh’s internal Shared Memory (SHM) Provider, used within the transport layer, is now available via public API ([PR](https://github.com/eclipse-zenoh/zenoh/pull/2221)).

**What does this mean for you?**

Previously, to use SHM, you had to instantiate and manage your own provider in userland. Now, you can directly utilize the optimized, transport-internal provider, simplifying your code, reducing complexity, and ensuring better integration with Zenoh’s core.

**Understanding the Provider’s State Machine**

The API exposes the provider’s state machine, which is crucial for robust integration. Its lazy-init lifecycle is managed via the `ShmProviderState` enum. Here’s a detailed breakdown of each state and the typical transitions:

`ShmProviderState`
`pub enum ShmProviderState {
 Disabled,
 Initializing,
 Ready(Arc<ShmProvider<PosixShmProviderBackend>>),
 Error,
}`
`Disabled`
`transport_optimization`
`Initializing`
`Ready`
`Error`
`Ready`
`Error`
`Ready(Arc<ShmProvider<PosixShmProviderBackend>>)`
`Arc<ShmProvider>`
`Arc`
`Error`

**Example:**

`let session = zenoh::open(zenoh::Config::default()).await.unwrap();
// Try to get session's provider for the first time - it is not immediately available
let shm_provider = session.get_shm_provider();
assert!(shm_provider.into_option().is_none());
// Wait a moment
std::thread::sleep(std::time::Duration::from_millis(100));
// Provider becomes available
let shm_provider = session.get_shm_provider();
assert!(shm_provider.into_option().is_some());`

**Practical Implication for Developers:**

You no longer need to manage this lifecycle yourself. Instead of instantiating your own provider, you can now query or observe the transport’s provider state and seamlessly hook into the ready provider when it becomes available. This leads to more reliable and less verbose integration code.

### C Bindings for the Transport SHM Provider

Following the introduction of the public Transport SHM Provider API in Rust ([PR](https://github.com/eclipse-zenoh/zenoh/pull/2221)), we’ve extended this functionality to the C ecosystem ([PR](https://github.com/eclipse-zenoh/zenoh-c/pull/1132)).

#### Key Features of the C Bindings

##### 1. Full State Machine Exposure

The C bindings faithfully expose the complete state machine from the Rust implementation:

`typedef enum {
 Z_SHM_PROVIDER_STATE_DISABLED,
 Z_SHM_PROVIDER_STATE_INITIALIZING,
 Z_SHM_PROVIDER_STATE_READY,
 Z_SHM_PROVIDER_STATE_ERROR
} z_shm_provider_state_t;`

Each state corresponds directly to its Rust counterpart, ensuring consistent behavior across language boundaries.

##### 2. State access API

State access API is also similar to Rust:

`z_result_t z_obtain_shm_provider(
 const struct z_loaned_session_t *this_,
 struct z_owned_shared_shm_provider_t *out_provider,
 enum z_shm_provider_state *out_state
);`

##### 3. Shared SHM Provider design

`z_owned_shared_shm_provider_t` is an owned representation of shared strong reference to underlying z\_owned\_shm\_provider\_t. It is designed to support `z_clone()` for z\_owned\_shm\_provider\_t and can be loaned as z\_loaned\_shm\_provider\_t:

`z_owned_shared_shm_provider_t`
`z_clone()`
`const z_loaned_shm_provider_t* provider =
 z_shared_shm_provider_loan_as(z_loan(shared_provider));`

### Transport SHM Provider in C++

To reflect C API additions, similar changes were made in C++ bindings, including provider state machine and SharedShmProvider.

#### Semantic changes for State Machine

The provider’s state is exposed similarly, but with a few semantic changes.

The “non-available” state is expressed with the enum:

`/// @brief The non-ready state for SHM provider.
enum class ShmProviderNotReadyState {
 /// Provider is disabled by configuration.
 SHM_PROVIDER_DISABLED,
 /// Provider is concurrently-initializing.
 SHM_PROVIDER_INITIALIZING,
 /// Error initializing provider.
 SHM_PROVIDER_ERROR,
};`

And the full provider state looks like this:

`std::variant<SharedShmProvider, ShmProviderNotReadyState>`

#### API usage example

`auto session = Session::open(Config::create_default());
auto provider_state = session.get_shm_provider();
if (std::holds_alternative<ShmProviderNotReadyState>(provider_state)) {
 auto state = std::get<ShmProviderNotReadyState>(provider_state);
 // inspect state: SHM_PROVIDER_DISABLED / INITIALIZING / ERROR
} else {
 auto provider = std::get<SharedShmProvider>(provider_state);
 // call provider methods (introspection, tuning, diagnostics, etc.)
}`

## Zenoh-Pico

### Local messages optimization

This release features a co-locazation optimization. PUT/DELETE, query, reply and reply-final messages whose key expressions are declared in the same session are delivered directly without going through the transport layer. This removes serialization, syscalls and network I/O for local flows which helps reduce latency and CPU usage for in-process or single-device use cases. More importantly this all happens with zero-copies.

Additionally, Zenoh-Pico now exposes a locality selector z\_locality\_t, to control the locality of publications, subscriptions, etc., where the possible values are:

`Z_LOCALITY_ANY`
`Z_LOCALITY_SESSION_LOCAL`
`Z_LOCALITY_REMOTE`

You can configure locality via `allowed_origin` / `allowed_destination` fields in options such as `z_subscriber_options_t`, `z_publisher_options_t`, `z_put_options_t`, `z_queryable_options_t`, and querier/get options.

`allowed_origin`
`allowed_destination`
`z_subscriber_options_t`
`z_publisher_options_t`
`z_put_options_t`
`z_queryable_options_t`

**Behavior change note:** queries can now be handled locally. In previous releases, query/reply flows relied on the transport path and there was no same-session delivery mechanism for queries, so a querier and a queryable declared in the same session would not communicate in a purely local setup. In 1.7.x, the new loopback path allows local queryables to answer local queries without any network activity.

This feature is enabled by `Z_FEATURE_LOCAL_SUBSCRIBER` and `Z_FEATURE_LOCAL_QUERYABLE` build options.

`Z_FEATURE_LOCAL_SUBSCRIBER`
`Z_FEATURE_LOCAL_QUERYABLE`

**Benchmark note:** The chart shows query throughput (msgs/s) per payload size. “Remote” is the following setup: two client sessions talking through a router (even running on the same host, AMD Ryzen 7 7840U, 64GB DDR5, Linux). “1.7.x (local)” is the new 1.7.x path: querier and queryable in the same `z_session_t` in the same process, communicating via in-process loopback. This local query scenario was not possible in previous releases, so the improvement reflects a new local path. Importantly, the remote curves for 1.6.2 vs 1.7.x show no regressions in the existing remote workflow.

`z_session_t`

![Query throughput](../../img/20251211-zenoh-jiaolong/pico_local_thr.png)

![Query throughput](../../img/20251211-zenoh-jiaolong/pico_local_thr.png)

And the following chart shows latency for the same scenarios:

![Query latency](../../img/20251211-zenoh-jiaolong/pico_local_latency.png)

![Query latency](../../img/20251211-zenoh-jiaolong/pico_local_latency.png)

### Automatic tasks start/stop

In multi-thread builds, Zenoh-Pico can now manage its background tasks automatically. `z_open()` can autostart the read and lease tasks (enabled by default), so most applications no longer need to call `zp_start_read_task()` / `zp_start_lease_task()` manually. This also works nicely with restarting tasks on reconnect: tasks are restarted only if they were configured to run.

`z_open()`
`zp_start_read_task()`
`zp_start_lease_task()`

This behavior is controlled via `z_open_options_t`. Users can initialize it with `z_open_options_default()` and pass it to `z_open()`. The defaults keep autostart enabled for read and lease tasks. If your application needs stricter control, you can disable autostart and continue starting/stopping tasks explicitly. There is also a separate switch to autostart the periodic scheduler task (only when periodic tasks are compiled in), so you can keep periodic work fully manual or let Zenoh-Pico manage it.

`z_open_options_t`
`z_open_options_default()`
`z_open()`

Example:

`z_open_options_t opts;
z_open_options_default(&opts);
// opts.auto_start_read_task = false; // Default is true
// opts.auto_start_lease_task = false; // Default is true
// opts.auto_start_periodic_task = true; // Disabled by default, requires periodic tasks feature enabled
z_open(&session, z_move(config), &opts);`

### Peer mode improvements

When a Zenoh Pico peer was connected to a router, late-joining subscribers behind that router could miss publications because the writer didn’t advertise the correct interest flags to the router. We now include the missing `KEYEXPRS` and `FUTURE` interest flags, so `peer → router → client` flows work reliably.

`KEYEXPRS`
`FUTURE`
`peer → router → client`

## Zenoh-C

### Locality API updates

With local subscriber/queryable support being introduced in Zenoh-Pico, `zc_locality` enum was renamed into `z_locality`. The `zc_` prefixed version is still kept for backward compatibility, but marked as deprecated.

`zc_locality`
`z_locality`
`zc_`

## zenoh-plugin-dds

The Zenoh DDS Plugin now supports [DDS Security](https://cyclonedds.io/docs/cyclonedds/latest/security/dds_security.html) on Linux and macOS as an optional feature. The Authentication, AccessControl and Cryptographic service plugins are included as part of the plugin.

## zenoh-dissector

Zenoh-dissector now fully supports the latest Wireshark 4.6, leveraging its latest library for enhanced protocol dissection for the latest Zenoh protocol 1.7.x.

## Changelogs

The full changelog for every Zenoh repository is available at the following links:

[Rust](https://github.com/eclipse-zenoh/zenoh/releases) | [C](https://github.com/eclipse-zenoh/zenoh-c/releases) | [C++](https://github.com/eclipse-zenoh/zenoh-cpp/releases) | [Python](https://github.com/eclipse-zenoh/zenoh-python/releases) | [Java](https://github.com/eclipse-zenoh/zenoh-java/releases) | [Kotlin](https://github.com/eclipse-zenoh/zenoh-kotlin/releases) | [TypeScript](https://github.com/eclipse-zenoh/zenoh-ts/releases) | [Pico](https://github.com/eclipse-zenoh/zenoh-pico/releases) | [DDS plugin](https://github.com/eclipse-zenoh/zenoh-plugin-dds/releases) | [ROS2 plugin](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds/releases) | [MQTT plugin](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt/releases) | [WebServer plugin](https://github.com/eclipse-zenoh/zenoh-plugin-webserver/releases) | [Filesystem backend](https://github.com/eclipse-zenoh/zenoh-backend-filesystem/releases) | [RocksDB backend](https://github.com/eclipse-zenoh/zenoh-backend-rocksdb/releases) | [S3 backend](https://github.com/eclipse-zenoh/zenoh-backend-s3/releases) | [InfluxDB backend](https://github.com/eclipse-zenoh/zenoh-backend-influxdb/releases)

That’s a wrap for Zenoh 1.7.x — **Jiāolóng**! This release delivers practical improvements that make Zenoh easier to use and more powerful — from query cancellation that gives you control over long-running operations, to local message optimization in Zenoh-Pico that eliminates unnecessary network hops, to direct access to the transport SHM provider that simplifies zero-copy workflows.

Whether you’re building responsive distributed queries, optimizing embedded applications, securing DDS communication, or leveraging shared memory for high-performance data flows, this release provides the tools and refinements to make your work more productive and your systems more reliable.

We’re excited to see what you’ll build with these enhancements. As always, your feedback, contributions, and success stories help shape the future of Zenoh. Join the conversation, share your experiences, and help us continue making Zenoh better for everyone.

You can reach us on [Zenoh’s Discord server](https://discord.com/invite/vSDSpqnbkm)!

Like the Jiāolóng commanding the flow of data streams, may your systems flow effortlessly and powerfully,

**– The Zenoh Team**

##### Eclipse Incubation

![](../../img/eclipse-incubation.png)

![](../../img/eclipse-incubation.png)

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

[![](../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../img/eclipse-foundation.svg)

[![](../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../docs/overview/what-is-zenoh)

![](../../img/zenoh-dragon-150x163.png)

![](../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

