# Source: https://juno.build/docs/miscellaneous/provisioning-options.md

# Provisioning Options

The creation wizard for Satellites and Orbiters includes advanced provisioning options for developers who need more control.

---

## Hosting Memory

When you initialize a satellite, you must decide how the frontend will be kept in memory and served on the web.

In the Console this is presented as _"What are you building? Website or Application"_.

If you pick Website, the hosting will be provisioned on heap memory. If you pick Application, it will be on stable memory.

Heap provides the fastest response. It is a good choice when you want to deliver content as quickly as possible to users, and it also benefits SEO, since speed matters. For this reason, it is the default for websites.

Stable is slightly more expensive and slower on average. Unlike heap, each access requires data to be deserialized. This process is fast but still has an impact. The advantage of stable comes during upgrades: assets do not need to be serialized and deserialized again, which means you are not limited to 1 GB of assets. For this reason, stable is the default for applications with rich features, such as single-page applications.

Our benchmarks showed that heap generally delivered more consistent responses with fewer slow spikes. Stable performed similarly on average but tended to be spikier under load. For larger assets, heap was typically faster and more reliable at higher percentiles, though it could show a small startup penalty or the occasional outlier.

Lighthouse measurements indicated that stable added roughly 0.5 seconds to CFP compared to heap for a small website.

Ultimately, there are no strict rules. You can use heap for an application or stable for a website. You can also switch from one to the other in Hosting > Settings in the Console, with the prerequisite that no files are being served at the time of the switch.

**Info:**

For more background on memory behavior and limits, see the [Memory](/docs/miscellaneous/memory.md) documentation.

---

## Selecting a Subnet

