# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## *Revision History*

| Revision Number | Date | Comments |
| --- | --- | --- |
| v1.0 | 2017-07-13 | Adopted by the Bluetooth SIG Board of Directors |
| v1.0.1 | 2019-01-21 | Adopted by the Bluetooth SIG Board of Directors |
| v1.1 | 2023-09-12 | Adopted by the Bluetooth SIG Board of Directors. |

## *Version History*

| Versions | Changes |
| --- | --- |
| v1.0.0 to v1.0.1 | Incorporated errata E9618, E9634, E9639, E9693, E9743, E9748, E9752, E9761, E9788, E9796, E9805, E9807, E9808, E9811, E9812, E9819, E9882, E9883, E9894, E9939, E9957, E9959,E9964, E9969, E9981, E9982, E9983, E10015, E10024, E10025, E10026, E10027, E10028, E10054, E10066, E10081, E10082, E10084, E10086, E10087, E10100, E10101, E10148, E10157, E10168, E10247, E10296, E10310, E10317, E10321, E10322, E10332, E10344, E10395, E10426, E10514, E10515, E10520, E10569, E10575, E10578, E10636, E10664, E10670, E10746, E10748, E10777, E10863, E10864, E11306 |
| v1.0.1 to v1.1 | Changed the specification name from “Mesh Profile” to “Mesh Protocol”.  Incorporated the Mesh Certificate-Based Provisioning CR, Mesh Remote Provisioning CR, Mesh Directed Forwarding CR, Mesh Private Beacons CR, Mesh Subnet Bridge CR, Mesh Profile Minor Enhancements CR, and the Mesh Profile Enhanced Provisioning Authentication CR.  Incorporated errata E10635, E10950, E10974, E11128, E11173, E11176, E11206, E11207, E11213, E11249, E11256, E11271, E11272, E11273, E11275, E11276, E11301, E11302, E11309, E11310, E11322, E11329, E11341, E11345, E11358, E11359, E11384, E11392, E11394, E11414, E11415, E11416, E11627, E11700, E11712, E11737, E11799, E11802, E11836, E11850, E11901, E11922, E11936, E11940, E11976, E11977, E11978, E11991, E12006, E12013, E12046, E12079, E12092, E12111, E12154, E12226, E12277, E12390, E12403, E12426, E12439, E12543, E12556, E12579, E12581, E12582, E12586, E12587, E12781, E12825, E12834, E12871, E12975, E13008, E13010, E13030, E13084, E13101, E13124, E13171, E13217, E13331, E13430, E13433, E13443, E13446, E13506, E14731, E14734, E14743, E14745, E14804, E14814, E14815, E14885, E14921, E15011, E15080, E15106, E15155, E15210, E15335, E15456, E15457, E15458, E15499, E15696, E15755, E15875, E15889, E16334, E16350, E16386, E16391, E16402, E16408, E16436, E16462, E16701, E16827, E16847, E16870, E16871, E17029, E17059, E17093, E17158, E17203, E17215, E17341, E17345, E17348, E17364, E17369, E17376, E17624, E17955, E18051, E18071, E18117, E18131, E18137, E18181, E18316, E18469, E18487, E18491, E18741, E18932, E19041, E19118, E19250, E20514, E20541, E20554, E20568, E20574, E20586, E20596, E22321, E22354, E22468, E22717, E22761, E22766, E22942, E22979, E23258, E23406 |

## *Acknowledgments*

