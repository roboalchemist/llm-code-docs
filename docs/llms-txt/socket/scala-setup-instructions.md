# Source: https://docs.socket.dev/docs/scala-setup-instructions.md

# Scala setup instructions

Note: the following only applies to projects using `build.sbt`. If your project uses gradle, you should look at `socket cdxgen --help` or `socket manifest gradle --help`. If your project uses `pom.xml` files directly, you can skip generating the manifest file altogether because that's what `pom.xml` is.

## Generating manifest files with `sbt`

You can run `socket manifest scala` from your source dir. it will try to invoke `sbt` to generate `pom.xml` files for your project. Once generated these can be uploaded by running `socket scan create` in the same dir.

You can specify the input folder, the location of the `sbt` binary to use, and the output folder through the command flags. See `socket manifest scala --help` for details on this. You can also pass through additional options to `sbt`.

Once you have created the manifest(s) you can [create a report](https://docs.socket.dev/docs/socket-scan) by running `socket scan create`in the target dir.