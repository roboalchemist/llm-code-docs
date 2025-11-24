# Source: https://docs.hypermode.com/dgraph/concepts/wal-memtable.md

# WAL and Memtable

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

Per the Raft (and MVCC) approach, transactions write data to a `Write-Ahead Log`
(WAL) to ensure it's durably stored. Soon after commit, data is also updated in
the `memtables` which are memory buffers holding recently-updated data. The
`memtables` are mutable, unlike the SST files written to disk which hold most
data. Once full, memtables are flushed to disk and become SST files. See Log
Compaction for more details on this process.

In the event of a system crash, the persistent data in the Write Ahead Logs is
replayed to rebuild the memtables and restore the full system state from before
the crash.
