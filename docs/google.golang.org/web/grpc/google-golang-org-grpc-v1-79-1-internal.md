# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal

Title: internal package - google.golang.org/grpc/internal - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal

Markdown Content:
Path Synopsis
Package admin contains internal implementation for admin service.Package admin contains internal implementation for admin service.
Package backoff implement the backoff strategy for gRPC.Package backoff implement the backoff strategy for gRPC.
balancer
[gracefulswitch](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/balancer/gracefulswitch)

Package gracefulswitch implements a graceful switch load balancer.Package gracefulswitch implements a graceful switch load balancer.
[nop](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/balancer/nop)

Package nop implements a balancer with all of its balancer operations as no-ops, other than returning a Transient Failure Picker on a Client Conn update.Package nop implements a balancer with all of its balancer operations as no-ops, other than returning a Transient Failure Picker on a Client Conn update.
[stub](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/balancer/stub)

Package stub implements a balancer for testing purposes.Package stub implements a balancer for testing purposes.
[weight](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/balancer/weight)

Package weight contains utilities to manage endpoint weights.Package weight contains utilities to manage endpoint weights.
Package balancergroup implements a utility struct to bind multiple balancers into one balancer.Package balancergroup implements a utility struct to bind multiple balancers into one balancer.
Package balancerload defines APIs to parse server loads in trailers.Package balancerload defines APIs to parse server loads in trailers.
Package binarylog implementation binary logging as defined in https://github.com/grpc/proposal/blob/master/A16-binary-logging.md.Package binarylog implementation binary logging as defined in https://github.com/grpc/proposal/blob/master/A16-binary-logging.md.
Package buffer provides an implementation of an unbounded buffer.Package buffer provides an implementation of an unbounded buffer.
Package cache implements caches to be used in gRPC.Package cache implements caches to be used in gRPC.
Package channelz defines internal APIs for enabling channelz service, entry registration/deletion, and accessing channelz data.Package channelz defines internal APIs for enabling channelz service, entry registration/deletion, and accessing channelz data.
Package credentials defines APIs for parsing SPIFFE ID.Package credentials defines APIs for parsing SPIFFE ID.
[spiffe](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/credentials/spiffe)

Package spiffe defines APIs for working with SPIFFE Bundle Maps.Package spiffe defines APIs for working with SPIFFE Bundle Maps.
[xds](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/credentials/xds)

Package xds contains non-user facing functionality of the xds credentials.Package xds contains non-user facing functionality of the xds credentials.
Package envconfig contains grpc settings configured by environment variables.Package envconfig contains grpc settings configured by environment variables.
Package googlecloud contains internal helpful functions for google cloud.Package googlecloud contains internal helpful functions for google cloud.
Package grpclog provides logging functionality for internal gRPC packages, outside of the functionality provided by the external `grpclog` package.Package grpclog provides logging functionality for internal gRPC packages, outside of the functionality provided by the external `grpclog` package.
Package grpcsync implements additional synchronization primitives built upon the sync package.Package grpcsync implements additional synchronization primitives built upon the sync package.
Package grpctest implements testing helpers.Package grpctest implements testing helpers.
Package grpcutil provides utility functions used across the gRPC codebase.Package grpcutil provides utility functions used across the gRPC codebase.
Package hierarchy contains functions to set and get hierarchy string from addresses.Package hierarchy contains functions to set and get hierarchy string from addresses.
Package idle contains a component for managing idleness (entering and exiting) based on RPC activity.Package idle contains a component for managing idleness (entering and exiting) based on RPC activity.
Package leakcheck contains functions to check leaked goroutines and buffers.Package leakcheck contains functions to check leaked goroutines and buffers.
Package metadata contains functions to set and get metadata from addresses.Package metadata contains functions to set and get metadata from addresses.
Package pretty defines helper functions to pretty-print structs for logging.Package pretty defines helper functions to pretty-print structs for logging.
Package profiling contains two logical components: buffer.go and profiling.go.Package profiling contains two logical components: buffer.go and profiling.go.
[buffer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/profiling/buffer)

Package buffer provides a high-performant lock free implementation of a circular buffer used by the profiling code.Package buffer provides a high-performant lock free implementation of a circular buffer used by the profiling code.
proto

Package proxyattributes contains functions for getting and setting proxy attributes like the CONNECT address and user info.Package proxyattributes contains functions for getting and setting proxy attributes like the CONNECT address and user info.
Package resolver provides internal resolver-related functionality.Package resolver provides internal resolver-related functionality.
[delegatingresolver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/resolver/delegatingresolver)

Package delegatingresolver implements a resolver capable of resolving both target URIs and proxy addresses.Package delegatingresolver implements a resolver capable of resolving both target URIs and proxy addresses.
[dns](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/resolver/dns)

Package dns implements a dns resolver to be installed as the default resolver in grpc.Package dns implements a dns resolver to be installed as the default resolver in grpc.
[dns/internal](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/resolver/dns/internal)

Package internal contains functionality internal to the dns resolver package.Package internal contains functionality internal to the dns resolver package.
[passthrough](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/resolver/passthrough)

