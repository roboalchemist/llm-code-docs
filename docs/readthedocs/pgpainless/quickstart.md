# Quickstart Guide

In this guide, we will get you started with OpenPGP using PGPainless as quickly as possible.

At first though, you need to decide which API you want to use;

- 

PGPainless’ core API is powerful and heavily customizable

- 

The SOP API is a bit less powerful, but *dead* simple to use

The SOP API is the recommended way to go if you just want to get started already.

In case you need more technical documentation, Javadoc can be found in the following places:

- 

For the core API: pgpainless-core [https://javadoc.io/doc/org.pgpainless/pgpainless-core//index.html]

- 

For the SOP API: pgpainless-sop [https://javadoc.io/doc/org.pgpainless/pgpainless-sop//index.html]

## SOP API with pgpainless-sop

The Stateless OpenPGP Protocol (SOP) defines a simplistic interface for the most important OpenPGP operations.
It allows you to encrypt, decrypt, sign and verify messages, generate keys and add/remove ASCII armor from data.
However, it does not yet provide tools for key management.
Furthermore, the implementation is deciding for you, which (secure) algorithms to use, and it doesn’t let you
change those.

If you want to read more about the background of the SOP protocol, there is a whole chapter dedicated to it.

### Setup

PGPainless’ releases are published to and can be fetched from Maven Central.
To get started, you first need to include `pgpainless-sop` in your projects build script.

```
// If you use Gradle
...
dependencies {
    ...
    implementation "org.pgpainless:pgpainless-sop:XYZ"
    ...
}

// If you use Maven
...
<dependencies>
    ...
    <dependency>
        <groupId>org.pgpainless</groupId>
        <artifactId>pgpainless-sop</artifactId>
        <version>XYZ</version>
    </dependency>
    ...
</dependencies>

```