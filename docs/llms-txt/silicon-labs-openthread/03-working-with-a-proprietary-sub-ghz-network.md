# Source: https://docs.silabs.com/openthread/3.0.0/openthread-single-band-proprietary-sub-ghz/03-working-with-a-proprietary-sub-ghz-network.md

# Working with a Proprietary Sub-GHz Network

Silicon Labs radio boards supporting the sub-GHz ISM band are designed to the operate in the US FCC 902-928 MHz band with an external whip antenna. Accordingly, when working with this feature, connect the external whip antenna using the SMA antenna connector on your radio board. For more information about this requirement, please refer to your radio board’s reference manual.

## Creating a Proprietary Sub-GHz Network

As mentioned in the [Introduction](./index), the proprietary sub-GHz feature currently supports single band use only and so requires every node in the mesh to be running an application with the sub-GHz feature enabled. Accordingly, to create a sub-GHz network:

1. Build the **ot-cli-ftd** example with the proprietary sub-GHz feature enabled as discussed in [Building an OpenThread Sample App for Proprietary Sub-GHz](./02-building-an-openthread-sample-app-for-proprietary-sub-ghz) and flash the same application on all your nodes.
2. Use the standard OpenThread CLI commands to form and attach to a network. An example of this step is provided in the [OpenThread Quick Start Guide](/openthread/3.0.0/openthread-quick-start-guide/03-getting-started-with-development/creating-a-network).
3. The resulting network formed has nodes operating on the sub-GHz band (with channels supported between 0 – 24, covering 902 – 928 MHz).

## Enabling Proprietary Sub-GHz Support on an OpenThread Border Router

This section assumes that you are familiar with the basic build and install instructions for an OpenThread Border Router. If not, refer to [Using the Silicon Labs Co-processors with the OpenThread Border Router](/openthread/3.0.0/using-sl-coprocessors-with-openthread-border-router).

To enable proprietary sub-GHz support on an OpenThread Border Router:

1. Build an RCP image using Simplicity Studio with the sub-GHz feature enabled. Start with the **ot-rcp** example and follow the steps described in [Building an OpenThread Sample App for Proprietary Sub-GHz](./02-building-an-openthread-sample-app-for-proprietary-sub-ghz#building-an-openthread-sample-app-for-proprietary-sub-ghz).
2. For the Border Router Host you can either:  
   - Use a pre-built docker image (Recommended)    
     [https://hub.docker.com/r/siliconlabsinc/openthread-border-router-proprietary-na-915/tags](https://hub.docker.com/r/siliconlabsinc/openthread-border-router-proprietary-na-915/tags)  
   - Or, manually build the border router image for your host with the following OpenThread proprietary radio configurations set. This option requires you to modify the OT BR build scripts (details of which are beyond the scope of this document).

|Configuration|Value|
|---|---|
|OPENTHREAD_CONFIG_PLATFORM_RADIO_PROPRIETARY_SUPPORT|1|
|OPENTHREAD_CONFIG_RADIO_2P4GHZ_OQPSK_SUPPORT|0|
|OPENTHREAD_CONFIG_RADIO_915MHZ_OQPSK_SUPPORT|0|
|OPENTHREAD_CONFIG_PLATFORM_RADIO_PROPRIETARY_CHANNEL_PAGE|23|
|OPENTHREAD_CONFIG_PLATFORM_RADIO_PROPRIETARY_CHANNEL_MIN|0|
|OPENTHREAD_CONFIG_PLATFORM_RADIO_PROPRIETARY_CHANNEL_MAX|24|
|OPENTHREAD_CONFIG_PLATFORM_RADIO_PROPRIETARY_CHANNEL_MASK|0x1ffffff|
|OPENTHREAD_CONFIG_DEFAULT_CHANNEL|0|

## Verifying Sub-GHz Operation

To verify if your application has been configured correctly to operate on the sub-GHz band:

1. Execute the following CLI command on your node, to retrieve the supported channel mask:  
   ```C  
   > channel supported  
   0x1ffffff  
   Done  
   ```  
   For proprietary sub-GHz applications, the result of this command is `0x1ffffff`, indicating channels 0-24 supported for this configuration. For 2.4 GHz applications, the output returned is `0x7fff800`, indicating channels 11-26 supported for that band.
2. Alternately, for a node running the sub-GHz application and that is part of an OpenThread network, you can also verify the radio information using Silicon Labs Network Analyzer.  
   ![screenshot](/openthread-single-band-proprietary-sub-ghz/0.2/images/sld699-image3.png)

For more details on how to capture OpenThread packers using Silicon Labs Network Analyzer, refer to _Network Analyzer_ in [OpenThread Quick Start Guide](/openthread/3.0.0/openthread-quick-start-guide/05-development-tools/network-analyzer).