# Source: https://html.spec.whatwg.org/multipage/worklets.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/worklets.html

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 10 Web workers](https://html.spec.whatwg.org/multipage/workers.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [12 Web storage →](https://html.spec.whatwg.org/multipage/webstorage.html)
1.   [11 Worklets](https://html.spec.whatwg.org/multipage/worklets.html#worklets)
    1.   [11.1 Introduction](https://html.spec.whatwg.org/multipage/worklets.html#worklets-intro)
        1.   [11.1.1 Motivations](https://html.spec.whatwg.org/multipage/worklets.html#worklets-motivations)
        2.   [11.1.2 Code idempotence](https://html.spec.whatwg.org/multipage/worklets.html#worklets-idempotent)
        3.   [11.1.3 Speculative evaluation](https://html.spec.whatwg.org/multipage/worklets.html#worklets-speculative)

    2.   [11.2 Examples](https://html.spec.whatwg.org/multipage/worklets.html#worklets-examples)
        1.   [11.2.1 Loading scripts](https://html.spec.whatwg.org/multipage/worklets.html#worklets-examples-loading)
        2.   [11.2.2 Registering a class and invoking its methods](https://html.spec.whatwg.org/multipage/worklets.html#worklets-example-registering)

    3.   [11.3 Infrastructure](https://html.spec.whatwg.org/multipage/worklets.html#worklets-infrastructure)
        1.   [11.3.1 The global scope](https://html.spec.whatwg.org/multipage/worklets.html#worklets-global)
            1.   [11.3.1.1 Agents and event loops](https://html.spec.whatwg.org/multipage/worklets.html#worklet-agents-and-event-loops)
            2.   [11.3.1.2 Creation and termination](https://html.spec.whatwg.org/multipage/worklets.html#worklets-creation-termination)
            3.   [11.3.1.3 Script settings for worklets](https://html.spec.whatwg.org/multipage/worklets.html#script-settings-for-worklets)

        2.   [11.3.2 The `Worklet` class](https://html.spec.whatwg.org/multipage/worklets.html#worklets-worklet)
        3.   [11.3.3 The worklet's lifetime](https://html.spec.whatwg.org/multipage/worklets.html#worklets-lifetime)

11 Worklets[](https://html.spec.whatwg.org/multipage/worklets.html#worklets)
----------------------------------------------------------------------------

### 11.1 Introduction[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-intro)

_This section is non-normative._

Worklets are a piece of specification infrastructure which can be used for running scripts independent of the main JavaScript execution environment, while not requiring any particular implementation model.

The worklet infrastructure specified here cannot be used directly by web developers. Instead, other specifications build upon it to create directly-usable worklet types, specialized for running in particular parts of the browser implementation pipeline.

#### 11.1.1 Motivations[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-motivations)

_This section is non-normative._

Allowing extension points to rendering, or other sensitive parts of the implementation pipeline such as audio output, is difficult. If extension points were done with full access to the APIs available on `Window`, engines would need to abandon previously-held assumptions for what could happen in the middle of those phases. For example, during the layout phase, rendering engines assume that no DOM will be modified.

Additionally, defining extension points in the `Window` environment would restrict user agents to performing work in the same thread as the `Window` object. (Unless implementations added complex, high-overhead infrastructure to allow thread-safe APIs, as well as thread-joining guarantees.)

Worklets are designed to allow extension points, while keeping guarantees that user agents currently rely on. This is done through new global environments, based on subclasses of `WorkletGlobalScope`.

Worklets are similar to web workers. However, they:

*   Are thread-agnostic. That is, they are not designed to run on a dedicated separate thread, like each worker is. Implementations can run worklets wherever they choose (including on the main thread).

*   Are able to have multiple duplicate instances of the global scope created, for the purpose of parallelism.

*   Do not use an event-based API. Instead, classes are registered on the global scope, whose methods are invoked by the user agent.

*   Have a reduced API surface on the global scope.

*   Have a lifetime for their [global object](https://html.spec.whatwg.org/multipage/webappapis.html#global-object) which is defined by other specifications, often in an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) manner.

As worklets have relatively high overhead, they are best used sparingly. Due to this, a given `WorkletGlobalScope` is expected to be shared between multiple separate scripts. (This is similar to how a single `Window` is shared between multiple separate scripts.)

Worklets are a general technology that serve different use cases. Some worklets, such as those defined in CSS Painting API, provide extension points intended for stateless, idempotent, and short-running computations, which have special considerations as described in the next couple of sections. Others, such as those defined in Web Audio API, are used for stateful, long-running operations. [[CSSPAINT]](https://html.spec.whatwg.org/multipage/references.html#refsCSSPAINT)[[WEBAUDIO]](https://html.spec.whatwg.org/multipage/references.html#refsWEBAUDIO)

#### 11.1.2 Code idempotence[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-idempotent)

Some specifications which use worklets are intended to allow user agents to parallelize work over multiple threads, or to move work between threads as required. In these specifications, user agents might invoke methods on a web-developer-provided class in an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) order.

As a result of this, to prevent interoperability issues, authors who register classes on such `WorkletGlobalScope`s should make their code idempotent. That is, a method or set of methods on the class should produce the same output given a particular input.

This specification uses the following techniques in order to encourage authors to write code in an idempotent way:

*   No reference to the global object is available (i.e., there is no counterpart to `self` on `WorkletGlobalScope`).

Although this was the intention when worklets were first specified, the introduction of `globalThis` has made it no longer true. See [issue #6059](https://github.com/whatwg/html/issues/6059) for more discussion.

*   Code is loaded as a [module script](https://html.spec.whatwg.org/multipage/webappapis.html#module-script), which results in the code being executed in strict mode and with no shared `this` referencing the global proxy.

Together, these restrictions help prevent two different scripts from sharing state using properties of the [global object](https://html.spec.whatwg.org/multipage/webappapis.html#global-object).

Additionally, specifications which use worklets and intend to allow [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) behavior must obey the following:

*   They must require user agents to always have at least two `WorkletGlobalScope` instances per `Worklet`, and randomly assign a method or set of methods on a class to a particular `WorkletGlobalScope` instance. These specifications may provide an opt-out under memory constraints.

*   These specifications must allow user agents to create and destroy instances of their `WorkletGlobalScope` subclasses at any time.

#### 11.1.3 Speculative evaluation[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-speculative)

Some specifications which use worklets can invoke methods on a web-developer-provided class based on the state of the user agent. To increase concurrency between threads, a user agent may invoke a method speculatively, based on potential future states.

In these specifications, user agents might invoke such methods at any time, and with any arguments, not just ones corresponding to the current state of the user agent. The results of such speculative evaluations are not displayed immediately, but can be cached for use if the user agent state matches the speculated state. This can increase the concurrency between the user agent and worklet threads.

As a result of this, to prevent interoperability risks between user agents, authors who register classes on such `WorkletGlobalScope`s should make their code stateless. That is, the only effect of invoking a method should be its result, and not any side effects such as updating mutable state.

The same techniques which encourage [code idempotence](https://html.spec.whatwg.org/multipage/worklets.html#worklets-idempotent) also encourage authors to write stateless code.

### 11.2 Examples[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-examples)

_This section is non-normative._

For these examples, we'll use a fake worklet. The `Window` object provides two `Worklet` instances, which each run code in their own collection of `FakeWorkletGlobalScope`s:

Each `Window` has two `Worklet` instances, fake worklet 1 and fake worklet 2. Both of these have their [worklet global scope type](https://html.spec.whatwg.org/multipage/worklets.html#worklet-global-scope-type) set to `FakeWorkletGlobalScope`, and their [worklet destination type](https://html.spec.whatwg.org/multipage/worklets.html#worklet-destination-type) set to "`fakeworklet`". User agents should create at least two `FakeWorkletGlobalScope` instances per worklet.

"`fakeworklet`" is not actually a valid [destination](https://fetch.spec.whatwg.org/#concept-request-destination) per Fetch. But this illustrates how real worklets would generally have their own worklet-type-specific destination. [[FETCH]](https://html.spec.whatwg.org/multipage/references.html#refsFETCH)

The `fakeWorklet1` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [fake worklet 1](https://html.spec.whatwg.org/multipage/worklets.html#fake-worklet-1).

The `fakeWorklet2` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [fake worklet 2](https://html.spec.whatwg.org/multipage/worklets.html#fake-worklet-2).

* * *

Each `FakeWorkletGlobalScope` has a registered class constructors map, which is an [ordered map](https://infra.spec.whatwg.org/#ordered-map), initially empty.

The `registerFake(type, classConstructor)` method steps are to set [this](https://webidl.spec.whatwg.org/#this)'s [registered class constructors map](https://html.spec.whatwg.org/multipage/worklets.html#registered-class-constructors-map)[type] to classConstructor.

#### 11.2.1 Loading scripts[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-examples-loading)

_This section is non-normative._

To load scripts into [fake worklet 1](https://html.spec.whatwg.org/multipage/worklets.html#fake-worklet-1), a web developer would write:

```
window.fakeWorklet1.addModule('script1.mjs');
window.fakeWorklet1.addModule('script2.mjs');
```

Note that which script finishes fetching and runs first is dependent on network timing: it could be either `script1.mjs` or `script2.mjs`. This generally won't matter for well-written scripts intended to be loaded in worklets, if they follow the suggestions about preparing for [speculative evaluation](https://html.spec.whatwg.org/multipage/worklets.html#worklets-speculative).

If a web developer wants to perform a task only after the scripts have successfully run and loaded into some worklets, they could write:

```
Promise.all([
    window.fakeWorklet1.addModule('script1.mjs'),
    window.fakeWorklet2.addModule('script2.mjs')
]).then(() => {
    // Do something which relies on those scripts being loaded.
});
```

* * *

Another important point about script-loading is that loaded scripts can be run in multiple `WorkletGlobalScope`s per `Worklet`, as discussed in the section on [code idempotence](https://html.spec.whatwg.org/multipage/worklets.html#worklets-idempotent). In particular, the specification above for [fake worklet 1](https://html.spec.whatwg.org/multipage/worklets.html#fake-worklet-1) and [fake worklet 2](https://html.spec.whatwg.org/multipage/worklets.html#fake-worklet-2) require this. So, consider a scenario such as the following:

```
// script.mjs
console.log("Hello from a FakeWorkletGlobalScope!");
```

```
// app.mjs
window.fakeWorklet1.addModule("script.mjs");
```

This could result in output such as the following from a user agent's console:

```
[fakeWorklet1#1] Hello from a FakeWorkletGlobalScope!
[fakeWorklet1#4] Hello from a FakeWorkletGlobalScope!
[fakeWorklet1#2] Hello from a FakeWorkletGlobalScope!
[fakeWorklet1#3] Hello from a FakeWorkletGlobalScope!
```

If the user agent at some point decided to kill and restart the third instance of `FakeWorkletGlobalScope`, the console would again print `[fakeWorklet1#3] Hello from a FakeWorkletGlobalScope!` when this occurs.

#### 11.2.2 Registering a class and invoking its methods[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-example-registering)

_This section is non-normative._

Let's say that one of the intended usages of our fake worklet by web developers is to allow them to customize the highly-complex process of boolean negation. They might register their customization as follows:

```
// script.mjs
registerFake('negation-processor', class {
  process(arg) {
    return !arg;
  }
});
```

```
// app.mjs
window.fakeWorklet1.addModule("script.mjs");
```

To make use of such registered classes, the specification for fake worklets could define a find the opposite of true algorithm, given a `Worklet`worklet:

1.   Optionally, [create a worklet global scope](https://html.spec.whatwg.org/multipage/worklets.html#create-a-worklet-global-scope) for worklet.

2.   Let workletGlobalScope be one of worklet's [global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-global-scopes), chosen in an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) manner.

3.   Let classConstructor be workletGlobalScope's [registered class constructors map](https://html.spec.whatwg.org/multipage/worklets.html#registered-class-constructors-map)["`negation-processor`"].

4.   Let classInstance be the result of [constructing](https://webidl.spec.whatwg.org/#construct-a-callback-function)classConstructor, with no arguments.

5.   Let function be [Get](https://tc39.es/ecma262/#sec-get-o-p)(classInstance, "`process`"). Rethrow any exceptions.

6.   Let callback be the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)function to a Web IDL `Function` instance.

7.   Return the result of [invoking](https://webidl.spec.whatwg.org/#invoke-a-callback-function)callback with « true » and "`rethrow`", and with _[callback this value](https://webidl.spec.whatwg.org/#dfn-callback-this-value)_ set to classInstance.

Another, perhaps better, specification architecture would be to extract the "`process`" property and convert it into a `Function` at registration time, as part of the `registerFake()` method steps.

### 11.3 Infrastructure[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-infrastructure)

#### 11.3.1 The global scope[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-global)

Subclasses of `WorkletGlobalScope` are used to create [global objects](https://html.spec.whatwg.org/multipage/webappapis.html#global-object) wherein code loaded into a particular `Worklet` can execute.

```
[Exposed=Worklet, SecureContext]
interface WorkletGlobalScope {};
```

Other specifications are intended to subclass `WorkletGlobalScope`, adding APIs to register a class, as well as other APIs specific for their worklet type.

Each `WorkletGlobalScope` has an associated module map. It is a [module map](https://html.spec.whatwg.org/multipage/webappapis.html#module-map), initially empty.

##### 11.3.1.1 Agents and event loops[](https://html.spec.whatwg.org/multipage/worklets.html#worklet-agents-and-event-loops)

_This section is non-normative._

Each `WorkletGlobalScope` is contained in its own [worklet agent](https://html.spec.whatwg.org/multipage/webappapis.html#worklet-agent), which has its corresponding [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop). However, in practice, implementation of these agents and event loops is expected to be different from most others.

A [worklet agent](https://html.spec.whatwg.org/multipage/webappapis.html#worklet-agent) exists for each `WorkletGlobalScope` since, in theory, an implementation could use a separate thread for each `WorkletGlobalScope` instance, and allowing this level of parallelism is best done using agents. However, because their [[CanBlock]] value is false, there is no requirement that agents and threads are one-to-one. This allows implementations the freedom to execute scripts loaded into a worklet on any thread, including one running code from other agents with [[CanBlock]] of false, such as the thread of a [similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#similar-origin-window-agent) ("the main thread"). Contrast this with [dedicated worker agents](https://html.spec.whatwg.org/multipage/webappapis.html#dedicated-worker-agent), whose true value for [[CanBlock]] effectively requires them to get a dedicated operating system thread.

Worklet [event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) are also somewhat special. They are only used for [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) associated with `addModule()`, tasks wherein the user agent invokes author-defined methods, and [microtasks](https://html.spec.whatwg.org/multipage/webappapis.html#microtask). Thus, even though the [event loop processing model](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model) specifies that all event loops run continuously, implementations can achieve observably-equivalent results using a simpler strategy, which just [invokes](https://webidl.spec.whatwg.org/#invoke-a-callback-function) author-provided methods and then relies on that process to [perform a microtask checkpoint](https://html.spec.whatwg.org/multipage/webappapis.html#perform-a-microtask-checkpoint).

##### 11.3.1.2 Creation and termination[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-creation-termination)

To create a worklet global scope for a `Worklet`worklet:

1.   Let outsideSettings be worklet's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2.   Let agent be the result of [obtaining a worklet agent](https://html.spec.whatwg.org/multipage/webappapis.html#obtain-a-worklet-agent) given outsideSettings. Run the rest of these steps in that agent.

3.   Let realmExecutionContext be the result of [creating a new realm](https://html.spec.whatwg.org/multipage/webappapis.html#creating-a-new-javascript-realm) given agent and the following customizations:

    *   For the global object, create a new object of the type given by worklet's [worklet global scope type](https://html.spec.whatwg.org/multipage/worklets.html#worklet-global-scope-type).

4.   Let workletGlobalScope be the [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global) of realmExecutionContext's Realm component.

5.   Let insideSettings be the result of [setting up a worklet environment settings object](https://html.spec.whatwg.org/multipage/worklets.html#set-up-a-worklet-environment-settings-object) given realmExecutionContext and outsideSettings.

6.   Let pendingAddedModules be a [clone](https://infra.spec.whatwg.org/#list-clone) of worklet's [added modules list](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-added-modules-list).

7.   Let runNextAddedModule be the following steps:

    1.   If pendingAddedModules[is not empty](https://infra.spec.whatwg.org/#list-is-empty), then:

        1.   Let moduleURL be the result of [dequeuing](https://infra.spec.whatwg.org/#queue-dequeue) from pendingAddedModules.

        2.   [Fetch a worklet script graph](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-worklet-script-graph) given moduleURL, insideSettings, worklet's [worklet destination type](https://html.spec.whatwg.org/multipage/worklets.html#worklet-destination-type), what credentials mode?, insideSettings, worklet's [module responses map](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-module-responses-map), and with the following steps given script:

This will not actually perform a network request, as it will just reuse [responses](https://fetch.spec.whatwg.org/#concept-response) from worklet's [module responses map](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-module-responses-map). The main purpose of this step is to create a new workletGlobalScope-specific [module script](https://html.spec.whatwg.org/multipage/webappapis.html#module-script) from the [response](https://fetch.spec.whatwg.org/#concept-response).

            1.   [Assert](https://infra.spec.whatwg.org/#assert): script is not null, since the fetch succeeded and the source text was successfully parsed when worklet's [module responses map](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-module-responses-map) was initially populated with moduleURL.

            2.   [Run a module script](https://html.spec.whatwg.org/multipage/webappapis.html#run-a-module-script) given script.

            3.   Run runNextAddedModule.

        3.   Abort these steps.

    2.   [Append](https://infra.spec.whatwg.org/#list-append)workletGlobalScope to outsideSettings's [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-global)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [worklet global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-document-worklet-global-scopes).

    3.   [Append](https://infra.spec.whatwg.org/#list-append)workletGlobalScope to worklet's [global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-global-scopes).

    4.   Run the [responsible event loop](https://html.spec.whatwg.org/multipage/webappapis.html#responsible-event-loop) specified by insideSettings.

8.   Run runNextAddedModule.

##### 11.3.1.3 Script settings for worklets[](https://html.spec.whatwg.org/multipage/worklets.html#script-settings-for-worklets)

To set up a worklet environment settings object, given a [JavaScript execution context](https://tc39.es/ecma262/#sec-execution-contexts)executionContext and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)outsideSettings:

1.   Let origin be a unique [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque).

2.   Let inheritedAPIBaseURL be outsideSettings's [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

3.   Let inheritedPolicyContainer be a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of outsideSettings's [policy container](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-policy-container).

4.   Let realm be the value of executionContext's Realm component.

5.   Let workletGlobalScope be realm's [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global).

6.   Let settingsObject be a new [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object) whose algorithms are defined as follows:

The [realm execution context](https://html.spec.whatwg.org/multipage/webappapis.html#realm-execution-context)
Return executionContext.

The [module map](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-module-map)
Return workletGlobalScope's [module map](https://html.spec.whatwg.org/multipage/worklets.html#concept-workletglobalscope-module-map).

The [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url)
Return inheritedAPIBaseURL.

Unlike workers or other globals derived from a single resource, worklets have no primary resource; instead, multiple scripts, each with their own URL, are loaded into the global scope via `worklet.addModule()`. So this [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url) is rather unlike that of other globals. However, so far this doesn't matter, as no APIs available to worklet code make use of the [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

The [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin)
Return origin.

The [has cross-site ancestor](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-has-cross-site-ancestor)
Return true.

The [policy container](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-policy-container)
Return inheritedPolicyContainer.

The [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability)
Return TODO.

The [time origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-time-origin)
[Assert](https://infra.spec.whatwg.org/#assert): this algorithm is never called, because the [time origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-time-origin) is not available in a worklet context.

7.   Set settingsObject's [id](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-id) to a new unique opaque string, [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url) to inheritedAPIBaseURL, [top-level creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-creation-url) to null, [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin) to outsideSettings's [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin), [target browsing context](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-target-browsing-context) to null, and [active service worker](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-active-service-worker) to null.

8.   Set realm's [[HostDefined]] field to settingsObject.

9.   Return settingsObject.

#### 11.3.2 The `Worklet` class[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-worklet)

[Worklet](https://developer.mozilla.org/en-US/docs/Web/API/Worklet "The Worklet interface is a lightweight version of Web Workers and gives developers access to low-level parts of the rendering pipeline.")

Support in all current engines.

Firefox 76+Safari 14.1+Chrome 65+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `Worklet` class provides the capability to add module scripts into its associated `WorkletGlobalScope`s. The user agent can then create classes registered on the `WorkletGlobalScope`s and invoke their methods.

```
[Exposed=Window, SecureContext]
interface Worklet {
  [NewObject] Promise<undefined> addModule(USVString moduleURL, optional WorkletOptions options = {});
};

dictionary WorkletOptions {
  RequestCredentials credentials = "same-origin";
};
```

Specifications that create `Worklet` instances must specify the following for a given instance:

*   its worklet global scope type, which must be a Web IDL type that [inherits](https://webidl.spec.whatwg.org/#dfn-inherit) from `WorkletGlobalScope`; and

*   its worklet destination type, which must be a [destination](https://fetch.spec.whatwg.org/#concept-request-destination), and is used when fetching scripts.

`await worklet.addModule(moduleURL[, { credentials }])`

[Worklet/addModule](https://developer.mozilla.org/en-US/docs/Web/API/Worklet/addModule "The addModule() method of the Worklet interface loads the module in the given JavaScript file and adds it to the current Worklet.")

Support in all current engines.

Firefox 76+Safari 14.1+Chrome 65+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Loads and executes the [module script](https://html.spec.whatwg.org/multipage/webappapis.html#module-script) given by moduleURL into all of worklet's [global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-global-scopes). It can also create additional global scopes as part of this process, depending on the worklet type. The returned promise will fulfill once the script has been successfully loaded and run in all global scopes.

The `credentials` option can be set to a [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode) to modify the script-fetching process. It defaults to "`same-origin`".

Any failures in [fetching](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-worklet-script-graph) the script or its dependencies will cause the returned promise to be rejected with an ["`AbortError`"](https://webidl.spec.whatwg.org/#aborterror)`DOMException`. Any errors in parsing the script or its dependencies will cause the returned promise to be rejected with the exception generated during parsing.

A `Worklet` has a [list](https://infra.spec.whatwg.org/#list) of global scopes, which contains instances of the `Worklet`'s [worklet global scope type](https://html.spec.whatwg.org/multipage/worklets.html#worklet-global-scope-type). It is initially empty.

A `Worklet` has an added modules list, which is a [list](https://infra.spec.whatwg.org/#list) of [URLs](https://url.spec.whatwg.org/#concept-url), initially empty. Access to this list should be thread-safe.

A `Worklet` has a module responses map, which is an [ordered map](https://infra.spec.whatwg.org/#ordered-map) from [URLs](https://url.spec.whatwg.org/#concept-url) to either "`fetching`" or [tuples](https://infra.spec.whatwg.org/#tuple) consisting of a [response](https://fetch.spec.whatwg.org/#concept-response) and either null, failure, or a [byte sequence](https://infra.spec.whatwg.org/#byte-sequence) representing the response body. This map is initially empty, and access to it should be thread-safe.

The [added modules list](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-added-modules-list) and [module responses map](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-module-responses-map) exist to ensure that `WorkletGlobalScope`s created at different times get equivalent [module scripts](https://html.spec.whatwg.org/multipage/webappapis.html#module-script) run in them, based on the same source text. This allows the creation of additional `WorkletGlobalScope`s to be transparent to the author.

In practice, user agents are not expected to implement these data structures, and the algorithms that consult them, using thread-safe programming techniques. Instead, when `addModule()` is called, user agents can fetch the module graph on the main thread, and send the fetched source text (i.e., the important data contained in the [module responses map](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-module-responses-map)) to each thread which has a `WorkletGlobalScope`.

Then, when a user agent [creates](https://html.spec.whatwg.org/multipage/worklets.html#create-a-worklet-global-scope) a new `WorkletGlobalScope` for a given `Worklet`, it can simply send the map of fetched source text and the list of entry points from the main thread to the thread containing the new `WorkletGlobalScope`.

The 
```
addModule(moduleURL,
  options)
```
 method steps are:

1.   Let outsideSettings be the [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object) of [this](https://webidl.spec.whatwg.org/#this).

2.   Let moduleURLRecord be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given moduleURL, relative to outsideSettings.

3.   If moduleURLRecord is failure, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

4.   Let promise be a new promise.

5.   Let workletInstance be [this](https://webidl.spec.whatwg.org/#this).

6.   Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

    1.   If workletInstance's [global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-global-scopes)[is empty](https://infra.spec.whatwg.org/#list-is-empty), then:

        1.   [Create a worklet global scope](https://html.spec.whatwg.org/multipage/worklets.html#create-a-worklet-global-scope) given workletInstance.

        2.   Optionally, [create](https://html.spec.whatwg.org/multipage/worklets.html#create-a-worklet-global-scope) additional global scope instances given workletInstance, depending on the specific worklet in question and its specification.

        3.   Wait for all steps of the [creation](https://html.spec.whatwg.org/multipage/worklets.html#create-a-worklet-global-scope) process(es) — including those taking place within the [worklet agents](https://html.spec.whatwg.org/multipage/webappapis.html#worklet-agent) — to complete, before moving on.

    2.   Let pendingTasks be workletInstance's [global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-global-scopes)'s [size](https://infra.spec.whatwg.org/#list-size).

    3.   Let addedSuccessfully be false.

    4.   [For each](https://infra.spec.whatwg.org/#list-iterate)workletGlobalScope of workletInstance's [global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-global-scopes), [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) given workletGlobalScope to [fetch a worklet script graph](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-worklet-script-graph) given moduleURLRecord, outsideSettings, workletInstance's [worklet destination type](https://html.spec.whatwg.org/multipage/worklets.html#worklet-destination-type), options["`credentials`"], workletGlobalScope's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object), workletInstance's [module responses map](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-module-responses-map), and the following steps given script:

Only the first of these fetches will actually perform a network request; the ones for other `WorkletGlobalScope`s will reuse [responses](https://fetch.spec.whatwg.org/#concept-response) from workletInstance's [module responses map](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-module-responses-map).

        1.   If script is null, then:

            1.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) given workletInstance's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform the following steps:

                1.   If pendingTasks is not −1, then:

                    1.   Set pendingTasks to −1.

                    2.   Reject promise with an ["`AbortError`"](https://webidl.spec.whatwg.org/#aborterror)`DOMException`.

            2.   Abort these steps.

        2.   If script's [error to rethrow](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-error-to-rethrow) is not null, then:

            1.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) given workletInstance's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform the following steps:

                1.   If pendingTasks is not −1, then:

                    1.   Set pendingTasks to −1.

                    2.   Reject promise with script's [error to rethrow](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-error-to-rethrow).

            2.   Abort these steps.

        3.   If addedSuccessfully is false, then:

            1.   [Append](https://infra.spec.whatwg.org/#list-append)moduleURLRecord to workletInstance's [added modules list](https://html.spec.whatwg.org/multipage/worklets.html#concept-worklet-added-modules-list).

            2.   Set addedSuccessfully to true.

        4.   [Run a module script](https://html.spec.whatwg.org/multipage/webappapis.html#run-a-module-script) given script.

        5.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) given workletInstance's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform the following steps:

            1.   If pendingTasks is not −1, then:

                1.   Set pendingTasks to pendingTasks − 1.

                2.   If pendingTasks is 0, then resolve promise.

7.   Return promise.

#### 11.3.3 The worklet's lifetime[](https://html.spec.whatwg.org/multipage/worklets.html#worklets-lifetime)

The lifetime of a `Worklet` has no special considerations; it is tied to the object it belongs to, such as the `Window`.

Each `Document` has a worklet global scopes, which is a [set](https://infra.spec.whatwg.org/#ordered-set) of `WorkletGlobalScope`s, initially empty.

The lifetime of a `WorkletGlobalScope` is, at a minimum, tied to the `Document` whose [worklet global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-document-worklet-global-scopes) contain it. In particular, [destroying](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document) the `Document` will [terminate](https://html.spec.whatwg.org/multipage/worklets.html#terminate-a-worklet-global-scope) the corresponding `WorkletGlobalScope` and allow it to be garbage-collected.

Additionally, user agents may, at any time, [terminate](https://html.spec.whatwg.org/multipage/worklets.html#terminate-a-worklet-global-scope) a given `WorkletGlobalScope`, unless the specification defining the corresponding worklet type says otherwise. For example, they might terminate them if the [worklet agent](https://html.spec.whatwg.org/multipage/webappapis.html#worklet-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop) has no [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) queued, or if the user agent has no pending operations planning to make use of the worklet, or if the user agent detects abnormal operations such as infinite loops or callbacks exceeding imposed time limits.

Finally, specifications for specific worklet types can give more specific details on when to [create](https://html.spec.whatwg.org/multipage/worklets.html#create-a-worklet-global-scope)`WorkletGlobalScope`s for a given worklet type. For example, they might create them during specific processes that call upon worklet code, as in the [example](https://html.spec.whatwg.org/multipage/worklets.html#worklets-example-registering).

[← 10 Web workers](https://html.spec.whatwg.org/multipage/workers.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [12 Web storage →](https://html.spec.whatwg.org/multipage/webstorage.html)
