# Source: https://juno.build/docs/reference/functions/typescript/ic-cdk.md

# Source: https://juno.build/docs/reference/functions/rust/ic-cdk.md

# IC-CDK

The [Canister Development Kit](https://github.com/dfinity/cdk-rs) (`ic-cdk` or `ic_cdk`) provides core functionality for interacting with the Internet Computer in Rust.

In the context of Juno, it enables your Satellite to perform low-level operations such as logging, accessing your Satellite identities, or communicating with other canisters â all essential when writing advanced serverless functions.

**All features** of the IC CDK are supported in Juno Satellites.

Because of this compatibility, we do not list them individually here and encourage you to consult the official documentation instead.

ð¦ See full documentation on [docs.rs/ic-cdk](https://docs.rs/ic-cdk/latest/ic_cdk/)

**Note:**

For compatibility, always use the `ic_cdk` version specified in Junoâs release notes. This ensures proper integration and avoids version mismatch issues.