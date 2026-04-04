# Source: https://docs.edgeimpulse.com/hardware/deployments/run-webassembly-node.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run WebAssembly library (Node.js)

Impulses can be deployed as a WebAssembly library. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in web pages, or as part of your Node.js application. This allows you to run your impulse locally, without any compilation. In this tutorial you'll export an impulse, and build a Node.js application to classify sensor data. You can also load this library from a web page, see [Through WebAssembly (browser)](/hardware/deployments/run-webassembly-browser).

<Warning>
  **Edge Impulse for Linux**

  If you plan to run your impulse from Node.js you probably want to take a look at [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux). It offers full hardware acceleration, bindings to cameras and microphones, and Node.js bindings.
</Warning>

### Prerequisites

Make sure you followed the [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) tutorial, and have a trained impulse. Also install the following software:

* [Node.js](https://nodejs.org/en/) - to build the application.

### Deploying your impulse

Head over to your Edge Impulse project, and go to **Deployment**. From here you can create the full library which contains the impulse and all external required libraries. Select **WebAssembly** and then click **Build** to create the library. Download and unzip the `.zip` file.

Then, create a new file called `run-impulse.js` in the same folder, and add:

```js  theme={"system"}
// Load the inferencing WebAssembly module
const Module = require('./edge-impulse-standalone');
const fs = require('fs');

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

if (!process.argv[2]) {
    return console.error('Requires one parameter (a comma-separated list of raw features, or a file pointing at raw features)');
}

let features = process.argv[2];
if (fs.existsSync(features)) {
    features = fs.readFileSync(features, 'utf-8');
}

// Initialize the classifier, and invoke with the argument passed in
let classifier = new EdgeImpulseClassifier();
classifier.init().then(async () => {
    let result = classifier.classify(features.trim().split(',').map(n => Number(n)));

    console.log(result);
}).catch(err => {
    console.error('Failed to initialize classifier', err);
});
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

Then invoke the local application by passing these features as an argument to the application. Open a terminal or command prompt and run:

```
node run-impulse.js "-19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ..."
```

This will run the signal processing pipeline, and then classify the output:

```
{
  anomaly: 0.133557,
  results: [
    { label: 'idle', value: 0.015319 },
    { label: 'snake', value: 0.000444 },
    { label: 'updown', value: 0.006182 },
    { label: 'wave', value: 0.978056 }
  ]
}
```

Which matches the values we just saw in the studio. You now have your impulse running locally!

### Troubleshooting

#### Argument list too long

There's a limited number of arguments that you can pass on the command line, and if your raw features array is larger than this number you will be presented with the error: `Argument list too long`. To get around this you can create a file called `features.txt`, put your features in there, and then call the script via:

```
node run-impulse.js features.txt
```


Built with [Mintlify](https://mintlify.com).