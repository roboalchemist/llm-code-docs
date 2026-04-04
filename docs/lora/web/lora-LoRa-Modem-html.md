# Source: https://hexdocs.pm/lora/LoRa.Modem.html

Title: LoRa.Modem — LoRa v1.0.1

URL Source: https://hexdocs.pm/lora/LoRa.Modem.html

Markdown Content:
LoRa v1.0.1 LoRa.Modem [View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L1 "View Source")
----------------------------------------------------------------------------------------------------------------------------

[Link to this section](https://hexdocs.pm/lora/LoRa.Modem.html#summary) Summary
-------------------------------------------------------------------------------

[Functions](https://hexdocs.pm/lora/LoRa.Modem.html#functions)
--------------------------------------------------------------

[begin(frequency, spi, power \\ 17)](https://hexdocs.pm/lora/LoRa.Modem.html#begin/3)

[bit_write(value, bit, subs)](https://hexdocs.pm/lora/LoRa.Modem.html#bit_write/3)

[disable_crc(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#disable_crc/1)

[enable_crc(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#enable_crc/1)

[end_packet(from, spi, async? \\ false)](https://hexdocs.pm/lora/LoRa.Modem.html#end_packet/3)

[get_signal_band_width(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#get_signal_band_width/1)

[get_spreading_factor(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#get_spreading_factor/1)

[get_version(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#get_version/1)

[idle(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#idle/1)

[parse_packet(from, spi, size \\ 0)](https://hexdocs.pm/lora/LoRa.Modem.html#parse_packet/3)

[read(frequency, owner, spi, index \\ 0, msg \\ [])](https://hexdocs.pm/lora/LoRa.Modem.html#read/5)

[reset(rst)](https://hexdocs.pm/lora/LoRa.Modem.html#reset/1)

[reset_fifo_payload(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#reset_fifo_payload/1)

[rssi(frequency, spi)](https://hexdocs.pm/lora/LoRa.Modem.html#rssi/2)

[set_LNA_boost(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_LNA_boost/1)

[set_auto_AGC(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_auto_AGC/1)

[set_bandwidth(sbw, spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_bandwidth/2)

[set_base_address(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_base_address/1)

[set_frequency(freq, spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_frequency/2)

[set_header_mode(expl, spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_header_mode/2)

[set_ldo_flag(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_ldo_flag/1)

[set_ocp(ocp, spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_ocp/2)

[set_spreading_factor(sf, spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_spreading_factor/2)

[set_tx_power(level, spi)](https://hexdocs.pm/lora/LoRa.Modem.html#set_tx_power/2)

[sleep(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#sleep/1)

[snr(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#snr/1)

[tx_done_flag(spi)](https://hexdocs.pm/lora/LoRa.Modem.html#tx_done_flag/1)

[verify_end_packet(spi, from, counter \\ 0)](https://hexdocs.pm/lora/LoRa.Modem.html#verify_end_packet/3)

[Link to this section](https://hexdocs.pm/lora/LoRa.Modem.html#functions) Functions
-----------------------------------------------------------------------------------

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#begin/3 "Link to this function")

begin(frequency, spi, power \\ 17)
----------------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L19 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#bit_write/3 "Link to this function")

bit_write(value, bit, subs)
---------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L374 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#disable_crc/1 "Link to this function")

disable_crc(spi)
----------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L353 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#enable_crc/1 "Link to this function")

enable_crc(spi)
---------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L345 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#end_packet/3 "Link to this function")

end_packet(from, spi, async? \\ false)
--------------------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L36 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#get_signal_band_width/1 "Link to this function")

get_signal_band_width(spi)
--------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L361 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#get_spreading_factor/1 "Link to this function")

get_spreading_factor(spi)
-------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L366 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#get_version/1 "Link to this function")

get_version(spi)
----------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L372 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#idle/1 "Link to this function")

idle(spi)
---------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L75 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#parse_packet/3 "Link to this function")

parse_packet(from, spi, size \\ 0)
----------------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L109 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#read/5 "Link to this function")

read(frequency, owner, spi, index \\ 0, msg \\ [])
--------------------------------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L83 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#reset/1 "Link to this function")

reset(rst)
----------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L154 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#reset_fifo_payload/1 "Link to this function")

reset_fifo_payload(spi)
-----------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L171 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#rssi/2 "Link to this function")

rssi(frequency, spi)
--------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L104 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_LNA_boost/1 "Link to this function")

set_LNA_boost(spi)
------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L314 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_auto_AGC/1 "Link to this function")

set_auto_AGC(spi)
-----------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L322 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_bandwidth/2 "Link to this function")

set_bandwidth(sbw, spi)
-----------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L289 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_base_address/1 "Link to this function")

set_base_address(spi)
---------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L308 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_frequency/2 "Link to this function")

set_frequency(freq, spi)
------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L177 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_header_mode/2 "Link to this function")

set_header_mode(expl, spi)
--------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L325 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_ldo_flag/1 "Link to this function")

set_ldo_flag(spi)
-----------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L251 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_ocp/2 "Link to this function")

set_ocp(ocp, spi)
-----------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L230 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_spreading_factor/2 "Link to this function")

set_spreading_factor(sf, spi)
-----------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L272 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#set_tx_power/2 "Link to this function")

set_tx_power(level, spi)
------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L192 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#sleep/1 "Link to this function")

sleep(spi)
----------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L67 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#snr/1 "Link to this function")

snr(spi)
--------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L102 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#tx_done_flag/1 "Link to this function")

tx_done_flag(spi)
-----------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L163 "View Source")

[Link to this function](https://hexdocs.pm/lora/LoRa.Modem.html#verify_end_packet/3 "Link to this function")

verify_end_packet(spi, from, counter \\ 0)
------------------------------------------

[View Source](https://github.com/brunosantanaa/Elixir-LoRa/blob/master/lib/modem.ex#L51 "View Source")
