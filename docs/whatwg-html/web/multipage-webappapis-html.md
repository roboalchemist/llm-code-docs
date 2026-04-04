# Source: https://html.spec.whatwg.org/multipage/webappapis.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/webappapis.html

Markdown Content:
HTML

Living Standard — Last Updated 16 March 2026

← 7.6 Speculative loading — Table of Contents — 8.4 Dynamic markup insertion →
8 Web application APIs
8.1 Scripting
8.1.1 Introduction
8.1.2 Agents and agent clusters
8.1.2.1 Integration with the JavaScript agent formalism
8.1.2.2 Integration with the JavaScript agent cluster formalism
8.1.3 Realms and their counterparts
8.1.3.1 Environments
8.1.3.2 Environment settings objects
8.1.3.3 Realms, settings objects, and global objects
8.1.3.3.1 Entry
8.1.3.3.2 Incumbent
8.1.3.3.3 Current
8.1.3.3.4 Relevant
8.1.3.4 Enabling and disabling scripting
8.1.3.5 Secure contexts
8.1.4 Script processing model
8.1.4.1 Scripts
8.1.4.2 Fetching scripts
8.1.4.3 Creating scripts
8.1.4.4 Calling scripts
8.1.4.5 Killing scripts
8.1.4.6 Runtime script errors
8.1.4.7 Unhandled promise rejections
8.1.4.8 Import map parse results
8.1.4.9 Speculation rules parse results
8.1.5 Module specifier resolution
8.1.5.1 The resolution algorithm
8.1.5.2 Import maps
8.1.5.3 Import map processing model
8.1.6 JavaScript specification host hooks
8.1.6.1 HostEnsureCanAddPrivateElement(O)
8.1.6.2 HostEnsureCanCompileStrings(realm, parameterStrings, bodyString, codeString, compilationType, parameterArgs, bodyArg)
8.1.6.3 HostGetCodeForEval(argument)
8.1.6.4 HostPromiseRejectionTracker(promise, operation)
8.1.6.5 HostSystemUTCEpochNanoseconds(global)
8.1.6.6 Job-related host hooks
8.1.6.6.1 HostCallJobCallback(callback, V, argumentsList)
8.1.6.6.2 HostEnqueueFinalizationRegistryCleanupJob(finalizationRegistry)
8.1.6.6.3 HostEnqueueGenericJob(job, realm)
8.1.6.6.4 HostEnqueuePromiseJob(job, realm)
8.1.6.6.5 HostEnqueueTimeoutJob(job, realm, milliseconds)
8.1.6.6.6 HostMakeJobCallback(callable)
8.1.6.7 Module-related host hooks
8.1.6.7.1 HostGetImportMetaProperties(moduleRecord)
8.1.6.7.2 HostGetSupportedImportAttributes()
8.1.6.7.3 HostLoadImportedModule(referrer, moduleRequest, loadState, payload)
8.1.7 Event loops
8.1.7.1 Definitions
8.1.7.2 Queuing tasks
8.1.7.3 Processing model
8.1.7.4 Generic task sources
8.1.7.5 Dealing with the event loop from other specifications
8.1.8 Events
8.1.8.1 Event handlers
8.1.8.2 Event handlers on elements, Document objects, and Window objects
8.1.8.2.1 IDL definitions
8.1.8.3 Event firing
8.2 The WindowOrWorkerGlobalScope mixin
8.3 Base64 utility methods
8 Web application APIs
8.1 Scripting
8.1.1 Introduction

Various mechanisms can cause author-provided executable code to run in the context of a document. These mechanisms include, but are probably not limited to:

Processing of script elements.
Navigating to javascript: URLs.
Event handlers, whether registered through the DOM using addEventListener(), by explicit event handler content attributes, by event handler IDL attributes, or otherwise.
Processing of technologies like SVG that have their own scripting features.
8.1.2 Agents and agent clusters
8.1.2.1 Integration with the JavaScript agent formalism

JavaScript defines the concept of an agent. This section gives the mapping of that language-level concept on to the web platform.

Conceptually, the agent concept is an architecture-independent, idealized "thread" in which JavaScript code runs. Such code can involve multiple globals/realms that can synchronously access each other, and thus needs to run in a single execution thread.

Two Window objects having the same agent does not indicate they can directly access all objects created in each other's realms. They would have to be same origin-domain; see IsPlatformObjectSameOrigin.

The following types of agents exist on the web platform:

Similar-origin window agent

Contains various Window objects which can potentially reach each other, either directly or by using document.domain.

If the encompassing agent cluster's is origin-keyed is true, then all the Window objects will be same origin, can reach each other directly, and document.domain will no-op.

Two Window objects that are same origin can be in different similar-origin window agents, for instance if they are each in their own browsing context group.

Dedicated worker agent

Contains a single DedicatedWorkerGlobalScope.

Shared worker agent

Contains a single SharedWorkerGlobalScope.

Service worker agent

Contains a single ServiceWorkerGlobalScope.

Worklet agent

Contains a single WorkletGlobalScope object.

Although a given worklet can have multiple realms, each such realm needs its own agent, as each realm can be executing code independently and at the same time as the others.

Only shared and dedicated worker agents allow the use of JavaScript Atomics APIs to potentially block.

To create an agent, given a boolean canBlock:

Let signifier be a new unique internal value.

Let candidateExecution be a new candidate execution.

Let agent be a new agent whose [[CanBlock]] is canBlock, [[Signifier]] is signifier, [[CandidateExecution]] is candidateExecution, and [[IsLockFree1]], [[IsLockFree2]], and [[LittleEndian]] are set at the implementation's discretion.

Set agent's event loop to a new event loop.

Return agent.

For a realm realm, the agent whose [[Signifier]] is realm.[[AgentSignifier]] is the realm's agent.

The relevant agent for a platform object platformObject is platformObject's relevant realm's agent.

The agent equivalent of the current realm is the surrounding agent.

8.1.2.2 Integration with the JavaScript agent cluster formalism

JavaScript also defines the concept of an agent cluster, which this standard maps to the web platform by placing agents appropriately when they are created using the obtain a similar-origin window agent or obtain a worker/worklet agent algorithms.

The agent cluster concept is crucial for defining the JavaScript memory model, and in particular among which agents the backing data of SharedArrayBuffer objects can be shared.

Conceptually, the agent cluster concept is an architecture-independent, idealized "process boundary" that groups together multiple "threads" (agents). The agent clusters defined by the specification are generally more restrictive than the actual process boundaries implemented in user agents. By enforcing these idealized divisions at the specification level, we ensure that web developers see interoperable behavior with regard to shared memory, even in the face of varying and changing user agent process models.

An agent cluster has an associated cross-origin isolation mode, which is a cross-origin isolation mode. It is initially "none".

An agent cluster has an associated is origin-keyed (a boolean), which is initially false.

The following defines the allocation of the agent clusters of similar-origin window agents.

An agent cluster key is a site or tuple origin. Without web developer action to achieve origin-keyed agent clusters, it will be a site.

An equivalent formulation is that an agent cluster key can be a scheme-and-host or an origin.

To obtain a similar-origin window agent, given an origin origin, a browsing context group group, and a boolean requestsOAC, run these steps:

Let site be the result of obtaining a site with origin.

Let key be site.

If group's cross-origin isolation mode is not "none", then set key to origin.

Otherwise, if group's historical agent cluster key map[origin] exists, then set key to group's historical agent cluster key map[origin].

Otherwise:

If requestsOAC is true, then set key to origin.

Set group's historical agent cluster key map[origin] to key.

If group's agent cluster map[key] does not exist, then:

Let agentCluster be a new agent cluster.

Set agentCluster's cross-origin isolation mode to group's cross-origin isolation mode.

If key is an origin:

Assert: key is origin.

Set agentCluster's is origin-keyed to true.

Add the result of creating an agent, given false, to agentCluster.

Set group's agent cluster map[key] to agentCluster.

Return the single similar-origin window agent contained in group's agent cluster map[key].

This means that there is only one similar-origin window agent per browsing context agent cluster. (However, dedicated worker and worklet agents might be in the same cluster.)

The following defines the allocation of the agent clusters of all other types of agents.

To obtain a worker/worklet agent, given an environment settings object or null outside settings, a boolean isTopLevel, and a boolean canBlock, run these steps:

Let agentCluster be null.

If isTopLevel is true, then:

Set agentCluster to a new agent cluster.

Set agentCluster's is origin-keyed to true.

These workers can be considered to be origin-keyed. However, this is not exposed through any APIs (in the way that originAgentCluster exposes the origin-keyedness for windows).

Otherwise:

Assert: outside settings is not null.

Let ownerAgent be outside settings's realm's agent.

Set agentCluster to the agent cluster which contains ownerAgent.

Let agent be the result of creating an agent given canBlock.

Add agent to agentCluster.

Return agent.

To obtain a dedicated/shared worker agent, given an environment settings object outside settings and a boolean isShared, return the result of obtaining a worker/worklet agent given outside settings, isShared, and true.

To obtain a worklet agent, given an environment settings object outside settings, return the result of obtaining a worker/worklet agent given outside settings, false, and false.

To obtain a service worker agent, return the result of obtaining a worker/worklet agent given null, true, and false.

The following pairs of global objects are each within the same agent cluster, and thus can use SharedArrayBuffer instances to share memory with each other:

A Window object and a dedicated worker that it created.

A worker (of any type) and a dedicated worker it created.

A Window object A and the Window object of an iframe element that A created that could be same origin-domain with A.

A Window object and a same origin-domain Window object that opened it.

A Window object and a worklet that it created.

The following pairs of global objects are not within the same agent cluster, and thus cannot share memory:

A Window object and a shared worker it created.

A worker (of any type) and a shared worker it created.

A Window object and a service worker it created.

A Window object A and the Window object of an iframe element that A created that cannot be same origin-domain with A.

Any two Window objects with no opener or ancestor relationship. This holds even if the two Window objects are same origin.

8.1.3 Realms and their counterparts

The JavaScript specification introduces the realm concept, representing a global environment in which script is run. Each realm comes with an implementation-defined global object; much of this specification is devoted to defining that global object and its properties.

For web specifications, it is often useful to associate values or algorithms with a realm/global object pair. When the values are specific to a particular type of realm, they are associated directly with the global object in question, e.g., in the definition of the Window or WorkerGlobalScope interfaces. When the values have utility across multiple realms, we use the environment settings object concept.

Finally, in some cases it is necessary to track associated values before a realm/global object/environment settings object even comes into existence (for example, during navigation). These values are tracked in the environment concept.

8.1.3.1 Environments

An environment is an object that identifies the settings of a current or potential execution environment (i.e., a navigation params's reserved environment or a request's reserved client). An environment has the following fields:

An id

An opaque string that uniquely identifies this environment.

A creation URL

A URL that represents the location of the resource with which this environment is associated.

In the case of a Window environment settings object, this URL might be distinct from its global object's associated Document's URL, due to mechanisms such as history.pushState() which modify the latter.

A top-level creation URL

Null or a URL that represents the creation URL of the "top-level" environment. It is null for workers and worklets.

A top-level origin

A for now implementation-defined value, null, or an origin. For a "top-level" potential execution environment it is null (i.e., when there is no response yet); otherwise it is the "top-level" environment's origin. For a dedicated worker or worklet it is the top-level origin of its creator. For a shared or service worker it is an implementation-defined value.

This is distinct from the top-level creation URL's origin when sandboxing, workers, and worklets are involved.

A target browsing context

Null or a target browsing context for a navigation request.

An active service worker

Null or a service worker that controls the environment.

An execution ready flag

A flag that indicates whether the environment setup is done. It is initially unset.

Specifications may define environment discarding steps for environments. The steps take an environment as input.

The environment discarding steps are run for only a select few environments: the ones that will never become execution ready because, for example, they failed to load.

8.1.3.2 Environment settings objects

An environment settings object is an environment that additionally specifies algorithms for:

A realm execution context

A JavaScript execution context shared by all scripts that use this settings object, i.e., all scripts in a given realm. When we run a classic script or run a module script, this execution context becomes the top of the JavaScript execution context stack, on top of which another execution context specific to the script in question is pushed. (This setup ensures Source Text Module Record's Evaluate knows which realm to use.)

A module map

A module map that is used when importing JavaScript modules.

An API base URL

A URL used by APIs called by scripts that use this environment settings object to parse URLs.

An origin

An origin used in security checks.

A has cross-site ancestor

A boolean used in security checks.

A policy container

A policy container containing policies used for security checks.

A cross-origin isolated capability

A boolean representing whether scripts that use this environment settings object are allowed to use APIs that require cross-origin isolation.

A time origin
A number used as the baseline for performance-related timestamps. [HRT]

An environment settings object's responsible event loop is its global object's relevant agent's event loop.

8.1.3.3 Realms, settings objects, and global objects

A global object is a JavaScript object that is the [[GlobalObject]] field of a realm.

In this specification, all realms are created with global objects that are either Window, WorkerGlobalScope, or WorkletGlobalScope objects.

A global object has an in error reporting mode boolean, which is initially false.

A global object has an outstanding rejected promises weak set, a set of Promise objects, initially empty. This set must not create strong references to any of its members, and implementations are free to limit its size in an implementation-defined manner, e.g., by removing old entries from it when new ones are added.

A global object has an about-to-be-notified rejected promises list, a list of Promise objects, initially empty.

A global object has an import map, initially an empty import map.

For now, only Window global objects have their import map modified from the initial empty one. The import map is only accessed for the resolution of a root module script.

A global object has a resolved module set, a set of specifier resolution records, initially empty.

The resolved module set ensures that module specifier resolution returns the same result when called multiple times with the same (referrer, specifier) pair. It does that by ensuring that import map rules that impact the specifier in its referrer's scope cannot be defined after its initial resolution. For now, only Window global objects have their module set data structures modified from the initial empty one.

There is always a 1-to-1-to-1 mapping between realms, global objects, and environment settings objects:

A realm has a [[HostDefined]] field, which contains the realm's settings object.

A realm has a [[GlobalObject]] field, which contains the realm's global object.

Each global object in this specification is created during the creation of a corresponding realm, known as the global object's realm.

Each global object in this specification is created alongside a corresponding environment settings object, known as its relevant settings object.

An environment settings object's realm execution context's Realm component is the environment settings object's realm.

An environment settings object's realm then has a [[GlobalObject]] field, which contains the environment settings object's global object.

To create a new realm in an agent agent, optionally with instructions to create a global object or a global this binding (or both), the following steps are taken:

Perform InitializeHostDefinedRealm() with the provided customizations for creating the global object and the global this binding.

Let realm execution context be the running JavaScript execution context.

This is the JavaScript execution context created in the previous step.

Remove realm execution context from the JavaScript execution context stack.

Let realm be realm execution context's Realm component.

If agent's agent cluster's cross-origin isolation mode is "none", then:

Let global be realm's global object.

Let status be ! global.[[Delete]]("SharedArrayBuffer").

Assert: status is true.

This is done for compatibility with web content and there is some hope that this can be removed in the future. Web developers can still get at the constructor through new WebAssembly.Memory({ shared:true, initial:0, maximum:0 }).buffer.constructor.

Return realm execution context.

When defining algorithm steps throughout this specification, it is often important to indicate what realm is to be used—or, equivalently, what global object or environment settings object is to be used. In general, there are at least four possibilities:

Entry
This corresponds to the script that initiated the currently running script action: i.e., the function or script that the user agent called into when it called into author code.
Incumbent
This corresponds to the most-recently-entered author function or script on the stack, or the author function or script that originally scheduled the currently-running callback.
Current
This corresponds to the currently-running function object, including built-in user-agent functions which might not be implemented as JavaScript. (It is derived from the current realm.)
Relevant
Every platform object has a relevant realm, which is roughly the realm in which it was created. When writing algorithms, the most prominent platform object whose relevant realm might be important is the this value of the currently-running function object. In some cases, there can be other important relevant realms, such as those of any arguments.

Note how the entry, incumbent, and current concepts are usable without qualification, whereas the relevant concept must be applied to a particular platform object.

The incumbent and entry concepts should not be used by new specifications, as they are excessively complicated and unintuitive to work with. We are working to remove almost all existing uses from the platform: see issue #1430 for incumbent, and issue #1431 for entry.

In general, web platform specifications should use the relevant concept, applied to the object being operated on (usually the this value of the current method). This mismatches the JavaScript specification, where current is generally used as the default (e.g., in determining the realm whose Array constructor should be used to construct the result in Array.prototype.map). But this inconsistency is so embedded in the platform that we have to accept it going forward.

Consider the following pages, with a.html being loaded in a browser window, b.html being loaded in an iframe as shown, and c.html and d.html omitted (they can simply be empty documents):

<!-- a.html -->
<!DOCTYPE html>
<html lang="en">
<title>Entry page</title>

<iframe src="b.html"></iframe>
<button onclick="frames[0].hello()">Hello</button>

<!--b.html -->
<!DOCTYPE html>
<html lang="en">
<title>Incumbent page</title>

<iframe src="c.html" id="c"></iframe>
<iframe src="d.html" id="d"></iframe>

<script>
  const c = document.querySelector("#c").contentWindow;
  const d = document.querySelector("#d").contentWindow;

  window.hello = () => {
    c.print.call(d);
  };
</script>

Each page has its own browsing context, and thus its own realm, global object, and environment settings object.

When the print() method is called in response to pressing the button in a.html, then:

The entry realm is that of a.html.

The incumbent realm is that of b.html.

The current realm is that of c.html (since it is the print() method from c.html whose code is running).

The relevant realm of the object on which the print() method is being called is that of d.html.

One reason why the relevant concept is generally a better default choice than the current concept is that it is more suitable for creating an object that is to be persisted and returned multiple times. For example, the navigator.getBattery() method creates promises in the relevant realm for the Navigator object on which it is invoked. This has the following impact: [BATTERY]

<!-- outer.html -->
<!DOCTYPE html>
<html lang="en">
<title>Relevant realm demo: outer page</title>
<script>
  function doTest() {
    const promise = navigator.getBattery.call(frames[0].navigator);

    console.log(promise instanceof Promise);           // logs false
    console.log(promise instanceof frames[0].Promise); // logs true

    frames[0].hello();
  }
</script>
<iframe src="inner.html" onload="doTest()"></iframe>

<!-- inner.html -->
<!DOCTYPE html>
<html lang="en">
<title>Relevant realm demo: inner page</title>
<script>
  function hello() {
    const promise = navigator.getBattery();

    console.log(promise instanceof Promise);        // logs true
    console.log(promise instanceof parent.Promise); // logs false
  }
</script>

If the algorithm for the getBattery() method had instead used the current realm, all the results would be reversed. That is, after the first call to getBattery() in outer.html, the Navigator object in inner.html would be permanently storing a Promise object created in outer.html's realm, and calls like that inside the hello() function would thus return a promise from the "wrong" realm. Since this is undesirable, the algorithm instead uses the relevant realm, giving the sensible results indicated in the comments above.

The rest of this section deals with formally defining the entry, incumbent, current, and relevant concepts.

8.1.3.3.1 Entry

The process of calling scripts will push or pop realm execution contexts onto the JavaScript execution context stack, interspersed with other execution contexts.

With this in hand, we define the entry execution context to be the most recently pushed item in the JavaScript execution context stack that is a realm execution context. The entry realm is the entry execution context's Realm component.

Then, the entry settings object is the environment settings object of the entry realm.

Similarly, the entry global object is the global object of the entry realm.

8.1.3.3.2 Incumbent

All JavaScript execution contexts must contain, as part of their code evaluation state, a skip-when-determining-incumbent counter value, which is initially zero. In the process of preparing to run a callback and cleaning up after running a callback, this value will be incremented and decremented.

Every event loop has an associated backup incumbent settings object stack, initially empty. Roughly speaking, it is used to determine the incumbent settings object when no author code is on the stack, but author code is responsible for the current algorithm having been run in some way. The process of preparing to run a callback and cleaning up after running a callback manipulate this stack. [WEBIDL]

When Web IDL is used to invoke author code, or when HostEnqueuePromiseJob invokes a promise job, they use the following algorithms to track relevant data for determining the incumbent settings object:

To prepare to run a callback with an environment settings object settings:

Push settings onto the backup incumbent settings object stack.

Let context be the topmost script-having execution context.

If context is not null, increment context's skip-when-determining-incumbent counter.

To clean up after running a callback with an environment settings object settings:

Let context be the topmost script-having execution context.

This will be the same as the topmost script-having execution context inside the corresponding invocation of prepare to run a callback.

If context is not null, decrement context's skip-when-determining-incumbent counter.

Assert: the topmost entry of the backup incumbent settings object stack is settings.

Remove settings from the backup incumbent settings object stack.

Here, the topmost script-having execution context is the topmost entry of the JavaScript execution context stack that has a non-null ScriptOrModule component, or null if there is no such entry in the JavaScript execution context stack.

With all this in place, the incumbent settings object is determined as follows:

Let context be the topmost script-having execution context.

If context is null, or if context's skip-when-determining-incumbent counter is greater than zero, then:

Assert: the backup incumbent settings object stack is not empty.

This assert would fail if you try to obtain the incumbent settings object from inside an algorithm that was triggered neither by calling scripts nor by Web IDL invoking a callback. For example, it would trigger if you tried to obtain the incumbent settings object inside an algorithm that ran periodically as part of the event loop, with no involvement of author code. In such cases the incumbent concept cannot be used.

Return the topmost entry of the backup incumbent settings object stack.

Return context's Realm component's settings object.

Then, the incumbent realm is the realm of the incumbent settings object.

Similarly, the incumbent global object is the global object of the incumbent settings object.

The following series of examples is intended to make it clear how all of the different mechanisms contribute to the definition of the incumbent concept:

Consider the following starter example:

<!DOCTYPE html>
<iframe></iframe>
<script>
  frames[0].postMessage("some data", "*");
</script>

There are two interesting environment settings objects here: that of window, and that of frames[0]. Our concern is: what is the incumbent settings object at the time that the algorithm for postMessage() executes?

It should be that of window, to capture the intuitive notion that the author script responsible for causing the algorithm to happen is executing in window, not frames[0]. This makes sense: the window post message steps use the incumbent settings object to determine the source property of the resulting MessageEvent, and in this case window is definitely the source of the message.

Let us now explain how the steps given above give us our intuitively-desired result of window's relevant settings object.

When the window post message steps look up the incumbent settings object, the topmost script-having execution context will be that corresponding to the script element: it was pushed onto the JavaScript execution context stack as part of ScriptEvaluation during the run a classic script algorithm. Since there are no Web IDL callback invocations involved, the context's skip-when-determining-incumbent counter is zero, so it is used to determine the incumbent settings object; the result is the environment settings object of window.

(Note how the environment settings object of frames[0] is the relevant settings object of this at the time the postMessage() method is called, and thus is involved in determining the target of the message. Whereas the incumbent is used to determine the source.)

Consider the following more complicated example:

<!DOCTYPE html>
<iframe></iframe>
<script>
  const bound = frames[0].postMessage.bind(frames[0], "some data", "*");
  window.setTimeout(bound);
</script>

This example is very similar to the previous one, but with an extra indirection through Function.prototype.bind as well as setTimeout(). But, the answer should be the same: invoking algorithms asynchronously should not change the incumbent concept.

This time, the result involves more complicated mechanisms:

When bound is converted to a Web IDL callback type, the incumbent settings object is that corresponding to window (in the same manner as in our starter example above). Web IDL stores this as the resulting callback value's callback context.

When the task posted by setTimeout() executes, the algorithm for that task uses Web IDL to invoke the stored callback value. Web IDL in turn calls the above prepare to run a callback algorithm. This pushes the stored callback context onto the backup incumbent settings object stack. At this time (inside the timer task) there is no author code on the stack, so the topmost script-having execution context is null, and nothing gets its skip-when-determining-incumbent counter incremented.

Invoking the callback then calls bound, which in turn calls the postMessage() method of frames[0]. When the postMessage() algorithm looks up the incumbent settings object, there is still no author code on the stack, since the bound function just directly calls the built-in method. So the topmost script-having execution context will be null: the JavaScript execution context stack only contains an execution context corresponding to postMessage(), with no ScriptEvaluation context or similar below it.

This is where we fall back to the backup incumbent settings object stack. As noted above, it will contain as its topmost entry the relevant settings object of window. So that is what is used as the incumbent settings object while executing the postMessage() algorithm.

Consider this final, even more convoluted example:

<!-- a.html -->
<!DOCTYPE html>
<button>click me</button>
<iframe></iframe>
<script>
const bound = frames[0].location.assign.bind(frames[0].location, "https://example.com/");
document.querySelector("button").addEventListener("click", bound);
</script>
<!-- b.html -->
<!DOCTYPE html>
<iframe src="a.html"></iframe>
<script>
  const iframe = document.querySelector("iframe");
  iframe.onload = function onLoad() {
    iframe.contentWindow.document.querySelector("button").click();
  };
</script>

Again there are two interesting environment settings objects in play: that of a.html, and that of b.html. When the location.assign() method triggers the Location-object navigate algorithm, what will be the incumbent settings object? As before, it should intuitively be that of a.html: the click listener was originally scheduled by a.html, so even if something involving b.html causes the listener to fire, the incumbent responsible is that of a.html.

The callback setup is similar to the previous example: when bound is converted to a Web IDL callback type, the incumbent settings object is that corresponding to a.html, which is stored as the callback's callback context.

When the click() method is called inside b.html, it dispatches a click event on the button that is inside a.html. This time, when the prepare to run a callback algorithm executes as part of event dispatch, there is author code on the stack; the topmost script-having execution context is that of the onLoad function, whose skip-when-determining-incumbent counter gets incremented. Additionally, a.html's environment settings object (stored as the EventHandler's callback context) is pushed onto the backup incumbent settings object stack.

