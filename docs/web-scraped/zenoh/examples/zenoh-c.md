# Zenoh Examples: zenoh-c

if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_SOURCE_DIR})
    # Settings when 'examples' is the root projet
    cmake_minimum_required(VERSION 3.16)
    project(zenohc_examples LANGUAGES C)
    set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../cmake" ${CMAKE_MODULE_PATH})
    include(helpers)
    find_package(zenohc REQUIRED)
    add_custom_target(examples ALL)
else()
    message(STATUS "zenoh-c examples")
    add_custom_target(examples)
endif()

file(GLOB files "${CMAKE_CURRENT_SOURCE_DIR}/*.c")

foreach(file ${files})
    get_filename_component(target ${file} NAME_WE)
    # Exclude SHM examples if SHM feature is disabled
    if(NOT(ZENOHC_BUILD_WITH_SHARED_MEMORY AND (ZENOHC_BUILD_WITH_UNSTABLE_API)))
        if(${target} MATCHES "^.*_shm.*$")
            continue()
        endif()
    endif()
    # Exclude Liveliness and zenoh-ext examples if unstable api feature is disabled
    if(NOT(ZENOHC_BUILD_WITH_UNSTABLE_API))
        if(
            (${target} MATCHES "^.*_advanced_sub.*$")
            OR (${target} MATCHES "^.*_advanced_pub.*$") 
        )
            continue()
        endif()
    endif()

    add_executable(${target} EXCLUDE_FROM_ALL ${file})
    add_dependencies(examples ${target})

    add_dependencies(${target} zenohc::lib)
    target_link_libraries(${target} PRIVATE zenohc::lib)
    copy_dlls(${target})

    set_property(TARGET ${target} PROPERTY C_STANDARD 11)
endforeach()

---

# examples--parse_args.h

```cpp
//
// Copyright (c) 2024 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "zenoh.h"

#define COMMON_HELP \
    "\
        -c, --config <CONFIG> (optional, string): The path to a configuration file for the session. If this option isn't passed, the default configuration will be used.\n\
        -m, --mode <MODE> (optional, string, default='peer'): The zenoh session mode. [possible values: peer, client, router]\n\
        -e, --connect <CONNECT> (optional, string): Endpoint to connect to. Repeat option to pass multiple endpoints. If none are given, endpoints will be discovered through multicast-scouting if it is enabled.\n\
            e.g.: '-e tcp/192.168.1.1:7447'\n\
        -l, --listen <LISTEN> (optional, string): Locator to listen on. Repeat option to pass multiple locators. If none are given, the default configuration will be used.\n\
            e.g.: '-l tcp/192.168.1.1:7447'\n\
        --no-multicast-scouting (optional): By default zenohd replies to multicast scouting messages for being discovered by peers and clients. This option disables this feature.\n\
        --cfg (optional, string): Allows arbitrary configuration changes as column-separated KEY:VALUE pairs. Where KEY must be a valid config path and VALUE must be a valid JSON5 string that can be deserialized to the expected type for the KEY field. Example: --cfg='transport/unicast/max_links:2'.\n\
        -h, --help: Print help\n\
"
#define _Z_PARSE_ARG(VALUE, ID_SHORT, ID_LONG, FUNC, DEFAULT_VALUE)  \
    do {                                                             \
        const char* arg_val = parse_opt(argc, argv, ID_SHORT, true); \
        if (!arg_val) {                                              \
            arg_val = parse_opt(argc, argv, ID_LONG, true);          \
        }                                                            \
        if (!arg_val) {                                              \
            VALUE = DEFAULT_VALUE;                                   \
        } else {                                                     \
            VALUE = FUNC(arg_val);                                   \
        }                                                            \
    } while (0)

#define _Z_PARSE_ARG_SINGLE_OPT(VALUE, ID, FUNC, DEFAULT_VALUE) \
    do {                                                        \
        const char* arg_val = parse_opt(argc, argv, ID, true);  \
        if (!arg_val) {                                         \
            VALUE = DEFAULT_VALUE;                              \
        } else {                                                \
            VALUE = FUNC(arg_val);                              \
        }                                                       \
    } while (0)

#define _Z_CHECK_HELP                                                                    \
    do {                                                                                 \
        if (parse_opt(argc, argv, "h", false) || parse_opt(argc, argv, "help", false)) { \
            print_help();                                                                \
            exit(1);                                                                     \
        }                                                                                \
    } while (0)

#define _Z_CHECK_FLAG(ID) (parse_opt(argc, argv, ID, false) != NULL)

/**
 * Parse an option of format `-f`, `--flag`, `-f <value>` or `--flag <value>` from `argv`. If found, the option and its
 * eventual value are each replaced by NULL in `argv`
 * @param argc: argc passed from `main` function
 * @param argv: argv passed from `main` function
 * @param opt: option to parse (without `-` or `--` prefix)
 * @param opt_has_value: if true, the option is of format `-f <value>` or `--flag <value>` and `value` will be returned
 * if found, else an error message is printed and program will exit. If false, option has no value and a non-null
 * pointer will be returned if option is found.
 * @returns NULL if option was not found, else a non-null value depending on if `opt_has_value`.
 */
const char* parse_opt(int argc, char** argv, const char* opt, bool opt_has_value) {
    size_t optlen = strlen(opt);
    char* value = NULL;
    for (int i = 1; i < argc; i++) {
        if (argv[i] == NULL) {
            continue;
        }
        size_t len = strlen(argv[i]);
        if (len < 2) {
            continue;
        }
        if (optlen == 1) {
            if (argv[i][0] == '-' && argv[i][1] == opt[0] && argv[i][2] == 0) {
                argv[i] = NULL;
                if (!opt_has_value) {
                    return (char*)opt;
                } else if (i + 1 < argc && argv[i + 1]) {
                    value = argv[i + 1];
                    argv[i + 1] = NULL;
                    return value;
                } else {
                    printf("Option -%s given without a value\n", opt);
                    exit(-1);
                }
            }
        } else if (optlen > 1 && len > 3 && argv[i][0] == '-' && argv[i][1] == '-') {
            if (strncmp(argv[i] + 2, opt, optlen) == 0) {
                char* pos = strchr(argv[i], '=');
                if (!opt_has_value) {
                    argv[i] = NULL;
                    return (char*)opt;
                } else if (pos != NULL) {
                    value = pos + 1;
                    argv[i] = NULL;
                    return value;
                } else if (i + 1 < argc && argv[i + 1]) {
                    argv[i] = NULL;
                    value = argv[i + 1];
                    argv[i + 1] = NULL;
                    return value;
                } else {
                    printf("Option --%s given without a value\n", opt);
                    exit(-1);
                }
            }
        }
    }
    return NULL;
}

/**
 * Check if any options remains in `argv`. Must be called after all expected options are parsed
 * @param argc
 * @param argv
 * @returns NULL if no option was found, else the first option string that was found
 */
const char* check_unknown_opts(int argc, char** const argv) {
    for (int i = 1; i < argc; i++) {
        if (argv[i] && argv[i][0] == '-') {
            return argv[i];
        }
    }
    return NULL;
}

/**
 * Parse positional arguments from `argv`. Must be called after all expected options are parsed, and after checking that
 * no unknown options remain in `argv`
 * @param argc
 * @param argv
 * @param nb_args: number of expected positional arguments
 * @returns NULL if found more positional arguments than `nb_args`. Else an array of found arguments in order, followed
 * by NULL values if found less positional arguments than `nb_args`
 * @note Returned pointer is dynamically allocated and must be freed
 */
char** parse_pos_args(const int argc, char** argv, const size_t nb_args) {
    char** pos_argv = (char**)calloc(nb_args, sizeof(char*));
    size_t pos_argc = 0;
    for (int i = 1; i < argc; i++) {
        if (argv[i]) {
            pos_argc++;
            if (pos_argc > nb_args) {
                free(pos_argv);
                return NULL;
            }
            pos_argv[pos_argc - 1] = argv[i];
        }
    }
    return pos_argv;
}

/**
 * Parse zenoh options that require a JSON-serialized list (-e, -l from common args) and add them to
 * `config`. Prints error message and exits if fails to insert parsed values
 * @param argc
 * @param argv
 * @param opt: option to parse (without `-` or `--` prefix)
 * @param config: address of an owned zenoh configuration
 * @param config_key: zenoh configuration key under which the parsed values will be inserted
 */
void parse_zenoh_json_list_config(int argc, char** argv, const char* opt_short, const char* opt_long,
                                  const char* config_key, z_owned_config_t* config) {
    char* buf = (char*)calloc(1, sizeof(char));
    const char* value;
    _Z_PARSE_ARG(value, opt_short, opt_long, (const char*), NULL);
    while (value) {
        size_t len_newbuf = strlen(buf) + strlen(value) + 4;  // value + quotes + comma + nullbyte
        char* newbuf = (char*)malloc(len_newbuf);
        snprintf(newbuf, len_newbuf, "%s'%s',", buf, value);
        free(buf);
        buf = newbuf;
        _Z_PARSE_ARG(value, opt_short, opt_long, (const char*), NULL);
    }
    size_t buflen = strlen(buf);
    if (buflen > 0) {
        // remove trailing comma
        buf[buflen - 1] = '\0';
        buflen--;
        // add list delimiters
        size_t json_list_len = buflen + 3;  // buf + brackets + nullbyte
        char* json_list = (char*)malloc(json_list_len);
        snprintf(json_list, json_list_len, "[%s]", buf);
        // insert in config
        if (zc_config_insert_json5(z_loan_mut(*config), config_key, json_list) < 0) {
            printf(
                "Couldn't insert value `%s` in configuration at `%s`\n`%s` is either not a JSON-serialized list of "
                "strings, or values within the list do not respect expected format for `%s`\n",
                json_list, config_key, json_list, config_key);
            free(json_list);
            exit(-1);
        }
        free(json_list);
    }
    free(buf);
}

void parse_zenoh_json_list_cfg(int argc, char** argv, const char* opt_long, z_owned_config_t* config) {
    char* buf = (char*)calloc(1, sizeof(char));
    const char* value;
    _Z_PARSE_ARG_SINGLE_OPT(value, opt_long, (char*), NULL);
    while (value) {
        char* pos = strchr(value, ':');
        if (pos == NULL) {
            printf("--cfg` argument: expected KEY:VALUE pair, got %s ", value);
            exit(-1);
        }
        *pos = 0;
        const char* key = value;
        const char* val = pos + 1;
        if (zc_config_insert_json5(z_loan_mut(*config), key, val) < 0) {
            printf("Couldn't insert value `%s` in configuration at `%s`\n", key, val);
            exit(-1);
        }
        _Z_PARSE_ARG_SINGLE_OPT(value, opt_long, (char*), NULL);
    }
}

/**
 * Parse zenoh options that are common to all examples (-c, -m, -e, -l, --no-multicast-scouting) and add them to
 * `config`
 * @param argc
 * @param argv
 * @param config: address of an owned zenoh configuration
 */
void parse_zenoh_common_args(const int argc, char** argv, z_owned_config_t* config) {
    // -c, --config: A configuration file.
    const char* config_file;
    _Z_PARSE_ARG(config_file, "c", "config", (const char*), NULL);
    if (config_file) {
        zc_config_from_file(config, config_file);
    } else {
        z_config_default(config);
    }
    // -m: The Zenoh session mode [default: peer].
    const char* mode;
    _Z_PARSE_ARG(mode, "m", "mode", (const char*), NULL);
    if (mode) {
        size_t buflen = strlen(mode) + 3;  // mode + quotes + nullbyte
        char* buf = (char*)malloc(buflen);
        snprintf(buf, buflen, "'%s'", mode);
        if (zc_config_insert_json5(z_loan_mut(*config), Z_CONFIG_MODE_KEY, buf) < 0) {
            printf(
                "Couldn't insert value `%s` in configuration at `%s`. Value must be one of: 'client', 'peer' or "
                "'router'\n",
                mode, Z_CONFIG_MODE_KEY);
            free(buf);
            exit(-1);
        }
        free(buf);
    }
    // -e: Endpoint to connect to. Can be repeated
    parse_zenoh_json_list_config(argc, argv, "e", "connect", Z_CONFIG_CONNECT_KEY, config);
    // -l: Endpoint to listen on. Can be repeated
    parse_zenoh_json_list_config(argc, argv, "l", "listen", Z_CONFIG_LISTEN_KEY, config);
    // -cfg: Config entires. Can be repeated
    parse_zenoh_json_list_cfg(argc, argv, "cfg", config);
    // --no-multicast-scrouting: Disable the multicast-based scouting mechanism.
    bool no_multicast_scouting = _Z_CHECK_FLAG("no-multicast-scouting");
    if (no_multicast_scouting &&
        zc_config_insert_json5(z_loan_mut(*config), Z_CONFIG_MULTICAST_SCOUTING_KEY, "false") < 0) {
        printf("Couldn't disable multicast-scouting.\n");
        exit(-1);
    }
}

z_query_target_t parse_query_target(const char* arg) {
    if (strcmp(arg, "BEST_MATCHING") == 0) {
        return Z_QUERY_TARGET_BEST_MATCHING;
    } else if (strcmp(arg, "ALL") == 0) {
        return Z_QUERY_TARGET_ALL;
    } else if (strcmp(arg, "ALL_COMPLETE") == 0) {
        return Z_QUERY_TARGET_ALL_COMPLETE;
    } else {
        printf("Unsupported query target value [%s]\n", arg);
        exit(-1);
    }
}

