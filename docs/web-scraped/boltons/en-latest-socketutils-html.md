# Source: https://boltons.readthedocs.io/en/latest/socketutils.html

Title: socket wrappers — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/socketutils.html

Markdown Content:
`socketutils` - `socket` wrappers[](https://boltons.readthedocs.io/en/latest/socketutils.html#module-boltons.socketutils "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

At its heart, Python can be viewed as an extension of the C programming language. Springing from the most popular systems programming language has made Python itself a great language for systems programming. One key to success in this domain is Python’s very serviceable [`socket`](https://docs.python.org/3/library/socket.html#module-socket "(in Python v3.14)") module and its [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "(in Python v3.14)") type.

The `socketutils` module provides natural next steps to the `socket` builtin: straightforward, tested building blocks for higher-level protocols.

The [`BufferedSocket`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket "boltons.socketutils.BufferedSocket") wraps an ordinary socket, providing a layer of intuitive buffering for both sending and receiving. This facilitates parsing messages from streams, i.e., all sockets with type `SOCK_STREAM`. The BufferedSocket enables receiving until the next relevant token, up to a certain size, or until the connection is closed. For all of these, it provides consistent APIs to size limiting, as well as timeouts that are compatible with multiple concurrency paradigms. Use it to parse the next one-off text or binary socket protocol you encounter.

This module also provides the [`NetstringSocket`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.NetstringSocket "boltons.socketutils.NetstringSocket"), a pure-Python implementation of [the Netstring protocol](https://en.wikipedia.org/wiki/Netstring), built on top of the [`BufferedSocket`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket "boltons.socketutils.BufferedSocket"), serving as a ready-made, production-grade example.

Special thanks to [Kurt Rose](https://github.com/doublereedkurt) for his original authorship and all his contributions on this module. Also thanks to [Daniel J. Bernstein](https://cr.yp.to/), the original author of [Netstring](https://cr.yp.to/proto/netstrings.txt).

BufferedSocket[](https://boltons.readthedocs.io/en/latest/socketutils.html#bufferedsocket "Link to this heading")
------------------------------------------------------------------------------------------------------------------

_class_ boltons.socketutils.BufferedSocket(_sock_, _timeout=\_UNSET_, _maxsize=32768_, _recvsize=\_UNSET_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket "Link to this definition")
Mainly provides recv_until and recv_size. recv, send, sendall, and peek all function as similarly as possible to the built-in socket API.

This type has been tested against both the built-in socket type as well as those from gevent and eventlet. It also features support for sockets with timeouts set to 0 (aka nonblocking), provided the caller is prepared to handle the EWOULDBLOCK exceptions.

Parameters:
*   **sock** (_socket_) – The connected socket to be wrapped.

*   **timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – The default timeout for sends and recvs, in seconds. Set to `None` for no timeout, and 0 for nonblocking. Defaults to _sock_’s own timeout if already set, and 10 seconds otherwise.

*   **maxsize** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The default maximum number of bytes to be received into the buffer before it is considered full and raises an exception. Defaults to 32 kilobytes.

*   **recvsize** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The number of bytes to recv for every lower-level `socket.recv()` call. Defaults to _maxsize_.

_timeout_ and _maxsize_ can both be overridden on individual socket operations.

All `recv` methods return bytestrings ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")) and can raise [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)"). [`Timeout`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Timeout "boltons.socketutils.Timeout"), [`ConnectionClosed`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.ConnectionClosed "boltons.socketutils.ConnectionClosed"), and [`MessageTooLong`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.MessageTooLong "boltons.socketutils.MessageTooLong") all inherit from [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)") and exist to provide better error messages. Received bytes are always buffered, even if an exception is raised. Use [`BufferedSocket.getrecvbuffer()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getrecvbuffer "boltons.socketutils.BufferedSocket.getrecvbuffer") to retrieve partial recvs.

BufferedSocket does not replace the built-in socket by any means. While the overlapping parts of the API are kept parallel to the built-in [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "(in Python v3.14)"), BufferedSocket does not inherit from socket, and most socket functionality is only available on the underlying socket. `socket.getpeername()`, `socket.getsockname()`, `socket.fileno()`, and others are only available on the underlying socket that is wrapped. Use the `BufferedSocket.sock` attribute to access it. See the examples for more information on how to use BufferedSockets with built-in sockets.

The BufferedSocket is threadsafe, but consider the semantics of your protocol before accessing a single socket from multiple threads. Similarly, once the BufferedSocket is constructed, avoid using the underlying socket directly. Only use it for operations unrelated to messages, e.g., `socket.getpeername()`.

buffer(_data_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.buffer)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.buffer "Link to this definition")
Buffer _data_ bytes for the next send operation.

close()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.close)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.close "Link to this definition")
Closes the wrapped socket, and empties the internal buffers. The send buffer is not flushed automatically, so if you have been calling [`buffer()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.buffer "boltons.socketutils.BufferedSocket.buffer"), be sure to call [`flush()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.flush "boltons.socketutils.BufferedSocket.flush") before calling this method. After calling this method, future socket operations will raise [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)").

_property_ family[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.family "Link to this definition")
A passthrough to the wrapped socket’s family. BufferedSocket supports all widely-used families, so this read-only attribute can be one of [`socket.AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "(in Python v3.14)") for IP, [`socket.AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "(in Python v3.14)") for IPv6, and [`socket.AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "(in Python v3.14)") for UDS.

fileno()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.fileno)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.fileno "Link to this definition")
Returns the file descriptor of the wrapped socket. -1 if it has been closed on this end.

Note that this makes the BufferedSocket selectable, i.e., usable for operating system event loops without any external libraries. Keep in mind that the operating system cannot know about data in BufferedSocket’s internal buffer. Exercise discipline with calling `recv*` functions.

flush()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.flush)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.flush "Link to this definition")
Send the contents of the internal send buffer.

getpeername()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.getpeername)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getpeername "Link to this definition")
Convenience function to return the remote address to which the wrapped socket is connected. See `socket.getpeername()` for more details.

getrecvbuffer()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.getrecvbuffer)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getrecvbuffer "Link to this definition")
Returns the receive buffer bytestring (rbuf).

getsendbuffer()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.getsendbuffer)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getsendbuffer "Link to this definition")
Returns a copy of the send buffer list.

getsockname()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.getsockname)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getsockname "Link to this definition")
Convenience function to return the wrapped socket’s own address. See `socket.getsockname()` for more details.

getsockopt(_level_, _optname_, _buflen=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.getsockopt)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getsockopt "Link to this definition")
Convenience function passing through to the wrapped socket’s `socket.getsockopt()`.

peek(_size_, _timeout=\_UNSET_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.peek)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.peek "Link to this definition")
Returns _size_ bytes from the socket and/or internal buffer. Bytes are retained in BufferedSocket’s internal recv buffer. To only see bytes in the recv buffer, use [`getrecvbuffer()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getrecvbuffer "boltons.socketutils.BufferedSocket.getrecvbuffer").

Parameters:
*   **size** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The exact number of bytes to peek at

*   **timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – The timeout for this operation. Can be 0 for nonblocking and None for no timeout. Defaults to the value set in the constructor of BufferedSocket.

If the appropriate number of bytes cannot be fetched from the buffer and socket before _timeout_ expires, then a [`Timeout`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Timeout "boltons.socketutils.Timeout") will be raised. If the connection is closed, a [`ConnectionClosed`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.ConnectionClosed "boltons.socketutils.ConnectionClosed") will be raised.

_property_ proto[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.proto "Link to this definition")
A passthrough to the wrapped socket’s protocol. The `proto` attribute is very rarely used, so it’s always 0, meaning “the default” protocol. Pretty much all the practical information is in [`type`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.type "boltons.socketutils.BufferedSocket.type") and [`family`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.family "boltons.socketutils.BufferedSocket.family"), so you can go back to never thinking about this.

recv(_size_, _flags=0_, _timeout=\_UNSET_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.recv)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv "Link to this definition")
Returns **up to**_size_ bytes, using the internal buffer before performing a single `socket.recv()` operation.

