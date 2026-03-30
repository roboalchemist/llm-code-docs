# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn

Title: conn package - google.golang.org/grpc/credentials/alts/internal/conn - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn

Markdown Content:
conn package - google.golang.org/grpc/credentials/alts/internal/conn - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#)
    *   [Recorded Talks](https://go.dev/talks/) 
Videos from prior events

    *   [Meetups _![Image 7](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go) 
Meet other local Go developers

    *   [Conferences _![Image 8](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences) 
Learn and network with Go developers from around the world

    *   [Go blog](https://go.dev/blog) 
The Go project's official blog.

    *   [Go project](https://go.dev/help) 
Get help and stay informed from Go

    *    Get connected  [![Image 9](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts "Get connected with google-groups (Opens in new window)")[![Image 10](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang "Get connected with github (Opens in new window)")[![Image 11](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang "Get connected with twitter (Opens in new window)")[![Image 12](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/ "Get connected with reddit (Opens in new window)")[![Image 13](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/ "Get connected with slack (Opens in new window)")[![Image 14](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

[![Image 15: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1)
3.   [credentials](https://pkg.go.dev/google.golang.org/grpc/credentials@v1.79.1)
4.   [alts](https://pkg.go.dev/google.golang.org/grpc/credentials/alts@v1.79.1)
5.   [internal](https://pkg.go.dev/google.golang.org/grpc/credentials/alts/internal@v1.79.1)
6.   [conn](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
conn
====

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.79.1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/google.golang.org/grpc/credentials/alts/internal/conn) Published: Feb 13, 2026  License: [Apache-2.0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn?tab=licenses)

 Opens a new window with license information. 

[Imports: 12](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 34: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/grpc/grpc-go/tree/v1.79.1/go.mod) file ![Image 35](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 
*   ![Image 36: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Redistributable license ![Image 37](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 
*   ![Image 38: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Tagged version ![Image 39](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Modules with tagged versions give importers more predictable builds. 
*   ![Image 40: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Stable version ![Image 41](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
When a project reaches major version v1 it is considered stable. 
*   [Learn more about best practices](https://pkg.go.dev/about#best-practices)

Repository
----------

[github.com/grpc/grpc-go](https://github.com/grpc/grpc-go "https://github.com/grpc/grpc-go")

Links
-----

*   [![Image 42: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/google.golang.org%2Fgrpc/v1.79.1 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#section-documentation)
    *   [Overview](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-overview)
    *   [Index](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-index)
    *   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-constants)
    *   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-variables)
    *   [Functions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-functions)
        *   [CounterSide(c)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#CounterSide "CounterSide(c)")
        *   [NewConn(c, side, recordProtocol, key, protected)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewConn "NewConn(c, side, recordProtocol, key, protected)")
        *   [ParseFramedMsg(b, maxLen)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ParseFramedMsg "ParseFramedMsg(b, maxLen)")
        *   [RegisterProtocol(protocol, f)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#RegisterProtocol "RegisterProtocol(protocol, f)")
        *   [SliceForAppend(in, n)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#SliceForAppend "SliceForAppend(in, n)")

    *   [Types](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-types)
        *   [type ALTSRecordCrypto](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordCrypto "type ALTSRecordCrypto")
            *   [NewAES128GCM(side, key)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewAES128GCM "NewAES128GCM(side, key)")
            *   [NewAES128GCMRekey(side, key)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewAES128GCMRekey "NewAES128GCMRekey(side, key)")

        *   [type ALTSRecordFunc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordFunc "type ALTSRecordFunc")
        *   [type Counter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter "type Counter")
            *   [CounterFromValue(value, overflowLen)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#CounterFromValue "CounterFromValue(value, overflowLen)")
            *   [NewInCounter(s, overflowLen)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewInCounter "NewInCounter(s, overflowLen)")
            *   [NewOutCounter(s, overflowLen)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewOutCounter "NewOutCounter(s, overflowLen)")
            *   [(c) Inc()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter.Inc "(c) Inc()")
            *   [(c) Value()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter.Value "(c) Value()")

        *   [type KeySizeError](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#KeySizeError "type KeySizeError")
            *   [(k) Error()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#KeySizeError.Error "(k) Error()")

*   [Source Files](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#section-documentation "Go to Documentation")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-overview "Go to Overview")

Package conn contains an implementation of a secure channel created by gRPC handshakers.

### Index [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-index "Go to Index")

*   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-constants)
*   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-variables)
*   [func CounterSide(c []byte) core.Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#CounterSide)
*   [func NewConn(c net.Conn, side core.Side, recordProtocol string, key []byte, ...) (net.Conn, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewConn)
*   [func ParseFramedMsg(b []byte, maxLen uint32) ([]byte, []byte, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ParseFramedMsg)
*   [func RegisterProtocol(protocol string, f ALTSRecordFunc) error](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#RegisterProtocol)
*   [func SliceForAppend(in []byte, n int) (head, tail []byte)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#SliceForAppend)
*   [type ALTSRecordCrypto](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordCrypto)
*       *   [func NewAES128GCM(side core.Side, key []byte) (ALTSRecordCrypto, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewAES128GCM)
    *   [func NewAES128GCMRekey(side core.Side, key []byte) (ALTSRecordCrypto, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewAES128GCMRekey)

*   [type ALTSRecordFunc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordFunc)
*   [type Counter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter)
*       *   [func CounterFromValue(value []byte, overflowLen int) (c Counter)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#CounterFromValue)
    *   [func NewInCounter(s core.Side, overflowLen int) (c Counter)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewInCounter)
    *   [func NewOutCounter(s core.Side, overflowLen int) (c Counter)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewOutCounter)

*       *   [func (c *Counter) Inc()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter.Inc)
    *   [func (c *Counter) Value() ([]byte, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter.Value)

*   [type KeySizeError](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#KeySizeError)
*       *   [func (k KeySizeError) Error() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#KeySizeError.Error)

### Constants [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-constants "Go to Constants")

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/common.go#L27)const (
// GcmTagSize is the GCM tag size is the difference in length between	// plaintext and ciphertext. From crypto/cipher/gcm.go in Go crypto
	// library.
	GcmTagSize = 16
)

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/record.go#L53)const (
// MsgLenFieldSize is the byte size of the frame length field of a	// framed message.
	MsgLenFieldSize = 4
)

### Variables [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-variables "Go to Variables")

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/common.go#L35)var ErrAuth = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("message authentication failed")

ErrAuth occurs on authentication failure.

### Functions [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-functions "Go to Functions")

#### func [CounterSide](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/utils.go#L58)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#CounterSide "Go to CounterSide")

func CounterSide(c [][byte](https://pkg.go.dev/builtin#byte)) [core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Side)

CounterSide returns the connection side (client/server) a sequence counter is associated with.

#### func [NewConn](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/record.go#L111)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewConn "Go to NewConn")

func NewConn(c [net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn), side [core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Side), recordProtocol [string](https://pkg.go.dev/builtin#string), key [][byte](https://pkg.go.dev/builtin#byte), protected [][byte](https://pkg.go.dev/builtin#byte)) ([net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn), [error](https://pkg.go.dev/builtin#error))

NewConn creates a new secure channel instance given the other party role and handshaking result.

#### func [ParseFramedMsg](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/common.go#L54)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ParseFramedMsg "Go to ParseFramedMsg")

func ParseFramedMsg(b [][byte](https://pkg.go.dev/builtin#byte), maxLen [uint32](https://pkg.go.dev/builtin#uint32)) ([][byte](https://pkg.go.dev/builtin#byte), [][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

ParseFramedMsg parse the provided buffer and returns a frame of the format msgLength+msg and any remaining bytes in that buffer.

#### func [RegisterProtocol](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/record.go#L81)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#RegisterProtocol "Go to RegisterProtocol")

func RegisterProtocol(protocol [string](https://pkg.go.dev/builtin#string), f [ALTSRecordFunc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordFunc)) [error](https://pkg.go.dev/builtin#error)

RegisterProtocol register a ALTS record encryption protocol.

#### func [SliceForAppend](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/common.go#L41)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#SliceForAppend "Go to SliceForAppend")

func SliceForAppend(in [][byte](https://pkg.go.dev/builtin#byte), n [int](https://pkg.go.dev/builtin#int)) (head, tail [][byte](https://pkg.go.dev/builtin#byte))

SliceForAppend takes a slice and a requested number of bytes. It returns a slice with the contents of the given slice followed by that many bytes and a second slice that aliases into it and contains only the extra bytes. If the original slice has sufficient capacity then no allocation is performed.

### Types [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#pkg-types "Go to Types")

#### type [ALTSRecordCrypto](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/record.go#L33)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordCrypto "Go to ALTSRecordCrypto")

type ALTSRecordCrypto interface {
// Encrypt encrypts the plaintext, computes the tag (if any) of dst and	// plaintext, and appends the result to dst, returning the updated slice.
	// dst and plaintext may fully overlap or not at all.
	Encrypt(dst, plaintext [][byte](https://pkg.go.dev/builtin#byte)) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))
// EncryptionOverhead returns the tag size (if any) in bytes.	EncryptionOverhead() [int](https://pkg.go.dev/builtin#int)
// Decrypt decrypts ciphertext and verifies the tag (if any). If successful,	// this function appends the resulting plaintext to dst, returning the
	// updated slice. dst and ciphertext may alias exactly or not at all. To
	// reuse ciphertext's storage for the decrypted output, use ciphertext[:0]
	// as dst. Even if the function fails, the contents of dst, up to its
	// capacity, may be overwritten.
	Decrypt(dst, ciphertext [][byte](https://pkg.go.dev/builtin#byte)) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))
}

ALTSRecordCrypto is the interface for gRPC ALTS record protocol.

#### func [NewAES128GCM](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/aes128gcm.go#L47)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewAES128GCM "Go to NewAES128GCM")

func NewAES128GCM(side [core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Side), key [][byte](https://pkg.go.dev/builtin#byte)) ([ALTSRecordCrypto](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordCrypto), [error](https://pkg.go.dev/builtin#error))

NewAES128GCM creates an instance that uses aes128gcm for ALTS record.

#### func [NewAES128GCMRekey](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/aes128gcmrekey.go#L56)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewAES128GCMRekey "Go to NewAES128GCMRekey")

func NewAES128GCMRekey(side [core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Side), key [][byte](https://pkg.go.dev/builtin#byte)) ([ALTSRecordCrypto](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordCrypto), [error](https://pkg.go.dev/builtin#error))

NewAES128GCMRekey creates an instance that uses aes128gcm with rekeying for ALTS record. The key argument should be 44 bytes, the first 32 bytes are used as a key for HKDF-expand and the remaining 12 bytes are used as a random mask for the counter.

#### type [ALTSRecordFunc](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/record.go#L51)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordFunc "Go to ALTSRecordFunc")

type ALTSRecordFunc func(s [core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Side), keyData [][byte](https://pkg.go.dev/builtin#byte)) ([ALTSRecordCrypto](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#ALTSRecordCrypto), [error](https://pkg.go.dev/builtin#error))

ALTSRecordFunc is a function type for factory functions that create ALTSRecordCrypto instances.

#### type [Counter](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/counter.go#L32)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter "Go to Counter")

type Counter struct {
	// contains filtered or unexported fields
}

Counter is a 96-bit, little-endian counter.

#### func [CounterFromValue](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/utils.go#L50)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#CounterFromValue "Go to CounterFromValue")

func CounterFromValue(value [][byte](https://pkg.go.dev/builtin#byte), overflowLen [int](https://pkg.go.dev/builtin#int)) (c [Counter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter))

CounterFromValue creates a new counter given an initial value.

#### func [NewInCounter](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/utils.go#L39)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewInCounter "Go to NewInCounter")

func NewInCounter(s [core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Side), overflowLen [int](https://pkg.go.dev/builtin#int)) (c [Counter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter))

NewInCounter returns an incoming counter initialized to the starting sequence number for the client/server side of a connection. This is used in ALTS record to check that incoming counters are as expected, since ALTS record guarantees that messages are unwrapped in the same order that the peer wrapped them.

#### func [NewOutCounter](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/utils.go#L25)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#NewOutCounter "Go to NewOutCounter")

func NewOutCounter(s [core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Side](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Side), overflowLen [int](https://pkg.go.dev/builtin#int)) (c [Counter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter))

NewOutCounter returns an outgoing counter initialized to the starting sequence number for the client/server side of a connection.

#### func (*Counter) [Inc](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/counter.go#L47)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter.Inc "Go to Counter.Inc")

func (c *[Counter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter)) Inc()

Inc increments the counter and checks for overflow.

#### func (*Counter) [Value](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/counter.go#L39)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter.Value "Go to Counter.Value")

func (c *[Counter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#Counter)) Value() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

Value returns the current value of the counter as a byte slice.

#### type [KeySizeError](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/aeadrekey.go#L44)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#KeySizeError "Go to KeySizeError")

type KeySizeError [int](https://pkg.go.dev/builtin#int)

KeySizeError signals that the given key does not have the correct size.

#### func (KeySizeError) [Error](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/aeadrekey.go#L46)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#KeySizeError.Error "Go to KeySizeError.Error")

func (k [KeySizeError](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#KeySizeError)) Error() [string](https://pkg.go.dev/builtin#string)

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn#section-sourcefiles "Go to Source Files")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/grpc/grpc-go/tree/v1.79.1/credentials/alts/internal/conn)

*   [aeadrekey.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/aeadrekey.go "aeadrekey.go")
*   [aes128gcm.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/aes128gcm.go "aes128gcm.go")
*   [aes128gcmrekey.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/aes128gcmrekey.go "aes128gcmrekey.go")
*   [common.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/common.go "common.go")
*   [counter.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/counter.go "counter.go")
*   [record.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/record.go "record.go")
*   [utils.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/conn/utils.go "utils.go")

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 45: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 46: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 47: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 48: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 49](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 50: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 51](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 52](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