z_priority_t parse_priority(const char* arg) {
    int p = atoi(arg);
    if (p < Z_PRIORITY_REAL_TIME || p > Z_PRIORITY_BACKGROUND) {
        printf("Unsupported priority value [%s]\n", arg);
        exit(-1);
    }
    return (z_priority_t)p;
}
```

---

# Zenoh C examples

## Start instructions

   When Zenoh is built in release mode:

   ```bash
   ./target/release/example/<example_name>
   ```

   Each example accepts the `-h` or `--help` option that provides a description of its arguments and their default values.

   If you run the tests against the Zenoh router running in a Docker container, you need to add the
   `-e tcp/localhost:7447` option to your examples. That's because Docker doesn't support UDP multicast
   transport, and therefore the Zenoh scouting and discovery mechanism cannot work with.

## Examples description

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
   z_put -k demo/example/test -p 'Hello World'
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
   z_pub -k demo/example/test -p 'Hello World'
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

### z_get

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
   z_queryable -k demo/example/queryable -p 'This is the result'
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

# Example: examples--z_advanced_pub.c

```c
//
// Copyright (c) 2024 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-pub"
#define DEFAULT_VALUE "Pub from C!"
#define DEFAULT_HISTORY 1

struct args_t {
    char* keyexpr;   // -k, --key
    char* value;     // -p, --payload
    size_t history;  // -i, --history
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    if (zc_config_insert_json5(z_loan_mut(config), Z_CONFIG_ADD_TIMESTAMP_KEY, "true") < 0) {
        printf("Unable to configure timestamps!\n");
        exit(-1);
    }

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Declaring AdvancedPublisher on '%s'...\n", args.keyexpr);
    ze_owned_advanced_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);

    ze_advanced_publisher_options_t pub_opts;
    ze_advanced_publisher_options_default(&pub_opts);
    ze_advanced_publisher_cache_options_default(&pub_opts.cache);  // or pub_opts.cache.is_enabled = true;
    pub_opts.cache.max_samples = args.history;
    pub_opts.publisher_detection = true;
    ze_advanced_publisher_sample_miss_detection_options_default(&pub_opts.sample_miss_detection);
    // or pub_opts.sample_miss_detection = true
    pub_opts.sample_miss_detection.heartbeat_period_ms = 500;
    pub_opts.sample_miss_detection.heartbeat_mode = ZE_ADVANCED_PUBLISHER_HEARTBEAT_MODE_PERIODIC;
    // if not set, publisher will retransmit samples based on periodic queries from advanced subscriber

    if (ze_declare_advanced_publisher(z_loan(s), &pub, z_loan(ke), &pub_opts) < 0) {
        printf("Unable to declare AdvancedPublisher for key expression!\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    char buf[256] = {0};
    for (int idx = 0; 1; ++idx) {
        z_sleep_s(1);
        sprintf(buf, "[%4d] %s", idx, args.value);
        printf("Put Data ('%s': '%s')...\n", args.keyexpr, buf);
        ze_advanced_publisher_put_options_t options;
        ze_advanced_publisher_put_options_default(&options);

        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, buf);
        ze_advanced_publisher_put(z_loan(pub), z_move(payload), &options);
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_advanced_pub [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to write to\n\
        -p, --payload <PAYLOAD> (optional, string, default='%s'): The value to write\n\
        -i, --history <HISTORY_SIZE> (optional, string, default=%d): The number of publications to keep in cache\n",
        DEFAULT_KEYEXPR, DEFAULT_VALUE, DEFAULT_HISTORY);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    _Z_PARSE_ARG(args.history, "i", "hisotry", atoi, DEFAULT_HISTORY);

    parse_zenoh_common_args(argc, argv, config);
    const char* unknown_arg = check_unknown_opts(argc, argv);
    if (unknown_arg) {
        printf("Unknown option %s\n", unknown_arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_advanced_sub.c

```c
//
// Copyright (c) 2024 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/**"

struct args_t {
    char* keyexpr;  // -k, --key
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

const char* kind_to_str(z_sample_kind_t kind);

void data_handler(z_loaned_sample_t* sample, void* arg) {
    z_view_string_t key_string;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_string);
    z_owned_string_t payload_string;
    z_bytes_to_string(z_sample_payload(sample), &payload_string);

    printf(">> [Subscriber] Received %s ('%.*s': '%.*s')\n", kind_to_str(z_sample_kind(sample)),
           (int)z_string_len(z_loan(key_string)), z_string_data(z_loan(key_string)),
           (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)));
    z_drop(z_move(payload_string));
}

void miss_handler(const ze_miss_t* miss, void* arg) {
    z_id_t id = z_entity_global_id_zid(&miss->source);
    z_owned_string_t id_string;
    z_id_to_string(&id, &id_string);
    printf(">> [Subscriber] Missed %d samples from '%.*s' !!!", miss->nb, (int)z_string_len(z_loan(id_string)),
           z_string_data(z_loan(id_string)));
    z_drop(z_move(id_string));
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);

    ze_advanced_subscriber_options_t sub_opts;
    ze_advanced_subscriber_options_default(&sub_opts);
    ze_advanced_subscriber_history_options_default(&sub_opts.history);  // or sub_opts.history.is_enabled = true;
    sub_opts.history.detect_late_publishers = true;
    ze_advanced_subscriber_recovery_options_default(&sub_opts.recovery);  // or sub_opts.recovery.is_enabled = true;
    ze_advanced_subscriber_last_sample_miss_detection_options_default(&sub_opts.recovery.last_sample_miss_detection);
    // or sub_opts.recovery.last_sample_miss_detection.is_enabled = true;
    // use publisher heartbeats by default, otherwise enable periodic queries as follows:
    // sub_opts.recovery.last_sample_miss_detection.periodic_queries_period_ms = 1000;
    sub_opts.subscriber_detection = true;

    z_owned_closure_sample_t callback;
    z_closure(&callback, data_handler, NULL, NULL);
    printf("Declaring AdvancedSubscriber on '%s'...\n", args.keyexpr);
    ze_owned_advanced_subscriber_t sub;
    if (ze_declare_advanced_subscriber(z_loan(s), &sub, z_loan(ke), z_move(callback), &sub_opts) < 0) {
        printf("Unable to declare advanced subscriber.\n");
        exit(-1);
    }
    ze_owned_closure_miss_t miss_callback;
    z_closure(&miss_callback, miss_handler, NULL, NULL);
    ze_advanced_subscriber_declare_background_sample_miss_listener(z_loan(sub), z_move(miss_callback));

    printf("Press CTRL-C to quit...\n");
    while (1) {
        z_sleep_s(1);
    }

    z_drop(z_move(sub));
    z_drop(z_move(s));

    return 0;
}

const char* kind_to_str(z_sample_kind_t kind) {
    switch (kind) {
        case Z_SAMPLE_KIND_PUT:
            return "PUT";
        case Z_SAMPLE_KIND_DELETE:
            return "DELETE";
        default:
            return "UNKNOWN";
    }
}

void print_help() {
    printf(
        "\
    Usage: z_advanced_sub [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to subscribe to\n",
        DEFAULT_KEYEXPR);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_bytes.c

```c
//
// Copyright (c) 2024 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zenoh.h>

#undef NDEBUG
#include <assert.h>

typedef struct custom_struct_t {
    float f;
    uint64_t u[2][3];
    const char *c;
} custom_struct_t;

typedef struct kv_pair_t {
    int32_t key;
    z_owned_string_t value;
} kv_pair_t;

static void print_slice_data(z_view_slice_t *slice);

int main(void) {
    // Wrapping raw data into z_bytes_t
    z_owned_bytes_t payload;
    {
        const uint8_t input_bytes[] = {1, 2, 3, 4};
        z_owned_slice_t output_bytes;
        z_bytes_copy_from_buf(&payload, input_bytes, sizeof(input_bytes));
        z_bytes_to_slice(z_loan(payload), &output_bytes);
        assert(memcmp(input_bytes, z_slice_data(z_loan(output_bytes)), z_slice_len(z_loan(output_bytes))) == 0);
        z_drop(z_move(payload));
        z_drop(z_move(output_bytes));
        // Corresponding encoding to be used in operations options like `z_put()`, `z_get()`, etc.
        // const z_loaned_encoding* encoding = z_encoding_zenoh_bytes();

        // The same can be done for const char*
        const char *input_str = "test";
        z_owned_string_t output_string;
        z_bytes_copy_from_str(&payload, input_str);
        z_bytes_to_string(z_loan(payload), &output_string);
        assert(strncmp(input_str, z_string_data(z_loan(output_string)), z_string_len(z_loan(output_string))) == 0);
        z_drop(z_move(payload));
        z_drop(z_move(output_string));
        // Corresponding encoding to be used in operations options like `z_put()`, `z_get()`, etc.
        // const z_loaned_encoding* encoding = z_encoding_zenoh_string();
    }

    // Serialization
    {
        // Arithmetic types: uint8, uint16, uint32, uint64, int8, int16, int32, int64, float, double
        uint32_t input_u32 = 1234;
        uint32_t output_u32 = 0;
        ze_serialize_uint32(&payload, input_u32);
        ze_deserialize_uint32(z_loan(payload), &output_u32);
        assert(input_u32 == output_u32);
        z_drop(z_move(payload));
        // Corresponding encoding to be used in operations options like `z_put()`, `z_get()`, etc.
        // const z_loaned_encoding* encoding = z_encoding_zenoh_serialized();
    }

    // Writer/reader for raw bytes
    {
        uint8_t input_writer[] = {0, 1, 2, 3, 4};
        uint8_t output_reader[5] = {0};
        z_owned_bytes_writer_t writer;
        z_bytes_writer_empty(&writer);
        z_bytes_writer_write_all(z_loan_mut(writer), input_writer, 3);
        z_bytes_writer_write_all(z_loan_mut(writer), input_writer + 3, 2);
        z_bytes_writer_finish(z_move(writer), &payload);
        z_bytes_reader_t reader = z_bytes_get_reader(z_loan(payload));
        z_bytes_reader_read(&reader, output_reader, sizeof(output_reader));
        assert(0 == memcmp(input_writer, output_reader, sizeof(output_reader)));
        z_drop(z_move(payload));
    }

    // Using serializer/deserializer for composite types
    {
        // A sequence of primitive types
        int32_t input_vec[] = {1, 2, 3, 4};
        int32_t output_vec[4] = {0};
        ze_owned_serializer_t serializer;
        ze_serializer_empty(&serializer);
        ze_serializer_serialize_sequence_length(z_loan_mut(serializer), 4);
        for (size_t i = 0; i < 4; ++i) {
            ze_serializer_serialize_int32(z_loan_mut(serializer), input_vec[i]);
        }
        ze_serializer_finish(z_move(serializer), &payload);

        ze_deserializer_t deserializer = ze_deserializer_from_bytes(z_loan(payload));
        size_t num_elements = 0;
        ze_deserializer_deserialize_sequence_length(&deserializer, &num_elements);
        assert(num_elements == 4);
        for (size_t i = 0; i < num_elements; ++i) {
            ze_deserializer_deserialize_int32(&deserializer, &output_vec[i]);
        }

        for (size_t i = 0; i < 4; ++i) {
            assert(input_vec[i] == output_vec[i]);
        }
        z_drop(z_move(payload));
    }

    {
        // Sequence of key-value pairs
        kv_pair_t kvs_input[2];
        kvs_input[0].key = 0;
        z_string_from_str(&kvs_input[0].value, "abc", NULL, NULL);
        kvs_input[1].key = 1;
        z_string_from_str(&kvs_input[1].value, "def", NULL, NULL);

        ze_owned_serializer_t serializer;
        ze_serializer_empty(&serializer);
        ze_serializer_serialize_sequence_length(z_loan_mut(serializer), 2);
        for (size_t i = 0; i < 2; ++i) {
            ze_serializer_serialize_int32(z_loan_mut(serializer), kvs_input[i].key);
            ze_serializer_serialize_string(z_loan_mut(serializer), z_loan(kvs_input[i].value));
        }
        ze_serializer_finish(z_move(serializer), &payload);

        ze_deserializer_t deserializer = ze_deserializer_from_bytes(z_loan(payload));
        size_t num_elements = 0;
        ze_deserializer_deserialize_sequence_length(&deserializer, &num_elements);
        assert(num_elements == 2);
        kv_pair_t kvs_output[2];
        for (size_t i = 0; i < num_elements; ++i) {
            ze_deserializer_deserialize_int32(&deserializer, &kvs_output[i].key);
            ze_deserializer_deserialize_string(&deserializer, &kvs_output[i].value);
        }

        for (size_t i = 0; i < 2; ++i) {
            assert(kvs_input[i].key == kvs_output[i].key);
            assert(strncmp(z_string_data(z_loan(kvs_input[i].value)), z_string_data(z_loan(kvs_output[i].value)),
                           z_string_len(z_loan(kvs_input[i].value))) == 0);
            z_drop(z_move(kvs_input[i].value));
            z_drop(z_move(kvs_output[i].value));
        }
        z_drop(z_move(payload));
    }

    {
        // Custom struct/tuple serializaiton
        custom_struct_t cs = (custom_struct_t){.f = 1.0f, .u = {{1, 2, 3}, {4, 5, 6}}, .c = "test"};

        ze_owned_serializer_t serializer;
        ze_serializer_empty(&serializer);
        ze_serializer_serialize_float(z_loan_mut(serializer), cs.f);
        ze_serializer_serialize_sequence_length(z_loan_mut(serializer), 2);
        for (size_t i = 0; i < 2; ++i) {
            ze_serializer_serialize_sequence_length(z_loan_mut(serializer), 3);
            for (size_t j = 0; j < 3; ++j) {
                ze_serializer_serialize_uint64(z_loan_mut(serializer), cs.u[i][j]);
            }
        }
        ze_serializer_serialize_str(z_loan_mut(serializer), cs.c);
        ze_serializer_finish(z_move(serializer), &payload);

        float f = 0.0f;
        uint64_t u = 0;
        z_owned_string_t c;

        ze_deserializer_t deserializer = ze_deserializer_from_bytes(z_loan(payload));
        ze_deserializer_deserialize_float(&deserializer, &f);
        assert(f == cs.f);
        size_t num_elements0 = 0;
        ze_deserializer_deserialize_sequence_length(&deserializer, &num_elements0);
        assert(num_elements0 == 2);
        for (size_t i = 0; i < 2; ++i) {
            size_t num_elements1 = 0;
            ze_deserializer_deserialize_sequence_length(&deserializer, &num_elements1);
            assert(num_elements1 == 3);
            for (size_t j = 0; j < 3; ++j) {
                ze_deserializer_deserialize_uint64(&deserializer, &u);
                assert(u == cs.u[i][j]);
            }
        }
        ze_deserializer_deserialize_string(&deserializer, &c);
        assert(strncmp(cs.c, z_string_data(z_loan(c)), z_string_len(z_loan(c))) == 0);

        z_drop(z_move(c));
        z_drop(z_move(payload));
    }

    // Slice iterator
    {
        /// fill z_bytes with some data
        z_owned_bytes_t b1, b2, b3;
        z_bytes_from_static_str(&b1, "abc");
        z_bytes_from_static_str(&b2, "def");
        z_bytes_from_static_str(&b3, "hij");
        z_owned_bytes_writer_t writer;
        z_bytes_writer_empty(&writer);
        z_bytes_writer_append(z_loan_mut(writer), z_move(b1));
        z_bytes_writer_append(z_loan_mut(writer), z_move(b2));
        z_bytes_writer_append(z_loan_mut(writer), z_move(b3));
        z_bytes_writer_finish(z_move(writer), &payload);

        z_bytes_slice_iterator_t slice_iter = z_bytes_get_slice_iterator(z_bytes_loan(&payload));
        z_view_slice_t curr_slice;
        while (z_bytes_slice_iterator_next(&slice_iter, &curr_slice)) {
            printf("slice len: %d, slice data: '", (int)z_slice_len(z_view_slice_loan(&curr_slice)));
            print_slice_data(&curr_slice);
            printf("'\n");
        }
        z_drop(z_move(payload));
    }

    return 0;
}

static void print_slice_data(z_view_slice_t *slice) {
    for (size_t i = 0; i < z_slice_len(z_view_slice_loan(slice)); i++) {
        printf("0x%02x ", z_slice_data(z_view_slice_loan(slice))[i]);
    }
}
```

---

# Example: examples--z_delete.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-put"

struct args_t {
    char* keyexpr;  // -k, --key
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Deleting resources matching '%s'...\n", args.keyexpr);
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);
    int res = z_delete(z_loan(s), z_loan(ke), NULL);
    if (res < 0) {
        printf("Delete failed...\n");
    }

    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_delete [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to write to\n",
        DEFAULT_KEYEXPR);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_get_liveliness.c

```c
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "group1/**"
#define DEFAULT_TIMEOUT_MS 10000

struct args_t {
    char* keyexpr;        // -k, --key
    uint64_t timeout_ms;  // -o, --timeout
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    z_view_keyexpr_t keyexpr;
    if (z_view_keyexpr_from_str(&keyexpr, args.keyexpr) < 0) {
        printf("%s is not a valid key expression\n", args.keyexpr);
        exit(-1);
    }

    z_owned_session_t s;
    printf("Opening session...\n");
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Sending liveliness query '%s'...\n", args.keyexpr);
    z_owned_fifo_handler_reply_t handler;
    z_owned_closure_reply_t closure;
    z_fifo_channel_reply_new(&closure, &handler, 16);
    z_liveliness_get_options_t opts;
    z_liveliness_get_options_default(&opts);
    opts.timeout_ms = args.timeout_ms;
    z_liveliness_get(z_loan(s), z_loan(keyexpr), z_move(closure), &opts);
    z_owned_reply_t reply;
    while (z_recv(z_loan(handler), &reply) == Z_OK) {
        if (z_reply_is_ok(z_loan(reply))) {
            const z_loaned_sample_t* sample = z_reply_ok(z_loan(reply));
            z_view_string_t key_str;
            z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_str);
            printf(">> Alive token ('%.*s')\n", (int)z_string_len(z_loan(key_str)), z_string_data(z_loan(key_str)));
        } else {
            printf("Received an error\n");
        }
    }

    z_drop(z_move(reply));
    z_drop(z_move(handler));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_get_liveliness [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to query\n\
        -o, --timeout <TIMEOUT_MS> (optional, number, default = '%d'): Query timeout in milliseconds\n",
        DEFAULT_KEYEXPR, DEFAULT_TIMEOUT_MS);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.timeout_ms, "o", "timeout", atoi, DEFAULT_TIMEOUT_MS);

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_get_shm.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_SELECTOR "demo/example/**"
#define DEFAULT_VALUE NULL
#define DEFAULT_TIMEOUT_MS 10000

struct args_t {
    char* selector;           // -s, --selector
    char* value;              // -p, --payload
    z_query_target_t target;  // -t, --target
    uint64_t timeout_ms;      // -o, --timeout
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");
    z_owned_config_t config;

    struct args_t args = parse_args(argc, argv, &config);
    if (!args.value) {
        args.value = "Get from Rust SHM!";
    }

    const char* ke = args.selector;
    size_t ke_len = strlen(ke);
    const char* params = strchr(args.selector, '?');
    if (params != NULL) {
        ke_len = params - ke;
        params += 1;
    }

    size_t value_len = args.value ? strlen(args.value) : 0;

    z_view_keyexpr_t keyexpr;
    if (z_view_keyexpr_from_substr(&keyexpr, ke, ke_len) < 0) {
        printf("%.*s is not a valid key expression", (int)ke_len, ke);
        exit(-1);
    }

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    // Create SHM Provider
    z_owned_shm_provider_t provider;
    z_shm_provider_default_new(&provider, value_len);

    // Allocate SHM Buffer
    z_buf_layout_alloc_result_t alloc;
    z_shm_provider_alloc(&alloc, z_loan(provider), value_len);
    if (alloc.status != ZC_BUF_LAYOUT_ALLOC_STATUS_OK) {
        printf("Unexpected failure during SHM buffer allocation...");
        return -1;
    }
    // Fill SHM Buffer with data
    uint8_t* data = z_shm_mut_data_mut(z_loan_mut(alloc.buf));
    memcpy(data, args.value, value_len);
    // Convert mutable SHM Buffer into immutable one (to be able to make it's ref copies)
    z_owned_shm_t shm;
    z_shm_from_mut(&shm, z_move(alloc.buf));

    printf("Sending Query '%s'...\n", args.selector);
    z_owned_fifo_handler_reply_t handler;
    z_owned_closure_reply_t closure;
    z_fifo_channel_reply_new(&closure, &handler, 16);

    z_get_options_t opts;
    z_get_options_default(&opts);
    opts.target = args.target;
    opts.timeout_ms = args.timeout_ms;

    z_owned_bytes_t payload;
    if (args.value != NULL) {
        if (z_bytes_from_shm(&payload, z_move(shm)) != Z_OK) {
            printf("Unexpected failure during SHM buffer serialization...\n");
            return -1;
        }
        opts.payload = z_move(payload);
    }
    z_get(z_loan(s), z_loan(keyexpr), params, z_move(closure),
          &opts);  // here, the send is moved and will be dropped by zenoh when adequate
    z_owned_reply_t reply;

    while (z_recv(z_loan(handler), &reply) == Z_OK) {
        if (z_reply_is_ok(z_loan(reply))) {
            const z_loaned_sample_t* sample = z_reply_ok(z_loan(reply));

            z_view_string_t key_str;
            z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_str);

            z_owned_string_t reply_str;
            z_bytes_to_string(z_sample_payload(sample), &reply_str);

            printf(">> Received ('%.*s': '%.*s')\n", (int)z_string_len(z_loan(key_str)), z_string_data(z_loan(key_str)),
                   (int)z_string_len(z_loan(reply_str)), z_string_data(z_loan(reply_str)));
            z_drop(z_move(reply_str));
        } else {
            printf("Received an error\n");
        }
        z_drop(z_move(reply));
    }

    z_drop(z_move(handler));
    z_drop(z_move(s));

    z_drop(z_move(shm));
    z_drop(z_move(provider));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_get [OPTIONS]\n\n\
    Options:\n\
        -s, --selector <SELECTOR> (optional, string, default='%s'): The selection of resources to query\n\
        -p, --payload <PAYLOAD> (optional, string): An optional value to put in the query\n\
        -t, --target <TARGET> (optional, BEST_MATCHING | ALL | ALL_COMPLETE): Query target\n\
        -o, --timeout <TIMEOUT_MS> (optional, number, default = '%d'): Query timeout in milliseconds\n",
        DEFAULT_SELECTOR, DEFAULT_TIMEOUT_MS);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.selector, "s", "selector", (char*), (char*)DEFAULT_SELECTOR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    _Z_PARSE_ARG(args.timeout_ms, "o", "timeout", atoi, DEFAULT_TIMEOUT_MS);
    _Z_PARSE_ARG(args.target, "t", "target", parse_query_target, z_query_target_default());

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_get.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_SELECTOR "demo/example/**"
#define DEFAULT_VALUE NULL
#define DEFAULT_TIMEOUT_MS 10000

struct args_t {
    char* selector;           // -s, --selector
    char* value;              // -p, --payload
    z_query_target_t target;  // -t, --target
    uint64_t timeout_ms;      // -o, --timeout
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    const char* ke = args.selector;
    size_t ke_len = strlen(ke);
    const char* params = strchr(args.selector, '?');
    if (params != NULL) {
        ke_len = params - ke;
        params += 1;
    }

    z_view_keyexpr_t keyexpr;

    if (z_view_keyexpr_from_substr(&keyexpr, ke, ke_len) < 0) {
        printf("%.*s is not a valid key expression", (int)ke_len, ke);
        exit(-1);
    }

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Sending Query '%s'...\n", args.selector);
    z_owned_fifo_handler_reply_t handler;
    z_owned_closure_reply_t closure;
    z_fifo_channel_reply_new(&closure, &handler, 16);

    z_get_options_t opts;
    z_get_options_default(&opts);
    opts.target = args.target;
    opts.timeout_ms = args.timeout_ms;

    z_owned_bytes_t payload;
    if (args.value != NULL) {
        z_bytes_from_static_str(&payload, args.value);
        opts.payload = z_move(payload);
    }
    z_get(z_loan(s), z_loan(keyexpr), params, z_move(closure),
          &opts);  // here, the send is moved and will be dropped by zenoh when adequate
    z_owned_reply_t reply;

    while (z_recv(z_loan(handler), &reply) == Z_OK) {
        if (z_reply_is_ok(z_loan(reply))) {
            const z_loaned_sample_t* sample = z_reply_ok(z_loan(reply));

            z_view_string_t key_str;
            z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_str);

            z_owned_string_t reply_str;
            z_bytes_to_string(z_sample_payload(sample), &reply_str);

            printf(">> Received ('%.*s': '%.*s')\n", (int)z_string_len(z_loan(key_str)), z_string_data(z_loan(key_str)),
                   (int)z_string_len(z_loan(reply_str)), z_string_data(z_loan(reply_str)));
            z_drop(z_move(reply_str));
        } else {
            printf("Received an error\n");
        }
        z_drop(z_move(reply));
    }

    z_drop(z_move(handler));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_get [OPTIONS]\n\n\
    Options:\n\
        -s, --selector <SELECTOR> (optional, string, default='%s'): The selection of resources to query\n\
        -p, --payload <PAYLOAD> (optional, string): An optional value to put in the query\n\
        -t, --target <TARGET> (optional, BEST_MATCHING | ALL | ALL_COMPLETE): Query target\n\
        -o, --timeout <TIMEOUT_MS> (optional, number, default = '%d'): Query timeout in milliseconds\n",
        DEFAULT_SELECTOR, DEFAULT_TIMEOUT_MS);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.selector, "s", "selector", (char*), (char*)DEFAULT_SELECTOR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    _Z_PARSE_ARG(args.timeout_ms, "o", "timeout", atoi, DEFAULT_TIMEOUT_MS);
    _Z_PARSE_ARG(args.target, "t", "target", parse_query_target, z_query_target_default());

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_info.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>

#include "parse_args.h"
#include "zenoh.h"

void print_zid(const z_id_t* id, void* ctx) {
    z_owned_string_t str;
    z_id_to_string(id, &str);
    printf("%.*s\n", (int)z_string_len(z_loan(str)), z_string_data(z_loan(str)));
    z_drop(z_move(str));
}

void parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_id_t self_id = z_info_zid(z_loan(s));
    printf("own id: ");
    print_zid(&self_id, NULL);

    printf("routers ids:\n");
    z_owned_closure_zid_t callback;
    z_closure(&callback, print_zid, NULL, NULL);
    z_info_routers_zid(z_loan(s), z_move(callback));

    // `callback` has been `z_move`d just above, so it's safe to reuse the variable,
    // we'll just have to make sure we `z_move` it again to avoid mem-leaks.
    printf("peers ids:\n");
    z_owned_closure_zid_t callback2;
    z_closure(&callback2, print_zid, NULL, NULL);
    z_info_peers_zid(z_loan(s), z_move(callback2));

    z_drop(z_move(s));
}