Now, when the Location-object navigate algorithm looks up the incumbent settings object, the topmost script-having execution context is still that of the onLoad function (due to the fact we are using a bound function as the callback). Its skip-when-determining-incumbent counter value is one, however, so we fall back to the backup incumbent settings object stack. This gives us the environment settings object of a.html, as expected.

Note that this means that even though it is the iframe inside a.html that navigates, it is a.html itself that is used as the source Document, which determines among other things the request client. This is perhaps the only justifiable use of the incumbent concept on the web platform; in all other cases the consequences of using it are simply confusing and we hope to one day switch them to use current or relevant as appropriate.

8.1.3.3.3 Current

The JavaScript specification defines the current realm, also known as the "current Realm Record". [JAVASCRIPT]

Then, the current settings object is the environment settings object of the current realm.

Similarly, the current global object is the global object of the current realm.

8.1.3.3.4 Relevant

The relevant realm for a platform object is the value of its [[Realm]] field.

Then, the relevant settings object for a platform object o is the environment settings object of the relevant realm for o.

Similarly, the relevant global object for a platform object o is the global object of the relevant realm for o.

8.1.3.4 Enabling and disabling scripting

Scripting is enabled for an environment settings object settings when all of the following conditions are true:

The user agent supports scripting.
The user has not disabled scripting for settings at this time. (User agents may provide users with the option to disable scripting globally, or in a finer-grained manner, e.g., on a per-origin basis, down to the level of individual environment settings objects.)
Either settings's global object is not a Window object, or settings's global object's associated Document's active sandboxing flag set does not have its sandboxed scripts browsing context flag set.
The result of WebDriver BiDi scripting is enabled with settings is true.

Scripting is disabled for an environment settings object when scripting is not enabled for it, i.e., when any of the above conditions are false.

Scripting is disabled for a platform object object if any of the following are true:

Scripting is disabled for object's relevant settings object.

The object implements Node, and object's node document's browsing context is null.

The object implements Window and object's associated Document's browsing context is null.

Scripting is enabled for a platform object object, when object's scripting is not disabled.

8.1.3.5 Secure contexts

An environment environment is a secure context if the following algorithm returns true:

If environment is an environment settings object, then:

Let global be environment's global object.

If global is a WorkerGlobalScope, then:

If global's owner set[0]'s relevant settings object is a secure context, then return true.

We only need to check the 0th item since they will necessarily all be consistent.

Return false.

If global is a WorkletGlobalScope, then return true.

Worklets can only be created in secure contexts.

If the result of Is url potentially trustworthy? given environment's top-level creation URL is "Potentially Trustworthy", then return true.

Return false.

An environment is a non-secure context if it is not a secure context.

8.1.4 Script processing model
8.1.4.1 Scripts

A script is one of two possible structs (namely, a classic script or a module script). All scripts have:

A settings object

An environment settings object, containing various settings that are shared with other scripts in the same context.

A record

One of the following:

a script record, for classic scripts;

a Source Text Module Record, for JavaScript module scripts;

a Synthetic Module Record, for CSS module scripts and JSON module scripts;

a WebAssembly Module Record, for WebAssembly module scripts; or

null, representing a parsing failure.

A parse error

A JavaScript value, which has meaning only if the record is null, indicating that the corresponding script source text could not be parsed.

This value is used for internal tracking of immediate parse errors when creating scripts, and is not to be used directly. Instead, consult the error to rethrow when determining "what went wrong" for this script.

An error to rethrow

A JavaScript value representing an error that will prevent evaluation from succeeding. It will be re-thrown by any attempts to run the script.

This could be the script's parse error, but in the case of a module script it could instead be the parse error from one of its dependencies, or an error from resolve a module specifier.

Since this exception value is provided by the JavaScript specification, we know that it is never null, so we use null to signal that no error has occurred.

Fetch options
Null or a script fetch options, containing various options related to fetching this script or module scripts that it imports.
A base URL

Null or a base URL used for resolving module specifiers. When non-null, this will either be the URL from which the script was obtained, for external scripts, or the document base URL of the containing document, for inline scripts.

A classic script is a type of script that has the following additional item:

A muted errors boolean

A boolean which, if true, means that error information will not be provided for errors in this script. This is used to mute errors for cross-origin scripts, since that can leak private information.

A module script is another type of script. It has no additional items.

Module scripts can be classified into four types:

A module script is a JavaScript module script if its record is a Source Text Module Record.

A module script is a CSS module script if its record is a Synthetic Module Record, and it was created via the create a CSS module script algorithm. CSS module scripts represent a parsed CSS style sheet.

A module script is a JSON module script if its record is a Synthetic Module Record, and it was created via the create a JSON module script algorithm. JSON module scripts represent a parsed JSON document.

A module script is a WebAssembly module script if its record is a WebAssembly Module Record.

As CSS style sheets and JSON documents do not import dependent modules, and do not throw exceptions on evaluation, the fetch options and base URL of CSS module scripts and JSON module scripts and are always null.

The active script is determined by the following algorithm:

Let record be GetActiveScriptOrModule().

If record is null, return null.

Return record.[[HostDefined]].

The active script concept is so far only used by the import() feature, to determine the base URL to use for resolving relative module specifiers.

8.1.4.2 Fetching scripts

This section introduces a number of algorithms for fetching scripts, taking various necessary inputs and resulting in classic or module scripts.

Script fetch options is a struct with the following items:

cryptographic nonce

The cryptographic nonce metadata used for the initial fetch and for fetching any imported modules

integrity metadata

The integrity metadata used for the initial fetch

parser metadata

The parser metadata used for the initial fetch and for fetching any imported modules

credentials mode

The credentials mode used for the initial fetch (for module scripts) and for fetching any imported modules (for both module scripts and classic scripts)

referrer policy

The referrer policy used for the initial fetch and for fetching any imported modules

This policy can mutate after a module script's response is received, to be the referrer policy parsed from the response, and used when fetching any module dependencies.

render-blocking

The boolean value of render-blocking used for the initial fetch and for fetching any imported modules. Unless otherwise stated, its value is false.

fetch priority

The priority used for the initial fetch

Recall that via the import() feature, classic scripts can import module scripts.

The default script fetch options are a script fetch options whose cryptographic nonce is the empty string, integrity metadata is the empty string, parser metadata is "not-parser-inserted", credentials mode is "same-origin", referrer policy is the empty string, and fetch priority is "auto".

To set up the classic script request, given a request request and a script fetch options options, set request's cryptographic nonce metadata to options's cryptographic nonce, its integrity metadata to options's integrity metadata, its parser metadata to options's parser metadata, its referrer policy to options's referrer policy, its render-blocking to options's render-blocking, and its priority to options's fetch priority.

To set up the module script request, given a request request and a script fetch options options, set request's cryptographic nonce metadata to options's cryptographic nonce, its integrity metadata to options's integrity metadata, its parser metadata to options's parser metadata, its credentials mode to options's credentials mode, its referrer policy to options's referrer policy, its render-blocking to options's render-blocking, and its priority to options's fetch priority.

To get the descendant script fetch options given a script fetch options originalOptions, a URL url, and an environment settings object settingsObject:

Let newOptions be a copy of originalOptions.

Let integrity be the result of resolving a module integrity metadata with url and settingsObject.

Set newOptions's integrity metadata to integrity.

Set newOptions's fetch priority to "auto".

Return newOptions.

To resolve a module integrity metadata, given a URL url and an environment settings object settingsObject:

Let map be settingsObject's global object's import map.

If map's integrity[url] does not exist, then return the empty string.

Return map's integrity[url].

Several of the below algorithms can be customized with a perform the fetch hook algorithm, which takes a request, a boolean isTopLevel, and a processCustomFetchResponse algorithm. It runs processCustomFetchResponse with a response and either null (on failure) or a byte sequence containing the response body. isTopLevel will be true for all classic script fetches, and for the initial fetch when fetching an external module script graph or fetching a module worker script graph, but false for the fetches resulting from import statements encountered throughout the graph or from import() expressions.

By default, not supplying a perform the fetch hook will cause the below algorithms to simply fetch the given request, with algorithm-specific customizations to the request and validations of the resulting response.

To layer your own customizations on top of these algorithm-specific ones, supply a perform the fetch hook that modifies the given request, fetches it, and then performs specific validations of the resulting response (completing with a network error if the validations fail).

The hook can also be used to perform more subtle customizations, such as keeping a cache of responses and avoiding performing a fetch at all.

Service Workers is an example of a specification that runs these algorithms with its own options for the hook. [SW]

Now for the algorithms themselves.

To fetch a classic script given a URL url, an environment settings object settingsObject, a script fetch options options, a CORS settings attribute state corsSetting, an encoding encoding, and an algorithm onComplete, run these steps. onComplete must be an algorithm accepting null (on failure) or a classic script (on success).

Let request be the result of creating a potential-CORS request given url, "script", and corsSetting.

Set request's client to settingsObject.

Set request's initiator type to "script".

Set up the classic script request given request and options.

Fetch request with the following processResponseConsumeBody steps given response response and null, failure, or a byte sequence bodyBytes:

response can be either CORS-same-origin or CORS-cross-origin. This only affects how error reporting happens.

Set response to response's unsafe response.

If any of the following are true:

bodyBytes is null or failure; or

response's status is not an ok status,

then run onComplete given null, and abort these steps.

For historical reasons, this algorithm does not include MIME type checking, unlike the other script-fetching algorithms in this section.

Let potentialMIMETypeForEncoding be the result of extracting a MIME type given response's header list.

Set encoding to the result of legacy extracting an encoding given potentialMIMETypeForEncoding and encoding.

This intentionally ignores the MIME type essence.

Let sourceText be the result of decoding bodyBytes to Unicode, using encoding as the fallback encoding.

The decode algorithm overrides encoding if the file contains a BOM.

Let mutedErrors be true if response was CORS-cross-origin, and false otherwise.

Let script be the result of creating a classic script given sourceText, settingsObject, response's URL, options, mutedErrors, and url.

Run onComplete given script.

To fetch a classic worker script given a URL url, an environment settings object fetchClient, a destination destination, an environment settings object settingsObject, an algorithm onComplete, and an optional perform the fetch hook performFetch, run these steps. onComplete must be an algorithm accepting null (on failure) or a classic script (on success).

Let request be a new request whose URL is url, client is fetchClient, destination is destination, initiator type is "other", mode is "same-origin", credentials mode is "same-origin", parser metadata is "not parser-inserted", and whose use-URL-credentials flag is set.

If performFetch was given, run performFetch with request, true, and with processResponseConsumeBody as defined below.

Otherwise, fetch request with processResponseConsumeBody set to processResponseConsumeBody as defined below.

In both cases, let processResponseConsumeBody given response response and null, failure, or a byte sequence bodyBytes be the following algorithm:

Set response to response's unsafe response.

If any of the following are true:

bodyBytes is null or failure; or

response's status is not an ok status,

then run onComplete given null, and abort these steps.

If all of the following are true:

response's URL's scheme is an HTTP(S) scheme; and

the result of extracting a MIME type from response's header list is not a JavaScript MIME type,

then run onComplete given null, and abort these steps.

Other fetch schemes are exempted from MIME type checking for historical web-compatibility reasons. We might be able to tighten this in the future; see issue #3255.

Let sourceText be the result of UTF-8 decoding bodyBytes.

Let script be the result of creating a classic script using sourceText, settingsObject, response's URL, and the default script fetch options.

Run onComplete given script.

To fetch a classic worker-imported script given a URL url, an environment settings object settingsObject, and an optional perform the fetch hook performFetch, run these steps. The algorithm will return a classic script on success, or throw an exception on failure.

Let response be null.

Let bodyBytes be null.

Let request be a new request whose URL is url, client is settingsObject, destination is "script", initiator type is "other", parser metadata is "not parser-inserted", and whose use-URL-credentials flag is set.

If performFetch was given, run performFetch with request, isTopLevel, and with processResponseConsumeBody as defined below.

Otherwise, fetch request with processResponseConsumeBody set to processResponseConsumeBody as defined below.

In both cases, let processResponseConsumeBody given response res and null, failure, or a byte sequence bb be the following algorithm:

Set bodyBytes to bb.

Set response to res.

Pause until response is not null.

Unlike other algorithms in this section, the fetching process is synchronous here.

Set response to response's unsafe response.

If any of the following are true:

bodyBytes is null or failure;

response's status is not an ok status; or

the result of extracting a MIME type from response's header list is not a JavaScript MIME type,

then throw a "NetworkError" DOMException.

Let sourceText be the result of UTF-8 decoding bodyBytes.

Let mutedErrors be true if response was CORS-cross-origin, and false otherwise.

Let script be the result of creating a classic script given sourceText, settingsObject, response's URL, the default script fetch options, and mutedErrors.

Return script.

To fetch an external module script graph given a URL url, an environment settings object settingsObject, a script fetch options options, and an algorithm onComplete, run these steps. onComplete must be an algorithm accepting null (on failure) or a module script (on success).

Fetch a single module script given url, settingsObject, "script", options, settingsObject, "client", true, and with the following steps given result:

If result is null, run onComplete given null, and abort these steps.

Fetch the descendants of and link result given settingsObject, "script", and onComplete.

To fetch a modulepreload module script graph given a URL url, a destination destination, an environment settings object settingsObject, a script fetch options options, and an algorithm onComplete, run these steps. onComplete must be an algorithm accepting null (on failure) or a module script (on success).

Fetch a single module script given url, settingsObject, destination, options, settingsObject, "client", true, and with the following steps given result:

Run onComplete given result.

Assert: settingsObject's global object implements Window.

If result is not null, optionally fetch the descendants of and link result given settingsObject, destination, and an empty algorithm.

Generally, performing this step will be beneficial for performance, as it allows pre-loading the modules that will invariably be requested later, via algorithms such as fetch an external module script graph that fetch the entire graph. However, user agents might wish to skip them in bandwidth-constrained situations, or situations where the relevant fetches are already in flight.

To fetch an inline module script graph given a string sourceText, a URL baseURL, an environment settings object settingsObject, a script fetch options options, and an algorithm onComplete, run these steps. onComplete must be an algorithm accepting null (on failure) or a module script (on success).

Let script be the result of creating a JavaScript module script using sourceText, settingsObject, baseURL, and options.

Fetch the descendants of and link script, given settingsObject, "script", and onComplete.

To fetch a module worker script graph given a URL url, an environment settings object fetchClient, a destination destination, a credentials mode credentialsMode, an environment settings object settingsObject, and an algorithm onComplete, fetch a worklet/module worker script graph given url, fetchClient, destination, credentialsMode, settingsObject, and onComplete.

To fetch a worklet script graph given a URL url, an environment settings object fetchClient, a destination destination, a credentials mode credentialsMode, an environment settings object settingsObject, a module responses map moduleResponsesMap, and an algorithm onComplete, fetch a worklet/module worker script graph given url, fetchClient, destination, credentialsMode, settingsObject, onComplete, and the following perform the fetch hook given request and processCustomFetchResponse:

Let requestURL be request's URL.

If moduleResponsesMap[requestURL] is "fetching", wait in parallel until that entry's value changes, then queue a task on the networking task source to proceed with running the following steps.

If moduleResponsesMap[requestURL] exists, then:

Let cached be moduleResponsesMap[requestURL].

Run processCustomFetchResponse with cached[0] and cached[1].

Return.

Set moduleResponsesMap[requestURL] to "fetching".

Fetch request, with processResponseConsumeBody set to the following steps given response response and null, failure, or a byte sequence bodyBytes:

Set moduleResponsesMap[requestURL] to (response, bodyBytes).

Run processCustomFetchResponse with response and bodyBytes.

The following algorithms are meant for internal use by this specification only as part of fetching an external module script graph or other similar concepts above, and should not be used directly by other specifications.

