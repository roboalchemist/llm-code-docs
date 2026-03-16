# Source: https://html.spec.whatwg.org/multipage/workers.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/workers.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 9.3 Cross-document messaging](https://html.spec.whatwg.org/multipage/web-messaging.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [11 Worklets →](https://html.spec.whatwg.org/multipage/worklets.html)
1.   [10 Web workers](https://html.spec.whatwg.org/multipage/workers.html#workers)
    1.   [10.1 Introduction](https://html.spec.whatwg.org/multipage/workers.html#introduction-14)
        1.   [10.1.1 Scope](https://html.spec.whatwg.org/multipage/workers.html#scope-2)
        2.   [10.1.2 Examples](https://html.spec.whatwg.org/multipage/workers.html#examples-6)
            1.   [10.1.2.1 A background number-crunching worker](https://html.spec.whatwg.org/multipage/workers.html#a-background-number-crunching-worker)
            2.   [10.1.2.2 Using a JavaScript module as a worker](https://html.spec.whatwg.org/multipage/workers.html#module-worker-example)
            3.   [10.1.2.3 Shared workers introduction](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-introduction)
            4.   [10.1.2.4 Shared state using a shared worker](https://html.spec.whatwg.org/multipage/workers.html#shared-state-using-a-shared-worker)
            5.   [10.1.2.5 Delegation](https://html.spec.whatwg.org/multipage/workers.html#delegation)
            6.   [10.1.2.6 Providing libraries](https://html.spec.whatwg.org/multipage/workers.html#providing-libraries)

        3.   [10.1.3 Tutorials](https://html.spec.whatwg.org/multipage/workers.html#tutorials)
            1.   [10.1.3.1 Creating a dedicated worker](https://html.spec.whatwg.org/multipage/workers.html#creating-a-dedicated-worker)
            2.   [10.1.3.2 Communicating with a dedicated worker](https://html.spec.whatwg.org/multipage/workers.html#communicating-with-a-dedicated-worker)
            3.   [10.1.3.3 Shared workers](https://html.spec.whatwg.org/multipage/workers.html#shared-workers)

    2.   [10.2 Infrastructure](https://html.spec.whatwg.org/multipage/workers.html#infrastructure-2)
        1.   [10.2.1 The global scope](https://html.spec.whatwg.org/multipage/workers.html#the-global-scope)
            1.   [10.2.1.1 The `WorkerGlobalScope` common interface](https://html.spec.whatwg.org/multipage/workers.html#the-workerglobalscope-common-interface)
            2.   [10.2.1.2 Dedicated workers and the `DedicatedWorkerGlobalScope` interface](https://html.spec.whatwg.org/multipage/workers.html#dedicated-workers-and-the-dedicatedworkerglobalscope-interface)
            3.   [10.2.1.3 Shared workers and the `SharedWorkerGlobalScope` interface](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-and-the-sharedworkerglobalscope-interface)

        2.   [10.2.2 The event loop](https://html.spec.whatwg.org/multipage/workers.html#worker-event-loop)
        3.   [10.2.3 The worker's lifetime](https://html.spec.whatwg.org/multipage/workers.html#the-worker's-lifetime)
        4.   [10.2.4 Processing model](https://html.spec.whatwg.org/multipage/workers.html#worker-processing-model)
        5.   [10.2.5 Runtime script errors](https://html.spec.whatwg.org/multipage/workers.html#runtime-script-errors-2)
        6.   [10.2.6 Creating workers](https://html.spec.whatwg.org/multipage/workers.html#creating-workers)
            1.   [10.2.6.1 The `AbstractWorker` mixin](https://html.spec.whatwg.org/multipage/workers.html#the-abstractworker-mixin)
            2.   [10.2.6.2 Script settings for workers](https://html.spec.whatwg.org/multipage/workers.html#script-settings-for-workers)
            3.   [10.2.6.3 Dedicated workers and the `Worker` interface](https://html.spec.whatwg.org/multipage/workers.html#dedicated-workers-and-the-worker-interface)
            4.   [10.2.6.4 Shared workers and the `SharedWorker` interface](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-and-the-sharedworker-interface)

        7.   [10.2.7 Concurrent hardware capabilities](https://html.spec.whatwg.org/multipage/workers.html#navigator.hardwareconcurrency)

    3.   [10.3 APIs available to workers](https://html.spec.whatwg.org/multipage/workers.html#apis-available-to-workers)
        1.   [10.3.1 Importing scripts and libraries](https://html.spec.whatwg.org/multipage/workers.html#importing-scripts-and-libraries)
        2.   [10.3.2 The `WorkerNavigator` interface](https://html.spec.whatwg.org/multipage/workers.html#the-workernavigator-object)
        3.   [10.3.3 The `WorkerLocation` interface](https://html.spec.whatwg.org/multipage/workers.html#worker-locations)

10 Web workers[](https://html.spec.whatwg.org/multipage/workers.html#workers)
-----------------------------------------------------------------------------

[Web_Workers_API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API "Web Workers makes it possible to run a script operation in a background thread separate from the main execution thread of a web application. The advantage of this is that laborious processing can be performed in a separate thread, allowing the main (usually the UI) thread to run without being blocked/slowed down.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

### 10.1 Introduction[](https://html.spec.whatwg.org/multipage/workers.html#introduction-14)

#### 10.1.1 Scope[](https://html.spec.whatwg.org/multipage/workers.html#scope-2)

_This section is non-normative._

This specification defines an API for running scripts in the background independently of any user interface scripts.

This allows for long-running scripts that are not interrupted by scripts that respond to clicks or other user interactions, and allows long tasks to be executed without yielding to keep the page responsive.

Workers (as these background scripts are called herein) are relatively heavy-weight, and are not intended to be used in large numbers. For example, it would be inappropriate to launch one worker for each pixel of a four megapixel image. The examples below show some appropriate uses of workers.

Generally, workers are expected to be long-lived, have a high start-up performance cost, and a high per-instance memory cost.

#### 10.1.2 Examples[](https://html.spec.whatwg.org/multipage/workers.html#examples-6)

_This section is non-normative._

There are a variety of uses that workers can be put to. The following subsections show various examples of this use.

##### 10.1.2.1 A background number-crunching worker[](https://html.spec.whatwg.org/multipage/workers.html#a-background-number-crunching-worker)

_This section is non-normative._

The simplest use of workers is for performing a computationally expensive task without interrupting the user interface.

In this example, the main document spawns a worker to (naïvely) compute prime numbers, and progressively displays the most recently found prime number.

The main page is as follows:

```
<!DOCTYPE HTML>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>Worker example: One-core computation</title>
 </head>
 <body>
  <p>The highest prime number discovered so far is: <output id="result"></output></p>
  <script>
   var worker = new Worker('worker.js');
   worker.onmessage = function (event) {
     document.getElementById('result').textContent = event.data;
   };
  </script>
 </body>
</html>
```

The `Worker()` constructor call creates a worker and returns a `Worker` object representing that worker, which is used to communicate with the worker. That object's `onmessage` event handler allows the code to receive messages from the worker.

The worker itself is as follows:

```
var n = 1;
search: while (true) {
  n += 1;
  for (var i = 2; i <= Math.sqrt(n); i += 1)
    if (n % i == 0)
     continue search;
  // found a prime!
  postMessage(n);
}
```

The bulk of this code is simply an unoptimized search for a prime number. The `postMessage()` method is used to send a message back to the page when a prime is found.

[View this example online](https://html.spec.whatwg.org/demos/workers/primes/page.html).

##### 10.1.2.2 Using a JavaScript module as a worker[](https://html.spec.whatwg.org/multipage/workers.html#module-worker-example)

_This section is non-normative._

All of our examples so far show workers that run [classic scripts](https://html.spec.whatwg.org/multipage/webappapis.html#classic-script). Workers can instead be instantiated using [module scripts](https://html.spec.whatwg.org/multipage/webappapis.html#module-script), which have the usual benefits: the ability to use the JavaScript `import` statement to import other modules; strict mode by default; and top-level declarations not polluting the worker's global scope.

As the `import` statement is available, the `importScripts()` method will automatically fail inside module workers.

In this example, the main document uses a worker to do off-main-thread image manipulation. It imports the filters used from another module.

The main page is as follows:

```
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Worker example: image decoding</title>

<p>
  <label>
    Type an image URL to decode
    <input type="url" id="image-url" list="image-list">
    <datalist id="image-list">
      <option value="https://html.spec.whatwg.org/images/drawImage.png">
      <option value="https://html.spec.whatwg.org/images/robots.jpeg">
      <option value="https://html.spec.whatwg.org/images/arcTo2.png">
    </datalist>
  </label>
</p>

<p>
  <label>
    Choose a filter to apply
    <select id="filter">
      <option value="none">none</option>
      <option value="grayscale">grayscale</option>
      <option value="brighten">brighten by 20%</option>
    </select>
  </label>
</p>

<div id="output"></div>

<script type="module">
  const worker = new Worker("worker.js", { type: "module" });
  worker.onmessage = receiveFromWorker;

  const url = document.querySelector("#image-url");
  const filter = document.querySelector("#filter");
  const output = document.querySelector("#output");

  url.oninput = updateImage;
  filter.oninput = sendToWorker;

  let imageData, context;

  function updateImage() {
    const img = new Image();
    img.src = url.value;

    img.onload = () => {
      const canvas = document.createElement("canvas");
      canvas.width = img.width;
      canvas.height = img.height;

      context = canvas.getContext("2d");
      context.drawImage(img, 0, 0);
      imageData = context.getImageData(0, 0, canvas.width, canvas.height);

      sendToWorker();
      output.replaceChildren(canvas);
    };
  }

  function sendToWorker() {
    worker.postMessage({ imageData, filter: filter.value });
  }

  function receiveFromWorker(e) {
    context.putImageData(e.data, 0, 0);
  }
</script>
```

The worker file is then:

```
import * as filters from "./filters.js";

self.onmessage = e => {
  const { imageData, filter } = e.data;
  filters[filter](imageData);
  self.postMessage(imageData, [imageData.data.buffer]);
};
```

Which imports the file `filters.js`:

```
export function none() {}

export function grayscale({ data: d }) {
  for (let i = 0; i < d.length; i += 4) {
    const [r, g, b] = [d[i], d[i + 1], d[i + 2]];

    // CIE luminance for the RGB
    // The human eye is bad at seeing red and blue, so we de-emphasize them.
    d[i] = d[i + 1] = d[i + 2] = 0.2126 * r + 0.7152 * g + 0.0722 * b;
  }
};

export function brighten({ data: d }) {
  for (let i = 0; i < d.length; ++i) {
    d[i] *= 1.2;
  }
};
```

[View this example online](https://html.spec.whatwg.org/demos/workers/modules/page.html).

##### 10.1.2.3 Shared workers introduction[](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-introduction)

[SharedWorker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker "The SharedWorker interface represents a specific kind of worker that can be accessed from several browsing contexts, such as several windows, iframes or even workers. They implement an interface different than dedicated workers and have a different global scope, SharedWorkerGlobalScope.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 5+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android 33+Safari iOS 16+Chrome Android No WebView Android?Samsung Internet 4.0–5.0 Opera Android 11–14

_This section is non-normative._

This section introduces shared workers using a Hello World example. Shared workers use slightly different APIs, since each worker can have multiple connections.

This first example shows how you connect to a worker and how a worker can send a message back to the page when it connects to it. Received messages are displayed in a log.

Here is the HTML page:

```
<!DOCTYPE HTML>
<html lang="en">
<meta charset="utf-8">
<title>Shared workers: demo 1</title>
<pre id="log">Log:</pre>
<script>
  var worker = new SharedWorker('test.js');
  var log = document.getElementById('log');
  worker.port.onmessage = function(e) { // note: not worker.onmessage!
    log.textContent += '\n' + e.data;
  }
</script>
```

Here is the JavaScript worker:

```
onconnect = function(e) {
  var port = e.ports[0];
  port.postMessage('Hello World!');
}
```

[View this example online](https://html.spec.whatwg.org/demos/workers/shared/001/test.html).

* * *

This second example extends the first one by changing two things: first, messages are received using `addEventListener()` instead of an [event handler IDL attribute](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes), and second, a message is sent _to_ the worker, causing the worker to send another message in return. Received messages are again displayed in a log.

Here is the HTML page:

```
<!DOCTYPE HTML>
<html lang="en">
<meta charset="utf-8">
<title>Shared workers: demo 2</title>
<pre id="log">Log:</pre>
<script>
  var worker = new SharedWorker('test.js');
  var log = document.getElementById('log');
  worker.port.addEventListener('message', function(e) {
    log.textContent += '\n' + e.data;
  }, false);
  worker.port.start(); // note: need this when using addEventListener
  worker.port.postMessage('ping');
</script>
```

Here is the JavaScript worker:

```
onconnect = function(e) {
  var port = e.ports[0];
  port.postMessage('Hello World!');
  port.onmessage = function(e) {
    port.postMessage('pong'); // not e.ports[0].postMessage!
    // e.target.postMessage('pong'); would work also
  }
}
```

[View this example online](https://html.spec.whatwg.org/demos/workers/shared/002/test.html).

* * *

Finally, the example is extended to show how two pages can connect to the same worker; in this case, the second page is merely in an `iframe` on the first page, but the same principle would apply to an entirely separate page in a separate [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable).

Here is the outer HTML page:

```
<!DOCTYPE HTML>
<html lang="en">
<meta charset="utf-8">
<title>Shared workers: demo 3</title>
<pre id="log">Log:</pre>
<script>
  var worker = new SharedWorker('test.js');
  var log = document.getElementById('log');
  worker.port.addEventListener('message', function(e) {
    log.textContent += '\n' + e.data;
  }, false);
  worker.port.start();
  worker.port.postMessage('ping');
</script>
<iframe src="inner.html"></iframe>
```

Here is the inner HTML page:

```
<!DOCTYPE HTML>
<html lang="en">
<meta charset="utf-8">
<title>Shared workers: demo 3 inner frame</title>
<pre id=log>Inner log:</pre>
<script>
  var worker = new SharedWorker('test.js');
  var log = document.getElementById('log');
  worker.port.onmessage = function(e) {
   log.textContent += '\n' + e.data;
  }
</script>
```

Here is the JavaScript worker:

```
var count = 0;
onconnect = function(e) {
  count += 1;
  var port = e.ports[0];
  port.postMessage('Hello World! You are connection #' + count);
  port.onmessage = function(e) {
    port.postMessage('pong');
  }
}
```

[View this example online](https://html.spec.whatwg.org/demos/workers/shared/003/test.html).

##### 10.1.2.4 Shared state using a shared worker[](https://html.spec.whatwg.org/multipage/workers.html#shared-state-using-a-shared-worker)

_This section is non-normative._

In this example, multiple windows (viewers) can be opened that are all viewing the same map. All the windows share the same map information, with a single worker coordinating all the viewers. Each viewer can move around independently, but if they set any data on the map, all the viewers are updated.

The main page isn't interesting, it merely provides a way to open the viewers:

```
<!DOCTYPE HTML>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>Workers example: Multiviewer</title>
  <script>
   function openViewer() {
     window.open('viewer.html');
   }
  </script>
 </head>
 <body>
  <p><button type=button onclick="openViewer()">Open a new
  viewer</button></p>
  <p>Each viewer opens in a new window. You can have as many viewers
  as you like, they all view the same data.</p>
 </body>
</html>
```

The viewer is more involved:

```
<!DOCTYPE HTML>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>Workers example: Multiviewer viewer</title>
  <script>
   var worker = new SharedWorker('worker.js', 'core');

   // CONFIGURATION
   function configure(event) {
     if (event.data.substr(0, 4) != 'cfg ') return;
     var name = event.data.substr(4).split(' ', 1)[0];
     // update display to mention our name is name
     document.getElementsByTagName('h1')[0].textContent += ' ' + name;
     // no longer need this listener
     worker.port.removeEventListener('message', configure, false);
   }
   worker.port.addEventListener('message', configure, false);

   // MAP
   function paintMap(event) {
     if (event.data.substr(0, 4) != 'map ') return;
     var data = event.data.substr(4).split(',');
     // display tiles data[0] .. data[8]
     var canvas = document.getElementById('map');
     var context = canvas.getContext('2d');
     for (var y = 0; y < 3; y += 1) {
       for (var x = 0; x < 3; x += 1) {
         var tile = data[y * 3 + x];
         if (tile == '0')
           context.fillStyle = 'green';
         else
           context.fillStyle = 'maroon';
         context.fillRect(x * 50, y * 50, 50, 50);
       }
     }
   }
   worker.port.addEventListener('message', paintMap, false);

   // PUBLIC CHAT
   function updatePublicChat(event) {
     if (event.data.substr(0, 4) != 'txt ') return;
     var name = event.data.substr(4).split(' ', 1)[0];
     var message = event.data.substr(4 + name.length + 1);
     // display "<name> message" in public chat
     var public = document.getElementById('public');
     var p = document.createElement('p');
     var n = document.createElement('button');
     n.textContent = '<' + name + '> ';
     n.onclick = function () { worker.port.postMessage('msg ' + name); };
     p.appendChild(n);
     var m = document.createElement('span');
     m.textContent = message;
     p.appendChild(m);
     public.appendChild(p);
   }
   worker.port.addEventListener('message', updatePublicChat, false);

   // PRIVATE CHAT
   function startPrivateChat(event) {
     if (event.data.substr(0, 4) != 'msg ') return;
     var name = event.data.substr(4).split(' ', 1)[0];
     var port = event.ports[0];
     // display a private chat UI
     var ul = document.getElementById('private');
     var li = document.createElement('li');
     var h3 = document.createElement('h3');
     h3.textContent = 'Private chat with ' + name;
     li.appendChild(h3);
     var div = document.createElement('div');
     var addMessage = function(name, message) {
       var p = document.createElement('p');
       var n = document.createElement('strong');
       n.textContent = '<' + name + '> ';
       p.appendChild(n);
       var t = document.createElement('span');
       t.textContent = message;
       p.appendChild(t);
       div.appendChild(p);
     };
     port.onmessage = function (event) {
       addMessage(name, event.data);
     };
     li.appendChild(div);
     var form = document.createElement('form');
     var p = document.createElement('p');
     var input = document.createElement('input');
     input.size = 50;
     p.appendChild(input);
     p.appendChild(document.createTextNode(' '));
     var button = document.createElement('button');
     button.textContent = 'Post';
     p.appendChild(button);
     form.onsubmit = function () {
       port.postMessage(input.value);
       addMessage('me', input.value);
       input.value = '';
       return false;
     };
     form.appendChild(p);
     li.appendChild(form);
     ul.appendChild(li);
   }
   worker.port.addEventListener('message', startPrivateChat, false);

   worker.port.start();
  </script>
 </head>
 <body>
  <h1>Viewer</h1>
  <h2>Map</h2>
  <p><canvas id="map" height=150 width=150></canvas></p>
  <p>
   <button type=button onclick="worker.port.postMessage('mov left')">Left</button>
   <button type=button onclick="worker.port.postMessage('mov up')">Up</button>
   <button type=button onclick="worker.port.postMessage('mov down')">Down</button>
   <button type=button onclick="worker.port.postMessage('mov right')">Right</button>
   <button type=button onclick="worker.port.postMessage('set 0')">Set 0</button>
   <button type=button onclick="worker.port.postMessage('set 1')">Set 1</button>
  </p>
  <h2>Public Chat</h2>
  <div id="public"></div>
  <form onsubmit="worker.port.postMessage('txt ' + message.value); message.value = ''; return false;">
   <p>
    <input type="text" name="message" size="50">
    <button>Post</button>
   </p>
  </form>
  <h2>Private Chat</h2>
  <ul id="private"></ul>
 </body>
</html>
```

There are several key things worth noting about the way the viewer is written.

**Multiple listeners**. Instead of a single message processing function, the code here attaches multiple event listeners, each one performing a quick check to see if it is relevant for the message. In this example it doesn't make much difference, but if multiple authors wanted to collaborate using a single port to communicate with a worker, it would allow for independent code instead of changes having to all be made to a single event handling function.

Registering event listeners in this way also allows you to unregister specific listeners when you are done with them, as is done with the `configure()` method in this example.

Finally, the worker:

```
var nextName = 0;
function getNextName() {
  // this could use more friendly names
  // but for now just return a number
  return nextName++;
}

var map = [
 [0, 0, 0, 0, 0, 0, 0],
 [1, 1, 0, 1, 0, 1, 1],
 [0, 1, 0, 1, 0, 0, 0],
 [0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 1, 0, 0, 0],
 [1, 0, 0, 1, 1, 1, 1],
 [1, 1, 0, 1, 1, 0, 1],
];

function wrapX(x) {
  if (x < 0) return wrapX(x + map[0].length);
  if (x >= map[0].length) return wrapX(x - map[0].length);
  return x;
}

function wrapY(y) {
  if (y < 0) return wrapY(y + map.length);
  if (y >= map[0].length) return wrapY(y - map.length);
  return y;
}

function wrap(val, min, max) {
  if (val < min)
    return val + (max-min)+1;
  if (val > max)
    return val - (max-min)-1;
  return val;
}

function sendMapData(viewer) {
  var data = '';
  for (var y = viewer.y-1; y <= viewer.y+1; y += 1) {
    for (var x = viewer.x-1; x <= viewer.x+1; x += 1) {
      if (data != '')
        data += ',';
      data += map[wrap(y, 0, map[0].length-1)][wrap(x, 0, map.length-1)];
    }
  }
  viewer.port.postMessage('map ' + data);
}

var viewers = {};
onconnect = function (event) {
  var name = getNextName();
  event.ports[0]._data = { port: event.ports[0], name: name, x: 0, y: 0, };
  viewers[name] = event.ports[0]._data;
  event.ports[0].postMessage('cfg ' + name);
  event.ports[0].onmessage = getMessage;
  sendMapData(event.ports[0]._data);
};

function getMessage(event) {
  switch (event.data.substr(0, 4)) {
    case 'mov ':
      var direction = event.data.substr(4);
      var dx = 0;
      var dy = 0;
      switch (direction) {
        case 'up': dy = -1; break;
        case 'down': dy = 1; break;
        case 'left': dx = -1; break;
        case 'right': dx = 1; break;
      }
      event.target._data.x = wrapX(event.target._data.x + dx);
      event.target._data.y = wrapY(event.target._data.y + dy);
      sendMapData(event.target._data);
      break;
    case 'set ':
      var value = event.data.substr(4);
      map[event.target._data.y][event.target._data.x] = value;
      for (var viewer in viewers)
        sendMapData(viewers[viewer]);
      break;
    case 'txt ':
      var name = event.target._data.name;
      var message = event.data.substr(4);
      for (var viewer in viewers)
        viewers[viewer].port.postMessage('txt ' + name + ' ' + message);
      break;
    case 'msg ':
      var party1 = event.target._data;
      var party2 = viewers[event.data.substr(4).split(' ', 1)[0]];
      if (party2) {
        var channel = new MessageChannel();
        party1.port.postMessage('msg ' + party2.name, [channel.port1]);
        party2.port.postMessage('msg ' + party1.name, [channel.port2]);
      }
      break;
  }
}
```

**Connecting to multiple pages**. The script uses the `onconnect` event listener to listen for multiple connections.

**Direct channels**. When the worker receives a "msg" message from one viewer naming another viewer, it sets up a direct connection between the two, so that the two viewers can communicate directly without the worker having to proxy all the messages.

[View this example online](https://html.spec.whatwg.org/demos/workers/multiviewer/page.html).

##### 10.1.2.5 Delegation[](https://html.spec.whatwg.org/multipage/workers.html#delegation)

_This section is non-normative._

With multicore CPUs becoming prevalent, one way to obtain better performance is to split computationally expensive tasks amongst multiple workers. In this example, a computationally expensive task that is to be performed for every number from 1 to 10,000,000 is farmed out to ten subworkers.

The main page is as follows, it just reports the result:

```
<!DOCTYPE HTML>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>Worker example: Multicore computation</title>
 </head>
 <body>
  <p>Result: <output id="result"></output></p>
  <script>
   var worker = new Worker('worker.js');
   worker.onmessage = function (event) {
     document.getElementById('result').textContent = event.data;
   };
  </script>
 </body>
</html>
```

The worker itself is as follows:

```
// settings
var num_workers = 10;
var items_per_worker = 1000000;

// start the workers
var result = 0;
var pending_workers = num_workers;
for (var i = 0; i < num_workers; i += 1) {
  var worker = new Worker('core.js');
  worker.postMessage(i * items_per_worker);
  worker.postMessage((i+1) * items_per_worker);
  worker.onmessage = storeResult;
}

// handle the results
function storeResult(event) {
  result += 1*event.data;
  pending_workers -= 1;
  if (pending_workers <= 0)
    postMessage(result); // finished!
}
```

It consists of a loop to start the subworkers, and then a handler that waits for all the subworkers to respond.

The subworkers are implemented as follows:

```
var start;
onmessage = getStart;
function getStart(event) {
  start = 1*event.data;
  onmessage = getEnd;
}

var end;
function getEnd(event) {
  end = 1*event.data;
  onmessage = null;
  work();
}

function work() {
  var result = 0;
  for (var i = start; i < end; i += 1) {
    // perform some complex calculation here
    result += 1;
  }
  postMessage(result);
  close();
}
```

They receive two numbers in two events, perform the computation for the range of numbers thus specified, and then report the result back to the parent.

[View this example online](https://html.spec.whatwg.org/demos/workers/multicore/page.html).

##### 10.1.2.6 Providing libraries[](https://html.spec.whatwg.org/multipage/workers.html#providing-libraries)

_This section is non-normative._

Suppose that a cryptography library is made available that provides three tasks:

Generate a public/private key pair Takes a port, on which it will send two messages, first the public key and then the private key.Given a plaintext and a public key, return the corresponding ciphertext Takes a port, to which any number of messages can be sent, the first giving the public key, and the remainder giving the plaintext, each of which is encrypted and then sent on that same channel as the ciphertext. The user can close the port when it is done encrypting content.Given a ciphertext and a private key, return the corresponding plaintext Takes a port, to which any number of messages can be sent, the first giving the private key, and the remainder giving the ciphertext, each of which is decrypted and then sent on that same channel as the plaintext. The user can close the port when it is done decrypting content.
The library itself is as follows:

```
function handleMessage(e) {
  if (e.data == "genkeys")
    genkeys(e.ports[0]);
  else if (e.data == "encrypt")
    encrypt(e.ports[0]);
  else if (e.data == "decrypt")
    decrypt(e.ports[0]);
}

function genkeys(p) {
  var keys = _generateKeyPair();
  p.postMessage(keys[0]);
  p.postMessage(keys[1]);
}

function encrypt(p) {
  var key, state = 0;
  p.onmessage = function (e) {
    if (state == 0) {
      key = e.data;
      state = 1;
    } else {
      p.postMessage(_encrypt(key, e.data));
    }
  };
}

function decrypt(p) {
  var key, state = 0;
  p.onmessage = function (e) {
    if (state == 0) {
      key = e.data;
      state = 1;
    } else {
      p.postMessage(_decrypt(key, e.data));
    }
  };
}

// support being used as a shared worker as well as a dedicated worker
if ('onmessage' in this) // dedicated worker
  onmessage = handleMessage;
else // shared worker
  onconnect = function (e) { e.port.onmessage = handleMessage; }

// the "crypto" functions:

function _generateKeyPair() {
  return [Math.random(), Math.random()];
}

function _encrypt(k, s) {
  return 'encrypted-' + k + ' ' + s;
}

function _decrypt(k, s) {
  return s.substr(s.indexOf(' ')+1);
}
```

Note that the crypto functions here are just stubs and don't do real cryptography.

This library could be used as follows:

```
<!DOCTYPE HTML>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>Worker example: Crypto library</title>
  <script>
   const cryptoLib = new Worker('libcrypto-v1.js'); // or could use 'libcrypto-v2.js'
   function startConversation(source, message) {
     const messageChannel = new MessageChannel();
     source.postMessage(message, [messageChannel.port2]);
     return messageChannel.port1;
   }
   function getKeys() {
     let state = 0;
     startConversation(cryptoLib, "genkeys").onmessage = function (e) {
       if (state === 0)
         document.getElementById('public').value = e.data;
       else if (state === 1)
         document.getElementById('private').value = e.data;
       state += 1;
     };
   }
   function enc() {
     const port = startConversation(cryptoLib, "encrypt");
     port.postMessage(document.getElementById('public').value);
     port.postMessage(document.getElementById('input').value);
     port.onmessage = function (e) {
       document.getElementById('input').value = e.data;
       port.close();
     };
   }
   function dec() {
     const port = startConversation(cryptoLib, "decrypt");
     port.postMessage(document.getElementById('private').value);
     port.postMessage(document.getElementById('input').value);
     port.onmessage = function (e) {
       document.getElementById('input').value = e.data;
       port.close();
     };
   }
  </script>
  <style>
   textarea { display: block; }
  </style>
 </head>
 <body onload="getKeys()">
  <fieldset>
   <legend>Keys</legend>
   <p><label>Public Key: <textarea id="public"></textarea></label></p>
   <p><label>Private Key: <textarea id="private"></textarea></label></p>
  </fieldset>
  <p><label>Input: <textarea id="input"></textarea></label></p>
  <p><button onclick="enc()">Encrypt</button> <button onclick="dec()">Decrypt</button></p>
 </body>
</html>
```

A later version of the API, though, might want to offload all the crypto work onto subworkers. This could be done as follows:

```
function handleMessage(e) {
  if (e.data == "genkeys")
    genkeys(e.ports[0]);
  else if (e.data == "encrypt")
    encrypt(e.ports[0]);
  else if (e.data == "decrypt")
    decrypt(e.ports[0]);
}

function genkeys(p) {
  var generator = new Worker('libcrypto-v2-generator.js');
  generator.postMessage('', [p]);
}

function encrypt(p) {
  p.onmessage = function (e) {
    var key = e.data;
    var encryptor = new Worker('libcrypto-v2-encryptor.js');
    encryptor.postMessage(key, [p]);
  };
}

function encrypt(p) {
  p.onmessage = function (e) {
    var key = e.data;
    var decryptor = new Worker('libcrypto-v2-decryptor.js');
    decryptor.postMessage(key, [p]);
  };
}

// support being used as a shared worker as well as a dedicated worker
if ('onmessage' in this) // dedicated worker
  onmessage = handleMessage;
else // shared worker
  onconnect = function (e) { e.ports[0].onmessage = handleMessage };
```

The little subworkers would then be as follows.

For generating key pairs:

```
onmessage = function (e) {
  var k = _generateKeyPair();
  e.ports[0].postMessage(k[0]);
  e.ports[0].postMessage(k[1]);
  close();
}

function _generateKeyPair() {
  return [Math.random(), Math.random()];
}
```

For encrypting:

```
onmessage = function (e) {
  var key = e.data;
  e.ports[0].onmessage = function (e) {
    var s = e.data;
    postMessage(_encrypt(key, s));
  }
}

function _encrypt(k, s) {
  return 'encrypted-' + k + ' ' + s;
}
```

For decrypting:

```
onmessage = function (e) {
  var key = e.data;
  e.ports[0].onmessage = function (e) {
    var s = e.data;
    postMessage(_decrypt(key, s));
  }
}

function _decrypt(k, s) {
  return s.substr(s.indexOf(' ')+1);
}
```

Notice how the users of the API don't have to even know that this is happening — the API hasn't changed; the library can delegate to subworkers without changing its API, even though it is accepting data using message channels.

[View this example online](https://html.spec.whatwg.org/demos/workers/crypto/page.html).

#### 10.1.3 Tutorials[](https://html.spec.whatwg.org/multipage/workers.html#tutorials)

##### 10.1.3.1 Creating a dedicated worker[](https://html.spec.whatwg.org/multipage/workers.html#creating-a-dedicated-worker)

_This section is non-normative._

Creating a worker requires a URL to a JavaScript file. The `Worker()` constructor is invoked with the URL to that file as its only argument; a worker is then created and returned:

`var worker = new Worker('helper.js');`
If you want your worker script to be interpreted as a [module script](https://html.spec.whatwg.org/multipage/webappapis.html#module-script) instead of the default [classic script](https://html.spec.whatwg.org/multipage/webappapis.html#classic-script), you need to use a slightly different signature:

`var worker = new Worker('helper.mjs', { type: "module" });`
##### 10.1.3.2 Communicating with a dedicated worker[](https://html.spec.whatwg.org/multipage/workers.html#communicating-with-a-dedicated-worker)

_This section is non-normative._

Dedicated workers use `MessagePort` objects behind the scenes, and thus support all the same features, such as sending structured data, transferring binary data, and transferring other ports.

To receive messages from a dedicated worker, use the `onmessage`[event handler IDL attribute](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes) on the `Worker` object:

`worker.onmessage = function (event) { ... };`
You can also use the `addEventListener()` method.

The implicit `MessagePort` used by dedicated workers has its [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) implicitly enabled when it is created, so there is no equivalent to the `MessagePort` interface's `start()` method on the `Worker` interface.

To _send_ data to a worker, use the `postMessage()` method. Structured data can be sent over this communication channel. To send `ArrayBuffer` objects efficiently (by transferring them rather than cloning them), list them in an array in the second argument.

```
worker.postMessage({
  operation: 'find-edges',
  input: buffer, // an ArrayBuffer object
  threshold: 0.6,
}, [buffer]);
```

To receive a message inside the worker, the `onmessage`[event handler IDL attribute](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes) is used.

`onmessage = function (event) { ... };`
You can again also use the `addEventListener()` method.

In either case, the data is provided in the event object's `data` attribute.

To send messages back, you again use `postMessage()`. It supports the structured data in the same manner.

`postMessage(event.data.input, [event.data.input]); // transfer the buffer back`
##### 10.1.3.3 Shared workers[](https://html.spec.whatwg.org/multipage/workers.html#shared-workers)

[SharedWorker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker "The SharedWorker interface represents a specific kind of worker that can be accessed from several browsing contexts, such as several windows, iframes or even workers. They implement an interface different than dedicated workers and have a different global scope, SharedWorkerGlobalScope.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 5+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android 33+Safari iOS 16+Chrome Android No WebView Android?Samsung Internet 4.0–5.0 Opera Android 11–14

_This section is non-normative._

Shared workers are identified by the URL of the script used to create it, optionally with an explicit name. The name allows multiple instances of a particular shared worker to be started.

Shared workers are scoped by [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin). Two different sites using the same names will not collide. However, if a page tries to use the same shared worker name as another page on the same site, but with a different script URL, it will fail.

Creating shared workers is done using the `SharedWorker()` constructor. This constructor takes the URL to the script to use for its first argument, and the name of the worker, if any, as the second argument.

`var worker = new SharedWorker('service.js');`
Communicating with shared workers is done with explicit `MessagePort` objects. The object returned by the `SharedWorker()` constructor holds a reference to the port on its `port` attribute.

```
worker.port.onmessage = function (event) { ... };
worker.port.postMessage('some message');
worker.port.postMessage({ foo: 'structured', bar: ['data', 'also', 'possible']});
```

Inside the shared worker, new clients of the worker are announced using the `connect` event. The port for the new client is given by the event object's `source` attribute.

```
onconnect = function (event) {
  var newPort = event.source;
  // set up a listener
  newPort.onmessage = function (event) { ... };
  // send a message back to the port
  newPort.postMessage('ready!'); // can also send structured data, of course
};
```

### 10.2 Infrastructure[](https://html.spec.whatwg.org/multipage/workers.html#infrastructure-2)

This standard defines two kinds of workers: dedicated workers, and shared workers. Dedicated workers, once created, are linked to their creator, but message ports can be used to communicate from a dedicated worker to multiple other browsing contexts or workers. Shared workers, on the other hand, are named, and once created any script running in the same [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) can obtain a reference to that worker and communicate with it. Service Workers defines a third kind. [[SW]](https://html.spec.whatwg.org/multipage/references.html#refsSW)

#### 10.2.1 The global scope[](https://html.spec.whatwg.org/multipage/workers.html#the-global-scope)

The global scope is the "inside" of a worker.

##### 10.2.1.1 The `WorkerGlobalScope` common interface[](https://html.spec.whatwg.org/multipage/workers.html#the-workerglobalscope-common-interface)

[WorkerGlobalScope](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope "The WorkerGlobalScope interface of the Web Workers API is an interface representing the scope of any worker. Workers have no browsing context; this scope contains the information usually conveyed by Window objects — in this case event handlers, the console or the associated WorkerNavigator object. Each WorkerGlobalScope has its own event loop.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

```
[Exposed=Worker]
interface WorkerGlobalScope : EventTarget {
  readonly attribute WorkerGlobalScope self;
  readonly attribute WorkerLocation location;
  readonly attribute WorkerNavigator navigator;
  undefined importScripts((TrustedScriptURL or USVString)... urls);

  attribute OnErrorEventHandler onerror;
  attribute EventHandler onlanguagechange;
  attribute EventHandler onoffline;
  attribute EventHandler ononline;
  attribute EventHandler onrejectionhandled;
  attribute EventHandler onunhandledrejection;
};
```

`WorkerGlobalScope` serves as the base class for specific types of worker global scope objects, including `DedicatedWorkerGlobalScope`, `SharedWorkerGlobalScope`, and `ServiceWorkerGlobalScope`.

A `WorkerGlobalScope` object has an associated owner set (a [set](https://infra.spec.whatwg.org/#ordered-set) of `Document` and `WorkerGlobalScope` objects). It is initially empty and populated when the worker is created or obtained.

It is a [set](https://infra.spec.whatwg.org/#ordered-set), instead of a single owner, to accommodate `SharedWorkerGlobalScope` objects.

A `WorkerGlobalScope` object has an associated type ("`classic`" or "`module`"). It is set during creation.

A `WorkerGlobalScope` object has an associated url (null or a [URL](https://url.spec.whatwg.org/#concept-url)). It is initially null.

A `WorkerGlobalScope` object has an associated name (a string). It is set during creation.

The [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name) can have different semantics for each subclass of `WorkerGlobalScope`. For `DedicatedWorkerGlobalScope` instances, it is simply a developer-supplied name, useful mostly for debugging purposes. For `SharedWorkerGlobalScope` instances, it allows obtaining a reference to a common shared worker via the `SharedWorker()` constructor. For `ServiceWorkerGlobalScope` objects, it doesn't make sense (and as such isn't exposed through the JavaScript API at all).

A `WorkerGlobalScope` object has an associated policy container (a [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container)). It is initially a new [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container).

A `WorkerGlobalScope` object has an associated embedder policy (an [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy)).

A `WorkerGlobalScope` object has an associated module map. It is a [module map](https://html.spec.whatwg.org/multipage/webappapis.html#module-map), initially empty.

A `WorkerGlobalScope` object has an associated cross-origin isolated capability boolean. It is initially false.

`workerGlobal.self`

[WorkerGlobalScope/self](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/self "The self read-only property of the WorkerGlobalScope interface returns a reference to the WorkerGlobalScope itself. Most of the time it is a specific scope like DedicatedWorkerGlobalScope, SharedWorkerGlobalScope, or ServiceWorkerGlobalScope.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 11.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android 34+Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns workerGlobal.`workerGlobal.location`

[WorkerGlobalScope/location](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/location "The location read-only property of the WorkerGlobalScope interface returns the WorkerLocation associated with the worker. It is a specific location object, mostly a subset of the Location for browsing scopes, but adapted to workers.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 11.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns workerGlobal's `WorkerLocation` object.`workerGlobal.navigator`

[WorkerGlobalScope/navigator](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/navigator "The navigator read-only property of the WorkerGlobalScope interface returns the WorkerNavigator associated with the worker. It is a specific navigator object, mostly a subset of the Navigator for browsing scopes, but adapted to workers.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 11.5+Edge 79+

* * *

Edge (Legacy)17+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns workerGlobal's `WorkerNavigator` object.`workerGlobal.importScripts(...urls)`

[WorkerGlobalScope/importScripts](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/importScripts "The importScripts() method of the WorkerGlobalScope interface synchronously imports one or more scripts into the worker's scope.")

Support in all current engines.

Firefox 4+Safari 4+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Fetches each [URL](https://url.spec.whatwg.org/#concept-url) in urls, executes them one-by-one in the order they are passed, and then returns (or throws if something went amiss).
The `self` attribute must return the `WorkerGlobalScope` object itself.

The `location` attribute must return the `WorkerLocation` object whose associated [`WorkerGlobalScope` object](https://html.spec.whatwg.org/multipage/workers.html#concept-workerlocation-workerglobalscope) is the `WorkerGlobalScope` object.

While the `WorkerLocation` object is created after the `WorkerGlobalScope` object, this is not problematic as it cannot be observed from script.

* * *

The following are the [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) (and their corresponding [event handler event types](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type)) that must be supported, as [event handler IDL attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes), by objects implementing the `WorkerGlobalScope` interface:

| [Event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) | [Event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) |
| --- | --- |
| `onerror` [WorkerGlobalScope/error_event](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/error_event "The error event of the WorkerGlobalScope interface fires when an error occurs in the worker.") Support in all current engines. Firefox 3.5+Safari 4+Chrome 4+ * * * Opera 11.5+Edge 79+ * * * Edge (Legacy)12+Internet Explorer 10+ * * * Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android? | `error` |
| `onlanguagechange` [WorkerGlobalScope/languagechange_event](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/languagechange_event "The languagechange event is fired at the global scope object when the user's preferred language changes.") Support in all current engines. Firefox 74+Safari 4+Chrome 4+ * * * Opera 11.5+Edge 79+ * * * Edge (Legacy)?Internet Explorer No * * * Firefox Android?Safari iOS 5+Chrome Android?WebView Android 37+Samsung Internet?Opera Android? | `languagechange` |
| `onoffline` [WorkerGlobalScope/offline_event](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/offline_event "The offline event of the WorkerGlobalScope fires when the device loses connection to the internet.") Firefox 29+Safari 8+Chrome No * * * Opera?Edge No * * * Edge (Legacy)?Internet Explorer No * * * Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android? | `offline` |
| `ononline` [WorkerGlobalScope/online_event](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/online_event "The online event of the WorkerGlobalScope fires when the device reconnects to the internet.") Firefox 29+Safari 8+Chrome No * * * Opera?Edge No * * * Edge (Legacy)?Internet Explorer No * * * Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android? | `online` |
| `onrejectionhandled` | `rejectionhandled` |
| `onunhandledrejection` | `unhandledrejection` |

##### 10.2.1.2 Dedicated workers and the `DedicatedWorkerGlobalScope` interface[](https://html.spec.whatwg.org/multipage/workers.html#dedicated-workers-and-the-dedicatedworkerglobalscope-interface)

[DedicatedWorkerGlobalScope](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope "The DedicatedWorkerGlobalScope object (the Worker global scope) is accessible through the self keyword. Some additional global functions, namespaces objects, and constructors, not typically associated with the worker global scope, but available on it, are listed in the JavaScript Reference. See also: Functions available to workers.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

```
[Global=(Worker,DedicatedWorker),Exposed=DedicatedWorker]
interface DedicatedWorkerGlobalScope : WorkerGlobalScope {
  [Replaceable] readonly attribute DOMString name;

  undefined postMessage(any message, sequence<object> transfer);
  undefined postMessage(any message, optional StructuredSerializeOptions options = {});

  undefined close();
};

DedicatedWorkerGlobalScope includes MessageEventTarget;
```

`DedicatedWorkerGlobalScope` objects have an associated inside port (a `MessagePort`). This port is part of a channel that is set up when the worker is created, but it is not exposed. This object must never be garbage collected before the `DedicatedWorkerGlobalScope` object.

`dedicatedWorkerGlobal.name`

[DedicatedWorkerGlobalScope/name](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/name "The name read-only property of the DedicatedWorkerGlobalScope interface returns the name that the Worker was (optionally) given when it was created. This is the name that the Worker() constructor can pass to get a reference to the DedicatedWorkerGlobalScope.")

Support in all current engines.

Firefox 55+Safari 12.1+Chrome 70+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns dedicatedWorkerGlobal's [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name), i.e. the value given to the `Worker` constructor. Primarily useful for debugging.

`dedicatedWorkerGlobal.postMessage(message [, transfer ])`

[DedicatedWorkerGlobalScope/postMessage](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/postMessage "The postMessage() method of the DedicatedWorkerGlobalScope interface sends a message to the main thread that spawned it.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

`dedicatedWorkerGlobal.postMessage(message [, { transfer } ])`
Clones message and transmits it to the `Worker` object associated with dedicatedWorkerGlobal. transfer can be passed as a list of objects that are to be transferred rather than cloned.

`dedicatedWorkerGlobal.close()`

[DedicatedWorkerGlobalScope/close](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/close "The close() method of the DedicatedWorkerGlobalScope interface discards any tasks queued in the DedicatedWorkerGlobalScope's event loop, effectively closing this particular scope.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Aborts dedicatedWorkerGlobal.

The `name` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name). Its value represents the name given to the worker using the `Worker` constructor, used primarily for debugging purposes.

The 
```
postMessage(message,
  transfer)
```
 and 
```
postMessage(message,
  options)
```
 methods on `DedicatedWorkerGlobalScope` objects act as if, when invoked, it immediately invoked the respective `postMessage(message, transfer)` and 
```
postMessage(message,
  options)
```
 on the port, with the same arguments, and returned the same return value.

To close a worker, given a workerGlobal, run these steps:

1.   Discard any [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that have been added to workerGlobal's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop)'s [task queues](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue).

2.   Set workerGlobal's [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag to true. (This prevents any further tasks from being queued.)

The `close()` method steps are to [close a worker](https://html.spec.whatwg.org/multipage/workers.html#close-a-worker) given [this](https://webidl.spec.whatwg.org/#this).

* * *

##### 10.2.1.3 Shared workers and the `SharedWorkerGlobalScope` interface[](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-and-the-sharedworkerglobalscope-interface)

[SharedWorkerGlobalScope](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorkerGlobalScope "The SharedWorkerGlobalScope object (the SharedWorker global scope) is accessible through the self keyword. Some additional global functions, namespaces objects, and constructors, not typically associated with the worker global scope, but available on it, are listed in the JavaScript Reference. See the complete list of functions available to workers.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS 16+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

```
[Global=(Worker,SharedWorker),Exposed=SharedWorker]
interface SharedWorkerGlobalScope : WorkerGlobalScope {
  [Replaceable] readonly attribute DOMString name;

  undefined close();

  attribute EventHandler onconnect;
};
```

A `SharedWorkerGlobalScope` object has associated constructor origin (an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)), constructor URL (a [URL record](https://url.spec.whatwg.org/#concept-url)), and credentials (a [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode)), and extended lifetime (a boolean). They are initialized when the `SharedWorkerGlobalScope` object is created, in the [run a worker](https://html.spec.whatwg.org/multipage/workers.html#run-a-worker) algorithm.

Shared workers receive message ports through `connect` events on their `SharedWorkerGlobalScope` object for each connection.

`sharedWorkerGlobal.name`

[SharedWorkerGlobalScope/name](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorkerGlobalScope/name "The name read-only property of the SharedWorkerGlobalScope interface returns the name that the SharedWorker was (optionally) given when it was created. This is the name that the SharedWorker() constructor can pass to get a reference to the SharedWorkerGlobalScope.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS 16+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Returns sharedWorkerGlobal's [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name), i.e. the value given to the `SharedWorker` constructor. Multiple `SharedWorker` objects can correspond to the same shared worker (and `SharedWorkerGlobalScope`), by reusing the same name.

`sharedWorkerGlobal.close()`

[SharedWorkerGlobalScope/close](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorkerGlobalScope/close "The close() method of the SharedWorkerGlobalScope interface discards any tasks queued in the SharedWorkerGlobalScope's event loop, effectively closing this particular scope.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS 16+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Aborts sharedWorkerGlobal.

The `name` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name). Its value represents the name that can be used to obtain a reference to the worker using the `SharedWorker` constructor.

The `close()` method steps are to [close a worker](https://html.spec.whatwg.org/multipage/workers.html#close-a-worker) given [this](https://webidl.spec.whatwg.org/#this).

* * *

The following are the [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) (and their corresponding [event handler event types](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type)) that must be supported, as [event handler IDL attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes), by objects implementing the `SharedWorkerGlobalScope` interface:

| [Event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) | [Event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) |
| --- | --- |
| `onconnect` [SharedWorkerGlobalScope/connect_event](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorkerGlobalScope/connect_event "The connect event is fired in shared workers at their SharedWorkerGlobalScope when a new client connects.") Support in all current engines. Firefox 29+Safari 16+Chrome 4+ * * * Opera 10.6+Edge 79+ * * * Edge (Legacy)?Internet Explorer No * * * Firefox Android?Safari iOS 16+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+ | `connect` |

#### 10.2.2 The event loop[](https://html.spec.whatwg.org/multipage/workers.html#worker-event-loop)

A [worker event loop](https://html.spec.whatwg.org/multipage/webappapis.html#worker-event-loop-2)'s [task queues](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) only have events, callbacks, and networking activity as [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task). These [worker event loops](https://html.spec.whatwg.org/multipage/webappapis.html#worker-event-loop-2) are created by the [run a worker](https://html.spec.whatwg.org/multipage/workers.html#run-a-worker) algorithm.

Each `WorkerGlobalScope` object has a closing flag, which must be initially false, but which can get set to true by the algorithms in the processing model section below.

Once the `WorkerGlobalScope`'s [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag is set to true, the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop)'s [task queues](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) must discard any further [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that would be added to them (tasks already on the queue are unaffected except where otherwise specified). Effectively, once the [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag is true, timers stop firing, notifications for all pending background operations are dropped, etc.

#### 10.2.3 The worker's lifetime[](https://html.spec.whatwg.org/multipage/workers.html#the-worker's-lifetime)

Workers communicate with other workers and with `Window`s through [message channels](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-messaging) and their `MessagePort` objects.

Each `WorkerGlobalScope` object worker global scope has a list of the worker's ports, which consists of all the `MessagePort` objects that are entangled with another port and that have one (but only one) port owned by worker global scope. This list includes the implicit `MessagePort` in the case of [dedicated workers](https://html.spec.whatwg.org/multipage/workers.html#dedicatedworkerglobalscope).

Given an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)o when creating or obtaining a worker, the relevant owner to add depends on the type of [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-global) specified by o. If o's [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-global) is a `WorkerGlobalScope` object (i.e., if we are creating a nested dedicated worker), then the relevant owner is that global object. Otherwise, o's [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-global) is a `Window` object, and the relevant owner is that `Window`'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window).

* * *

A user agent has an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) value, the between-loads shared worker timeout, which is some small amount of time. This represents how long the user agent allows shared workers to survive while a page is loading, in case that page is going to contact the shared worker again. Setting this value to greater than zero lets user agents avoid the cost of restarting a shared worker used by a site when the user is navigating from page to page within that site.

A typical value for the [between-loads shared worker timeout](https://html.spec.whatwg.org/multipage/workers.html#between-loads-shared-worker-timeout) might be 5 seconds.

A user agent has an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) value, the extended lifetime shared worker timeout, which is some amount of time. This represents how long the user agent allows shared workers which the web developer has requested be given an extended lifetime, to survive and perform work after all of their [owners](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set) have disappeared. User agents should choose a value that is equal to the longest lifetime that a service worker can stay alive without any [clients](https://w3c.github.io/ServiceWorker/#dfn-service-worker-client), and must not choose a value that is longer than that amount of time.

A typical value for the [extended lifetime shared worker timeout](https://html.spec.whatwg.org/multipage/workers.html#extended-lifetime-shared-worker-timeout) could be anywhere from 10 seconds to 5 minutes, depending on the implementation's individual policies regarding background work being performed by an origin without a user-visible representation.

* * *

A `WorkerGlobalScope`global is in extended lifetime if the following algorithm returns true:

1.   If global is not a `SharedWorkerGlobalScope`, then return false.

2.   If global's [extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-extended-lifetime) is false, then return false.

3.   If global's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set)[is empty](https://infra.spec.whatwg.org/#list-is-empty), but has been empty for less than the user agent's [extended lifetime shared worker timeout](https://html.spec.whatwg.org/multipage/workers.html#extended-lifetime-shared-worker-timeout), then return true.

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)owner of global's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set):

    1.   If owner is a `Document` that is [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return false:

In this case global will be [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker), but it's not in extended lifetime.

5.   [For each](https://infra.spec.whatwg.org/#list-iterate)owner of global's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set):

    1.   If owner is a `Document` and the amount of time that owner that has been non-[fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) is less than the user agent's [extended lifetime shared worker timeout](https://html.spec.whatwg.org/multipage/workers.html#extended-lifetime-shared-worker-timeout), then return true.

    2.   If owner is a `WorkerGlobalScope` that is [in extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#in-extended-lifetime-worker), then return true.

6.   Return false.

A `WorkerGlobalScope`global is actively needed if the following algorithm returns true:

1.   If global is [in extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#in-extended-lifetime-worker), then return true.

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)owner of global's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set):

    1.   If owner is a `Document`, and owner is [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return true.

    2.   If owner is a `WorkerGlobalScope` that is [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker), then return true.

3.   Return false.

A `WorkerGlobalScope`global is protected if the following algorithm returns true:

1.   If global is not [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker), then return false.

2.   If global is [in extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#in-extended-lifetime-worker), then return true.

3.   If global is a `SharedWorkerGlobalScope`, then return true.

4.   If global's [the worker's ports](https://html.spec.whatwg.org/multipage/workers.html#the-worker's-ports) is not [empty](https://infra.spec.whatwg.org/#list-is-empty), then return true.

5.   If global has outstanding timers, database transactions, or network connections, then return true.

6.   Return false.

A `WorkerGlobalScope`global is permissible if the following algorithm returns true:

1.   If global's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set) is not [empty](https://infra.spec.whatwg.org/#list-is-empty), then return true.

2.   If global is [in extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#in-extended-lifetime-worker), then return true.

3.   If all of the following are true:

    *   global is a `SharedWorkerGlobalScope`;

    *   global's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set) has been [empty](https://infra.spec.whatwg.org/#list-is-empty) for no more than the user agent's [between-loads shared worker timeout](https://html.spec.whatwg.org/multipage/workers.html#between-loads-shared-worker-timeout); and

    *   the user agent has a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) whose [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) is not [completely loaded](https://html.spec.whatwg.org/multipage/document-lifecycle.html#completely-loaded),

then return true.

4.   Return false.

The following relationships hold between these terms:

*   Every `WorkerGlobalScope` that is [in extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#in-extended-lifetime-worker) is [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker), [protected](https://html.spec.whatwg.org/multipage/workers.html#protected-worker), and [permissible](https://html.spec.whatwg.org/multipage/workers.html#permissible-worker).

*   Every `WorkerGlobalScope` that is [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker) or [protected](https://html.spec.whatwg.org/multipage/workers.html#protected-worker) is [permissible](https://html.spec.whatwg.org/multipage/workers.html#permissible-worker).

*   Every `WorkerGlobalScope` that is [protected](https://html.spec.whatwg.org/multipage/workers.html#protected-worker) is [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker).

However, the converses do not always hold:

*   A `WorkerGlobalScope` can be [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker) but not [protected](https://html.spec.whatwg.org/multipage/workers.html#protected-worker), if it's a dedicated worker with no outstanding async work that is still performing computation on behalf of a fully active owner, but whose corresponding `Worker` object has been garbage collected. [Because of the garbage collection](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-and-garbage-collection), the [ports](https://html.spec.whatwg.org/multipage/workers.html#the-worker's-ports) collection is empty, so it is no longer protected. However, its event loop has not yet yielded to [empty its owner set](https://html.spec.whatwg.org/multipage/workers.html#step-empty-worker-global-scope-owner-set), so it is still actively needed.

*   A `WorkerGlobalScope` can be [permissible](https://html.spec.whatwg.org/multipage/workers.html#permissible-worker) but not [protected](https://html.spec.whatwg.org/multipage/workers.html#protected-worker) or [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker), if all the `Document`s in its transitive set of owners are in [bfcache](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-bfcache), or if it's a `SharedWorkerGlobalScope` with no current owners being kept alive for the duration of the [between-loads shared worker timeout](https://html.spec.whatwg.org/multipage/workers.html#between-loads-shared-worker-timeout).

A `WorkerGlobalScope`global is suspendable if the following algorithm returns true:

1.   If global is [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker), then return false.

2.   If global is [permissible](https://html.spec.whatwg.org/multipage/workers.html#permissible-worker), then return true.

3.   Return false.

These concepts are used elsewhere in the specification's normative requirements as follows:

*   Workers get [closed as orphans](https://html.spec.whatwg.org/multipage/workers.html#step-closing-orphan-workers) between when they stop being [protected](https://html.spec.whatwg.org/multipage/workers.html#protected-worker) and when they stop being [permissible](https://html.spec.whatwg.org/multipage/workers.html#permissible-worker).

*   Workers that have been closed, but keep executing, [can be terminated](https://html.spec.whatwg.org/multipage/workers.html#terminate-rampant-workers) at the user agent's discretion, once they stop being [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker).

*   Workers get [suspended or un-suspended](https://html.spec.whatwg.org/multipage/workers.html#step-suspending-workers) based on whether they are [suspendable](https://html.spec.whatwg.org/multipage/workers.html#suspendable-worker).

#### 10.2.4 Processing model[](https://html.spec.whatwg.org/multipage/workers.html#worker-processing-model)

When a user agent is to run a worker for a script with `Worker` or `SharedWorker` object worker, [URL](https://url.spec.whatwg.org/#concept-url)url, [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)outside settings, `MessagePort`outside port, and a `WorkerOptions` dictionary options, it must run the following steps.

1.   Let is shared be true if worker is a `SharedWorker` object, and false otherwise.

2.   Let owner be the [relevant owner to add](https://html.spec.whatwg.org/multipage/workers.html#relevant-owner-to-add) given outside settings.

3.   Let unsafeWorkerCreationTime be the [unsafe shared current time](https://w3c.github.io/hr-time/#dfn-unsafe-shared-current-time).

4.   Let agent be the result of [obtaining a dedicated/shared worker agent](https://html.spec.whatwg.org/multipage/webappapis.html#obtain-a-dedicated/shared-worker-agent) given outside settings and is shared. Run the rest of these steps in that agent.

5.   Let realm execution context be the result of [creating a new realm](https://html.spec.whatwg.org/multipage/webappapis.html#creating-a-new-javascript-realm) given agent and the following customizations:

    *   For the global object, if is shared is true, create a new `SharedWorkerGlobalScope` object. Otherwise, create a new `DedicatedWorkerGlobalScope` object.

6.   Let worker global scope be the [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global) of realm execution context's Realm component.

This is the `DedicatedWorkerGlobalScope` or `SharedWorkerGlobalScope` object created in the previous step.

7.   [Set up a worker environment settings object](https://html.spec.whatwg.org/multipage/workers.html#set-up-a-worker-environment-settings-object) with realm execution context, outside settings, and unsafeWorkerCreationTime, and let inside settings be the result.

8.   Set worker global scope's [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name) to options["`name`"].

9.   [Append](https://infra.spec.whatwg.org/#set-append)owner to worker global scope's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set).

10.   If is shared is true, then:

    1.   Set worker global scope's [constructor origin](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-constructor-origin) to outside settings's [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

    2.   Set worker global scope's [constructor URL](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-constructor-url) to url.

    3.   Set worker global scope's [type](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-type) to options["`type`"].

    4.   Set worker global scope's [credentials](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-credentials) to options["`credentials`"].

    5.   Set worker global scope's [extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-extended-lifetime) to options["`extendedLifetime`"].

11.   Let destination be "`sharedworker`" if is shared is true, and "`worker`" otherwise.

12.   Obtain script by switching on options["`type`"]:

"`classic`"[Fetch a classic worker script](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-classic-worker-script) given url, outside settings, destination, inside settings, and with onComplete and performFetch as defined below."`module`"[Fetch a module worker script graph](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-module-worker-script-tree) given url, outside settings, destination, the value of the `credentials` member of options, inside settings, and with onComplete and performFetch as defined below.
In both cases, let performFetch be the following [perform the fetch hook](https://html.spec.whatwg.org/multipage/webappapis.html#fetching-scripts-perform-fetch) given request, [isTopLevel](https://html.spec.whatwg.org/multipage/webappapis.html#fetching-scripts-is-top-level), and [processCustomFetchResponse](https://html.spec.whatwg.org/multipage/webappapis.html#fetching-scripts-processcustomfetchresponse):

    1.   If isTopLevel is false, [fetch](https://fetch.spec.whatwg.org/#concept-fetch)request with _[processResponseConsumeBody](https://fetch.spec.whatwg.org/#process-response-end-of-body)_ set to processCustomFetchResponse, and abort these steps.

    2.   Set request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client) to inside settings.
    3.   [Fetch](https://fetch.spec.whatwg.org/#concept-fetch)request with _[processResponseConsumeBody](https://fetch.spec.whatwg.org/#process-response-end-of-body)_ set to the following steps given [response](https://fetch.spec.whatwg.org/#concept-response)response and null, failure, or a [byte sequence](https://infra.spec.whatwg.org/#byte-sequence)bodyBytes:

        1.   Set worker global scope's [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url) to response's [url](https://fetch.spec.whatwg.org/#concept-response-url).

        2.   Set inside settings's [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url) to response's [url](https://fetch.spec.whatwg.org/#concept-response-url).

        3.   [Initialize worker global scope's policy container](https://html.spec.whatwg.org/multipage/browsers.html#initialize-worker-policy-container) given worker global scope, response, and inside settings.

        4.   If the [Run CSP initialization for a global object](https://w3c.github.io/webappsec-csp/#run-global-object-csp-initialization) algorithm returns "`Blocked`" when executed upon worker global scope, set response to a [network error](https://fetch.spec.whatwg.org/#concept-network-error). [[CSP]](https://html.spec.whatwg.org/multipage/references.html#refsCSP)

        5.   If worker global scope's [embedder policy](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-embedder-policy)'s [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation) and is shared is true, then set agent's [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters)'s [cross-origin isolation mode](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-cross-origin-isolation) to "`logical`" or "`concrete`". The one chosen is [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined).

This really ought to be set when the agent cluster is created, which requires a redesign of this section.

        6.   If the result of [checking a global object's embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#check-a-global-object's-embedder-policy) with worker global scope, outside settings, and response is false, then set response to a [network error](https://fetch.spec.whatwg.org/#concept-network-error).

        7.   Set worker global scope's [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-cross-origin-isolated-capability) to true if agent's [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters)'s [cross-origin isolation mode](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-cross-origin-isolation) is "`concrete`".

        8.   If is shared is false and owner's [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability) is false, then set worker global scope's [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-cross-origin-isolated-capability) to false.

        9.   If is shared is false and response's [url](https://fetch.spec.whatwg.org/#concept-response-url)'s [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`data`", then set worker global scope's [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-cross-origin-isolated-capability) to false.

This is a conservative default for now, while we figure out how workers in general, and `data:` URL workers in particular (which are cross-origin from their owner), will be treated in the context of permissions policies. See [w3c/webappsec-permissions-policy issue #207](https://github.com/w3c/webappsec-permissions-policy/issues/207) for more details.

        10.   Run processCustomFetchResponse with response and bodyBytes.

In both cases, let onComplete given script be the following steps:

    1.   If script is null or if script's [error to rethrow](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-error-to-rethrow) is non-null, then:

        1.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given worker's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `error` at worker.

        2.   Run the [environment discarding steps](https://html.spec.whatwg.org/multipage/webappapis.html#environment-discarding-steps) for inside settings.

        3.   Abort these steps.

    2.   Associate worker with worker global scope.

    3.   Let inside port be a [new](https://webidl.spec.whatwg.org/#new)`MessagePort` object in inside settings's [realm](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object's-realm).

    4.   If is shared is false, then:

        1.   Set inside port's [message event target](https://html.spec.whatwg.org/multipage/web-messaging.html#message-event-target) to worker global scope.

        2.   Set worker global scope's [inside port](https://html.spec.whatwg.org/multipage/workers.html#inside-port) to inside port.

    5.   [Entangle](https://html.spec.whatwg.org/multipage/web-messaging.html#entangle)outside port and inside port.

    6.   Create a new `WorkerLocation` object and associate it with worker global scope.

    7.   _Closing orphan workers_: Start monitoring worker global scope such that no sooner than it stops being [protected](https://html.spec.whatwg.org/multipage/workers.html#protected-worker), and no later than it stops being [permissible](https://html.spec.whatwg.org/multipage/workers.html#permissible-worker), worker global scope's [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag is set to true.

    8.   _Suspending workers_: Start monitoring worker global scope, such that whenever worker global scope's [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag is false and it is [suspendable](https://html.spec.whatwg.org/multipage/workers.html#suspendable-worker), the user agent suspends execution of script in worker global scope until such time as either the [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag switches to true or worker global scope stops being [suspendable](https://html.spec.whatwg.org/multipage/workers.html#suspendable-worker).

    9.   Set inside settings's [execution ready flag](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-execution-ready-flag).

    10.   If script is a [classic script](https://html.spec.whatwg.org/multipage/webappapis.html#classic-script), then [run the classic script](https://html.spec.whatwg.org/multipage/webappapis.html#run-a-classic-script)script. Otherwise, it is a [module script](https://html.spec.whatwg.org/multipage/webappapis.html#module-script); [run the module script](https://html.spec.whatwg.org/multipage/webappapis.html#run-a-module-script)script.

In addition to the usual possibilities of returning a value or failing due to an exception, this could be [prematurely aborted](https://html.spec.whatwg.org/multipage/webappapis.html#abort-a-running-script) by the [terminate a worker](https://html.spec.whatwg.org/multipage/workers.html#terminate-a-worker) algorithm defined below.

    11.   Enable outside port's [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue).

    12.   If is shared is false, enable the [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) of the worker's implicit port.

    13.   If is shared is true, then [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given worker global scope to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `connect` at worker global scope, using `MessageEvent`, with the `data` attribute initialized to the empty string, the `ports` attribute initialized to a new [frozen array](https://webidl.spec.whatwg.org/#dfn-frozen-array-type) containing inside port, and the `source` attribute initialized to inside port.

    14.   Enable the [client message queue](https://w3c.github.io/ServiceWorker/#dfn-client-message-queue) of the `ServiceWorkerContainer` object whose associated [service worker client](https://w3c.github.io/ServiceWorker/#serviceworkercontainer-service-worker-client) is worker global scope's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

    15.   _Event loop_: Run the [responsible event loop](https://html.spec.whatwg.org/multipage/webappapis.html#responsible-event-loop) specified by inside settings until it is destroyed.

The handling of events or the execution of callbacks by [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) run by the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) might get [prematurely aborted](https://html.spec.whatwg.org/multipage/webappapis.html#abort-a-running-script) by the [terminate a worker](https://html.spec.whatwg.org/multipage/workers.html#terminate-a-worker) algorithm defined below.

The worker processing model remains on this step until the event loop is destroyed, which happens after the [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag is set to true, as described in the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) processing model.

    16.   [Clear](https://infra.spec.whatwg.org/#map-clear) the worker global scope's [map of active timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-active-timers).

    17.   Disentangle all the ports in the list of [the worker's ports](https://html.spec.whatwg.org/multipage/workers.html#the-worker's-ports).

    18.   [Empty](https://infra.spec.whatwg.org/#list-empty)worker global scope's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set).

* * *

When a user agent is to terminate a worker, it must run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel) with the worker's main loop (the "[run a worker](https://html.spec.whatwg.org/multipage/workers.html#run-a-worker)" processing model defined above):

1.   Set the worker's `WorkerGlobalScope` object's [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag to true.

2.   If there are any [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) queued in the `WorkerGlobalScope` object's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop)'s [task queues](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue), discard them without processing them.

3.   [Abort the script](https://html.spec.whatwg.org/multipage/webappapis.html#abort-a-running-script) currently running in the worker.

4.   If the worker's `WorkerGlobalScope` object is actually a `DedicatedWorkerGlobalScope` object (i.e. the worker is a dedicated worker), then empty the [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) of the port that the worker's implicit port is entangled with.

User agents may invoke the [terminate a worker](https://html.spec.whatwg.org/multipage/workers.html#terminate-a-worker) algorithm when a worker stops being [actively needed](https://html.spec.whatwg.org/multipage/workers.html#active-needed-worker) and the worker continues executing even after its [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag was set to true.

#### 10.2.5 Runtime script errors[](https://html.spec.whatwg.org/multipage/workers.html#runtime-script-errors-2)

Whenever an uncaught runtime script error occurs in one of the worker's scripts, if the error did not occur while handling a previous script error, the user agent will [report](https://html.spec.whatwg.org/multipage/webappapis.html#report-an-exception) it for the worker's `WorkerGlobalScope` object.

#### 10.2.6 Creating workers[](https://html.spec.whatwg.org/multipage/workers.html#creating-workers)

##### 10.2.6.1 The `AbstractWorker` mixin[](https://html.spec.whatwg.org/multipage/workers.html#the-abstractworker-mixin)

```
interface mixin AbstractWorker {
  attribute EventHandler onerror;
};
```

The following are the [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) (and their corresponding [event handler event types](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type)) that must be supported, as [event handler IDL attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes), by objects implementing the `AbstractWorker` interface:

| [Event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) | [Event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) |
| --- | --- |
| `onerror` [ServiceWorker/error_event](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorker/error_event "The error event fires whenever an error occurs in the service worker.") Support in all current engines. Firefox 44+Safari 11.1+Chrome 40+ * * * Opera?Edge 79+ * * * Edge (Legacy)17+Internet Explorer No * * * Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android? [SharedWorker/error_event](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker/error_event "The error event of the SharedWorker interface fires when an error occurs in the worker.") Support in all current engines. Firefox 29+Safari 16+Chrome 5+ * * * Opera 10.6+Edge 79+ * * * Edge (Legacy)?Internet Explorer No * * * Firefox Android 33+Safari iOS 16+Chrome Android No WebView Android?Samsung Internet 4.0–5.0 Opera Android 11–14 [Worker/error_event](https://developer.mozilla.org/en-US/docs/Web/API/Worker/error_event "The error event of the Worker interface fires when an error occurs in the worker.") Support in all current engines. Firefox 3.5+Safari 4+Chrome 4+ * * * Opera 10.6+Edge 79+ * * * Edge (Legacy)12+Internet Explorer 10+ * * * Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+ | `error` |

##### 10.2.6.2 Script settings for workers[](https://html.spec.whatwg.org/multipage/workers.html#script-settings-for-workers)

To set up a worker environment settings object, given a [JavaScript execution context](https://tc39.es/ecma262/#sec-execution-contexts)execution context, an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)outside settings, and a number unsafeWorkerCreationTime:

1.   Let realm be the value of execution context's Realm component.

2.   Let worker global scope be realm's [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global).

3.   Let origin be a unique [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque) if worker global scope's [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)'s [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`data`"; otherwise outside settings's [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

4.   Let settings object be a new [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object) whose algorithms are defined as follows:

The [realm execution context](https://html.spec.whatwg.org/multipage/webappapis.html#realm-execution-context)
Return execution context.

The [module map](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-module-map)
Return worker global scope's [module map](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-module-map).

The [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url)
Return worker global scope's [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url).

The [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin)
Return origin.

The [has cross-site ancestry](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-has-cross-site-ancestor)
    1.   If outside settings's [has cross-site ancestor](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-has-cross-site-ancestor) is true, then return true.

    2.   If worker global scope's [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)'s [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`data`", then return true.

    3.   Return false.

The [policy container](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-policy-container)
Return worker global scope's [policy container](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-policy-container).

The [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability)
Return worker global scope's [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-cross-origin-isolated-capability).

The [time origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-time-origin)
Return the result of [coarsening](https://w3c.github.io/hr-time/#dfn-coarsen-time)unsafeWorkerCreationTime with worker global scope's [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-cross-origin-isolated-capability).

5.   Set settings object's [id](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-id) to a new unique opaque string, [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url) to worker global scope's [url](https://url.spec.whatwg.org/#concept-url), [top-level creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-creation-url) to null, [target browsing context](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-target-browsing-context) to null, and [active service worker](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-active-service-worker) to null.

6.   If worker global scope is a `DedicatedWorkerGlobalScope` object, then set settings object's [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin) to outside settings's [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin).

7.   Otherwise, set settings object's [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin) to an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) value.

See [Client-Side Storage Partitioning](https://privacycg.github.io/storage-partitioning/) for the latest on properly defining this.

8.   Set realm's [[HostDefined]] field to settings object.

9.   Return settings object.

##### 10.2.6.3 Dedicated workers and the `Worker` interface[](https://html.spec.whatwg.org/multipage/workers.html#dedicated-workers-and-the-worker-interface)

[Worker](https://developer.mozilla.org/en-US/docs/Web/API/Worker "The Worker interface of the Web Workers API represents a background task that can be created via script, which can send messages back to its creator.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

```
[Exposed=(Window,DedicatedWorker,SharedWorker)]
interface Worker : EventTarget {
  constructor((TrustedScriptURL or USVString) scriptURL, optional WorkerOptions options = {});

  undefined terminate();

  undefined postMessage(any message, sequence<object> transfer);
  undefined postMessage(any message, optional StructuredSerializeOptions options = {});
};

dictionary WorkerOptions {
  DOMString name = "";
  WorkerType type = "classic";
  RequestCredentials credentials = "same-origin"; // credentials is only used if type is "module"
};

enum WorkerType { "classic", "module" };

Worker includes AbstractWorker;
Worker includes MessageEventTarget;
```
`worker = new Worker(scriptURL [, options ])`

[Worker/Worker](https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker "The Worker() constructor creates a Worker object that executes the script at the specified URL. This script must obey the same-origin policy.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Returns a new `Worker` object. scriptURL will be fetched and executed in the background, creating a new global environment for which worker represents the communication channel.

options can contain the following values:

*   `name` can be used to define the [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name) of that global environment, primarily for debugging purposes.

*   `type` can be used to load the new global environment from scriptURL as a JavaScript module, by setting it to the value "`module`".

*   `credentials` can be used to specify how scriptURL is fetched, but only if `type` is set to "`module`".

`worker.terminate()`

[Worker/terminate](https://developer.mozilla.org/en-US/docs/Web/API/Worker/terminate "The terminate() method of the Worker interface immediately terminates the Worker. This does not offer the worker an opportunity to finish its operations; it is stopped at once.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Aborts worker's associated global environment.`worker.postMessage(message [, transfer ])`

[Worker/postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Worker/postMessage "The postMessage() method of the Worker interface sends a message to the worker. The first parameter is the data to send to the worker. The data may be any JavaScript object that can be handled by the structured clone algorithm.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

`worker.postMessage(message [, { transfer } ])`
Clones message and transmits it to worker's global environment. transfer can be passed as a list of objects that are to be transferred rather than cloned.

Each `Worker` object has an associated outside port (a `MessagePort`). This port is part of a channel that is set up when the worker is created, but it is not exposed. This object must never be garbage collected before the `Worker` object.

The `terminate()` method steps are to [terminate a worker](https://html.spec.whatwg.org/multipage/workers.html#terminate-a-worker) given [this](https://webidl.spec.whatwg.org/#this)'s worker.

The `postMessage(message, transfer)` and 
```
postMessage(message,
  options)
```
 methods on `Worker` objects act as if, when invoked, they immediately invoked the respective `postMessage(message, transfer)` and 
```
postMessage(message,
  options)
```
 on [this](https://webidl.spec.whatwg.org/#this)'s [outside port](https://html.spec.whatwg.org/multipage/workers.html#outside-port), with the same arguments, and returned the same return value.

The `postMessage()` method's first argument can be structured data:

`worker.postMessage({opcode: 'activate', device: 1938, parameters: [23, 102]});`

* * *

The 
```
new Worker(scriptURL,
  options)
```
 constructor steps are:

1.   Let compliantScriptURL be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedScriptURL`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), scriptURL, "`Worker constructor`", and "`script`".

2.   Let outsideSettings be [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

3.   Let workerURL be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given compliantScriptURL, relative to outsideSettings.

Any [same-origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) URL (including `blob:` URLs) can be used. `data:` URLs can also be used, but they create a worker with an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque).

4.   If workerURL is failure, then throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

5.   Let outsidePort be a [new](https://webidl.spec.whatwg.org/#new)`MessagePort` in outsideSettings's [realm](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object's-realm).

6.   Set outsidePort's [message event target](https://html.spec.whatwg.org/multipage/web-messaging.html#message-event-target) to [this](https://webidl.spec.whatwg.org/#this).

7.   Set [this](https://webidl.spec.whatwg.org/#this)'s [outside port](https://html.spec.whatwg.org/multipage/workers.html#outside-port) to outsidePort.

8.   Let worker be [this](https://webidl.spec.whatwg.org/#this).

9.   Run this step [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

    1.   [Run a worker](https://html.spec.whatwg.org/multipage/workers.html#run-a-worker) given worker, workerURL, outsideSettings, outsidePort, and options.

##### 10.2.6.4 Shared workers and the `SharedWorker` interface[](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-and-the-sharedworker-interface)

[SharedWorker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker "The SharedWorker interface represents a specific kind of worker that can be accessed from several browsing contexts, such as several windows, iframes or even workers. They implement an interface different than dedicated workers and have a different global scope, SharedWorkerGlobalScope.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 5+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android 33+Safari iOS 16+Chrome Android No WebView Android?Samsung Internet 4.0–5.0 Opera Android 11–14

```
[Exposed=Window]
interface SharedWorker : EventTarget {
  constructor((TrustedScriptURL or USVString) scriptURL, optional (DOMString or SharedWorkerOptions) options = {});

  readonly attribute MessagePort port;
};
SharedWorker includes AbstractWorker;

dictionary SharedWorkerOptions : WorkerOptions {
  boolean extendedLifetime = false;
};
```
`sharedWorker = new SharedWorker(scriptURL [, name ])`

[SharedWorker/SharedWorker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker/SharedWorker "The SharedWorker() constructor creates a SharedWorker object that executes the script at the specified URL. This script must obey the same-origin policy.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 5+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android 33+Safari iOS 16+Chrome Android No WebView Android?Samsung Internet 4.0–5.0 Opera Android 11–14

Returns a new `SharedWorker` object. scriptURL will be fetched and executed in the background, creating a new global environment for which sharedWorker represents the communication channel. name can be used to define the [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name) of that global environment.

`sharedWorker = new SharedWorker(scriptURL [, options ])`
Returns a new `SharedWorker` object. scriptURL will be fetched and executed in the background, creating a new global environment for which sharedWorker represents the communication channel.

options can contain the following values:

*   `name` can be used to define the [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name) of that global environment.

*   `type` can be used to load the new global environment from scriptURL as a JavaScript module, by setting it to the value "`module`".

*   `credentials` can be used to specify how scriptURL is fetched, but only if `type` is set to "`module`".

*   `extendedLifetime` can be set to request that the newly-created global environment be given extra time to perform its operations even after all of its [owners](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set) have disappeared. This can be useful, for example, for performing asynchronous work after page unload.

Note that attempting to construct a shared worker with options whose `type`, `credentials`, or `extendedLifetime` values mismatch those of an existing shared worker with the same [constructor URL](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-constructor-url) and [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name), will cause the returned sharedWorker to fire an `error` event and not connect to the existing shared worker.

`sharedWorker.port`

[SharedWorker/port](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker/port "The port property of the SharedWorker interface returns a MessagePort object used to communicate and control the shared worker.")

Support in all current engines.

Firefox 29+Safari 16+Chrome 5+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android 33+Safari iOS 16+Chrome Android No WebView Android?Samsung Internet 4.0–5.0 Opera Android 11–14

Returns sharedWorker's `MessagePort` object which can be used to communicate with the global environment.

A user agent has an associated shared worker manager which is the result of [starting a new parallel queue](https://html.spec.whatwg.org/multipage/infrastructure.html#starting-a-new-parallel-queue).

Each user agent has a single [shared worker manager](https://html.spec.whatwg.org/multipage/workers.html#shared-worker-manager) for simplicity. Implementations could use one per [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin); that would not be observably different and enables more concurrency.

* * *

Each `SharedWorker` has a port, a `MessagePort` set when the object is created.

The `port` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [port](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworker-port).

The 
```
new
  SharedWorker(scriptURL, options)
```
 constructor steps are:

1.   Let compliantScriptURL be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedScriptURL`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), scriptURL, "`SharedWorker constructor`", and "`script`".

2.   If options is a `DOMString`, set options to a new `WorkerOptions` dictionary whose `name` member is set to the value of options and whose other members are set to their default values.

3.   Let outsideSettings be [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

4.   Let urlRecord be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given compliantScriptURL, relative to outsideSettings.

Any [same-origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) URL (including `blob:` URLs) can be used. `data:` URLs can also be used, but they create a worker with an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque).

5.   If urlRecord is failure, then throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

6.   Let outsidePort be a [new](https://webidl.spec.whatwg.org/#new)`MessagePort` in outsideSettings's [realm](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object's-realm).

7.   Set [this](https://webidl.spec.whatwg.org/#this)'s [port](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworker-port) to outsidePort.

8.   Let callerIsSecureContext be true if outsideSettings is a [secure context](https://html.spec.whatwg.org/multipage/webappapis.html#secure-context); otherwise, false.

9.   Let outsideStorageKey be the result of running [obtain a storage key for non-storage purposes](https://storage.spec.whatwg.org/#obtain-a-storage-key-for-non-storage-purposes) given outsideSettings.

10.   Let worker be [this](https://webidl.spec.whatwg.org/#this).

11.   [Enqueue the following steps](https://html.spec.whatwg.org/multipage/infrastructure.html#enqueue-the-following-steps) to the [shared worker manager](https://html.spec.whatwg.org/multipage/workers.html#shared-worker-manager):

    1.   Let workerGlobalScope be null.

    2.   [For each](https://infra.spec.whatwg.org/#list-iterate)scope in the list of all `SharedWorkerGlobalScope` objects:

        1.   Let workerStorageKey be the result of running [obtain a storage key for non-storage purposes](https://storage.spec.whatwg.org/#obtain-a-storage-key-for-non-storage-purposes) given scope's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

        2.   If all of the following are true:

            *   workerStorageKey[equals](https://storage.spec.whatwg.org/#storage-key-equal)outsideStorageKey;
            *   scope's [closing](https://html.spec.whatwg.org/multipage/workers.html#dom-workerglobalscope-closing) flag is false;
            *   scope's [constructor URL](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-constructor-url)[equals](https://url.spec.whatwg.org/#concept-url-equals)urlRecord; and
            *   scope's [name](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-name) equals options["`name`"],

then:

            1.   Set workerGlobalScope to scope.

            2.   [Break](https://infra.spec.whatwg.org/#iteration-break).

`data:` URLs create a worker with an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque). Both the [constructor origin](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-constructor-origin) and [constructor URL](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-constructor-url) are compared so the same `data:` URL can be used within an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) to get to the same `SharedWorkerGlobalScope` object, but cannot be used to bypass the [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) restriction.

    3.   If workerGlobalScope is not null, but the user agent has been configured to disallow communication between the worker represented by the workerGlobalScope and the [scripts](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script) whose [settings object](https://html.spec.whatwg.org/multipage/webappapis.html#settings-object) is outsideSettings, then set workerGlobalScope to null.

For example, a user agent could have a development mode that isolates a particular [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable) from all other pages, and scripts in that development mode could be blocked from connecting to shared workers running in the normal browser mode.

    4.   If workerGlobalScope is not null, and any of the following are true:

        *   workerGlobalScope's [type](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-type) is not equal to options["`type`"];

        *   workerGlobalScope's [credentials](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-credentials) is not equal to options["`credentials`"]; or

        *   workerGlobalScope's [extended lifetime](https://html.spec.whatwg.org/multipage/workers.html#concept-sharedworkerglobalscope-extended-lifetime) is not equal to options["`extendedLifetime`"],

then:

        1.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given worker's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `error` at worker.

        2.   Abort these steps.

    5.   If workerGlobalScope is not null:

        1.   Let insideSettings be workerGlobalScope's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

        2.   Let workerIsSecureContext be true if insideSettings is a [secure context](https://html.spec.whatwg.org/multipage/webappapis.html#secure-context); otherwise, false.

        3.   If workerIsSecureContext is not callerIsSecureContext:

            1.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given worker's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `error` at worker.

            2.   Abort these steps.

        4.   Associate worker with workerGlobalScope.

        5.   Let insidePort be a [new](https://webidl.spec.whatwg.org/#new)`MessagePort` in insideSettings's [realm](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object's-realm).

        6.   [Entangle](https://html.spec.whatwg.org/multipage/web-messaging.html#entangle)outsidePort and insidePort.

        7.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given workerGlobalScope to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `connect` at workerGlobalScope, using `MessageEvent`, with the `data` attribute initialized to the empty string, the `ports` attribute initialized to a new [frozen array](https://webidl.spec.whatwg.org/#dfn-frozen-array-type) containing only insidePort, and the `source` attribute initialized to insidePort.

        8.   [Append](https://infra.spec.whatwg.org/#set-append) the [relevant owner to add](https://html.spec.whatwg.org/multipage/workers.html#relevant-owner-to-add) given outsideSettings to workerGlobalScope's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set).

    6.   Otherwise, [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel), [run a worker](https://html.spec.whatwg.org/multipage/workers.html#run-a-worker) given worker, urlRecord, outsideSettings, outsidePort, and options.

#### 10.2.7 Concurrent hardware capabilities[](https://html.spec.whatwg.org/multipage/workers.html#navigator.hardwareconcurrency)

```
interface mixin NavigatorConcurrentHardware {
  readonly attribute unsigned long long hardwareConcurrency;
};
```
`self.navigator.hardwareConcurrency`

[Navigator/hardwareConcurrency](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/hardwareConcurrency "The navigator.hardwareConcurrency read-only property returns the number of logical processors available to run threads on the user's computer.")

Firefox 48+Safari 10.1–11 Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)15+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[Navigator/hardwareConcurrency](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/hardwareConcurrency "The navigator.hardwareConcurrency read-only property returns the number of logical processors available to run threads on the user's computer.")

Firefox 48+Safari 10.1–11 Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)15+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns the number of logical processors potentially available to the user agent.

[![Image 2: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") The `navigator.hardwareConcurrency` attribute's getter must return a number between 1 and the number of logical processors potentially available to the user agent. If this cannot be determined, the getter must return 1.

User agents should err toward exposing the number of logical processors available, using lower values only in cases where there are user-agent specific limits in place (such as a limitation on the number of [workers](https://html.spec.whatwg.org/multipage/workers.html#worker) that can be created) or when the user agent desires to limit fingerprinting possibilities.

### 10.3 APIs available to workers[](https://html.spec.whatwg.org/multipage/workers.html#apis-available-to-workers)

#### 10.3.1 Importing scripts and libraries[](https://html.spec.whatwg.org/multipage/workers.html#importing-scripts-and-libraries)

The `importScripts(...urls)` method steps are:

1.   Let urlStrings be « ».

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)url of urls:

    1.   [Append](https://infra.spec.whatwg.org/#list-append) the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedScriptURL`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), url, "`WorkerGlobalScope importScripts`", and "`script`" to urlStrings.

3.   [Import scripts into worker global scope](https://html.spec.whatwg.org/multipage/workers.html#import-scripts-into-worker-global-scope) given [this](https://webidl.spec.whatwg.org/#this) and urlStrings.

To import scripts into worker global scope, given a `WorkerGlobalScope` object worker global scope, a [list](https://infra.spec.whatwg.org/#list) of [scalar value strings](https://infra.spec.whatwg.org/#scalar-value-string)urls, and an optional [perform the fetch hook](https://html.spec.whatwg.org/multipage/webappapis.html#fetching-scripts-perform-fetch)performFetch:

1.   If worker global scope's [type](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-type) is "`module`", throw a `TypeError` exception.

2.   Let settings object be the [current settings object](https://html.spec.whatwg.org/multipage/webappapis.html#current-settings-object).

3.   If urls is empty, return.

4.   Let urlRecords be « ».

5.   For each url of urls:

    1.   Let urlRecord be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given url, relative to settings object.

    2.   If urlRecord is failure, then throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

    3.   [Append](https://infra.spec.whatwg.org/#list-append)urlRecord to urlRecords.

6.   For each urlRecord of urlRecords:

    1.   [Fetch a classic worker-imported script](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-classic-worker-imported-script) given urlRecord and settings object, passing along performFetch if provided. If this succeeds, let script be the result. Otherwise, rethrow the exception.

    2.   [Run the classic script](https://html.spec.whatwg.org/multipage/webappapis.html#run-a-classic-script)script, with _rethrow errors_ set to true.

script will run until it either returns, fails to parse, fails to catch an exception, or gets [prematurely aborted](https://html.spec.whatwg.org/multipage/webappapis.html#abort-a-running-script) by the [terminate a worker](https://html.spec.whatwg.org/multipage/workers.html#terminate-a-worker) algorithm defined above.

If an exception was thrown or if the script was [prematurely aborted](https://html.spec.whatwg.org/multipage/webappapis.html#abort-a-running-script), then abort all these steps, letting the exception or aborting continue to be processed by the calling [script](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script).

Service Workers is an example of a specification that runs this algorithm with its own [perform the fetch hook](https://html.spec.whatwg.org/multipage/webappapis.html#fetching-scripts-perform-fetch). [[SW]](https://html.spec.whatwg.org/multipage/references.html#refsSW)

#### 10.3.2 The `WorkerNavigator` interface[](https://html.spec.whatwg.org/multipage/workers.html#the-workernavigator-object)

[WorkerNavigator](https://developer.mozilla.org/en-US/docs/Web/API/WorkerNavigator "The WorkerNavigator interface represents a subset of the Navigator interface allowed to be accessed from a Worker. Such an object is initialized for each worker and is available via the self.navigator property.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

The `navigator` attribute of the `WorkerGlobalScope` interface must return an instance of the `WorkerNavigator` interface, which represents the identity and state of the user agent (the client):

```
[Exposed=Worker]
interface WorkerNavigator {};
WorkerNavigator includes NavigatorID;
WorkerNavigator includes NavigatorLanguage;
WorkerNavigator includes NavigatorOnLine;
WorkerNavigator includes NavigatorConcurrentHardware;
```

#### 10.3.3 The `WorkerLocation` interface[](https://html.spec.whatwg.org/multipage/workers.html#worker-locations)

[WorkerLocation](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation "The WorkerLocation interface defines the absolute location of the script executed by the Worker. Such an object is initialized for each worker and is available via the WorkerGlobalScope.location property obtained by calling self.location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[WorkerLocation/toString](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/toString "The toString() stringifier method of a WorkerLocation object returns a string containing the serialized URL for the worker's location. It is a synonym for WorkerLocation.href.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 15+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 14+

```
[Exposed=Worker]
interface WorkerLocation {
  stringifier readonly attribute USVString href;
  readonly attribute USVString origin;
  readonly attribute USVString protocol;
  readonly attribute USVString host;
  readonly attribute USVString hostname;
  readonly attribute USVString port;
  readonly attribute USVString pathname;
  readonly attribute USVString search;
  readonly attribute USVString hash;
};
```

A `WorkerLocation` object has an associated `WorkerGlobalScope` object (a `WorkerGlobalScope` object).

[WorkerLocation/href](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/href "The href property of a WorkerLocation object returns a string containing the serialized URL for the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[WorkerLocation/origin](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/origin "The origin property of a WorkerLocation object returns the worker's origin.")

Support in all current engines.

Firefox 29+Safari 10+Chrome 38+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)14+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[WorkerLocation/protocol](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/protocol "The protocol property of a WorkerLocation object returns the protocol part of the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

The `protocol` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [`WorkerGlobalScope` object](https://html.spec.whatwg.org/multipage/workers.html#concept-workerlocation-workerglobalscope)'s [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)'s [scheme](https://url.spec.whatwg.org/#concept-url-scheme), followed by "`:`".

[WorkerLocation/host](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/host "The host property of a WorkerLocation object returns the host part of the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[WorkerLocation/hostname](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/hostname "The hostname property of a WorkerLocation object returns the hostname part of the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

The `hostname` getter steps are:

1.   Let host be [this](https://webidl.spec.whatwg.org/#this)'s [`WorkerGlobalScope` object](https://html.spec.whatwg.org/multipage/workers.html#concept-workerlocation-workerglobalscope)'s [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)'s [host](https://url.spec.whatwg.org/#concept-url-host).

2.   If host is null, return the empty string.

3.   Return host, [serialized](https://url.spec.whatwg.org/#concept-host-serializer).

[WorkerLocation/port](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/port "The port property of a WorkerLocation object returns the port part of the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

The `port` getter steps are:

1.   Let port be [this](https://webidl.spec.whatwg.org/#this)'s [`WorkerGlobalScope` object](https://html.spec.whatwg.org/multipage/workers.html#concept-workerlocation-workerglobalscope)'s [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)'s [port](https://url.spec.whatwg.org/#concept-url-port).

2.   If port is null, return the empty string.

3.   Return port, [serialized](https://url.spec.whatwg.org/#serialize-an-integer).

[WorkerLocation/pathname](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/pathname "The pathname property of a WorkerLocation object returns the pathname part of the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[WorkerLocation/search](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/search "The search property of a WorkerLocation object returns the search part of the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

The `search` getter steps are:

1.   Let query be [this](https://webidl.spec.whatwg.org/#this)'s [`WorkerGlobalScope` object](https://html.spec.whatwg.org/multipage/workers.html#concept-workerlocation-workerglobalscope)'s [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)'s [query](https://url.spec.whatwg.org/#concept-url-query).

2.   If query is either null or the empty string, return the empty string.

3.   Return "`?`", followed by query.

[WorkerLocation/hash](https://developer.mozilla.org/en-US/docs/Web/API/WorkerLocation/hash "The hash property of a WorkerLocation object returns the hash part of the worker's location.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

The `hash` getter steps are:

1.   Let fragment be [this](https://webidl.spec.whatwg.org/#this)'s [`WorkerGlobalScope` object](https://html.spec.whatwg.org/multipage/workers.html#concept-workerlocation-workerglobalscope)'s [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)'s [fragment](https://url.spec.whatwg.org/#concept-url-fragment).

2.   If fragment is either null or the empty string, return the empty string.

3.   Return "`#`", followed by fragment.

[← 9.3 Cross-document messaging](https://html.spec.whatwg.org/multipage/web-messaging.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [11 Worklets →](https://html.spec.whatwg.org/multipage/worklets.html)