void print_help() {
    printf(
        "\
    Usage: z_info [OPTIONS]\n\n\
    Options:\n");
    printf(COMMON_HELP);
}

void parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
}
```

---

# Example: examples--z_liveliness.c

```c
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "group1/zenoh-rs"

struct args_t {
    char* keyexpr;  // -k, --key
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    z_view_keyexpr_t keyexpr;
    if (z_view_keyexpr_from_str(&keyexpr, args.keyexpr) < 0) {
        printf("%s is not a valid key expression\n", args.keyexpr);
        exit(-1);
    }

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Declaring liveliness token '%s'...\n", args.keyexpr);
    z_owned_liveliness_token_t token;
    if (z_liveliness_declare_token(z_loan(s), &token, z_loan(keyexpr), NULL) < 0) {
        printf("Unable to create liveliness token!\n");
        exit(-1);
    }

    printf("Press CTRL-C to undeclare liveliness token and quit...\n");
    while (1) {
        z_sleep_s(1);
    }

    // LivelinessTokens are automatically closed when dropped
    // Use the code below to manually undeclare it if needed
    printf("Undeclaring liveliness token...\n");
    z_drop(z_move(token));

    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_liveliness [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression for the liveliness token\n",
        DEFAULT_KEYEXPR);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_non_blocking_get.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_SELECTOR "demo/example/**"
#define DEFAULT_VALUE NULL
#define DEFAULT_TIMEOUT_MS 10000

struct args_t {
    char* selector;           // -s, --selector
    char* value;              // -p, --payload
    z_query_target_t target;  // -t, --target
    uint64_t timeout_ms;      // -o, --timeout
};

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    const char* ke = args.selector;
    size_t ke_len = strlen(ke);
    const char* params = strchr(args.selector, '?');
    if (params != NULL) {
        ke_len = params - ke;
        params += 1;
    }

