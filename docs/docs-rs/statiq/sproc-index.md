statiq
# Module sproc 
Source 
## Structs§
MultiReaderManual reader for 5+ result sets — or when typed tuples are insufficient.RequiredFirst row of a result set — error if the set is empty.ScalarFirst column of the first row, parsed via `std::str::FromStr`.SingleFirst row of a result set — `None` if the set is empty.SprocPagedResultPaged result from a stored procedure.SprocParamsFluent parameter builder for stored procedure calls.SprocResultBusiness-level result wrapper — mirrors the common `SprocResult<T>` pattern.SprocServiceStored procedure execution service.
## Traits§
FromResultSetConvert one ODBC result set (a `Vec<OdbcRow>`) into `Self`.