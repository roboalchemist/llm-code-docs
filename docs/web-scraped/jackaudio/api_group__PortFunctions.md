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

Creating & manipulating ports

[Creating & manipulating clients](group__ClientFunctions.html) » [The non-callback API](group__NonCallbackAPI.html) » [Setting Client Callbacks](group__ClientCallbacks.html) » [Controlling & querying JACK server operation](group__ServerControl.html)

##  Modules  
  
---  
| [Managing and determining latency](group__LatencyFunctions.html)  
  
##  Functions  
  
---  
[jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | [jack_port_register](group__PortFunctions.html#ga3e21d145c3c82d273a889272f0e405e7) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, const char *port_name, const char *port_type, unsigned long flags, unsigned long buffer_size) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_unregister](group__PortFunctions.html#ga9ac3ccd93be18999c0bd817bc032e876) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
void * | [jack_port_get_buffer](group__PortFunctions.html#ga209880b64774dd039c703ea8e3b9ca63) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *, [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6)) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
const char * | [jack_port_name](group__PortFunctions.html#ga2abf1e9c3fa7d2afae6fd85a6e2ba843) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
[jack_uuid_t](types_8h.html#a346b785a201c9eb5a41a106f87829c9f) | [jack_port_uuid](group__PortFunctions.html#gae563c918af166e1285b8d2811199c302) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
const char * | [jack_port_short_name](group__PortFunctions.html#gaf1554d11abaff29321db1daf1fa614c1) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_flags](group__PortFunctions.html#ga2c9ed0ee016e19070b2e42f7f0a12b95) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
const char * | [jack_port_type](group__PortFunctions.html#gae2b2ef9ef3ba606be342a7d2c292cb00) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_is_mine](group__PortFunctions.html#ga2935e21ef49da7a420aca8cd25e179e6) (const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_connected](group__PortFunctions.html#gafa704768d67d1a30f263a9384d845b14) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_connected_to](group__PortFunctions.html#ga996d8f5176b87bb8d333208468b6af12) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, const char *port_name) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
const char ** | [jack_port_get_connections](group__PortFunctions.html#gac1c942d03daee62ac6d0ed0ad044de43) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
const char ** | [jack_port_get_all_connections](group__PortFunctions.html#ga4e1bd29a68acb4fb45f75931de0d36b2) (const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_tie](group__PortFunctions.html#ga14afcad849c17bcd6cb739d14899cecf) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *src, [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *dst) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
int | [jack_port_untie](group__PortFunctions.html#gaab2cfe13d90991fbf1d03a2050b93f54) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
int | [jack_port_set_name](group__PortFunctions.html#ga1591ad5d2eb3a3d086f2624e006e8daf) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, const char *port_name) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
int | [jack_port_rename](group__PortFunctions.html#ga2de80bfb1a64523a82d1a088379eb6f8) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, const char *port_name) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_set_alias](group__PortFunctions.html#gae76a201e7a6dfe3af6ee78b99a055117) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, const char *alias) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_unset_alias](group__PortFunctions.html#ga51af66966211d2a81a749ab2f689872d) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, const char *alias) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_get_aliases](group__PortFunctions.html#ga3fcae6e043fdb3ac87b173ff4cbf88d9) (const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, char *const aliases[2]) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_request_monitor](group__PortFunctions.html#gab30737dde8a3168a575863de35ed5895) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, int onoff) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_request_monitor_by_name](group__PortFunctions.html#ga5fd1725d66427287abbec29fbae9214b) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, const char *port_name, int onoff) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_ensure_monitor](group__PortFunctions.html#ga75f0438ba447ad96ae890c1922e4af0d) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port, int onoff) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_monitoring_input](group__PortFunctions.html#ga5e52890253590c913913765edf0f9606) ([jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_connect](group__PortFunctions.html#gae6090e81f2ee23b5c0e432a899085ec8) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, const char *source_port, const char *destination_port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_disconnect](group__PortFunctions.html#gaf2bd9f649c51dafdb382847f0c15963f) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, const char *source_port, const char *destination_port) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_disconnect](group__PortFunctions.html#ga92f84d611d7dea399bc97516799ef89d) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *, [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) *) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_name_size](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1) (void) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_port_type_size](group__PortFunctions.html#ga8acf71c319f50c5789f7454e4b6ef2e5) (void) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
size_t | [jack_port_type_get_buffer_size](group__PortFunctions.html#ga52a65a0dd00695ecf75e23f1bd48f96a) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, const char *port_type) JACK_WEAK_EXPORT  
  
## Detailed Description

## Function Documentation

## ◆ jack_connect()

int jack_connect  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | const char * | _source_port_ ,   
|  | const char * | _destination_port_  
| ) | |   
  
Establish a connection between two ports.

When a connection exists, data written to the source port will be available to be read at the destination port.

Precondition
    The port types must be identical.
     The [JackPortFlags](types_8h.html#acbcada380e9dfdd5bff1296e7156f478) of the _source_port_ must include [JackPortIsOutput](types_8h.html#acbcada380e9dfdd5bff1296e7156f478aa0e103ad40ec14c6b50120dd85089c26).
     The [JackPortFlags](types_8h.html#acbcada380e9dfdd5bff1296e7156f478) of the _destination_port_ must include [JackPortIsInput](types_8h.html#acbcada380e9dfdd5bff1296e7156f478a9dea0e7c0d7f57b9674f7c321a5cc50c).

Returns
    0 on success, EEXIST if the connection is already made, otherwise a non-zero error code 

## ◆ jack_disconnect()

int jack_disconnect  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | const char * | _source_port_ ,   
|  | const char * | _destination_port_  
| ) | |   
  
Remove a connection between two ports.

Precondition
    The port types must be identical.
     The [JackPortFlags](types_8h.html#acbcada380e9dfdd5bff1296e7156f478) of the _source_port_ must include [JackPortIsOutput](types_8h.html#acbcada380e9dfdd5bff1296e7156f478aa0e103ad40ec14c6b50120dd85089c26).
     The [JackPortFlags](types_8h.html#acbcada380e9dfdd5bff1296e7156f478) of the _destination_port_ must include [JackPortIsInput](types_8h.html#acbcada380e9dfdd5bff1296e7156f478a9dea0e7c0d7f57b9674f7c321a5cc50c).

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_port_connected()

int jack_port_connected  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    number of connections to or from _port_.

Precondition
    The calling client must own _port_. 

## ◆ jack_port_connected_to()

int jack_port_connected_to  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
---|---|---|---  
|  | const char * | _port_name_  
| ) | |   
  
Returns
    TRUE if the locally-owned _port_ is **directly** connected to the _port_name_.

See also
    [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1)

## ◆ jack_port_disconnect()

int jack_port_disconnect  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * |   
| ) | |   
  
Perform the same function as [jack_disconnect()](group__PortFunctions.html#gaf2bd9f649c51dafdb382847f0c15963f) using port handles rather than names. This avoids the name lookup inherent in the name-based version.

Clients connecting their own ports are likely to use this function, while generic connection clients (e.g. patchbays) would use [jack_disconnect()](group__PortFunctions.html#gaf2bd9f649c51dafdb382847f0c15963f). 

## ◆ jack_port_ensure_monitor()

int jack_port_ensure_monitor  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
---|---|---|---  
|  | int | _onoff_  
| ) | |   
  
If [JackPortCanMonitor](types_8h.html#acbcada380e9dfdd5bff1296e7156f478a0271c73ded98c373ebf8c5e59b51bb0c) is set for a port, this function turns on input monitoring if it was off, and turns it off if only one request has been made to turn it on. Otherwise it does nothing.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_port_flags()

int jack_port_flags  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    the [JackPortFlags](types_8h.html#acbcada380e9dfdd5bff1296e7156f478) of the jack_port_t. 

## ◆ jack_port_get_aliases()

int jack_port_get_aliases  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
---|---|---|---  
|  | char *const | _aliases_[2]  
| ) | |   
  
## ◆ jack_port_get_all_connections()

const char** jack_port_get_all_connections  | ( | const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_  
| ) | |   
  
Returns
    a null-terminated array of full port names to which the _port_ is connected. If none, returns NULL.

The caller is responsible for calling jack_free(3) on any non-NULL returned value.

This differs from [jack_port_get_connections()](group__PortFunctions.html#gac1c942d03daee62ac6d0ed0ad044de43) in two important respects: 
    
    
    1) You may not call this function from code that is
         executed in response to a JACK event. For example,
         you cannot use it in a GraphReordered handler.
    
    2) You need not be the owner of the port to get information
         about its connections. 
    

See also
    [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1)

## ◆ jack_port_get_buffer()

void* jack_port_get_buffer  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | ,   
---|---|---|---  
|  | [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) |   
| ) | |   
  
This returns a pointer to the memory area associated with the specified port. For an output port, it will be a memory area that can be written to; for an input port, it will be an area containing the data from the port's connection(s), or zero-filled. if there are multiple inbound connections, the data will be mixed appropriately.   


Do not cache the returned address across process() callbacks. Port buffers have to be retrieved in each callback for proper functionning. 

## ◆ jack_port_get_connections()

const char** jack_port_get_connections  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    a null-terminated array of full port names to which the _port_ is connected. If none, returns NULL.

The caller is responsible for calling jack_free(3) on any non-NULL returned value.

Parameters
     port| locally owned jack_port_t pointer.  
---|---  
  
See also
    [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1), [jack_port_get_all_connections()](group__PortFunctions.html#ga4e1bd29a68acb4fb45f75931de0d36b2)

## ◆ jack_port_is_mine()

int jack_port_is_mine  | ( | const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_  
| ) | |   
  
Returns
    TRUE if the jack_port_t belongs to the jack_client_t. 

## ◆ jack_port_monitoring_input()

int jack_port_monitoring_input  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    TRUE if input monitoring has been requested for _port_. 

## ◆ jack_port_name()

const char* jack_port_name  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    the full name of the jack_port_t (including the _"client_name:"_ prefix).

See also
    [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1). 

## ◆ jack_port_name_size()

int jack_port_name_size  | ( | void | | ) |   
---|---|---|---|---|---  
  
Returns
    the maximum number of characters in a full JACK port name including the final NULL character. This value is a constant.

A port's full name contains the owning client name concatenated with a colon (:) followed by its short name and a NULL character. 

## ◆ jack_port_register()

[jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931)* jack_port_register  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | const char * | _port_name_ ,   
|  | const char * | _port_type_ ,   
|  | unsigned long | _flags_ ,   
|  | unsigned long | _buffer_size_  
| ) | |   
  
Create a new port for the client. This is an object used for moving data of any type in or out of the client. Ports may be connected in various ways.

Each port has a short name. The port's full name contains the name of the client concatenated with a colon (:) followed by its short name. The [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1) is the maximum length of this full name. Exceeding that will cause the port registration to fail and return NULL.

The _port_name_ must be unique among all ports owned by this client. If the name is not unique, the registration will fail.

All ports have a type, which may be any non-NULL and non-zero length string, passed as an argument. Some port types are built into the JACK API, like JACK_DEFAULT_AUDIO_TYPE or JACK_DEFAULT_MIDI_TYPE

Parameters
     client| pointer to JACK client structure.   
---|---  
port_name| non-empty short name for the new port (not including the leading _"client_name:"_). Must be unique.   
port_type| port type name. If longer than [jack_port_type_size()](group__PortFunctions.html#ga8acf71c319f50c5789f7454e4b6ef2e5), only that many characters are significant.   
flags| [JackPortFlags](types_8h.html#acbcada380e9dfdd5bff1296e7156f478) bit mask.   
buffer_size| must be non-zero if this is not a built-in _port_type_. Otherwise, it is ignored.  
  
Returns
    jack_port_t pointer on success, otherwise NULL. 

## ◆ jack_port_rename()

int jack_port_rename  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
|  | const char * | _port_name_  
| ) | |   
  
Modify a port's short name. May NOT be called from a callback handling a server event.   
If the resulting full name (including the _"client_name:"_ prefix) is longer than [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1), it will be truncated.

Returns
    0 on success, otherwise a non-zero error code.

This differs from [jack_port_set_name()](group__PortFunctions.html#ga1591ad5d2eb3a3d086f2624e006e8daf) by triggering PortRename notifications to clients that have registered a port rename handler. 

## ◆ jack_port_request_monitor()

int jack_port_request_monitor  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
---|---|---|---  
|  | int | _onoff_  
| ) | |   
  
If [JackPortCanMonitor](types_8h.html#acbcada380e9dfdd5bff1296e7156f478a0271c73ded98c373ebf8c5e59b51bb0c) is set for this _port_ , turn input monitoring on or off. Otherwise, do nothing. 

## ◆ jack_port_request_monitor_by_name()

int jack_port_request_monitor_by_name  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | const char * | _port_name_ ,   
|  | int | _onoff_  
| ) | |   
  
If [JackPortCanMonitor](types_8h.html#acbcada380e9dfdd5bff1296e7156f478a0271c73ded98c373ebf8c5e59b51bb0c) is set for this _port_name_ , turn input monitoring on or off. Otherwise, do nothing.

Returns
    0 on success, otherwise a non-zero error code.

See also
    [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1)

## ◆ jack_port_set_alias()

int jack_port_set_alias  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
---|---|---|---  
|  | const char * | _alias_  
| ) | |   
  
Set _alias_ as an alias for _port_. May be called at any time. If the alias is longer than [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1), it will be truncated.

After a successful call, and until JACK exits or [jack_port_unset_alias()](group__PortFunctions.html#ga51af66966211d2a81a749ab2f689872d) is called, may be used as a alternate name for the port.

Ports can have up to two aliases - if both are already set, this function will return an error.

Returns
    0 on success, otherwise a non-zero error code. 

## ◆ jack_port_set_name()

int jack_port_set_name  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
---|---|---|---  
|  | const char * | _port_name_  
| ) | |   
  
Modify a port's short name. May be called at any time. If the resulting full name (including the _"client_name:"_ prefix) is longer than [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1), it will be truncated.

Returns
    0 on success, otherwise a non-zero error code. 

## ◆ jack_port_short_name()

const char* jack_port_short_name  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    the short name of the jack_port_t (not including the _"client_name:"_ prefix).

See also
    [jack_port_name_size()](group__PortFunctions.html#gabaebfd70bedfaecc834ebb02f4546eb1). 

## ◆ jack_port_tie()

int jack_port_tie  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _src_ ,   
---|---|---|---  
|  | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _dst_  
| ) | |   
  
**[Deprecated:](deprecated.html#_deprecated000004)**
     This function will be removed from a future version of JACK. Do not use it. There is no replacement. It has turned out to serve essentially no purpose in real-life JACK clients. 

## ◆ jack_port_type()

const char* jack_port_type  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    the _port_ type, at most [jack_port_type_size()](group__PortFunctions.html#ga8acf71c319f50c5789f7454e4b6ef2e5) characters including a final NULL. 

## ◆ jack_port_type_get_buffer_size()

size_t jack_port_type_get_buffer_size  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | const char * | _port_type_  
| ) | |   
  
Returns
    the buffersize of a port of type 

  * port_type.

this function may only be called in a buffer_size callback. 

## ◆ jack_port_type_size()

int jack_port_type_size  | ( | void | | ) |   
---|---|---|---|---|---  
  
Returns
    the maximum number of characters in a JACK port type name including the final NULL character. This value is a constant. 

## ◆ jack_port_unregister()

int jack_port_unregister  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | ,   
---|---|---|---  
|  | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * |   
| ) | |   
  
Remove the port from the client, disconnecting any existing connections.

Returns
    0 on success, otherwise a non-zero error code 

## ◆ jack_port_unset_alias()

int jack_port_unset_alias  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_ ,   
---|---|---|---  
|  | const char * | _alias_  
| ) | |   
  
Remove _alias_ as an alias for _port_. May be called at any time.

After a successful call, _alias_ can no longer be used as a alternate name for the port.

Returns
    0 on success, otherwise a non-zero error code. 

## ◆ jack_port_untie()

int jack_port_untie  | ( | [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
**[Deprecated:](deprecated.html#_deprecated000005)**
     This function will be removed from a future version of JACK. Do not use it. There is no replacement. It has turned out to serve essentially no purpose in real-life JACK clients. 

## ◆ jack_port_uuid()

[jack_uuid_t](types_8h.html#a346b785a201c9eb5a41a106f87829c9f) jack_port_uuid  | ( | const [jack_port_t](types_8h.html#a91bf0f8fb0619705676136a7f5e3a931) * | _port_| ) |   
---|---|---|---|---|---  
  
Returns
    the UUID of the jack_port_t

See also
    jack_uuid_to_string() to convert into a string representation 

* * *

Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.9.1 