    z_view_keyexpr_t keyexpr;
    if (z_view_keyexpr_from_substr(&keyexpr, ke, ke_len) < 0) {
        printf("%.*s is not a valid key expression", (int)ke_len, ke);
        exit(-1);
    }

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Sending Query '%s'...\n", args.selector);
    z_get_options_t opts;
    z_get_options_default(&opts);
    opts.target = args.target;
    opts.timeout_ms = args.timeout_ms;

    z_owned_bytes_t payload;
    if (args.value != NULL) {
        z_bytes_from_static_str(&payload, args.value);
        opts.payload = z_move(payload);
    }

    z_owned_fifo_handler_reply_t handler;
    z_owned_closure_reply_t closure;
    z_fifo_channel_reply_new(&closure, &handler, 16);
    z_get(z_loan(s), z_loan(keyexpr), params, z_move(closure),
          &opts);  // here, the closure is moved and will be dropped by zenoh when adequate
    z_owned_reply_t reply;

    z_result_t res;
    while ((res = z_try_recv(z_loan(handler), &reply)) != Z_CHANNEL_DISCONNECTED) {
        if (res != Z_OK) {
            z_sleep_ms(50);
            continue;
        }
        if (z_reply_is_ok(z_loan(reply))) {
            const z_loaned_sample_t* sample = z_reply_ok(z_loan(reply));
            z_view_string_t key_str;
            z_owned_string_t payload_string;
            z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_str);
            z_bytes_to_string(z_sample_payload(sample), &payload_string);
            printf(">> Received ('%.*s': '%.*s')\n", (int)z_string_len(z_loan(key_str)), z_string_data(z_loan(key_str)),
                   (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)));
            z_drop(z_move(payload_string));
        } else {
            printf("Received an error\n");
        }
    }
    z_drop(z_move(reply));
    z_drop(z_move(handler));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_get [OPTIONS]\n\n\
    Options:\n\
        -s, --selector <SELECTOR> (optional, string, default='%s'): The selection of resources to query\n\
        -p, --payload <PAYLOAD> (optional, string): An optional value to put in the query\n\
        -t, --target <TARGET> (optional, BEST_MATCHING | ALL | ALL_COMPLETE): Query target\n\
        -o, --timeout <TIMEOUT_MS> (optional, number, default = '%d'): Query timeout in milliseconds\n",
        DEFAULT_SELECTOR, DEFAULT_TIMEOUT_MS);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.selector, "s", "selector", (char*), (char*)DEFAULT_SELECTOR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    _Z_PARSE_ARG(args.timeout_ms, "o", "timeout", atoi, DEFAULT_TIMEOUT_MS);
    _Z_PARSE_ARG(args.target, "t", "target", parse_query_target, z_query_target_default());

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_ping_shm.c

```c
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_PING_NB 100
#define DEFAULT_WARMUP_MS 1000
#define PING_TIMEOUT_SEC 1

#define handle_error_en(en, msg) \
    do {                         \
        errno = en;              \
        perror(msg);             \
        exit(EXIT_FAILURE);      \
    } while (0)

z_owned_condvar_t cond;
z_owned_mutex_t mutex;

void callback(z_loaned_sample_t* sample, void* context) { z_condvar_signal(z_loan(cond)); }
void drop(void* context) { z_drop(z_move(cond)); }

struct args_t {
    unsigned int size;             // positional_0
    unsigned int number_of_pings;  // -n, --samples
    unsigned int warmup_ms;        // -w, --warmup
    bool no_express;               // --no-express
};

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");
    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    z_mutex_init(&mutex);
    z_condvar_init(&cond);

    z_owned_session_t session;
    if (z_open(&session, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_view_keyexpr_t ping;
    z_view_keyexpr_from_str_unchecked(&ping, "test/ping");
    z_view_keyexpr_t pong;
    z_view_keyexpr_from_str_unchecked(&pong, "test/pong");
    z_publisher_options_t opts;
    z_publisher_options_default(&opts);
    opts.is_express = !args.no_express;

    z_owned_publisher_t pub;
    if (z_declare_publisher(z_loan(session), &pub, z_loan(ping), &opts) < 0) {
        printf("Unable to declare publisher for key expression!\n");
        exit(-1);
    }

    z_owned_closure_sample_t respond;
    z_closure(&respond, callback, drop, (void*)(&pub));

    z_owned_subscriber_t sub;
    if (z_declare_subscriber(z_loan(session), &sub, z_loan(pong), z_move(respond), NULL) < 0) {
        printf("Unable to declare subscriber for key expression!\n");
        exit(-1);
    }

    // Create SHM Provider
    z_owned_shm_provider_t provider;
    z_shm_provider_default_new(&provider, args.size);

    // Allocate SHM Buffer
    z_buf_layout_alloc_result_t alloc;
    z_shm_provider_alloc(&alloc, z_loan(provider), args.size);
    if (alloc.status != ZC_BUF_LAYOUT_ALLOC_STATUS_OK) {
        printf("Unexpected failure during SHM buffer allocation...");
        return -1;
    }
    // Fill SHM Buffer with data
    uint8_t* data = z_shm_mut_data_mut(z_loan_mut(alloc.buf));
    for (int i = 0; i < args.size; i++) {
        data[i] = i % 10;
    }
    // Convert mutable SHM Buffer into immutable one (to be able to make it's ref copies)
    z_owned_shm_t shm;
    z_shm_from_mut(&shm, z_move(alloc.buf));

    z_owned_bytes_t shmbs;
    if (z_bytes_from_shm(&shmbs, z_move(shm)) != Z_OK) {
        printf("Unexpected failure during SHM buffer serialization...\n");
        return -1;
    }

    z_mutex_lock(z_loan_mut(mutex));
    if (args.warmup_ms) {
        printf("Warming up for %dms...\n", args.warmup_ms);
        z_clock_t warmup_start = z_clock_now();

        unsigned long elapsed_us = 0;
        while (elapsed_us < args.warmup_ms * 1000) {
            z_owned_bytes_t payload;
            z_bytes_clone(&payload, z_loan(shmbs));
            z_publisher_put(z_loan(pub), z_move(payload), NULL);
            int s = z_condvar_wait(z_loan(cond), z_loan_mut(mutex));
            if (s != 0) {
                handle_error_en(s, "z_condvar_wait");
            }
            elapsed_us = z_clock_elapsed_us(&warmup_start);
        }
    }
    unsigned long* results = z_malloc(sizeof(unsigned long) * args.number_of_pings);
    for (int i = 0; i < args.number_of_pings; i++) {
        z_clock_t measure_start = z_clock_now();
        z_owned_bytes_t payload;
        z_bytes_clone(&payload, z_loan(shmbs));
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
        int s = z_condvar_wait(z_loan(cond), z_loan_mut(mutex));
        if (s != 0) {
            handle_error_en(s, "z_condvar_wait");
        }
        results[i] = z_clock_elapsed_us(&measure_start);
    }
    for (int i = 0; i < args.number_of_pings; i++) {
        printf("%d bytes: seq=%d rtt=%luµs, lat=%luµs\n", args.size, i, results[i], results[i] / 2);
    }
    z_mutex_unlock(z_loan_mut(mutex));
    z_free(results);
    z_drop(z_move(sub));
    z_drop(z_move(pub));
    z_drop(z_move(mutex));
    z_drop(z_move(session));

    z_drop(z_move(shm));
    z_drop(z_move(provider));
}

void print_help() {
    printf(
        "\
    Usage: z_ping [OPTIONS] <PAYLOAD_SIZE>\n\n\
    Arguments:\n\
        <PAYLOAD_SIZE> (required, number): Size of the payload to publish\n\n\
    Options:\n\
        -n, --samples <SAMPLES> (optional, int, default=%d): The number of pings to be attempted\n\
        -w, --warmup <WARMUP> (optional, int, default=%d): The warmup time in ms during which pings will be emitted but not measured\n\
        --no-express (optional): Disable message batching.\n",
        DEFAULT_PING_NB, DEFAULT_WARMUP_MS);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.number_of_pings, "n", "samples", atoi, DEFAULT_PING_NB);
    _Z_PARSE_ARG(args.warmup_ms, "w", "warmup", atoi, DEFAULT_WARMUP_MS);
    args.no_express = _Z_CHECK_FLAG("no-express");

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args[0]) {
        printf("<PAYLOAD_SIZE> argument is required\n");
        free(pos_args);
        exit(-1);
    }
    args.size = atoi(pos_args[0]);
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_ping.c

```c
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_PING_NB 100
#define DEFAULT_WARMUP_MS 1000
#define PING_TIMEOUT_SEC 1

#define handle_error_en(en, msg) \
    do {                         \
        errno = en;              \
        perror(msg);             \
        exit(EXIT_FAILURE);      \
    } while (0)

z_owned_condvar_t cond;
z_owned_mutex_t mutex;

void callback(z_loaned_sample_t* sample, void* context) { z_condvar_signal(z_loan(cond)); }
void drop(void* context) { z_drop(z_move(cond)); }

struct args_t {
    unsigned int size;             // positional_0
    unsigned int number_of_pings;  // -n, --samples
    unsigned int warmup_ms;        // -w, --warmup
    bool no_express;               // --no-express
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    z_mutex_init(&mutex);
    z_condvar_init(&cond);

