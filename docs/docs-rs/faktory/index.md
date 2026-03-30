# Crate faktory 
Source 
## Re-exports§
`pub use crate::error::Error;`
## Modules§
ent`ent`Constructs only available with the enterprise version of Faktory.errorEnumerates all errors that this crate may return.mutateConstructs used to mutate queues on the Faktory server.native_tls`native_tls`Namespace for native TLS powered `TlsStream`.rustls`rustls`Namespace for Rustls-powered `TlsStream`.
## Structs§
Client`Client` is used to enqueue new jobs that will in turn be processed by Faktory workers.DataSnapshotFaktory service information.FailureDetails on a job’s failure.FaktoryStateCurrent server state.JobA Faktory job.JobBuilderBuilder for `Job`.JobIdJob identifier.ServerSnapshotFaktory’s server process information.StopDetailsHolds some details aroung a worker’s run stoppage, such as the reason why this worker discontinued
and the number of workers that might still be processing jobs at that instant.Worker`Worker` is used to run a worker that processes jobs provided by Faktory.WorkerBuilderConvenience wrapper for building a Faktory worker.WorkerIdWorker identifier.
## Enums§
StopReasonA reason why `Worker::run` has discontinued.
## Traits§
ConnectionA duplex buffered stream to the Faktory service.JobRunnerImplementations of this trait can be registered to run jobs in a `Worker`.ReconnectA stream that can be re-established after failing.