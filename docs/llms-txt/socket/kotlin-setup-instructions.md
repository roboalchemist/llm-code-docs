# Source: https://docs.socket.dev/docs/kotlin-setup-instructions.md

# Kotlin setup instructions

Since Kotlin uses gradle and gradle supports Kotlin by default, you can use the general gradle approach.

Note that the preferred way is to use CycloneDX through `socket cdxgen`. Alternatively you can try to use your local  [Gradle config](https://docs.socket.dev/docs/gradle-setup-instructions-for-java-kotlin-and-scala) through `socket manifest gradle` as a way to unblock. See `socket manifest gradle --help` for more information (or [this page](https://docs.socket.dev/docs/gradle-setup-instructions-for-java-kotlin-and-scala)).

After generating the manifest(s) you can [create a report](https://docs.socket.dev/docs/socket-scan) by running `socket scan create` in the same dir.