    z_owned_session_t session;
    if (z_open(&session, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_view_keyexpr_t ping;
    z_view_keyexpr_from_str_unchecked(&ping, "test/ping");
    z_view_keyexpr_t pong;
    z_view_keyexpr_from_str_unchecked(&pong, "test/pong");
    z_publisher_options_t opts;
    z_publisher_options_default(&opts);
    opts.is_express = !args.no_express;

    z_owned_publisher_t pub;
    if (z_declare_publisher(z_loan(session), &pub, z_loan(ping), &opts) < 0) {
        printf("Unable to declare publisher for key expression!\n");
        exit(-1);
    }

    z_owned_closure_sample_t respond;
    z_closure(&respond, callback, drop, (void*)(&pub));

    z_owned_subscriber_t sub;
    if (z_declare_subscriber(z_loan(session), &sub, z_loan(pong), z_move(respond), NULL) < 0) {
        printf("Unable to declare subscriber for key expression!\n");
        exit(-1);
    }

    uint8_t* data = z_malloc(args.size);
    for (int i = 0; i < args.size; i++) {
        data[i] = i % 10;
    }
    z_owned_bytes_t payload;

    z_mutex_lock(z_loan_mut(mutex));
    if (args.warmup_ms) {
        printf("Warming up for %dms...\n", args.warmup_ms);
        z_clock_t warmup_start = z_clock_now();

        unsigned long elapsed_us = 0;
        while (elapsed_us < args.warmup_ms * 1000) {
            z_bytes_from_buf(&payload, data, args.size, NULL, NULL);
            z_publisher_put(z_loan(pub), z_move(payload), NULL);
            int s = z_condvar_wait(z_loan(cond), z_loan_mut(mutex));
            if (s != 0) {
                handle_error_en(s, "z_condvar_wait");
            }
            elapsed_us = z_clock_elapsed_us(&warmup_start);
        }
    }
    unsigned long* results = z_malloc(sizeof(unsigned long) * args.number_of_pings);
    for (int i = 0; i < args.number_of_pings; i++) {
        z_bytes_from_buf(&payload, data, args.size, NULL, NULL);
        z_clock_t measure_start = z_clock_now();
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
        int s = z_condvar_wait(z_loan(cond), z_loan_mut(mutex));
        if (s != 0) {
            handle_error_en(s, "z_condvar_wait");
        }
        results[i] = z_clock_elapsed_us(&measure_start);
    }
    for (int i = 0; i < args.number_of_pings; i++) {
        printf("%d bytes: seq=%d rtt=%luµs, lat=%luµs\n", args.size, i, results[i], results[i] / 2);
    }
    z_mutex_unlock(z_loan_mut(mutex));
    z_free(results);
    z_free(data);
    z_drop(z_move(sub));
    z_drop(z_move(pub));
    z_drop(z_move(mutex));
    z_drop(z_move(session));
}

void print_help() {
    printf(
        "\
    Usage: z_ping [OPTIONS] <PAYLOAD_SIZE>\n\n\
    Arguments:\n\
        <PAYLOAD_SIZE> (required, number): Size of the payload to publish\n\n\
    Options:\n\
        -n, --samples <SAMPLES> (optional, int, default=%d): The number of pings to be attempted\n\
        -w, --warmup <WARMUP> (optional, int, default=%d): The warmup time in ms during which pings will be emitted but not measured\n\
        --no-express (optional): Disable message batching.\n",
        DEFAULT_PING_NB, DEFAULT_WARMUP_MS);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.number_of_pings, "n", "samples", atoi, DEFAULT_PING_NB);
    _Z_PARSE_ARG(args.warmup_ms, "w", "warmup", atoi, DEFAULT_WARMUP_MS);
    args.no_express = _Z_CHECK_FLAG("no-express");

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args[0]) {
        printf("<PAYLOAD_SIZE> argument is required\n");
        free(pos_args);
        exit(-1);
    }
    args.size = atoi(pos_args[0]);
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_pong.c

```c
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

struct args_t {
    bool no_express;  // --no-express
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

void callback(z_loaned_sample_t* sample, void* context) {
    const z_loaned_publisher_t* pub = z_loan(*(z_owned_publisher_t*)context);
    z_owned_bytes_t payload;
    z_bytes_clone(&payload, z_sample_payload(sample));
    z_publisher_put(pub, z_move(payload), NULL);
}
void drop(void* context) {
    z_owned_publisher_t* pub = (z_owned_publisher_t*)context;
    z_drop(z_move(*pub));
    // A note on lifetimes:
    //  here, `sub` takes ownership of `pub` and will drop it before returning from its own `drop`,
    //  which makes passing a pointer to the stack safe as long as `sub` is dropped in a scope where `pub` is still
    //  valid.
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    z_owned_session_t session;
    if (z_open(&session, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_view_keyexpr_t ping;
    z_view_keyexpr_from_str_unchecked(&ping, "test/ping");
    z_view_keyexpr_t pong;
    z_view_keyexpr_from_str_unchecked(&pong, "test/pong");
    z_publisher_options_t opts;
    z_publisher_options_default(&opts);
    opts.is_express = !args.no_express;

    z_owned_publisher_t pub;
    if (z_declare_publisher(z_loan(session), &pub, z_loan(pong), &opts) < 0) {
        printf("Unable to declare publisher for key expression!\n");
        exit(-1);
    }

    z_owned_closure_sample_t respond;
    z_closure(&respond, callback, drop, (void*)&pub);
    if (z_declare_background_subscriber(z_loan(session), z_loan(ping), z_move(respond), NULL) < 0) {
        printf("Unable to declare background subscriber for key expression!\n");
        exit(-1);
    }

    while (1) {
        z_sleep_s(1);
    }

    z_drop(z_move(session));
}

void print_help() {
    printf(
        "\
    Usage: z_pong [OPTIONS]\n\n\
    Options:\n\
        --no-express (optional): Disable message batching.\n");
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    args.no_express = _Z_CHECK_FLAG("no-express");
    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_pub_shm_thr.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_SHARED_MEMORY_SIZE 32

struct args_t {
    unsigned int size;                         // positional_1
    unsigned long long shared_memory_size_mb;  // -s, --shared-memory
};

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    char* keyexpr = "test/thr";

    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_publisher_options_t options;
    z_publisher_options_default(&options);
    options.congestion_control = Z_CONGESTION_CONTROL_BLOCK;

    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, keyexpr);
    if (z_declare_publisher(z_loan(s), &pub, z_loan(ke), &options) < 0) {
        printf("Unable to declare publisher for key expression!\n");
        exit(-1);
    }

    printf("Creating POSIX SHM Provider...\n");
    z_owned_shm_provider_t provider;
    z_shm_provider_default_new(&provider, args.shared_memory_size_mb * 1024 * 1024);

    printf("Allocating single SHM buffer\n");
    z_buf_layout_alloc_result_t alloc;
    z_shm_provider_alloc(&alloc, z_loan(provider), args.size);
    if (alloc.status != ZC_BUF_LAYOUT_ALLOC_STATUS_OK) {
        printf("Unexpected failure during SHM buffer allocation...\n");
        return -1;
    }
    memset(z_shm_mut_data_mut(z_loan_mut(alloc.buf)), 1, args.size);
    z_owned_shm_t shm;
    z_shm_from_mut(&shm, z_move(alloc.buf));

    z_owned_bytes_t shmbs;
    if (z_bytes_from_shm(&shmbs, z_move(shm)) != Z_OK) {
        printf("Unexpected failure during SHM buffer serialization...\n");
        return -1;
    }

    while (1) {
        z_owned_bytes_t payload;
        z_bytes_clone(&payload, z_loan(shmbs));
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));

    z_drop(z_move(shm));
    z_drop(z_move(provider));
}

void print_help() {
    printf(
        "\
    Usage: z_pub_thr [OPTIONS] <PAYLOAD_SIZE>\n\n\
    Arguments:\n\
        <PAYLOAD_SIZE> (required, number): Size of the payload to publish\n\n\
    Options:\n\
        -s, --shared-memory <SHARED_MEMORY_SIZE> (optional, number, default='%d'): shared memory size in MBytes.\n",
        DEFAULT_SHARED_MEMORY_SIZE);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.shared_memory_size_mb, "s", "shared-memory", atoi, DEFAULT_SHARED_MEMORY_SIZE);

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args) {
        printf("Unexpected additional positional arguments\n");
        exit(-1);
    }
    if (!pos_args[0]) {
        printf("<PAYLOAD_SIZE> argument is required\n");
        free(pos_args);
        exit(-1);
    }
    args.size = atoi(pos_args[0]);
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_pub_shm.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-pub-shm"
#define DEFAULT_VALUE "Pub from C!"

struct args_t {
    char* keyexpr;               // -k, --key
    char* value;                 // -p, --payload
    bool add_matching_listener;  // --add-matching-listener
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

void matching_status_handler(const z_matching_status_t* matching_status, void* arg) {
    if (matching_status->matching) {
        printf("Publisher has matching subscribers.\n");
    } else {
        printf("Publisher has NO MORE matching subscribers.\n");
    }
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Declaring Publisher on '%s'...\n", args.keyexpr);
    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);
    if (z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL) < 0) {
        printf("Unable to declare Publisher for key expression!\n");
        exit(-1);
    }

    if (args.add_matching_listener) {
        z_owned_closure_matching_status_t callback;
        z_closure(&callback, matching_status_handler, NULL, NULL);
        if (z_publisher_declare_background_matching_listener(z_loan(pub), z_move(callback)) < 0) {
            printf("Unable to declare background matching listener for key expression!\n");
            exit(-1);
        }
    }

    printf("Creating POSIX SHM Provider...\n");
    const size_t total_size = 4096;
    const size_t buf_ok_size = total_size / 4;

    z_owned_shm_provider_t provider;
    z_shm_provider_default_new(&provider, total_size);

    for (int idx = 0; 1; ++idx) {
        z_sleep_s(1);

        z_buf_layout_alloc_result_t alloc;
        z_shm_provider_alloc_gc_defrag_blocking(&alloc, z_loan(provider), buf_ok_size);
        if (alloc.status == ZC_BUF_LAYOUT_ALLOC_STATUS_OK) {
            {
                uint8_t* buf = z_shm_mut_data_mut(z_loan_mut(alloc.buf));
                sprintf((char*)buf, "[%4d] %s", idx, args.value);
                printf("Putting Data ('%s': '%s')...\n", args.keyexpr, buf);
            }

            z_publisher_put_options_t options;
            z_publisher_put_options_default(&options);

            z_owned_bytes_t payload;
            z_bytes_from_shm_mut(&payload, z_move(alloc.buf));

            z_publisher_put(z_loan(pub), z_move(payload), &options);
        } else {
            printf("Unexpected failure during SHM buffer allocation...");
            break;
        }
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
    z_drop(z_move(provider));

    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_pub_shm [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to write to\n\
        -p, --payload <PAYLOAD> (optional, string, default='%s'): The value to write\n\
        --add-matching-listener (optional): Add matching listener\n",
        DEFAULT_KEYEXPR, DEFAULT_VALUE);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    args.add_matching_listener = _Z_CHECK_FLAG("add-matching-listener");
    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_pub_thr.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_PRIORITY Z_PRIORITY_DATA
struct args_t {
    unsigned int size;      // positional_1
    z_priority_t priority;  // -p, --priority
    bool express;           // --express
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    char* keyexpr = "test/thr";

    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);
    uint8_t* value = (uint8_t*)z_malloc(args.size);
    memset(value, 0, args.size);
    for (size_t i = 0; i < args.size; ++i) {
        value[i] = i % 10;
    }

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_publisher_options_t options;
    z_publisher_options_default(&options);
    options.congestion_control = Z_CONGESTION_CONTROL_BLOCK;
    options.priority = args.priority;
    options.is_express = args.express;

    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, keyexpr);
    if (z_declare_publisher(z_loan(s), &pub, z_loan(ke), &options) < 0) {
        printf("Unable to declare publisher for key expression!\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    z_owned_bytes_t payload;
    z_bytes_from_buf(&payload, value, args.size, NULL, NULL);
    while (1) {
        z_owned_bytes_t to_send;
        z_bytes_clone(&to_send, z_loan(payload));
        z_publisher_put(z_loan(pub), z_move(to_send), NULL);
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
}

void print_help() {
    printf(
        "\
    Usage: z_pub_thr [OPTIONS] <PAYLOAD_SIZE>\n\n\
    Arguments:\n\
        <PAYLOAD_SIZE> (required, number): Size of the payload to publish\n\n\
    Options:\n\
        -p, --priority <PRIORITY> (optional, number [%d - %d], default='%d'): Priority for sending data\n\
        --express (optional): Batch messages.\n",
        Z_PRIORITY_REAL_TIME, Z_PRIORITY_BACKGROUND, DEFAULT_PRIORITY);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.priority, "p", "priority", parse_priority, DEFAULT_PRIORITY);
    args.express = _Z_CHECK_FLAG("express");

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args) {
        printf("Unexpected additional positional arguments\n");
        exit(-1);
    }
    if (!pos_args[0]) {
        printf("<PAYLOAD_SIZE> argument is required\n");
        free(pos_args);
        exit(-1);
    }
    args.size = atoi(pos_args[0]);
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_pub.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-pub"
#define DEFAULT_VALUE "Pub from C!"
#define DEFAULT_ATTACHMENT NULL

struct args_t {
    char* keyexpr;               // -k, --key
    char* value;                 // -p, --payload
    char* attachment;            // -a, --attach
    bool add_matching_listener;  // --add-matching-listener
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

void matching_status_handler(const z_matching_status_t* matching_status, void* arg) {
    if (matching_status->matching) {
        printf("Publisher has matching subscribers.\n");
    } else {
        printf("Publisher has NO MORE matching subscribers.\n");
    }
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Declaring Publisher on '%s'...\n", args.keyexpr);
    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);
    if (z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL) < 0) {
        printf("Unable to declare Publisher for key expression!\n");
        exit(-1);
    }

    if (args.add_matching_listener) {
        z_owned_closure_matching_status_t callback;
        z_closure(&callback, matching_status_handler, NULL, NULL);
        if (z_publisher_declare_background_matching_listener(z_loan(pub), z_move(callback)) < 0) {
            printf("Unable to declare background matching listener for key expression!\n");
            exit(-1);
        }
    }

    printf("Press CTRL-C to quit...\n");
    char buf[256] = {0};
    for (int idx = 0; 1; ++idx) {
        z_sleep_s(1);
        sprintf(buf, "[%4d] %s", idx, args.value);
        printf("Putting Data ('%s': '%s')...\n", args.keyexpr, buf);
        z_publisher_put_options_t options;
        z_publisher_put_options_default(&options);

        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, buf);
        z_owned_bytes_t attachment;
        if (args.attachment != NULL) {
            z_bytes_copy_from_str(&attachment, args.attachment);
            options.attachment = z_move(attachment);
        }
        /// optional encoding
        z_owned_encoding_t encoding;
        z_encoding_clone(&encoding, z_encoding_text_plain());
        options.encoding = z_move(encoding);

        z_publisher_put(z_loan(pub), z_move(payload), &options);
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_pub [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to write to\n\
        -p, --payload <PAYLOAD> (optional, string, default='%s'): The value to write\n\
        -a, --attach <ATTACHMENT> (optional, string, default=NULL): The attachment to add to each put\n\
        --add-matching-listener (optional): Add matching listener\n",
        DEFAULT_KEYEXPR, DEFAULT_VALUE);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    _Z_PARSE_ARG(args.attachment, "a", "attach", (char*), (char*)DEFAULT_ATTACHMENT);
    args.add_matching_listener = _Z_CHECK_FLAG("add-matching-listener");

    parse_zenoh_common_args(argc, argv, config);
    const char* unknown_arg = check_unknown_opts(argc, argv);
    if (unknown_arg) {
        printf("Unknown option %s\n", unknown_arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_pull.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/**"
#define DEFAULT_RING_BUFFER_SIZE 3
#define DEFAULT_PULL_INTERVAL 5

struct args_t {
    char* keyexpr;           // -k, --key
    unsigned long size;      // -s, --size
    unsigned long interval;  // -i, --interval
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

const char* kind_to_str(z_sample_kind_t kind);

void handle_sample(const z_loaned_sample_t* sample) {
    z_view_string_t keystr;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &keystr);
    z_owned_string_t payload_value;
    z_bytes_to_string(z_sample_payload(sample), &payload_value);
    printf(">> [Subscriber] Received %s ('%.*s': '%.*s')\n", kind_to_str(z_sample_kind(sample)),
           (int)z_string_len(z_loan(keystr)), z_string_data(z_loan(keystr)), (int)z_string_len(z_loan(payload_value)),
           z_string_data(z_loan(payload_value)));
    z_drop(z_move(payload_value));
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;

    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_owned_closure_sample_t closure;
    z_owned_ring_handler_sample_t handler;
    z_ring_channel_sample_new(&closure, &handler, args.size);

    printf("Declaring Subscriber on '%s'...\n", args.keyexpr);
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);
    z_owned_subscriber_t sub;

    if (z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(closure), NULL) < 0) {
        printf("Unable to declare subscriber.\n");
        exit(-1);
    }

    printf("Press <enter> to pull data...\n");
    z_owned_sample_t sample;

    char c = 0;
    while (c != 'q') {
        c = getchar();
        if (c == -1) {
            z_sleep_s(args.interval);
        } else {
            z_result_t res = z_try_recv(z_loan(handler), &sample);
            if (res == Z_OK) {
                handle_sample(z_loan(sample));
                z_drop(z_move(sample));
            }
        }
    }
    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}

const char* kind_to_str(z_sample_kind_t kind) {
    switch (kind) {
        case Z_SAMPLE_KIND_PUT:
            return "PUT";
        case Z_SAMPLE_KIND_DELETE:
            return "DELETE";
        default:
            return "UNKNOWN";
    }
}

void print_help() {
    printf(
        "\
    Usage: z_pull [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to subscribe to\n\
        -s, --size <SIZE> (optional, number, default='%d'): The size of the ring buffer\n\
        -i, --interval <INTERVAL> (optional, number, default='%d'): The interval for pulling the ringbuffer.\n",
        DEFAULT_KEYEXPR, DEFAULT_RING_BUFFER_SIZE, DEFAULT_PULL_INTERVAL);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.size, "s", "size", atoi, DEFAULT_RING_BUFFER_SIZE);
    _Z_PARSE_ARG(args.interval, "i", "interval", atoi, DEFAULT_PULL_INTERVAL);

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_put.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-put"
#define DEFAULT_VALUE "Put from C!"

struct args_t {
    char* keyexpr;  // -k, --key
    char* value;    // -p, --payload
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Putting Data ('%s': '%s')...\n", args.keyexpr, args.value);

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);

    z_owned_bytes_t payload;
    z_bytes_from_static_str(&payload, args.value);

    int res = z_put(z_loan(s), z_loan(ke), z_move(payload), NULL);
    if (res < 0) {
        printf("Put failed...\n");
    }

    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_put [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to write to\n\
        -p, --payload <PAYLOAD> (optional, string, default='%s'): The value to write\n",
        DEFAULT_KEYEXPR, DEFAULT_VALUE);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_querier.c

```c
//
// Copyright (c) 2024 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_SELECTOR "demo/example/**"
#define DEFAULT_VALUE NULL
#define DEFAULT_TIMEOUT_MS 10000

struct args_t {
    char* selector;              // -s, --selector
    char* value;                 // -p, --payload
    bool add_matching_listener;  // --add-matching-listener
    z_query_target_t target;     // -t, --target
    uint64_t timeout_ms;         // -o, --timeout
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

void matching_status_handler(const z_matching_status_t* matching_status, void* arg) {
    if (matching_status->matching) {
        printf("Querier has matching queryables.\n");
    } else {
        printf("Querier has NO MORE matching queryables.\n");
    }
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    const char* ke = args.selector;
    size_t ke_len = strlen(ke);
    const char* params = strchr(args.selector, '?');
    if (params != NULL) {
        ke_len = params - ke;
        params += 1;
    }

    z_view_keyexpr_t keyexpr;
    if (z_view_keyexpr_from_substr(&keyexpr, ke, ke_len) < 0) {
        printf("%.*s is not a valid key expression", (int)ke_len, ke);
        exit(-1);
    }

    printf("Declaring Querier on '%s'...\n", ke);
    z_owned_querier_t querier;

    z_querier_options_t opts;
    z_querier_options_default(&opts);
    opts.timeout_ms = args.timeout_ms;
    opts.target = args.target;

    if (z_declare_querier(z_loan(s), &querier, z_loan(keyexpr), &opts) < 0) {
        printf("Unable to declare Querier for key expression!\n");
        exit(-1);
    }

    if (args.add_matching_listener) {
        z_owned_closure_matching_status_t callback;
        z_closure(&callback, matching_status_handler, NULL, NULL);
        if (z_querier_declare_background_matching_listener(z_loan(querier), z_move(callback)) < 0) {
            printf("Unable to declare background matching listener for key expression!\n");
            exit(-1);
        }
    }

    printf("Press CTRL-C to quit...\n");
    char buf[256] = {0};
    for (int idx = 0; 1; ++idx) {
        z_sleep_s(1);
        sprintf(buf, "[%4d] %s", idx, args.value ? args.value : "");
        printf("Querying '%s' with payload '%s'...\n", args.selector, buf);
        z_querier_get_options_t get_options;
        z_querier_get_options_default(&get_options);

        if (args.value) {
            z_owned_bytes_t payload;
            z_bytes_copy_from_str(&payload, buf);
            get_options.payload = z_move(payload);
        }

        z_owned_fifo_handler_reply_t handler;
        z_owned_closure_reply_t closure;
        z_fifo_channel_reply_new(&closure, &handler, 16);

        z_querier_get(z_loan(querier), params, z_move(closure), &get_options);

        z_owned_reply_t reply;
        for (z_result_t res = z_recv(z_loan(handler), &reply); res == Z_OK; res = z_recv(z_loan(handler), &reply)) {
            if (z_reply_is_ok(z_loan(reply))) {
                const z_loaned_sample_t* sample = z_reply_ok(z_loan(reply));

                z_view_string_t key_str;
                z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_str);

                z_owned_string_t reply_str;
                z_bytes_to_string(z_sample_payload(sample), &reply_str);

                printf(">> Received ('%.*s': '%.*s')\n", (int)z_string_len(z_loan(key_str)),
                       z_string_data(z_loan(key_str)), (int)z_string_len(z_loan(reply_str)),
                       z_string_data(z_loan(reply_str)));
                z_drop(z_move(reply_str));
            } else {
                printf("Received an error\n");
            }
            z_drop(z_move(reply));
        }
        z_drop(z_move(handler));
    }

