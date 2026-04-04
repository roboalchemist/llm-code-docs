# Source: https://screenshotone.com/docs/code-examples/go/

# Go SDK and Code Examples

import Alert from "@/components/Alert.astro";

<Alert>
    If you have any questions, please, reach out at `support@screenshotone.com`.
</Alert>

It takes minutes to start taking screenshots in Go. Just [sign up](https://dash.screenshotone.com/sign-up) to get access and secret keys, import the client, and you are ready to go.

### Installation

```shell
go get github.com/screenshotone/gosdk
```

### Usage

Import the library:

```go
import screenshots "github.com/screenshotone/gosdk"
```

Generate a screenshot URL without executing request:

```go
client, err := screenshots.NewClient("IVmt2ghj9TG_jQ", "Sxt94yAj9aQSgg")
if err != nil {
    // ...
}

options := screenshots.NewTakeOptions("https://scalabledeveloper.com").
    Format("png").
    FullPage(true).
    DeviceScaleFactor(2).
    BlockAds(true).
    BlockTrackers(true)

u, err := client.GenerateTakeURL(options)
if err != nil {
    // ...
}

fmt.Println(u.String())
// Output: https://api.screenshotone.com/take?access_key=IVmt2ghj9TG_jQ&block_ads=true&block_trackers=true&device_scale_factor=2&format=png&full_page=true&url=https%3A%2F%2Fscalabledeveloper.com&signature=85aabf7ac251563ec6158ef6839dd019bb79ce222cc85288a2e8cea0291a824e
```

Take a screenshot and save the image in the file:

```go
client, err := screenshots.NewClient("IVmt2ghj9TG_jQ", "Sxt94yAj9aQSgg")
if err != nil {
    // ...
}

options := screenshots.NewTakeOptions("https://example.com").
    Format("png").
    FullPage(true).
    DeviceScaleFactor(2).
    BlockAds(true).
    BlockTrackers(true)

image, err := client.Take(context.TODO(), options)
if err != nil {
    // ...
}

defer image.Close()
out, err := os.Create("example.png")
if err != nil {
    // ...
}

defer out.Close()
io.Copy(out, image)
```

Check out [other SDKs and code examples](/docs/code-examples/).