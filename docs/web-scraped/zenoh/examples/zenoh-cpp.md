# Zenoh Examples: zenoh-cpp

add_custom_target(examples)

if(ZENOHCXX_ZENOHC)
	add_custom_target(examples_zenohc)
	add_dependencies(examples examples_zenohc)
endif()

if(ZENOHCXX_ZENOHPICO)
	add_custom_target(examples_zenohpico)
	add_dependencies(examples examples_zenohpico)
endif()

function(add_protobuf target mode)
	if(ZENOHCXX_EXAMPLES_PROTOBUF)
		find_package(Protobuf)
		if(Protobuf_FOUND)
			message(STATUS "Found Protobuf ${protobuf_VERSION}, will build Protobuf example!")

			protobuf_generate_cpp(pb_src pb_hdr ${CMAKE_CURRENT_LIST_DIR}/universal/proto/entity.proto)

			add_library(example_message_${mode} ${pb_hdr} ${pb_src})
			target_include_directories(example_message_${mode} INTERFACE ${CMAKE_CURRENT_BINARY_DIR})
			target_link_libraries(example_message_${mode} PUBLIC protobuf::libprotobuf)

			target_link_libraries(${target} PRIVATE example_message_${mode})
			target_compile_definitions(${target} PRIVATE -DZENOH_CPP_EXAMPLE_WITH_PROTOBUF)
		else()
			message("Protobuf not found, will build without Protobuf example!")
		endif()
	endif()
endfunction()

function(add_example file mode lib)
	get_filename_component(filename ${file} NAME_WE)
	set(target ${filename}_${mode})
	add_executable(${target} EXCLUDE_FROM_ALL ${file})
	set_target_properties(${target} PROPERTIES 
		OUTPUT_NAME ${filename}
		RUNTIME_OUTPUT_DIRECTORY ${mode})
	add_dependencies(examples_${mode} ${target})
	add_dependencies(${target} ${lib})
    target_link_libraries(${target} PUBLIC ${lib})
	if("${target}" MATCHES "z_bytes_*")
		add_protobuf(${target} ${mode})
	endif()
	copy_dlls(${target})
endfunction()

function(add_examples glob mode lib)
	file(GLOB files ${glob})
	foreach(file ${files})
		if(("${mode}" STREQUAL "zenohc"))
			# Exclude SHM examples if SHM feature is disabled
			if((${file} MATCHES "^.*_shm.*$") AND NOT(ZENOHC_BUILD_WITH_SHARED_MEMORY AND (ZENOHC_BUILD_WITH_UNSTABLE_API)))
				continue()
			endif()
			if(((${file} MATCHES "^.*advanced_sub.*$") OR (${file} MATCHES "^.*advanced_pub.*$")) AND NOT(ZENOHC_BUILD_WITH_UNSTABLE_API))
				continue()
			endif()
		endif()
		if("${mode}" STREQUAL "zenohpico")
			if ((${file} MATCHES "^.*advanced_pub.*$") AND NOT(ZENOHPICO_FEATURE_ADVANCED_PUBLICATION))
				continue()
			elseif ((${file} MATCHES "^.*advanced_sub.*$") AND NOT(ZENOHPICO_FEATURE_ADVANCED_SUBSCRIPTION))
				continue()
			elseif (((${file} MATCHES "^.*pub.*$") OR (${file} MATCHES "^.*delete.*$") OR (${file} MATCHES "^.*put.*$")
				OR (${file} MATCHES "^.*ping.*$") OR (${file} MATCHES "^.*pong.*$"))
				AND NOT(ZENOHPICO_FEATURE_PUBLICATION)
			)
				continue()
			elseif (((${file} MATCHES "^.*sub.*$") OR (${file} MATCHES "^.*ping.*$") OR (${file} MATCHES "^.*pong.*$")) 
				AND NOT(ZENOHPICO_FEATURE_SUBSCRIPTION)
			)
				continue()
			elseif ((${file} MATCHES "^.*get.*$") AND NOT(ZENOHPICO_FEATURE_QUERY))
				continue()
			elseif ((${file} MATCHES "^.*queryable.*$") AND NOT(ZENOHPICO_FEATURE_QUERYABLE))
				continue()
			elseif ((${file} MATCHES "^.*liveliness.*$") AND NOT(ZENOHPICO_FEATURE_LIVELINESS))
				continue()
			elseif ((${file} MATCHES "^.*querier.*$") AND NOT(ZENOHPICO_FEATURE_QUERY))
				continue()
			endif()
		endif()

		add_example(${file} ${mode} ${lib})
	endforeach()