This diagram illustrates how these algorithms relate to the ones above, as well as to each other:

fetch an external module script graph
fetch a modulepreload module script graph
fetch an inline module script graph
fetch a module worker script graph
fetch a worklet script graph
fetch a worklet/module worker script graph
fetch the descendants of and link a module script

To fetch a worklet/module worker script graph given a URL url, an environment settings object fetchClient, a destination destination, a credentials mode credentialsMode, an environment settings object settingsObject, an algorithm onComplete, and an optional perform the fetch hook performFetch, run these steps. onComplete must be an algorithm accepting null (on failure) or a module script (on success).

Let options be a script fetch options whose cryptographic nonce is the empty string, integrity metadata is the empty string, parser metadata is "not-parser-inserted", credentials mode is credentialsMode, referrer policy is the empty string, and fetch priority is "auto".

Fetch a single module script given url, fetchClient, destination, options, settingsObject, "client", true, and onSingleFetchComplete as defined below. If performFetch was given, pass it along as well.

onSingleFetchComplete given result is the following algorithm:

If result is null, run onComplete given null, and abort these steps.

Fetch the descendants of and link result given fetchClient, destination, and onComplete. If performFetch was given, pass it along as well.

To fetch the descendants of and link a module script moduleScript, given an environment settings object fetchClient, a destination destination, an algorithm onComplete, and an optional perform the fetch hook performFetch, run these steps. onComplete must be an algorithm accepting null (on failure) or a module script (on success).

Let record be moduleScript's record.

If record is null, then:

Set moduleScript's error to rethrow to moduleScript's parse error.

Run onComplete given moduleScript.

Return.

Let state be Record { [[ErrorToRethrow]]: null, [[Destination]]: destination, [[PerformFetch]]: null, [[FetchClient]]: fetchClient }.

If performFetch was given, set state.[[PerformFetch]] to performFetch.

Let loadingPromise be record.LoadRequestedModules(state).

This step will recursively load all the module transitive dependencies.

Upon fulfillment of loadingPromise, run the following steps:

Perform record.Link().

This step will recursively call Link on all of the module's unlinked dependencies.

If this throws an exception, catch it, and set moduleScript's error to rethrow to that exception.

Run onComplete given moduleScript.

Upon rejection of loadingPromise, run the following steps:

If state.[[ErrorToRethrow]] is not null, set moduleScript's error to rethrow to state.[[ErrorToRethrow]] and run onComplete given moduleScript.

Otherwise, run onComplete given null.

state.[[ErrorToRethrow]] is null when loadingPromise is rejected due to a loading error.

To fetch a single module script, given a URL url, an environment settings object fetchClient, a destination destination, a script fetch options options, an environment settings object settingsObject, a referrer referrer, an optional ModuleRequest Record moduleRequest, a boolean isTopLevel, an algorithm onComplete, and an optional perform the fetch hook performFetch, run these steps. onComplete must be an algorithm accepting null (on failure) or a module script (on success).

Let moduleType be "javascript-or-wasm".

If moduleRequest was given, then set moduleType to the result of running the module type from module request steps given moduleRequest.

Assert: the result of running the module type allowed steps given moduleType and settingsObject is true. Otherwise, we would not have reached this point because a failure would have been raised when inspecting moduleRequest.[[Attributes]] in HostLoadImportedModule or fetch a single imported module script.

Let moduleMap be settingsObject's module map.

If moduleMap[(url, moduleType)] is "fetching", wait in parallel until that entry's value changes, then queue a task on the networking task source to proceed with running the following steps.

If moduleMap[(url, moduleType)] exists, run onComplete given moduleMap[(url, moduleType)], and return.

Set moduleMap[(url, moduleType)] to "fetching".

Let request be a new request whose URL is url, mode is "cors", referrer is referrer, and client is fetchClient.

Set request's destination to the result of running the fetch destination from module type steps given destination and moduleType.

If destination is "worker", "sharedworker", or "serviceworker", and isTopLevel is true, then set request's mode to "same-origin".

Set request's initiator type to "script".

Set up the module script request given request and options.

If performFetch was given, run performFetch with request, isTopLevel, and with processResponseConsumeBody as defined below.

Otherwise, fetch request with processResponseConsumeBody set to processResponseConsumeBody as defined below.

In both cases, let processResponseConsumeBody given response response and null, failure, or a byte sequence bodyBytes be the following algorithm:

response is always CORS-same-origin.

If any of the following are true:

bodyBytes is null or failure; or

response's status is not an ok status,

then set moduleMap[(url, moduleType)] to null, run onComplete given null, and abort these steps.

Let mimeType be the result of extracting a MIME type from response's header list.

Let moduleScript be null.

Let referrerPolicy be the result of parsing the `Referrer-Policy` header given response. [REFERRERPOLICY]

If referrerPolicy is not the empty string, set options's referrer policy to referrerPolicy.

If mimeType's essence is "application/wasm" and moduleType is "javascript-or-wasm", then set moduleScript to the result of creating a WebAssembly module script given bodyBytes, settingsObject, response's URL, and options.

Otherwise:

Let sourceText be the result of UTF-8 decoding bodyBytes.

If mimeType is a JavaScript MIME type and moduleType is "javascript-or-wasm", then set moduleScript to the result of creating a JavaScript module script given sourceText, settingsObject, response's URL, and options.

If the MIME type essence of mimeType is "text/css" and moduleType is "css", then set moduleScript to the result of creating a CSS module script given sourceText and settingsObject.

If mimeType is a JSON MIME type and moduleType is "json", then set moduleScript to the result of creating a JSON module script given sourceText and settingsObject.

Set moduleMap[(url, moduleType)] to moduleScript, and run onComplete given moduleScript.

It is intentional that the module map is keyed by the request URL, whereas the base URL for the module script is set to the response URL. The former is used to deduplicate fetches, while the latter is used for URL resolution.

To fetch a single imported module script, given a URL url, an environment settings object fetchClient, a destination destination, a script fetch options options, environment settings object settingsObject, a referrer referrer, a ModuleRequest Record moduleRequest, an algorithm onComplete, and an optional perform the fetch hook performFetch, run these steps. onComplete must be an algorithm accepting null (on failure) or a module script (on success).

Assert: moduleRequest.[[Attributes]] does not contain any Record entry such that entry.[[Key]] is not "type", because we only asked for "type" attributes in HostGetSupportedImportAttributes.

Let moduleType be the result of running the module type from module request steps given moduleRequest.

If the result of running the module type allowed steps given moduleType and settingsObject is false, then run onComplete given null, and return.

Fetch a single module script given url, fetchClient, destination, options, settingsObject, referrer, moduleRequest, false, and onComplete. If performFetch was given, pass it along as well.

8.1.4.3 Creating scripts

This standard refers to the following concepts defined there:

WebDriver BiDi command "script.evaluate"

To create a classic script, given a string source, an environment settings object settings, a URL baseURL, a script fetch options options, an optional boolean mutedErrors (default false), an optional URL-or-null sourceURLForWindowScripts (default null), and an optional boolean bypassDisabledScripting (default false):

The bypassDisabledScripting parameter is intended to be used for running scripts even if scripting is disabled. This is required for some automation scenarios, e.g. for WebDriver BiDi command "script.evaluate".

The bypassDisabledScripting parameter is intended to be used for running scripts even if scripting is disabled. This is required for some automation scenarios, e.g. for WebDriver BiDi command "script.evaluate". When the scripting process (e.g., executing a script via a WebDriver BiDi command) is invoked with bypassDisabledScripting set to true, the event loop is allowed to run to resolve thenables (from promises) and weakmap finalizations created by that script, even if scripting is disabled. This is necessary to ensure the proper functioning of testing scripts, which often rely on asynchronous operations.

If mutedErrors is true, then set baseURL to about:blank.

When mutedErrors is true, baseURL is the script's CORS-cross-origin response's url, which shouldn't be exposed to JavaScript. Therefore, baseURL is sanitized here.

If scripting is disabled for settings and bypassDisabledScripting is false, then set source to the empty string.

Let script be a new classic script that this algorithm will subsequently initialize.

Set script's settings object to settings.

Set script's base URL to baseURL.

Set script's fetch options to options.

Set script's muted errors to mutedErrors.

Set script's parse error and error to rethrow to null.

Record classic script creation time given script and sourceURLForWindowScripts.

