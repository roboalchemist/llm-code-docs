# Source: https://rocket.rs/guide/v0.5/fairings/

Title: Fairings - Rocket Web Framework

URL Source: https://rocket.rs/guide/v0.5/fairings/

Markdown Content:
Fairings are Rocket's approach to structured middleware. With fairings, your application can hook into the request lifecycle to record or rewrite information about incoming requests and outgoing responses.

[](https://rocket.rs/guide/v0.5/fairings/#overview "anchor")Overview
--------------------------------------------------------------------

Any type that implements the [`Fairing`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html) trait is a _fairing_. Fairings hook into Rocket's request lifecycle, receiving callbacks for events such as incoming requests and outgoing responses. Rocket passes information about these events to the fairing; the fairing can do what it wants with the information. This includes rewriting requests or responses, recording information about the event, or doing nothing at all.

Rocket’s fairings are a lot like middleware from other frameworks, but they bear a few key distinctions:

* Fairings **cannot** terminate or respond to an incoming request directly.
* Fairings **cannot** inject arbitrary, non-request data into a request.
* Fairings _can_ prevent an application from launching.
* Fairings _can_ inspect and modify the application's configuration.

If you are familiar with middleware from other frameworks, you may find yourself reaching for fairings instinctively. Before doing so, remember that Rocket provides a rich set of mechanisms such as [request guards](https://rocket.rs/guide/v0.5/requests/#request-guards) and [data guards](https://rocket.rs/guide/v0.5/requests/#body-data) that can be used to solve problems in a clean, composable, and robust manner.

As a general rule of thumb, only _globally applicable_ actions should be effected through fairings. You should **_not_** use a fairing to implement authentication or authorization (preferring to use a [request guard](https://rocket.rs/guide/v0.5/requests/#request-guards) instead) _unless_ the authentication or authorization applies to all or the overwhelming majority of the application. On the other hand, you _should_ use a fairing to record timing and usage statistics or to enforce global security policies.

### [](https://rocket.rs/guide/v0.5/fairings/#attaching "anchor")Attaching

Fairings are registered with Rocket via the [`attach`](https://api.rocket.rs/v0.5/rocket/struct.Rocket.html#method.attach) method on a [`Rocket`](https://api.rocket.rs/v0.5/rocket/struct.Rocket.html) instance. Only when a fairing is attached will its callbacks fire. As an example, the following snippet attached two fairings, `req_fairing` and `res_fairing`, to a new Rocket instance:

1
2
3
4
5
6#[launch]fn rocket() -> _{ rocket::build() .attach(req_fairing) .attach(res_fairing)}

Fairings are executed in the order in which they are attached: the first attached fairing has its callbacks executed before all others. A fairing can be attached any number of times. Except for [singleton fairings](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#singletons), all attached instances are polled at runtime. Fairing callbacks may not be commutative; the order in which fairings are attached may be significant.

### [](https://rocket.rs/guide/v0.5/fairings/#callbacks "anchor")Callbacks

There are five events for which Rocket issues fairing callbacks. Each of these events is briefly described below and in details in the [`Fairing`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html) trait docs:

* **Ignite (`on_ignite`)**

An ignite callback is called during [ignition](https://api.rocket.rs/v0.5/rocket/struct.Rocket.html#method.ignite) An ignite callback can arbitrarily modify the `Rocket` instance being built. They are commonly used to parse and validate configuration values, aborting on bad configurations, and inserting the parsed value into managed state for later retrieval.

* **Liftoff (`on_liftoff`)**

A liftoff callback is called immediately after a Rocket application has launched. A liftoff callback can inspect the `Rocket` instance being launched. A liftoff callback can be a convenient hook for launching services related to the Rocket application being launched.

* **Request (`on_request`)**

A request callback is called just after a request is received. A request callback can modify the request at will and peek into the incoming data. It may not, however, abort or respond directly to the request; these issues are better handled via request guards or via response callbacks.

* **Response (`on_response`)**

A response callback is called when a response is ready to be sent to the client. A response callback can modify part or all of the response. As such, a response fairing can be used to provide a response when the greater application fails by rewriting **404** responses as desired. As another example, response fairings can also be used to inject headers into all outgoing responses.

* **Shutdown (`on_shutdown`)**

A shutdown callback is called when [shutdown is triggered](https://api.rocket.rs/v0.5/rocket/config/struct.Shutdown.html#triggers). At this point, graceful shutdown has commenced but not completed; no new requests are accepted but the application may still be actively serving existing requests. All registered shutdown fairings are run concurrently; resolution of all fairings is awaited before resuming shutdown.

[](https://rocket.rs/guide/v0.5/fairings/#implementing "anchor")Implementing
----------------------------------------------------------------------------

Recall that a fairing is any type that implements the [`Fairing`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html) trait. A `Fairing` implementation has one required method: [`info`](https://api.rocket.rs/v0.5/rocket/fairing/struct.Info.html), which returns an [`Info`](https://api.rocket.rs/v0.5/rocket/fairing/struct.Info.html) structure. This structure is used by Rocket to assign a name to the fairing and determine the set of callbacks the fairing is registering for. A `Fairing` can implement any of the available callbacks: [`on_ignite`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#method.on_ignite), [`on_liftoff`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#method.on_liftoff), [`on_request`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#method.on_request), [`on_response`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#method.on_response), and [`on_shutdown`](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#method.on_shutdown). Each callback has a default implementation that does absolutely nothing.

### [](https://rocket.rs/guide/v0.5/fairings/#requirements "anchor")Requirements

A type implementing `Fairing` is required to be `Send + Sync + 'static`. This means that the fairing must be sendable across thread boundaries (`Send`), thread-safe (`Sync`), and have only static references, if any (`'static`). Note that these bounds _do not_ prohibit a `Fairing` from holding state: the state need simply be thread-safe and statically available or heap allocated.

### [](https://rocket.rs/guide/v0.5/fairings/#example "anchor")Example

As an example, we want to record the number of `GET` and `POST` requests that our application has received. While we could do this with request guards and managed state, it would require us to annotate every `GET` and `POST` request with custom types, polluting handler signatures. Instead, we can create a simple fairing that acts globally.

The code for a `Counter` fairing below implements exactly this. The fairing receives a request callback, where it increments a counter on each `GET` and `POST` request. It also receives a response callback, where it responds to unrouted requests to the `/counts` path by returning the recorded number of counts.

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
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49 use std::io::Cursor;use std::sync::atomic::{AtomicUsize, Ordering};use rocket::{Request, Data, Response};use rocket::fairing::{Fairing, Info, Kind};use rocket::http::{Method, ContentType, Status};struct Counter { get: AtomicUsize, post: AtomicUsize, }#[rocket::async_trait]impl Fairing for Counter { fn info(&self) -> Info { Info { name: "GET/POST Counter", kind: Kind::Request | Kind::Response } } async fn on_request(&self, request: &mut Request<'_>, _: &mut Data<'_>) { match request.method() { Method::Get => self.get.fetch_add(1, Ordering::Relaxed), Method::Post => self.post.fetch_add(1, Ordering::Relaxed), _ => return }; } async fn on_response<'r>(&self, request: &'r Request<'_>, response: &mut Response<'r>) { if response.status() != Status::NotFound { return } if request.method() == Method::Get && request.uri().path() == "/counts" { let get_count = self.get.load(Ordering::Relaxed); let post_count = self.post.load(Ordering::Relaxed); let body = format!("Get: {}\n Post: {}", get_count, post_count); response.set_status(Status::Ok); response.set_header(ContentType::Plain); response.set_sized_body(body.len(), Cursor::new(body)); } }}

The complete example can be found in the [`Fairing` documentation](https://api.rocket.rs/v0.5/rocket/fairing/trait.Fairing.html#example).

[](https://rocket.rs/guide/v0.5/fairings/#ad-hoc-fairings "anchor")Ad-Hoc Fairings
----------------------------------------------------------------------------------

For simpler cases, implementing the `Fairing` trait can be cumbersome. This is why Rocket provides the [`AdHoc`](https://api.rocket.rs/v0.5/rocket/fairing/struct.AdHoc.html) type, which creates a fairing from a simple function or closure. Using the `AdHoc` type is easy: simply call the `on_ignite`, `on_liftoff`, `on_request`, `on_response`, or `on_shutdown` constructors on `AdHoc` to create a fairing from a function or closure.

As an example, the code below creates a `Rocket` instance with two attached ad-hoc fairings. The first, a liftoff fairing named "Liftoff Printer", prints a message indicating that the application has launched. The second named "Put Rewriter", a request fairing, rewrites the method of all requests to be `PUT`.

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
13 use rocket::fairing::AdHoc;use rocket::http::Method;rocket::build() .attach(AdHoc::on_liftoff("Liftoff Printer", |_| Box::pin(async move { println!("...annnddd we have liftoff!"); }))) .attach(AdHoc::on_request("Put Rewriter", |req, _| Box::pin(async move { req.set_method(Method::Put); }))) .attach(AdHoc::on_shutdown("Shutdown Printer", |_| Box::pin(async move { println!("...shutdown has commenced!"); })));

* * *
