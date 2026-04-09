# go-sse Example - Hello World Server and Client

## Server

> Source: <https://github.com/tmaxmax/go-sse/blob/master/cmd/helloworld/main.go>

```go
package main

import (
	"log"
	"net/http"
	"time"

	"github.com/tmaxmax/go-sse"
)

func main() {
	s := &sse.Server{}

	go func() {
		ev := &sse.Message{}
		ev.AppendData("Hello world")

		for range time.Tick(time.Second) {
			_ = s.Publish(ev)
		}
	}()

	//nolint:gosec // Use http.Server in your code instead, to be able to set timeouts.
	if err := http.ListenAndServe(":8000", s); err != nil {
		log.Fatalln(err)
	}
}
```

## Client

> Source: <https://github.com/tmaxmax/go-sse/blob/master/cmd/helloworld_client/client.go>

```go
package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/tmaxmax/go-sse"
)

func main() {
	r, _ := http.NewRequest(http.MethodGet, "http://localhost:8000", http.NoBody)
	conn := sse.NewConnection(r)

	conn.SubscribeMessages(func(event sse.Event) {
		fmt.Printf("%s\n\n", event.Data)
	})

	if err := conn.Connect(); err != nil {
		fmt.Fprintln(os.Stderr, err)
	}
}
```
