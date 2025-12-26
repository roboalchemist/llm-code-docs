# Source: https://xtermjs.org/docs/guides/flowcontrol/

<div>

# [Flowcontrol](/docs/guides/flowcontrol/)

</div>

# Flow Control for xterm.js 

Very fast producers on the application side can overwhelm xterm.js with too much data. If that happens, the emulator will get sluggish, might not respond to keystrokes anymore or even worse, some transport buffers might overflow and segfault. To get fast producers under control we need **flow control**.

## How xterm.js processes incoming data 

To write stream data to the emulator we call `write` with chunks of a stream:

``` highlight
term.write(chunk_1);
...
term.write(chunk_n);
```

`write` itself is non-blocking, it buffers the data and returns immediately. The data will be processed with the next event loop invocation, the amount processed depends on a timer constraint and is designed to take less time than a single frame (16ms) to avoid blocking the UI thread.

Compared to very fast producers (up to several GB/s) this system has a rather low throughput (5 - 35 MB/s), thus fast producers might keep growing the input write buffer. To avoid an out of memory exception in xterm.js this buffer has a hardcoded limit ([50MB at time of writing](https://github.com/xtermjs/xterm.js/blob/7f598a36753f4d950ee63dc91bd6a92290f7e037/src/common/input/WriteBuffer.ts#L9-L17)). Any data beyond that limit gets discarded.

## Most simple flow control mechanism (inefficient)

To place a handbrake on caller side, we can use the optional callback of `write`:

``` highlight
term.write(chunk, () => );
```

The callback gets called once when the chunk was processed. This waiting condition can be applied directly to incoming interfaces like the pty object of `node-pty`:

``` highlight
pty.onData(chunk => );
});
```

Here the `pause` and the `resume` methods will take care of the flow control propagation to the underlying OS-pty with back pressure and real blocking semantics. This will also work across several layers (for websockets also see [below](#flow-control-over-websockets)).

Still this simple mechanism is quite inefficient for several reasons - it stops the data flow on the OS-pty for every single chunk (worst case - a single byte), waits a tiny bit for the processing to re-enable the data flow afterwards. The waits will sum up to a rather big idle time, furthermore the needed kernel context switches for the blocking/unblocking of the OS-pty will create additional nonsense workload. In the end the total throughput will drop.

If more layers are involved (e.g. websockets), their processing/latency will further add more on top resulting in a really bad throughput.

## Ideas for a better mechanism

A more advanced mechanism would try to lower the needs for `pause` and `resume` calls. This can be achieved by measuring the written data as a "watermark", compare it with high and low limits and use write callbacks as a commit response:

``` highlight
const HIGH = 100000;
const LOW = 10000;

let watermark = 0;

pty.onData(chunk => 
  });
  if (watermark > HIGH) 
});
```

This mechanism avoids most `pause` and `resume` calls and tries to get a steady flow between LOW and HIGH watermark. Optimal values for HIGH and LOW will vary alot depending on the circumstances. Rule of thumb - to keep the emulator snappy for keystrokes under fast input HIGH should not be greater than 500K. A good test scenario is running `yes`, then pressing Ctrl-C and check if the response is within an acceptible range.

Note that this variant still does some nonsense work - it places a callback for every single chunk of data. There are several ways to reduce the callback pressure, e.g. place it only on every n-th chunk, or, as shown here, count pending callbacks instead:

``` highlight
const CALLBACK_BYTE_LIMIT = 100000;
const HIGH = 5;
const LOW = 2;

let written = 0;
let pendingCallbacks = 0;

pty.onData(chunk => 
    });
    pendingCallbacks++;
    written = 0;
    if (pendingCallbacks > HIGH) 
  } else 
});
```

Now a callback would only occur every 100k bytes, HIGH/LOW now limit the pending callbacks. This again needs testing and fine tuning, furthermore the average chunk length should be much smaller than CALLBACK_BYTE_LIMIT to really benefit from the fast path.

There might be more elegant or stricter solutions than these, depending on your needs. Feel free to come up with your suggestion to improve this guide. For non-`node-pty` backends you will most likely have to build a flow control mechanism based on websockets as an additional transport layer (see below). Also note that a custom flow control mechanism can easily stop the whole stream forever if the limits are not calculated/applied correctly. Special care is needed if a lossy transport is involved (would be needed anyway for data integrity checks).

## Flow control over websockets

If a websocket is between your backend and xterm.js, additional work is needed to get proper flow control. The basic problem we have to work around is the non-blocking nature of message delivery, i.e. buffers on both ends of the websocket implementation might stock up data (sending and receiving side). This means we cannot reliably implement a flow control for those buffers directly (the websocket protocol also doesn't offer hooks for this).

It is still possible to get some flow control working on top of websockets. For this we simply treat the websocket transport as a datasink with infinite buffers and unknown latency and skip it in the flow control handling. Instead we span the write callback accounting from client side to server side, schematically:

**Client:**

``` highlight
if (ackCondition) );
} else 
```

**Server:**

``` highlight
pty.onData(chunk => 
});
socket.onData(chunk => 
  } else 
});
```

Here it is important that `ackCondition` on the client side and `condition` / `stopCondition` on the server side agree about the things to measure or the flow control will block the stream sooner or later. Furthermore the ACK message needs to be marked as a special message to not get confused as normal data (custom message protocol).

If you dont want to develop this with your own message protocol maybe have a look on ready-to-go solutions like [Socket.IO](https://socket.io/) or [sockette](https://github.com/lukeed/sockette). Both also provide mechanisms to forward events/callbacks, which can simplify the implementation alot.