    z_drop(z_move(querier));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_querier [OPTIONS]\n\n\
    Options:\n\
        -s, --selector <SELECTOR> (optional, string, default='%s'): The selection of resources to query\n\
        -p, --payload <PAYLOAD> (optional, string): An optional value to put in the query\n\
        -t, --target <TARGET> (optional, BEST_MATCHING | ALL | ALL_COMPLETE): Query target\n\
        -o, --timeout <TIMEOUT_MS> (optional, number, default = '%d'): Query timeout in milliseconds\n\
        --add-matching-listener (optional): Add matching listener\n",
        DEFAULT_SELECTOR, DEFAULT_TIMEOUT_MS);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.selector, "s", "selector", (char*), (char*)DEFAULT_SELECTOR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    _Z_PARSE_ARG(args.timeout_ms, "o", "timeout", atoi, DEFAULT_TIMEOUT_MS);
    _Z_PARSE_ARG(args.target, "t", "target", parse_query_target, z_query_target_default());
    args.add_matching_listener = _Z_CHECK_FLAG("add-matching-listener");

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_queryable_shm.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-queryable"
#define DEFAULT_VALUE "Queryable from C SHM!"
z_view_keyexpr_t ke;
const char *value;

typedef struct {
    const char *keyexpr;
    const z_loaned_shm_provider_t *provider;
} context_t;

struct args_t {
    char *keyexpr;  // -k, --key
    char *value;    // -p, --payload
    bool complete;  // --complete
};
struct args_t parse_args(int argc, char **argv, z_owned_config_t *config);

void query_handler(z_loaned_query_t *query, void *context) {
    context_t *handler_context = (context_t *)context;

    z_view_string_t key_string;
    z_keyexpr_as_view_string(z_query_keyexpr(query), &key_string);

    z_view_string_t params;
    z_query_parameters(query, &params);

    const z_loaned_bytes_t *payload = z_query_payload(query);
    if (payload != NULL && z_bytes_len(payload) > 0) {
        const z_loaned_shm_t *shm = NULL;
        char *payload_type = z_bytes_as_loaned_shm(payload, &shm) == Z_OK ? "SHM" : "RAW";

        z_owned_string_t payload_string;
        z_bytes_to_string(payload, &payload_string);

        printf(">> [Queryable ] Received Query '%.*s?%.*s' with value '%.*s' [%s]\n",
               (int)z_string_len(z_loan(key_string)), z_string_data(z_loan(key_string)),
               (int)z_string_len(z_loan(params)), z_string_data(z_loan(params)),
               (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)), payload_type);
        z_drop(z_move(payload_string));
    } else {
        printf(">> [Queryable ] Received Query '%.*s?%.*s'\n", (int)z_string_len(z_loan(key_string)),
               z_string_data(z_loan(key_string)), (int)z_string_len(z_loan(params)), z_string_data(z_loan(params)));
    }

    printf("Allocating Shared Memory Buffer...\n");
    size_t value_len = strlen(value) + 1;  // + NULL terminator
    z_buf_layout_alloc_result_t alloc;
    z_shm_provider_alloc_gc_defrag_blocking(&alloc, handler_context->provider, value_len);
    if (alloc.status == ZC_BUF_LAYOUT_ALLOC_STATUS_OK) {
        {
            uint8_t *buf = z_shm_mut_data_mut(z_loan_mut(alloc.buf));
            memcpy(buf, value, value_len);
            printf(">> [Queryable] Responding ('%s': '%s')...\n", handler_context->keyexpr, buf);
        }

        z_query_reply_options_t options;
        z_query_reply_options_default(&options);

        z_owned_bytes_t reply_payload;
        z_bytes_from_shm_mut(&reply_payload, z_move(alloc.buf));

        z_view_keyexpr_t reply_keyexpr;
        z_view_keyexpr_from_str(&reply_keyexpr, handler_context->keyexpr);

        z_query_reply(query, z_loan(reply_keyexpr), z_move(reply_payload), &options);

    } else {
        printf("Unexpected failure during SHM buffer allocation...");
        exit(-1);
    }
}

int main(int argc, char **argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);
    value = args.value;

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    if (z_view_keyexpr_from_str(&ke, args.keyexpr) < 0) {
        printf("%s is not a valid key expression", args.keyexpr);
        exit(-1);
    }

    printf("Creating POSIX SHM Provider...\n");
    const size_t total_size = 4096;
    z_owned_shm_provider_t provider;
    z_shm_provider_default_new(&provider, total_size);

    printf("Declaring Queryable on '%s'...\n", args.keyexpr);
    z_owned_closure_query_t callback;
    context_t context = (context_t){.keyexpr = args.keyexpr, .provider = z_loan(provider)};
    z_closure(&callback, query_handler, NULL, (void *)&context);
    z_owned_queryable_t qable;

    z_queryable_options_t opts;
    z_queryable_options_default(&opts);
    opts.complete = args.complete;

    if (z_declare_queryable(z_loan(s), &qable, z_loan(ke), z_move(callback), &opts) < 0) {
        printf("Unable to create queryable.\n");
        exit(-1);
    }

    printf("Enter 'q' to quit...\n");
    char c = 0;
    while (c != 'q') {
        c = getchar();
        if (c == -1) {
            z_sleep_s(1);
        }
    }

    z_drop(z_move(qable));
    z_drop(z_move(s));
    z_drop(z_move(provider));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_queryable_shm [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression matching queries to reply to\n\
        -p, --payload <PAYLOAD> (optional, string, default='%s'): The value to reply to queries with\n\
        --complete (optional, flag to indicate whether queryable is complete or not)",
        DEFAULT_KEYEXPR, DEFAULT_VALUE);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char **argv, z_owned_config_t *config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char *), (char *)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char *), (char *)DEFAULT_VALUE);
    args.complete = _Z_CHECK_FLAG("complete");

    parse_zenoh_common_args(argc, argv, config);
    const char *arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char **pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_queryable_with_channels.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-queryable"
#define DEFAULT_VALUE "Queryable from C!"

struct args_t {
    char* keyexpr;  // -k, --key
    char* value;    // -p, --payload
    bool complete;  // --complete
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

z_view_keyexpr_t ke;

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    if (z_view_keyexpr_from_str(&ke, args.keyexpr) < 0) {
        printf("%s is not a valid key expression", args.keyexpr);
        exit(-1);
    }

    printf("Declaring Queryable on '%s'...\n", args.keyexpr);
    z_owned_fifo_handler_query_t handler;
    z_owned_closure_query_t closure;
    z_fifo_channel_query_new(&closure, &handler, 16);
    z_owned_queryable_t qable;

    z_queryable_options_t opts;
    z_queryable_options_default(&opts);
    opts.complete = args.complete;

    if (z_declare_queryable(z_loan(s), &qable, z_loan(ke), z_move(closure), &opts) < 0) {
        printf("Unable to create queryable.\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    z_owned_query_t oquery;
    while (z_recv(z_loan(handler), &oquery) == Z_OK) {
        const z_loaned_query_t* query = z_loan(oquery);
        z_view_string_t key_string;
        z_keyexpr_as_view_string(z_query_keyexpr(query), &key_string);

        z_view_string_t params;
        z_query_parameters(query, &params);

        const z_loaned_bytes_t* payload = z_query_payload(query);
        if (payload != NULL && z_bytes_len(payload) > 0) {
            z_owned_string_t payload_string;
            z_bytes_to_string(payload, &payload_string);

            printf(">> [Queryable ] Received Query '%.*s?%.*s' with value '%.*s'\n",
                   (int)z_string_len(z_loan(key_string)), z_string_data(z_loan(key_string)),
                   (int)z_string_len(z_loan(params)), z_string_data(z_loan(params)),
                   (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)));
            z_drop(z_move(payload_string));
        } else {
            printf(">> [Queryable ] Received Query '%.*s?%.*s'\n", (int)z_string_len(z_loan(key_string)),
                   z_string_data(z_loan(key_string)), (int)z_string_len(z_loan(params)), z_string_data(z_loan(params)));
        }
        z_query_reply_options_t options;
        z_query_reply_options_default(&options);

        z_owned_bytes_t reply_payload;
        z_bytes_from_static_str(&reply_payload, args.value);
        z_query_reply(query, z_loan(ke), z_move(reply_payload), &options);
        z_drop(z_move(oquery));
    }

    z_drop(z_move(qable));
    z_drop(z_move(handler));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_queryable_with_channels [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression matching queries to reply to\n\
        -p, --payload <PAYLOAD> (optional, string, default='%s'): The value to reply to queries with\n\
        --complete (optional, flag to indicate whether queryable is complete or not)",
        DEFAULT_KEYEXPR, DEFAULT_VALUE);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char*), (char*)DEFAULT_VALUE);
    args.complete = _Z_CHECK_FLAG("complete");

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_queryable.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/zenoh-c-queryable"
#define DEFAULT_VALUE "Queryable from C!"
z_view_keyexpr_t ke;

struct args_t {
    char *keyexpr;  // -k, --key
    char *value;    // -p, --payload
    bool complete;  // --complete
};

char *value;

struct args_t parse_args(int argc, char **argv, z_owned_config_t *config);

