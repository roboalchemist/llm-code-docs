# Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/

Title: gRPC-Gateway v2 migration guide

URL Source: https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/

Markdown Content:
This guide is supposed to help users of the gateway migrate from v1 to v2. See [the original issue](https://github.com/grpc-ecosystem/grpc-gateway/issues/1223) for detailed information on all changes that were made specifically to v2.

The following behavioural defaults have been changed:

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#protoc-gen-swagger-has-been-renamed-protoc-gen-openapiv2) protoc-gen-swagger has been renamed protoc-gen-openapiv2
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See [the original issue](https://github.com/grpc-ecosystem/grpc-gateway/issues/675) for more information. Apart from the new name, the only real difference to users will be a slightly different proto annotation:

```
import "protoc-gen-openapiv2/options/annotations.proto";
```

instead of

```
import "protoc-gen-swagger/options/annotations.proto";
```

and

```
option (grpc.gateway.protoc_gen_openapiv2.options.openapiv2_swagger) = {
```

instead of

```
option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
```

The Bazel rule has been renamed `protoc_gen_openapiv2`.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#the-example-field-in-the-openapi-annotations-is-now-a-string) The example field in the OpenAPI annotations is now a string
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This was a `google.protobuf.Any` type, but it was only used for the JSON representation, and it was breaking some tools and it was generally unclear to the user how it works. It is now a string instead. The value is copied verbatim to the output OpenAPI file. Remember to escape any quotes in the strings.

For example, if you had an example that looked like this:

```
example: { value: '{ "uuid": "0cf361e1-4b44-483d-a159-54dabdf7e814" }' }
```

It would now look like this:

```
example: "{\"uuid\": \"0cf361e1-4b44-483d-a159-54dabdf7e814\"}"
```

See [a_bit_of_everything.proto](https://github.com/grpc-ecosystem/grpc-gateway/blob/main/examples/internal/proto/examplepb/a_bit_of_everything.proto) in the example protos for more examples.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#we-now-use-the-camelcase-json-names-by-default) We now use the camelCase JSON names by default
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See [the original issue](https://github.com/grpc-ecosystem/grpc-gateway/issues/375) and [original pull request](https://github.com/grpc-ecosystem/grpc-gateway/pull/540) for more information.

If you want to revert to the old behaviour, configure a custom marshaler with `UseProtoNames: true`:

```
mux := runtime.NewServeMux(
	runtime.WithMarshalerOption(runtime.MIMEWildcard, &runtime.HTTPBodyMarshaler{
		Marshaler: &runtime.JSONPb{
			MarshalOptions: protojson.MarshalOptions{
				UseProtoNames:   true,
				EmitUnpopulated: true,
			},
			UnmarshalOptions: protojson.UnmarshalOptions{
				DiscardUnknown: true,
			},
		},
	}),
)
```

To change the OpenAPI generator behaviour to match, set `json_names_for_fields=false` when generating:

```
--openapiv2_out=json_names_for_fields=false:./gen/openapiv2 path/to/my/proto/v1/myproto.proto
```

If using the Bazel rule, set `json_names_for_fields=False`.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#we-now-emit-default-values-for-all-fields) We now emit default values for all fields
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See [the original issue](https://github.com/grpc-ecosystem/grpc-gateway/issues/233) for more information.

If you want to revert to the old behaviour, configure a custom marshaler with `EmitUnpopulated: false`:

```
mux := runtime.NewServeMux(
	runtime.WithMarshalerOption(runtime.MIMEWildcard, &runtime.HTTPBodyMarshaler{
		Marshaler: &runtime.JSONPb{
			MarshalOptions: protojson.MarshalOptions{
				EmitUnpopulated: false,
			},
			UnmarshalOptions: protojson.UnmarshalOptions{
				DiscardUnknown: true,
			},
		},
	}),
)
```

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#we-now-support-googleapihttpbody-message-types-by-default) We now support google.api.HttpBody message types by default
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `runtime.SetHTTPBodyMarshaler` function has disappeared, and is now enabled by default. If you for some reason don’t want `HttpBody` messages to be respected, you can disable it by overwriting the default marshaler with one which does not wrap `runtime.JSONPb` in `runtime.HTTPBodyMarshaler`:

```
mux := runtime.NewServeMux(
	runtime.WithMarshalerOption(runtime.MIMEWildcard, &runtime.JSONPb{
		MarshalOptions: protojson.MarshalOptions{
			EmitUnpopulated: true,
		},
		UnmarshalOptions: protojson.UnmarshalOptions{
			DiscardUnknown: true,
		},
	}),
)
```

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#runtimedisallowunknownfields-has-been-removed) runtime.DisallowUnknownFields has been removed
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All marshalling settings are now inherited from the configured marshaler. If you wish to disallow unknown fields, configure a custom marshaler:

```
mux := runtime.NewServeMux(
	runtime.WithMarshalerOption(runtime.MIMEWildcard, &runtime.HTTPBodyMarshaler{
		Marshaler: &runtime.JSONPb{
			MarshalOptions: protojson.MarshalOptions{
				EmitUnpopulated: true,
			},
			UnmarshalOptions: protojson.UnmarshalOptions{
				DiscardUnknown: false,
			},
		},
	}),
)
```

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#withlastmatchwins-and-allow_colon_final_segmentstrue-is-now-default-behaviour) WithLastMatchWins and allow_colon_final_segments=true is now default behaviour
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you were previously specifying these, please remove them, as this is now the default behaviour. See [the original issue](https://github.com/grpc-ecosystem/grpc-gateway/issues/224) for more information.

There is no workaround for this, as we considered it a correct interpretation of the spec. If this breaks your application, carefully consider the order in which you define your services.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#error-handling-configuration-has-been-overhauled) Error handling configuration has been overhauled
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`runtime.HTTPError`, `runtime.OtherErrorHandler`, `runtime.GlobalHTTPErrorHandler`, `runtime.WithProtoErrorHandler` are all gone. Error handling is rewritten around the use of gRPCs Status types. If you wish to configure how the gateway handles errors, please use `runtime.WithErrorHandler` and `runtime.WithStreamErrorHandler`. To handle routing errors (similar to the removed `runtime.OtherErrorHandler`) please use `runtime.WithRoutingErrorHandler`.

[](https://grpc-ecosystem.github.io/grpc-gateway/docs/development/grpc-gateway_v2_migration_guide/#default-query-parameter-parsing-behaviour-change) Default query parameter parsing behaviour change
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default behaviour for query parameter parsing has changed to return an `InvalidArgument` (`400 Bad Request`) error when more than one of the same matching query parameters is parsed. Previously, it would log but not return an error, using the first query parameter that matched and ignoring any others. See [the original issue](https://github.com/grpc-ecosystem/grpc-gateway/issues/2632) for more information.

* * *
