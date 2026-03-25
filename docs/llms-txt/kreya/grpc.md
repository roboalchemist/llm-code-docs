# Source: https://kreya.app/docs/operations/grpc.md

# Source: https://kreya.app/docs/importers/grpc.md

# gRPC

For gRPC, using importers is a must. Without importing the protobuf definitions, Kreya cannot know the available gRPC methods and the request/response types.

### Import via gRPC server reflection[​](#import-via-grpc-server-reflection "Direct link to Import via gRPC server reflection")

Some gRPC service support [server reflection](https://github.com/grpc/grpc/blob/master/doc/server-reflection.md). Kreya can fetch all information directly from the service itself. If the gRPC service does not have a valid TLS certificate, you can disable the TLS (SSL) validation (this can be dangerous and impact security). [TLS certificates](/docs/ssl-tls.md) for authentication purposes are also supported here.

![Adding a gRPC importer with server reflection](/assets/ideal-img/grpc-server-reflection-importer.5b44d22.400.png)

### Import via file descriptor sets[​](#import-via-file-descriptor-sets "Direct link to Import via file descriptor sets")

You can import your gRPC service and message definitions via proto file descriptor sets. These can be generated via `protoc` with the `--include_imports --include_source_info --descriptor_set_out` flags or via `buf` (read more about it [here](https://docs.buf.build/reference/images/#how-do-i-create-filedescriptorsets-with-protoc)). Using file descriptor sets has the advantage that Kreya does not have to parse the protobuf files which will result in faster imports.

![Adding a gRPC importer with file descriptor sets](/assets/ideal-img/grpc-file-descriptor-set-importer.91a1457.400.png)

*Kreya only stores the path to the file descriptor set files. If you intend to share your Kreya project, make sure that the paths stay correct. Kreya uses relative paths by default, but you may also use system environment variables like `%APPDATA%` or `${GOPATH}`. They will work on any OS, regardless of the format.*

### Import via local protobuf files[​](#import-via-local-protobuf-files "Direct link to Import via local protobuf files")

You can add local protobuf files. Simply change the importer type to `gRPC proto files` and add your files.

If you have a complex directory structure with many files, use the `Add proto directories` button. All protobuf files found inside the chosen directory and subdirectories are automatically imported.

![Adding a gRPC importer with local protobuf files](/assets/ideal-img/proto-files-importer.c62013b.400.png)

*Kreya only stores the path to the protobuf files. If you intend to share your Kreya project, make sure that the paths stay correct. Kreya uses relative paths by default, but you may also use system environment variables like `%APPDATA%` or `${GOPATH}`. They will work on any OS, regardless of the format.*

#### Import paths[​](#import-paths "Direct link to Import paths")

Protobuf files may import other protobuf files via relative paths. Consider the following example:

```
/src
  /todo
    todo.proto
  /list
    todo-list.proto (imports todo/todo.proto)
```

Here, the `/src` directory needs to be added as an import path, so that the relative path in `todo-list.proto` points to the correct file.

Kreya tries to guess the correct import paths. However, if you have a complex setup with multiple import paths, you may need to specify them manually.