Package passthrough implements a pass-through resolver.Package passthrough implements a pass-through resolver.
[unix](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/resolver/unix)

Package unix implements a resolver for unix targets.Package unix implements a resolver for unix targets.
Package ringhash (internal) contains functions and types that need to be shared by the ring hash balancer and other gRPC code (such as xDS) without being exported.Package ringhash (internal) contains functions and types that need to be shared by the ring hash balancer and other gRPC code (such as xDS) without being exported.
Package serviceconfig contains utility functions to parse service config.Package serviceconfig contains utility functions to parse service config.
Package stats provides internal stats related functionality.Package stats provides internal stats related functionality.
Package status implements errors returned by gRPC.Package status implements errors returned by gRPC.
Package stubserver is a stubbable implementation of google.golang.org/grpc/interop/grpc_testing for testing purposes.Package stubserver is a stubbable implementation of google.golang.org/grpc/interop/grpc_testing for testing purposes.
Package syscall provides functionalities that grpc uses to get low-level operating system stats/info.Package syscall provides functionalities that grpc uses to get low-level operating system stats/info.
Package testutils contains testing helpers.Package testutils contains testing helpers.
[fakegrpclb](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/fakegrpclb)

Package fakegrpclb provides a fake implementation of the grpclb server.Package fakegrpclb provides a fake implementation of the grpclb server.
[pickfirst](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/pickfirst)

Package pickfirst contains helper functions to check for pickfirst load balancing of RPCs in tests.Package pickfirst contains helper functions to check for pickfirst load balancing of RPCs in tests.
[proxyserver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/proxyserver)

Package proxyserver provides an implementation of a proxy server for testing purposes.Package proxyserver provides an implementation of a proxy server for testing purposes.
[rls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/rls)

Package rls contains utilities for RouteLookupService e2e tests.Package rls contains utilities for RouteLookupService e2e tests.
[roundrobin](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/roundrobin)

Package roundrobin contains helper functions to check for roundrobin and weighted-roundrobin load balancing of RPCs in tests.Package roundrobin contains helper functions to check for roundrobin and weighted-roundrobin load balancing of RPCs in tests.
[stats](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/stats)

Package stats implements a TestMetricsRecorder utility.Package stats implements a TestMetricsRecorder utility.
[xds/e2e](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/xds/e2e)

Package e2e provides utilities for end2end testing of xDS functionality.Package e2e provides utilities for end2end testing of xDS functionality.
[xds/e2e/setup](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/xds/e2e/setup)

Package setup implements setup helpers for xDS e2e tests.Package setup implements setup helpers for xDS e2e tests.
[xds/fakeserver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/testutils/xds/fakeserver)

Package fakeserver provides a fake implementation of the management server.Package fakeserver provides a fake implementation of the management server.
Package transport defines and implements message oriented communication channel to complete various transactions (e.g., an RPC).Package transport defines and implements message oriented communication channel to complete various transactions (e.g., an RPC).
[networktype](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/transport/networktype)

Package networktype declares the network type to be used in the default dialer.Package networktype declares the network type to be used in the default dialer.
Package wrr contains the interface and common implementations of wrr algorithms.Package wrr contains the interface and common implementations of wrr algorithms.
Package xds contains functions, structs, and utilities for working with handshake cluster names, as well as shared components used by xds balancers and resolvers.Package xds contains functions, structs, and utilities for working with handshake cluster names, as well as shared components used by xds balancers and resolvers.
[balancer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/balancer)

Package balancer installs all the xds balancers.Package balancer installs all the xds balancers.
Package cdsbalancer implements a balancer to handle CDS responses.
Package clusterimpl implements the xds_cluster_impl balancing policy.
Package clustermanager implements the cluster manager LB policy for xds.
[balancer/clusterresolver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/balancer/clusterresolver)

Package clusterresolver contains the implementation of the cluster_resolver_experimental LB policy which resolves endpoint addresses using a list of one or more discovery mechanisms.Package clusterresolver contains the implementation of the cluster_resolver_experimental LB policy which resolves endpoint addresses using a list of one or more discovery mechanisms.
[balancer/loadstore](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/balancer/loadstore)

Package loadstore contains the loadStoreWrapper shared by the balancers.Package loadstore contains the loadStoreWrapper shared by the balancers.
[balancer/outlierdetection](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/balancer/outlierdetection)

Package outlierdetection provides an implementation of the outlier detection LB policy, as defined in https://github.com/grpc/proposal/blob/master/A50-xds-outlier-detection.md.Package outlierdetection provides an implementation of the outlier detection LB policy, as defined in https://github.com/grpc/proposal/blob/master/A50-xds-outlier-detection.md.
Package priority implements the priority balancer.
[balancer/wrrlocality](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/balancer/wrrlocality)

Package wrrlocality provides an implementation of the wrr locality LB policy, as defined in [A52 - xDS Custom LB Policies].Package wrrlocality provides an implementation of the wrr locality LB policy, as defined in [A52 - xDS Custom LB Policies].
[bootstrap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/bootstrap)

