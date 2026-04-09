# Crate statiq 
Source 
## Re-exports§
`pub use cache::CacheLayer;``pub use cache::NoCache;``pub use cache::RedisCache;``pub use config::AppConfig;``pub use entity::SqlEntity;``pub use error::SqlError;``pub use factory::SqlServiceFactory;``pub use params::OdbcParam;``pub use params::ParamValue;``pub use params::PkValue;``pub use pool::Pool;``pub use repository::SqlRepository;``pub use row::OdbcRow;``pub use service::SqlService;``pub use sproc::FromResultSet;``pub use sproc::MultiReader;``pub use sproc::Required;``pub use sproc::Scalar;``pub use sproc::Single;``pub use sproc::SprocPagedResult;``pub use sproc::SprocParams;``pub use sproc::SprocResult;``pub use sproc::SprocService;``pub use transaction::Transaction;`
## Modules§
cacheconfigentityerrorfactoryloggingparamspoolqueryrepositoryrowservicesprocSprocService — Stored Procedure Execution Layertransaction
## Macros§
paramsTip-güvenli parametre slice’ı oluşturur — heap allocation yok.
## Derive Macros§
SqlEntityDerive macro that implements `sqlservice::entity::SqlEntity` for a struct.