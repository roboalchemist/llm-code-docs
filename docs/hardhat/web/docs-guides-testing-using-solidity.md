# Source: https://hardhat.org/docs/guides/testing/using-solidity

Title: Writing unit tests in Solidity

URL Source: https://hardhat.org/docs/guides/testing/using-solidity

Markdown Content:
Writing unit tests in Solidity | Hardhat 3
===============
[Skip to content](https://hardhat.org/docs/guides/testing/using-solidity#_top)

### Cookie Policy

We use cookies to improve your experience on our website. [Read More](https://hardhat.org/privacy-policy.html)

Reject all Accept all

[![Image 1](https://hardhat.org/_astro/hardhat-logo-dark.Cci7oQuI.svg)![Image 2](https://hardhat.org/_astro/hardhat-logo-light.dg4Licbx.svg) Hardhat 3](https://hardhat.org/)

Search Ctrl K

 Cancel 

[GitHub](https://github.com/NomicFoundation/hardhat)[X](https://x.com/HardhatHQ)[Discord](https://hardhat.org/discord)

Select theme 

Hardhat 3

[Hardhat 3](https://hardhat.org/docs/getting-started)[Hardhat Ignition](https://hardhat.org/ignition/docs)[Migrate from Hardhat 2](https://hardhat.org/docs/migrate-from-hardhat2)[Plugin development](https://hardhat.org/docs/plugin-development)

*   [Getting started](https://hardhat.org/docs/getting-started)
*   
Hardhat 3
    *   [What's new in Hardhat 3](https://hardhat.org/docs/hardhat3/whats-new)
    *   [Beta status](https://hardhat.org/docs/hardhat3/beta-status)
    *   [Migrate to Hardhat 3](https://hardhat.org/docs/hardhat3/migration)

*   
Tutorial
    *   [Introduction](https://hardhat.org/docs/tutorial)
    *   [Setting up a Hardhat project](https://hardhat.org/docs/tutorial/setup)
    *   [Writing and testing a Solidity contract](https://hardhat.org/docs/tutorial/writing-and-testing)
    *   [Using an assertions library](https://hardhat.org/docs/tutorial/assertions-library)
    *   [Writing fuzz tests in Solidity](https://hardhat.org/docs/tutorial/fuzz-tests)
    *   [Using a Hardhat plugin](https://hardhat.org/docs/tutorial/plugins)
    *   [Writing TypeScript tests](https://hardhat.org/docs/tutorial/typescript-tests)
    *   [Measuring test coverage](https://hardhat.org/docs/tutorial/coverage)
    *   [Deploying a contract](https://hardhat.org/docs/tutorial/deploying)
    *   [Using Configuration Variables](https://hardhat.org/docs/tutorial/configuration-variables)
    *   [Verifying a contract](https://hardhat.org/docs/tutorial/verifying)
    *   [Learn more](https://hardhat.org/docs/tutorial/learn-more)

*   
Guides
    *   
Writing Smart contracts
        *   [Writing contracts overview](https://hardhat.org/docs/guides/writing-contracts)
        *   [Managing dependencies](https://hardhat.org/docs/guides/writing-contracts/dependencies)
        *   [Using remappings](https://hardhat.org/docs/guides/writing-contracts/remappings)
        *   [Configuring the compiler](https://hardhat.org/docs/guides/writing-contracts/configuring-the-compiler)
        *   [Isolated builds](https://hardhat.org/docs/guides/writing-contracts/isolated-builds)
        *   [Build profiles](https://hardhat.org/docs/guides/writing-contracts/build-profiles)

    *   
Testing Smart contracts
        *   [Testing overview](https://hardhat.org/docs/guides/testing)
        *   [Using Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity)
        *   [Using TypeScript & viem](https://hardhat.org/docs/guides/testing/using-viem)
        *   [Using TypeScript & ethers.js](https://hardhat.org/docs/guides/testing/using-ethers)
        *   [Code coverage](https://hardhat.org/docs/guides/testing/code-coverage)
        *   [Gas statistics for your test runs](https://hardhat.org/docs/guides/testing/gas-statistics)
        *   [Gas snapshots](https://hardhat.org/docs/guides/testing/gas-snapshots)

    *   
Deploying Smart contracts
        *   [Deployment overview](https://hardhat.org/docs/guides/deployment)
        *   [Using Hardhat Ignition](https://hardhat.org/docs/guides/deployment/using-ignition)
        *   [Using scripts](https://hardhat.org/docs/guides/deployment/using-scripts)

    *   [Verifying contracts](https://hardhat.org/docs/guides/smart-contract-verification)
    *   [Managing config values and secrets](https://hardhat.org/docs/guides/configuration-variables)
    *   [Writing Hardhat tasks](https://hardhat.org/docs/guides/writing-tasks)
    *   [Writing scripts with Hardhat](https://hardhat.org/docs/guides/writing-scripts)
    *   [Forking a network](https://hardhat.org/docs/guides/forking)
    *   [Running a local development node](https://hardhat.org/docs/guides/hardhat-node)
    *   [Using the Hardhat console](https://hardhat.org/docs/guides/hardhat-console)
    *   [Getting help](https://hardhat.org/docs/guides/getting-help)

*   
Cookbook
    *   [Cookbook overview](https://hardhat.org/docs/cookbook)
    *   [Using an HTTP proxy](https://hardhat.org/docs/cookbook/http-proxies)
    *   [Using multiple Solidity versions](https://hardhat.org/docs/cookbook/multiple-solidity-versions)
    *   [Generating artifacts from npm dependencies](https://hardhat.org/docs/cookbook/npm-artifacts)
    *   [Using absolute imports in Solidity](https://hardhat.org/docs/cookbook/absolute-imports)
    *   [Using a custom Solidity compiler](https://hardhat.org/docs/cookbook/custom-solidity-compiler)
    *   [Running Hardhat with debug logs](https://hardhat.org/docs/cookbook/debug-logs)
    *   [Creating a Hardhat Runtime Environment programmatically](https://hardhat.org/docs/cookbook/programmatic-hre)

*   
Reference
    *   [Configuration](https://hardhat.org/docs/reference/configuration)
    *   [Network Manager](https://hardhat.org/docs/reference/network-manager)
    *   [Simulated Networks](https://hardhat.org/docs/reference/edr-simulated-networks)
    *   [JSON-RPC Methods](https://hardhat.org/docs/reference/json-rpc-methods)
    *   [Build artifacts](https://hardhat.org/docs/reference/artifacts)
    *   [Solidity console.log](https://hardhat.org/docs/reference/console-log)
    *   [Foundry compatibility](https://hardhat.org/docs/reference/foundry-compatibility)
    *   
Solidity test cheatcodes
        *   [Cheatcodes overview](https://hardhat.org/docs/reference/cheatcodes/cheatcodes-overview)
        *   
Assertions
            *   [Asserts](https://hardhat.org/docs/reference/cheatcodes/assertions/asserts)
            *   [expectCall](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-call)
            *   [expectCallMinGas](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-call-min-gas)
            *   [expectCreate](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-create)
            *   [expectCreate2](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-create2)
            *   [expectEmit](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-emit)
            *   [expectEmitAnonymous](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-emit-anonymous)
            *   [expectRevert](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-revert)
            *   [expectSafeMemory](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-safe-memory)
            *   [expectSafeMemoryCall](https://hardhat.org/docs/reference/cheatcodes/assertions/expect-safe-memory-call)

        *   
Environment
            *   [accessList](https://hardhat.org/docs/reference/cheatcodes/environment/access-list)
            *   [accesses](https://hardhat.org/docs/reference/cheatcodes/environment/accesses)
            *   [blobBaseFee](https://hardhat.org/docs/reference/cheatcodes/environment/blob-base-fee)
            *   [blobhashes](https://hardhat.org/docs/reference/cheatcodes/environment/blobhashes)
            *   [chainId](https://hardhat.org/docs/reference/cheatcodes/environment/chain-id)
            *   [clearMockedCalls](https://hardhat.org/docs/reference/cheatcodes/environment/clear-mocked-calls)
            *   [cloneAccount](https://hardhat.org/docs/reference/cheatcodes/environment/clone-account)
            *   [coinbase](https://hardhat.org/docs/reference/cheatcodes/environment/coinbase)
            *   [cool](https://hardhat.org/docs/reference/cheatcodes/environment/cool)
            *   [coolSlot](https://hardhat.org/docs/reference/cheatcodes/environment/cool-slot)
            *   [deal](https://hardhat.org/docs/reference/cheatcodes/environment/deal)
            *   [difficulty](https://hardhat.org/docs/reference/cheatcodes/environment/difficulty)
            *   [envExists](https://hardhat.org/docs/reference/cheatcodes/environment/env-exists)
            *   [etch](https://hardhat.org/docs/reference/cheatcodes/environment/etch)
            *   [fee](https://hardhat.org/docs/reference/cheatcodes/environment/fee)
            *   [snapshotGas cheatcodes](https://hardhat.org/docs/reference/cheatcodes/environment/gas-snapshots)
            *   [getBlobBaseFee](https://hardhat.org/docs/reference/cheatcodes/environment/get-blob-base-fee)
            *   [getBlobhashes](https://hardhat.org/docs/reference/cheatcodes/environment/get-blobhashes)
            *   [getBlockNumber](https://hardhat.org/docs/reference/cheatcodes/environment/get-block-number)
            *   [getBlockTimestamp](https://hardhat.org/docs/reference/cheatcodes/environment/get-block-timestamp)
            *   [getChain](https://hardhat.org/docs/reference/cheatcodes/environment/get-chain)
            *   [getLabel](https://hardhat.org/docs/reference/cheatcodes/environment/get-label)
            *   [getMappingKeyAndParentOf](https://hardhat.org/docs/reference/cheatcodes/environment/get-mapping-key-and-parent-of)
            *   [getMappingLength](https://hardhat.org/docs/reference/cheatcodes/environment/get-mapping-length)
            *   [getMappingSlotAt](https://hardhat.org/docs/reference/cheatcodes/environment/get-mapping-slot-at)
            *   [getNonce](https://hardhat.org/docs/reference/cheatcodes/environment/get-nonce)
            *   [getRawBlockHeader](https://hardhat.org/docs/reference/cheatcodes/environment/get-raw-block-header)
            *   [getRecordedLogs](https://hardhat.org/docs/reference/cheatcodes/environment/get-recorded-logs)
            *   [getStateDiff](https://hardhat.org/docs/reference/cheatcodes/environment/get-state-diff)
            *   [getStateDiffJson](https://hardhat.org/docs/reference/cheatcodes/environment/get-state-diff-json)
            *   [interceptInitcode](https://hardhat.org/docs/reference/cheatcodes/environment/intercept-initcode)
            *   [isContext](https://hardhat.org/docs/reference/cheatcodes/environment/is-context)
            *   [lastCallGas](https://hardhat.org/docs/reference/cheatcodes/environment/last-call-gas)
            *   [load](https://hardhat.org/docs/reference/cheatcodes/environment/load)
            *   [loadAllocs](https://hardhat.org/docs/reference/cheatcodes/environment/load-allocs)
            *   [mockCall](https://hardhat.org/docs/reference/cheatcodes/environment/mock-call)
            *   [mockCallRevert](https://hardhat.org/docs/reference/cheatcodes/environment/mock-call-revert)
            *   [mockCalls](https://hardhat.org/docs/reference/cheatcodes/environment/mock-calls)
            *   [mockFunction](https://hardhat.org/docs/reference/cheatcodes/environment/mock-function)
            *   [noAccessList](https://hardhat.org/docs/reference/cheatcodes/environment/no-access-list)
            *   [pauseGasMetering](https://hardhat.org/docs/reference/cheatcodes/environment/pause-gas-metering)
            *   [pauseTracing](https://hardhat.org/docs/reference/cheatcodes/environment/pause-tracing)
            *   [prank](https://hardhat.org/docs/reference/cheatcodes/environment/prank)
            *   [prevrandao](https://hardhat.org/docs/reference/cheatcodes/environment/prevrandao)
            *   [readCallers](https://hardhat.org/docs/reference/cheatcodes/environment/read-callers)
            *   [record](https://hardhat.org/docs/reference/cheatcodes/environment/record)
            *   [recordLogs](https://hardhat.org/docs/reference/cheatcodes/environment/record-logs)
            *   [resetGasMetering](https://hardhat.org/docs/reference/cheatcodes/environment/reset-gas-metering)
            *   [resetNonce](https://hardhat.org/docs/reference/cheatcodes/environment/reset-nonce)
            *   [resumeGasMetering](https://hardhat.org/docs/reference/cheatcodes/environment/resume-gas-metering)
            *   [resumeTracing](https://hardhat.org/docs/reference/cheatcodes/environment/resume-tracing)
            *   [roll](https://hardhat.org/docs/reference/cheatcodes/environment/roll)
            *   [setBlockhash](https://hardhat.org/docs/reference/cheatcodes/environment/set-blockhash)
            *   [setNonce](https://hardhat.org/docs/reference/cheatcodes/environment/set-nonce)
            *   [setNonceUnsafe](https://hardhat.org/docs/reference/cheatcodes/environment/set-nonce-unsafe)
            *   [setSeed](https://hardhat.org/docs/reference/cheatcodes/environment/set-seed)
            *   [startDebugTraceRecording](https://hardhat.org/docs/reference/cheatcodes/environment/start-debug-trace-recording)
            *   [startMappingRecording](https://hardhat.org/docs/reference/cheatcodes/environment/start-mapping-recording)
            *   [startPrank](https://hardhat.org/docs/reference/cheatcodes/environment/start-prank)
            *   [startStateDiffRecording](https://hardhat.org/docs/reference/cheatcodes/environment/start-state-diff-recording)
            *   [stopAndReturnDebugTraceRecording](https://hardhat.org/docs/reference/cheatcodes/environment/stop-and-return-debug-trace-recording)
            *   [stopAndReturnStateDiff](https://hardhat.org/docs/reference/cheatcodes/environment/stop-and-return-state-diff)
            *   [stopExpectSafeMemory](https://hardhat.org/docs/reference/cheatcodes/environment/stop-expect-safe-memory)
            *   [stopMappingRecording](https://hardhat.org/docs/reference/cheatcodes/environment/stop-mapping-recording)
            *   [stopPrank](https://hardhat.org/docs/reference/cheatcodes/environment/stop-prank)
            *   [stopRecord](https://hardhat.org/docs/reference/cheatcodes/environment/stop-record)
            *   [store](https://hardhat.org/docs/reference/cheatcodes/environment/store)
            *   [txGasPrice](https://hardhat.org/docs/reference/cheatcodes/environment/tx-gas-price)
            *   [warmSlot](https://hardhat.org/docs/reference/cheatcodes/environment/warm-slot)
            *   [warp](https://hardhat.org/docs/reference/cheatcodes/environment/warp)

        *   
External
            *   [envAddress](https://hardhat.org/docs/reference/cheatcodes/external/env-address)
            *   [envBool](https://hardhat.org/docs/reference/cheatcodes/external/env-bool)
            *   [envBytes](https://hardhat.org/docs/reference/cheatcodes/external/env-bytes)
            *   [envBytes32](https://hardhat.org/docs/reference/cheatcodes/external/env-bytes32)
            *   [envInt](https://hardhat.org/docs/reference/cheatcodes/external/env-int)
            *   [envOr](https://hardhat.org/docs/reference/cheatcodes/external/env-or)
            *   [envString](https://hardhat.org/docs/reference/cheatcodes/external/env-string)
            *   [envUint](https://hardhat.org/docs/reference/cheatcodes/external/env-uint)
            *   [ffi](https://hardhat.org/docs/reference/cheatcodes/external/ffi)
            *   [getCode](https://hardhat.org/docs/reference/cheatcodes/external/get-code)
            *   [getDeployedCode](https://hardhat.org/docs/reference/cheatcodes/external/get-deployed-code)
            *   [keyExists](https://hardhat.org/docs/reference/cheatcodes/external/key-exists)
            *   [keyExistsJson](https://hardhat.org/docs/reference/cheatcodes/external/key-exists-json)
            *   [keyExistsToml](https://hardhat.org/docs/reference/cheatcodes/external/key-exists-toml)
            *   [parseJson](https://hardhat.org/docs/reference/cheatcodes/external/parse-json)
            *   [parseJsonAddress](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-address)
            *   [parseJsonAddressArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-address-array)
            *   [parseJsonBool](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-bool)
            *   [parseJsonBoolArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-bool-array)
            *   [parseJsonBytes](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-bytes)
            *   [parseJsonBytesArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-bytes-array)
            *   [parseJsonBytes32](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-bytes32)
            *   [parseJsonBytes32Array](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-bytes32-array)
            *   [parseJsonInt](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-int)
            *   [parseJsonIntArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-int-array)
            *   [parseJsonKeys](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-keys)
            *   [parseJsonString](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-string)
            *   [parseJsonStringArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-string-array)
            *   [parseJsonType](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-type)
            *   [parseJsonTypeArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-type-array)
            *   [parseJsonUint](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-uint)
            *   [parseJsonUintArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-json-uint-array)
            *   [parseToml](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml)
            *   [parseTomlAddress](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-address)
            *   [parseTomlAddressArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-address-array)
            *   [parseTomlBool](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-bool)
            *   [parseTomlBoolArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-bool-array)
            *   [parseTomlBytes](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-bytes)
            *   [parseTomlBytesArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-bytes-array)
            *   [parseTomlBytes32](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-bytes32)
            *   [parseTomlBytes32Array](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-bytes32-array)
            *   [parseTomlInt](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-int)
            *   [parseTomlIntArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-int-array)
            *   [parseTomlKeys](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-keys)
            *   [parseTomlString](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-string)
            *   [parseTomlStringArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-string-array)
            *   [parseTomlType](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-type)
            *   [parseTomlTypeArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-type-array)
            *   [parseTomlUint](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-uint)
            *   [parseTomlUintArray](https://hardhat.org/docs/reference/cheatcodes/external/parse-toml-uint-array)
            *   [projectRoot](https://hardhat.org/docs/reference/cheatcodes/external/project-root)
            *   [prompt](https://hardhat.org/docs/reference/cheatcodes/external/prompt)
            *   [serializeJson](https://hardhat.org/docs/reference/cheatcodes/external/serialize-json)
            *   [setEnv](https://hardhat.org/docs/reference/cheatcodes/external/set-env)
            *   [sleep](https://hardhat.org/docs/reference/cheatcodes/external/sleep)
            *   [unixTime](https://hardhat.org/docs/reference/cheatcodes/external/unix-time)
            *   [writeJson](https://hardhat.org/docs/reference/cheatcodes/external/write-json)
            *   [writeToml](https://hardhat.org/docs/reference/cheatcodes/external/write-toml)

        *   
File
            *   [File cheatcodes](https://hardhat.org/docs/reference/cheatcodes/file/fs)
            *   [fsMetadata](https://hardhat.org/docs/reference/cheatcodes/file/fs-metadata)

        *   
Forking
            *   [activeFork](https://hardhat.org/docs/reference/cheatcodes/forking/active-fork)
            *   [allowCheatcodes](https://hardhat.org/docs/reference/cheatcodes/forking/allow-cheatcodes)
            *   [createFork](https://hardhat.org/docs/reference/cheatcodes/forking/create-fork)
            *   [createSelectFork](https://hardhat.org/docs/reference/cheatcodes/forking/create-select-fork)
            *   [isPersistent](https://hardhat.org/docs/reference/cheatcodes/forking/is-persistent)
            *   [makePersistent](https://hardhat.org/docs/reference/cheatcodes/forking/make-persistent)
            *   [revokePersistent](https://hardhat.org/docs/reference/cheatcodes/forking/revoke-persistent)
            *   [rollFork](https://hardhat.org/docs/reference/cheatcodes/forking/roll-fork)
            *   [selectFork](https://hardhat.org/docs/reference/cheatcodes/forking/select-fork)
            *   [transact](https://hardhat.org/docs/reference/cheatcodes/forking/transact)

        *   
Fuzzer
            *   [assume](https://hardhat.org/docs/reference/cheatcodes/fuzzer/assume)
            *   [assumeNoRevert](https://hardhat.org/docs/reference/cheatcodes/fuzzer/assume-no-revert)

        *   
RPC
            *   [RPC related cheatcodes](https://hardhat.org/docs/reference/cheatcodes/rpc/rpc)

        *   
Signing
            *   [sign](https://hardhat.org/docs/reference/cheatcodes/signing/sign)
            *   [signCompact](https://hardhat.org/docs/reference/cheatcodes/signing/sign-compact)
            *   [signP256](https://hardhat.org/docs/reference/cheatcodes/signing/sign-p256)

        *   
State-snapshots
            *   [deleteSnapshot](https://hardhat.org/docs/reference/cheatcodes/state-snapshots/delete-snapshot)
            *   [deleteSnapshots](https://hardhat.org/docs/reference/cheatcodes/state-snapshots/delete-snapshots)
            *   [revertTo](https://hardhat.org/docs/reference/cheatcodes/state-snapshots/revert-to)
            *   [revertToAndDelete](https://hardhat.org/docs/reference/cheatcodes/state-snapshots/revert-to-and-delete)
            *   [snapshot](https://hardhat.org/docs/reference/cheatcodes/state-snapshots/snapshot)
            *   [snapshotState cheatcodes](https://hardhat.org/docs/reference/cheatcodes/state-snapshots/state-snapshots)

        *   
Utilities
            *   [addr](https://hardhat.org/docs/reference/cheatcodes/utilities/addr)
            *   [computeCreateAddress](https://hardhat.org/docs/reference/cheatcodes/utilities/compute-create-address)
            *   [computeCreate2Address](https://hardhat.org/docs/reference/cheatcodes/utilities/compute-create2-address)
            *   [contains](https://hardhat.org/docs/reference/cheatcodes/utilities/contains)
            *   [copyStorage](https://hardhat.org/docs/reference/cheatcodes/utilities/copy-storage)
            *   [dumpState](https://hardhat.org/docs/reference/cheatcodes/utilities/dump-state)
            *   [ensNamehash](https://hardhat.org/docs/reference/cheatcodes/utilities/ens-namehash)
            *   [eth_getLogs](https://hardhat.org/docs/reference/cheatcodes/utilities/eth-get-logs)
            *   [indexOf](https://hardhat.org/docs/reference/cheatcodes/utilities/index-of)
            *   [label](https://hardhat.org/docs/reference/cheatcodes/utilities/label)
            *   [parseAddress](https://hardhat.org/docs/reference/cheatcodes/utilities/parse-address)
            *   [parseBool](https://hardhat.org/docs/reference/cheatcodes/utilities/parse-bool)
            *   [parseBytes](https://hardhat.org/docs/reference/cheatcodes/utilities/parse-bytes)
            *   [parseBytes32](https://hardhat.org/docs/reference/cheatcodes/utilities/parse-bytes32)
            *   [parseInt](https://hardhat.org/docs/reference/cheatcodes/utilities/parse-int)
            *   [parseUint](https://hardhat.org/docs/reference/cheatcodes/utilities/parse-uint)
            *   [promptAddress](https://hardhat.org/docs/reference/cheatcodes/utilities/prompt-address)
            *   [promptSecret](https://hardhat.org/docs/reference/cheatcodes/utilities/prompt-secret)
            *   [promptSecretUint](https://hardhat.org/docs/reference/cheatcodes/utilities/prompt-secret-uint)
            *   [promptUint](https://hardhat.org/docs/reference/cheatcodes/utilities/prompt-uint)
            *   [publicKeyP256](https://hardhat.org/docs/reference/cheatcodes/utilities/public-key-p256)
            *   [randomAddress](https://hardhat.org/docs/reference/cheatcodes/utilities/random-address)
            *   [randomBytes](https://hardhat.org/docs/reference/cheatcodes/utilities/random-bytes)
            *   [randomBytes4](https://hardhat.org/docs/reference/cheatcodes/utilities/random-bytes4)
            *   [randomBytes8](https://hardhat.org/docs/reference/cheatcodes/utilities/random-bytes8)
            *   [randomInt](https://hardhat.org/docs/reference/cheatcodes/utilities/random-int)
            *   [randomUint](https://hardhat.org/docs/reference/cheatcodes/utilities/random-uint)
            *   [replace](https://hardhat.org/docs/reference/cheatcodes/utilities/replace)
            *   [serializeJsonType](https://hardhat.org/docs/reference/cheatcodes/utilities/serialize-json-type)
            *   [serializeUintToHex](https://hardhat.org/docs/reference/cheatcodes/utilities/serialize-uint-to-hex)
            *   [setArbitraryStorage](https://hardhat.org/docs/reference/cheatcodes/utilities/set-arbitrary-storage)
            *   [shuffle](https://hardhat.org/docs/reference/cheatcodes/utilities/shuffle)
            *   [skip](https://hardhat.org/docs/reference/cheatcodes/utilities/skip)
            *   [sort](https://hardhat.org/docs/reference/cheatcodes/utilities/sort)
            *   [split](https://hardhat.org/docs/reference/cheatcodes/utilities/split)
            *   [toBase64](https://hardhat.org/docs/reference/cheatcodes/utilities/to-base64)
            *   [toBase64URL](https://hardhat.org/docs/reference/cheatcodes/utilities/to-base64-url)
            *   [toLowercase](https://hardhat.org/docs/reference/cheatcodes/utilities/to-lowercase)
            *   [toString](https://hardhat.org/docs/reference/cheatcodes/utilities/to-string)
            *   [toUppercase](https://hardhat.org/docs/reference/cheatcodes/utilities/to-uppercase)
            *   [trim](https://hardhat.org/docs/reference/cheatcodes/utilities/trim)
            *   [tryFfi](https://hardhat.org/docs/reference/cheatcodes/utilities/try-ffi)

    *   [Stability guarantees](https://hardhat.org/docs/reference/stability-guarantees)
    *   [Node.js support](https://hardhat.org/docs/reference/nodejs-support)
    *   [Hardhat 3 errors](https://hardhat.org/docs/reference/errors)

*   
Explanations
    *   [Hardhat 3 projects](https://hardhat.org/docs/explanations/hardhat-projects)
    *   [The Hardhat Runtime Environment](https://hardhat.org/docs/explanations/hardhat-runtime-environment)
    *   [Multichain support](https://hardhat.org/docs/explanations/multichain-support)
    *   [Network Management](https://hardhat.org/docs/explanations/network-management)
    *   [Simulated Networks](https://hardhat.org/docs/explanations/edr-simulated-networks)
    *   [Configuration Variables](https://hardhat.org/docs/explanations/configuration-variables)
    *   [Global Options](https://hardhat.org/docs/explanations/global-options)

*   
Plugins
    *   [Official plugins](https://hardhat.org/docs/plugins/official-plugins)
    *   [Community plugins](https://hardhat.org/docs/plugins/community-plugins)
    *   [Plugin development docs](https://hardhat.org/docs/plugin-development)

*   [Hardhat 2 docs](https://hardhat.org/hardhat2)

[GitHub](https://github.com/NomicFoundation/hardhat)[X](https://x.com/HardhatHQ)[Discord](https://hardhat.org/discord)

Select theme 

On this page

*   [Overview](https://hardhat.org/docs/guides/testing/using-solidity#_top)
*   [Writing Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity#writing-solidity-tests)
    *   [Fuzz tests](https://hardhat.org/docs/guides/testing/using-solidity#fuzz-tests)
    *   [Using assertion libraries](https://hardhat.org/docs/guides/testing/using-solidity#using-assertion-libraries)
    *   [Setup functions](https://hardhat.org/docs/guides/testing/using-solidity#setup-functions)
    *   [Using cheatcodes](https://hardhat.org/docs/guides/testing/using-solidity#using-cheatcodes)

*   [Running Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity#running-solidity-tests)
    *   [Multichain support](https://hardhat.org/docs/guides/testing/using-solidity#multichain-support)

*   [Configuring Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity#configuring-solidity-tests)
    *   [Configuring the tests location](https://hardhat.org/docs/guides/testing/using-solidity#configuring-the-tests-location)
    *   [Configuring the tests execution](https://hardhat.org/docs/guides/testing/using-solidity#configuring-the-tests-execution)

On this page
------------

*   [Overview](https://hardhat.org/docs/guides/testing/using-solidity#_top)
*   [Writing Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity#writing-solidity-tests)
    *   [Fuzz tests](https://hardhat.org/docs/guides/testing/using-solidity#fuzz-tests)
    *   [Using assertion libraries](https://hardhat.org/docs/guides/testing/using-solidity#using-assertion-libraries)
    *   [Setup functions](https://hardhat.org/docs/guides/testing/using-solidity#setup-functions)
    *   [Using cheatcodes](https://hardhat.org/docs/guides/testing/using-solidity#using-cheatcodes)

*   [Running Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity#running-solidity-tests)
    *   [Multichain support](https://hardhat.org/docs/guides/testing/using-solidity#multichain-support)

*   [Configuring Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity#configuring-solidity-tests)
    *   [Configuring the tests location](https://hardhat.org/docs/guides/testing/using-solidity#configuring-the-tests-location)
    *   [Configuring the tests execution](https://hardhat.org/docs/guides/testing/using-solidity#configuring-the-tests-execution)

Writing unit tests in Solidity
==============================

Hardhat has built-in support for Solidity tests. You don’t need to install any plugin to use them.

Writing Solidity tests
----------------------

[Section titled “Writing Solidity tests”](https://hardhat.org/docs/guides/testing/using-solidity#writing-solidity-tests)

A Solidity file is considered a **test file** if:

*   It’s inside the `test/` directory
*   It’s inside the `contracts/` directory and ends with `.t.sol`

Both of these directories can be changed in your Hardhat [configuration](https://hardhat.org/docs/reference/configuration), but these are the default ones.

If a contract in a test file has at least one function that starts with `test`, it’s considered a **test contract**. When the tests are run, Hardhat deploys every test contract and calls each of its test functions.

For example, if you have a file named `contracts/CounterTest.t.sol` or `test/CounterTest.sol` with the following contract:

`contract CounterTest {  function testInc() public {    Counter counter = new Counter();    counter.inc();    require(counter.count() == 1, "count should be 1");  }}`

the test runner will deploy the `CounterTest` contract and call its `testInc` function. If the function execution reverts, the test is considered failed.

### Fuzz tests

[Section titled “Fuzz tests”](https://hardhat.org/docs/guides/testing/using-solidity#fuzz-tests)

Hardhat also supports **fuzz tests**, which are similar to regular tests but accept parameters. When the tests are executed, fuzz test functions are called multiple times with random values as arguments:

`contract CounterTest {  function testIncBy(uint by) public {    Counter counter = new Counter();    counter.incBy(by);    require(counter.count() == by, "count should match the 'by' value");  }}`

### Using assertion libraries

[Section titled “Using assertion libraries”](https://hardhat.org/docs/guides/testing/using-solidity#using-assertion-libraries)

In the previous example, the error message doesn’t show the actual value of `by` that made the test fail. That’s because interpolating the value into the string isn’t straightforward in Solidity. To get better error messages, plus other useful functionality, you can use an assertion library like [forge-std](https://github.com/foundry-rs/forge-std).

To use `forge-std` in a Hardhat project, first install it:

*   [npm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-300)
*   [pnpm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-301)
*   [Yarn](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-302)

Terminal window

`npm add --save-dev 'github:foundry-rs/forge-std#v1.9.7'`

Terminal window

`pnpm add --save-dev 'github:foundry-rs/forge-std#v1.9.7'`

Terminal window

`yarn add --dev 'github:foundry-rs/forge-std#v1.9.7'`

You can then import the `Test` base contract and extend your test contracts from it. This lets you use helper functions like `assertEq`, which shows the mismatched values when the assertion fails:

```
import { Test } from "forge-std/Test.sol";
contract CounterTest is Test {  function testIncBy(uint by) public {    Counter counter = new Counter();    counter.incBy(by);    assertEq(counter.count(), by, "count should match the 'by' value");  }}
```

### Setup functions

[Section titled “Setup functions”](https://hardhat.org/docs/guides/testing/using-solidity#setup-functions)

Both the unit and fuzz test examples shown above create an instance of the `Counter` contract. You can share setup logic like that across tests using the `setUp` function, which is called before each test execution:

```
contract CounterTest {  Counter counter;
  function setUp() public {    counter = new Counter();  }
  function testInc() public {    counter.inc();    require(counter.count() == 1, "count should be 1");  }
  function testIncBy(uint by) public {    counter.incBy(by);    require(counter.count() == by, "count should match the 'by' value");  }}
```

### Using cheatcodes

[Section titled “Using cheatcodes”](https://hardhat.org/docs/guides/testing/using-solidity#using-cheatcodes)

When writing Solidity tests in Hardhat, you can use [Solidity test cheatcodes](https://hardhat.org/docs/reference/cheatcodes/cheatcodes-overview) to manipulate the EVM state and control the execution environment of your tests.

For example, you can use the [`vm.prank`](https://hardhat.org/docs/reference/cheatcodes/environment/prank) cheatcode to change the `msg.sender` for the next call:

```
import { Test } from "forge-std/Test.sol";
contract CounterTest is Test {  Counter counter;
  function setUp() public {    counter = new Counter();  }
  function testIncAsAlice() public {    address alice = address(0x123);    vm.prank(alice);    counter.inc();    assertEq(counter.count(), 1, "count should be 1");    assertEq(counter.lastCaller(), alice, "last caller should be alice");  }}
```

Running Solidity tests
----------------------

[Section titled “Running Solidity tests”](https://hardhat.org/docs/guides/testing/using-solidity#running-solidity-tests)

You can run all the tests in your Hardhat project using the `test` task:

*   [npm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-303)
*   [pnpm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-304)
*   [Yarn](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-305)

Terminal window

`npx hardhat test`

Terminal window

`pnpm hardhat test`

Terminal window

`yarn hardhat test`

If you only want to run your Solidity tests, use the `test solidity` task instead:

*   [npm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-306)
*   [pnpm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-307)
*   [Yarn](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-308)

Terminal window

`npx hardhat test solidity`

Terminal window

`pnpm hardhat test solidity`

Terminal window

`yarn hardhat test solidity`

You can also pass one or more paths as arguments to these tasks, in which case only those files are executed:

*   [npm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-309)
*   [pnpm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-310)
*   [Yarn](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-311)

Terminal window

`npx hardhat test <test-file-1> <test-file-2> ...`

Terminal window

`pnpm hardhat test <test-file-1> <test-file-2> ...`

Terminal window

`yarn hardhat test <test-file-1> <test-file-2> ...`

### Multichain support

[Section titled “Multichain support”](https://hardhat.org/docs/guides/testing/using-solidity#multichain-support)

By default, Solidity tests run in an environment that simulates Ethereum Mainnet. If you’re building for other blockchains, you can test against their specific behavior by specifying a different Chain Type with the `--chain-type` option:

*   [npm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-312)
*   [pnpm](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-313)
*   [Yarn](https://hardhat.org/docs/guides/testing/using-solidity#tab-panel-314)

Terminal window

`npx hardhat test solidity --chain-type op`

Terminal window

`pnpm hardhat test solidity --chain-type op`

Terminal window

`yarn hardhat test solidity --chain-type op`

This example uses the `op` Chain Type, which simulates OP Mainnet and its testnets.

To learn more about Chain Types and testing on different blockchains, read our [multichain support](https://hardhat.org/docs/explanations/multichain-support) explanation.

Configuring Solidity tests
--------------------------

[Section titled “Configuring Solidity tests”](https://hardhat.org/docs/guides/testing/using-solidity#configuring-solidity-tests)

You can configure how Solidity tests are executed in your Hardhat configuration.

### Configuring the tests location

[Section titled “Configuring the tests location”](https://hardhat.org/docs/guides/testing/using-solidity#configuring-the-tests-location)

By default, Hardhat treats every Solidity file in the `test/` directory as a test file. To use a different location, set the `paths.tests.solidity` field:

hardhat.config.ts

```
import { defineConfig } from "hardhat/config";
export default defineConfig({  /// ... other config ...  paths: {    tests: {      solidity: "./solidity-tests",    },  },});
```

### Configuring the tests execution

[Section titled “Configuring the tests execution”](https://hardhat.org/docs/guides/testing/using-solidity#configuring-the-tests-execution)

To configure how Solidity tests are executed, use the `test.solidity` object in the Hardhat configuration.

For example, the `ffi` cheatcode is disabled by default for security reasons, but you can enable it:

hardhat.config.ts

```
import { defineConfig } from "hardhat/config";
export default defineConfig({  /// ... other config ...  test: {    solidity: {      ffi: true,    },  },});
```

It’s also possible to modify the execution environment of the tests. For example, you can modify the address that is returned by `msg.sender`:

hardhat.config.ts

```
import { defineConfig } from "hardhat/config";
export default defineConfig({  /// ... other config ...  test: {    solidity: {      from: "0x1234567890123456789012345678901234567890",    },  },});
```

To learn more about how to configure your Solidity tests, read [the Solidity tests Configuration reference](https://hardhat.org/docs/reference/configuration#solidity-tests-configuration).

[Edit page](https://github.com/NomicFoundation/hardhat-website/edit/main/src/content/docs/docs/guides/testing/using-solidity.mdx)

[Previous Testing overview](https://hardhat.org/docs/guides/testing)[Next Using TypeScript & viem](https://hardhat.org/docs/guides/testing/using-viem)