void query_handler(z_loaned_query_t *query, void *context) {
    z_view_string_t key_string;
    z_keyexpr_as_view_string(z_query_keyexpr(query), &key_string);

    z_view_string_t params;
    z_query_parameters(query, &params);

    const z_loaned_bytes_t *payload = z_query_payload(query);
    if (payload != NULL && z_bytes_len(payload) > 0) {
        z_owned_string_t payload_string;
        z_bytes_to_string(payload, &payload_string);

        printf(">> [Queryable ] Received Query '%.*s?%.*s' with value '%.*s'\n", (int)z_string_len(z_loan(key_string)),
               z_string_data(z_loan(key_string)), (int)z_string_len(z_loan(params)), z_string_data(z_loan(params)),
               (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)));
        z_drop(z_move(payload_string));
    } else {
        printf(">> [Queryable ] Received Query '%.*s?%.*s'\n", (int)z_string_len(z_loan(key_string)),
               z_string_data(z_loan(key_string)), (int)z_string_len(z_loan(params)), z_string_data(z_loan(params)));
    }
    z_query_reply_options_t options;
    z_query_reply_options_default(&options);

    z_owned_bytes_t reply_payload;
    z_bytes_from_static_str(&reply_payload, (char *)value);

    z_view_keyexpr_t reply_keyexpr;
    z_view_keyexpr_from_str(&reply_keyexpr, (const char *)context);
    printf(">> [Queryable ] Responding ('%s': '%s')\n", (const char *)context, value);

    z_query_reply(query, z_loan(reply_keyexpr), z_move(reply_payload), &options);
}

int main(int argc, char **argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);
    value = args.value;

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    if (z_view_keyexpr_from_str(&ke, args.keyexpr) < 0) {
        printf("%s is not a valid key expression", args.keyexpr);
        exit(-1);
    }

    printf("Declaring Queryable on '%s'...\n", args.keyexpr);
    z_owned_closure_query_t callback;
    z_closure(&callback, query_handler, NULL, (void *)args.keyexpr);
    z_owned_queryable_t qable;

    z_queryable_options_t opts;
    z_queryable_options_default(&opts);
    opts.complete = args.complete;

    if (z_declare_queryable(z_loan(s), &qable, z_loan(ke), z_move(callback), &opts) < 0) {
        printf("Unable to create queryable.\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    while (1) {
        z_sleep_s(1);
    }

    z_drop(z_move(qable));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_queryable [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression matching queries to reply to\n\
        -p, --payload <PAYLOAD> (optional, string, default='%s'): The value to reply to queries with\n\
        --complete (optional): Indicates whether queryable is complete or not",
        DEFAULT_KEYEXPR, DEFAULT_VALUE);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char **argv, z_owned_config_t *config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char *), (char *)DEFAULT_KEYEXPR);
    _Z_PARSE_ARG(args.value, "p", "payload", (char *), (char *)DEFAULT_VALUE);
    args.complete = _Z_CHECK_FLAG("complete");

    parse_zenoh_common_args(argc, argv, config);
    const char *arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char **pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_scout.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>

#include <stdio.h>

#include "zenoh.h"

void fprintpid(FILE *stream, z_id_t pid) {
    z_owned_string_t str;
    z_id_to_string(&pid, &str);
    fprintf(stream, "%.*s", (int)z_string_len(z_loan(str)), z_string_data(z_loan(str)));
    z_drop(z_move(str));
}

void fprintwhatami(FILE *stream, z_whatami_t whatami) {
    z_view_string_t whatami_str;
    z_whatami_to_view_string(whatami, &whatami_str);
    fprintf(stream, "%.*s", (int)z_string_len(z_loan(whatami_str)), z_string_data(z_loan(whatami_str)));
}

void fprintlocators(FILE *stream, const z_loaned_string_array_t *locs) {
    fprintf(stream, "[");
    for (unsigned int i = 0; i < z_string_array_len(locs); i++) {
        const z_loaned_string_t *loc = z_string_array_get(locs, i);
        fprintf(stream, "%.*s", (int)z_string_len(loc), z_string_data(loc));
        if (i < z_string_array_len(locs) - 1) {
            fprintf(stream, ", ");
        }
    }
    fprintf(stream, "]");
}

void fprinthello(FILE *stream, const z_loaned_hello_t *hello) {
    fprintf(stream, "Hello { pid: ");

    fprintpid(stream, z_hello_zid(hello));
    fprintf(stream, ", whatami: ");
    fprintwhatami(stream, z_hello_whatami(hello));

    fprintf(stream, ", locators: ");
    z_owned_string_array_t locators;
    z_hello_locators(hello, &locators);
    fprintlocators(stream, z_loan(locators));
    z_string_array_drop(z_move(locators));

    fprintf(stream, " }");
}

void callback(z_loaned_hello_t *hello, void *context) {
    fprinthello(stdout, hello);
    fprintf(stdout, "\n");
    (*(int *)context)++;
}

void drop(void *context) {
    printf("Dropping scout\n");
    int count = *(int *)context;
    z_free(context);
    if (!count) {
        printf("Did not find any zenoh process.\n");
    }
}

int main(int argc, char **argv) {
    zc_init_log_from_env_or("error");

    int *context = z_malloc(sizeof(int));
    *context = 0;
    z_owned_config_t config;
    z_config_default(&config);

    z_owned_closure_hello_t closure;
    z_closure(&closure, callback, drop, context);
    printf("Scouting...\n");
    z_scout(z_move(config), z_move(closure), NULL);
    z_sleep_s(1);
    return 0;
}
```

---

# Example: examples--z_storage.c

```c
//
// Copyright (c) 2025 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>
#include <string.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/**"
#define STORAGE_NUM_BINS 256

struct node_t;
typedef struct node_t node_t;

struct node_t {
    z_owned_sample_t sample;
    node_t* next;
    node_t* prev;
};

typedef struct {
    node_t** nodes;
    size_t num_bins;
} storage_t;

typedef struct {
    size_t bin;
    node_t* node;
} storage_iterator_t;

storage_t storage;
z_owned_mutex_t storage_mutex;

struct args_t {
    char* keyexpr;  // -k, --key
    bool complete;  // --complete
};

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);
const char* kind_to_str(z_sample_kind_t kind);

storage_t storage_new(size_t num_bins);
void storage_insert(storage_t* storage, const z_loaned_sample_t* sample);
z_owned_sample_t* storage_find(storage_t* storage, const z_loaned_string_t* key);
void storage_remove(storage_t* storage, const z_loaned_keyexpr_t* keyexpr);
void storage_drop(storage_t* storage);
storage_iterator_t storage_begin(storage_t* storage);
bool storage_is_end(storage_t* storage, storage_iterator_t it);
z_owned_sample_t* storage_iterator_value(storage_iterator_t it);
storage_iterator_t storage_iterator_next(storage_t* storage, storage_iterator_t it);

void sub_handler(z_loaned_sample_t* sample, void* arg) {
    z_view_string_t key_string;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_string);

    z_owned_string_t payload_string;
    z_bytes_to_string(z_sample_payload(sample), &payload_string);

    printf(">> [Subscriber] Received %s ('%.*s': '%.*s')\n", kind_to_str(z_sample_kind(sample)),
           (int)z_string_len(z_loan(key_string)), z_string_data(z_loan(key_string)),
           (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)));
    z_drop(z_move(payload_string));
    z_mutex_lock(z_loan_mut(storage_mutex));
    switch (z_sample_kind(sample)) {
        case Z_SAMPLE_KIND_PUT:
            storage_insert(&storage, sample);
            break;
        case Z_SAMPLE_KIND_DELETE:
            storage_remove(&storage, z_sample_keyexpr(sample));
            break;
    }
    z_mutex_unlock(z_loan_mut(storage_mutex));
}

