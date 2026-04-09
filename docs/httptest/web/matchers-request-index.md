httptest::matchers
# Module request 
Source 
## Structs§
BodyThe `Body` mapper returned by body()HeadersThe `Headers` mapper returned by headers()MethodThe `Method` mapper returned by method()MethodPathThe `MethodPath` mapper returned by method_path()PathThe `Path` mapper returned by path()QueryThe `Query` mapper returned by query()
## Functions§
bodyExtract the body from the HTTP request and pass it to the next mapper.headersExtract the headers from the HTTP request and pass the sequence to the next
mapper.methodExtract the method from the HTTP request and pass it to the next mapper.method_pathA convenience matcher for both method and path. Extracts a bolean true if the method and path both match.pathExtract the path from the HTTP request and pass it to the next mapper.queryExtract the query from the HTTP request and pass it to the next mapper.