Parameters:
*   **size** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The maximum number of bytes to receive.

*   **flags** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Kept for API compatibility with sockets. Only the default, `0`, is valid.

*   **timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – The timeout for this operation. Can be `0` for nonblocking and `None` for no timeout. Defaults to the value set in the constructor of BufferedSocket.

If the operation does not complete in _timeout_ seconds, a [`Timeout`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Timeout "boltons.socketutils.Timeout") is raised. Much like the built-in [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "(in Python v3.14)"), if this method returns an empty string, then the socket is closed and recv buffer is empty. Further calls to recv will raise [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)").

recv_close(_timeout=\_UNSET_, _maxsize=\_UNSET_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.recv_close)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv_close "Link to this definition")
Receive until the connection is closed, up to _maxsize_ bytes. If more than _maxsize_ bytes are received, raises [`MessageTooLong`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.MessageTooLong "boltons.socketutils.MessageTooLong").

recv_size(_size_, _timeout=\_UNSET_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.recv_size)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv_size "Link to this definition")
Read off of the internal buffer, then off the socket, until _size_ bytes have been read.

Parameters:
*   **size** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – number of bytes to read before returning.

*   **timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – The timeout for this operation. Can be 0 for nonblocking and None for no timeout. Defaults to the value set in the constructor of BufferedSocket.

