# Source: https://jackaudio.org/

JACK-AUDIO-CONNECTION-KIT   
---  
  
  * [Main Page](index.html)
  * [Related Pages](pages.html)
  * [Modules](modules.html)
  * [Data Structures](annotated.html)
  * [Files](files.html)
  * ![](search/mag_sel.svg) [![](search/close.svg)](javascript:searchBox.CloseResultsWindow\(\))




Data Structures | Typedefs | Enumerations | Enumerator | Functions | Variables

Transport and Timebase control

##  Data Structures  
  
---  
struct  | [jack_transport_info_t](structjack__transport__info__t.html)  
  
##  Typedefs  
  
---  
typedef int(* | [JackSyncCallback](group__TransportControl.html#ga566f27eba84e0029eb05a631be52b2e5)) ([jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) state, [jack_position_t](structjack__position__t.html) *pos, void *arg)  
typedef void(* | [JackTimebaseCallback](group__TransportControl.html#ga27ed5006f91b931408b11a5b31150af0)) ([jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) state, [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) nframes, [jack_position_t](structjack__position__t.html) *pos, int new_pos, void *arg)  
  
##  Enumerations  
  
---  
enum  | [jack_transport_bits_t](group__TransportControl.html#ga230191365921fd425c389ed5eab18eef) {   
[JackTransportState](group__TransportControl.html#gga230191365921fd425c389ed5eab18eefa6da5504263d81baf27d53ce2e40e2e9d) = 0x1 , [JackTransportPosition](group__TransportControl.html#gga230191365921fd425c389ed5eab18eefa16f3fb237dea88a0ff61515efc2e6ec8) = 0x2 , [JackTransportLoop](group__TransportControl.html#gga230191365921fd425c389ed5eab18eefa1757aa4327bc7be2cea3f7d07a570896) = 0x4 , [JackTransportSMPTE](group__TransportControl.html#gga230191365921fd425c389ed5eab18eefa19f7f95e8c369e9a2bd91f1e7b75d8ec) = 0x8 ,   
[JackTransportBBT](group__TransportControl.html#gga230191365921fd425c389ed5eab18eefac018587585c9420479978cd49154d02e) = 0x10   
}  
  
##  Functions  
  
---  
int | [jack_release_timebase](group__TransportControl.html#gaea06ff63b129ec6266b2b805b6c8216a) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_sync_callback](group__TransportControl.html#gae53f7ac54804d2896d51b6ad599fa93c) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [JackSyncCallback](group__TransportControl.html#ga566f27eba84e0029eb05a631be52b2e5) sync_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_sync_timeout](group__TransportControl.html#ga2e89b0bb8702d34bcbbe1eac70685ab2) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [jack_time_t](types_8h.html#af9a29b8728e95cc38e2932c0ef855b7e) timeout) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_set_timebase_callback](group__TransportControl.html#ga0c2f2f464f6ba1c0b2aa45e6507b7aa9) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, int conditional, [JackTimebaseCallback](group__TransportControl.html#ga27ed5006f91b931408b11a5b31150af0) timebase_callback, void *arg) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_transport_locate](group__TransportControl.html#gab3f52a42084aead87fd1ee75ed25b240) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) frame) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
[jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) | [jack_transport_query](group__TransportControl.html#ga5f08eb71a5ee5431a3d756af5729d5aa) (const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [jack_position_t](structjack__position__t.html) *pos) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_get_current_transport_frame](group__TransportControl.html#gaef1df9479faa3b7f400c787be173f805) (const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_transport_reposition](group__TransportControl.html#ga2f371010358add3cbed8454bd0bd2ef8) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, const [jack_position_t](structjack__position__t.html) *pos) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
void | [jack_transport_start](group__TransportControl.html#gab7b158bec8f27c03da29795f142d1caf) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
void | [jack_transport_stop](group__TransportControl.html#ga6be6637c314bd88344826e9bcc1957b0) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
void | [jack_get_transport_info](group__TransportControl.html#ga994ea49b518181fbdee2adc9be1ee40e) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [jack_transport_info_t](structjack__transport__info__t.html) *tinfo) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
void | [jack_set_transport_info](group__TransportControl.html#gad27bdf22d5642f2291ba77d7bdb2725a) ([jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) *client, [jack_transport_info_t](structjack__transport__info__t.html) *tinfo) JACK_OPTIONAL_WEAK_DEPRECATED_EXPORT  
  
##  Variables  
  
---  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_transport_info_t::frame_rate](group__TransportControl.html#gab9dcc731355c88c22554ccd18fdcacc0)  
[jack_time_t](types_8h.html#af9a29b8728e95cc38e2932c0ef855b7e) | [jack_transport_info_t::usecs](group__TransportControl.html#gafa8d37eda78c4ce47469157674aaa7e3)  
[jack_transport_bits_t](group__TransportControl.html#ga230191365921fd425c389ed5eab18eef) | [jack_transport_info_t::valid](group__TransportControl.html#ga69fc58b6d2004fd243186255acc7292e)  
[jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) | [jack_transport_info_t::transport_state](group__TransportControl.html#ga748678d245f92f396833cefaca67630c)  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_transport_info_t::frame](group__TransportControl.html#ga7d823f347b9788095d6473dd4ffdf589)  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_transport_info_t::loop_start](group__TransportControl.html#ga1ae73aca12a5e0404bf02f0aed497f02)  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_transport_info_t::loop_end](group__TransportControl.html#ga9effad51f43ef06580217c2c92b3f78d)  
long | [jack_transport_info_t::smpte_offset](group__TransportControl.html#gad04a7477cc221e0dec25b0e207352a2e)  
float | [jack_transport_info_t::smpte_frame_rate](group__TransportControl.html#ga62b6bea05fdb499ca5945a5a32a64350)  
int | [jack_transport_info_t::bar](group__TransportControl.html#gaf2a616f6b626180ca1755ace9b47f25f)  
int | [jack_transport_info_t::beat](group__TransportControl.html#ga3aa1e26090cfefa28315dc3ea2570b84)  
int | [jack_transport_info_t::tick](group__TransportControl.html#ga45efc4128e2405f4f54c8b2340c064cd)  
double | [jack_transport_info_t::bar_start_tick](group__TransportControl.html#ga95bc4a23ed5feaf1f21b5655913c3695)  
float | [jack_transport_info_t::beats_per_bar](group__TransportControl.html#ga7129c362cf296e381ffd992bb70c5659)  
float | [jack_transport_info_t::beat_type](group__TransportControl.html#ga3a568f42b2597a1a8fe5c5681b832c2e)  
double | [jack_transport_info_t::ticks_per_beat](group__TransportControl.html#ga4d98a25dc59cf9c7beb203f32b911a51)  
double | [jack_transport_info_t::beats_per_minute](group__TransportControl.html#ga4505cb67b61179da4a9dd03b7137144e)  
  
## Server-set fields  
  
---  
these cannot be set from clients; the server sets them   
[jack_unique_t](transport_8h.html#af01026c6ef9eb9ef003ed23b6d8ada5f) | [jack_position_t::unique_1](group__TransportControl.html#ga2fe4e3ede6d03c170abce08f867f9bc7)  
[jack_time_t](types_8h.html#af9a29b8728e95cc38e2932c0ef855b7e) | [jack_position_t::usecs](group__TransportControl.html#ga08e43943a7153ecff15b0f8ba6517e95)  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_position_t::frame_rate](group__TransportControl.html#gade3f7758360f5ec5432abaead67b553a)  
  
## Mandatory fields  
  
---  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_position_t::frame](group__TransportControl.html#gab1d0fe08334f47b1aa8bb36ba722228f)  
[jack_position_bits_t](transport_8h.html#a64608154318de05af9e763bfb5fb8529) | [jack_position_t::valid](group__TransportControl.html#ga838c733e8006d1a0cc6921b4a132a8e4)  
  
## JackPositionBBT fields  
  
---  
Bar:Beat.Tick-related information. Applications that support JackPositionBBT are encouraged to also fill the JackBBTFrameOffset   
int32_t | [jack_position_t::bar](group__TransportControl.html#ga4f42cef08eb48a97a1b746698697d0de)  
int32_t | [jack_position_t::beat](group__TransportControl.html#gafb3f220fd87757095057abc152289110)  
int32_t | [jack_position_t::tick](group__TransportControl.html#ga9ba36f6c4eaede3bb1c9b7a85b5f76d1)  
double | [jack_position_t::bar_start_tick](group__TransportControl.html#ga67ff65ba02ba4146b1e46ce6d51ec644)  
float | [jack_position_t::beats_per_bar](group__TransportControl.html#gadc52988414544ba1b86429dad68c6260)  
float | [jack_position_t::beat_type](group__TransportControl.html#ga15383588a3fb97333204bc564cf1c06c)  
double | [jack_position_t::ticks_per_beat](group__TransportControl.html#ga08ca4c388c6460dcef82f03346ccbf52)  
double | [jack_position_t::beats_per_minute](group__TransportControl.html#ga657486be93ebcb20e3a1b45a91f30d33)  
  
## JackPositionTimecode fields <br>  
  
---  
EXPERIMENTAL: could change   
double | [jack_position_t::frame_time](group__TransportControl.html#gabd97b0d447281eebffa750c2b90e791d)  
double | [jack_position_t::next_time](group__TransportControl.html#ga83e65f9658fa4d93658cbad47d446b0b)  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_position_t::bbt_offset](group__TransportControl.html#gae4bb9383734d2e7ca7758011102c03b2)  
float | [jack_position_t::audio_frames_per_video_frame](group__TransportControl.html#gaf28a3e9ee8b36a92309de372093f56f3)  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_position_t::video_offset](group__TransportControl.html#gac03889456c88714ddf680784ee970d3b)  
  
## JACK Extra transport fields  
  
---  
double | [jack_position_t::tick_double](group__TransportControl.html#gabf43d666f71ba6a9dd7f81c68affce99)  
  
## Other fields  
  
---  
int32_t | [jack_position_t::padding](group__TransportControl.html#ga13b42068f5024ec6c29686de66647a73) [5]  
[jack_unique_t](transport_8h.html#af01026c6ef9eb9ef003ed23b6d8ada5f) | [jack_position_t::unique_2](group__TransportControl.html#ga9c3d31034160d5d2b9205eae9983e385)  
  
## Detailed Description

## Typedef Documentation

## ◆ JackSyncCallback

typedef int(* JackSyncCallback) ([jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) state, [jack_position_t](structjack__position__t.html) *pos, void *arg)  
---  
  
Prototype for the _sync_callback_ defined by [slow-sync clients](transport-design.html#slowsyncclients). When the client is active, this callback is invoked just before process() in the same thread. This occurs once after registration, then subsequently whenever some client requests a new position, or the transport enters the [JackTransportStarting](group__TransportControl.html#ga66e50952a88eb087867922bfe3d0bd72a8c1e22fce8ef6c18baf7a5c6a69060ac) state. This realtime function must not wait.

The transport _state_ will be:

  * [JackTransportStopped](group__TransportControl.html#ga66e50952a88eb087867922bfe3d0bd72a30087dc754e67549d91e78a4242393f0) when a new position is requested;
  * [JackTransportStarting](group__TransportControl.html#ga66e50952a88eb087867922bfe3d0bd72a8c1e22fce8ef6c18baf7a5c6a69060ac) when the transport is waiting to start;
  * [JackTransportRolling](group__TransportControl.html#ga66e50952a88eb087867922bfe3d0bd72a4077d7d6fe566f3f0441755a588ad1b2) when the timeout has expired, and the position is now a moving target.



Parameters
     state| current transport state.   
---|---  
pos| new transport position.   
arg| the argument supplied by [jack_set_sync_callback()](group__TransportControl.html#gae53f7ac54804d2896d51b6ad599fa93c).  
  
Returns
    TRUE (non-zero) when ready to roll. 

## ◆ JackTimebaseCallback

typedef void(* JackTimebaseCallback) ([jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) state, [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) nframes, [jack_position_t](structjack__position__t.html) *pos, int new_pos, void *arg)  
---  
  
Prototype for the _timebase_callback_ used to provide extended position information. Its output affects all of the following process cycle. This realtime function must not wait.

This function is called immediately after process() in the same thread whenever the transport is rolling, or when any client has requested a new position in the previous cycle. The first cycle after [jack_set_timebase_callback()](group__TransportControl.html#ga0c2f2f464f6ba1c0b2aa45e6507b7aa9) is also treated as a new position, or the first cycle after [jack_activate()](group__ClientFunctions.html#ga9800d5b29bd7670d9944a15f6ea0ecf8) if the client had been inactive.

The timebase master may not use its _pos_ argument to set _pos- >frame_. To change position, use [jack_transport_reposition()](group__TransportControl.html#ga2f371010358add3cbed8454bd0bd2ef8) or [jack_transport_locate()](group__TransportControl.html#gab3f52a42084aead87fd1ee75ed25b240). These functions are realtime-safe, the _timebase_callback_ can call them directly.

Parameters
     state| current transport state.   
---|---  
nframes| number of frames in current period.   
pos| address of the position structure for the next cycle; _pos- >frame_ will be its frame number. If _new_pos_ is FALSE, this structure contains extended position information from the current cycle. If TRUE, it contains whatever was set by the requester. The _timebase_callback's_ task is to update the extended information here.   
new_pos| TRUE (non-zero) for a newly requested _pos_ , or for the first cycle after the _timebase_callback_ is defined.   
arg| the argument supplied by [jack_set_timebase_callback()](group__TransportControl.html#ga0c2f2f464f6ba1c0b2aa45e6507b7aa9).   
  
## Enumeration Type Documentation

## ◆ jack_transport_bits_t

enum [jack_transport_bits_t](group__TransportControl.html#ga230191365921fd425c389ed5eab18eef)  
---  
  
Optional struct [jack_transport_info_t](structjack__transport__info__t.html) fields.

See also
    [jack_position_bits_t](transport_8h.html#a64608154318de05af9e763bfb5fb8529). 
Enumerator  
---  
JackTransportState | Transport state   
JackTransportPosition | Frame number   
JackTransportLoop | Loop boundaries (ignored)   
JackTransportSMPTE | SMPTE (ignored)   
JackTransportBBT | Bar, Beat, Tick   
  
## Function Documentation

## ◆ jack_get_current_transport_frame()

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_get_current_transport_frame  | ( | const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Return an estimate of the current transport frame, including any time elapsed since the last transport positional update.

Parameters
     client| the JACK client structure   
---|---  
  
## ◆ jack_get_transport_info()

void jack_get_transport_info  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [jack_transport_info_t](structjack__transport__info__t.html) * | _tinfo_  
| ) | |   
  
Gets the current transport info structure (deprecated).

Parameters
     client| the JACK client structure.   
---|---  
tinfo| current transport info structure. The "valid" field describes which fields contain valid data.  
  
**[Deprecated:](deprecated.html#_deprecated000018)**
     This is for compatibility with the earlier transport interface. Use [jack_transport_query()](group__TransportControl.html#ga5f08eb71a5ee5431a3d756af5729d5aa), instead.

Precondition
    Must be called from the process thread. 

## ◆ jack_release_timebase()

int jack_release_timebase  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Called by the timebase master to release itself from that responsibility.

If the timebase master releases the timebase or leaves the JACK graph for any reason, the JACK engine takes over at the start of the next process cycle. The transport state does not change. If rolling, it continues to play, with frame numbers as the only available position information.

See also
    [jack_set_timebase_callback](group__TransportControl.html#ga0c2f2f464f6ba1c0b2aa45e6507b7aa9)

Parameters
     client| the JACK client structure.  
---|---  
  
Returns
    0 on success, otherwise a non-zero error code. 

## ◆ jack_set_sync_callback()

int jack_set_sync_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [JackSyncCallback](group__TransportControl.html#ga566f27eba84e0029eb05a631be52b2e5) | _sync_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Register (or unregister) as a [slow-sync client](transport-design.html#slowsyncclients), that cannot respond immediately to transport position changes.

The _sync_callback_ will be invoked at the first available opportunity after its registration is complete. If the client is currently active this will be the following process cycle, otherwise it will be the first cycle after calling [jack_activate()](group__ClientFunctions.html#ga9800d5b29bd7670d9944a15f6ea0ecf8). After that, it runs according to the [JackSyncCallback](group__TransportControl.html#ga566f27eba84e0029eb05a631be52b2e5) rules. Clients that don't set a _sync_callback_ are assumed to be ready immediately any time the transport wants to start.

Parameters
     client| the JACK client structure.   
---|---  
sync_callback| is a realtime function that returns TRUE when the client is ready. Setting _sync_callback_ to NULL declares that this client no longer requires slow-sync processing.   
arg| an argument for the _sync_callback_ function.  
  
Returns
    0 on success, otherwise a non-zero error code. 

## ◆ jack_set_sync_timeout()

int jack_set_sync_timeout  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [jack_time_t](types_8h.html#af9a29b8728e95cc38e2932c0ef855b7e) | _timeout_  
| ) | |   
  
Set the timeout value for [slow-sync clients](transport-design.html#slowsyncclients).

This timeout prevents unresponsive slow-sync clients from completely halting the transport mechanism. The default is two seconds. When the timeout expires, the transport starts rolling, even if some slow-sync clients are still unready. The _sync_callbacks_ of these clients continue being invoked, giving them a chance to catch up.

See also
    [jack_set_sync_callback](group__TransportControl.html#gae53f7ac54804d2896d51b6ad599fa93c)

Parameters
     client| the JACK client structure.   
---|---  
timeout| is delay (in microseconds) before the timeout expires.  
  
Returns
    0 on success, otherwise a non-zero error code. 

## ◆ jack_set_timebase_callback()

int jack_set_timebase_callback  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | int | _conditional_ ,   
|  | [JackTimebaseCallback](group__TransportControl.html#ga27ed5006f91b931408b11a5b31150af0) | _timebase_callback_ ,   
|  | void * | _arg_  
| ) | |   
  
Register as timebase master for the JACK subsystem.

The timebase master registers a callback that updates extended position information such as beats or timecode whenever necessary. Without this extended information, there is no need for this function.

There is never more than one master at a time. When a new client takes over, the former _timebase_callback_ is no longer called. Taking over the timebase may be done conditionally, so it fails if there was a master already.

The method may be called whether the client has been activated or not.

Parameters
     client| the JACK client structure.   
---|---  
conditional| non-zero for a conditional request.   
timebase_callback| is a realtime function that returns position information.   
arg| an argument for the _timebase_callback_ function.  
  
Returns
    

  * 0 on success;
  * EBUSY if a conditional request fails because there was already a timebase master;
  * other non-zero error code. 



## ◆ jack_set_transport_info()

void jack_set_transport_info  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [jack_transport_info_t](structjack__transport__info__t.html) * | _tinfo_  
| ) | |   
  
Set the transport info structure (deprecated).

**[Deprecated:](deprecated.html#_deprecated000019)**
     This function still exists for compatibility with the earlier transport interface, but it does nothing. Instead, define a [JackTimebaseCallback](group__TransportControl.html#ga27ed5006f91b931408b11a5b31150af0). 

## ◆ jack_transport_locate()

int jack_transport_locate  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | _frame_  
| ) | |   
  
Reposition the transport to a new frame number.

May be called at any time by any client. The new position takes effect in two process cycles. If there are [slow-sync clients](transport-design.html#slowsyncclients) and the transport is already rolling, it will enter the [JackTransportStarting](group__TransportControl.html#ga66e50952a88eb087867922bfe3d0bd72a8c1e22fce8ef6c18baf7a5c6a69060ac) state and begin invoking their _sync_callbacks_ until ready. This function is realtime-safe.

See also
    [jack_transport_reposition](group__TransportControl.html#ga2f371010358add3cbed8454bd0bd2ef8), [jack_set_sync_callback](group__TransportControl.html#gae53f7ac54804d2896d51b6ad599fa93c)

Parameters
     client| the JACK client structure.   
---|---  
frame| frame number of new transport position.  
  
Returns
    0 if valid request, non-zero otherwise. 

## ◆ jack_transport_query()

[jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) jack_transport_query  | ( | const [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | [jack_position_t](structjack__position__t.html) * | _pos_  
| ) | |   
  
Query the current transport state and position.

This function is realtime-safe, and can be called from any thread. If called from the process thread, _pos_ corresponds to the first frame of the current cycle and the state returned is valid for the entire cycle.

Parameters
     client| the JACK client structure.   
---|---  
pos| pointer to structure for returning current transport position; _pos- >valid_ will show which fields contain valid data. If _pos_ is NULL, do not return position information.  
  
Returns
    Current transport state. 

## ◆ jack_transport_reposition()

int jack_transport_reposition  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_ ,   
---|---|---|---  
|  | const [jack_position_t](structjack__position__t.html) * | _pos_  
| ) | |   
  
Request a new transport position.

May be called at any time by any client. The new position takes effect in two process cycles. If there are [slow-sync clients](transport-design.html#slowsyncclients) and the transport is already rolling, it will enter the [JackTransportStarting](group__TransportControl.html#ga66e50952a88eb087867922bfe3d0bd72a8c1e22fce8ef6c18baf7a5c6a69060ac) state and begin invoking their _sync_callbacks_ until ready. This function is realtime-safe.

See also
    [jack_transport_locate](group__TransportControl.html#gab3f52a42084aead87fd1ee75ed25b240), [jack_set_sync_callback](group__TransportControl.html#gae53f7ac54804d2896d51b6ad599fa93c)

Parameters
     client| the JACK client structure.   
---|---  
pos| requested new transport position. Fill pos->valid to specify which fields should be taken into account. If you mark a set of fields as valid, you are expected to fill them all.  
  
Returns
    0 if valid request, EINVAL if position structure rejected. 

## ◆ jack_transport_start()

void jack_transport_start  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Start the JACK transport rolling.

Any client can make this request at any time. It takes effect no sooner than the next process cycle, perhaps later if there are [slow-sync clients](transport-design.html#slowsyncclients). This function is realtime-safe.

See also
    [jack_set_sync_callback](group__TransportControl.html#gae53f7ac54804d2896d51b6ad599fa93c)

Parameters
     client| the JACK client structure.   
---|---  
  
## ◆ jack_transport_stop()

void jack_transport_stop  | ( | [jack_client_t](types_8h.html#a96cf103940d2ee71b141d4b9d0c116bf) * | _client_| ) |   
---|---|---|---|---|---  
  
Stop the JACK transport.

Any client can make this request at any time. It takes effect on the next process cycle. This function is realtime-safe.

Parameters
     client| the JACK client structure.   
---|---  
  
## Variable Documentation

## ◆ audio_frames_per_video_frame

float jack_position_t::audio_frames_per_video_frame  
---  
  
number of audio frames per video frame. Should be assumed zero if JackAudioVideoRatio is not set. If JackAudioVideoRatio is set and the value is zero, no video data exists within the JACK graph 

## ◆ bar [1/2]

int32_t jack_position_t::bar  
---  
  
current bar

Should be >0: the first bar is bar '1'. 

## ◆ bar [2/2]

int jack_transport_info_t::bar  
---  
  
## ◆ bar_start_tick [1/2]

double jack_position_t::bar_start_tick  
---  
  
number of ticks that have elapsed between frame 0 and the first beat of the current measure. 

## ◆ bar_start_tick [2/2]

double jack_transport_info_t::bar_start_tick  
---  
  
## ◆ bbt_offset

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_position_t::bbt_offset  
---  
  
frame offset for the BBT fields (the given bar, beat, and tick values actually refer to a time frame_offset frames before the start of the cycle), should be assumed to be 0 if JackBBTFrameOffset is not set. If JackBBTFrameOffset is set and this value is zero, the BBT time refers to the first frame of this cycle. If the value is positive, the BBT time refers to a frame that many frames before the start of the cycle. 

## ◆ beat [1/2]

int32_t jack_position_t::beat  
---  
  
current beat-within-bar

Should be >0 and <=beats_per_bar: the first beat is beat '1'. 

## ◆ beat [2/2]

int jack_transport_info_t::beat  
---  
  
## ◆ beat_type [1/2]

float jack_position_t::beat_type  
---  
  
time signature "denominator" 

## ◆ beat_type [2/2]

float jack_transport_info_t::beat_type  
---  
  
## ◆ beats_per_bar [1/2]

float jack_position_t::beats_per_bar  
---  
  
time signature "numerator" 

## ◆ beats_per_bar [2/2]

float jack_transport_info_t::beats_per_bar  
---  
  
## ◆ beats_per_minute [1/2]

double jack_position_t::beats_per_minute  
---  
  
BPM, quantized to block size. This means when the tempo is not constant within this block, the BPM value should adapted to compensate for this. This is different from most fields in this struct, which specify the value at the beginning of the block rather than an average. 

## ◆ beats_per_minute [2/2]

double jack_transport_info_t::beats_per_minute  
---  
  
## ◆ frame [1/2]

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_position_t::frame  
---  
  
frame number, always present/required.

This is the frame number on the transport timeline, which is not the same as what [jack_frame_time](group__TimeFunctions.html#ga45cec2e76db58e72b46339229de64697) returns. 

## ◆ frame [2/2]

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_transport_info_t::frame  
---  
  
## ◆ frame_rate [1/2]

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_position_t::frame_rate  
---  
  
current frame rate, in frames per second 

## ◆ frame_rate [2/2]

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_transport_info_t::frame_rate  
---  
  
current frame rate (per second) 

## ◆ frame_time

double jack_position_t::frame_time  
---  
  
current time in seconds 

## ◆ loop_end

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_transport_info_t::loop_end  
---  
  
## ◆ loop_start

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_transport_info_t::loop_start  
---  
  
## ◆ next_time

double jack_position_t::next_time  
---  
  
next sequential frame_time (unless repositioned) 

## ◆ padding

int32_t jack_position_t::padding[5]  
---  
  
## ◆ smpte_frame_rate

float jack_transport_info_t::smpte_frame_rate  
---  
  
29.97, 30, 24 etc. 

## ◆ smpte_offset

long jack_transport_info_t::smpte_offset  
---  
  
SMPTE offset (from frame 0) 

## ◆ tick [1/2]

int32_t jack_position_t::tick  
---  
  
current tick-within-beat

Should be >= 0 and < ticks_per_beat: the first tick is tick '0'. 

## ◆ tick [2/2]

int jack_transport_info_t::tick  
---  
  
## ◆ tick_double

double jack_position_t::tick_double  
---  
  
current tick-within-beat in double resolution. Should be assumed zero if JackTickDouble is not set. Since older versions of JACK do not expose this variable, the macro JACK_TICK_DOUBLE is provided, which can be used as build-time detection. 

## ◆ ticks_per_beat [1/2]

double jack_position_t::ticks_per_beat  
---  
  
number of ticks within a beat.

Usually a moderately large integer with many denominators, such as 1920.0 

## ◆ ticks_per_beat [2/2]

double jack_transport_info_t::ticks_per_beat  
---  
  
## ◆ transport_state

[jack_transport_state_t](transport_8h.html#a66e50952a88eb087867922bfe3d0bd72) jack_transport_info_t::transport_state  
---  
  
## ◆ unique_1

[jack_unique_t](transport_8h.html#af01026c6ef9eb9ef003ed23b6d8ada5f) jack_position_t::unique_1  
---  
  
unique ID 

## ◆ unique_2

[jack_unique_t](transport_8h.html#af01026c6ef9eb9ef003ed23b6d8ada5f) jack_position_t::unique_2  
---  
  
unique ID 

## ◆ usecs [1/2]

[jack_time_t](types_8h.html#af9a29b8728e95cc38e2932c0ef855b7e) jack_position_t::usecs  
---  
  
microsecond timestamp that is guaranteed to be monotonic, but not neccessarily linear.

The absolute value is implementation-dependent (i.e. it could be wall-clock, time since jack started, uptime, etc). 

## ◆ usecs [2/2]

[jack_time_t](types_8h.html#af9a29b8728e95cc38e2932c0ef855b7e) jack_transport_info_t::usecs  
---  
  
monotonic, free-rolling 

## ◆ valid [1/2]

[jack_position_bits_t](transport_8h.html#a64608154318de05af9e763bfb5fb8529) jack_position_t::valid  
---  
  
which other fields are valid, as a bitmask constructed from values in [jack_position_bits_t](transport_8h.html#a64608154318de05af9e763bfb5fb8529)

## ◆ valid [2/2]

[jack_transport_bits_t](group__TransportControl.html#ga230191365921fd425c389ed5eab18eef) jack_transport_info_t::valid  
---  
  
which fields are legal to read 

## ◆ video_offset

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_position_t::video_offset  
---  
  
audio frame at which the first video frame in this cycle occurs. Should be assumed to be 0 if JackVideoFrameOffset is not set. If JackVideoFrameOffset is set, but the value is zero, there is no video frame within this cycle. 

* * *

Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.9.1 
