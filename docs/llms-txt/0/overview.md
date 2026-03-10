# Overview

Wrapped0GBase is a wrapper for the `x/wrapped-og-base` module in the 0g chain. W0G is a wrapped ERC20 token for native 0G. It supports quota-based mint/burn functions based on native 0G transfers, on top of traditional wrapped token implementation. The minting/burning quota for each address will be determined through governance voting. `x/wrapped-og-base` is the module that supports and maintains the minting/burning quota.

In most cases this precompile should be only called by wrapped 0G contract.