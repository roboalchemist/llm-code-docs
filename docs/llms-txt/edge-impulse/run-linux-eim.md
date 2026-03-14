# Source: https://docs.edgeimpulse.com/hardware/deployments/run-linux-eim.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Linux EIM

"Edge Impulse Model" (EIM) files are native Linux and macOS binary applications that contains your full impulse created in Edge Impulse Studio. The impulse consists of the signal processing block(s) along with any learning and anomaly block(s) you added and trained. EIM files are compiled for your particular system architecture and are used to run inference natively on your system.

Source code for EIM can be found [here](https://github.com/edgeimpulse/example-standalone-inferencing-linux/blob/master/source/eim.cpp).

## Getting started with EIM artifacts

To download and use an EIM artifact, you will need to first install the Edge Impulse Linux CLI tool suite by [following these instructions](/tools/clis/edge-impulse-linux-cli#installation).

From there, use the *edge-impulse-linux-runner* tool to download the .eim file (named *modelfile.eim*):

```sh  theme={"system"}
edge-impulse-linux-runner --download modelfile.eim
```

Note that the first time you call this tool, it will ask you to log into your Edge Impulse account and select a project. Subsequent calls will use your cached credentials and assume your selected project. To select a different project, you will need to log in again by using the `--clean` argument:

```sh  theme={"system"}
edge-impulse-linux-runner --clean --download modelfile.eim
```

Note that you can also download a .eim file for your system from Edge Impulse Studio. The various .eim deployment options are listed in the **Deployment** page. Search for "Linux" or "macOS" to see the executables listed as possible targets for deployment.

<Frame caption="Download EIM file from Edge Impulse Studio">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/linux-eim-executable_linux-target.png?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=018af60231c97036f6e949fc68b33259" width="828" height="664" data-path=".assets/images/linux-eim-executable_linux-target.png" />
</Frame>

From there, you can use one of the supported high-level language SDKs to perform inference locally. These SDKs run the .eim executable as its own process in the background and provide an interface for you to use in your application. See the following guides to get started using these SDKs:

* [Linux Node.js SDK](/tools/libraries/sdks/inference/linux/node-js)
* [Linux Go SDK](/tools/libraries/sdks/inference/linux/go)
* [Linux Python SDK](/tools/libraries/sdks/inference/linux/python)

The interface, installed as a library for your language, allows you to send raw data to the EIM process and receive inference results.

You can also use the Linux Runner tool to run your `.eim` file or call the executable directly. For example:

```sh  theme={"system"}
edge-impulse-linux-runner --model-file modelfile.eim
```

or

```sh  theme={"system"}
chmod +x modelfile.eim
./modelfile.eim
```

If you would like to compile the .eim file manually, please refer to [these instructions](/tools/libraries/sdks/inference/linux/cpp#building-eim-files).

To print information about the model (such as input shape, labels, and parameters), pass the `--print-info` argument to either the `.eim` file or to `edge-impulse-linux-runner`:

```sh  theme={"system"}
edge-impulse-linux-runner --model-file modelfile.eim --print-info
```

This will output model details to the console.

## EIM artifact overview

The EIM file runs as a native Linux application. JSON data is passed to and from the EIM program using Unix-like sockets or standard input/output (stdio). The high-level architecture and data flow is shown below.

<Frame caption="EIM artifact overview">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/linux-eim-executable_eim-architecture.png?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=9ad0165419f48911332c575857e70f20" width="1600" height="974" data-path=".assets/images/linux-eim-executable_eim-architecture.png" />
</Frame>

In general, you use the *edge-impulse-linux-runner* application to download and interact with the EIM model. When you request to download the EIM file, you will be asked to log into your Edge Impulse Studio account. Studio will compile the .eim binary from a given project for your particular computer architecture.

From there, you can use the *edge-impulse-linux-runner* to interact with the EIM file. This includes sending raw samples and receiving inference results. Edge Impulse maintains high-level programming language interfaces (e.g. Python, Node.JS, Go) for you to use to interact with the *runner* process. From this, you can develop applications to natively perform inference using your impulse trained on Edge Impulse Studio.

EIM executables contain your signal processing and ML code, compiled with optimizations for your processor or GPU (e.g. NEON instructions on ARM cores) plus a very simple [IPC layer](https://en.wikipedia.org/wiki/Inter-process_communication) (over a Unix socket). By doing this, your model file is now completely self-contained, and it does not depend on anything (except glibc). As a result, you do not need specific TensorFlow versions, can avoid Python dependency hell, and will never have to worry about why you're not running at full native speed.

The high-level language SDKs talk to the model through the IPC layer to run inference, so these SDKs are very thin and just need the ability to spawn a binary.

## Troubleshooting

### Wrong OS bits

If you encounter the following error message when trying to run a .eim file, it likely means the .eim file was compiled for the incorrect system architecture:

```sh  theme={"system"}
Failed to run impulse Error: Unsupported architecture "<some-architecture>"
```

Often, it means that you are attempting to deploy the .eim file to a 32-bit operating system running on a 64-bit CPU. You can check your CPU's bit width with the following commands:

```sh  theme={"system"}
uname -m
uname -a
```

These should show you if you are running on a 32-bit CPU (e.g. `x86`) or a 64-bit CPU (e.g. `x86_64` or `aarch64`).

Next, check your operating system bit width:

```sh  theme={"system"}
getconf LONG_BIT
```

This will return `32` for 32 bits or `64` for 64 bits. When you use the *runner* tool to download an .eim file, it will provide the Edge Impulse servers information about your hardware architecture. If you are using a 64-bit CPU, you will receive an .eim file compiled for 64-bit systems. Such an executable will not run on 32-bit operating systems.

To correct this, make sure that you are running a 32-bit OS on 32-bit hardware or a 64-bit OS on 64-bit hardware only.

## Advanced Usage

If you would like to modify, debug, or interface with EIM artifacts on a lower level, these notes should help you get started.

### JSON protocol

JSON frames are used to pass data to and from the EIM executable running on your system. They can be transferred via Unix-like sockets (what *edge-impulse-linux-runner* uses) or standard input/output (stdio). Example frames are given below.

An example dataflow of how such JSON messages are passed between the runner and EIM executable is shown below:

<Frame caption="EIM JSON data flow">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/linux-eim-executable_eim-flow-1.png?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=44c2c3fa1651981e942cf8ea9abdd641" width="914" height="1000" data-path=".assets/images/linux-eim-executable_eim-flow-1.png" />
</Frame>

If the EIM executable encounters an error, you might see something like this:

<Frame caption="EIM JSON data flow with error condition">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/linux-eim-executable_eim-flow-2.png?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=c712879ec7dbb94b73803f2c0de26413" width="804" height="1000" data-path=".assets/images/linux-eim-executable_eim-flow-2.png" />
</Frame>

#### Runner to EIM JSON examples

Basic "hello" frame:

```json  theme={"system"}
{
	"hello": 1, // always 1 (version number)
	"id": 1 // ID should be incremented with each message
}
```

Sending raw features to be classified:

```json  theme={"system"}
{
	"classify": [1, 2, ..., 3],
	"id": 2,
	"debug": false // OPTIONAL, enables debug output from EIM
}
```

#### EIM to runner JSON examples

Model info:

To print this information pass the `--print-info` argument.

```json  theme={"system"}
{
   "id": 1,
   "model_parameters": {
      "axis_count": 3,
      "frequency": 62.5,
      "has_anomaly": 1,
      "image_channel_count": 0,
      "image_input_frames": 0,
      "image_input_height": 0,
      "image_input_width": 0,
      "input_features_count": 375,
      "interval_ms": 16,
      "label_count": 4,
      "labels": [
         "idle",
         "snake",
         "updown",
         "wave"
      ],
      "model_type": "classification",
      "sensor": 2,
      "slice_size": 31,
      "use_continuous_mode": false
   },
   "project": {
      "deploy_version": 411,
      "id": 1,
      "name": "Continuous gestures",
      "owner": "EdgeImpulse Inc."
   },
   "success": true
}
```

Classification inference result:

```json  theme={"system"}
{
	"id": 1, // ID of the 'classify' message
	"success": true,
	"result": {
		"classification": {
			"up": 0.98,
			"down": 0.00,
			"wave": 0.02
		}
	},
	"timing": {
		"dsp": 0, // miliseconds of the DSP processing
		"classification": 0, // miliseconds of the NN processing
		"anomaly": 0, // miliseconds of the anomaly block processing
		"json": 0, // miliseconds spent on the JSON parsing
		"stdin": 0 // miliseconds sepnt on the STDIN processing
	}
}
```

Object detection inference result:

```json  theme={"system"}
{
	"id": 1, // ID of the 'classify' message
	"success": true,
	"result": {
		"bounding_boxes": [
		    {
		      "height": 8,
	        "label": "beer",
	        "value": 0.5000159740447998,
	        "width": 8,
	        "x": 8,
	        "y": 40
	     },
	     {
		     "height": 8,
	       "label": "beer",
	       "value": 0.5000159740447998,
	       "width": 8,
	       "x": 72,
	       "y": 40
		  }
		]
	},
	"timing": {
		"dsp": 0, // miliseconds of the DSP processing
		"classification": 0, // miliseconds of the NN processing
		"anomaly": 0, // miliseconds of the anomaly block processing
		"json": 0, // miliseconds spent on the JSON parsing
		"stdin": 0 // miliseconds sepnt on the STDIN processing
	}
}
```

Error frame:

```json  theme={"system"}
{
	"success": false,
	"error": "Error message",
	"id": 1 // OPTIONAL, ID of the message that generated error
}
```

### Debugging with stdout

You can run the .eim file as any other binary executable. Instead of using sockets to send and receive JSON frames manually, you can connect the runner to the EIM's socket to use your shell's standard input/output. To do that, open a terminal and run your .eim file as an executable, giving it a temporary socket as an argument:

```sh  theme={"system"}
./modelfile.eim /tmp/hello.sock
```

Open another terminal and start the impulse runner, connecting it to your temporary socket:

```sh  theme={"system"}
edge-impulse-linux-runner --model-file /tmp/hello.sock
```

In addition to using stdout, you can also use common debugger tools with the runner to assist in debugging the EIM program. To use LLDB, run:

```sh  theme={"system"}
lldb -o run ./modelfile.eim /tmp/hello.sock
```

For GDB:

```sh  theme={"system"}
gdb --args ./modelfile.eim /tmp/hello.sock
```


Built with [Mintlify](https://mintlify.com).