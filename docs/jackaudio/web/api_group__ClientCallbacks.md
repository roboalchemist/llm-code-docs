# Source: https://jackaudio.org/

JACK-AUDIO-CONNECTION-KIT   
---  
  
  * [Main Page](index.html)
  * [Related Pages](pages.html)
  * [Modules](modules.html)
  * [Data Structures](annotated.html)
  * [Files](files.html)
  * ![](search/mag_sel.svg) [![](search/close.svg)](javascript:searchBox.CloseResultsWindow\(\))




Modules | Functions

Setting Client Callbacks

[Creating & manipulating clients](group__ClientFunctions.html) » [The non-callback API](group__NonCallbackAPI.html)

##  Modules  
  
---  
| [Controlling & querying JACK server operation](group__ServerControl.html)  
  
##  Functions  
  
---  
int | [jack_set_thread_init_callback](group__ClientCallbacks.html#gad5a6904292f5c9790223c18aeab202bf) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackThreadInitCallback](types_8h.html#a36a615301840e4edcfc3f61456c43020) thread_init_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
void | [jack_on_shutdown](group__ClientCallbacks.html#ga417b907ee02efbe00f5e9a2f4d202599) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackShutdownCallback](types_8h.html#a1f461fe99711af7edcb1b73b1315fbb3) function, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
void | [jack_on_info_shutdown](group__ClientCallbacks.html#gaf54d9f133267170ef1e6ce5219d24dd4) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackInfoShutdownCallback](types_8h.html#ad30b9f6d5898ba8954bd51c4bc428a9e) function, void *arg) JACK_WEAK_EXPORT  
int | [jack_set_process_callback](group__ClientCallbacks.html#gafb5ec9fb4b736606d676c135fb97888b) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackProcessCallback](types_8h.html#ab94e71df11ce055f9a278f55a6e476bc) process_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_freewheel_callback](group__ClientCallbacks.html#gae797e2cde20faecb9be510c8873fbdd6) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackFreewheelCallback](types_8h.html#a2a9a8af9ac8206a0c67cef6a27e88be7) freewheel_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_buffer_size_callback](group__ClientCallbacks.html#ga030cc371acb19abe52861492acb960ad) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackBufferSizeCallback](types_8h.html#aae24422729bb05aa0731a2d9545d278c) bufsize_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_sample_rate_callback](group__ClientCallbacks.html#gac1b3eb298cfa2869b8773c6cecf7f4b3) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackSampleRateCallback](types_8h.html#a0735e21ddb96029d46bf35f14fc7e895) srate_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_client_registration_callback](group__ClientCallbacks.html#ga51b01a31e56c92f4e2788a94840f0f37) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [JackClientRegistrationCallback](types_8h.html#a9221225159a10a6eedaf0d98eff6de84) registration_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_port_registration_callback](group__ClientCallbacks.html#ga30983a0478551a3cd20b71d692b24007) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [JackPortRegistrationCallback](types_8h.html#ab67ac0b5c60ab9f94eba0c06ab16725c) registration_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_port_rename_callback](group__ClientCallbacks.html#ga0c73095c1d8ebba413de6834bd7757b9) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [JackPortRenameCallback](types_8h.html#ab5e21db10d45f938ec0fa688230c2c24) rename_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_port_connect_callback](group__ClientCallbacks.html#ga5312576d779c0664a7c703c87a9dba89) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [JackPortConnectCallback](types_8h.html#a351e09441e88b3013db37d3eb8e0a2b3) connect_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_graph_order_callback](group__ClientCallbacks.html#gacd0804ccef7c6891d8265bd88e7429ee) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [JackGraphOrderCallback](types_8h.html#ac3336628b231d38cfb07a94fd29067b3) graph_callback, void *) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_xrun_callback](group__ClientCallbacks.html#ga08196c75f06d9e68f9a3570dfcb1e323) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [JackXRunCallback](types_8h.html#ac19798b331fa11b864f874408d26a0b0) xrun_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_latency_callback](group__ClientCallbacks.html#ga70a38fb1e74c5e9df9f1305c695c58bf) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [JackLatencyCallback](types_8h.html#abbf969808e55bf3302079c2f57fae8c1) latency_callback, void *) JACK_WEAK_EXPORT  
  
## Detailed Description

## Function Documentation

## ◆ jack_on_info_shutdown()

void jack_on_info_shutdown  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackInfoShutdownCallback](types_8h.html#ad30b9f6d5898ba8954bd51c4bc428a9e) | _function_ ,   
|  | void * | _arg_  
| ) | |   
  
Parameters
     client| pointer to JACK client structure.   
---|---  
function| The jack_shutdown function pointer.   
arg| The arguments for the jack_shutdown function.  
  
Register a function (and argument) to be called if and when the JACK server shuts down the client thread. The function must be written as if it were an asynchonrous POSIX signal handler -- use only async-safe functions, and remember that it is executed from another thread. A typical function might set a flag or write to a pipe so that the rest of the application knows that the JACK client thread has shut down.

NOTE: clients do not need to call this. It exists only to help more complex clients understand what is going on. It should be called before jack_client_activate().

NOTE: if a client calls this AND [jack_on_shutdown()](group__ClientCallbacks.html#ga417b907ee02efbe00f5e9a2f4d202599), then in the event of a client thread shutdown, the callback passed to this function will be called, and the one passed to [jack_on_shutdown()](group__ClientCallbacks.html#ga417b907ee02efbe00f5e9a2f4d202599) will not. 

## ◆ jack_on_shutdown()

void jack_on_shutdown  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackShutdownCallback](types_8h.html#a1f461fe99711af7edcb1b73b1315fbb3) | _function_ ,   
|  | void * | _arg_  
| ) | |   
  
Parameters
     client| pointer to JACK client structure.   
---|---  
function| The jack_shutdown function pointer.   
arg| The arguments for the jack_shutdown function.  
  
Register a function (and argument) to be called if and when the JACK server shuts down the client thread. The function must be written as if it were an asynchonrous POSIX signal handler -- use only async-safe functions, and remember that it is executed from another thread. A typical function might set a flag or write to a pipe so that the rest of the application knows that the JACK client thread has shut down.

NOTE: clients do not need to call this. It exists only to help more complex clients understand what is going on. It should be called before jack_client_activate().

NOTE: if a client calls this AND [jack_on_info_shutdown()](group__ClientCallbacks.html#gaf54d9f133267170ef1e6ce5219d24dd4), then the event of a client thread shutdown, the callback passed to this function will not be called, and the one passed to [jack_on_info_shutdown()](group__ClientCallbacks.html#gaf54d9f133267170ef1e6ce5219d24dd4) will. 

## ◆ jack_set_buffer_size_callback()

int jack_set_buffer_size_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackBufferSizeCallback](types_8h.html#aae24422729bb05aa0731a2d9545d278c) | _bufsize_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell JACK to call _bufsize_callback_ whenever the size of the the buffer that will be passed to the _process_callback_ is about to change. Clients that depend on knowing the buffer size must supply a _bufsize_callback_ before activating themselves.

Parameters
     client| pointer to JACK client structure.   
---|---  
bufsize_callback| function to call when the buffer size changes.   
arg| argument for _bufsize_callback_.  
  
Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_client_registration_callback()

int jack_set_client_registration_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [JackClientRegistrationCallback](types_8h.html#a9221225159a10a6eedaf0d98eff6de84) | _registration_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the JACK server to call _registration_callback_ whenever a port is registered or unregistered, passing _arg_ as a parameter.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_freewheel_callback()

int jack_set_freewheel_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackFreewheelCallback](types_8h.html#a2a9a8af9ac8206a0c67cef6a27e88be7) | _freewheel_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the Jack server to call _freewheel_callback_ whenever we enter or leave "freewheel" mode, passing _arg_ as the second argument. The first argument to the callback will be non-zero if JACK is entering freewheel mode, and zero otherwise.

Returns
    0 on success, otherwise a non-zero error code. 

## ◆ jack_set_graph_order_callback()

int jack_set_graph_order_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [JackGraphOrderCallback](types_8h.html#ac3336628b231d38cfb07a94fd29067b3) | _graph_callback_ ,   
|  | void * |   
| ) | |   
  
Tell the JACK server to call _graph_callback_ whenever the processing graph is reordered, passing _arg_ as a parameter.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_latency_callback()

int jack_set_latency_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [JackLatencyCallback](types_8h.html#abbf969808e55bf3302079c2f57fae8c1) | _latency_callback_ ,   
|  | void * |   
| ) | |   
  
Tell the Jack server to call _latency_callback_ whenever it is necessary to recompute the latencies for some or all Jack ports.

_latency_callback_ will be called twice each time it is needed, once being passed JackCaptureLatency and once JackPlaybackLatency. See [Managing and determining latency](group__LatencyFunctions.html) for the definition of each type of latency and related functions.

**IMPORTANT: Most JACK clients do NOT need to register a latency callback.**

Clients that meet any of the following conditions do NOT need to register a latency callback:

  * have only input ports
  * have only output ports
  * their output is totally unrelated to their input
  * their output is not delayed relative to their input (i.e. data that arrives in a given process() callback is processed and output again in the same callback)



Clients NOT registering a latency callback MUST also satisfy this condition:

  * have no multiple distinct internal signal pathways



This means that if your client has more than 1 input and output port, and considers them always "correlated" (e.g. as a stereo pair), then there is only 1 (e.g. stereo) signal pathway through the client. This would be true, for example, of a stereo FX rack client that has a left/right input pair and a left/right output pair.

However, this is somewhat a matter of perspective. The same FX rack client could be connected so that its two input ports were connected to entirely separate sources. Under these conditions, the fact that the client does not register a latency callback MAY result in port latency values being incorrect.

Clients that do not meet any of those conditions SHOULD register a latency callback.

Another case is when a client wants to use [jack_port_get_latency_range()](group__LatencyFunctions.html#gaf379bc0e88a6df6c4b7836db4b9382d7), which only returns meaninful values when ports get connected and latency values change.

See the documentation for [jack_port_set_latency_range()](group__LatencyFunctions.html#ga7a8f181fcec32945db7b8e06ee1ca94b) on how the callback should operate. Remember that the _mode_ argument given to the latency callback will need to be passed into [jack_port_set_latency_range()](group__LatencyFunctions.html#ga7a8f181fcec32945db7b8e06ee1ca94b)

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_port_connect_callback()

int jack_set_port_connect_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [JackPortConnectCallback](types_8h.html#a351e09441e88b3013db37d3eb8e0a2b3) | _connect_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the JACK server to call _connect_callback_ whenever a port is connected or disconnected, passing _arg_ as a parameter.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_port_registration_callback()

int jack_set_port_registration_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [JackPortRegistrationCallback](types_8h.html#ab67ac0b5c60ab9f94eba0c06ab16725c) | _registration_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the JACK server to call _registration_callback_ whenever a port is registered or unregistered, passing _arg_ as a parameter.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_port_rename_callback()

int jack_set_port_rename_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [JackPortRenameCallback](types_8h.html#ab5e21db10d45f938ec0fa688230c2c24) | _rename_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the JACK server to call _rename_callback_ whenever a port is renamed, passing _arg_ as a parameter.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_process_callback()

int jack_set_process_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackProcessCallback](types_8h.html#ab94e71df11ce055f9a278f55a6e476bc) | _process_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the Jack server to call _process_callback_ whenever there is work be done, passing _arg_ as the second argument.

The code in the supplied function must be suitable for real-time execution. That means that it cannot call functions that might block for a long time. This includes all I/O functions (disk, TTY, network), malloc, free, printf, pthread_mutex_lock, sleep, wait, poll, select, pthread_join, pthread_cond_wait, etc, etc.

Returns
    0 on success, otherwise a non-zero error code, causing JACK to remove that client from the process() graph. 

## ◆ jack_set_sample_rate_callback()

int jack_set_sample_rate_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackSampleRateCallback](types_8h.html#a0735e21ddb96029d46bf35f14fc7e895) | _srate_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the Jack server to call _srate_callback_ whenever the system sample rate changes.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_set_thread_init_callback()

int jack_set_thread_init_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackThreadInitCallback](types_8h.html#a36a615301840e4edcfc3f61456c43020) | _thread_init_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell JACK to call _thread_init_callback_ once just after the creation of the thread in which all other callbacks will be handled.

The code in the supplied function does not need to be suitable for real-time execution.

Returns
    0 on success, otherwise a non-zero error code, causing JACK to remove that client from the process() graph. 

## ◆ jack_set_xrun_callback()

int jack_set_xrun_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [JackXRunCallback](types_8h.html#ac19798b331fa11b864f874408d26a0b0) | _xrun_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Tell the JACK server to call _xrun_callback_ whenever there is a xrun, passing _arg_ as a parameter.

Returns
    0 on success, otherwise a non-zero error code 

* * *

Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.9.1 
