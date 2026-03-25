# Source: https://hardhat.org/docs/guides/writing-tasks

Title: Writing Hardhat tasks

URL Source: https://hardhat.org/docs/guides/writing-tasks

Markdown Content:
Writing Hardhat tasks | Hardhat 3
===============
[Skip to content](https://hardhat.org/docs/guides/writing-tasks#_top)

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

*   [Overview](https://hardhat.org/docs/guides/writing-tasks#_top)
*   [Writing a task](https://hardhat.org/docs/guides/writing-tasks#writing-a-task)
*   [Using inline actions](https://hardhat.org/docs/guides/writing-tasks#using-inline-actions)
    *   [Choosing between setAction and setInlineAction](https://hardhat.org/docs/guides/writing-tasks#choosing-between-setaction-and-setinlineaction)

*   [Returning a result](https://hardhat.org/docs/guides/writing-tasks#returning-a-result)

On this page
------------

*   [Overview](https://hardhat.org/docs/guides/writing-tasks#_top)
*   [Writing a task](https://hardhat.org/docs/guides/writing-tasks#writing-a-task)
*   [Using inline actions](https://hardhat.org/docs/guides/writing-tasks#using-inline-actions)
    *   [Choosing between setAction and setInlineAction](https://hardhat.org/docs/guides/writing-tasks#choosing-between-setaction-and-setinlineaction)

*   [Returning a result](https://hardhat.org/docs/guides/writing-tasks#returning-a-result)

Writing Hardhat tasks
=====================

At its core, Hardhat is a task runner that lets you automate your development workflow. It comes with built-in tasks like `compile` and `test`, but you can also add your own custom tasks.

In this guide, we’ll explore how to extend Hardhat’s functionality using tasks. It assumes you’ve initialized a sample project. If you haven’t, read the [getting started guide](https://hardhat.org/docs/getting-started) first.

Writing a task
--------------

[Section titled “Writing a task”](https://hardhat.org/docs/guides/writing-tasks#writing-a-task)

Let’s write a simple task that prints the list of available accounts. This will help you understand how tasks work and how to create your own.

First, copy and paste the following code into your Hardhat config file:

hardhat.config.ts

```
import { defineConfig, task } from "hardhat/config";
const printAccounts = task("accounts", "Print the accounts")  .setAction(() => import("./tasks/accounts.js"))  .build();
```

Now let’s create a `tasks/accounts.ts` file with the task action, which contains the logic that the task will run:

tasks/accounts.ts

```
import { HardhatRuntimeEnvironment } from "hardhat/types/hre";
interface AccountTaskArguments {  // No argument in this case}
export default async function (  taskArguments: AccountTaskArguments,  hre: HardhatRuntimeEnvironment,) {  const { provider } = await hre.network.connect();  console.log(await provider.request({ method: "eth_accounts" }));}
```

Next, add the `printAccounts` task to the exported configuration object in your Hardhat config file:

hardhat.config.ts

`export default defineConfig({  // ... rest of the config  tasks: [printAccounts],});`

Now you should be able to run it:

*   [npm](https://hardhat.org/docs/guides/writing-tasks#tab-panel-114)
*   [pnpm](https://hardhat.org/docs/guides/writing-tasks#tab-panel-115)
*   [Yarn](https://hardhat.org/docs/guides/writing-tasks#tab-panel-116)

Terminal window

`npx hardhat accounts`

Terminal window

`pnpm hardhat accounts`

Terminal window

`yarn hardhat accounts`

We’re using the `task` function to define our new task. Its first argument is the name of the task, which is what we use on the command line to run it. The second argument is the description, which appears when you run `hardhat help`.

The `task` function returns a task builder object that lets you further configure the task. In this case, we use the `setAction` method to define the task’s behavior by providing a function that lazy loads another module.

That module exports the action function itself, which implements your custom logic. In this case, we send a request to the network provider to get all the configured accounts and print their addresses.

Add parameters to your tasks, and Hardhat handles their parsing and validation for you. Override existing tasks to customize how different parts of Hardhat work.

Using inline actions
--------------------

[Section titled “Using inline actions”](https://hardhat.org/docs/guides/writing-tasks#using-inline-actions)

As an alternative to defining task actions in separate files, define them directly inline using `setInlineAction`. This is convenient for simple tasks where a separate file would be overkill.

Here’s how the accounts task would look using an inline action:

hardhat.config.ts

```
import { defineConfig, task } from "hardhat/config";
const printAccounts = task("accounts", "Print the accounts")  .setInlineAction(async (taskArguments, hre) => {    const { provider } = await hre.network.connect();    console.log(await provider.request({ method: "eth_accounts" }));  })  .build();
export default defineConfig({  // ... rest of the config  tasks: [printAccounts],});
```

With `setInlineAction`, the task logic is defined directly as a function parameter, eliminating the need for a separate file.

### Choosing between `setAction` and `setInlineAction`

[Section titled “Choosing between setAction and setInlineAction”](https://hardhat.org/docs/guides/writing-tasks#choosing-between-setaction-and-setinlineaction)

Use `setAction` when you’re building a plugin or a complex task with a lot of code, or if it needs to import dependencies. This keeps the code organized, improves Hardhat’s load time (as they’re loaded on demand), and makes your setup or plugin more resilient to installation errors.

On the other hand, if you’re building a simple task that only uses the Hardhat Runtime Environment, use `setInlineAction` to define the task’s behavior inline, without the boilerplate of a separate file.

Here’s a comparison of the two approaches:

|  | `setAction()` (Lazy-loaded) | `setInlineAction()` |
| --- | --- | --- |
| **Use cases** | Complex tasks Plugin tasks Tasks that import dependencies | Simple user tasks |
| **Available for plugins** | ✅ Yes (required) | ❌ No |
| **Available for users** | ✅ Yes | ✅ Yes |
| **Performance** | Lazy-loaded on demand | Loaded every time you run Hardhat |
| **File organization** | Separate action files | Defined inline in your config |
| **Can use `import { ... } from 'hardhat'`?** | ✅ Yes, because they are loaded after Hardhat’s initialization | ❌ No, because they are evaluated during Hardhat’s initialization |

Each task must define exactly one action: call either `setAction()` or `setInlineAction()`, but not both.

You can also use `setInlineAction` with `overrideTask` to customize existing tasks directly in your config file.

Plugin developers

If you’re developing a plugin, you must use `setAction()` with lazy-loaded modules. The `setInlineAction()` method is only available for user-defined tasks in configuration files.

To learn more about how task actions are loaded, see the [Task Actions’ lifecycle](https://hardhat.org/docs/plugin-development/explanations/lifecycle#task-actions-lifecycle) documentation.

Returning a result
------------------

[Section titled “Returning a result”](https://hardhat.org/docs/guides/writing-tasks#returning-a-result)

Task actions can optionally return a `Result` to signal success or failure to the CLI. When a task action returns a failed result, the CLI sets the process exit code to 1. This is useful when you want to indicate failure to scripts or CI pipelines without throwing an exception.

To use this, import the `Result` type from `hardhat/types/utils` and the helper functions from `hardhat/utils/result`:

tasks/accounts.ts

```
import type { HardhatRuntimeEnvironment } from "hardhat/types/hre";import type { Result } from "hardhat/types/utils";import { successfulResult, errorResult } from "hardhat/utils/result";
interface AccountTaskArguments {}
export default async function (  _taskArguments: AccountTaskArguments,  hre: HardhatRuntimeEnvironment,): Promise<Result<string[], string>> {  const { provider } = await hre.network.connect();  const accounts = await provider.request({ method: "eth_accounts" });
  if (accounts.length === 0) {    return errorResult("No accounts found");  }
  return successfulResult(accounts);}
```

`Result<ValueT, ErrorT>` is a discriminated union:

*   `{ success: true; value: ValueT }` - a successful result, carrying a value
*   `{ success: false; error: ErrorT }` - a failed result, carrying error information

Use `successfulResult(value?)` and `errorResult(error?)` to create these objects. Both helpers can be called without a parameter, in which case they set `value` or `error` to `undefined`.

If a task action doesn’t return a `Result` (for example, it returns `undefined` or any other value), the CLI exit code is left unchanged.

[Edit page](https://github.com/NomicFoundation/hardhat-website/edit/main/src/content/docs/docs/guides/writing-tasks.mdx)

[Previous Managing config values and secrets](https://hardhat.org/docs/guides/configuration-variables)[Next Writing scripts with Hardhat](https://hardhat.org/docs/guides/writing-scripts)
