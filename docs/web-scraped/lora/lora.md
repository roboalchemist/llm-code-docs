# Source: https://hexdocs.pm/lora/

Title: LoRa — LoRa v1.0.1

URL Source: https://hexdocs.pm/lora/

Markdown Content:
LoRa — LoRa v1.0.1
===============

[LoRa](https://hexdocs.pm/lora/LoRa.html)

[![Image 1: LoRa](https://hexdocs.pm/lora/assets/logo.png)](https://hexdocs.pm/lora/LoRa.html)

*   [Pages](https://hexdocs.pm/lora/#full-list)
*   [Modules](https://hexdocs.pm/lora/#full-list)

*   [LoRa](https://hexdocs.pm/lora/LoRa.html)
    *   [Top](https://hexdocs.pm/lora/LoRa.html#content)
    *   [Summary](https://hexdocs.pm/lora/LoRa.html#summary)
    *   [Functions](https://hexdocs.pm/lora/LoRa.html#functions)
        *   [awake/1](https://hexdocs.pm/lora/LoRa.html#awake/1)
        *   [begin/2](https://hexdocs.pm/lora/LoRa.html#begin/2)
        *   [child_spec/1](https://hexdocs.pm/lora/LoRa.html#child_spec/1)
        *   [disable_crc/1](https://hexdocs.pm/lora/LoRa.html#disable_crc/1)
        *   [enable_crc/1](https://hexdocs.pm/lora/LoRa.html#enable_crc/1)
        *   [init/1](https://hexdocs.pm/lora/LoRa.html#init/1)
        *   [send/3](https://hexdocs.pm/lora/LoRa.html#send/3)
        *   [set_signal_bandwidth/2](https://hexdocs.pm/lora/LoRa.html#set_signal_bandwidth/2)
        *   [set_spreading_factor/2](https://hexdocs.pm/lora/LoRa.html#set_spreading_factor/2)
        *   [sleep/1](https://hexdocs.pm/lora/LoRa.html#sleep/1)
        *   [start_link/1](https://hexdocs.pm/lora/LoRa.html#start_link/1)

*   [LoRa.Communicator](https://hexdocs.pm/lora/LoRa.Communicator.html)
    *   [Top](https://hexdocs.pm/lora/LoRa.Communicator.html#content)
    *   [Summary](https://hexdocs.pm/lora/LoRa.Communicator.html#summary)
    *   [Functions](https://hexdocs.pm/lora/LoRa.Communicator.html#functions)
        *   [print/2](https://hexdocs.pm/lora/LoRa.Communicator.html#print/2)
        *   [read_register/2](https://hexdocs.pm/lora/LoRa.Communicator.html#read_register/2)
        *   [single_transfer/3](https://hexdocs.pm/lora/LoRa.Communicator.html#single_transfer/3)
        *   [write/3](https://hexdocs.pm/lora/LoRa.Communicator.html#write/3)
        *   [write_register/3](https://hexdocs.pm/lora/LoRa.Communicator.html#write_register/3)

*   [LoRa.Modem](https://hexdocs.pm/lora/LoRa.Modem.html)
    *   [Top](https://hexdocs.pm/lora/LoRa.Modem.html#content)
    *   [Summary](https://hexdocs.pm/lora/LoRa.Modem.html#summary)
    *   [Functions](https://hexdocs.pm/lora/LoRa.Modem.html#functions)
        *   [begin/3](https://hexdocs.pm/lora/LoRa.Modem.html#begin/3)
        *   [bit_write/3](https://hexdocs.pm/lora/LoRa.Modem.html#bit_write/3)
        *   [disable_crc/1](https://hexdocs.pm/lora/LoRa.Modem.html#disable_crc/1)
        *   [enable_crc/1](https://hexdocs.pm/lora/LoRa.Modem.html#enable_crc/1)
        *   [end_packet/3](https://hexdocs.pm/lora/LoRa.Modem.html#end_packet/3)
        *   [get_signal_band_width/1](https://hexdocs.pm/lora/LoRa.Modem.html#get_signal_band_width/1)
        *   [get_spreading_factor/1](https://hexdocs.pm/lora/LoRa.Modem.html#get_spreading_factor/1)
        *   [get_version/1](https://hexdocs.pm/lora/LoRa.Modem.html#get_version/1)
        *   [idle/1](https://hexdocs.pm/lora/LoRa.Modem.html#idle/1)
        *   [parse_packet/3](https://hexdocs.pm/lora/LoRa.Modem.html#parse_packet/3)
        *   [read/5](https://hexdocs.pm/lora/LoRa.Modem.html#read/5)
        *   [reset/1](https://hexdocs.pm/lora/LoRa.Modem.html#reset/1)
        *   [reset_fifo_payload/1](https://hexdocs.pm/lora/LoRa.Modem.html#reset_fifo_payload/1)
        *   [rssi/2](https://hexdocs.pm/lora/LoRa.Modem.html#rssi/2)
        *   [set_LNA_boost/1](https://hexdocs.pm/lora/LoRa.Modem.html#set_LNA_boost/1)
        *   [set_auto_AGC/1](https://hexdocs.pm/lora/LoRa.Modem.html#set_auto_AGC/1)
        *   [set_bandwidth/2](https://hexdocs.pm/lora/LoRa.Modem.html#set_bandwidth/2)
        *   [set_base_address/1](https://hexdocs.pm/lora/LoRa.Modem.html#set_base_address/1)
        *   [set_frequency/2](https://hexdocs.pm/lora/LoRa.Modem.html#set_frequency/2)
        *   [set_header_mode/2](https://hexdocs.pm/lora/LoRa.Modem.html#set_header_mode/2)
        *   [set_ldo_flag/1](https://hexdocs.pm/lora/LoRa.Modem.html#set_ldo_flag/1)
        *   [set_ocp/2](https://hexdocs.pm/lora/LoRa.Modem.html#set_ocp/2)
        *   [set_spreading_factor/2](https://hexdocs.pm/lora/LoRa.Modem.html#set_spreading_factor/2)
        *   [set_tx_power/2](https://hexdocs.pm/lora/LoRa.Modem.html#set_tx_power/2)
        *   [sleep/1](https://hexdocs.pm/lora/LoRa.Modem.html#sleep/1)
        *   [snr/1](https://hexdocs.pm/lora/LoRa.Modem.html#snr/1)
        *   [tx_done_flag/1](https://hexdocs.pm/lora/LoRa.Modem.html#tx_done_flag/1)
        *   [verify_end_packet/3](https://hexdocs.pm/lora/LoRa.Modem.html#verify_end_packet/3)

*   [LoRa.Parameters](https://hexdocs.pm/lora/LoRa.Parameters.html)
    *   [Top](https://hexdocs.pm/lora/LoRa.Parameters.html#content)
    *   [Summary](https://hexdocs.pm/lora/LoRa.Parameters.html#summary)
    *   [Functions](https://hexdocs.pm/lora/LoRa.Parameters.html#functions)
        *   [bw_freqs/0](https://hexdocs.pm/lora/LoRa.Parameters.html#bw_freqs/0)
        *   [header/1](https://hexdocs.pm/lora/LoRa.Parameters.html#header/1)
        *   [irq/0](https://hexdocs.pm/lora/LoRa.Parameters.html#irq/0)
        *   [max/0](https://hexdocs.pm/lora/LoRa.Parameters.html#max/0)
        *   [mode/0](https://hexdocs.pm/lora/LoRa.Parameters.html#mode/0)
        *   [pa/0](https://hexdocs.pm/lora/LoRa.Parameters.html#pa/0)
        *   [register/0](https://hexdocs.pm/lora/LoRa.Parameters.html#register/0)

LoRa v1.0.1 LoRa [View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L1 "View Source")
=====================================================================================================================

This is a module for transmitter data using LoRa Radios.

Radios:

`Semtech SX1276/77/78/79 based boards.`
[Link to this section](https://hexdocs.pm/lora/#summary) Summary
================================================================

[Functions](https://hexdocs.pm/lora/#functions)
-----------------------------------------------

[awake(pid)](https://hexdocs.pm/lora/#awake/1)

Awake the LoRa Radio.

[begin(pid, frequency)](https://hexdocs.pm/lora/#begin/2)

Initialize the LoRa Radio and set your frequency work.

[child_spec(init_arg)](https://hexdocs.pm/lora/#child_spec/1)

Returns a specification to start this module under a supervisor.

[disable_crc(pid)](https://hexdocs.pm/lora/#disable_crc/1)

Remove the verify digit.

[enable_crc(pid)](https://hexdocs.pm/lora/#enable_crc/1)

This is a verify digit add in the data message.

[init(config)](https://hexdocs.pm/lora/#init/1)

Callback implementation for [`GenServer.init/1`](https://hexdocs.pm/elixir/GenServer.html#c:init/1).

[send(pid, data, header \\ true)](https://hexdocs.pm/lora/#send/3)

Send data for other radios.

[set_signal_bandwidth(pid, sbw)](https://hexdocs.pm/lora/#set_signal_bandwidth/2)

Set Trasmission Signal Bandwidth.

[set_spreading_factor(pid, sf \\ 6)](https://hexdocs.pm/lora/#set_spreading_factor/2)

Set Spreading Factor. `sf` is a value between 6 and 12. Standar value is 6.

[sleep(pid)](https://hexdocs.pm/lora/#sleep/1)

Set the LoRa Radio in sleep mode.

[start_link(config \\ [])](https://hexdocs.pm/lora/#start_link/1)

Start and link a new GenServer for LoRa radio.

[Link to this section](https://hexdocs.pm/lora/#functions) Functions
====================================================================

[Link to this function](https://hexdocs.pm/lora/#awake/1 "Link to this function")
awake(pid)
==========

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L52 "View Source")

Awake the LoRa Radio.

`LoRa.awake(lora_pid)`

[Link to this function](https://hexdocs.pm/lora/#begin/2 "Link to this function")
begin(pid, frequency)
=====================

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L42 "View Source")

Initialize the LoRa Radio and set your frequency work.

```
{:ok, lora} = LoRa.start_link()
LoRa.begin(lora, 433.0e6)
```

[Link to this function](https://hexdocs.pm/lora/#child_spec/1 "Link to this function")
child_spec(init_arg)
====================

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L9 "View Source")

Returns a specification to start this module under a supervisor.

See [`Supervisor`](https://hexdocs.pm/elixir/Supervisor.html).

[Link to this function](https://hexdocs.pm/lora/#disable_crc/1 "Link to this function")
disable_crc(pid)
================

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L77 "View Source")

Remove the verify digit.

`LoRa.disable_crc(lora_pid)`

[Link to this function](https://hexdocs.pm/lora/#enable_crc/1 "Link to this function")
enable_crc(pid)
===============

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L71 "View Source")

This is a verify digit add in the data message.

`LoRa.enable_crc(lora_pid)`

[Link to this function](https://hexdocs.pm/lora/#init/1 "Link to this function")
init(config)
============

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L90 "View Source")

Callback implementation for [`GenServer.init/1`](https://hexdocs.pm/elixir/GenServer.html#c:init/1).

[Link to this function](https://hexdocs.pm/lora/#send/3 "Link to this function")
send(pid, data, header \\ true)
===============================

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L85 "View Source")

Send data for other radios.

```
LoRa.send(lora_pid, 'hello world')
LoRa.send(lora_pid, "hello world")
LoRa.send(lora_pid, %{value: 10})
```

[Link to this function](https://hexdocs.pm/lora/#set_signal_bandwidth/2 "Link to this function")
set_signal_bandwidth(pid, sbw)
==============================

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L65 "View Source")

Set Trasmission Signal Bandwidth.

`LoRa.set_signal_bandwidth(lora_pid, 31.25e3)`

[Link to this function](https://hexdocs.pm/lora/#set_spreading_factor/2 "Link to this function")
set_spreading_factor(pid, sf \\ 6)
==================================

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L58 "View Source")

Set Spreading Factor. `sf` is a value between 6 and 12. Standar value is 6.

`LoRa.set_spreading_factor(lora_pid, 10)`

[Link to this function](https://hexdocs.pm/lora/#sleep/1 "Link to this function")
sleep(pid)
==========

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L47 "View Source")

Set the LoRa Radio in sleep mode.

`LoRa.sleep(lora_pid)`

[Link to this function](https://hexdocs.pm/lora/#start_link/1 "Link to this function")
start_link(config \\ [])
========================

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/lora.ex#L36 "View Source")

Start and link a new GenServer for LoRa radio.

Can be set the parameters of SPI and GPIO pin for the reset of radio.

# standard values: `spi: "spidev0.0", spi_speed: 8_000_000, rst: 25`

`{:ok, lora} = LoRa.start_link()`
or

`{:ok, lora} = LoRa.start_link([spi: "spidev0.1", spi_speed: 5_000_000, rst: 27])`

Built using [ExDoc](https://github.com/elixir-lang/ex_doc "ExDoc") (v0.21.3),  designed by [Friedel Ziegelmayer](https://twitter.com/dignifiedquire "@dignifiedquire") for the [Elixir programming language](https://elixir-lang.org/ "Elixir").

Display keyboard shortcuts  Toggle night mode  Go to a HexDocs package Disable tooltips Enable tooltips

Keyboard Shortcuts

×

c Toggle sidebar n Toggle night mode / or s  Focus search bar g  Go to a HexDocs package ? Bring up this help dialog 

Go to a HexDocs package

×