If you want more control over where your module is provisioned, you can select a [subnet](/docs/terminology.md#subnet) during the creation process.

Below is a list of available subnets with relevant metadata to help you choose the most appropriate one:

**Note:**

Satellites and Orbiters running on larger subnets with more nodes will incur higher cycle costs compared to those on the standard 13-node subnets. However, this increased cost comes with the benefit of enhanced security due to the greater size of the subnet.

For most applications, we recommend using the default subnets and staying on the same subnet as Juno.

| Subnet ID | Type | Canisters (Running/Stopped) | Nodes (Up/Total) |
| --- | --- | --- | --- |
| 6pbhf-qzpdk-kuqbr-pklfa-5ehhf-jfjps-zsj6q-57nrl-kzhpd-mu7hc-vae | Juno's Subnet | 36101/703 | 13/13 |
| pzp6e-ekpqk-3c5x7-2h6so-njoeq-mt45d-h3h6c-q3mxf-vpeq5-fk5o7-yae | Fiduciary | 3564/12 | 34/34 |
| bkfrj-6k62g-dycql-7h53p-atvkj-zg4to-gaogh-netha-ptybj-ntsgw-rqe | European | 25096/663 | 13/13 |
| brlsh-zidhj-3yy3e-6vqbz-7xnih-xeq2l-as5oc-g32c4-i5pdn-2wwof-oae |     | 35432/815 | 13/13 |
| o3ow2-2ipam-6fcjo-3j5vt-fzbge-2g7my-5fz2m-p4o2t-dwlc4-gt2q7-5ae |     | 57571/170 | 13/13 |
| 4ecnw-byqwz-dtgss-ua2mh-pfvs7-c3lct-gtf4e-hnu75-j7eek-iifqm-sqe |     | 8684/303 | 13/13 |
| opn46-zyspe-hhmyp-4zu6u-7sbrh-dok77-m7dch-im62f-vyimr-a3n2c-4ae |     | 40491/835 | 13/13 |
| nl6hn-ja4yw-wvmpy-3z2jx-ymc34-pisx3-3cp5z-3oj4a-qzzny-jbsv3-4qe |     | 32293/818 | 13/13 |
| io67a-2jmkw-zup3h-snbwi-g6a5n-rm5dn-b6png-lvdpl-nqnto-yih6l-gqe |     | 2997/2528 | 13/13 |
| ejbmu-grnam-gk6ol-6irwa-htwoj-7ihfl-goimw-hlnvh-abms4-47v2e-zqe |     | 12068/111 | 13/13 |
| gmq5v-hbozq-uui6y-o55wc-ihop3-562wb-3qspg-nnijg-npqp5-he3cj-3ae |     | 34558/256 | 13/13 |
| pjljw-kztyl-46ud4-ofrj6-nzkhm-3n4nt-wi3jt-ypmav-ijqkt-gjf66-uae |     | 32743/243 | 12/13 |
| 4zbus-z2bmt-ilreg-xakz4-6tyre-hsqj4-slb4g-zjwqo-snjcc-iqphi-3qe |     | 59568/87 | 13/13 |
| 5kdm2-62fc6-fwnja-hutkz-ycsnm-4z33i-woh43-4cenu-ev7mi-gii6t-4ae |     | 13234/154 | 13/13 |
| e66qm-3cydn-nkf4i-ml4rb-4ro6o-srm5s-x5hwq-hnprz-3meqp-s7vks-5qe |     | 35861/769 | 13/13 |
| qdvhd-os4o2-zzrdw-xrcv4-gljou-eztdp-bj326-e6jgr-tkhuc-ql6v2-yqe |     | 53577/125 | 13/13 |
| snjp4-xlbw4-mnbog-ddwy6-6ckfd-2w5a2-eipqo-7l436-pxqkh-l6fuv-vae |     | 4277/1511 | 13/13 |
| shefu-t3kr5-t5q3w-mqmdq-jabyv-vyvtf-cyyey-3kmo4-toyln-emubw-4qe |     | 3004/2624 | 13/13 |
| csyj4-zmann-ys6ge-3kzi6-onexi-obayx-2fvak-zersm-euci4-6pslt-lae |     | 3682/1812 | 13/13 |
| yinp6-35cfo-wgcd2-oc4ty-2kqpf-t4dul-rfk33-fsq3r-mfmua-m2ngh-jqe |     | 8457/582 | 13/13 |
| w4asl-4nmyj-qnr7c-6cqq4-tkwmt-o26di-iupkq-vx4kt-asbrx-jzuxh-4ae |     | 3151/2468 | 12/13 |
| c4isl-65rwf-emhk5-5ta5m-ngl73-rgrl3-tcc56-2hkja-4erqd-iivmy-7ae |     | 1700/4011 | 13/13 |
| mpubz-g52jc-grhjo-5oze5-qcj74-sex34-omprz-ivnsm-qvvhr-rfzpv-vae |     | 55938/327 | 12/13 |
| fuqsr-in2lc-zbcjj-ydmcw-pzq7h-4xm2z-pto4i-dcyee-5z4rz-x63ji-nae |     | 22380/117 | 13/13 |
| cv73p-6v7zi-u67oy-7jc3h-qspsz-g5lrj-4fn7k-xrax3-thek2-sl46v-jae |     | 51889/339 | 13/13 |
| pae4o-o6dxf-xki7q-ezclx-znyd6-fnk6w-vkv5z-5lfwh-xym2i-otrrw-fqe |     | 5134/630 | 13/13 |
| qxesv-zoxpm-vc64m-zxguk-5sj74-35vrb-tbgwg-pcird-5gr26-62oxl-cae |     | 2531/3146 | 13/13 |
| 4utr6-xo2fz-v7fsb-t3wsg-k7sfl-cj2ba-ghdnd-kcrfo-xavdb-ebean-mqe |     | 2756/3071 | 13/13 |
| lspz2-jx4pu-k3e7p-znm7j-q4yum-ork6e-6w4q6-pijwq-znehu-4jabe-kqe |     | 40004/944 | 13/13 |
| jtdsg-3h6gi-hs7o5-z2soi-43w3z-soyl3-ajnp3-ekni5-sw553-5kw67-nqe |     | 27813/206 | 13/13 |