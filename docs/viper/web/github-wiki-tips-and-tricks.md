# Tips and tricks

Let's collect some more or less obvious tips here.

<details><summary>Customized unmarshaling</summary>
<p>

If you need to customize unmarshaling look at [mapstructure config options](https://godoc.org/github.com/mitchellh/mapstructure#DecoderConfig) and you can set it like that:

```go
// if you need error on unknown fields in your config file
viper.Unmarshal(&f.d, func(config *mapstructure.DecoderConfig) {                                                          
        config.ErrorUnused = true                                                                                                    
    })
```

</p>
</details>

<details><summary>Using go text templates</summary>
<p>

If you need to store go templates in viper configs and then execute them, look at [Viper Template](github.com/sv-tools/viper-templat) library.

Here is an example:

```go
package main

import (
	"fmt"
	"text/template"

	"github.com/spf13/viper"
	vipertemplate "github.com/sv-tools/viper-template"
)

func main() {
	v := viper.New()
	v.Set("foo", `{{ Get "bar" }}`)
	v.Set("bar", `{{ Mul . 2 }}`)

	type Data struct {
		Bar int
	}
	data := Data{
		Bar: 42,
	}

	funcs := template.FuncMap{
		"Mul": func(d *Data, v int) int {
			return d.Bar * v
		},
	}

	val, err := vipertemplate.Get(
		"foo",
		vipertemplate.WithViper(v),
		vipertemplate.WithData(&data),
		vipertemplate.WithFuncs(funcs),
	)
	if err != nil {
		panic(err)
	}

	fmt.Println(val)
	// Output: 84
}
```
</p>
</details>