Let result be ParseScript(source, settings's realm, script).

Passing script as the last parameter here ensures result.[[HostDefined]] will be script.

If result is a list of errors, then:

Set script's parse error and its error to rethrow to result[0].

Return script.

Set script's record to result.

Return script.

To create a JavaScript module script, given a string source, an environment settings object settings, a URL baseURL, and a script fetch options options:

If scripting is disabled for settings, then set source to the empty string.

Let script be a new module script that this algorithm will subsequently initialize.

Set script's settings object to settings.

Set script's base URL to baseURL.

Set script's fetch options to options.

Set script's parse error and error to rethrow to null.

Let result be ParseModule(source, settings's realm, script).

Passing script as the last parameter here ensures result.[[HostDefined]] will be script.

If result is a list of errors, then:

Set script's parse error to result[0].

Return script.

Set script's record to result.

Return script.

To create a WebAssembly module script, given a byte sequence bodyBytes, an environment settings object settings, a URL baseURL, and a script fetch options options:

If scripting is disabled for settings, then set bodyBytes to the byte sequence 0x00 0x61 0x73 0x6D 0x01 0x00 0x00 0x00.

This byte sequence corresponds to an empty WebAssembly module with only the magic bytes and version number provided.

Let script be a new module script that this algorithm will subsequently initialize.

Set script's settings object to settings.

Set script's base URL to baseURL.

Set script's fetch options to options.

Set script's parse error and error to rethrow to null.

Let result be the result of parsing a WebAssembly module given bodyBytes, settings's realm, and script.

Passing script as the last parameter here ensures result.[[HostDefined]] will be script.

If the previous step threw an error error, then:

Set script's parse error to error.

Return script.

Set script's record to result.

Return script.

WebAssembly JavaScript Interface: ESM Integration specifies the hooks for the WebAssembly integration with ECMA-262 module loading. This includes support both for direct dependency imports, as well as for source phase imports, which support virtualization and multi-instantiation. [WASMESM]

To create a CSS module script, given a string source and an environment settings object settings:

Let script be a new module script that this algorithm will subsequently initialize.

Set script's settings object to settings.

Set script's base URL and fetch options to null.

Set script's parse error and error to rethrow to null.

Let sheet be the result of running the steps to create a constructed CSSStyleSheet with an empty dictionary as the argument.

Run the steps to synchronously replace the rules of a CSSStyleSheet on sheet given source.

If this throws an exception, catch it, and set script's parse error to that exception, and return script.

The steps to synchronously replace the rules of a CSSStyleSheet will throw if source contains any @import rules. This is by-design for now because there is not yet an agreement on how to handle these for CSS module scripts; therefore they are blocked altogether until a consensus is reached.

Set script's record to the result of CreateDefaultExportSyntheticModule(sheet).

Return script.

To create a JSON module script, given a string source and an environment settings object settings:

Let script be a new module script that this algorithm will subsequently initialize.

Set script's settings object to settings.

Set script's base URL and fetch options to null.

Set script's parse error and error to rethrow to null.

Let result be ParseJSONModule(source).

If this throws an exception, catch it, and set script's parse error to that exception, and return script.

Set script's record to result.

Return script.

The module type from module request steps, given a ModuleRequest Record moduleRequest, are as follows:

Let moduleType be "javascript-or-wasm".

If moduleRequest.[[Attributes]] has a Record entry such that entry.[[Key]] is "type", then:

If entry.[[Value]] is "javascript-or-wasm", then set moduleType to null.

This specification uses the "javascript-or-wasm" module type internally for JavaScript module scripts or WebAssembly module scripts, so this step is needed to prevent modules from being imported using a "javascript-or-wasm" type attribute (a null moduleType will cause the module type allowed check to fail).

Otherwise, set moduleType to entry.[[Value]].

Return moduleType.

The module type allowed steps, given a string moduleType and an environment settings object settings, are as follows:

If moduleType is not "javascript-or-wasm", "css", or "json", then return false.

If moduleType is "css" and the CSSStyleSheet interface is not exposed in settings's realm, then return false.

Return true.

The fetch destination from module type steps, given a destination defaultDestination and a string moduleType, are as follows:

If moduleType is "json", then return "json".
If moduleType is "css", then return "style".
Return defaultDestination.
8.1.4.4 Calling scripts

To run a classic script given a classic script script and an optional boolean rethrow errors (default false):

Let settings be the settings object of script.

Check if we can run script with settings. If this returns "do not run", then return NormalCompletion(empty).

Record classic script execution start time given script.

Prepare to run script given settings.

Let evaluationStatus be null.

If script's error to rethrow is not null, then set evaluationStatus to ThrowCompletion(script's error to rethrow).

Otherwise, set evaluationStatus to ScriptEvaluation(script's record).

If ScriptEvaluation does not complete because the user agent has aborted the running script, leave evaluationStatus as null.

If evaluationStatus is an abrupt completion, then:

If rethrow errors is true and script's muted errors is false, then:

Clean up after running script with settings.

Rethrow evaluationStatus.[[Value]].

If rethrow errors is true and script's muted errors is true, then:

Clean up after running script with settings.

Throw a "NetworkError" DOMException.

Otherwise, rethrow errors is false. Perform the following steps:

Report an exception given by evaluationStatus.[[Value]] for script's settings object's global object.

Clean up after running script with settings.

Return evaluationStatus.

Clean up after running script with settings.

If evaluationStatus is a normal completion, then return evaluationStatus.

If we've reached this point, evaluationStatus was left as null because the script was aborted prematurely during evaluation. Return ThrowCompletion(a new QuotaExceededError).

To run a module script given a module script script and an optional boolean preventErrorReporting (default false):

Let settings be the settings object of script.

Check if we can run script with settings. If this returns "do not run", then return a promise resolved with undefined.

Record module script execution start time given script.

Prepare to run script given settings.

Let evaluationPromise be null.

If script's error to rethrow is not null, then set evaluationPromise to a promise rejected with script's error to rethrow.

Otherwise:

Let record be script's record.

Set evaluationPromise to record.Evaluate().

This step will recursively evaluate all of the module's dependencies.

If Evaluate fails to complete as a result of the user agent aborting the running script, then set evaluationPromise to a promise rejected with a new QuotaExceededError.

If preventErrorReporting is false, then upon rejection of evaluationPromise with reason, report an exception given by reason for script's settings object's global object.

Clean up after running script with settings.

Return evaluationPromise.

The steps to check if we can run script with an environment settings object settings are as follows. They return either "run" or "do not run".

If the global object specified by settings is a Window object whose Document object is not fully active, then return "do not run".

If scripting is disabled for settings, then return "do not run".

Return "run".

The steps to prepare to run script with an environment settings object settings are as follows:

Push settings's realm execution context onto the JavaScript execution context stack; it is now the running JavaScript execution context.

Add settings to the surrounding agent's event loop's currently running task's script evaluation environment settings object set.

The steps to clean up after running script with an environment settings object settings are as follows:

Assert: settings's realm execution context is the running JavaScript execution context.

Remove settings's realm execution context from the JavaScript execution context stack.

If the JavaScript execution context stack is now empty, perform a microtask checkpoint. (If this runs scripts, these algorithms will be invoked reentrantly.)

These algorithms are not invoked by one script directly calling another, but they can be invoked reentrantly in an indirect manner, e.g. if a script dispatches an event which has event listeners registered.

The running script is the script in the [[HostDefined]] field in the ScriptOrModule component of the running JavaScript execution context.

8.1.4.5 Killing scripts

Although the JavaScript specification does not account for this possibility, it's sometimes necessary to abort a running script. This causes any ScriptEvaluation or Source Text Module Record Evaluate invocations to cease immediately, emptying the JavaScript execution context stack without triggering any of the normal mechanisms like finally blocks. [JAVASCRIPT]

User agents may impose resource limitations on scripts, for example CPU quotas, memory limits, total execution time limits, or bandwidth limitations. When a script exceeds a limit, the user agent may either throw a QuotaExceededError, abort the script without an exception, prompt the user, or throttle script execution.

For example, the following script never terminates. A user agent could, after waiting for a few seconds, prompt the user to either terminate the script or let it continue.

<script>
 while (true) { /* loop */ }
</script>

User agents are encouraged to allow users to disable scripting whenever the user is prompted either by a script (e.g. using the window.alert() API) or because of a script's actions (e.g. because it has exceeded a time limit).

If scripting is disabled while a script is executing, the script should be terminated immediately.

User agents may allow users to specifically disable scripts just for the purposes of closing a browsing context.

For example, the prompt mentioned in the example above could also offer the user with a mechanism to just close the page entirely, without running any unload event handlers.

8.1.4.6 Runtime script errors
✔MDN
self.reportError(e)

Dispatches an error event at the global object for the given value e, in the same fashion as an unhandled exception.

To extract error information from a JavaScript value exception:

Let attributes be an empty map keyed by IDL attributes.

Set attributes[error] to exception.

Set attributes[message], attributes[filename], attributes[lineno], and attributes[colno] to implementation-defined values derived from exception.

Browsers implement behavior not specified here or in the JavaScript specification to gather values which are helpful, including in unusual cases (e.g., eval). In the future, this might be specified in greater detail.

Return attributes.

To report an exception exception which is a JavaScript value, for a particular global object global and optional boolean omitError (default false):

Let notHandled be true.

Let errorInfo be the result of extracting error information from exception.

Let script be a script found in an implementation-defined way, or null. This should usually be the running script (most notably during run a classic script).

Implementations have not yet settled on interoperable behavior for which script is used to determine whether errors are muted in less common cases.

If script is a classic script and script's muted errors is true, then set errorInfo[error] to null, errorInfo[message] to "Script error.", errorInfo[filename] to the empty string, errorInfo[lineno] to 0, and errorInfo[colno] to 0.

If omitError is true, then set errorInfo[error] to null.

If global is not in error reporting mode, then:

Set global's in error reporting mode to true.

If global implements EventTarget, then set notHandled to the result of firing an event named error at global, using ErrorEvent, with the cancelable attribute initialized to true, and additional attributes initialized according to errorInfo.

Returning true in an event handler cancels the event per the event handler processing algorithm.

Set global's in error reporting mode to false.

If notHandled is true, then:

Set errorInfo[error] to null.

If global implements DedicatedWorkerGlobalScope, queue a global task on the DOM manipulation task source with the global's associated Worker's relevant global object to run these steps:

Let workerObject be the Worker object associated with global.

Set notHandled to the result of firing an event named error at workerObject, using ErrorEvent, with the cancelable attribute initialized to true, and additional attributes initialized according to errorInfo.

If notHandled is true, then report exception for workerObject's relevant global object with omitError set to true.

The actual exception value will not be available in the owner realm, but the user agent still carries through enough information to set the message, filename, and other attributes, as well as potentially report to a developer console.

Otherwise, the user agent may report exception to a developer console.

If the implicit port connecting a worker to its Worker object has been disentangled (i.e. if the parent worker has been terminated), then the user agent must act as if the Worker object had no error event handler and as if that worker's onerror attribute was null, but must otherwise act as described above.

Thus, error reports propagate up to the chain of dedicated workers up to the original Document, even if some of the workers along this chain have been terminated and garbage collected.

Previous revisions of this standard defined an algorithm to report the exception. As part of issue #958, this has been superseded by report an exception which behaves differently and takes different inputs. Issue #10516 tracks updating the specification ecosystem.

The reportError(e) method steps are to report an exception e for this.

It is unclear whether muting is applicable here. In Chrome and Safari it is muted, but in Firefox it is not. See also issue #958.

✔MDN

The ErrorEvent interface is defined as follows:

[Exposed=*]
interface ErrorEvent : Event {
  constructor(DOMString type, optional ErrorEventInit eventInitDict = {});

  readonly attribute DOMString message;
  readonly attribute USVString filename;
  readonly attribute unsigned long lineno;
  readonly attribute unsigned long colno;
  readonly attribute any error;
};

dictionary ErrorEventInit : EventInit {
  DOMString message = "";
  USVString filename = "";
  unsigned long lineno = 0;
  unsigned long colno = 0;
  any error;
};

The message attribute must return the value it was initialized to. It represents the error message.

The filename attribute must return the value it was initialized to. It represents the URL of the script in which the error originally occurred.

The lineno attribute must return the value it was initialized to. It represents the line number where the error occurred in the script.

The colno attribute must return the value it was initialized to. It represents the column number where the error occurred in the script.

The error attribute must return the value it was initialized to. It must initially be initialized to undefined. Where appropriate, it is set to the object representing the error (e.g., the exception object in the case of an uncaught exception).

8.1.4.7 Unhandled promise rejections
✔MDN

In addition to synchronous runtime script errors, scripts may experience asynchronous promise rejections, tracked via the unhandledrejection and rejectionhandled events. Tracking these rejections is done via the HostPromiseRejectionTracker abstract operation, but reporting them is defined here.

To notify about rejected promises given a global object global:

Let list be a clone of global's about-to-be-notified rejected promises list.

If list is empty, then return.

Empty global's about-to-be-notified rejected promises list.

Queue a global task on the DOM manipulation task source given global to run the following step:

For each promise p of list:

If p.[[PromiseIsHandled]] is true, then continue.

Let notCanceled be the result of firing an event named unhandledrejection at global, using PromiseRejectionEvent, with the cancelable attribute initialized to true, the promise attribute initialized to p, and the reason attribute initialized to p.[[PromiseResult]].

If notCanceled is true, then the user agent may report p.[[PromiseResult]] to a developer console.

If p.[[PromiseIsHandled]] is false, then append p to global's outstanding rejected promises weak set.

✔MDN

The PromiseRejectionEvent interface is defined as follows:

[Exposed=*]
interface PromiseRejectionEvent : Event {
  constructor(DOMString type, PromiseRejectionEventInit eventInitDict);

  readonly attribute object promise;
  readonly attribute any reason;
};

dictionary PromiseRejectionEventInit : EventInit {
  required object promise;
  any reason;
};
✔MDN

The promise attribute must return the value it was initialized to. It represents the promise which this notification is about.

Because of how Web IDL conversion rules for Promise<T> types always wrap the input into a new promise, the promise attribute is of type object instead, which is more appropriate for representing an opaque handle to the original promise object.

✔MDN

The reason attribute must return the value it was initialized to. It represents the rejection reason for the promise.

8.1.4.8 Import map parse results

An import map parse result is a struct that is similar to a script, and also can be stored in a script element's result, but is not counted as a script for other purposes. It has the following items:

An import map
An import map or null.
An error to rethrow
A JavaScript value representing an error that will prevent using this import map, when non-null.

To create an import map parse result given a string input and a URL baseURL:

Let result be an import map parse result whose import map is null and whose error to rethrow is null.

Parse an import map string given input and baseURL, catching any exceptions. If this threw an exception, then set result's error to rethrow to that exception. Otherwise, set result's import map to the return value.

Return result.

To register an import map given a Window global and an import map parse result result:

If result's error to rethrow is not null, then report an exception given by result's error to rethrow for global and return.

Merge existing and new import maps, given global and result's import map.

8.1.4.9 Speculation rules parse results

A speculation rules parse result is a struct that is similar to a script, and also can be stored in a script element's result, but is not counted as a script for other purposes. It has the following items:

A speculation rule set
A speculation rule set or null.
An error to rethrow
A JavaScript value representing an error that will prevent using these speculation rules, when non-null.

To create a speculation rules parse result given a string input and a Document document:

Let result be a speculation rules parse result whose import map is null and whose error to rethrow is null.

Parse a speculation rule set string given input, document, and document's document base URL, catching any exceptions. If this threw an exception, then set result's error to rethrow to that exception. Otherwise, set result's speculation rule set to the return value.

Return result.

To register speculation rules given a Window global, a speculation rules parse result result, and an optional boolean queueErrors (default false):

If result's error to rethrow is not null, then:

If queueErrors is true, then queue a global task on the DOM manipulation task source given global to perform the following step:

Report an exception given by result's error to rethrow for global.

Otherwise, report an exception given by result's error to rethrow for global.

Return.

Append result's speculation rule set to global's associated Document's speculation rule sets.

Consider speculative loads for global's associated Document.

To unregister speculation rules given a Window global and a speculation rules parse result result:

If result's error to rethrow is not null, then return.

Remove result's speculation rule set from global's associated Document's speculation rule sets.

Consider speculative loads for global's associated Document.

To update speculation rules given a Window global, a speculation rules parse result oldResult, and a speculation rules parse result newResult:

Remove oldResult's speculation rule set from global's associated Document's speculation rule sets.

Register speculation rules given global, newResult, and true.

When updating speculation rules, as opposed to registering them for the first time, we ensure that any error events are queued as tasks, instead of synchronously fired. Although synchronously executing error event handlers is OK when inserting script elements, it's best if other modifications do not cause such synchronous script execution.

8.1.5 Module specifier resolution
8.1.5.1 The resolution algorithm

The resolve a module specifier algorithm is the primary entry point for converting module specifier strings into URLs. When no import maps are involved, it is relatively straightforward, and reduces to resolving a URL-like module specifier.

When there is a non-empty import map present, the behavior is more complex. It checks candidate entries from all applicable module specifier maps, from most-specific to least-specific scopes (falling back to the top-level unscoped imports), and from most-specific to least-specific prefixes. For each candidate, the resolve an imports match algorithm will give one of the following results:

Successful resolution of the specifier to a URL. Then the resolve a module specifier algorithm will return that URL.

Throwing an exception. Then the resolve a module specifier algorithm will rethrow that exception, without any further fallbacks.

Failing to resolve, without an error. In this case the outer resolve a module specifier algorithm will move on to the next candidate.

In the end, if no successful resolution is found via any of the candidate module specifier maps, resolve a module specifier will throw an exception. Thus the result is always either a URL or a thrown exception.

To resolve a module specifier given a script-or-null referringScript and a string specifier:

Let settingsObject and baseURL be null.

If referringScript is not null, then:

Set settingsObject to referringScript's settings object.

Set baseURL to referringScript's base URL.

Otherwise:

Assert: there is a current settings object.

Set settingsObject to the current settings object.

Set baseURL to settingsObject's API base URL.

Let importMap be an empty import map.

If settingsObject's global object implements Window, then set importMap to settingsObject's global object's import map.

Let serializedBaseURL be baseURL, serialized.

Let asURL be the result of resolving a URL-like module specifier given specifier and baseURL.

Let normalizedSpecifier be the serialization of asURL, if asURL is non-null; otherwise, specifier.

Let result be a URL-or-null, initially null.

For each scopePrefix → scopeImports of importMap's scopes:

If scopePrefix is serializedBaseURL, or if scopePrefix ends with U+002F (/) and scopePrefix is a code unit prefix of serializedBaseURL, then:

Let scopeImportsMatch be the result of resolving an imports match given normalizedSpecifier, asURL, and scopeImports.

If scopeImportsMatch is not null, then set result to scopeImportsMatch, and break.

If result is null, set result to the result of resolving an imports match given normalizedSpecifier, asURL, and importMap's imports.

If result is null, set it to asURL.

By this point, if result was null, specifier wasn't remapped to anything by importMap, but it might have been able to be turned into a URL.

If result is not null, then:

Add module to resolved module set given settingsObject, serializedBaseURL, normalizedSpecifier, and asURL.

Return result.

Throw a TypeError indicating that specifier was a bare specifier, but was not remapped to anything by importMap.

To resolve an imports match, given a string normalizedSpecifier, a URL-or-null asURL, and a module specifier map specifierMap:

For each specifierKey → resolutionResult of specifierMap:

If specifierKey is normalizedSpecifier, then:

If resolutionResult is null, then throw a TypeError indicating that resolution of specifierKey was blocked by a null entry.

This will terminate the entire resolve a module specifier algorithm, without any further fallbacks.

Assert: resolutionResult is a URL.

Return resolutionResult.

If all of the following are true:

specifierKey ends with U+002F (/);

specifierKey is a code unit prefix of normalizedSpecifier; and

either asURL is null, or asURL is special,

then:

If resolutionResult is null, then throw a TypeError indicating that the resolution of specifierKey was blocked by a null entry.

This will terminate the entire resolve a module specifier algorithm, without any further fallbacks.

Assert: resolutionResult is a URL.

Let afterPrefix be the portion of normalizedSpecifier after the initial specifierKey prefix.

Assert: resolutionResult, serialized, ends with U+002F (/), as enforced during parsing.

Let url be the result of URL parsing afterPrefix with resolutionResult.

If url is failure, then throw a TypeError indicating that resolution of normalizedSpecifier was blocked since the afterPrefix portion could not be URL-parsed relative to the resolutionResult mapped to by the specifierKey prefix.

This will terminate the entire resolve a module specifier algorithm, without any further fallbacks.

Assert: url is a URL.

If the serialization of resolutionResult is not a code unit prefix of the serialization of url, then throw a TypeError indicating that the resolution of normalizedSpecifier was blocked due to it backtracking above its prefix specifierKey.

This will terminate the entire resolve a module specifier algorithm, without any further fallbacks.

Return url.

Return null.

The resolve a module specifier algorithm will fall back to a less-specific scope, or to "imports", if possible.

To resolve a URL-like module specifier, given a string specifier and a URL baseURL:

If specifier starts with "/", "./", or "../", then:

Let url be the result of URL parsing specifier with baseURL.

If url is failure, then return null.

One way this could happen is if specifier is "../foo" and baseURL is a data: URL.

Return url.

This includes cases where specifier starts with "//", i.e., scheme-relative URLs. Thus, url might end up with a different host than baseURL.

Let url be the result of URL parsing specifier (with no base URL).

If url is failure, then return null.

Return url.

8.1.5.2 Import maps

An import map allows control over module specifier resolution. Import maps are delivered via inline script elements with their type attribute set to "importmap", and with their child text content containing a JSON representation of the import map.

A Document can have multiple import maps processed, which can happen either before or after any modules have been imported, e.g., via import() expressions or script elements with their type attribute set to "module". The merge existing and new import maps algorithm ensures that new import maps cannot define the module resolution for modules that were already defined by past import maps, or for ones that were already resolved.

The simplest use of import maps is to globally remap a bare module specifier:

{
  "imports": {
    "moment": "/node_modules/moment/src/moment.js"
  }
}

This enables statements like import moment from "moment"; to work, fetching and evaluating the JavaScript module at the /node_modules/moment/src/moment.js URL.

An import map can remap a class of module specifiers into a class of URLs by using trailing slashes, like so:

{
  "imports": {
    "moment/": "/node_modules/moment/src/"
  }
}

This enables statements like import localeData from "moment/locale/zh-cn.js"; to work, fetching and evaluating the JavaScript module at the /node_modules/moment/src/locale/zh-cn.js URL. Such trailing-slash mappings are often combined with bare-specifier mappings, e.g.

{
  "imports": {
    "moment": "/node_modules/moment/src/moment.js",
    "moment/": "/node_modules/moment/src/"
  }
}

so that both the "main module" specified by "moment" and the "submodules" specified by paths such as "moment/locale/zh-cn.js" are available.

Bare specifiers are not the only type of module specifiers which import maps can remap. "URL-like" specifiers, i.e., those that are either parseable as absolute URLs or start with "/", "./", or "../", can be remapped as well:

{
  "imports": {
    "https://cdn.example.com/vue/dist/vue.runtime.esm.js": "/node_modules/vue/dist/vue.runtime.esm.js",
    "/js/app.mjs": "/js/app-8e0d62a03.mjs",
    "../helpers/": "https://cdn.example/helpers/"
  }
}

Note how the URL to be remapped, as well as the URL being mapped to, can be specified either as absolute URLs, or as relative URLs starting with "/", "./", or "../". (They cannot be specified as relative URLs without those starting sigils, as those help distinguish from bare module specifiers.) Also note how the trailing slash mapping works in this context as well.

Such remappings operate on the post-canonicalization URL, and do not require a match between the literal strings supplied in the import map key and the imported module specifier. So for example, if this import map was included on https://example.com/app.html, then not only would import "/js/app.mjs" be remapped, but so would import "./js/app.mjs" and import "./foo/../js/app.mjs".

All previous examples have globally remapped module specifiers, by using the top-level "imports" key in the import map. The top-level "scopes" key can be used to provide localized remappings, which only apply when the referring module matches a specific URL prefix. For example:

{
  "scopes": {
    "/a/" : {
      "moment": "/node_modules/moment/src/moment.js"
    },
    "/b/" : {
      "moment": "https://cdn.example.com/moment/src/moment.js"
    }
  }
}

With this import map, the statement import "moment" will have different meanings depending on which referrer script contains the statement:

Inside scripts located under /a/, this will import /node_modules/moment/src/moment.js.

Inside scripts located under /b/, this will import https://cdn.example.com/moment/src/moment.js.

Inside scripts located under /c/, this will fail to resolve and thus throw an exception.

A typical usage of scopes is to allow multiple versions of the "same" module to exist in a web application, with some parts of the module graph importing one version, and other parts importing another version.

Scopes can overlap each other, and overlap the global "imports" specifier map. At resolution time, scopes are consulted in order of most- to least-specific, where specificity is measured by sorting the scopes using the code unit less than operation. So, for example, "/scope2/scope3/" is treated as more specific than "/scope2/", which is treated as more specific than the top-level (unscoped) mappings.

The following import map illustrates this:

{
  "imports": {
    "a": "/a-1.mjs",
    "b": "/b-1.mjs",
    "c": "/c-1.mjs"
  },
  "scopes": {
    "/scope2/": {
      "a": "/a-2.mjs"
    },
    "/scope2/scope3/": {
      "b": "/b-3.mjs"
    }
  }
}

This results in the following resolutions (using relative URLs for brevity):

	Specifier
"a"	"b"	"c"
Referrer	/scope1/r.mjs	/a-1.mjs	/b-1.mjs	/c-1.mjs
/scope2/r.mjs	/a-2.mjs	/b-1.mjs	/c-1.mjs
/scope2/scope3/r.mjs	/a-2.mjs	/b-3.mjs	/c-1.mjs

Import maps can also be used to provide modules with integrity metadata to be used in Subresource Integrity checks. [SRI]

The following import map illustrates this:

{
  "imports": {
    "a": "/a-1.mjs",
    "b": "/b-1.mjs",
    "c": "/c-1.mjs"
  },
  "integrity": {
    "/a-1.mjs": "sha384-Li9vy3DqF8tnTXuiaAJuML3ky+er10rcgNR/VqsVpcw+ThHmYcwiB1pbOxEbzJr7",
    "/d-1.mjs": "sha384-MBO5IDfYaE6c6Aao94oZrIOiC6CGiSN2n4QUbHNPhzk5Xhm0djZLQqTpL0HzTUxk"
  }
}

The above example provides integrity metadata to be enforced on the modules /a-1.mjs and /d-1.mjs, even if the latter is not defined as an import in the map.

The child text content of a script element representing an import map must match the following import map authoring requirements:

It must be valid JSON. [JSON]

The JSON must represent a JSON object, with at most the three keys "imports", "scopes", and "integrity".

The values corresponding to the "imports", "scopes", and "integrity" keys, if present, must themselves be JSON objects.

The value corresponding to the "imports" key, if present, must be a valid module specifier map.

The value corresponding to the "scopes" key, if present, must be a JSON object, whose keys are valid URL strings and whose values are valid module specifier maps.

The value corresponding to the "integrity" key, if present, must be a JSON object, whose keys are valid URL strings and whose values fit the requirements of the integrity attribute.

A valid module specifier map is a JSON object that meets the following requirements:

All of its keys must be nonempty.

All of its values must be strings.

Each value must be either a valid absolute URL or a valid URL string that starts with "/", "./", or "../".

If a given key ends with "/", then the corresponding value must also.

8.1.5.3 Import map processing model

Formally, an import map is a struct with three items:

imports, a module specifier map;

scopes, an ordered map of URLs to module specifier maps; and

integrity, a module integrity map.

A module specifier map is an ordered map whose keys are strings and whose values are either URLs or nulls.

A module integrity map is an ordered map whose keys are URLs and whose values are strings that will be used as integrity metadata.

An empty import map is an import map with its imports and scopes both being empty maps.

A specifier resolution record is a struct. It has the following items:

A serialized base URL
A string-or-null that represents the base URL of the specifier, when one exists.
A specifier
A string representing the specifier.
A specifier as a URL
A URL-or-null that represents the URL in case of a URL-like module specifier.

Implementations can replace specifier as a URL with a boolean that indicates that the specifier is either bare or URL-like that is special.

To add module to resolved module set given an environment settings object settingsObject, a string serializedBaseURL, a string normalizedSpecifier, and a URL-or-null asURL:

Let global be settingsObject's global object.

If global does not implement Window, then return.

Let record be a new specifier resolution record, with serialized base URL set to serializedBaseURL, specifier set to normalizedSpecifier, and specifier as a URL set to asURL.

Append record to global's resolved module set.

To parse an import map string, given a string input and a URL baseURL:

Let parsed be the result of parsing a JSON string to an Infra value given input.

If parsed is not an ordered map, then throw a TypeError indicating that the top-level value needs to be a JSON object.

Let sortedAndNormalizedImports be an empty ordered map.

If parsed["imports"] exists, then:

If parsed["imports"] is not an ordered map, then throw a TypeError indicating that the value for the "imports" top-level key needs to be a JSON object.

Set sortedAndNormalizedImports to the result of sorting and normalizing a module specifier map given parsed["imports"] and baseURL.

Let sortedAndNormalizedScopes be an empty ordered map.

If parsed["scopes"] exists, then:

If parsed["scopes"] is not an ordered map, then throw a TypeError indicating that the value for the "scopes" top-level key needs to be a JSON object.

Set sortedAndNormalizedScopes to the result of sorting and normalizing scopes given parsed["scopes"] and baseURL.

Let normalizedIntegrity be an empty ordered map.

If parsed["integrity"] exists, then:

If parsed["integrity"] is not an ordered map, then throw a TypeError indicating that the value for the "integrity" top-level key needs to be a JSON object.

Set normalizedIntegrity to the result of normalizing a module integrity map given parsed["integrity"] and baseURL.

If parsed's keys contains any items besides "imports", "scopes", or "integrity", then the user agent should report a warning to the console indicating that an invalid top-level key was present in the import map.

This can help detect typos. It is not an error, because that would prevent any future extensions from being added backward-compatibly.

Return an import map whose imports are sortedAndNormalizedImports, whose scopes are sortedAndNormalizedScopes, and whose integrity are normalizedIntegrity.

The import map that results from this parsing algorithm is highly normalized. For example, given a base URL of https://example.com/base/page.html, the input

{
  "imports": {
    "/app/helper": "node_modules/helper/index.mjs",
    "lodash": "/node_modules/lodash-es/lodash.js"
  }
}

will generate an import map with imports of

«[
  "https://example.com/app/helper" → https://example.com/base/node_modules/helper/index.mjs
  "lodash" → https://example.com/node_modules/lodash-es/lodash.js
]»

and (despite nothing being present in the input string) an empty ordered map for its scopes.

To merge module specifier maps, given a module specifier map newMap and a module specifier map oldMap:

Let mergedMap be a deep copy of oldMap.

For each specifier → url of newMap:

If specifier exists in oldMap, then:

The user agent may report a warning to the console indicating the ignored rule. They may choose to avoid reporting if the rule is identical to an existing one.

Continue.

Set mergedMap[specifier] to url.

Return mergedMap.

To merge existing and new import maps, given a global object global and an import map newImportMap:

Let newImportMapScopes be a deep copy of newImportMap's scopes.

We're mutating these copies and removing items from them when they are used to ignore scope-specific rules. This is true for newImportMapScopes, as well as to newImportMapImports below.

Let oldImportMap be global's import map.

Let newImportMapImports be a deep copy of newImportMap's imports.

For each scopePrefix → scopeImports of newImportMapScopes:

For each record of global's resolved module set:

If scopePrefix is record's serialized base URL, or if scopePrefix ends with U+002F (/) and scopePrefix is a code unit prefix of record's serialized base URL, then:

For each specifierKey → resolutionResult of scopeImports:

If specifierKey is record's specifier, or if all of the following conditions are true:

specifierKey ends with U+002F (/);

specifierKey is a code unit prefix of record's specifier;

either record's specifier as a URL is null or is special,

then:

The user agent may report a warning to the console indicating the ignored rule. They may choose to avoid reporting if the rule is identical to an existing one.

Remove scopeImports[specifierKey].

Implementers are encouraged to implement a more efficient matching algorithm when working with the resolved module set. As guidance, the number of resolved/mapped modules in a large application can be on the order of thousands.

If scopePrefix exists in oldImportMap's scopes, then set oldImportMap's scopes[scopePrefix] to the result of merging module specifier maps, given scopeImports and oldImportMap's scopes[scopePrefix].

Otherwise, set oldImportMap's scopes[scopePrefix] to scopeImports.

For each url → integrity of newImportMap's integrity:

If url exists in oldImportMap's integrity, then:

The user agent may report a warning to the console indicating the ignored rule. They may choose to avoid reporting if the rule is identical to an existing one.

Continue.

Set oldImportMap's integrity[url] to integrity.

For each record of global's resolved module set:

For each specifier → url of newImportMapImports:

If specifier starts with record's specifier, then:

The user agent may report a warning to the console indicating the ignored rule. They may choose to avoid reporting if the rule is identical to an existing one.

Remove newImportMapImports[specifier].

Set oldImportMap's imports to the result of merge module specifier maps, given newImportMapImports and oldImportMap's imports.

The above algorithm merges a new import map into the given environment settings object's global object's import map. Let's examine a few examples:

There are two cases when rules of the new import map don't get merged into the existing one.

The new import map rule has the exact same scope and specifier as a rule in the existing import map. We'll call that "conflicting rule".

The new import map rule may impact the resolution of an already resolved module. We'll call that "impacted already resolved module".

When the new import map has no conflicting rules, and there are no impacted resolved modules, the resulting map would be a combination of the new and existing maps. Rules that would have individually impacted similar modules (e.g. "/app/" and "/app/helper") but are not an exact match are not conflicting, and all make it to the merged map.

So, the following existing and new import maps:

{
   "imports": {
    "/app/": "./original-app/",
  }
}
{
  "imports": {
    "/app/helper": "./helper/index.mjs"
  },
  "scopes": {
    "/js": {
      "/app/": "./js-app/"
    }
  }
}

Would be equivalent to the following single import map:

{
  "imports": {
    "/app/": "./original-app/",
    "/app/helper": "./helper/index.mjs"
  },
  "scopes": {
    "/js": {
      "/app/": "./js-app/"
    }
  }
}

When the new import map impacts an already resolved module, that rule gets dropped from the import map.

So, if the resolved module set already contains the "/app/helper", the following new import map:

{
   "imports": {
    "/app/helper": "./helper/index.mjs",
    "lodash": "/node_modules/lodash-es/lodash.js"
  }
}

Would be equivalent to the following one:

{
  "imports": {
    "lodash": "/node_modules/lodash-es/lodash.js"
  }
}

The same is true for rules that impact already resolved modules defined in specific scopes. If we already resolved "/app/helper" from "/app/main.mjs" the following new import map:

{
  "scopes": {
    "/app/": {
      "/app/helper": "./helper/index.mjs"
    }
  },
   "imports": {
    "lodash": "/node_modules/lodash-es/lodash.js"
  }
}

Would similarly be equivalent to:

{
  "imports": {
    "lodash": "/node_modules/lodash-es/lodash.js"
  }
}

We could also have cases where a single already-resolved module specifier has multiple rules for its resolution, depending on the referring script. In such cases, only the relevant rules would not be added to the map.

For example, if we already resolved "/app/helper" from "/app/vendor/main.mjs", the following new import map:

{
  "scopes": {
    "/app/": {
      "/app/helper": "./helper/index.mjs"
    },
    "/app/vendor/": {
      "/app/": "./vendor_helper/"
    },
    "/vendor/": {
      "/app/helper": "./helper/vendor_index.mjs"
    }
  },
   "imports": {
    "lodash": "/node_modules/lodash-es/lodash.js"
    "/app/": "./general_app_path/"
    "/app/helper": "./other_path/helper/index.mjs"
  }
}

Would be equivalent to:

{
  "scopes": {
    "/vendor/": {
      "/app/helper": "./helper/vendor_index.mjs"
    }
  },
  "imports": {
    "lodash": "/node_modules/lodash-es/lodash.js"
  }
}

This is achieved by the fact that the merge algorithm tracks already resolved modules and removes rules affecting them from new import maps before they are merged into the existing one.

When the new import map has conflicting rules to the existing import map, with no impacted already resolved modules, the existing import map rules persist.

For example, the following existing and new import maps:

{
   "imports": {
    "/app/helper": "./helper/index.mjs",
    "lodash": "/node_modules/lodash-es/lodash.js"
  }
}
{
  "imports": {
    "/app/helper": "./main/helper/index.mjs"
  }
}

Would be equivalent to the following single import map:

{
  "imports": {
    "/app/helper": "./helper/index.mjs",
    "lodash": "/node_modules/lodash-es/lodash.js",
  }
}

To sort and normalize a module specifier map, given an ordered map originalMap and a URL baseURL:

Let normalized be an empty ordered map.

For each specifierKey → value of originalMap:

Let normalizedSpecifierKey be the result of normalizing a specifier key given specifierKey and baseURL.

If normalizedSpecifierKey is null, then continue.

If value is not a string, then:

The user agent may report a warning to the console indicating that addresses need to be strings.

Set normalized[normalizedSpecifierKey] to null.

Continue.

Let addressURL be the result of resolving a URL-like module specifier given value and baseURL.

If addressURL is null, then:

The user agent may report a warning to the console indicating that the address was invalid.

Set normalized[normalizedSpecifierKey] to null.

Continue.

If specifierKey ends with U+002F (/), and the serialization of addressURL does not end with U+002F (/), then:

The user agent may report a warning to the console indicating that an invalid address was given for the specifier key specifierKey; since specifierKey ends with a slash, the address needs to as well.

Set normalized[normalizedSpecifierKey] to null.

Continue.

Set normalized[normalizedSpecifierKey] to addressURL.

Return the result of sorting in descending order normalized, with an entry a being less than an entry b if a's key is code unit less than b's key.

To sort and normalize scopes, given an ordered map originalMap and a URL baseURL:

Let normalized be an empty ordered map.

For each scopePrefix → potentialSpecifierMap of originalMap:

If potentialSpecifierMap is not an ordered map, then throw a TypeError indicating that the value of the scope with prefix scopePrefix needs to be a JSON object.

Let scopePrefixURL be the result of URL parsing scopePrefix with baseURL.

If scopePrefixURL is failure, then:

The user agent may report a warning to the console that the scope prefix URL was not parseable.

Continue.

Let normalizedScopePrefix be the serialization of scopePrefixURL.

Set normalized[normalizedScopePrefix] to the result of sorting and normalizing a module specifier map given potentialSpecifierMap and baseURL.

Return the result of sorting in descending order normalized, with an entry a being less than an entry b if a's key is code unit less than b's key.

In the above two algorithms, sorting keys and scopes in descending order has the effect of putting "foo/bar/" before "foo/". This in turn gives "foo/bar/" a higher priority than "foo/" during module specifier resolution.

To normalize a module integrity map, given an ordered map originalMap:

Let normalized be an empty ordered map.

For each key → value of originalMap:

Let resolvedURL be the result of resolving a URL-like module specifier given key and baseURL.

Unlike "imports", keys of the integrity map are treated as URLs, not module specifiers. However, we use the resolve a URL-like module specifier algorithm to prohibit "bare" relative URLs like foo, which could be mistaken for module specifiers.

If resolvedURL is null, then:

The user agent may report a warning to the console indicating that the key failed to resolve.

Continue.

If value is not a string, then:

The user agent may report a warning to the console indicating that integrity metadata values need to be strings.

Continue.

Set normalized[resolvedURL] to value.

Return normalized.

To normalize a specifier key, given a string specifierKey and a URL baseURL:

If specifierKey is the empty string, then:

The user agent may report a warning to the console indicating that specifier keys may not be the empty string.

Return null.

Let url be the result of resolving a URL-like module specifier, given specifierKey and baseURL.

If url is not null, then return the serialization of url.

Return specifierKey.

8.1.6 JavaScript specification host hooks

The JavaScript specification contains a number of implementation-defined abstract operations, that vary depending on the host environment. This section defines them for user agent hosts.

8.1.6.1 HostEnsureCanAddPrivateElement(O)

JavaScript contains an implementation-defined HostEnsureCanAddPrivateElement(O) abstract operation. User agents must use the following implementation: [JAVASCRIPT]

If O is a WindowProxy object, or implements Location, then return ThrowCompletion(a new TypeError).

Return NormalCompletion(unused).

JavaScript private fields can be applied to arbitrary objects. Since this can dramatically complicate implementation for particularly-exotic host objects, the JavaScript language specification provides this hook to allow hosts to reject private fields on objects meeting a host-defined criteria. In the case of HTML, WindowProxy and Location have complicated semantics — particularly around navigation and security — that make implementation of private field semantics challenging, so our implementation simply rejects those objects.

8.1.6.2 HostEnsureCanCompileStrings(realm, parameterStrings, bodyString, codeString, compilationType, parameterArgs, bodyArg)

JavaScript contains an implementation-defined HostEnsureCanCompileStrings abstract operation, redefined by the Dynamic Code Brand Checks proposal. User agents must use the following implementation: [JAVASCRIPT] [JSDYNAMICCODEBRANDCHECKS]

Perform ? EnsureCSPDoesNotBlockStringCompilation(realm, parameterStrings, bodyString, codeString, compilationType, parameterArgs, bodyArg). [CSP]

8.1.6.3 HostGetCodeForEval(argument)

The Dynamic Code Brand Checks proposal contains an implementation-defined HostGetCodeForEval(argument) abstract operation. User agents must use the following implementation: [JSDYNAMICCODEBRANDCHECKS]

If argument is a TrustedScript object, then return argument's data.

Otherwise, return no-code.

8.1.6.4 HostPromiseRejectionTracker(promise, operation)

JavaScript contains an implementation-defined HostPromiseRejectionTracker(promise, operation) abstract operation. User agents must use the following implementation: [JAVASCRIPT]

Let script be the running script.

If script is a classic script and script's muted errors is true, then return.

Let settingsObject be the current settings object.

If script is not null, then set settingsObject to script's settings object.

Let global be settingsObject's global object.

If operation is "reject", then:

Append promise to global's about-to-be-notified rejected promises list.

If operation is "handle", then:

If global's about-to-be-notified rejected promises list contains promise, then remove promise from that list and return.

If global's outstanding rejected promises weak set does not contain promise, then return.

Remove promise from global's outstanding rejected promises weak set.

Queue a global task on the DOM manipulation task source given global to fire an event named rejectionhandled at global, using PromiseRejectionEvent, with the promise attribute initialized to promise, and the reason attribute initialized to promise.[[PromiseResult]].

8.1.6.5 HostSystemUTCEpochNanoseconds(global)

The Temporal proposal contains an implementation-defined HostSystemUTCEpochNanoseconds abstract operation. User agents must use the following implementation: [JSTEMPORAL]

Let settingsObject be global's relevant settings object.

Let time be settingsObject's current wall time.

Let ns be the number of nanoseconds from the Unix epoch to time, rounded to the nearest integer.

Return the result of clamping ns between nsMinInstant and nsMaxInstant.

8.1.6.6 Job-related host hooks
⚠MDN

The JavaScript specification defines Jobs to be scheduled and run later by the host, as well as JobCallback Records which encapsulate JavaScript functions that are called as part of jobs. The JavaScript specification contains a number of implementation-defined abstract operations that lets the host define how jobs are scheduled and how JobCallbacks are handled. HTML uses these abstract operations to track the incumbent settings object in promises and FinalizationRegistry callbacks by saving and restoring the incumbent settings object and a JavaScript execution context for the active script in JobCallbacks. This section defines them for user agent hosts.

8.1.6.6.1 HostCallJobCallback(callback, V, argumentsList)

JavaScript contains an implementation-defined HostCallJobCallback(callback, V, argumentsList) abstract operation to let hosts restore state when invoking JavaScript callbacks from inside tasks. User agents must use the following implementation: [JAVASCRIPT]

Let incumbent settings be callback.[[HostDefined]].[[IncumbentSettings]].

Let script execution context be callback.[[HostDefined]].[[ActiveScriptContext]].

Prepare to run a callback with incumbent settings.

This affects the incumbent concept while the callback runs.

If script execution context is not null, then push script execution context onto the JavaScript execution context stack.

This affects the active script while the callback runs.

Let result be Call(callback.[[Callback]], V, argumentsList).

If script execution context is not null, then pop script execution context from the JavaScript execution context stack.

Clean up after running a callback with incumbent settings.

Return result.

8.1.6.6.2 HostEnqueueFinalizationRegistryCleanupJob(finalizationRegistry)

JavaScript has the ability to register objects with FinalizationRegistry objects, in order to schedule a cleanup action if they are found to be garbage collected. The JavaScript specification contains an implementation-defined HostEnqueueFinalizationRegistryCleanupJob(finalizationRegistry) abstract operation to schedule the cleanup action.

The timing and occurrence of cleanup work is implementation-defined in the JavaScript specification. User agents might differ in when and whether an object is garbage collected, affecting both whether the return value of the WeakRef.prototype.deref() method is undefined, and whether FinalizationRegistry cleanup callbacks occur. There are well-known cases in popular web browsers where objects are not accessible to JavaScript, but they remain retained by the garbage collector indefinitely. HTML clears kept-alive WeakRef objects in the perform a microtask checkpoint algorithm. Authors would be best off not depending on the timing details of garbage collection implementations.

Cleanup actions do not take place interspersed with synchronous JavaScript execution, but rather happen in queued tasks. User agents must use the following implementation: [JAVASCRIPT]

Let global be finalizationRegistry.[[Realm]]'s global object.

Queue a global task on the JavaScript engine task source given global to perform the following steps:

Let entry be finalizationRegistry.[[CleanupCallback]].[[Callback]].[[Realm]]'s environment settings object.

Prepare to run script with entry.

This affects the entry concept while the cleanup callback runs.

Let result be the result of performing CleanupFinalizationRegistry(finalizationRegistry).

Clean up after running script with entry.

If result is an abrupt completion, then report an exception given by result.[[Value]] for global.

8.1.6.6.3 HostEnqueueGenericJob(job, realm)

JavaScript contains an implementation-defined HostEnqueueGenericJob(job, realm) abstract operation to perform generic jobs in a particular realm (e.g., resolve promises resulting from Atomics.waitAsync). User agents must use the following implementation: [JAVASCRIPT]

Let global be realm's global object.

Queue a global task on the JavaScript engine task source given global to perform job().

8.1.6.6.4 HostEnqueuePromiseJob(job, realm)

JavaScript contains an implementation-defined HostEnqueuePromiseJob(job, realm) abstract operation to schedule Promise-related operations. HTML schedules these operations in the microtask queue. User agents must use the following implementation: [JAVASCRIPT]

If realm is not null, then let job settings be the settings object for realm. Otherwise, let job settings be null.

If realm is not null, it is the realm of the author code that will run. When job is returned by NewPromiseReactionJob, it is the realm of the promise's handler function. When job is returned by NewPromiseResolveThenableJob, it is the realm of the then function.

If realm is null, either no author code will run or author code is guaranteed to throw. For the former, the author may not have passed in code to run, such as in promise.then(null, null). For the latter, it is because a revoked Proxy was passed. In both cases, all the steps below that would otherwise use job settings get skipped.

NewPromiseResolveThenableJob and NewPromiseReactionJob both seem to provide non-null realms (the current Realm Record) in the case of a revoked proxy. The previous text could be updated to reflect that.

Queue a microtask to perform the following steps:

If job settings is not null, then prepare to run script with job settings.

This affects the entry concept while the job runs.

Let result be job().

job is an abstract closure returned by NewPromiseReactionJob or NewPromiseResolveThenableJob. The promise's handler function when job is returned by NewPromiseReactionJob, and the then function when job is returned by NewPromiseResolveThenableJob, are wrapped in JobCallback Records. HTML saves the incumbent settings object and a JavaScript execution context for to the active script in HostMakeJobCallback and restores them in HostCallJobCallback.

If job settings is not null, then clean up after running script with job settings.

If result is an abrupt completion, then report an exception given by result.[[Value]] for realm's global object.

There is a very gnarly case where HostEnqueuePromiseJob is called with a null realm (e.g., because Promise.prototype.then was called with null handlers) but also the job returns abruptly (because the promise capability's resolve or reject handler threw, possibly because this is a subclass of Promise that takes the supplied functions and wraps them in throwing functions before passing them on to the function passed to the Promise superclass constructor). Which global is to be used then, considering that the current realm could be different at each of those steps, by using a Promise constructor or Promise.prototype.then from another realm? See issue #10526.

8.1.6.6.5 HostEnqueueTimeoutJob(job, realm, milliseconds)

JavaScript contains an implementation-defined HostEnqueueTimeoutJob(job, milliseconds) abstract operation to schedule an operation to be performed after a timeout. HTML schedules these operations using run steps after a timeout. User agents must use the following implementation: [JAVASCRIPT]

Let global be realm's global object.

Let timeoutStep be an algorithm step which queues a global task on the JavaScript engine task source given global to perform job().

Run steps after a timeout given global, "JavaScript", milliseconds, and timeoutStep.

8.1.6.6.6 HostMakeJobCallback(callable)

JavaScript contains an implementation-defined HostMakeJobCallback(callable) abstract operation to let hosts attach state to JavaScript callbacks that are called from inside tasks. User agents must use the following implementation: [JAVASCRIPT]

Let incumbent settings be the incumbent settings object.

Let active script be the active script.

Let script execution context be null.

If active script is not null, set script execution context to a new JavaScript execution context, with its Function field set to null, its Realm field set to active script's settings object's realm, and its ScriptOrModule set to active script's record.

As seen below, this is used in order to propagate the current active script forward to the time when the job callback is invoked.

A case where active script is non-null, and saving it in this way is useful, is the following:

Promise.resolve('import(`./example.mjs`)').then(eval);

Without this step (and the steps that use it in HostCallJobCallback), there would be no active script when the import() expression is evaluated, since eval() is a built-in function that does not originate from any particular script.

With this step in place, the active script is propagated from the above code into the job, allowing import() to use the original script's base URL appropriately.

active script can be null if the user clicks on the following button:

<button onclick="Promise.resolve('import(`./example.mjs`)').then(eval)">Click me</button>

In this case, the JavaScript function for the event handler will be created by the get the current value of the event handler algorithm, which creates a function with null [[ScriptOrModule]] value. Thus, when the promise machinery calls HostMakeJobCallback, there will be no active script to pass along.

As a consequence, this means that when the import() expression is evaluated, there will still be no active script. Fortunately that is handled by our implementation of HostLoadImportedModule by falling back to using the current settings object's API base URL.

Return the JobCallback Record { [[Callback]]: callable, [[HostDefined]]: { [[IncumbentSettings]]: incumbent settings, [[ActiveScriptContext]]: script execution context } }.

8.1.6.7 Module-related host hooks

The JavaScript specification defines a syntax for modules, as well as some host-agnostic parts of their processing model. This specification defines the rest of their processing model: how the module system is bootstrapped, via the script element with type attribute set to "module", and how modules are fetched, resolved, and executed. [JAVASCRIPT]

Although the JavaScript specification speaks in terms of "scripts" versus "modules", in general this specification speaks in terms of classic scripts versus module scripts, since both of them use the script element.

modulePromise = import(specifier)

Returns a promise for the module namespace object for the module script identified by specifier. This allows dynamic importing of module scripts at runtime, instead of statically using the import statement form. The specifier will be resolved relative to the active script.

The returned promise will be rejected if an invalid specifier is given, or if a failure is encountered while fetching or evaluating the resulting module graph.

This syntax can be used inside both classic and module scripts. It thus provides a bridge into the module-script world, from the classic-script world.

url = import.meta.url

Returns the active module script's base URL.

This syntax can only be used inside module scripts.

url = import.meta.resolve(specifier)

Returns specifier, resolved relative to the active script. That is, this returns the URL that would be imported by using import(specifier).

Throws a TypeError exception if an invalid specifier is given.

This syntax can only be used inside module scripts.

A module map is a map keyed by tuples consisting of a URL record and a string. The URL record is the request URL at which the module was fetched, and the string indicates the type of the module (e.g. "javascript-or-wasm"). The module map's values are either a module script, null (used to represent failed fetches), or a placeholder value "fetching". Module maps are used to ensure that imported module scripts are only fetched, parsed, and evaluated once per Document or worker.

Since module maps are keyed by (URL, module type), the following code will create three separate entries in the module map, since it results in three different (URL, module type) tuples (all with "javascript-or-wasm" type):

import "https://example.com/module.mjs";
import "https://example.com/module.mjs#map-buster";
import "https://example.com/module.mjs?debug=true";

That is, URL queries and fragments can be varied to create distinct entries in the module map; they are not ignored. Thus, three separate fetches and three separate module evaluations will be performed.

In contrast, the following code would only create a single entry in the module map, since after applying the URL parser to these inputs, the resulting URL records are equal:

import "https://example.com/module2.mjs";
import "https:example.com/module2.mjs";
import "https://///example.com\\module2.mjs";
import "https://example.com/foo/../module2.mjs";

So in this second example, only one fetch and one module evaluation will occur.

Note that this behavior is the same as how shared workers are keyed by their parsed constructor URL.

Since module type is also part of the module map key, the following code will create two separate entries in the module map (the type is "javascript-or-wasm" for the first, and "css" for the second):

<script type=module>
  import "https://example.com/module";
</script>
<script type=module>
  import "https://example.com/module" with { type: "css" };
</script>

This can result in two separate fetches and two separate module evaluations being performed.

In practice, due to the as-yet-unspecified memory cache (see issue #6110) the resource may only be fetched once in WebKit and Blink-based browsers. Additionally, as long as all module types are mutually exclusive, the module type check in fetch a single module script will fail for at least one of the imports, so at most one module evaluation will occur.

The purpose of including the type in the module map key is so that an import with the wrong type attribute does not prevent a different import of the same specifier but with the correct type from succeeding.

JavaScript module scripts are the default import type when importing from another JavaScript module; that is, when an import statement lacks a type import attribute the imported module script's type will be JavaScript. Attempting to import a JavaScript resource using an import statement with a type import attribute will fail:

<script type="module">
    // All of the following will fail, assuming that the imported .mjs files are served with a
    // JavaScript MIME type. JavaScript module scripts are the default and cannot be imported with
    // any import type attribute.
    import foo from "./foo.mjs" with { type: "javascript" };
    import foo2 from "./foo2.mjs" with { type: "js" };
    import foo3 from "./foo3.mjs" with { type: "" };
    await import("./foo4.mjs", { with: { type: null } });
    await import("./foo5.mjs", { with: { type: undefined } });
</script>
8.1.6.7.1 HostGetImportMetaProperties(moduleRecord)
✔MDN

JavaScript contains an implementation-defined HostGetImportMetaProperties abstract operation. User agents must use the following implementation: [JAVASCRIPT]

Let moduleScript be moduleRecord.[[HostDefined]].

Assert: moduleScript's base URL is not null, as moduleScript is a JavaScript module script.

Let urlString be moduleScript's base URL, serialized.

Let steps be the following steps, given the argument specifier:

Set specifier to ? ToString(specifier).

Let url be the result of resolving a module specifier given moduleScript and specifier.

Return the serialization of url.

Let resolveFunction be ! CreateBuiltinFunction(steps, 1, "resolve", « »).

Return « Record { [[Key]]: "url", [[Value]]: urlString }, Record { [[Key]]: "resolve", [[Value]]: resolveFunction } ».

8.1.6.7.2 HostGetSupportedImportAttributes()

JavaScript contains an implementation-defined HostGetSupportedImportAttributes abstract operation. User agents must use the following implementation: [JAVASCRIPT]

Return « "type" ».

8.1.6.7.3 HostLoadImportedModule(referrer, moduleRequest, loadState, payload)

JavaScript contains an implementation-defined HostLoadImportedModule abstract operation. User agents must use the following implementation: [JAVASCRIPT]

Let settingsObject be the current settings object.

If settingsObject's global object implements WorkletGlobalScope or ServiceWorkerGlobalScope and loadState is undefined, then:

loadState is undefined when the current fetching process has been initiated by a dynamic import() call, either directly or when loading the transitive dependencies of the dynamically imported module.

Perform FinishLoadingImportedModule(referrer, moduleRequest, payload, ThrowCompletion(a new TypeError)).

Return.

Let referencingScript be null.

Let originalFetchOptions be the default script fetch options.

Let fetchReferrer be "client".

If referrer is a Script Record or a Cyclic Module Record, then:

Set referencingScript to referrer.[[HostDefined]].

Set settingsObject to referencingScript's settings object.

Set fetchReferrer to referencingScript's base URL.

Set originalFetchOptions to referencingScript's fetch options.

referrer is usually a Script Record or a Cyclic Module Record, but it will not be so for event handlers per the get the current value of the event handler algorithm. For example, given:

<button onclick="import('./foo.mjs')">Click me</button>

If a click event occurs, then at the time the import() expression runs, GetActiveScriptOrModule will return null, and this operation will receive the current realm as a fallback referrer.

If referrer is a Cyclic Module Record and moduleRequest is equal to the first element of referrer.[[RequestedModules]], then:

For each ModuleRequest record requested of referrer.[[RequestedModules]]:

If requested.[[Attributes]] contains a Record entry such that entry.[[Key]] is not "type", then:

Let error be a new SyntaxError exception.

If loadState is not undefined and loadState.[[ErrorToRethrow]] is null, set loadState.[[ErrorToRethrow]] to error.

Perform FinishLoadingImportedModule(referrer, moduleRequest, payload, ThrowCompletion(error)).

Return.

The JavaScript specification re-performs this validation but it is duplicated here to avoid unnecessarily loading any of the dependencies on validation failure.

Resolve a module specifier given referencingScript and requested.[[Specifier]], catching any exceptions. If they throw an exception, let resolutionError be the thrown exception.

If the previous step threw an exception, then:

If loadState is not undefined and loadState.[[ErrorToRethrow]] is null, set loadState.[[ErrorToRethrow]] to resolutionError.

Perform FinishLoadingImportedModule(referrer, moduleRequest, payload, ThrowCompletion(resolutionError)).

Return.

Let moduleType be the result of running the module type from module request steps given requested.

If the result of running the module type allowed steps given moduleType and settingsObject is false, then:

Let error be a new TypeError exception.

If loadState is not undefined and loadState.[[ErrorToRethrow]] is null, set loadState.[[ErrorToRethrow]] to error.

Perform FinishLoadingImportedModule(referrer, moduleRequest, payload, ThrowCompletion(error)).

Return.

This step is essentially validating all of the requested module specifiers and type attributes when the first call to HostLoadImportedModule for a static module dependency list is made, to avoid further loading operations in the case any one of the dependencies has a static error. We treat a module with unresolvable module specifiers or unsupported type attributes the same as one that cannot be parsed; in both cases, a syntactic issue makes it impossible to ever contemplate linking the module later.

Let url be the result of resolving a module specifier given referencingScript and moduleRequest.[[Specifier]], catching any exceptions. If they throw an exception, let resolutionError be the thrown exception.

If the previous step threw an exception, then:

If loadState is not undefined and loadState.[[ErrorToRethrow]] is null, set loadState.[[ErrorToRethrow]] to resolutionError.

Perform FinishLoadingImportedModule(referrer, moduleRequest, payload, ThrowCompletion(resolutionError)).

Return.

Let fetchOptions be the result of getting the descendant script fetch options given originalFetchOptions, url, and settingsObject.

Let destination be "script".

Let fetchClient be settingsObject.

If loadState is not undefined, then:

Set destination to loadState.[[Destination]].

Set fetchClient to loadState.[[FetchClient]].

Fetch a single imported module script given url, fetchClient, destination, fetchOptions, settingsObject, fetchReferrer, moduleRequest, and onSingleFetchComplete as defined below. If loadState is not undefined and loadState.[[PerformFetch]] is not null, pass loadState.[[PerformFetch]] along as well.

onSingleFetchComplete given moduleScript is the following algorithm:

Let completion be null.

If moduleScript is null, then set completion to ThrowCompletion(a new TypeError).

Otherwise, if moduleScript's parse error is not null, then:

Let parseError be moduleScript's parse error.

Set completion to ThrowCompletion(parseError).

If loadState is not undefined and loadState.[[ErrorToRethrow]] is null, set loadState.[[ErrorToRethrow]] to parseError.

Otherwise, set completion to NormalCompletion(moduleScript's record).

Perform FinishLoadingImportedModule(referrer, moduleRequest, payload, completion).

8.1.7 Event loops
8.1.7.1 Definitions

To coordinate events, user interaction, scripts, rendering, networking, and so forth, user agents must use event loops as described in this section. Each agent has an associated event loop, which is unique to that agent.

The event loop of a similar-origin window agent is known as a window event loop. The event loop of a dedicated worker agent, shared worker agent, or service worker agent is known as a worker event loop. And the event loop of a worklet agent is known as a worklet event loop.

Event loops do not necessarily correspond to implementation threads. For example, multiple window event loops could be cooperatively scheduled in a single thread.

However, for the various worker agents that are allocated with [[CanBlock]] set to true, the JavaScript specification does place requirements on them regarding forward progress, which effectively amount to requiring dedicated per-agent threads in those cases.

An event loop has one or more task queues. A task queue is a set of tasks.

Task queues are sets, not queues, because the event loop processing model grabs the first runnable task from the chosen queue, instead of dequeuing the first task.

The microtask queue is not a task queue.

Tasks encapsulate algorithms that are responsible for such work as:

Events

Dispatching an Event object at a particular EventTarget object is often done by a dedicated task.

Not all events are dispatched using the task queue; many are dispatched during other tasks.

Parsing

The HTML parser tokenizing one or more bytes, and then processing any resulting tokens, is typically a task.

Callbacks

Calling a callback is often done by a dedicated task.

Using a resource

When an algorithm fetches a resource, if the fetching occurs in a non-blocking fashion then the processing of the resource once some or all of the resource is available is performed by a task.

Reacting to DOM manipulation

Some elements have tasks that trigger in response to DOM manipulation, e.g. when that element is inserted into the document.

Formally, a task is a struct which has:

Steps
A series of steps specifying the work to be done by the task.
A source
One of the task sources, used to group and serialize related tasks.
A document
A Document associated with the task, or null for tasks that are not in a window event loop.
A script evaluation environment settings object set
A set of environment settings objects used for tracking script evaluation during the task.

A task is runnable if its document is either null or fully active.

Per its source field, each task is defined as coming from a specific task source. For each event loop, every task source must be associated with a specific task queue.

Essentially, task sources are used within standards to separate logically-different types of tasks, which a user agent might wish to distinguish between. Task queues are used by user agents to coalesce task sources within a given event loop.

For example, a user agent could have one task queue for mouse and key events (to which the user interaction task source is associated), and another to which all other task sources are associated. Then, using the freedom granted in the initial step of the event loop processing model, it could give keyboard and mouse events preference over other tasks three-quarters of the time, keeping the interface responsive but not starving other task queues. Note that in this setup, the processing model still enforces that the user agent would never process events from any one task source out of order.

Each event loop has a currently running task, which is either a task or null. Initially, this is null. It is used to handle reentrancy.

Each event loop has a microtask queue, which is a queue of microtasks, initially empty. A microtask is a colloquial way of referring to a task that was created via the queue a microtask algorithm.

Each event loop has a performing a microtask checkpoint boolean, which is initially false. It is used to prevent reentrant invocation of the perform a microtask checkpoint algorithm.

Each window event loop has a DOMHighResTimeStamp last render opportunity time, initially set to zero.

Each window event loop has a DOMHighResTimeStamp last idle period start time, initially set to zero.

To get the same-loop windows for a window event loop loop, return all Window objects whose relevant agent's event loop is loop.

8.1.7.2 Queuing tasks

To queue a task on a task source source, which performs a series of steps steps, optionally given an event loop event loop and a document document:

If event loop was not given, set event loop to the implied event loop.

If document was not given, set document to the implied document.

Let task be a new task.

Set task's steps to steps.

Set task's source to source.

Set task's document to the document.

Set task's script evaluation environment settings object set to an empty set.

Let queue be the task queue to which source is associated on event loop.

Append task to queue.

Failing to pass an event loop and document to queue a task means relying on the ambiguous and poorly-specified implied event loop and implied document concepts. Specification authors should either always pass these values, or use the wrapper algorithms queue a global task or queue an element task instead. Using the wrapper algorithms is recommended.

To queue a global task on a task source source, with a global object global and a series of steps steps:

Let event loop be global's relevant agent's event loop.

Let document be global's associated Document, if global is a Window object; otherwise null.

Queue a task given source, event loop, document, and steps.

To queue an element task on a task source source, with an element element and a series of steps steps:

Let global be element's relevant global object.

Queue a global task given source, global, and steps.

To queue a microtask which performs a series of steps steps, optionally given a document document:

Assert: there is a surrounding agent. I.e., this algorithm is not called while in parallel.

Let eventLoop be the surrounding agent's event loop.

If document was not given, set document to the implied document.

Let microtask be a new task.

Set microtask's steps to steps.

Set microtask's source to the microtask task source.

Set microtask's document to document.

Set microtask's script evaluation environment settings object set to an empty set.

Enqueue microtask on eventLoop's microtask queue.

It is possible for a microtask to be moved to a regular task queue, if, during its initial execution, it spins the event loop. This is the only case in which the source, document, and script evaluation environment settings object set of the microtask are consulted; they are ignored by the perform a microtask checkpoint algorithm.

The implied event loop when queuing a task is the one that can deduced from the context of the calling algorithm. This is generally unambiguous, as most specification algorithms only ever involve a single agent (and thus a single event loop). The exception is algorithms involving or specifying cross-agent communication (e.g., between a window and a worker); for those cases, the implied event loop concept must not be relied upon and specifications must explicitly provide an event loop when queuing a task.

The implied document when queuing a task on an event loop event loop is determined as follows:

If event loop is not a window event loop, then return null.

If the task is being queued in the context of an element, then return the element's node document.

If the task is being queued in the context of a browsing context, then return the browsing context's active document.

If the task is being queued by or for a script, then return the script's settings object's global object's associated Document.

Assert: this step is never reached, because one of the previous conditions is true. Really?

Both implied event loop and implied document are vaguely-defined and have a lot of action-at-a-distance. The hope is to remove these, especially implied document. See issue #4980.

8.1.7.3 Processing model

An event loop must continually run through the following steps for as long as it exists:

Let oldestTask and taskStartTime be null.

If the event loop has a task queue with at least one runnable task, then:

Let taskQueue be one such task queue, chosen in an implementation-defined manner.

Remember that the microtask queue is not a task queue, so it will not be chosen in this step. However, a task queue to which the microtask task source is associated might be chosen in this step. In that case, the task chosen in the next step was originally a microtask, but it got moved as part of spinning the event loop.

Set taskStartTime to the unsafe shared current time.

Set oldestTask to the first runnable task in taskQueue, and remove it from taskQueue.

If oldestTask's document is not null, then record task start time given taskStartTime and oldestTask's document.

Set the event loop's currently running task to oldestTask.

Perform oldestTask's steps.

Set the event loop's currently running task back to null.

Perform a microtask checkpoint.

Let taskEndTime be the unsafe shared current time. [HRT]

If oldestTask is not null, then:

Let top-level browsing contexts be an empty set.

For each environment settings object settings of oldestTask's script evaluation environment settings object set:

Let global be settings's global object.

If global is not a Window object, then continue.

If global's browsing context is null, then continue.

Let tlbc be global's browsing context's top-level browsing context.

If tlbc is not null, then append it to top-level browsing contexts.

Report long tasks, passing in taskStartTime, taskEndTime, top-level browsing contexts, and oldestTask.

If oldestTask's document is not null, then record task end time given taskEndTime and oldestTask's document.

If this is a window event loop that has no runnable task in this event loop's task queues, then:

Set this event loop's last idle period start time to the unsafe shared current time.

Let computeDeadline be the following steps:

Let deadline be this event loop's last idle period start time plus 50.

The cap of 50ms in the future is to ensure responsiveness to new user input within the threshold of human perception.

Let hasPendingRenders be false.

For each windowInSameLoop of the same-loop windows for this event loop:

If windowInSameLoop's map of animation frame callbacks is not empty, or if the user agent believes that the windowInSameLoop might have pending rendering updates, set hasPendingRenders to true.

Let timerCallbackEstimates be the result of getting the values of windowInSameLoop's map of active timers.

For each timeoutDeadline of timerCallbackEstimates, if timeoutDeadline is less than deadline, set deadline to timeoutDeadline.

If hasPendingRenders is true, then:

Let nextRenderDeadline be this event loop's last render opportunity time plus (1000 divided by the current refresh rate).

The refresh rate can be hardware- or implementation-specific. For a refresh rate of 60Hz, the nextRenderDeadline would be about 16.67ms after the last render opportunity time.

If nextRenderDeadline is less than deadline, then return nextRenderDeadline.

Return deadline.

For each win of the same-loop windows for this event loop, perform the start an idle period algorithm for win with the following step: return the result of calling computeDeadline, coarsened given win's relevant settings object's cross-origin isolated capability. [REQUESTIDLECALLBACK]

If this is a worker event loop, then:

If this event loop's agent's single realm's global object is a supported DedicatedWorkerGlobalScope and the user agent believes that it would benefit from having its rendering updated at this time, then:

Let now be the current high resolution time given the DedicatedWorkerGlobalScope. [HRT]

Run the animation frame callbacks for that DedicatedWorkerGlobalScope, passing in now as the timestamp.

Update the rendering of that dedicated worker to reflect the current state.

Similar to the notes for updating the rendering in a window event loop, a user agent can determine the rate of rendering in the dedicated worker.

If there are no tasks in the event loop's task queues and the WorkerGlobalScope object's closing flag is true, then destroy the event loop, aborting these steps, resuming the run a worker steps described in the Web workers section below.

A window event loop eventLoop must also run the following in parallel, as long as it exists:

Wait until at least one navigable whose active document's relevant agent's event loop is eventLoop might have a rendering opportunity.

Set eventLoop's last render opportunity time to the unsafe shared current time.

For each navigable that has a rendering opportunity, queue a global task on the rendering task source given navigable's active window to update the rendering:

This might cause redundant calls to update the rendering. However, these calls would have no observable effect because there will be no rendering necessary, as per the Unnecessary rendering step. Implementations can introduce further optimizations such as only queuing this task when it is not already queued. However, note that the document associated with the task might become inactive before the task is processed.

Let frameTimestamp be eventLoop's last render opportunity time.

Let docs be all fully active Document objects whose relevant agent's event loop is eventLoop, sorted arbitrarily except that the following conditions must be met:

Any Document B whose container document is A must be listed after A in the list.

If there are two documents A and B that both have the same non-null container document C, then the order of A and B in the list must match the shadow-including tree order of their respective navigable containers in C's node tree.

In the steps below that iterate over docs, each Document must be processed in the order it is found in the list.

Filter non-renderable documents: Remove from docs any Document object doc for which any of the following are true:

doc is render-blocked;

doc's visibility state is "hidden";

doc's rendering is suppressed for view transitions; or

doc's node navigable doesn't currently have a rendering opportunity.

We have to check for rendering opportunities here, in addition to checking that in the in parallel steps, as some documents that share the same event loop might not have a rendering opportunity at the same time.

Unnecessary rendering: Remove from docs any Document object doc for which all of the following are true:

the user agent believes that updating the rendering of doc's node navigable would have no visible effect; and

doc's map of animation frame callbacks is empty.

Remove from docs all Document objects for which the user agent believes that it's preferable to skip updating the rendering for other reasons.

The step labeled Filter non-renderable documents prevents the user agent from updating the rendering when it is unable to present new content to the user.

The step labeled Unnecessary rendering prevents the user agent from updating the rendering when there's no new content to draw.

This step enables the user agent to prevent the steps below from running for other reasons, for example, to ensure certain tasks are executed immediately after each other, with only microtask checkpoints interleaved (and without, e.g., animation frame callbacks interleaved). Concretely, a user agent might wish to coalesce timer callbacks together, with no intermediate rendering updates.

For each doc of docs, reveal doc.

For each doc of docs, flush autofocus candidates for doc if its node navigable is a top-level traversable.

For each doc of docs, run the resize steps for doc. [CSSOMVIEW]

For each doc of docs, run the scroll steps for doc. [CSSOMVIEW]

For each doc of docs, evaluate media queries and report changes for doc. [CSSOMVIEW]

For each doc of docs, update animations and send events for doc, passing in relative high resolution time given frameTimestamp and doc's relevant global object as the timestamp. [WEBANIMATIONS]

For each doc of docs, run the fullscreen steps for doc. [FULLSCREEN]

For each doc of docs, if the user agent detects that the backing storage associated with a CanvasRenderingContext2D or an OffscreenCanvasRenderingContext2D, context, has been lost, then it must run the context lost steps for each such context:

Let canvas be the value of context's canvas attribute, if context is a CanvasRenderingContext2D, or the associated OffscreenCanvas object for context otherwise.

Set context's context lost to true.

Reset the rendering context to its default state given context.

Let shouldRestore be the result of firing an event named contextlost at canvas, with the cancelable attribute initialized to true.

If shouldRestore is false, then abort these steps.

Attempt to restore context by creating a backing storage using context's attributes and associating them with context. If this fails, then abort these steps.

Set context's context lost to false.

Fire an event named contextrestored at canvas.

For each doc of docs, run the animation frame callbacks for doc, passing in the relative high resolution time given frameTimestamp and doc's relevant global object as the timestamp.

Let unsafeStyleAndLayoutStartTime be the unsafe shared current time.

For each doc of docs:

Let resizeObserverDepth be 0.

While true:

Recalculate styles and update layout for doc.

Let hadInitialVisibleContentVisibilityDetermination be false.

For each element element with 'auto' used value of 'content-visibility':

Let checkForInitialDetermination be true if element's proximity to the viewport is not determined and it is not relevant to the user. Otherwise, let checkForInitialDetermination be false.

Determine proximity to the viewport for element.

If checkForInitialDetermination is true and element is now relevant to the user, then set hadInitialVisibleContentVisibilityDetermination to true.

If hadInitialVisibleContentVisibilityDetermination is true, then continue.

The intent of this step is for the initial viewport proximity determination, which takes effect immediately, to be reflected in the style and layout calculation which is carried out in a previous step of this loop. Proximity determinations other than the initial one take effect at the next rendering opportunity. [CSSCONTAIN]

Gather active resize observations at depth resizeObserverDepth for doc.

If doc has active resize observations:

Set resizeObserverDepth to the result of broadcasting active resize observations given doc.

Continue.
Otherwise, break.

If doc has skipped resize observations, then deliver resize loop error given doc.

For each doc of docs, if the focused area of doc is not a focusable area, then run the focusing steps for doc's viewport, and set doc's relevant global object's navigation API's focus changed during ongoing navigation to false.

For example, this might happen because an element has the hidden attribute added, causing it to stop being rendered. It might also happen to an input element when the element gets disabled.

This will usually fire blur events, and possibly change events.

In addition to this asynchronous fixup, if the focused area of the document is removed, there is a synchronous fixup. That one will not fire blur or change events.

For each doc of docs, perform pending transition operations for doc. [CSSVIEWTRANSITIONS]

For each doc of docs, run the update intersection observations steps for doc, passing in the relative high resolution time given now and doc's relevant global object as the timestamp. [INTERSECTIONOBSERVER]

For each doc of docs, record rendering time for doc given unsafeStyleAndLayoutStartTime.

For each doc of docs, mark paint timing for doc.

For each doc of docs, update the rendering or user interface of doc and its node navigable to reflect the current state.

For each doc of docs, process top layer removals given doc.

A navigable has a rendering opportunity if the user agent is currently able to present the contents of the navigable to the user, accounting for hardware refresh rate constraints and user agent throttling for performance reasons, but considering content presentable even if it's outside the viewport.

A navigable's rendering opportunities are determined based on hardware constraints such as display refresh rates and other factors such as page performance or whether its active document's visibility state is "visible". Rendering opportunities typically occur at regular intervals.

This specification does not mandate any particular model for selecting rendering opportunities. But for example, if the browser is attempting to achieve a 60Hz refresh rate, then rendering opportunities occur at a maximum of every 60th of a second (about 16.7ms). If the browser finds that a navigable is not able to sustain this rate, it might drop to a more sustainable 30 rendering opportunities per second for that navigable, rather than occasionally dropping frames. Similarly, if a navigable is not visible, the user agent might decide to drop that page to a much slower 4 rendering opportunities per second, or even less.

When a user agent is to perform a microtask checkpoint:

If the event loop's performing a microtask checkpoint is true, then return.

Set the event loop's performing a microtask checkpoint to true.

While the event loop's microtask queue is not empty:

Let oldestMicrotask be the result of dequeuing from the event loop's microtask queue.

Set the event loop's currently running task to oldestMicrotask.

Run oldestMicrotask.

This might involve invoking scripted callbacks, which eventually calls the clean up after running script steps, which call this perform a microtask checkpoint algorithm again, which is why we use the performing a microtask checkpoint flag to avoid reentrancy.

Set the event loop's currently running task back to null.

For each environment settings object settingsObject whose responsible event loop is this event loop, notify about rejected promises given settingsObject's global object.

Cleanup Indexed Database transactions.

Perform ClearKeptObjects().

When WeakRef.prototype.deref() returns an object, that object is kept alive until the next invocation of ClearKeptObjects(), after which it is again subject to garbage collection.

Set the event loop's performing a microtask checkpoint to false.

Record timing info for microtask checkpoint.

When an algorithm running in parallel is to await a stable state, the user agent must queue a microtask that runs the following steps, and must then stop executing (execution of the algorithm resumes when the microtask is run, as described in the following steps):

Run the algorithm's synchronous section.

Resume execution of the algorithm in parallel, if appropriate, as described in the algorithm's steps.

Steps in synchronous sections are marked with ⌛.

Algorithm steps that say to spin the event loop until a condition goal is met are equivalent to substituting in the following algorithm steps:

Let task be the event loop's currently running task.

task could be a microtask.

Let task source be task's source.

Let old stack be a copy of the JavaScript execution context stack.

Empty the JavaScript execution context stack.

Perform a microtask checkpoint.

If task is a microtask this step will be a no-op due to performing a microtask checkpoint being true.

In parallel:

Wait until the condition goal is met.

Queue a task on task source to:

Replace the JavaScript execution context stack with old stack.

Perform any steps that appear after this spin the event loop instance in the original algorithm.

This resumes task.

Stop task, allowing whatever algorithm that invoked it to resume.

This causes the event loop's main set of steps or the perform a microtask checkpoint algorithm to continue.

Unlike other algorithms in this and other specifications, which behave similar to programming-language function calls, spin the event loop is more like a macro, which saves typing and indentation at the usage site by expanding into a series of steps and operations.

An algorithm whose steps are:

Do something.

Spin the event loop until awesomeness happens.

Do something else.

is a shorthand which, after "macro expansion", becomes

Do something.

Let old stack be a copy of the JavaScript execution context stack.

Empty the JavaScript execution context stack.

Perform a microtask checkpoint.

In parallel:

Wait until awesomeness happens.

Queue a task on the task source in which "do something" was done to:

Replace the JavaScript execution context stack with old stack.

Do something else.

Here is a more full example of the substitution, where the event loop is spun from inside a task that is queued from work in parallel. The version using spin the event loop:

In parallel:

Do parallel thing 1.

Queue a task on the DOM manipulation task source to:

Do task thing 1.

Spin the event loop until awesomeness happens.

Do task thing 2.

Do parallel thing 2.

The fully expanded version:

In parallel:

Do parallel thing 1.

Let old stack be null.

Queue a task on the DOM manipulation task source to:

Do task thing 1.

Set old stack to a copy of the JavaScript execution context stack.

Empty the JavaScript execution context stack.

Perform a microtask checkpoint.

Wait until awesomeness happens.

Queue a task on the DOM manipulation task source to:

Replace the JavaScript execution context stack with old stack.

Do task thing 2.

Do parallel thing 2.

Some of the algorithms in this specification, for historical reasons, require the user agent to pause while running a task until a condition goal is met. This means running the following steps:

Let global be the current global object.

Let timeBeforePause be the current high resolution time given global.

If necessary, update the rendering or user interface of any Document or navigable to reflect the current state.

Wait until the condition goal is met. While a user agent has a paused task, the corresponding event loop must not run further tasks, and any script in the currently running task must block. User agents should remain responsive to user input while paused, however, albeit in a reduced capacity since the event loop will not be doing anything.

Record pause duration given the duration from timeBeforePause to the current high resolution time given global.

Pausing is highly detrimental to the user experience, especially in scenarios where a single event loop is shared among multiple documents. User agents are encouraged to experiment with alternatives to pausing, such as spinning the event loop or even simply proceeding without any kind of suspended execution at all, insofar as it is possible to do so while preserving compatibility with existing content. This specification will happily change if a less-drastic alternative is discovered to be web-compatible.

In the interim, implementers should be aware that the variety of alternatives that user agents might experiment with can change subtle aspects of event loop behavior, including task and microtask timing. Implementations should continue experimenting even if doing so causes them to violate the exact semantics implied by the pause operation.

8.1.7.4 Generic task sources

The following task sources are used by a number of mostly unrelated features in this and other specifications.

The DOM manipulation task source

This task source is used for features that react to DOM manipulations, such as things that happen in a non-blocking fashion when an element is inserted into the document.

The user interaction task source

This task source is used for features that react to user interaction, for example keyboard or mouse input.

Events sent in response to user input (e.g., click events) must be fired using tasks queued with the user interaction task source. [UIEVENTS]

The networking task source

This task source is used for features that trigger in response to network activity.

The navigation and traversal task source

This task source is used to queue tasks involved in navigation and history traversal.

The rendering task source

This task source is used solely to update the rendering.

8.1.7.5 Dealing with the event loop from other specifications

Writing specifications that correctly interact with the event loop can be tricky. This is compounded by how this specification uses concurrency-model-independent terminology, so we say things like "event loop" and "in parallel" instead of using more familiar model-specific terms like "main thread" or "on a background thread".

By default, specification text generally runs on the event loop. This falls out from the formal event loop processing model, in that you can eventually trace most algorithms back to a task queued there.

The algorithm steps for any JavaScript method will be invoked by author code calling that method. And author code can only be run via queued tasks, usually originating somewhere in the script processing model.

From this starting point, the overriding guideline is that any work a specification needs to perform that would otherwise block the event loop must instead be performed in parallel with it. This includes (but is not limited to):

performing heavy computation;

displaying a user-facing prompt;

performing operations which could require involving outside systems (i.e. "going out of process").

The next complication is that, in algorithm sections that are in parallel, you must not create or manipulate objects associated to a specific realm, global, or environment settings object. (Stated in more familiar terms, you must not directly access main-thread artifacts from a background thread.) Doing so would create data races observable to JavaScript code, since after all, your algorithm steps are running in parallel to the JavaScript code.

By extension, you cannot access Web IDL's this value from steps running in parallel, even if those steps were activated by an algorithm that does have access to the this value.

You can, however, manipulate specification-level data structures and values from Infra, as those are realm-agnostic. They are never directly exposed to JavaScript without a specific conversion taking place (often via Web IDL). [INFRA] [WEBIDL]

To affect the world of observable JavaScript objects, then, you must queue a global task to perform any such manipulations. This ensures your steps are properly interleaved with respect to other things happening on the event loop. Furthermore, you must choose a task source when queuing a global task; this governs the relative order of your steps versus others. If you are unsure which task source to use, pick one of the generic task sources that sounds most applicable. Finally, you must indicate which global object your queued task is associated with; this ensures that if that global object is inactive, the task does not run.

The base primitive, on which queue a global task builds, is the queue a task algorithm. In general, queue a global task is better because it automatically picks the right event loop and, where appropriate, document. Older specifications often use queue a task combined with the implied event loop and implied document concepts, but this is discouraged.

Putting this all together, we can provide a template for a typical algorithm that needs to do work asynchronously:

Do any synchronous setup work, while still on the event loop. This may include converting realm-specific JavaScript values into realm-agnostic specification-level values.

Perform a set of potentially-expensive steps in parallel, operating entirely on realm-agnostic values, and producing a realm-agnostic result.

Queue a global task, on a specified task source and given an appropriate global object, to convert the realm-agnostic result back into observable effects on the observable world of JavaScript objects on the event loop.

The following is an algorithm that "encrypts" a passed-in list of scalar value strings input, after parsing them as URLs:

Let urls be an empty list.

For each string of input:

Let parsed be the result of encoding-parsing a URL given string, relative to the current settings object.

If parsed is failure, then return a promise rejected with a "SyntaxError" DOMException.

Let serialized be the result of applying the URL serializer to parsed.

Append serialized to urls.

Let realm be the current realm.

Let p be a new promise.

Run the following steps in parallel:

Let encryptedURLs be an empty list.

For each url of urls:

Wait 100 milliseconds, so that people think we're doing heavy-duty encryption.

Let encrypted be a new string derived from url, whose nth code unit is equal to url's nth code unit plus 13.

Append encrypted to encryptedURLs.

Queue a global task on the networking task source, given realm's global object, to perform the following steps:

Let array be the result of converting encryptedURLs to a JavaScript array, in realm.

Resolve p with array.

Return p.

Here are several things to notice about this algorithm:

It does its URL parsing up front, on the event loop, before going to the in parallel steps. This is necessary, since parsing depends on the current settings object, which would no longer be current after going in parallel.

Alternately, it could have saved a reference to the current settings object's API base URL and used it during the in parallel steps; that would have been equivalent. However, we recommend instead doing as much work as possible up front, as this example does. Attempting to save the correct values can be error prone; for example, if we'd saved just the current settings object, instead of its API base URL, there would have been a potential race.

It implicitly passes a list of strings from the initial steps to the in parallel steps. This is OK, as both lists and strings are realm-agnostic.

It performs "expensive computation" (waiting for 100 milliseconds per input URL) during the in parallel steps, thus not blocking the main event loop.

Promises, as observable JavaScript objects, are never created and manipulated during the in parallel steps. p is created before entering those steps, and then is manipulated during a task that is queued specifically for that purpose.

The creation of a JavaScript array object also happens during the queued task, and is careful to specify which realm it creates the array in since that is no longer obvious from context.

(On these last two points, see also whatwg/webidl issue #135 and whatwg/webidl issue #371, where we are still mulling over the subtleties of the above promise-resolution pattern.)

Another thing to note is that, in the event this algorithm was called from a Web IDL-specified operation taking a sequence<USVString>, there was an automatic conversion from realm-specific JavaScript objects provided by the author as input, into the realm-agnostic sequence<USVString> Web IDL type, which we then treat as a list of scalar value strings. So depending on how your specification is structured, there may be other implicit steps happening on the main event loop that play a part in this whole process of getting you ready to go in parallel.

8.1.8 Events
8.1.8.1 Event handlers
MDN

Many objects can have event handlers specified. These act as non-capture event listeners for the object on which they are specified. [DOM]

An event handler is a struct with two items:

a value, which is either null, a callback object, or an internal raw uncompiled handler. The EventHandler callback function type describes how this is exposed to scripts. Initially, an event handler's value must be set to null.

a listener, which is either null or an event listener responsible for running the event handler processing algorithm. Initially, an event handler's listener must be set to null.

Event handlers are exposed in two ways.

The first way, common to all event handlers, is as an event handler IDL attribute.

The second way is as an event handler content attribute. Event handlers on HTML elements and some of the event handlers on Window objects are exposed in this way.

For both of these two ways, the event handler is exposed through a name, which is a string that always starts with "on" and is followed by the name of the event for which the handler is intended.

Most of the time, the object that exposes an event handler is the same as the object on which the corresponding event listener is added. However, the body and frameset elements expose several event handlers that act upon the element's Window object, if one exists. In either case, we call the object an event handler acts upon the target of that event handler.

To determine the target of an event handler, given an EventTarget object eventTarget on which the event handler is exposed, and an event handler name name, the following steps are taken:

If eventTarget is not a body element or a frameset element, then return eventTarget.

If name is not the name of an attribute member of the WindowEventHandlers interface mixin and the Window-reflecting body element event handler set does not contain name, then return eventTarget.

If eventTarget's node document is not an active document, then return null.

This could happen if this object is a body element without a corresponding Window object, for example.

This check does not necessarily prevent body and frameset elements that are not the body element of their node document from reaching the next step. In particular, a body element created in an active document (perhaps with document.createElement()) but not connected will also have its corresponding Window object as the target of several event handlers exposed through it.

Return eventTarget's node document's relevant global object.

Each EventTarget object that has one or more event handlers specified has an associated event handler map, which is a map of strings representing names of event handlers to event handlers.

When an EventTarget object that has one or more event handlers specified is created, its event handler map must be initialized such that it contains an entry for each event handler that has that object as target, with items in those event handlers set to their initial values.

The order of the entries of event handler map could be arbitrary. It is not observable through any algorithms that operate on the map.

Entries are not created in the event handler map of an object for event handlers that are merely exposed on that object, but have some other object as their targets.

An event handler IDL attribute is an IDL attribute for a specific event handler. The name of the IDL attribute is the same as the name of the event handler.

The getter of an event handler IDL attribute with name name, when called, must run these steps:

Let eventTarget be the result of determining the target of an event handler given this object and name.

If eventTarget is null, then return null.

Return the result of getting the current value of the event handler given eventTarget and name.

The setter of an event handler IDL attribute with name name, when called, must run these steps:

Let eventTarget be the result of determining the target of an event handler given this object and name.

If eventTarget is null, then return.

If the given value is null, then deactivate an event handler given eventTarget and name.

Otherwise:

Let handlerMap be eventTarget's event handler map.

Let eventHandler be handlerMap[name].

Set eventHandler's value to the given value.

Activate an event handler given eventTarget and name.

Certain event handler IDL attributes have additional requirements, in particular the onmessage attribute of MessagePort objects.

An event handler content attribute is a content attribute for a specific event handler. The name of the content attribute is the same as the name of the event handler.

Event handler content attributes, when specified, must contain valid JavaScript code which, when parsed, would match the FunctionBody production after automatic semicolon insertion.

The following attribute change steps are used to synchronize between event handler content attributes and event handlers: [DOM]

If namespace is not null, or localName is not the name of an event handler content attribute on element, then return.

Let eventTarget be the result of determining the target of an event handler given element and localName.

If eventTarget is null, then return.

If value is null, then deactivate an event handler given eventTarget and localName.

Otherwise:

If the Should element's inline behavior be blocked by Content Security Policy? algorithm returns "Blocked" when executed upon element, "script attribute", and value, then return. [CSP]

Let handlerMap be eventTarget's event handler map.

Let eventHandler be handlerMap[localName].

Let location be the script location that triggered the execution of these steps.

Set eventHandler's value to the internal raw uncompiled handler value/location.

Activate an event handler given eventTarget and localName.

Per the DOM Standard, these steps are run even if oldValue and value are identical (setting an attribute to its current value), but not if oldValue and value are both null (removing an attribute that doesn't currently exist). [DOM]

To deactivate an event handler given an EventTarget object eventTarget and a string name that is the name of an event handler, run these steps:

Let handlerMap be eventTarget's event handler map.

Let eventHandler be handlerMap[name].

Set eventHandler's value to null.

Let listener be eventHandler's listener.

If listener is not null, then remove an event listener with eventTarget and listener.

Set eventHandler's listener to null.

To erase all event listeners and handlers given an EventTarget object eventTarget, run these steps:

If eventTarget has an associated event handler map, then for each name → eventHandler of eventTarget's associated event handler map, deactivate an event handler given eventTarget and name.

Remove all event listeners given eventTarget.

This algorithm is used to define document.open().

To activate an event handler given an EventTarget object eventTarget and a string name that is the name of an event handler, run these steps:

Let handlerMap be eventTarget's event handler map.

Let eventHandler be handlerMap[name].

If eventHandler's listener is not null, then return.

Let callback be the result of creating a Web IDL EventListener instance representing a reference to a function of one argument that executes the steps of the event handler processing algorithm, given eventTarget, name, and its argument.

The EventListener's callback context can be arbitrary; it does not impact the steps of the event handler processing algorithm. [DOM]

The callback is emphatically not the event handler itself. Every event handler ends up registering the same callback, the algorithm defined below, which takes care of invoking the right code, and processing the code's return value.

Let listener be a new event listener whose type is the event handler event type corresponding to eventHandler and callback is callback.

To be clear, an event listener is different from an EventListener.

Add an event listener with eventTarget and listener.

Set eventHandler's listener to listener.

The event listener registration happens only if the event handler's value is being set to non-null, and the event handler is not already activated. Since listeners are called in the order they were registered, assuming no deactivation occurred, the order of event listeners for a particular event type will always be:

the event listeners registered with addEventListener() before the first time the event handler's value was set to non-null

then the callback to which it is currently set, if any

and finally the event listeners registered with addEventListener() after the first time the event handler's value was set to non-null.

This example demonstrates the order in which event listeners are invoked. If the button in this example is clicked by the user, the page will show four alerts, with the text "ONE", "TWO", "THREE", and "FOUR" respectively.

<button id="test">Start Demo</button>
<script>
 var button = document.getElementById('test');
 button.addEventListener('click', function () { alert('ONE') }, false);
 button.setAttribute('onclick', "alert('NOT CALLED')"); // event handler listener is registered here
 button.addEventListener('click', function () { alert('THREE') }, false);
 button.onclick = function () { alert('TWO'); };
 button.addEventListener('click', function () { alert('FOUR') }, false);
</script>

However, in the following example, the event handler is deactivated after its initial activation (and its event listener is removed), before being reactivated at a later time. The page will show five alerts with "ONE", "TWO", "THREE", "FOUR", and "FIVE" respectively, in order.

<button id="test">Start Demo</button>
<script>
 var button = document.getElementById('test');
 button.addEventListener('click', function () { alert('ONE') }, false);
 button.setAttribute('onclick', "alert('NOT CALLED')"); // event handler is activated here
 button.addEventListener('click', function () { alert('TWO') }, false);
 button.onclick = null;                                 // but deactivated here
 button.addEventListener('click', function () { alert('THREE') }, false);
 button.onclick = function () { alert('FOUR'); };       // and re-activated here
 button.addEventListener('click', function () { alert('FIVE') }, false);
</script>

The interfaces implemented by the event object do not influence whether an event handler is triggered or not.

The event handler processing algorithm for an EventTarget object eventTarget, a string name representing the name of an event handler, and an Event object event is as follows:

If scripting is disabled for eventTarget, then return.

Let callback be the result of getting the current value of the event handler given eventTarget and name.

If callback is null, then return.

Let special error event handling be true if event is an ErrorEvent object, event's type is "error", and event's currentTarget implements the WindowOrWorkerGlobalScope mixin. Otherwise, let special error event handling be false.

Process the Event object event as follows:

If special error event handling is true

Let return value be the result of invoking callback with « event's message, event's filename, event's lineno, event's colno, event's error », "rethrow", and with callback this value set to event's currentTarget.

Otherwise

Let return value be the result of invoking callback with « event », "rethrow", and with callback this value set to event's currentTarget.

If an exception gets thrown by the callback, it will be rethrown, ending these steps. The exception will propagate to the DOM event dispatch logic, which will then report it.

Process return value as follows:

If event is a BeforeUnloadEvent object and event's type is "beforeunload"

In this case, the event handler IDL attribute's type will be OnBeforeUnloadEventHandler, so return value will have been coerced into either null or a DOMString.

If return value is not null, then:

Set event's canceled flag.

If event's returnValue attribute's value is the empty string, then set event's returnValue attribute's value to return value.

If special error event handling is true

If return value is true, then set event's canceled flag.

Otherwise

If return value is false, then set event's canceled flag.

If we've gotten to this "Otherwise" clause because event's type is "beforeunload" but event is not a BeforeUnloadEvent object, then return value will never be false, since in such cases return value will have been coerced into either null or a DOMString.

The EventHandler callback function type represents a callback used for event handlers. It is represented in Web IDL as follows:

[LegacyTreatNonObjectAsNull]
callback EventHandlerNonNull = any (Event event);
typedef EventHandlerNonNull? EventHandler;

In JavaScript, any Function object implements this interface.

For example, the following document fragment:

<body onload="alert(this)" onclick="alert(this)">

...leads to an alert saying "[object Window]" when the document is loaded, and an alert saying "[object HTMLBodyElement]" whenever the user clicks something in the page.

The return value of the function affects whether the event is canceled or not: as described above, if the return value is false, the event is canceled.

There are two exceptions in the platform, for historical reasons:

The onerror handlers on global objects, where returning true cancels the event.

The onbeforeunload handler, where returning any non-null and non-undefined value will cancel the event.

For historical reasons, the onerror handler has different arguments:

[LegacyTreatNonObjectAsNull]
callback OnErrorEventHandlerNonNull = any ((Event or DOMString) event, optional DOMString source, optional unsigned long lineno, optional unsigned long colno, optional any error);
typedef OnErrorEventHandlerNonNull? OnErrorEventHandler;
window.onerror = (message, source, lineno, colno, error) => { … };

Similarly, the onbeforeunload handler has a different return value:

[LegacyTreatNonObjectAsNull]
callback OnBeforeUnloadEventHandlerNonNull = DOMString? (Event event);
typedef OnBeforeUnloadEventHandlerNonNull? OnBeforeUnloadEventHandler;

An internal raw uncompiled handler is a tuple with the following information:

An uncompiled script body

A location where the script body originated, in case an error needs to be reported

When the user agent is to get the current value of the event handler given an EventTarget object eventTarget and a string name that is the name of an event handler, it must run these steps:

Let handlerMap be eventTarget's event handler map.

Let eventHandler be handlerMap[name].

If eventHandler's value is an internal raw uncompiled handler, then:

If eventTarget is an element, then let element be eventTarget, and document be element's node document. Otherwise, eventTarget is a Window object, let element be null, and document be eventTarget's associated Document.

If document's active sandboxing flag set has its sandboxed scripts browsing context flag set, then return null.

Let body be the uncompiled script body in eventHandler's value.

Let location be the location where the script body originated, as given by eventHandler's value.

If element is not null and element has a form owner, let form owner be that form owner. Otherwise, let form owner be null.

Let settings object be the relevant settings object of document.

If body is not parsable as FunctionBody or if parsing detects an early error, then follow these substeps:

Set eventHandler's value to null.

This does not deactivate the event handler, which additionally removes the event handler's listener (if present).

Let syntaxError be a new SyntaxError exception associated with settings object's realm which describes the error while parsing. It should be based on location, where the script body originated.

Report an exception with syntaxError for settings object's global object.

Return null.

Push settings object's realm execution context onto the JavaScript execution context stack; it is now the running JavaScript execution context.

This is necessary so the subsequent invocation of OrdinaryFunctionCreate takes place in the correct realm.

Let function be the result of calling OrdinaryFunctionCreate, with arguments:

functionPrototype
%Function.prototype%
sourceText
If name is onerror and eventTarget is a Window object
The string formed by concatenating "function ", name, "(event, source, lineno, colno, error) {", U+000A LF, body, U+000A LF, and "}".
Otherwise
The string formed by concatenating "function ", name, "(event) {", U+000A LF, body, U+000A LF, and "}".
ParameterList
If name is onerror and eventTarget is a Window object
Let the function have five arguments, named event, source, lineno, colno, and error.
Otherwise
Let the function have a single argument called event.
body
The result of parsing body above.
thisMode
non-lexical-this
scope

Let realm be settings object's realm.

Let scope be realm.[[GlobalEnv]].

If eventHandler is an element's event handler, then set scope to NewObjectEnvironment(document, true, scope).

(Otherwise, eventHandler is a Window object's event handler.)

If form owner is not null, then set scope to NewObjectEnvironment(form owner, true, scope).

If element is not null, then set scope to NewObjectEnvironment(element, true, scope).

Return scope.

Remove settings object's realm execution context from the JavaScript execution context stack.

Set function.[[ScriptOrModule]] to null.

This is done because the default behavior, of associating the created function with the nearest script on the stack, can lead to path-dependent results. For example, an event handler which is first invoked by user interaction would end up with null [[ScriptOrModule]] (since then this algorithm would be first invoked when the active script is null), whereas one that is first invoked by dispatching an event from script would have its [[ScriptOrModule]] set to that script.

Instead, we just always set [[ScriptOrModule]] to null. This is more intuitive anyway; the idea that the first script which dispatches an event is somehow responsible for the event handler code is dubious.

In practice, this only affects the resolution of relative URLs via import(), which consult the base URL of the associated script. Nulling out [[ScriptOrModule]] means that HostLoadImportedModule will fall back to the current settings object's API base URL.

Set eventHandler's value to the result of creating a Web IDL EventHandler callback function object whose object reference is function and whose callback context is settings object.

Return eventHandler's value.

8.1.8.2 Event handlers on elements, Document objects, and Window objects

The following are the event handlers (and their corresponding event handler event types) that must be supported by all HTML elements, as both event handler content attributes and event handler IDL attributes; and that must be supported by all Document and Window objects, as event handler IDL attributes:

Event handler	Event handler event type
onabort
✔MDN
	abort
onauxclick
MDN
	auxclick
onbeforeinput	beforeinput
onbeforematch	beforematch
onbeforetoggle	beforetoggle
oncancel
✔MDN
	cancel
oncanplay
✔MDN
	canplay
oncanplaythrough
✔MDN
	canplaythrough
onchange
✔MDN
	change
onclick
✔MDN
	click
onclose	close
oncommand	command
oncontextlost	contextlost
oncontextmenu	contextmenu
oncontextrestored	contextrestored
oncopy
✔MDN
	copy
oncuechange
✔MDN
	cuechange
oncut
✔MDN
	cut
ondblclick
✔MDN
	dblclick
ondrag	drag
ondragend	dragend
ondragenter	dragenter
ondragleave	dragleave
ondragover	dragover
ondragstart	dragstart
ondrop	drop
ondurationchange
✔MDN
	durationchange
onemptied
✔MDN
	emptied
onended
✔MDN
	ended
onformdata	formdata
oninput
✔MDN
	input
oninvalid	invalid
onkeydown
✔MDN
	keydown
onkeypress	keypress
onkeyup
✔MDN
	keyup
onloadeddata
✔MDN
	loadeddata
onloadedmetadata
✔MDN
	loadedmetadata
onloadstart
✔MDN
	loadstart
onmousedown
✔MDN
	mousedown
onmouseenter
✔MDN
	mouseenter
onmouseleave
✔MDN
	mouseleave
onmousemove
✔MDN
	mousemove
onmouseout
✔MDN
	mouseout
onmouseover
✔MDN
	mouseover
onmouseup
✔MDN
	mouseup
onpaste
✔MDN
	paste
onpause
✔MDN
	pause
onplay
✔MDN
	play
onplaying
✔MDN
	playing
onprogress
✔MDN
	progress
onratechange
✔MDN
	ratechange
onreset	reset
onscrollend
MDN
	scrollend
onsecuritypolicyviolation
✔MDN
	securitypolicyviolation
onseeked
✔MDN
	seeked
onseeking
✔MDN
	seeking
onselect
✔MDN
	select
onslotchange
✔MDN
	slotchange
onstalled
✔MDN
	stalled
onsubmit
✔MDN
	submit
onsuspend
✔MDN
	suspend
ontimeupdate
✔MDN
	timeupdate
ontoggle	toggle
onvolumechange
✔MDN
	volumechange
onwaiting
✔MDN
	waiting
onwebkitanimationend	webkitAnimationEnd
onwebkitanimationiteration	webkitAnimationIteration
onwebkitanimationstart	webkitAnimationStart
onwebkittransitionend	webkitTransitionEnd
onwheel
✔MDN
	wheel

The following are the event handlers (and their corresponding event handler event types) that must be supported by all HTML elements other than body and frameset elements, as both event handler content attributes and event handler IDL attributes; that must be supported by all Document objects, as event handler IDL attributes; and that must be supported by all Window objects, as event handler IDL attributes on the Window objects themselves, and with corresponding event handler content attributes and event handler IDL attributes exposed on all body and frameset elements that are owned by that Window object's associated Document:

Event handler	Event handler event type
onblur
✔MDN
	blur
onerror
✔MDN
	error
onfocus
✔MDN
	focus
onload	load
onresize	resize
onscroll
✔MDN
	scroll

We call the set of the names of the event handlers listed in the first column of this table the Window-reflecting body element event handler set.

The following are the event handlers (and their corresponding event handler event types) that must be supported by Window objects, as event handler IDL attributes on the Window objects themselves, and with corresponding event handler content attributes and event handler IDL attributes exposed on all body and frameset elements that are owned by that Window object's associated Document:

Event handler	Event handler event type
onafterprint
✔MDN
	afterprint
onbeforeprint
✔MDN
	beforeprint
onbeforeunload
✔MDN
	beforeunload
onhashchange
✔MDN
	hashchange
onlanguagechange
✔MDN
	languagechange
onmessage
✔MDN
	message
onmessageerror
✔MDN
	messageerror
onoffline
✔MDN
	offline
ononline
✔MDN
	online
onpageswap	pageswap
onpagehide	pagehide
onpagereveal	pagereveal
onpageshow	pageshow
onpopstate
✔MDN
	popstate
onrejectionhandled
✔MDN
	rejectionhandled
onstorage
✔MDN
	storage
onunhandledrejection
✔MDN
	unhandledrejection
onunload
✔MDN
	unload

This list of event handlers is reified as event handler IDL attributes through the WindowEventHandlers interface mixin.

The following are the event handlers (and their corresponding event handler event types) that must be supported on Document objects as event handler IDL attributes:

Event handler	Event handler event type
onreadystatechange	readystatechange
onvisibilitychange
✔MDN
	visibilitychange
8.1.8.2.1 IDL definitions
interface mixin GlobalEventHandlers {
  attribute EventHandler onabort;
  attribute EventHandler onauxclick;
  attribute EventHandler onbeforeinput;
  attribute EventHandler onbeforematch;
  attribute EventHandler onbeforetoggle;
  attribute EventHandler onblur;
  attribute EventHandler oncancel;
  attribute EventHandler oncanplay;
  attribute EventHandler oncanplaythrough;
  attribute EventHandler onchange;
  attribute EventHandler onclick;
  attribute EventHandler onclose;
  attribute EventHandler oncommand;
  attribute EventHandler oncontextlost;
  attribute EventHandler oncontextmenu;
  attribute EventHandler oncontextrestored;
  attribute EventHandler oncopy;
  attribute EventHandler oncuechange;
  attribute EventHandler oncut;
  attribute EventHandler ondblclick;
  attribute EventHandler ondrag;
  attribute EventHandler ondragend;
  attribute EventHandler ondragenter;
  attribute EventHandler ondragleave;
  attribute EventHandler ondragover;
  attribute EventHandler ondragstart;
  attribute EventHandler ondrop;
  attribute EventHandler ondurationchange;
  attribute EventHandler onemptied;
  attribute EventHandler onended;
  attribute OnErrorEventHandler onerror;
  attribute EventHandler onfocus;
  attribute EventHandler onformdata;
  attribute EventHandler oninput;
  attribute EventHandler oninvalid;
  attribute EventHandler onkeydown;
  attribute EventHandler onkeypress;
  attribute EventHandler onkeyup;
  attribute EventHandler onload;
  attribute EventHandler onloadeddata;
  attribute EventHandler onloadedmetadata;
  attribute EventHandler onloadstart;
  attribute EventHandler onmousedown;
  [LegacyLenientThis] attribute EventHandler onmouseenter;
  [LegacyLenientThis] attribute EventHandler onmouseleave;
  attribute EventHandler onmousemove;
  attribute EventHandler onmouseout;
  attribute EventHandler onmouseover;
  attribute EventHandler onmouseup;
  attribute EventHandler onpaste;
  attribute EventHandler onpause;
  attribute EventHandler onplay;
  attribute EventHandler onplaying;
  attribute EventHandler onprogress;
  attribute EventHandler onratechange;
  attribute EventHandler onreset;
  attribute EventHandler onresize;
  attribute EventHandler onscroll;
  attribute EventHandler onscrollend;
  attribute EventHandler onsecuritypolicyviolation;
  attribute EventHandler onseeked;
  attribute EventHandler onseeking;
  attribute EventHandler onselect;
  attribute EventHandler onslotchange;
  attribute EventHandler onstalled;
  attribute EventHandler onsubmit;
  attribute EventHandler onsuspend;
  attribute EventHandler ontimeupdate;
  attribute EventHandler ontoggle;
  attribute EventHandler onvolumechange;
  attribute EventHandler onwaiting;
  attribute EventHandler onwebkitanimationend;
  attribute EventHandler onwebkitanimationiteration;
  attribute EventHandler onwebkitanimationstart;
  attribute EventHandler onwebkittransitionend;
  attribute EventHandler onwheel;
};

interface mixin WindowEventHandlers {
  attribute EventHandler onafterprint;
  attribute EventHandler onbeforeprint;
  attribute OnBeforeUnloadEventHandler onbeforeunload;
  attribute EventHandler onhashchange;
  attribute EventHandler onlanguagechange;
  attribute EventHandler onmessage;
  attribute EventHandler onmessageerror;
  attribute EventHandler onoffline;
  attribute EventHandler ononline;
  attribute EventHandler onpagehide;
  attribute EventHandler onpagereveal;
  attribute EventHandler onpageshow;
  attribute EventHandler onpageswap;
  attribute EventHandler onpopstate;
  attribute EventHandler onrejectionhandled;
  attribute EventHandler onstorage;
  attribute EventHandler onunhandledrejection;
  attribute EventHandler onunload;
};
8.1.8.3 Event firing

Certain operations and methods are defined as firing events on elements. For example, the click() method on the HTMLElement interface is defined as firing a click event on the element. [POINTEREVENTS]

Firing a synthetic pointer event named e at target, with an optional not trusted flag, means running these steps:

Let event be the result of creating an event using PointerEvent.

Initialize event's type attribute to e.

Initialize event's bubbles and cancelable attributes to true.

Set event's composed flag.

If the not trusted flag is set, initialize event's isTrusted attribute to false.

Initialize event's ctrlKey, shiftKey, altKey, and metaKey attributes according to the current state of the key input device, if any (false for any keys that are not available).

Initialize event's view attribute to target's node document's Window object, if any, and null otherwise.

event's getModifierState() method is to return values appropriately describing the current state of the key input device.

Return the result of dispatching event at target.

Firing a click event at target means firing a synthetic pointer event named click at target.

8.2 The WindowOrWorkerGlobalScope mixin

The WindowOrWorkerGlobalScope mixin is for use of APIs that are to be exposed on Window and WorkerGlobalScope objects.

Other standards are encouraged to further extend it using partial interface mixin WindowOrWorkerGlobalScope { … }; along with an appropriate reference.

typedef (DOMString or Function or TrustedScript) TimerHandler;

interface mixin WindowOrWorkerGlobalScope {
  [Replaceable] readonly attribute USVString origin;
  readonly attribute boolean isSecureContext;
  readonly attribute boolean crossOriginIsolated;

  undefined reportError(any e);

  // base64 utility methods
  DOMString btoa(DOMString data);
  ByteString atob(DOMString data);

  // timers
  long setTimeout(TimerHandler handler, optional long timeout = 0, any... arguments);
  undefined clearTimeout(optional long id = 0);
  long setInterval(TimerHandler handler, optional long timeout = 0, any... arguments);
  undefined clearInterval(optional long id = 0);

  // microtask queuing
  undefined queueMicrotask(VoidFunction callback);

  // ImageBitmap
  Promise<ImageBitmap> createImageBitmap(ImageBitmapSource image, optional ImageBitmapOptions options = {});
  Promise<ImageBitmap> createImageBitmap(ImageBitmapSource image, long sx, long sy, long sw, long sh, optional ImageBitmapOptions options = {});

  // structured cloning
  any structuredClone(any value, optional StructuredSerializeOptions options = {});
};
Window includes WindowOrWorkerGlobalScope;
WorkerGlobalScope includes WindowOrWorkerGlobalScope;
self.isSecureContext
✔MDN

Returns whether or not this global object represents a secure context. [SECURE-CONTEXTS]

self.origin
✔MDN

Returns the global object's origin, serialized as string.

self.crossOriginIsolated
✔MDN

Returns whether scripts running in this global are allowed to use APIs that require cross-origin isolation. This depends on the `Cross-Origin-Opener-Policy` and `Cross-Origin-Embedder-Policy` HTTP response headers and the "cross-origin-isolated" feature.

Developers are strongly encouraged to use self.origin over location.origin. The former returns the origin of the environment, the latter of the URL of the environment. Imagine the following script executing in a document on https://stargate.example/:

var frame = document.createElement("iframe")
frame.onload = function() {
  var frameWin = frame.contentWindow
  console.log(frameWin.location.origin) // "null"
  console.log(frameWin.origin) // "https://stargate.example"
}
document.body.appendChild(frame)

self.origin is a more reliable security indicator.

The isSecureContext getter steps are to return true if this's relevant settings object is a secure context, or false otherwise.

The origin getter steps are to return this's relevant settings object's origin, serialized.

The crossOriginIsolated getter steps are to return this's relevant settings object's cross-origin isolated capability.

An element implementing the WindowOrWorkerGlobalScope mixin has the following extract an origin steps:

If this's relevant settings object's origin is not same origin-domain with the entry settings object's origin, then return null.

Return this's relevant settings object's origin.

Since these objects are potentially accessible cross-origin (e.g., through WindowProxy), we need a security check here before granting access to the origin.

8.3 Base64 utility methods

The atob() and btoa() methods allow developers to transform content to and from the base64 encoding.

In these APIs, for mnemonic purposes, the "b" can be considered to stand for "binary", and the "a" for "ASCII". In practice, though, for primarily historical reasons, both the input and output of these functions are Unicode strings.

result = self.btoa(data)
✔MDN

Takes the input data, in the form of a Unicode string containing only characters in the range U+0000 to U+00FF, each representing a binary byte with values 0x00 to 0xFF respectively, and converts it to its base64 representation, which it returns.

Throws an "InvalidCharacterError" DOMException if the input string contains any out-of-range characters.

result = self.atob(data)
✔MDN

Takes the input data, in the form of a Unicode string containing base64-encoded binary data, decodes it, and returns a string consisting of characters in the range U+0000 to U+00FF, each representing a binary byte with values 0x00 to 0xFF respectively, corresponding to that binary data.

Throws an "InvalidCharacterError" DOMException if the input string is not valid base64 data.

The btoa(data) method must throw an "InvalidCharacterError" DOMException if data contains any character whose code point is greater than U+00FF. Otherwise, the user agent must convert data to a byte sequence whose nth byte is the eight-bit representation of the nth code point of data, and then must apply forgiving-base64 encode to that byte sequence and return the result.

The atob(data) method steps are:

Let decodedData be the result of running forgiving-base64 decode on data.

If decodedData is failure, then throw an "InvalidCharacterError" DOMException.

Return decodedData.

← 7.6 Speculative loading — Table of Contents — 8.4 Dynamic markup insertion →
