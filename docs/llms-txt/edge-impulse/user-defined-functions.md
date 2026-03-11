# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/cpp/user-defined-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User-defined

These functions are required to be implemented by the user for the target platform. See [this porting guide](/hardware/porting-guide) for more information. They are declared internally in the Edge Impulse C++ SDK library, and they must be defined by the user.

**Source**: [porting/ei\_classifier\_porting.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/ei_classifier_porting.h)

**Examples**: The following examples demonstrate possible implementations of this function for various platforms. Note the `__attribute__((weak))` in most of the definitions, which means that a user could override the implementation elsewhere in the program:

* [Arduino classifier porting](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/arduino/ei_classifier_porting.cpp)

* [mbed classifier porting](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/mbed/ei_classifier_porting.cpp)

* [POSIX classifier porting](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/posix/ei_classifier_porting.cpp)

* [Silicon Labs classifier porting](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/silabs/ei_classifier_porting.cpp)

* [STM32 classifier porting](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/stm32-cubeai/ei_classifier_porting.cpp)

* [TI classifier porting](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/ti/debug_log.cpp)

* [Zephyr classifier porting](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/porting/zephyr/ei_classifier_porting.cpp)

## ei\_sleep

```cpp  theme={"system"}
public EI_IMPULSE_ERROR ei_sleep(
    int32_t time_ms
)
```

**Brief**: Cancellable sleep, can be triggered with signal from other thread.

**Description**:
Cancellable sleep, can be triggered with signal from other thread Allow the processor or thread to sleep or block for the given time.

#### Parameters

* `time_ms` Time in milliseconds to sleep

#### Returns

`EI_IMPULSE_OK` if successful, error code otherwise

## ei\_read\_timer\_ms

```cpp  theme={"system"}
public uint64_t ei_read_timer_ms(

)
```

**Brief**: Read the millisecond timer.

**Description**:
Read the millisecond timer This function should return the number of milliseconds that have passed since the start of the program. If you do not need to determine the run times for DSP and inference blocks, you can simply return 0 from this function. Your impulse will still work correctly without timing information.

#### Returns

The number of milliseconds that have passed since the start of the program

## ei\_read\_timer\_us

```cpp  theme={"system"}
public uint64_t ei_read_timer_us(

)
```

**Brief**: Read the microsecond timer.

**Description**:
This function should return the number of milliseconds that have passed since the start of the program. If you do not need to determine the run times for DSP and inference blocks, you can simply return 0 from this function. Your impulse will still work correctly without timing information.

#### Returns

The number of microseconds that have passed since the start of the program

## ei\_putchar

```cpp  theme={"system"}
public void ei_putchar(
    char c
)
```

**Brief**: Send a single character to the serial port.

**Description**:

#### Parameters

* `c` The character to send

## ei\_getchar

```cpp  theme={"system"}
public char ei_getchar(
    void
)
```

**Brief**: Read a single character from the serial port.

**Description**:

#### Returns

The character read from the serial port

## ei\_printf

```cpp  theme={"system"}
public void ei_printf(
    const char * format,
    ...
)
```

**Brief**: Print wrapper around printf()

**Description**:
`ei_printf()` is declared internally to the Edge Impulse SDK library so that debugging information (e.g. during inference) can be printed out. However, the function must be defined by the user, as printing methods can change depending on the platform and use case. For example, you may want to print debugging information to stdout in Linux or over a UART serial port on a microcontroller.

#### Parameters

* `format` Pointer to a character array or string that should be printed

* `...` Other optional arguments may be passed as necessary (e.g. handle to a UART object). Note that any calls to `ei_printf()` from within the *edge-impulse-sdk* library do not pass anything other than the `format` argument.

## ei\_printf\_float

```cpp  theme={"system"}
public void ei_printf_float(
    float f
)
```

**Brief**: Used to print floating point numbers.

**Description**:
Some platforms cannot handle directly printing floating point numbers (e.g. to a console or over a serial port). If your platform cannot directly print floats, provide an implementation of this function to print them as needed (for example, construct a string containing scientific notation with integers and call `ei_printf()`).

If your platform can print floating point values, the easiest implementation of this function is as follows:

```
__attribute__((weak)) void ei_printf_float(float f) {
    printf("%f", f);
}
```

#### Parameters

* `f` The floating point number to print

## ei\_malloc

```cpp  theme={"system"}
public void * ei_malloc(
    size_t size
)
```

**Brief**: Wrapper around malloc.

**Description**:
This function should allocate `size` bytes and return a pointer to the allocated memory. In bare-metal implementations, it can simply be a wrapper for `malloc()`. For example:

```
__attribute__((weak)) void *ei_malloc(size_t size) {
    return malloc(size);
}
```

If you intend to run your impulse in a multi-threaded environment, you will need to ensure that your implementation of `ei_malloc()` is thread-safe. For example, if you are using FreeRTOS, here is one possible implementation:

```
__attribute__((weak)) void *ei_malloc(size_t size) {
    return pvPortMalloc(size);
}
```

#### Parameters

* `size` The number of bytes to allocate

## ei\_calloc

```cpp  theme={"system"}
public void * ei_calloc(
    size_t nitems,
    size_t size
)
```

**Brief**: Wrapper around calloc.

**Description**:
This function should allocate `nitems * size` bytes and initialize all bytes in this allocated memory to 0. It should return a pointer to the allocated memory. In bare-metal implementations, it can simply be a wrapper for `calloc()`. For example:

```
__attribute__((weak)) void *ei_calloc(size_t nitems, size_t size) {
    return calloc(nitems, size);
}
```

If you intend to run your impulse in a multi-threaded environment, you will need to ensure that your implementation of `ei_calloc()` is thread-safe. For example, if you are using FreeRTOS, here is one possible implementation:

```
__attribute__((weak)) void *ei_calloc(size_t nitems, size_t size) {
    void *ptr = NULL;
    if (size > 0) {
        ptr = pvPortMalloc(nitems * size);
        if(ptr)
           memset(ptr, 0, (nitems * size));
    }
    return ptr;
}
```

#### Parameters

* `nitems` Number of blocks to allocate and clear

* `size` Size (in bytes) of each block

## ei\_free

```cpp  theme={"system"}
public void ei_free(
    void * ptr
)
```

**Brief**: Wrapper around free.

**Description**:
This function should free the memory space pointed to by `ptr`. If `ptr` is `NULL`, no operation should be performed. In bare-metal implementations, it can simply be a wrapper for `free()`. For example:

```
__attribute__((weak)) void ei_free(void *ptr) {
    free(ptr);
}
```

If you intend to run your impulse in a multi-threaded environment, you will need to ensure that your implementation of `ei_free()` is thread-safe. For example, if you are using FreeRTOS, here is one possible implementation:

```
__attribute__((weak)) void ei_free(void *ptr) {
    pvPortFree(ptr);
}
```

#### Parameters

* `ptr` Pointer to the memory to free


Built with [Mintlify](https://mintlify.com).