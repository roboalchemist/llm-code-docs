# Source: https://rocket.rs/guide/v0.5/faq/

Title: FAQ - Rocket Web Framework

URL Source: https://rocket.rs/guide/v0.5/faq/

Markdown Content:
![Image 1: cloud](https://rocket.rs/images/cloud-0.png)![Image 2: cloud](https://rocket.rs/images/cloud-1.png)![Image 3: cloud](https://rocket.rs/images/cloud-2.png)![Image 4: cloud](https://rocket.rs/images/cloud-0.png)![Image 5: cloud](https://rocket.rs/images/cloud-0.png)![Image 6: cloud](https://rocket.rs/images/cloud-0.png)

Below you'll find a collection of commonly asked questions and answers. If you have suggestions for questions you'd like to see answered here, [comment on the discussion thread](https://github.com/rwf2/Rocket/discussions/1836).

[](https://rocket.rs/guide/v0.5/faq/#about-rocket "anchor")About Rocket
-----------------------------------------------------------------------

[#](https://rocket.rs/guide/v0.5/faq/#monolithic "anchor")
Is Rocket a monolithic framework like Rails? Or is it more like Flask?

Neither!

Rocket's core is small yet complete with respect to security and correctness. It mainly consists of:

* Guard traits like [`FromRequest`](https://api.rocket.rs/v0.5/rocket/request/trait.FromRequest.html) and [`FromData`](https://api.rocket.rs/v0.5/rocket/data/trait.FromData.html).
* Derive macros for all common traits.
* Attribute macros for routing.
* Thorough compile and launch-time checking.
* Zero-copy parsers and validators for common formats like multipart and SSE.
* Syntax sugar extensions for features like async streams and traits.
* Optional features for functionality like TLS, secrets, and so on.

The goal is for functionality like templating, sessions, ORMs, and so on to be implemented entirely outside of Rocket while maintaining a first-class feel and experience. Indeed, crates like [`rocket_dyn_templates`](https://api.rocket.rs/v0.5/rocket_dyn_templates/) and [`rocket_db_pools`](https://api.rocket.rs/v0.5/rocket_db_pools/) do just this. As a result, Rocket is neither "bare-bones" nor is it a kitchen sink for all possible features.

Unlike other frameworks, Rocket makes it its mission to help you avoid security and correctness blunders. It does this by including, out-of-the-box:

* A flexible, type-based [configuration](https://rocket.rs/guide/v0.5/configuration/) system.
* [Security and privacy headers](https://api.rocket.rs/v0.5/rocket/shield/) by default.
* Zero-Copy RFC compliant [URI parsers](https://api.rocket.rs/v0.5/rocket/http/uri).
* Safe, [typed URIs](https://api.rocket.rs/v0.5/rocket/macro.uri.html) with compile-time checking.
* [Compile-time and launch-time route checking](https://api.rocket.rs/v0.5/rocket/attr.route.html).
* A [testing framework](https://api.rocket.rs/v0.5/rocket/local) with sync and `async` variants.
* Safe, exclusive access to fully decoded HTTP values.
* Mandatory [data limits](https://api.rocket.rs/v0.5/rocket/data/struct.Limits.html) to prevent trivial DoS attacks.

Of course, this functionality comes at a compile-time cost (but notably, _not_ a runtime cost), impacting Rocket's clean build-time. For comparison, here's what a clean build of "Hello, world!" looks like for some Rust web frameworks:

| Framework | Dependencies | Build Time | Build w/ `sscache` |
| --- | --- | --- | --- |
| Rocket 0.5 | 105 | 12s | 5s |
| Actix-Web 4.4.0 | 119 | 11s | 4s |
| Axum 0.6.20 | 78 | 10s | 4s |

· Measurements taken on Apple Mac14,6 M2 Max, macOS 13, Rust 1.75. Best of 3.

· Rocket includes features like graceful shutdown, HTTP/2 keepalive, SSE support, and static file serving that require additional deps in other frameworks.

Of course, iterative build-time is nearly identical for all frameworks, and the time can be further reduced by using faster linkers like `lld`. We think the trade-off is worth it. Rocket will never compromise security, correctness, or usability to "win" at benchmarks of any sort.

[#](https://rocket.rs/guide/v0.5/faq/#compact "anchor")
I want a small and compact web framework. Is Rocket it?

We think so! See ["Is Rocket a monolithic framework like Rails?"](https://rocket.rs/guide/v0.5/faq/#monolithic)

[#](https://rocket.rs/guide/v0.5/faq/#complete "anchor")
I want a web framework with all the bells and whistles. Is Rocket it?

We think so! See ["Is Rocket a monolithic framework like Rails?"](https://rocket.rs/guide/v0.5/faq/#monolithic)

[#](https://rocket.rs/guide/v0.5/faq/#in-prod "anchor")
Can I use Rocket in production? Should I? It's only v0.x!

We **enthusiastically** recommend using Rocket in production, with the following non-exhaustive list of caveats:

1. Run Rocket behind a reverse proxy like HAProxy or in a production load balancing environment. Rocket (Hyper) doesn't employ any defenses against DDoS attacks or certain DoS attacks which can be mitigated by an external service.

2. Use a TLS termination proxy (perhaps from 1.) for zero-downtime certificate rotation.

3. Properly configure your databases and database pools, especially with respect to the pool size.

4. Ensure no blocking I/O happens outside of `spawn_blocking()` invocations.

While Rocket _is_ still in the `0.x` phase, the version number is purely a stylistic choice. In fact, we consider Rocket to be the most mature web framework in the Rust ecosystem. To our knowledge, Rocket is the only Rust web framework that correctly implements:

* Server-Sent Events
* Graceful Shutdown
* Form Parsing with Arbitrarily Structure
* Zero-Copy, RFC Conforming URI Types
* Ambiguity-Free Routing
* Streamed Multipart Uploads

If you're coming from a different ecosystem, you should feel comfortable considering Rocket's `v0.x` as someone else's `vx.0`. Rust and Cargo's semver policy, and Rocket's strict adherence to it, ensures that Rocket will _never_ break your application when upgrading from `0.x.y` to `0.x.z`, where `z >= y`. Furthermore, we backport _all_ security and correctness patches to the previous major release (`0.{x-1}.y`), so your application remains secure if you need time to upgrade.

[#](https://rocket.rs/guide/v0.5/faq/#performance "anchor")
Is Rocket slow? Is Rocket fast?

Rocket is pretty fast.

A commonly repeated myth is that Rocket's great usability comes at the cost of runtime performance. _**This is false.**_ Rocket's usability derives largely from compile-time checks with _zero_ bearing on runtime performance.

So what about benchmarks? Well, benchmarking is _hard_, and besides often being conducted incorrectly _*_, often appear to say more than they do. So, when you see a benchmark for "Hello, world!", you should know that the benchmark's relevance doesn't extend far beyond those specific "Hello, world!" servers and the specific way the measurement was taken. In other words, it provides _some_ baseline that is hard to extrapolate to real-world use-cases, _your_ use-case.

Nevertheless, here are some things you can consider as _generally_ true about Rocket applications:

* They'll perform much, _much_ better than those written in scripting languages like Python or Ruby.
* They'll perform much better than those written in VM or JIT languages like JavaScript or Java.
* They'll perform a bit better than those written in compiled-to-native but GC'd languages like Go.
* They'll perform competitively with those written in compiled-to-native, non-GC'd languages like Rust or C.

Again, we emphasize _generally_ true. It is trivial to write a Rocket application that is slower than a similar Python application.

Besides a framework's _internal_ performance, you should also consider whether it enables your _application itself_ to perform well. Rocket takes great care to enable your application to perform as little work as possible through unique-to-Rocket features like [managed state](https://rocket.rs/guide/v0.5/state/#managed-state), [request-local state](https://rocket.rs/guide/v0.5/state/#request-local-state), and zero-copy parsing and deserialization.

* A common mistake is to pit against Rocket's "Hello, world!" without normalizing for response size, especially security headers.

[#](https://rocket.rs/guide/v0.5/faq/#showcase "anchor")
What are some examples of "big" apps written in Rocket?

Here are some notable projects and websites in Rocket we're aware of:

* [Vaultwarden](https://github.com/dani-garcia/vaultwarden) - A BitWarden Server
* [Rust-Lang.org](https://www.rust-lang.org/) - Rust Language Website
* [Plume](https://github.com/Plume-org/Plume) - Federated Blogging Engine
* [Hagrid](https://gitlab.com/keys.openpgp.org/hagrid) - OpenPGP KeyServer ([keys.openpgp.org](https://keys.openpgp.org/))
* [SourceGraph Syntax Highlighter](https://github.com/sourcegraph/sourcegraph/tree/main/docker-images/syntax-highlighter) - Syntax Highlighting API
* [Revolt](https://github.com/revoltchat/backend) - Open source user-first chat platform

[Let us know](https://github.com/rwf2/Rocket/discussions/categories/show-and-tell) if you have a notable, public facing application written in Rocket you'd like to see here!

[#](https://rocket.rs/guide/v0.5/faq/#releases "anchor")
When will version `$y` be released? Why does it take so long?

Rocket represents an ecosystem-wide effort to create a web framework that enables writing web applications with unparalleled security, performance, and usability. From design to implementation to documentation, Rocket is carefully crafted to ensure the greatest productivity and reliability with the fewest surprises. Our goal is to make Rocket a compelling choice across _all_ languages.

Accomplishing this takes time, and our efforts extend to the entire ecosystem. For example, work for Rocket v0.5 included:

* [Fixing correctness issues in `x509-parser`.](https://github.com/rusticata/x509-parser/pull/90)
* [Reporting multiple](https://github.com/bikeshedder/deadpool/issues/114)[correctness issues](https://github.com/bikeshedder/deadpool/issues/113) in `deadpool`.
* [Fixing a major usability issue in `async-stream`.](https://github.com/tokio-rs/async-stream/pull/57)
* [Creating a brand new configuration library.](https://github.com/SergioBenitez/Figment)
* [Updating](https://github.com/rousan/multer-rs/pull/21), [fixing](https://github.com/rousan/multer-rs/pull/29), and [maintaining](https://github.com/rousan/multer-rs/commit/2758e778e6aa2785b737c82fe45e58026bea2f01)`multer`.
* [Significantly improving `async_trait` correctness and usability.](https://github.com/dtolnay/async-trait/pull/143)
* [Porting `Pattern` APIs to stable.](https://github.com/SergioBenitez/stable-pattern)
* [Porting macro diagnostics to stable.](https://github.com/SergioBenitez/proc-macro2-diagnostics)
* [Creating a brand new byte unit library.](https://github.com/SergioBenitez/ubyte)
* [Fixing a bug in `rustc`'s `libtest`.](https://github.com/rust-lang/rust/pull/78227)

A version of Rocket is released whenever it is feature-complete and exceeds feature, security, and usability parity with the previous version. As a result, specifying a release date is nearly impossible. We are _always_ willing to delay a release if these properties are not readily evident.

We know it can be frustrating, but we hope you'll agree that Rocket is worth the wait.

[](https://rocket.rs/guide/v0.5/faq/#how-to "anchor")How To
-----------------------------------------------------------

[#](https://rocket.rs/guide/v0.5/faq/#web-sockets "anchor")
Can I, and if so how, do I use WebSockets?

You can! WebSocket support is provided by the officially maintained [`rocket_ws`](https://api.rocket.rs/v0.5/rocket_ws/) crate. You'll find all the docs you need there.

Rocket _also_ supports [Server-Sent Events](https://api.rocket.rs/v0.5/rocket/response/stream/struct.EventStream.html), which allows for real-time _unidirectional_ communication from the server to the client. The protocol is a bit simpler, and you may find SSE sufficient for your use-case. For instance, the [chat example](https://github.com/rwf2/Rocket/tree/v0.5/examples/chat) uses SSE to implement a real-time, multiroom chat application.

[#](https://rocket.rs/guide/v0.5/faq/#global-state "anchor")
Should I use global state via something like `lazy_static!`?

No. Rocket's [managed state](https://rocket.rs/guide/v0.5/state/#managed-state) provides a better alternative.

While it may be convenient or comfortable to use global state, the downsides are numerous. They include:

* The inability to test your application with different state.
* The inability to run your application on different threads with different state.
* The inability to know the state a route accesses by looking at its signature.

[#](https://rocket.rs/guide/v0.5/faq/#file-uploads "anchor")
How do I handle file uploads? What is this "multipart" in my stream?

For a quick example on how to handle file uploads, see [multipart forms](https://rocket.rs/guide/v0.5/requests/#multipart). The gist is: use `Form<TempFile>` as a data guard.

File uploads are encoded and transmitted by the browser as [multipart](https://datatracker.ietf.org/doc/html/rfc7578) forms. The raw stream, as seen by [`Data`](https://api.rocket.rs/v0.5/rocket/struct.Data.html) for example, thus contains the necessary metadata to encode the form. Rocket's [`Form`](https://api.rocket.rs/v0.5/rocket/form/struct.Form.html) data guard can parse these form submissions into any type that implements [`FromForm`](https://api.rocket.rs/v0.5/rocket/form/trait.FromForm.html). This includes types like [`TempFile`](https://api.rocket.rs/v0.5/rocket/fs/enum.TempFile.html) which streams the decoded data to disk for persistence.

[#](https://rocket.rs/guide/v0.5/faq/#raw-request "anchor")
How do I get an `&Request` in a handler?

You don't!

Rocket's [philosophy](https://rocket.rs/guide/v0.5/introduction/#foreword) is that as much of the request should be validated and converted into useful typed values _before_ being processed. Allowing a `Request` to be handled directly is incompatible with this idea.

Instead, Rocket's handlers work through _guards_, reified as traits, which validate and extract parts of a request as needed. Rocket automatically invokes these guards for you, so custom guards are write-once-use-everywhere. Rocket won't invoke a handler with failing guards. This way, handlers only deal with fully validated, typed, secure values.

Rocket provides all of the guard implementations you would expect out-of-the-box, and you can implement your own, too. See the following:

* Parameter Guards: [`FromParam`](https://api.rocket.rs/v0.5/rocket/request/trait.FromParam.html)
* Multi-Segment Guards: [`FromSegments`](https://api.rocket.rs/v0.5/rocket/request/trait.FromSegments.html)
* Data Guards: [`FromData`](https://api.rocket.rs/v0.5/rocket/data/trait.FromData.html)
* Form Guards: [`FromForm`](https://api.rocket.rs/v0.5/rocket/form/trait.FromForm.html)
* Request Guards: [`FromRequest`](https://api.rocket.rs/v0.5/rocket/request/trait.FromRequest.html)

[#](https://rocket.rs/guide/v0.5/faq/#multiple-responses "anchor")
How do I make one handler return different responses or status codes?

If you're returning _two_ different responses, use a `Result<T, E>` or an [`Either<A, B>`](https://docs.rs/either/1/either/enum.Either.html).

If you need to return _more_ than two kinds, [derive a custom `Responder`](https://api.rocket.rs/v0.5/rocket/derive.Responder.html)`enum`:

1
2
3
4
5
6
7
8
9
10
11
12 use rocket::fs::NamedFile;use rocket::http::ContentType;#[derive(Responder)]enum Error<'r, T> { #[response(status = 400)] Unauthorized(T), #[response(status = 404)] NotFound(NamedFile), #[response(status = 500)] A(&'r str, ContentType),}

[#](https://rocket.rs/guide/v0.5/faq/#automatic-reload "anchor")
How do I make Rocket reload automatically when I change source code?

In debug mode, Rocket automatically reloads templates for you. So if all you need is live template reloading, Rocket's got you covered.

For everything else, you'll need to use an external tool like [`cargo-watch`](https://github.com/watchexec/cargo-watch), [`watchexec`](https://github.com/watchexec/watchexec) or [`entr`](http://eradman.com/entrproject/). With `cargo-watch`, you can automatically rebuild and run a Rocket application by executing:

1 cargo watch -x run

To only restart on successful compilations, see [this note](https://github.com/watchexec/cargo-watch/tree/b75ce2c260874dea480f4accfd46ab28709ec56a#restarting-an-application-only-if-the-buildcheck-succeeds).

[#](https://rocket.rs/guide/v0.5/faq/#external-managed-state "anchor")
How do I access managed state outside of a Rocket-related context?

Use an `Arc`, like this:

1
2
3
4
5
6
7
8
9
10
11
12
13 use std::sync::Arc;#[launch]fn rocket() -> _{ let state = Arc::new(MyState); let external = state.clone(); std::thread::spawn(move || { let use_state = external; }); rocket::build().manage(state)}

[#](https://rocket.rs/guide/v0.5/faq/#internal-server "anchor")
How do I make Rocket a _part_ of my application as opposed to the whole thing?

Use the `#[main]` attribute and manually call [`launch()`](https://api.rocket.rs/v0.5/rocket/struct.Rocket.html#method.launch):

1
2
3
4
5
6
7
8#[rocket::main] async fn main() { if should_start_server { let result = rocket::build().launch().await; } else { }}

The cost to using the attribute is imperceptible and guarantees compatibility with Rocket's async I/O.

[](https://rocket.rs/guide/v0.5/faq/#debugging "anchor")Debugging
-----------------------------------------------------------------

[#](https://rocket.rs/guide/v0.5/faq/#broken-example "anchor")
Is example `foo` broken? It doesn't work for me.

Almost certainly not.

Every example and code snippet you see in published documentation is tested by the CI on every commit, and we only publish docs that pass the CI. Unless the CI environment is broken, the examples _cannot_ be wrong.

Common mistakes when running examples include:

* Looking at an example for version `y` but depending on version `x`. Select the proper git tag!
* Looking at outdated examples on StackOverflow or Google. Check the date/version!
* Not configuring the correct dependencies. See the example's `Cargo.toml`!

[#](https://rocket.rs/guide/v0.5/faq/#unsat-bound "anchor")
The trait bound `rocket::Responder` (`FromRequest`, etc.) is not satisfied.

If you're fairly certain a type implements a given Rocket trait but still get an error like:

1
2
3
4
5
6
7 error[E0277]: the trait bound `Foo: Responder<'_, '_>` is not satisfied --> src\main.rs:4:20 | 4 | fn foo() -> Foo | ^^^ the trait `Responder<'_, '_>` is not implemented for `Foo` | = note: required by `respond_to`

...then you're almost certainly depending, perhaps transitively, on _two different versions_ of a single library. For example, you may be depending on `rocket` which depends on `time 0.3` while also depending directly on `time 0.2`. Or you may depending on `rocket` from `crates.io` while depending on a library that depends on `rocket` from `git`. A common instance of this mistake is to depend on a `contrib` library from git while also depending on a `crates.io` version of Rocket or vice-versa:

1
2 rocket = "0.5.1"rocket_db_pools = { git = "https://github.com/rwf2/Rocket.git" }

This is _never_ correct. If libraries or applications interact via types from a common library, those libraries or applications _must_ specify the _same_ version of that common library. This is because in Rust, types from two different versions of a library or from different providers (like `git` vs. `crates.io`) are _always_ considered distinct, even if they have the same name. Therefore, even if a type implements a trait from one library, it _does not_ implement the trait from the other library (since it is considered to be a _different_, _distinct_ library). In other words, you can _never_ mix two different published versions of Rocket, a published version and a `git` version, or two instances from different `git` revisions.

* * *

[](https://rocket.rs/guide/v0.5/conclusion/)[](https://rocket.rs/guide/v0.5/conclusion/)[](https://rocket.rs/guide/v0.5/conclusion/)![Image 7: cloud](https://rocket.rs/images/cloud-0.png)![Image 8: cloud](https://rocket.rs/images/cloud-1.png)![Image 9: cloud](https://rocket.rs/images/cloud-2.png)
