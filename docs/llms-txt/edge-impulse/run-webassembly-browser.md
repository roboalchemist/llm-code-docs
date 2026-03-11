# Source: https://docs.edgeimpulse.com/hardware/deployments/run-webassembly-browser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run WebAssembly library (browser)

Impulses can be deployed as a WebAssembly library. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in web pages, or as part of your Node.js application. This allows you to run your impulse locally, without any compilation. In this tutorial you'll export an impulse, and build a web application to classify sensor data. You can also load this library from Node.js, see [Through WebAssembly (Node.js)](/hardware/deployments/run-webassembly-node).

### Prerequisites

Make sure you followed the [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) tutorial, and have a trained impulse. Also install the following software:

* Python 3 - to run a web server that serves the MIME type of the `.wasm` file correctly.

### Deploying your impulse

Head over to your Edge Impulse project, and go to **Deployment**. From here you can create the full library which contains the impulse and all external required libraries. Select **WebAssembly** and then click **Build** to create the library. Download and unzip the `.zip` file.

Then, create a new file called `run-impulse.js` in the same folder, and add:

```js  theme={"system"}
// Classifier module
let classifierInitialized = false;
Module.onRuntimeInitialized = function() {
    classifierInitialized = true;
};

class EdgeImpulseClassifier {
    _initialized = false;

    init() {
        if (classifierInitialized === true) return Promise.resolve();

        return new Promise((resolve) => {
            Module.onRuntimeInitialized = () => {
                resolve();
                classifierInitialized = true;
            };
        });
    }

    classify(rawData, debug = false) {
        if (!classifierInitialized) throw new Error('Module is not initialized');

        const obj = this._arrayToHeap(rawData);
        let ret = Module.run_classifier(obj.buffer.byteOffset, rawData.length, debug);
        Module._free(obj.ptr);

        if (ret.result !== 0) {
            throw new Error('Classification failed (err code: ' + ret.result + ')');
        }


        let jsResult = {
            anomaly: ret.anomaly,
            results: []
        };


        for (let cx = 0; cx < ret.size(); cx++) {
            let c = ret.get(cx);
            jsResult.results.push({ label: c.label, value: c.value, x: c.x, y: c.y, width: c.width, height: c.height });
            c.delete();
        }

        ret.delete();

        return jsResult;
    }

    getProperties() {
        return Module.get_properties();
    }

    _arrayToHeap(data) {
        let typedArray = new Float32Array(data);
        let numBytes = typedArray.length * typedArray.BYTES_PER_ELEMENT;
        let ptr = Module._malloc(numBytes);
        let heapBytes = new Uint8Array(Module.HEAPU8.buffer, ptr, numBytes);
        heapBytes.set(new Uint8Array(typedArray.buffer));
        return { ptr: ptr, buffer: heapBytes };
    }
}
```

Also, add a file called `server.py` and add:

```py  theme={"system"}
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

PORT = 8082

Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map={
    '.manifest': 'text/cache-manifest',
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.svg': 'image/svg+xml',
    '.css': 'text/css',
    '.js': 'application/x-javascript',
    '.wasm': 'application/wasm',
    '': 'application/octet-stream', # Default
    }

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
```

### Running the impulse

With the project ready it's time to verify that the application works. Head back to the studio and click on **Live classification**. Then load a validation sample, and click on a row under 'Detailed result'.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

To verify that the local application classifies the same, we need the raw features for this timestamp. To do so click on the 'Copy to clipboard' button next to 'Raw features'. This will copy the raw values from this validation file, before any signal processing or inferencing happened.

<Frame caption="Copying the raw features.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2e53b5-wave.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=6f8d0ba48d5dd5894b887a600011753a" width="469" height="381" data-path=".assets/images/f2e53b5-wave.png" />
</Frame>

Then, create a new HTML file where you'll call the inferencing engine with these features. Add a new file called `index.html` and add:

```html  theme={"system"}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Browser inference demo</title>
</head>
<body>
    <script src="edge-impulse-standalone.js"></script>
    <script src="run-impulse.js"></script>
    <script>
        (async () => {
            var classifier = new EdgeImpulseClassifier();
            await classifier.init();
            console.log('results', classifier.classify([
                // YOUR FEATURES HERE
                -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
            ]));
        })();
    </script>
</body>
</html>
```

Make sure to replace the features under `YOUR FEATURES HERE`.

Then run the application via:

```
$ python3 server.py
```

And navigate to [http://localhost:8082](http://localhost:8082) to see the application.

### Seeing the output

To see the output of the impulse, open the developer console in your browser.

<Frame caption="Seeing the results of your impulse running in the browser.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3d8e719-console.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=a2c82db4e29e64fdf8bddffb56e88ed8" width="538" height="282" data-path=".assets/images/3d8e719-console.png" />
</Frame>

Which matches the values we just saw in the studio. You now have your impulse running in your browser!


Built with [Mintlify](https://mintlify.com).