endfunction()

if(ZENOHCXX_ZENOHC)
	# zenohcxx examples compiled with C++ compiler with zenohc
	add_examples("${CMAKE_CURRENT_SOURCE_DIR}/zenohc/*.cxx" zenohc zenohcxx::zenohc)
	add_examples("${CMAKE_CURRENT_SOURCE_DIR}/universal/*.cxx" zenohc zenohcxx::zenohc)
endif()
if(ZENOHCXX_ZENOHPICO)
	# zenohcxx examples compiled with C++ compiler with zenohpico
	add_examples("${CMAKE_CURRENT_SOURCE_DIR}/universal/*.cxx" zenohpico zenohcxx::zenohpico)
endif()

# check compilation of simple examples
#add_examples("${CMAKE_CURRENT_SOURCE_DIR}/simple/universal/z_simple.cxx" zenohpico zenohcxx::zenohpico)
#add_examples("${CMAKE_CURRENT_SOURCE_DIR}/simple/universal/z_simple.cxx" zenohc zenohcxx::zenohc::lib)
#add_examples("${CMAKE_CURRENT_SOURCE_DIR}/simple/zenohpico/zp_simple.cxx" zenohpico zenohcxx::zenohpico)
#add_examples("${CMAKE_CURRENT_SOURCE_DIR}/simple/zenohc/zc_simple.cxx" zenohc zenohcxx::zenohc::lib)

---

# Zenoh CPP examples

