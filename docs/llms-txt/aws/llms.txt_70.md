# Source: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/llms.txt

# Amazon S3 Encryption Client Developer Guide

> Learn how to use the Amazon S3 Encryption Client to protect your Amazon Simple Storage Service objects.

- [Supported encryption algorithms](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/encryption-algorithms.html)
- [Document history](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/doc-history.html)

## [What is the Amazon S3 Encryption Client?](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/what-is-s3-encryption-client.html)

- [Terms and concepts](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/concepts.html): Understand the concepts used in the Amazon S3 Encryption Client.
- [How it works](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/how-it-works.html)
- [Client-side and server-side encryption](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/client-server-side.html)


## [Programming languages](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/programming-languages.html)

### [Java](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java.html)

- [Examples](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java-examples.html): The following examples show you how to use the Amazon S3 Encryption Client for Java to encrypt and decrypt Amazon S3 objects.
- [Asynchronous programming](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/using-s3ec-async.html): Version 3.x and later of the Amazon S3 Encryption Client provides a nonblocking asynchronous client that implements high concurrency across a few threads.
- [Migrate to version 4.x](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java-v4-migration.html): Version 4.x of the Amazon S3 Encryption Client introduces AES GCM with Key Commitment (ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY) and Commitment Policies to enhance security by protecting against data key tampering in Instruction Files.
- [Migrate from version 2.x to 3.x](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java-v3-migration.html)

### [Go](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go.html)

- [Examples](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go-examples.html): Learn how to use the Amazon S3 Encryption Client for Go to encrypt and decrypt Amazon S3 objects.
- [Migrate from 3.x to 4.x](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go-v4-migration.html): Learn how to migrate your Amazon S3 Encryption Client for Go from version 3.x to version 4.x, which introduces AES GCM with Key Commitment and Commitment Policies for enhanced security.
- [Migrate from 2.x to 3.x](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go-v3-migration.html): Note: If you're using version 3.x of the Amazon S3 Encryption Client for Go and want to migrate to version 4.x, see .