If the appropriate number of bytes cannot be fetched from the buffer and socket before _timeout_ expires, then a [`Timeout`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Timeout "boltons.socketutils.Timeout") will be raised. If the connection is closed, a [`ConnectionClosed`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.ConnectionClosed "boltons.socketutils.ConnectionClosed") will be raised.

recv_until(_delimiter_, _timeout=\_UNSET_, _maxsize=\_UNSET_, _with\_delimiter=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.recv_until)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv_until "Link to this definition")
Receive until _delimiter_ is found, _maxsize_ bytes have been read, or _timeout_ is exceeded.

Parameters:
*   **delimiter** ([_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")) – One or more bytes to be searched for in the socket stream.

*   **timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – The timeout for this operation. Can be 0 for nonblocking and None for no timeout. Defaults to the value set in the constructor of BufferedSocket.

*   **maxsize** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The maximum size for the internal buffer. Defaults to the value set in the constructor.

*   **with_delimiter** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether or not to include the delimiter in the output. `False` by default, but `True` is useful in cases where one is simply forwarding the messages.

`recv_until` will raise the following exceptions:

> *   [`Timeout`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Timeout "boltons.socketutils.Timeout") if more than _timeout_ seconds expire.
> 
> *   [`ConnectionClosed`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.ConnectionClosed "boltons.socketutils.ConnectionClosed") if the underlying socket is closed by the sending end.
> 
> *   [`MessageTooLong`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.MessageTooLong "boltons.socketutils.MessageTooLong") if the delimiter is not found in the first _maxsize_ bytes.
> 
> *   [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)") if operating in nonblocking mode (_timeout_ equal to 0), or if some unexpected socket error occurs, such as operating on a closed socket.

send(_data_, _flags=0_, _timeout=\_UNSET_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.send)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.send "Link to this definition")
Send the contents of the internal send buffer, as well as _data_, to the receiving end of the connection. Returns the total number of bytes sent. If no exception is raised, all of _data_ was sent and the internal send buffer is empty.

Parameters:
*   **data** ([_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")) – The bytes to send.

*   **flags** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Kept for API compatibility with sockets. Only the default 0 is valid.

*   **timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – The timeout for this operation. Can be 0 for nonblocking and None for no timeout. Defaults to the value set in the constructor of BufferedSocket.

Will raise [`Timeout`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Timeout "boltons.socketutils.Timeout") if the send operation fails to complete before _timeout_. In the event of an exception, use [`BufferedSocket.getsendbuffer()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.getsendbuffer "boltons.socketutils.BufferedSocket.getsendbuffer") to see which data was unsent.

sendall(_data_, _flags=0_, _timeout=\_UNSET_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.sendall)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.sendall "Link to this definition")
A passthrough to [`send()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.send "boltons.socketutils.BufferedSocket.send"), retained for parallelism to the [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "(in Python v3.14)") API.

setmaxsize(_maxsize_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.setmaxsize)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.setmaxsize "Link to this definition")
Set the default maximum buffer size _maxsize_ for future operations, in bytes. Does not truncate the current buffer.

setsockopt(_level_, _optname_, _value_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.setsockopt)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.setsockopt "Link to this definition")
Convenience function passing through to the wrapped socket’s `socket.setsockopt()`.

settimeout(_timeout_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.settimeout)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.settimeout "Link to this definition")
Set the default _timeout_ for future operations, in seconds.