## Start instructions

   Depending on the backend used, the examples will be available either in `examples/zenohc` or `examples/zenohpico` (or in both, if zenoh-cpp is built for both backends) in the build directory.

   Each example accepts the `-h` or `--help` option that provides a description of its arguments and their default values.

   `zenohc` examples can work standalone, but for `zenohpico` examples the working zenoh router is required, so you will need to download [zenoh](https://github.com/eclipse-zenoh/zenoh) project and run the router ([Rust](https://www.rust-lang.org) should be installed):

   ```bash
   git clone https://github.com/eclipse-zenoh/zenoh
   cd zenoh
   cargo run
   ```

   If you run the tests against the Zenoh router running in a Docker container, you need to add the
   `-e tcp/localhost:7447` option to your examples. That's because Docker doesn't support UDP multicast
   transport, and therefore the Zenoh scouting and discovery mechanism cannot work with.

## Examples description

Note: few examples might not be available under one of the backends, due to unsupportrd APIs.

### z_scout

   Scouts for Zenoh peers and routers available on the network.

   Typical usage:

   ```bash
   z_scout
   ```

### z_info

   Gets information about the Zenoh session.

   Typical usage:

   ```bash
   z_info
   ```

### z_put

   Puts a path/value into Zenoh.
   The path/value will be received by all matching subscribers, for instance the [z_sub](#z_sub)
   and [z_storage](#z_storage) examples.

   Typical usage:

   ```bash
   z_put
   ```

   or

   ```bash
   z_put -k demo/example/test -v 'Hello World'
   ```

### z_pub

   Declares a key expression and a publisher. Then writes values periodically on the declared key expression.
   The published value will be received by all matching subscribers, for instance the [z_sub](#z_sub) and [z_storage](#z_storage) examples.

   Typical usage:

   ```bash
   z_pub
   ```

   or

   ```bash
   z_pub -k demo/example/test -v 'Hello World'
   ```

### z_sub

   Declares a key expression and a subscriber.
   The subscriber will be notified of each `put` or `delete` made on any key expression matching the subscriber key expression, and will print this notification.

   Typical usage:

   ```bash
   z_sub
   ```

   or

   ```bash
   z_sub -k 'demo/**'
   ```

### z_pull

   Declares a key expression and a pull subscriber.  
   On each pull, the pull subscriber will be notified of the last N `put` or `delete` made on each key expression matching the subscriber key expression, and will print this notification.

   Typical usage:

   ```bash
   z_pull
   ```

   or

   ```bash
   z_pull -k demo/** --size 3
   ```

### z_get, z_get_channel and z_get_channel_non_blocking

   Sends a query message for a selector.
   The queryables with a matching path or selector (for instance [z_queryable](#z_queryable) and [z_storage](#z_storage))
   will receive this query and reply with paths/values that will be received by the receiver stream.

   Typical usage:

   ```bash
   z_get
   ```

   or

   ```bash
   z_get -s 'demo/**'
   ```

### z_querier

   Continuously sends query messages for a selector.
   The queryables with a matching path or selector (for instance [z_queryable](#z_queryable) and [z_storage](#z_storage))
   will receive these queries and reply with paths/values that will be received by the querier.

   Typical usage:

   ```bash
   z_querier
   ```

   or

   ```bash
   z_querier -s 'demo/**'
   ```

### z_queryable

   Declares a queryable function with a path.
   This queryable function will be triggered by each call to get
   with a selector that matches the path, and will return a value to the querier.

   Typical usage:

   ```bash
   z_queryable
   ```

   or

   ```bash
   z_queryable -k demo/example/queryable -v 'This is the result'
   ```

### z_storage

   Trivial implementation of a storage in memory.
   This example declares a subscriber and a queryable on the same selector.
   The subscriber callback will store the received paths/values in a hashmap.
   The queryable callback will answer to queries with the paths/values stored in the hashmap
   and that match the queried selector.

   Typical usage:

   ```bash
   z_storage
   ```

   or

   ```bash
   z_storage -k 'demo/**'
   ```

### z_pub_shm & z_sub

   A pub/sub example involving the shared-memory feature.
   Note that on subscriber side, the same `z_sub` example than for non-shared-memory example is used.

   Typical Subscriber usage:

   ```bash
   z_sub
   ```

   Typical Publisher usage:

   ```bash
   z_pub_shm
   ```

### z_pub_thr & z_sub_thr

   Pub/Sub throughput test.
   This example allows performing throughput measurements between a publisher performing
   put operations and a subscriber receiving notifications of those puts.

   Typical Subscriber usage:

   ```bash
   z_sub_thr
   ```

   Typical Publisher usage:

   ```bash
   z_pub_thr 1024
   ```

### z_ping & z_pong

   Pub/Sub roundtrip time test.
   This example allows performing roundtrip time measurements. The z_ping example
   performs a put operation on a first key expression, waits for a reply from the pong
   example on a second key expression and measures the time between the two.
   The pong application waits for samples on the first key expression and replies by
   writing back the received data on the second key expression.

  :warning: z_pong needs to start first to avoid missing the kickoff from z_ping.

   Typical Pong usage:

   ```bash
   z_pong
   ```

   Typical Ping usage:

   ```bash
   z_ping 1024
   ```

### z_pub_shm_thr & z_sub_thr

   Pub/Sub throughput test involving the shared-memory feature.
   This example allows performing throughput measurements between a publisher performing
   put operations with the shared-memory feature and a subscriber receiving notifications
   of those puts.
   Note that on subscriber side, the same `z_sub_thr` example than for non-shared-memory example is used.

   Typical Subscriber usage:

   ```bash
   z_sub_thr
   ```

   Typical Publisher usage:

   ```bash
   z_pub_shm_thr
   ```

### z_liveliness

   Declares a liveliness token on a given key expression (`group1/zenoh-rs` by default).
   This token will be seen alive by the `z_get_liveliness` and `z_sub_liveliness` until
   user explicitly drops the token by pressing `'d'` or implicitly dropped by terminating
   or killing the `z_liveliness` example.

   Typical usage:

   ```bash
   z_liveliness
   ```

   or

   ```bash
   z_liveliness -k 'group1/member1'
   ```

### z_get_liveliness

   Queries all the currently alive liveliness tokens that match a given key expression
   (`group1/**` by default). Those tokens could be declared by the `z_liveliness` example.

   Typical usage:

   ```bash
   z_get_liveliness
   ```

   or

   ```bash
   z_get_liveliness -k 'group1/**'
   ```

### z_sub_liveliness

   Subscribe to all liveliness changes (liveliness tokens getting alive or
   liveliness tokens being dropped) that match a given key expression
   (`group1/**` by default). Those tokens could be declared by the `z_liveliness`
   example.
   Note: the `z_sub_liveliness` example will not receive information about
   matching liveliness tokens that were alive before it's start.

   Typical usage:

   ```bash
   z_sub_liveliness
   ```

   or

   ```bash
   z_sub_liveliness -k 'group1/**'
   ```

### z_bytes

   Show how to serialize different message types into ZBytes, and then deserialize from ZBytes to the original message types.

---

# Simple CMake projects demonstrating usage of zenoh-cpp

* [universal](universal) - Use same C++ source for both zenoh-c and zenoh-pico
* [zenohc](zenohc) - Explicitly use Zenoh-C library
* [zenohpico](zenohpico) - Explicitly use Zenoh-Pico library

---

cmake_minimum_required(VERSION 3.16)
project(zenohcxx_examples LANGUAGES C CXX)

set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../../../cmake" ${CMAKE_MODULE_PATH})
include(helpers)

if(CMAKE_BUILD_TYPE STREQUAL "")
    set(CMAKE_BUILD_TYPE Release)
endif()

find_package(zenohpico REQUIRED)
find_package(zenohc REQUIRED)
find_package(zenohcxx REQUIRED)

add_executable(zp_simple z_simple.cxx)
target_link_libraries(zp_simple PRIVATE zenohcxx::zenohpico)
set_property(TARGET zp_simple PROPERTY LANGUAGE CXX)
set_property(TARGET zp_simple PROPERTY CXX_STANDARD 17)
copy_dlls(zp_simple)

add_executable(zc_simple z_simple.cxx)
target_link_libraries(zc_simple PRIVATE zenohcxx::zenohc)
set_property(TARGET zc_simple PROPERTY LANGUAGE CXX)
set_property(TARGET zc_simple PROPERTY CXX_STANDARD 17)
copy_dlls(zc_simple)

---

cmake_minimum_required(VERSION 3.16)
project(zenohcxx_examples LANGUAGES C CXX)
set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../../../cmake" ${CMAKE_MODULE_PATH})
include(helpers)

if(CMAKE_BUILD_TYPE STREQUAL "")
    set(CMAKE_BUILD_TYPE Release)
endif()

find_package(zenohc REQUIRED)
find_package(zenohcxx REQUIRED)

add_executable(zc_simple zc_simple.cxx)
target_link_libraries(zc_simple PRIVATE zenohcxx::zenohc)
set_property(TARGET zc_simple PROPERTY LANGUAGE CXX)
set_property(TARGET zc_simple PROPERTY CXX_STANDARD 17)
copy_dlls(zc_simple)

---

cmake_minimum_required(VERSION 3.16)
project(zenohcxx_examples LANGUAGES C CXX)

set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../../../cmake" ${CMAKE_MODULE_PATH})
include(helpers)

if(CMAKE_BUILD_TYPE STREQUAL "")
    set(CMAKE_BUILD_TYPE Release)
endif()

find_package(zenohpico REQUIRED)
find_package(zenohcxx REQUIRED)

add_executable(zp_simple zp_simple.cxx)
target_link_libraries(zp_simple PRIVATE zenohcxx::zenohpico)
set_property(TARGET zp_simple PROPERTY LANGUAGE CXX)
set_property(TARGET zp_simple PROPERTY CXX_STANDARD 17)
copy_dlls(zp_simple)

---