Package bootstrap provides the functionality to initialize certain aspects of an xDS client by reading a bootstrap file.Package bootstrap provides the functionality to initialize certain aspects of an xDS client by reading a bootstrap file.
[bootstrap/jwtcreds](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/bootstrap/jwtcreds)

Package jwtcreds implements JWT CallCredentials for XDS, configured via xDS Bootstrap File.Package jwtcreds implements JWT CallCredentials for XDS, configured via xDS Bootstrap File.
Package tlscreds implements mTLS Credentials in xDS Bootstrap File.
[clients](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/clients)

Package clients provides implementations of the clients to interact with xDS and LRS servers.Package clients provides implementations of the clients to interact with xDS and LRS servers.
[clients/grpctransport](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/clients/grpctransport)

Package grpctransport provides an implementation of the clients.TransportBuilder interface using gRPC.Package grpctransport provides an implementation of the clients.TransportBuilder interface using gRPC.
Package internal contains helpers for xDS and LRS clients.
Package backoff implements the backoff strategy for clients.
Package buffer provides an implementation of an unbounded buffer.
Package pretty defines helper functions to pretty-print structs for logging.
Package syncutil implements additional synchronization primitives built upon the sync package.
Package testutils contains testing helpers for xDS and LRS clients.
Package e2e provides utilities for end2end testing of xDS and LRS clients functionalities.
Package fakeserver provides a fake implementation of the management server.
Package lrsclient provides an LRS (Load Reporting Service) client.
Package internal contains functionality internal to the lrsclient package.
Package xdsclient provides an xDS (* Discovery Service) client.
Package internal contains functionality internal to the xdsclient package.
Package xdsresource defines constants to distinguish between supported xDS API versions.
Package metrics defines all metrics that can be produced by an xDS client.
[clusterspecifier](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/clusterspecifier)

Package clusterspecifier contains the ClusterSpecifier interface and a registry for storing and retrieving their implementations.Package clusterspecifier contains the ClusterSpecifier interface and a registry for storing and retrieving their implementations.
Package rls implements the RLS cluster specifier plugin.
[httpfilter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/httpfilter)

Package httpfilter contains the HTTPFilter interface and a registry for storing and retrieving their implementations.Package httpfilter contains the HTTPFilter interface and a registry for storing and retrieving their implementations.
[httpfilter/fault](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/httpfilter/fault)

Package fault implements the Envoy Fault Injection HTTP filter.Package fault implements the Envoy Fault Injection HTTP filter.
Package rbac implements the Envoy RBAC HTTP filter.
Package router implements the Envoy Router HTTP filter.
[matcher](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/matcher)

Package matcher contains types that need to be shared between code under google.golang.org/grpc/xds/...Package matcher contains types that need to be shared between code under google.golang.org/grpc/xds/...
[rbac](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/rbac)

Package rbac provides service-level and method-level access control for a service.Package rbac provides service-level and method-level access control for a service.
[resolver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/resolver)

Package resolver implements the xds resolver, that does LDS and RDS to find the cluster to use.Package resolver implements the xds resolver, that does LDS and RDS to find the cluster to use.
[resolver/internal](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/resolver/internal)

Package internal contains functionality internal to the xDS resolver.Package internal contains functionality internal to the xDS resolver.
[server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/server)

Package server contains internal server-side functionality used by the public facing xds package.Package server contains internal server-side functionality used by the public facing xds package.
[test/e2e](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/test/e2e)

Package e2e implements xds e2e tests using go-control-plane.Package e2e implements xds e2e tests using go-control-plane.
[testutils](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/testutils)

Package testutils provides utility types, for use in xds tests.Package testutils provides utility types, for use in xds tests.
Package fakeclient provides a fake implementation of an xDS client.
[xdsclient](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/xdsclient)

Package xdsclient implements a full fledged gRPC client for the xDS API used by the xds resolver and balancer implementations.Package xdsclient implements a full fledged gRPC client for the xDS API used by the xds resolver and balancer implementations.
[xdsclient/internal](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/xdsclient/internal)

Package internal contains functionality internal to the xdsclient package.Package internal contains functionality internal to the xdsclient package.
[xdsclient/xdslbregistry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/xdsclient/xdslbregistry)

Package xdslbregistry provides a registry of converters that convert proto from load balancing configuration, defined by the xDS API spec, to JSON load balancing configuration.Package xdslbregistry provides a registry of converters that convert proto from load balancing configuration, defined by the xDS API spec, to JSON load balancing configuration.
[xdsclient/xdslbregistry/converter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/xdsclient/xdslbregistry/converter)

Package converter provides converters to convert proto load balancing configuration, defined by the xDS API spec, to JSON load balancing configuration.Package converter provides converters to convert proto load balancing configuration, defined by the xDS API spec, to JSON load balancing configuration.
Package xdsresource implements the xDS data model layer.
Package version defines constants to distinguish between supported xDS API versions.
[xdsdepmgr](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal/xds/xdsdepmgr)

Package xdsdepmgr provides the implementation of the xDS dependency manager that manages all the xDS watches and resources as described in gRFC A74.Package xdsdepmgr provides the implementation of the xDS dependency manager that manages all the xDS watches and resources as described in gRFC A74.