shutdown(_how_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#BufferedSocket.shutdown)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.shutdown "Link to this definition")
Convenience method which passes through to the wrapped socket’s `shutdown()`. Semantics vary by platform, so no special internal handling is done with the buffers. This method exists to facilitate the most common usage, wherein a full `shutdown` is followed by a [`close()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.close "boltons.socketutils.BufferedSocket.close"). Developers requiring more support, please open [an issue](https://github.com/mahmoud/boltons/issues).

_property_ type[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.type "Link to this definition")
A passthrough to the wrapped socket’s type. Valid usages should only ever see [`socket.SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "(in Python v3.14)").

### Exceptions[](https://boltons.readthedocs.io/en/latest/socketutils.html#exceptions "Link to this heading")

These are a few exceptions that derive from [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)") and provide clearer code and better error messages.

_exception_ boltons.socketutils.Error[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#Error)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Error "Link to this definition")
A subclass of [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)") from which all other `socketutils` exceptions inherit.

When using [`BufferedSocket`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket "boltons.socketutils.BufferedSocket") and other `socketutils` types, generally you want to catch one of the specific exception types below, or [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "(in Python v3.14)").

_exception_ boltons.socketutils.Timeout(_timeout_, _extra=''_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#Timeout)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.Timeout "Link to this definition")
Inheriting from [`socket.timeout`](https://docs.python.org/3/library/socket.html#socket.timeout "(in Python v3.14)"), Timeout is used to indicate when a socket operation did not complete within the time specified. Raised from any of [`BufferedSocket`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket "boltons.socketutils.BufferedSocket")’s `recv` methods.

_exception_ boltons.socketutils.ConnectionClosed[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#ConnectionClosed)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.ConnectionClosed "Link to this definition")
Raised when receiving and the connection is unexpectedly closed from the sending end. Raised from [`BufferedSocket`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket "boltons.socketutils.BufferedSocket")’s [`peek()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.peek "boltons.socketutils.BufferedSocket.peek"), [`recv_until()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv_until "boltons.socketutils.BufferedSocket.recv_until"), and [`recv_size()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv_size "boltons.socketutils.BufferedSocket.recv_size"), and never from its [`recv()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv "boltons.socketutils.BufferedSocket.recv") or [`recv_close()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv_close "boltons.socketutils.BufferedSocket.recv_close").

_exception_ boltons.socketutils.MessageTooLong(_bytes\_read=None_, _delimiter=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#MessageTooLong)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.MessageTooLong "Link to this definition")
Raised from [`BufferedSocket.recv_until()`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.BufferedSocket.recv_until "boltons.socketutils.BufferedSocket.recv_until") and `BufferedSocket.recv_closed()` when more than _maxsize_ bytes are read without encountering the delimiter or a closed connection, respectively.

Netstring[](https://boltons.readthedocs.io/en/latest/socketutils.html#id1 "Link to this heading")
--------------------------------------------------------------------------------------------------

_class_ boltons.socketutils.NetstringSocket(_sock_, _timeout=10_, _maxsize=32768_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#NetstringSocket)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.NetstringSocket "Link to this definition")
Reads and writes using the netstring protocol.

More info: [https://en.wikipedia.org/wiki/Netstring](https://en.wikipedia.org/wiki/Netstring) Even more info: [http://cr.yp.to/proto/netstrings.txt](http://cr.yp.to/proto/netstrings.txt)

### Nestring Exceptions[](https://boltons.readthedocs.io/en/latest/socketutils.html#nestring-exceptions "Link to this heading")

These are a few higher-level exceptions for Netstring connections.

_exception_ boltons.socketutils.NetstringProtocolError[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#NetstringProtocolError)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.NetstringProtocolError "Link to this definition")
Base class for all of socketutils’ Netstring exception types.

_exception_ boltons.socketutils.NetstringInvalidSize(_msg_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#NetstringInvalidSize)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.NetstringInvalidSize "Link to this definition")
NetstringInvalidSize is raised when the `:`-delimited size prefix of the message does not contain a valid integer.

Message showing valid size:

5:hello,

Here the `5` is the size. Anything in this prefix position that is not parsable as a Python integer (i.e., [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) will raise this exception.

_exception_ boltons.socketutils.NetstringMessageTooLong(_size_, _maxsize_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/socketutils.html#NetstringMessageTooLong)[](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.NetstringMessageTooLong "Link to this definition")
NetstringMessageTooLong is raised when the size prefix contains a valid integer, but that integer is larger than the [`NetstringSocket`](https://boltons.readthedocs.io/en/latest/socketutils.html#boltons.socketutils.NetstringSocket "boltons.socketutils.NetstringSocket")’s configured _maxsize_.

When this exception is raised, it’s recommended to simply close the connection instead of trying to recover.