void query_handler(z_loaned_query_t* query, void* context) {
    z_mutex_lock(z_loan_mut(storage_mutex));
    storage_iterator_t it = storage_begin(&storage);
    while (!storage_is_end(&storage, it)) {
        const z_loaned_sample_t* sample = z_loan(*storage_iterator_value(it));
        if (z_keyexpr_intersects(z_query_keyexpr(query), z_sample_keyexpr(sample))) {
            z_owned_bytes_t payload;
            z_bytes_clone(&payload, z_sample_payload(sample));
            z_query_reply(query, z_sample_keyexpr(sample), z_move(payload), NULL);
        }
        it = storage_iterator_next(&storage, it);
    }
    z_mutex_unlock(z_loan_mut(storage_mutex));
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_mutex_init(&storage_mutex);
    storage = storage_new(STORAGE_NUM_BINS);

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_owned_closure_sample_t sub_callback;
    z_closure(&sub_callback, sub_handler, NULL, NULL);
    printf("Declaring Subscriber on '%s'...\n", args.keyexpr);
    z_owned_subscriber_t sub;
    if (z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(sub_callback), NULL) < 0) {
        printf("Unable to declare subscriber.\n");
        exit(-1);
    }

    printf("Declaring Queryable on '%s'...\n", args.keyexpr);
    z_owned_closure_query_t query_callback;
    z_closure(&query_callback, query_handler, NULL, (void*)args.keyexpr);
    z_owned_queryable_t qable;

    z_queryable_options_t opts;
    z_queryable_options_default(&opts);
    opts.complete = args.complete;

    if (z_declare_queryable(z_loan(s), &qable, z_loan(ke), z_move(query_callback), &opts) < 0) {
        printf("Unable to create queryable.\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    while (1) {
        z_sleep_s(1);
    }

    z_drop(z_move(qable));
    z_drop(z_move(sub));
    z_drop(z_move(s));
    z_mutex_drop(z_move(storage_mutex));
    storage_drop(&storage);
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_storage [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The selection of resources to store\n\
        --complete (optional): Declare the storage as complete w.r.t. the key expression",
        DEFAULT_KEYEXPR);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    args.complete = _Z_CHECK_FLAG("complete");
    parse_zenoh_common_args(argc, argv, config);
    const char* unknown_arg = check_unknown_opts(argc, argv);
    if (unknown_arg) {
        printf("Unknown option %s\n", unknown_arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}

size_t _storage_hash_string(const z_loaned_string_t* s) {
    size_t hash = 5381;
    size_t len = z_string_len(s);
    const char* data = z_string_data(s);
    for (size_t i = 0; i < len; ++i) {
        hash = ((hash << 5) + hash) + (size_t)data[i];
    }
    return hash;
}

size_t _storage_compare_string(const z_loaned_string_t* s1, const z_loaned_string_t* s2) {
    size_t len1 = z_string_len(s1);
    const char* data1 = z_string_data(s1);
    size_t len2 = z_string_len(s2);
    const char* data2 = z_string_data(s2);
    return len1 == len2 && strncmp(data1, data2, len1) == 0;
}

node_t* _storage_find(node_t* hash_bin, const z_loaned_string_t* key) {
    node_t* node = hash_bin;
    while (node != NULL) {
        z_view_string_t key_string;
        z_keyexpr_as_view_string(z_sample_keyexpr(z_loan(node->sample)), &key_string);
        if (_storage_compare_string(z_loan(key_string), key)) {
            return node;
        }
        node = node->next;
    }
    return NULL;
}

z_owned_sample_t* storage_find(storage_t* storage, const z_loaned_string_t* key) {
    size_t hash = _storage_hash_string(key);
    size_t bin = hash % storage->num_bins;
    node_t* res = _storage_find(storage->nodes[bin], key);
    if (res == NULL) {
        return NULL;
    }
    return &res->sample;
}

void storage_insert(storage_t* storage, const z_loaned_sample_t* sample) {
    z_view_string_t key;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key);

    size_t hash = _storage_hash_string(z_loan(key));
    size_t bin = hash % storage->num_bins;
    node_t* res = _storage_find(storage->nodes[bin], z_loan(key));
    if (res != NULL) {
        z_drop(z_move(res->sample));
    } else if (storage->nodes[bin] == NULL) {
        res = (node_t*)z_malloc(sizeof(node_t));
        res->prev = NULL;
        res->next = NULL;
        storage->nodes[bin] = res;
    } else {
        res = storage->nodes[bin];
        while (res->next != NULL) res = res->next;
        res->next = (node_t*)z_malloc(sizeof(node_t));
        res->next->prev = res;
        res = res->next;
        res->next = NULL;
    }
    z_sample_clone(&res->sample, sample);
}

void storage_remove(storage_t* storage, const z_loaned_keyexpr_t* keyexpr) {
    z_view_string_t key;
    z_keyexpr_as_view_string(keyexpr, &key);

    size_t hash = _storage_hash_string(z_loan(key));
    size_t bin = hash % storage->num_bins;
    node_t* res = _storage_find(storage->nodes[bin], z_loan(key));
    if (res == NULL) {
        return;
    }
    if (res->prev == NULL) {
        storage->nodes[bin] = res->next;
    } else {
        res->prev->next = res->next;
    }
    if (res->next != NULL) {
        res->next->prev = res->prev;
    }

    z_drop(z_move(res->sample));
    z_free(res);
}

storage_t storage_new(size_t num_bins) {
    storage_t storage;
    storage.num_bins = num_bins;
    storage.nodes = (node_t**)z_malloc(sizeof(node_t*) * num_bins);
    for (size_t i = 0; i < num_bins; ++i) {
        storage.nodes[i] = NULL;
    }
    return storage;
}

void storage_drop(storage_t* storage) {
    for (size_t i = 0; i < storage->num_bins; ++i) {
        node_t* node = storage->nodes[i];
        while (node != NULL) {
            z_drop(z_move(node->sample));
            node_t* to_free = node;
            node = node->next;
            z_free(to_free);
        }
    }
    z_free(storage->nodes);
}

storage_iterator_t _storage_first_non_empty_bin(storage_t* storage, size_t start) {
    while (start < storage->num_bins) {
        if (storage->nodes[start] != NULL) {
            return (storage_iterator_t){.bin = start, .node = storage->nodes[start]};
        }
        start++;
    }
    return (storage_iterator_t){.bin = start, .node = NULL};
}

storage_iterator_t storage_begin(storage_t* storage) { return _storage_first_non_empty_bin(storage, 0); }

bool storage_is_end(storage_t* storage, storage_iterator_t it) { return it.bin >= storage->num_bins; }

z_owned_sample_t* storage_iterator_value(storage_iterator_t it) { return &it.node->sample; }

storage_iterator_t storage_iterator_next(storage_t* storage, storage_iterator_t it) {
    if (it.node->next != NULL) {
        return (storage_iterator_t){.bin = it.bin, .node = it.node->next};
    }
    return _storage_first_non_empty_bin(storage, it.bin + 1);
}

const char* kind_to_str(z_sample_kind_t kind) {
    switch (kind) {
        case Z_SAMPLE_KIND_PUT:
            return "PUT";
        case Z_SAMPLE_KIND_DELETE:
            return "DELETE";
        default:
            return "UNKNOWN";
    }
}
```

---

# Example: examples--z_sub_liveliness.c

```c
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "group1/**"

struct args_t {
    char* keyexpr;  // -k, --key
    bool history;   // --history
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);

void data_handler(z_loaned_sample_t* sample, void* arg) {
    z_view_string_t key_string;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_string);
    switch (z_sample_kind(sample)) {
        case Z_SAMPLE_KIND_PUT:
            printf(">> [LivelinessSubscriber] New alive token ('%.*s')\n", (int)z_string_len(z_loan(key_string)),
                   z_string_data(z_loan(key_string)));
            break;
        case Z_SAMPLE_KIND_DELETE:
            printf(">> [LivelinessSubscriber] Dropped token ('%.*s')\n", (int)z_string_len(z_loan(key_string)),
                   z_string_data(z_loan(key_string)));
            break;
    }
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);
    z_view_keyexpr_t ke;
    if (z_view_keyexpr_from_str(&ke, args.keyexpr) < 0) {
        printf("%s is not a valid key expression\n", args.keyexpr);
        exit(-1);
    }

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    printf("Declaring liveliness subscriber on '%s'...\n", args.keyexpr);
    z_owned_closure_sample_t callback;
    z_closure(&callback, data_handler, NULL, NULL);
    z_liveliness_subscriber_options_t opts;
    z_liveliness_subscriber_options_default(&opts);
    opts.history = args.history;
    z_owned_subscriber_t sub;
    if (z_liveliness_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(callback), &opts) < 0) {
        printf("Unable to declare liveliness subscriber.\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    while (1) {
        z_sleep_s(1);
    }

    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_sub_liveliness [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression matching liveliness tokens to subscribe to\n\
        --history (optional): Get historical liveliness tokens.\n",
        DEFAULT_KEYEXPR);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);
    args.history = _Z_CHECK_FLAG("history");

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_sub_shm.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/**"

struct args_t {
    char *keyexpr;  // -k, --key
};
struct args_t parse_args(int argc, char **argv, z_owned_config_t *config);

const char *kind_to_str(z_sample_kind_t kind);

void data_handler(z_loaned_sample_t *sample, void *arg) {
    z_view_string_t key_string;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_string);

// if Zenoh is built without SHM support, the only buffer type it can receive is RAW
#if !defined(Z_FEATURE_SHARED_MEMORY)
    char *payload_type = "RAW";
#endif

// if Zenoh is built with SHM support but without SHM API (that is unstable), it can
// receive buffers of any type, but there is no way to detect the buffer type
#if defined(Z_FEATURE_SHARED_MEMORY) && !defined(Z_FEATURE_UNSTABLE_API)
    char *payload_type = "UNKNOWN";
#endif

// if Zenoh is built with SHM support and with SHM API, we can detect the exact buffer type
#if defined(Z_FEATURE_SHARED_MEMORY) && defined(Z_FEATURE_UNSTABLE_API)
    char *payload_type = "RAW";
    {
        // try to convert sample payload into SHM buffer. The conversion will succeed
        // only if payload is carrying underlying SHM buffer
        z_loaned_shm_t *shm = NULL;
        if (z_bytes_as_mut_loaned_shm(z_sample_payload_mut(sample), &shm) == Z_OK) {
            // try to get mutable access to SHM buffer
            z_loaned_shm_mut_t *shm_mut = z_shm_try_reloan_mut(shm);
            if (shm_mut) {
                payload_type = "SHM (MUT)";
            } else {
                payload_type = "SHM (IMMUT)";
            }
        }
    }
#endif

    z_owned_string_t payload_string;
    z_bytes_to_string(z_sample_payload(sample), &payload_string);

    printf(">> [Subscriber] Received %s ('%.*s': '%.*s') [%s]", kind_to_str(z_sample_kind(sample)),
           (int)z_string_len(z_loan(key_string)), z_string_data(z_loan(key_string)),
           (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)), payload_type);

    const z_loaned_bytes_t *attachment = z_sample_attachment(sample);
    // checks if attachment exists
    if (attachment != NULL) {
        z_owned_string_t attachment_string;
        z_bytes_to_string(attachment, &attachment_string);
        printf(" (%.*s)", (int)z_string_len(z_loan(attachment_string)), z_string_data(z_loan(attachment_string)));
        z_drop(z_move(attachment_string));
    }
    printf("\n");

    z_drop(z_move(payload_string));
}

int main(int argc, char **argv) {
    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);

    zc_init_log_from_env_or("error");

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_owned_closure_sample_t callback;
    z_closure(&callback, data_handler, NULL, NULL);
    printf("Declaring Subscriber on '%s'...\n", args.keyexpr);
    z_owned_subscriber_t sub;
    if (z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(callback), NULL) < 0) {
        printf("Unable to declare subscriber.\n");
        exit(-1);
    }

    printf("Enter 'q' to quit...\n");
    char c = 0;
    while (c != 'q') {
        c = getchar();
        if (c == -1) {
            z_sleep_s(1);
        }
    }

    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}

const char *kind_to_str(z_sample_kind_t kind) {
    switch (kind) {
        case Z_SAMPLE_KIND_PUT:
            return "PUT";
        case Z_SAMPLE_KIND_DELETE:
            return "DELETE";
        default:
            return "UNKNOWN";
    }
}

void print_help() {
    printf(
        "\
    Usage: z_sub_shm [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to subscribe to\n",
        DEFAULT_KEYEXPR);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char **argv, z_owned_config_t *config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char *), (char *)DEFAULT_KEYEXPR);

    parse_zenoh_common_args(argc, argv, config);
    const char *arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char **pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_sub_thr.c

```c
//
// Copyright (c) 2022 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdio.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_MEASUREMENTS 10
#define DEFAULT_MESSAGES 1000000

typedef struct {
    unsigned long samples;       // -s, --samples
    unsigned long num_messages;  // -n, --number
} args_t;

args_t parse_args(int argc, char **argv, z_owned_config_t *config);

typedef struct {
    volatile unsigned long count;
    volatile unsigned long finished_rounds;
    z_clock_t start;
    z_clock_t first_start;
    bool started;
    unsigned long max_rounds;
    unsigned long messages_per_round;
} z_stats_t;

z_stats_t *z_stats_make(unsigned long max_rounds, unsigned long messages_per_round) {
    z_stats_t *stats = z_malloc(sizeof(z_stats_t));
    stats->count = 0;
    stats->finished_rounds = 0;
    stats->started = false;
    stats->max_rounds = max_rounds;
    stats->messages_per_round = messages_per_round;
    return stats;
}

void on_sample(z_loaned_sample_t *sample, void *context) {
    z_stats_t *stats = (z_stats_t *)context;
    if (stats->count == 0) {
        stats->start = z_clock_now();
        if (!stats->started) {
            stats->first_start = stats->start;
            stats->started = true;
        }
        stats->count++;
    } else if (stats->count < stats->messages_per_round) {
        stats->count++;
    } else {
        stats->finished_rounds++;
        printf("%f msg/s\n", 1000.0 * stats->messages_per_round / z_clock_elapsed_ms(&stats->start));
        stats->count = 0;
        if (stats->finished_rounds > stats->max_rounds) {
            exit(0);
        }
    }
}
void drop_stats(void *context) {
    const z_stats_t *stats = (z_stats_t *)context;
    const unsigned long sent_messages = stats->messages_per_round * stats->finished_rounds + stats->count;
    double elapsed_s = z_clock_elapsed_s(&stats->first_start);
    printf("Stats being dropped after unsubscribing: sent %ld messages over %f seconds (%f msg/s)\n", sent_messages,
           elapsed_s, (double)sent_messages / elapsed_s);
    z_free(context);
}

int main(int argc, char **argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    args_t args = parse_args(argc, argv, &config);

#if defined(Z_FEATURE_SHARED_MEMORY)
    // A probing procedure for shared memory is performed upon session opening. To operate over shared memory
    // (and to not fallback on network mode), shared memory needs to be enabled in the configuration.
    if (zc_config_insert_json5(z_loan_mut(config), Z_CONFIG_SHARED_MEMORY_KEY, "true") < 0) {
        printf(
            "Couldn't insert value `true` in configuration at `%s`. This is likely because `%s` expects a "
            "JSON-serialized value\n",
            Z_CONFIG_SHARED_MEMORY_KEY, Z_CONFIG_SHARED_MEMORY_KEY);
        exit(-1);
    }
#endif

    z_owned_session_t s;

    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, "test/thr");

    z_stats_t *context = z_stats_make(args.samples, args.num_messages);
    z_owned_closure_sample_t callback;
    z_closure(&callback, on_sample, drop_stats, context);
    if (z_declare_background_subscriber(z_loan(s), z_loan(ke), z_move(callback), NULL) < 0) {
        printf("Unable to create subscriber.\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    while (1) {
        z_sleep_s(1);
    }

    z_drop(z_move(s));
    return 0;
}

void print_help() {
    printf(
        "\
    Usage: z_sub_thr [OPTIONS]\n\n\
    Options:\n\
        -s, --samples <MESUREMENTS> (optional, number, default='%d'): Number of throughput measurements.\n\
        -n, --number <NUM_MESSAGES> (optional, number, default='%d'): Number of messages in each throughput measurements.\n",
        DEFAULT_MEASUREMENTS, DEFAULT_MESSAGES);
    printf(COMMON_HELP);
}

args_t parse_args(int argc, char **argv, z_owned_config_t *config) {
    _Z_CHECK_HELP;
    args_t args;
    _Z_PARSE_ARG(args.samples, "s", "samples", atoi, DEFAULT_MEASUREMENTS);
    _Z_PARSE_ARG(args.num_messages, "n", "number", atoi, DEFAULT_MESSAGES);

    parse_zenoh_common_args(argc, argv, config);
    const char *arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char **pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

# Example: examples--z_sub.c

```c
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#include <stdint.h>
#include <stdio.h>

#include "parse_args.h"
#include "zenoh.h"

#define DEFAULT_KEYEXPR "demo/example/**"

struct args_t {
    char* keyexpr;  // -k, --key
};
struct args_t parse_args(int argc, char** argv, z_owned_config_t* config);
const char* kind_to_str(z_sample_kind_t kind);

void data_handler(z_loaned_sample_t* sample, void* arg) {
    z_view_string_t key_string;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_string);

    z_owned_string_t payload_string;
    z_bytes_to_string(z_sample_payload(sample), &payload_string);

    printf(">> [Subscriber] Received %s ('%.*s': '%.*s')", kind_to_str(z_sample_kind(sample)),
           (int)z_string_len(z_loan(key_string)), z_string_data(z_loan(key_string)),
           (int)z_string_len(z_loan(payload_string)), z_string_data(z_loan(payload_string)));

    const z_loaned_bytes_t* attachment = z_sample_attachment(sample);
    // checks if attachment exists
    if (attachment != NULL) {
        z_owned_string_t attachment_string;
        z_bytes_to_string(attachment, &attachment_string);
        printf(" (%.*s)", (int)z_string_len(z_loan(attachment_string)), z_string_data(z_loan(attachment_string)));
        z_drop(z_move(attachment_string));
    }
    printf("\n");
    z_drop(z_move(payload_string));
}

int main(int argc, char** argv) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    struct args_t args = parse_args(argc, argv, &config);
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, args.keyexpr);

    printf("Opening session...\n");
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        exit(-1);
    }

    z_owned_closure_sample_t callback;
    z_closure(&callback, data_handler, NULL, NULL);
    printf("Declaring Subscriber on '%s'...\n", args.keyexpr);
    z_owned_subscriber_t sub;
    if (z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(callback), NULL) < 0) {
        printf("Unable to declare subscriber.\n");
        exit(-1);
    }

    printf("Press CTRL-C to quit...\n");
    while (1) {
        z_sleep_s(1);
    }

    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}

const char* kind_to_str(z_sample_kind_t kind) {
    switch (kind) {
        case Z_SAMPLE_KIND_PUT:
            return "PUT";
        case Z_SAMPLE_KIND_DELETE:
            return "DELETE";
        default:
            return "UNKNOWN";
    }
}

void print_help() {
    printf(
        "\
    Usage: z_sub [OPTIONS]\n\n\
    Options:\n\
        -k, --key <KEYEXPR> (optional, string, default='%s'): The key expression to subscribe to\n",
        DEFAULT_KEYEXPR);
    printf(COMMON_HELP);
}

struct args_t parse_args(int argc, char** argv, z_owned_config_t* config) {
    _Z_CHECK_HELP;
    struct args_t args;
    _Z_PARSE_ARG(args.keyexpr, "k", "key", (char*), (char*)DEFAULT_KEYEXPR);

    parse_zenoh_common_args(argc, argv, config);
    const char* arg = check_unknown_opts(argc, argv);
    if (arg) {
        printf("Unknown option %s\n", arg);
        exit(-1);
    }
    char** pos_args = parse_pos_args(argc, argv, 1);
    if (!pos_args || pos_args[0]) {
        printf("Unexpected positional arguments\n");
        free(pos_args);
        exit(-1);
    }
    free(pos_args);
    return args;
}
```

---

