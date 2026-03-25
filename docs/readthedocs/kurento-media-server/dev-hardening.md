# Security Hardening

*Hardening* is a set of mechanisms that can be activated by turning on several compiler flags, and are commonly used to protect resulting programs against memory corruption attacks. These mechanisms have been standard practice since at least 2011, when the Debian project set on the goal of releasing all their packages with the security hardening build flags enabled 1. Ubuntu has also followed the same policy regarding their own build procedures 2.

Kurento Media Server had been lagging in this respect, and old releases only implemented the standard Debian hardening options [https://wiki.debian.org/HardeningWalkthrough#Selecting_security_hardening_options] that are applied by the *dpkg-buildflags* tool by default:

- 

**Format string checks** (`-Wformat -Werror=format-security`) 3. These options instruct the compiler to make sure that the arguments supplied to string functions such as *printf* and *scanf* have types appropriate to the format string specified, and that the conversions specified in the format string make sense.

- 

**Fortify Source** (`-D_FORTIFY_SOURCE=2`) 4. When this macro is defined at compilation time, several compile-time and run-time protections are enabled around unsafe use of some glibc string and memory functions such as *memcpy* and *strcpy*, with get replaced by their safer counterparts. This feature can prevent some buffer overflow attacks, but it requires optimization level `-O1` or higher so it is not enabled in Debug builds (which use `-O0`).

- 

**Stack protector** (`-fstack-protector-strong`) 5. This compiler option provides a randomized stack canary that protects against *stack smashing* attacks that could lead to buffer overflows, and reduces the chances of arbitrary code execution via controlling return address destinations.

- 

**Read-Only Relocations** (RELRO) (`-Wl,-z,relro`). This linker option marks any regions of the relocation table as “read-only” if they were resolved before execution begins. This reduces the possible areas of memory in a program that can be used by an attacker that performs a successful *GOT-overwrite* memory corruption exploit. This option works best with the linker’s *Immediate Binding* mode, which forces *all* regions of the relocation table to be resolved before execution begins. However, immediate binding is disabled by default.

Starting from version **6.7**, KMS also implements these extra hardening measurements:

- 

**Position Independent Code** (`-fPIC`) / **Position Independent Executable** (`-fPIE -pie`) 6. Allows taking advantage of the Address Space Layout Randomization (ASLR) [https://en.wikipedia.org/wiki/en,Address_space_layout_randomization] protection offered by the Kernel. This protects against Return-Oriented Programming (ROP) [https://en.wikipedia.org/wiki/en,Return-oriented_programming] attacks and generally frustrates memory corruption attacks. This option was initially made the default in Ubuntu 16.10 for some selected architectures, and in Ubuntu 17.10 was finally enabled by default across all architectures supported by Ubuntu.

Note

The *PIC*/*PIE* feature adds a very valuable protection against attacks, but has one important requisite: *all shared objects must be compiled as position-independent code*. If your shared library has stopped linking with KMS, or your plugin stopped loading at run-time, try recompiling your code with the `-fPIC` option.