# Source: https://jackaudio.org/

JACK-AUDIO-CONNECTION-KIT   
---  
  
  * [Main Page](index.html)
  * [Related Pages](pages.html)
  * [Modules](modules.html)
  * [Data Structures](annotated.html)
  * [Files](files.html)
  * ![](search/mag_sel.svg) [![](search/close.svg)](javascript:searchBox.CloseResultsWindow\(\))




Functions | Variables

Reading and writing MIDI data

##  Functions  
  
---  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [jack_midi_get_event_count](group__MIDIAPI.html#ga0a87111085b94460401b0b688595a138) (void *port_buffer) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_midi_event_get](group__MIDIAPI.html#ga838c794bd1451bfd47edde1c7cd1ff4f) ([jack_midi_event_t](midiport_8h.html#ae34bec0cd504eee54afffda51122a352) *event, void *port_buffer, uint32_t event_index) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
void | [jack_midi_clear_buffer](group__MIDIAPI.html#ga7635c6e0a4eb2314a5fb5a058c278078) (void *port_buffer) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
size_t | [jack_midi_max_event_size](group__MIDIAPI.html#gab69743a191f150757fa3708eae8fdb81) (void *port_buffer) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
[jack_midi_data_t](midiport_8h.html#ad1df9c73b07584ffb69c276421ff55c9) * | [jack_midi_event_reserve](group__MIDIAPI.html#ga150dcdc37583e1ecbe0a6f16b6ac48a9) (void *port_buffer, [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) time, size_t data_size) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
int | [jack_midi_event_write](group__MIDIAPI.html#gaa25503c07ac3c2ed62d79be9c25d42ed) (void *port_buffer, [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) time, const [jack_midi_data_t](midiport_8h.html#ad1df9c73b07584ffb69c276421ff55c9) *data, size_t data_size) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
uint32_t | [jack_midi_get_lost_event_count](group__MIDIAPI.html#ga0f5af3d054e218a5b90fd4c636425e45) (void *port_buffer) [JACK_OPTIONAL_WEAK_EXPORT](weakmacros_8h.html#adf1bde0dd996bbf61a44311165014dd1)  
  
##  Variables  
  
---  
[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | [_jack_midi_event::time](group__MIDIAPI.html#ga7acc6a81ac12e2a042d5af9fb7b56532)  
size_t | [_jack_midi_event::size](group__MIDIAPI.html#gabc254ee669d342c75ccfa49658b54a56)  
[jack_midi_data_t](midiport_8h.html#ad1df9c73b07584ffb69c276421ff55c9) * | [_jack_midi_event::buffer](group__MIDIAPI.html#gadebcb1577b20165e4da170f8992bc0ba)  
  
## Detailed Description

## Function Documentation

## ◆ jack_midi_clear_buffer()

void jack_midi_clear_buffer  | ( | void * | _port_buffer_| ) |   
---|---|---|---|---|---  
  
Clear an event buffer.

This should be called at the beginning of each process cycle before calling [jack_midi_event_reserve](group__MIDIAPI.html#ga150dcdc37583e1ecbe0a6f16b6ac48a9) or [jack_midi_event_write](group__MIDIAPI.html#gaa25503c07ac3c2ed62d79be9c25d42ed). This function may not be called on an input port's buffer.

Parameters
     port_buffer| Port buffer to clear (must be an output port buffer).   
---|---  
  
## ◆ jack_midi_event_get()

int jack_midi_event_get  | ( | [jack_midi_event_t](midiport_8h.html#ae34bec0cd504eee54afffda51122a352) * | _event_ ,   
---|---|---|---  
|  | void * | _port_buffer_ ,   
|  | uint32_t | _event_index_  
| ) | |   
  
Get a MIDI event from an event port buffer.

Jack MIDI is normalised, the MIDI event returned by this function is guaranteed to be a complete MIDI event (the status byte will always be present, and no realtime events will interspered with the event).

Parameters
     event| Event structure to store retrieved event in.   
---|---  
port_buffer| Port buffer from which to retrieve event.   
event_index| Index of event to retrieve.   
  
Returns
    0 on success, ENODATA if buffer is empty. 

## ◆ jack_midi_event_reserve()

[jack_midi_data_t](midiport_8h.html#ad1df9c73b07584ffb69c276421ff55c9)* jack_midi_event_reserve  | ( | void * | _port_buffer_ ,   
---|---|---|---  
|  | [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | _time_ ,   
|  | size_t | _data_size_  
| ) | |   
  
Allocate space for an event to be written to an event port buffer.

Clients are to write the actual event data to be written starting at the pointer returned by this function. Clients must not write more than _data_size_ bytes into this buffer. Clients must write normalised MIDI data to the port - no running status and no (1-byte) realtime messages interspersed with other messages (realtime messages are fine when they occur on their own, like other messages).

Events must be written in order, sorted by their sample offsets. JACK will not sort the events for you, and will refuse to store out-of-order events.

Parameters
     port_buffer| Buffer to write event to.   
---|---  
time| Sample offset of event.   
data_size| Length of event's raw data in bytes.   
  
Returns
    Pointer to the beginning of the reserved event's data buffer, or NULL on error (ie not enough space). 

## ◆ jack_midi_event_write()

int jack_midi_event_write  | ( | void * | _port_buffer_ ,   
---|---|---|---  
|  | [jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) | _time_ ,   
|  | const [jack_midi_data_t](midiport_8h.html#ad1df9c73b07584ffb69c276421ff55c9) * | _data_ ,   
|  | size_t | _data_size_  
| ) | |   
  
Write an event into an event port buffer.

This function is simply a wrapper for [jack_midi_event_reserve](group__MIDIAPI.html#ga150dcdc37583e1ecbe0a6f16b6ac48a9) which writes the event data into the space reserved in the buffer.

Clients must not write more than _data_size_ bytes into this buffer. Clients must write normalised MIDI data to the port - no running status and no (1-byte) realtime messages interspersed with other messages (realtime messages are fine when they occur on their own, like other messages).

Events must be written in order, sorted by their sample offsets. JACK will not sort the events for you, and will refuse to store out-of-order events.

Parameters
     port_buffer| Buffer to write event to.   
---|---  
time| Sample offset of event.   
data| Message data to be written.   
data_size| Length of _data_ in bytes.   
  
Returns
    0 on success, ENOBUFS if there's not enough space in buffer for event. 

## ◆ jack_midi_get_event_count()

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) jack_midi_get_event_count  | ( | void * | _port_buffer_| ) |   
---|---|---|---|---|---  
  
## ◆ jack_midi_get_lost_event_count()

uint32_t jack_midi_get_lost_event_count  | ( | void * | _port_buffer_| ) |   
---|---|---|---|---|---  
  
Get the number of events that could not be written to _port_buffer_.

This function returning a non-zero value implies _port_buffer_ is full. Currently the only way this can happen is if events are lost on port mixdown.

Parameters
     port_buffer| Port to receive count for.   
---|---  
  
Returns
    Number of events that could not be written to _port_buffer_. 

## ◆ jack_midi_max_event_size()

size_t jack_midi_max_event_size  | ( | void * | _port_buffer_| ) |   
---|---|---|---|---|---  
  
Get the size of the largest event that can be stored by the port.

This function returns the current space available, taking into account events already stored in the port.

Parameters
     port_buffer| Port buffer to check size of.   
---|---  
  
## Variable Documentation

## ◆ buffer

[jack_midi_data_t](midiport_8h.html#ad1df9c73b07584ffb69c276421ff55c9)* _jack_midi_event::buffer  
---  
  
Raw MIDI data 

## ◆ size

size_t _jack_midi_event::size  
---  
  
Number of bytes of data in _buffer_

## ◆ time

[jack_nframes_t](types_8h.html#aa954df532e901ae5172e68a23f3da9b6) _jack_midi_event::time  
---  
  
Sample index at which event is valid 

* * *

Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.9.1 
