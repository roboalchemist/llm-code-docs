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

Creating & manipulating clients

##  Modules  
  
---  
| [The non-callback API](group__NonCallbackAPI.html)  
  
##  Functions  
  
---  
[jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | [jack_client_open](group__ClientFunctions.html#gabbd2041bca191943b6ef29a991a131c5) (const char *client_name, [jack_options_t](types_8h.html#a0ef5011e5aab7655ad0d64babf7d91f0) options, [jack_status_t](types_8h.html#a49053418570427a7a99d1bb45fb43f38) *status,...) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
[jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | [jack_client_new](group__ClientFunctions.html#ga97482adad8116b76635a63f646a2d2f5) (const char *client_name) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
int | [jack_client_close](group__ClientFunctions.html#ga405646705e600d8bf66327bdbab8e363) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_client_name_size](group__ClientFunctions.html#gab8b16ee616207532d0585d04a0bd1d60) (void) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
char * | [jack_get_client_name](group__ClientFunctions.html#ga49f7d301475b45a8a3cc0da848d81e2f) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
char * | [jack_get_uuid_for_client_name](group__ClientFunctions.html#ga4c995eb51f38f3962dea4408122ced88) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, const char *name) JACK_WEAK_EXPORT  
char * | [jack_get_client_name_by_uuid](group__ClientFunctions.html#gab4cf2516014b436e762907016b5be2b4) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, const char *uuid) JACK_WEAK_EXPORT  
int | [jack_internal_client_new](group__ClientFunctions.html#ga87be6679700acc40a0da17ac9ba3a31e) (const char *client_name, const char *load_name, const char *load_init) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
void | [jack_internal_client_close](group__ClientFunctions.html#ga0ad890884c983c78ba93ed2d9b8ee8cc) (const char *client_name) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
int | [jack_activate](group__ClientFunctions.html#ga9800d5b29bd7670d9944a15f6ea0ecf8) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_deactivate](group__ClientFunctions.html#ga2c6447b766b13d3aa356aba2b48e51fa) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
jack_native_thread_t | [jack_client_thread_id](group__ClientFunctions.html#ga4e78f0a2ca6c837709c7ec641afd9954) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_is_realtime](group__ClientFunctions.html#ga15719a4abdcc5fa8415167dd6ed6512c) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
  
## Detailed Description

Note: More documentation can be found in [jack/types.h](types_8h.html). 

## Function Documentation

## ◆ jack_activate()

int jack_activate  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Tell the Jack server that the program is ready to start processing audio.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_client_close()

int jack_client_close  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Disconnects an external client from a JACK server.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_client_name_size()

int jack_client_name_size  | ( | void | | ) |   
---|---|---|---|---|---  
  
Returns
    the maximum number of characters in a JACK client name including the final NULL character. This value is a constant. 

## ◆ jack_client_new()

[jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf)* jack_client_new  | ( | const char * | _client_name_| ) |   
---|---|---|---|---|---  
  
**THIS FUNCTION IS DEPRECATED AND SHOULD NOT BE USED IN NEW JACK CLIENTS**

## ◆ jack_client_open()

[jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf)* jack_client_open  | ( | const char * | _client_name_ ,   
---|---|---|---  
|  | [jack_options_t](types_8h.html#a0ef5011e5aab7655ad0d64babf7d91f0) | _options_ ,   
|  | [jack_status_t](types_8h.html#a49053418570427a7a99d1bb45fb43f38) * | _status_ ,   
|  |  | _..._  
| ) | |   
  
Open an external client session with a JACK server. This interface is more complex but more powerful than [jack_client_new()](group__ClientFunctions.html#ga97482adad8116b76635a63f646a2d2f5). With it, clients may choose which of several servers to connect, and control whether and how to start the server automatically, if it was not already running. There is also an option for JACK to generate a unique client name, when necessary.

Parameters
     client_name| of at most [jack_client_name_size()](group__ClientFunctions.html#gab8b16ee616207532d0585d04a0bd1d60) characters. The name scope is local to each server. Unless forbidden by the [JackUseExactName](types_8h.html#a396617de2ef101891c51346f408a375ea352b176ffa092ec946a06b707f6aa21b) option, the server will modify this name to create a unique variant, if needed.  
---|---  
options| formed by OR-ing together [JackOptions](types_8h.html#a396617de2ef101891c51346f408a375e) bits. Only the [JackOpenOptions](types_8h.html#ab39e7f78dba631f3c0d34ac4cddcf80f) bits are allowed.  
status| (if non-NULL) an address for JACK to return information from the open operation. This status word is formed by OR-ing together the relevant [JackStatus](types_8h.html#aaf80297bce18297403b99e3d320ac8a8) bits.  
  
**Optional parameters:** depending on corresponding [_options_ bits] additional parameters may follow _status_ (in this order).

  * [[JackServerName](types_8h.html#a396617de2ef101891c51346f408a375ea348557bfdc579daed2e35cc41c4f09c7)] _(char *) server_name_ selects from among several possible concurrent server instances. Server names are unique to each user. If unspecified, use "default" unless $JACK_DEFAULT_SERVER is defined in the process environment.



Returns
    Opaque client handle if successful. If this is NULL, the open operation failed, _*status_ includes [JackFailure](types_8h.html#aaf80297bce18297403b99e3d320ac8a8a354fbb027d989173f50921d239f3812b) and the caller is not a JACK client. 

## ◆ jack_client_thread_id()

jack_native_thread_t jack_client_thread_id  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | | ) |   
---|---|---|---|---|---  
  
Returns
    the pthread ID of the thread running the JACK client side code. 

## ◆ jack_deactivate()

int jack_deactivate  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Tell the Jack server to remove this _client_ from the process graph. Also, disconnect all ports belonging to it, since inactive clients have no port connections.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_get_client_name()

char* jack_get_client_name  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Returns
    pointer to actual client name. This is useful when [JackUseExactName](types_8h.html#a396617de2ef101891c51346f408a375ea352b176ffa092ec946a06b707f6aa21b) is not specified on open and [JackNameNotUnique](types_8h.html#aaf80297bce18297403b99e3d320ac8a8a09a73b951f3601ae9436bd3429ac0691) status was returned. In that case, the actual name will differ from the _client_name_ requested. 

## ◆ jack_get_client_name_by_uuid()

char* jack_get_client_name_by_uuid  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | const char * | _uuid_  
| ) | |   
  
Returns
    a pointer to the name of the client with the UUID specified by uuid.

Parameters
     client| making the request   
---|---  
uuid| the uuid of the client whose name is desired  
  
Return NULL if no such client with the given UUID exists 

## ◆ jack_get_uuid_for_client_name()

char* jack_get_uuid_for_client_name  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | const char * | _name_  
| ) | |   
  
Returns
    pointer to a string representation of the UUID for a client named

Parameters
     name| . If no such client exists, return NULL  
---|---  
client| the client making the request   
name| the name of the client whose UUID is desired  
  
Return NULL if no such client with the given name exists 

## ◆ jack_internal_client_close()

void jack_internal_client_close  | ( | const char * | _client_name_| ) |   
---|---|---|---|---|---  
  
Remove an internal client from a JACK server.

**[Deprecated:](deprecated.html#_deprecated000002)**
     Please use [jack_internal_client_load()](intclient_8h.html#aff038e9c251a2cdf4a5ce94d9d0ea88c). 

## ◆ jack_internal_client_new()

int jack_internal_client_new  | ( | const char * | _client_name_ ,   
---|---|---|---  
|  | const char * | _load_name_ ,   
|  | const char * | _load_init_  
| ) | |   
  
Load an internal client into the Jack server.

Internal clients run inside the JACK server process. They can use most of the same functions as external clients. Each internal client must declare jack_initialize() and jack_finish() entry points, called at load and unload times. See inprocess.c for an example of how to write an internal client.

**[Deprecated:](deprecated.html#_deprecated000001)**
     Please use [jack_internal_client_load()](intclient_8h.html#aff038e9c251a2cdf4a5ce94d9d0ea88c).

Parameters
     client_name| of at most [jack_client_name_size()](group__ClientFunctions.html#gab8b16ee616207532d0585d04a0bd1d60) characters.  
---|---  
load_name| of a shared object file containing the code for the new client.  
load_init| an arbitary string passed to the jack_initialize() routine of the new client (may be NULL).  
  
Returns
    0 if successful. 

## ◆ jack_is_realtime()

int jack_is_realtime  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Parameters
     client| pointer to JACK client structure.  
---|---  
  
Check if the JACK subsystem is running with -R (-realtime).

Returns
    1 if JACK is running realtime, 0 otherwise 

* * *

Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.9.1 