| Name | Company |
| --- | --- |
| Robin Heydon | Qualcomm Technologies International, Ltd. |
| Jonathan Tanner | Qualcomm Technologies International, Ltd. |
| Victor Zhodzishsky | Broadcom Corporation |
| Victor Zhodzishsky | Cypress Semiconductor Corporation |
| Wei Shen | Ericsson AB |
| Christoffer Jerkeby | Ericsson AB |
| Bogdan Alexandru | NXP Semiconductors |
| Martin Turon | Google Inc. |
| Robert D. Hughes | Intel Corporation |
| Marcel Holtmann | Intel Corporation |
| Brian Gix | Intel Corporation |
| Simon Slupik | Silvair, Inc. |
| Piotr Winiarczyk | Silvair, Inc. |
| Danilo Blasi | STMicroelectronics |
| Yao Wang | Barrot Technology Co., Ltd. |
| Rustam Kovyazin | Motorola Solutions |
| Uday Agarwal | Cypress Semiconductor Corporation |
| Vasilii Aleksandrov | Motorola Solutions |
| LC Ko | MediaTek, Inc. |
| Omkar Kulkarni | Cypress Semiconductor Corporation |
| Omkar Kulkarni | Nordic Semiconductor ASA |
| Pontus Arvidson | Ericsson AB |
| Ravi Kiran Bamidi | Silvair, Inc. |
| Robert Cragie | ARM Ltd |
| Piergiuseppe Di Marco | Ericsson AB |
| Piergiuseppe Di Marco | Silvair, Inc. |
| Per Elmdahl | Ericsson AB |
| Arvind Kandhalu | Texas Instruments Incorporated |
| Yiting Liao | Intel Corporation |
| Jingcheng Zhang | Ericsson AB |
| Thomas Stenersen | Nordic Semiconductor ASA |
| Hannu Mallat | Silicon Laboratories |
| Max Palumbo | Silicon Laboratories |
| Max Palumbo | Katerra Inc. |
| Jori Rintahaka | Silicon Laboratories |
| Kim Schulz | Samsung Electronics Co., Ltd. |
| Michał Budzoń | Silvair, Inc. |
| Luca Zappaterra | Signify Netherlands B.V. |
| Erik Anderlind | KiteSpring Inc. |

Use of this specification is your acknowledgement that you agree to and will comply with the following notices and disclaimers. You are advised to seek appropriate legal, engineering, and other professional advice regarding the use, interpretation, and effect of this specification.

Use of Bluetooth specifications by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG and its members, including those agreements posted on Bluetooth SIG’s website located at www.bluetooth.com. Any use of this specification by a member that is not in compliance
with the applicable membership and other related agreements is prohibited and, among other things, may result in (i) termination of the applicable agreements and (ii) liability for infringement of the intellectual property rights of Bluetooth SIG and its members. This specification may provide options, because, for example, some products
do not implement every portion of the specification. All content within the specification, including notes, appendices, figures, tables, message sequence charts, examples, sample data, and each option identified is intended to be within the bounds of the Scope as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”). Also,
the identification of options for implementing a portion of the specification is intended to provide design flexibility without establishing, for purposes of the PCLA, that any of these options is a “technically reasonable non-infringing alternative.”

Use of this specification by anyone who is not a member of Bluetooth SIG is prohibited and is an infringement of the intellectual property rights of Bluetooth SIG and its members. The furnishing of this specification does not grant any license to any intellectual property of Bluetooth SIG or its members. THIS
SPECIFICATION IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTIES OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, OR THAT THE CONTENT OF THIS SPECIFICATION IS FREE OF ERRORS.
For the avoidance of doubt, Bluetooth SIG has not made any search or investigation as to third parties that may claim rights in or to any specifications or any intellectual property that may be required to implement any specifications and it disclaims any obligation or duty to do so.

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS SPECIFICATION AND ANY INFORMATION CONTAINED IN THIS SPECIFICATION, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR
SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF THE DAMAGES.

Products equipped with Bluetooth wireless technology ("Bluetooth Products") and their combination, operation, use, implementation, and distribution may be subject to regulatory controls under the laws and regulations of numerous countries that regulate products that use wireless non-licensed spectrum. Examples
include airline regulations, telecommunications regulations, technology transfer controls, and health and safety regulations. You are solely responsible for complying with all applicable laws and regulations and for obtaining any and all required authorizations, permits, or licenses in connection with your use of this specification and
development, manufacture, and distribution of Bluetooth Products. Nothing in this specification provides any information or assistance in connection with complying with applicable laws or regulations or obtaining required authorizations, permits, or licenses.

Bluetooth SIG is not required to adopt any specification or portion thereof. If this specification is not the final version adopted by Bluetooth SIG’s Board of Directors, it may not be adopted. Any specification adopted by Bluetooth SIG’s Board of Directors may be withdrawn, replaced, or modified at any time.
Bluetooth SIG reserves the right to change or alter final specifications in accordance with its membership and operating agreements.

Copyright © 2015–2023. All copyrights in the Bluetooth Specifications themselves are owned by Apple Inc., Ericsson AB, Intel Corporation, Lenovo (Singapore) Pte. Ltd., Microsoft Corporation, Nokia Corporation, and Toshiba Corporation. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other
third-party brands and names are the property of their respective owners.
