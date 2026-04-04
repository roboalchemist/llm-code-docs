# Source: https://docs.datafold.com/integrations/oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OAuth Support

> Set up OAuth App Connections in your supported data warehouses to securely execute data diffs on behalf of your users.

<Note>
  This feature is currently supported for Databricks, Snowflake, Redshift, and BigQuery.
</Note>

OAuth support empowers users to run data diffs based on their individual permissions and roles configured within the data warehouses. This ensures that data access is governed by existing security policies and protocols.

## How it works

### 1. Create a Data Diff

When you attempt to run a data diff, you will notice that it won't run without authentication:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cd7e4bebaad25ee87ee8f9af1276b394" data-og-width="1351" width="1351" data-og-height="506" height="506" data-path="images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=195e49c927a5fe592e1b102f2a29b7be 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f0cb562f9843f7ce6dab563e5b59bed0 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d02eaac4cdaf17c39ccc1e59e13417dc 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7a2da244a27834108940f1678e31978c 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cdc4d1406b80309fd8b0af97a9e2c49d 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-b9afb4d6ec25ca58b9a033ff1eaf6efb.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e476b20694e97943353a1137c225ad8f 2500w" />
</Frame>

### 2. Authorize the Data Diff

Authorize the data diff by clicking the **Authenticate** button. This will redirect you to the data warehouse for authentication:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ed69e89b64e6a3d78420304cad83aa56" data-og-width="692" width="692" data-og-height="689" height="689" data-path="images/2-01bbf79b7aaf007bc33dc4652a825e31.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cc3033abe34ccb7baae0e1a4275c94d1 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d33a10f83a772a4d80313f38d627a0b0 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=14172780ba3b63b6ccbaf4ea6b9b6f03 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c48a994bb8c896960bd3512d88c52048 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0559d8f1be5b5a75fab27b48c0624d2d 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-01bbf79b7aaf007bc33dc4652a825e31.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4e3214159c568cf8c5ea1505da0dbdb7 2500w" />
</Frame>

Upon successful authentication, you will be redirected back.

### 3. The Data Diff is now running <Icon icon="party-horn" />

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0cd380754dc3b5894e055590d2638473" data-og-width="1444" width="1444" data-og-height="660" height="660" data-path="images/3-7d49f847dba2d6ebefe0215a7251d3e7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6d875f7e171d67f3b3df4116ba70508d 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e49c8e8d0b648191c88f47526212fb21 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=bcd2d270da75b7c4e3b597057a1ed24f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=badcae551df707e90656f61fc1e25eb2 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4ff503167e0ed264596f730d485a3bbc 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-7d49f847dba2d6ebefe0215a7251d3e7.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8f1948bba26c08ba890505297c338e36 2500w" />
</Frame>

### 4. View the Data Diff results

The results reflect your permissions within the data warehouse:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=897aa005c633ba7fdea578447a97828a" data-og-width="616" width="616" data-og-height="329" height="329" data-path="images/4-1e3cf172b19bd6616700f3c82f17b256.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cc7668dbfdeb95b0e6324454303aaeea 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c9b739c02576debd0b5ff99c8e4561dc 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=671d55c6418991662e95fa42fbd67fb8 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e2efd53df3ab32f243b0d3ec6054401e 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=edea40bb30e8b0b022442b10797aea60 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-1e3cf172b19bd6616700f3c82f17b256.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=613e912826a8622e7bc4227bdbd8c0ef 2500w" />
</Frame>

Note that running the same data diff, as a different user, renders different results:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5e89ea4ea01811b1ffcdab58f0c7990e" data-og-width="668" width="668" data-og-height="348" height="348" data-path="images/5-585c0ee49689bb8af229ad44eb260ace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=431e0250ed4b32083ed9c3eebd0bf709 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f8f7871c7a7c078733d187d781ee7dc1 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9f6eebe93cf67954ec76fc73649d111c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e52cfccd6a7532e9f9aa559154b64cc9 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=96039c2a7908da697d0d8e046dabd9cf 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-585c0ee49689bb8af229ad44eb260ace.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=616915ffae6110716f613cd70d9f6995 2500w" />
</Frame>

The masked values represent the data retrieved from the data warehouse. We do not conduct any post-processing:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3783c5502d8e301edc487ddb2d7fbef3" data-og-width="2019" width="2019" data-og-height="522" height="522" data-path="images/6-f09d99fb5db326846be80a54d24606b0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=898f215c8d9f08234cd03eab7fc97b5b 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d99bce0c4d6369d098264344a65b94ef 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f18094e55a094528dbbb1a8e61b2f10b 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=25b02a547eaca94a10e4186325a7b206 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=abd90ef895528566cd7c2cc3446b35c9 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-f09d99fb5db326846be80a54d24606b0.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2f91c45870ff384f6046de39f0b55202 2500w" />
</Frame>

By default, results are only visible for their authors. Users can still clone the data diffs, but the results might be different depending on their data warehouse access levels.

For example, as a different user, I won't be able to access the data diff results for Filip's data diff:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=abbc65d13fd6f9fd766ae84fb815d9b1" data-og-width="1253" width="1253" data-og-height="526" height="526" data-path="images/7-0e23da80a3e63960a91301cdf38d8207.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0378959d5f546b39a207f8f024a24074 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d24b78901f302d1da0b8a4d7896247a1 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=91a5499844c9e2099ff8f9a422d6bba4 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c4c591f7d274d17ab4f32e296a091e7c 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=aea6ad16c4fa9c52f362d83ef0ca4b08 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/7-0e23da80a3e63960a91301cdf38d8207.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4853922ce3561089f308e9a890d4df6a 2500w" />
</Frame>

### 5. Sharing Data Diffs

Data diff sharing is a feature that enables you to share data diffs with other users. This is useful in scenarios such as compliance verification, where auditors can access specific data diffs without first requiring permissions to be set up in the data warehouse.

Sharing can be accessed via the **Actions** dropdown on the data diff page:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=789165034442807be5003399934f40f7" data-og-width="379" width="379" data-og-height="356" height="356" data-path="images/1-2f00e7c34ec87bada9d464dcb97053df.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1c47a66df147dae821908122196e1b8c 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3d465a16f8a27bbc4b5265efc71ac3e4 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5bf23de8a42cefdfae16c515b15dfdf1 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ff9442ca8ad8369bba31d0553f45f74b 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=afde9ca1305e4527f972cef28244d84c 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-2f00e7c34ec87bada9d464dcb97053df.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=47d15d0d6d5532f6ac22c76e1880844e 2500w" />
</Frame>

Note that data diff sharing is disabled by default:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ebfb0bfc01a1ced78c489906b41354fc" data-og-width="693" width="693" data-og-height="329" height="329" data-path="images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=327942722007ab9d72a72e26c4ef4972 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f3e66b6655803bb6820ced0d5b9c9fbc 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8462a78617cc020dd74b34f5d90a6e96 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5decc53f6eaaaa66a560412009e69a5c 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=70d95b33939cecbcd4b2262afd528914 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-badcc3a6ac297bc1c3ff27f8f4b6c9e0.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ae3ce479550c239cb9a85fe3c697cb2f 2500w" />
</Frame>

It can be enabled under **Org Settings** by clicking on **Allow Data Diff sharing**:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=bc1bf09028d88aa65d3a3ce75508810f" data-og-width="1154" width="1154" data-og-height="422" height="422" data-path="images/3-889664da5c85c56985659d0c9e675340.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=85a09f0a67c449242acbdf091905b5a7 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a2f515b93844dd745b05a6363f017209 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5f138b74c733b74d576673be4b1e314c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9c18444a04effb2a40ca19c9c83d4125 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6b20db867e2b9f9f6f1971a4b41e9f75 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-889664da5c85c56985659d0c9e675340.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a46ab3bc37c9301847e3b235017da8aa 2500w" />
</Frame>

Once enabled, you can share data diffs with other users:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=12830c2279779e7344273e1b9ce72aab" data-og-width="913" width="913" data-og-height="774" height="774" data-path="images/4-58827ded9574bddc7ef7ce0d4f156bf8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d74d11242338eeee30293c968916c526 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d37928e13b15fa8ffc1602edeb9ae532 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5232f81d8a7dc8ec0d6e96188902d003 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c532fa8733fd87c2f04e6cd3b3a484e9 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0f4e85b16c10c2ffb857567661da38cd 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-58827ded9574bddc7ef7ce0d4f156bf8.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a7527c6188f94bb08df9704e036aaccc 2500w" />
</Frame>

## Configuring OAuth

Navigate to **Settings** and click on your data connection. Then, click on **Advanced settings** and under **OAuth**, set the **Client Id** and **Client Secret** fields:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=483e82a0cfd9eb259f7423eb1ff97498" data-og-width="1639" width="1639" data-og-height="623" height="623" data-path="images/1-6541ee9948bb173fe28a64cb72b7ba8d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=408053f47c35658e971dda9d833c69b6 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=15bb1af0700abb2cb4deb39481091c77 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8824e49c7507464fc9b7dbf5303d7d27 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e7cba352e262d8d64812aeb3e9f9d294 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=693f103e21314927d4d68169bde97d19 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-6541ee9948bb173fe28a64cb72b7ba8d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2805e57d72531297123e2b9e5e6aea28 2500w" />
</Frame>

## Example: Databricks

To create a new Databricks app connection:

1. Go to **Settings** and **App connections**.
2. Click **Add connection** in the top right of the screen.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a69989f57df0f8720e00a76f98816b38" data-og-width="714" width="714" data-og-height="835" height="835" data-path="images/2-f59b84118a8979128d2476989b4f5262.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d4f2ea05d78059e3a3300a763969df76 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d2c8eb7c9d29ba6945e1416ea48f10f5 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5d148bb26eb06c028c864464184f20ae 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6e8adc1d158298733ba2e415a4a5ac52 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8568eb3d1032c28650f861d84cd1a244 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-f59b84118a8979128d2476989b4f5262.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2d260e633142df1e9fe7f8baeea766d8 2500w" />
</Frame>

3. Fill in the required fields:

Application Name:

```
Datafold OAuth connection
```

Redirect URLs:

```
https://app.datafold.com/api/internal/oauth_dwh/callback
```

<Note>
  **INFO**

  Datafold caches **access tokens** and using **refresh tokens** fetches new valid tokens in order to complete the diffs and reduce the number of times users need to authenticate against the data warehouses.

  One hour is sufficient for the access token.

  The refresh token will determine the frequency of user reauthentication, whether it's daily, weekly, or monthly.
</Note>

### 3. Click **Add** to obtain the **Client ID** and **Client Secret** <Icon icon="hand-sparkles" />

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=589b0cf2f42d86c1ec263cc47fb33365" data-og-width="628" width="628" data-og-height="391" height="391" data-path="images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=788520c072a39c4b79e5f9f445318717 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1b6edd2eba304c11f6f6137ed63c222f 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=32c72eaaf56e232a33466419557c0deb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=628e6af54f7d45d902d37367e5894e6a 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b5e1ed3327453efe695e140c4e25a4d2 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-c59900f8bd662e3ee8036f40eb2fcc4d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d48001fa82d678b45d86d1a32c8b9c2e 2500w" />
</Frame>

### 4. Fill in the **Client ID** and **Client Secret** fields in Datafold's Data Connection advanced settings:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=52b22b3c356fb6b6d7e4a905687d2715" data-og-width="1584" width="1584" data-og-height="338" height="338" data-path="images/4-75640ad5d18710fced1d22c108bbd0c9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d4a4a92da61693b411ef9a6f0c8d72fc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=460a00a3e82040db37043021196ff93d 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e5e4d08f2c193f8757110771197341c6 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f8d16340673a6cae96b9c1004a113741 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1222e977e30b8fdf9ab67cb3db8e5ffe 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=02ced3c862f91a53fd7a982f2f820216 2500w" />
</Frame>

### 5. Click **Test and save OAuth**

You will be redirected to Databricks to complete authentication. If you are already authenticated, you will be redirected back.

This notification signals a successful OAuth configuration:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=821eded0675f2c3319efee82e368caed" data-og-width="1647" width="1647" data-og-height="1284" height="1284" data-path="images/5-63f6c2f97041e030191e9abc5ca70637.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ec404016b242bc7beb77b9b4ba87a4dc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=166115bb5eddaa0dbb2d647224c70cfd 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7637451d19df712e3ea3eaf27b6a37cb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e067e3595978265bb27f425993f1c25 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c0c30eff5a3404e582c8539b19ead006 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=df269d44e95b405748512cfa1198c32d 2500w" />
</Frame>

### Additional steps for Databricks

To ensure that users have correct access rights to temporary tables (stored in **Dataset for temporary tables** provided in the **Basic settings** for the Databricks connection), follow these steps:

1. Update the permissions for the **Dataset for temporary tables** in Databricks.
2. Grant these permissions to Datafold users: **USE SCHEMA** and **CREATE TABLE**.

This will ensure that materialization results from data diffs are only readable by their authors.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=6a231a976529a7d6fbfdfa11e9638197" data-og-width="1138" width="1138" data-og-height="1239" height="1239" data-path="images/6-c4186dd5e91cd8aabf283649efe7461e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1c55ec5ab9301d127e478adc3d818454 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a52216ec9ffb28ae8230685bac7b22f2 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4cf511433f16971d49d64a3b3241d8a9 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e8aee9090c7cf5302d325d269173bcf8 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=483d6c66c63e65d6f64e8c31acf20275 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/6-c4186dd5e91cd8aabf283649efe7461e.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9631df3758a018a8bf371883486e7edf 2500w" />
</Frame>

## Example: Snowflake

To create a new Snowflake app connection:

1. Go to Snowflake and run this SQL:

```Bash  theme={null}
CREATE SECURITY INTEGRATION DATAFOLD_OAUTH
TYPE = OAUTH
ENABLED = TRUE
OAUTH_CLIENT = CUSTOM
OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'
OAUTH_REDIRECT_URI = 'https://app.datafold.com/api/internal/oauth_dwh/callback'
PRE_AUTHORIZED_ROLES_LIST=(<ROLENAME1>, <ROLENAME2>, ...)
OAUTH_ISSUE_REFRESH_TOKENS = TRUE
OAUTH_REFRESH_TOKEN_VALIDITY = 604800
OAUTH_ENFORCE_PKCE=TRUE;
```

It should result in this message:

<Warning>
  **CAUTION**

  * `PRE_AUTHORIZED_ROLES_LIST` must include all roles allowed to use the current security integration.
  * By default, `ACCOUNTADMIN`, `SECURITYADMIN`, and `ORGADMIN` are not allowed to be included in `PRE_AUTHORIZED_ROLES_LIST`.
</Warning>

<Note>
  **INFO**

  Datafold caches **access tokens** and uses **refresh tokens** to fetch new valid tokens in order to complete the diffs and reduce the number of times users need to authenticate against the data warehouses.

  `OAUTH_REFRESH_TOKEN_VALIDITY` can be in the range of 3600 (1 hour) to 7776000 (90 days).
</Note>

1. To retrieve `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`, run the following SQL:

```
select system$show_oauth_client_secrets('DATAFOLD_OAUTH');
```

### Example result:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ce9a57e787e1d1a98b9cb10bc77cc2be" data-og-width="1471" width="1471" data-og-height="71" height="71" data-path="images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e967abadcafc11c197a5581463da69dd 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=11553ac290971c5a55596b0335f2c76d 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7ad4f68ee71fecd7f62edd169c77d2c3 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=57586b5686ef991a592b731b92714ac2 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1775b83d05ba34fab6b6731375ec405e 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/oauth_snowflake_client_creds-47b11899ea2d5df0fce5f17f1711dc62.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c90744de328ea48873a9eebe68c44000 2500w" />
</Frame>

1. Fill in the **Client ID** and **Client Secret** fields in Datafold's Data Connection advanced settings:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=52b22b3c356fb6b6d7e4a905687d2715" data-og-width="1584" width="1584" data-og-height="338" height="338" data-path="images/4-75640ad5d18710fced1d22c108bbd0c9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d4a4a92da61693b411ef9a6f0c8d72fc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=460a00a3e82040db37043021196ff93d 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e5e4d08f2c193f8757110771197341c6 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f8d16340673a6cae96b9c1004a113741 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1222e977e30b8fdf9ab67cb3db8e5ffe 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-75640ad5d18710fced1d22c108bbd0c9.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=02ced3c862f91a53fd7a982f2f820216 2500w" />
</Frame>

2. Click **Test and save OAuth**

You will be redirected to Snowflake to complete authentication.

info

Your default Snowflake role will be used for the generated **access token**.

This notification signals a successful OAuth configuration:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=821eded0675f2c3319efee82e368caed" data-og-width="1647" width="1647" data-og-height="1284" height="1284" data-path="images/5-63f6c2f97041e030191e9abc5ca70637.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ec404016b242bc7beb77b9b4ba87a4dc 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=166115bb5eddaa0dbb2d647224c70cfd 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=7637451d19df712e3ea3eaf27b6a37cb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2e067e3595978265bb27f425993f1c25 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c0c30eff5a3404e582c8539b19ead006 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-63f6c2f97041e030191e9abc5ca70637.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=df269d44e95b405748512cfa1198c32d 2500w" />
</Frame>

### Additional steps for Snowflake

To guarantee correct access rights to temporary tables (stored in **Dataset for temporary tables** provided in the **Basic settings** for Snowflake connection):

* Grant the required privileges on the database and `TEMP` schema for all roles that will be using the OAuth flow. This must be done for all roles that will be utilizing the OAuth flow.

```Bash  theme={null}
GRANT USAGE ON WAREHOUSE <WH_NAME> TO ROLE <ROLENAME>;
GRANT USAGE ON DATABASE <DB_NAME> TO ROLE <ROLENAME>;
GRANT USAGE ON ALL SCHEMAS IN DATABASE <DB_NAME> TO ROLE <ROLENAME>;
GRANT USAGE ON FUTURE SCHEMAS IN DATABASE <DB_NAME> TO ROLE <ROLENAME>;
GRANT ALL ON SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> TO ROLE <ROLENAME>;
```

* Revoke `SELECT` privileges for tables in the `TEMP` schema for all roles that will be using the OAuth flow (except for the `DATAFOLDROLE` role), if they were provided. This action must be performed for all roles utilizing the OAuth flow\..

```Bash  theme={null}
-- Revoke SELECT privileges for the TEMP SCHEMA
revoke SELECT ON ALL TABLES IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE TABLES IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL MATERIALIZED VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE MATERIALIZED VIEWS IN SCHEMA <DB_NAME>.<TEMP_SCHEMA_NAME> FROM ROLE <ROLENAME>;
-- Revoke SELECT privileges for a Database
revoke SELECT ON ALL TABLES IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE TABLES IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON ALL MATERIALIZED VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
revoke SELECT ON FUTURE MATERIALIZED VIEWS IN DATABASE <DB_NAME> FROM ROLE <ROLENAME>;
```

<Warning>
  **CAUTION**

  If one of the roles will have `FUTURE GRANTS` at the database level, this role will also will have `FUTURE GRANTS` on the `TEMP` schema.
</Warning>

## Example: Redshift

Redshift does not support OAuth2. To execute data diffs on behalf of a specific user, that user needs to provide their own credentials to Redshift.

1. Configure permissions on the Redshift side. Grant the necessary access rights to temporary tables (stored in the **Dataset for temporary tables** provided in the **Basic settings** for Redshift connection):

```Bash  theme={null}
GRANT USAGE on SCHEMA <TEMP_SCHEMA_NAME> to <USERNAME>;
GRANT CREATE on SCHEMA <TEMP_SCHEMA_NAME> to <USERNAME>;
```

1. As an Administrator, select the **Enabled** toggle in Datafold's Redshift Data Connection **Advanced settings**:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1225a8001fa74dbeeead41b1675b2af1" data-og-width="573" width="573" data-og-height="357" height="357" data-path="images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fb743cd936ef569429288dc7f9783463 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6903a604b069ec8507e82d18c0c3abe8 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b88989e4cae2f4dc098776904f830144 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0259bf2891b63e2b6d5df436dfa9fae9 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2e2eb149539e059e5a34c186288638db 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_enable_toggle-df94b6b675d5b7a080b0569fed4943b0.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4e343749a80f2d5a4fbf8c5caadec60f 2500w" />
</Frame>

Then, click the **Test and Save** button.

1. As a User, add your Redshift credentials into Datafold. Click on your Datafold username to **Edit Profile**:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=94bb0a38ce1502c37884fbfdcce735b4" data-og-width="428" width="428" data-og-height="276" height="276" data-path="images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=11b8e43702d1bd72c843979730163c74 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f94d7f62dbf31b31730c8cb8b2697317 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b3226c0af0dd1340fa57135097e75679 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ea6b6fe0b6d2740fff30c9a44d3b2e51 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7d91a7ddf0d2b3394b12aa06ea363296 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_credentials_ui-749a49c20ca40f8857831a49526473cc.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4b343c2b6e1ec13859f0819046a49ec6 2500w" />
</Frame>

Then, click **Add credentials** and select the required Redshift data connection from the **Data Connections** list:

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4bd6e92d2df678a8625f8b69be7c4580" data-og-width="533" width="533" data-og-height="365" height="365" data-path="images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=dc5a30a103a1ecbad292db61119689ab 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f40447f504254a4ecb3018473e8cf372 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f7fd9cce0fd6316814a34974de843267 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=391c4cbc8e222ac90b219f3a2e0087ce 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fdb5b74a3b8cec8d82f56ceef57d4f97 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_before_create_creds-09bad0b040c673230f8890d35e883533.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=790da9b6820bb16d72ebaeec28c081c3 2500w" />
</Frame>

Finally, provide your Redshift username and password, and configure the **Delete on** field (after this date, your credentials will be removed from Datafold):

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d3f72a0e9d5dabfb88870f81f1e7bdfc" data-og-width="531" width="531" data-og-height="475" height="475" data-path="images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=40b9e30cd983f877c1f3444d2fd8507f 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=04b711aaf0388fdb3eca481dc1d9670e 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93404ca422fb458ccdd2586170ef37c3 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3d0cad66495744e7a99927326cbcd5da 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=df4f8d3c2c4b222165507ff4faf0dd3a 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/redshift_create_creds-efc65762308b064bfd208a0b3f19c4b3.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ca6d4dff56a9f605c93e1db9604b15fe 2500w" />
</Frame>

Click **Create credentials**.

## Example: BigQuery

1. To create a new Google Cloud OAuth 2.0 Client ID, go to the Google Cloud console, navigate to **APIs & Services**, then **Credentials**, and click **+ CREATE CREDENTIALS**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4905913a31f2f328e7a755ac5d09650d" data-og-width="1034" width="1034" data-og-height="304" height="304" data-path="images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f84077faf4c5f9d8a0a0dd793074ab1c 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f471870433e12a1e2b2c0ee329aa3e04 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5af4cee4f923ee74e7454cd4015bee5b 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f47c3a4ffb798c56e66dd627559a4fa1 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=64fe7791bddeb58e0e3b1f33d6f651aa 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_btn-15e16ea9d19edb6d0ad61835bd774970.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=496a6fa90f5d61129e2bf2024dc72217 2500w" />
</Frame>

Select **OAuth client ID**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0e709d4a6a5916bf21c6f940553c2a9c" data-og-width="502" width="502" data-og-height="275" height="275" data-path="images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=898c4b21c76bcfa8e5176ca2530f2343 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6b8ad94acd03f8926abc0178d91b8227 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=41e45dec682a86e69e0c04decf3c8b14 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=558b1b690e8969ea444ee02c7a4a897c 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9db85c16d696451c7891343a181fca0d 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_create_type-6412ecce9428e3aaf21722c81daa0ac9.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=db5c1c7d7e8c78a87b91d8d182936de7 2500w" />
</Frame>

From the list of **Application type**, select **Web application**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c197423a208dc2d144b9dcd2cbc905a9" data-og-width="617" width="617" data-og-height="459" height="459" data-path="images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d7b7aa8076045631f2bed9f8082c48b7 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=aae4f30e3c363dde551fb7bd7b952b68 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=45737eb052d7829449d01573da6e2eb1 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e4e8eab900e3bb47b1a2ab30ce278a67 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=073a9e055566e913b524cfc319eae15c 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_select_type-a21194f9850db4fe9d6babea49a36ba9.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=312eedd9efd3adf3467abab254fc53e7 2500w" />
</Frame>

Provide a name in the **Name** field:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d35dc1be31c0bc487576675f6e6d07ea" data-og-width="605" width="605" data-og-height="335" height="335" data-path="images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cdace1632c44a6c2a3e7c94c1edb6743 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2324d310af9db1d69df98251d6b759f7 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=21f44cc1336e67c55309c0fc1154114c 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e8434dd68bf74cdc3f6f523732319ce6 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4a2b937c2579b5676480ab890a3abd72 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_oauth_name-b31b7e54a61b764134fd8f8bab61ccda.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e9ddce0aecb9360480f4701926c144f8 2500w" />
</Frame>

In **Authorized redirect URIs**, provide `https://app.datafold.com/api/internal/oauth_dwh/callback`:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6a5dee352c37fa168fa413932070893e" data-og-width="606" width="606" data-og-height="391" height="391" data-path="images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=df5bdb9757734ec9f2703fa7b1557312 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5fdd1e2603724c593b3a749e40a0ca9e 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=48747cd3568ab6de8d6ba6b32495fdd6 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=decdeb4b34ba1cbb86986fe63cbb6a25 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=db48b4fb4904a31499857d8961c53dc4 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_redirect_uri-81f4b0fd9d93db76bf043170c6b027d6.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3af4afe07a253c2d98a75f20efb1462f 2500w" />
</Frame>

Click **CREATE**. Then, download the OAuth Client credentials as a JSON file:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1d5f2345d0c3b8dae42fd05ff31010a7" data-og-width="959" width="959" data-og-height="157" height="157" data-path="images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=62661927034a0a7190e848eac80a0fda 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f3ff896f467d2eddc5815f1e5db7eb7e 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=81f66feec8f4e354f62496c51b3cf57d 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=33ddf7aef7b4996b1618f2828e7e2b39 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fe6c5ed672f9d69de489c9eebf6cd8b2 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json1-1dfd1d02cbe9a84bd1124f24b28a293b.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a3fa18761b17014b9284e4986ceed700 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=dce5fb185e1daeccad692b9e2de95ce5" data-og-width="570" width="570" data-og-height="464" height="464" data-path="images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f61119b3df9b48fcdcb6049ef7f73b5c 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4b33ed12674578fd86ab8455cfbfed71 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0756eb523c38eebeced406ab85d6fac2 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a3f9c163ab7ab6f5db00997f846b0be3 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4a45ab9e608dc23a8de2f5f08673dcc5 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_download_json2-c6002a086c551afe7f06615bd1189ad9.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1f38bd4ea7b00fbb549ee6bd2c5fa9e4 2500w" />
</Frame>

1. Activate BigQuery OAuth in Datafold by uploading the JSON OAuth credentials in the **JSON OAuth keys file** section, in Datafold's BigQuery Data Connection **Advanced settings**:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ec7651764c65ca5944a9fba3ecc7abff" data-og-width="565" width="565" data-og-height="364" height="364" data-path="images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9436aa79fdadce93824eab16119ea947 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3ccbfb449fd888aed90a7d9cc0fbf083 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c935fb29b47c9b401ecc973b8cc63a47 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0ade161dfdf86396751f758cf36ec253 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=50241ab3380af18544eb7adcf9b9a2c9 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcloud_upload_json-72298dc179c0244871824afa1c0d1362.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=70df8d3ce62aa6ae1285f026246758be 2500w" />
</Frame>

Click **Test and Save**.

### Additional steps for BigQuery

1. Create a new temporary schema (dataset) for each OAuth user.

Go to Google Cloud console, navigate to BigQuery, select your project in BigQuery, and click on **Create dataset**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d96e1d0baa2f541b8982e561ccd7dec0" data-og-width="854" width="854" data-og-height="461" height="461" data-path="images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=88cf832b4449cb152cb26812acea5198 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=231980b9bbbef86b2cccfaa52d2a722d 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e700db87e381d871cb2730bd0d17255b 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=42dbfb7bdad770d3837a7fb6608b976a 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=da30326201a549ab8e6ede307f6f0b0c 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset1-56868087d2d2829fcf35c92046361179.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9d1633799da92ff4a2d72919c629c8bb 2500w" />
</Frame>

Provide `datafold_tmp_<username>` as the **Dataset ID** and set the same region as configured for other datasets. Click **CREATE DATASET**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6f5eee9e23b5e0cc17ac5cf4cf3bbfea" data-og-width="600" width="600" data-og-height="717" height="717" data-path="images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=04f480bd675d118869dcdbeb72a2fe80 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5fe7c1fc99db3fe9bf276f7ea7c4af10 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2ce3538d70cf07e4df09d864c7231e5c 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=630de468106efe6f17e0380bc4e5f96f 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8b333589474cbd5a28ee7adb41f41581 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_create_dataset2-ae5cb54f7dfb02699c0a8c6baf991205.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=54acc1cfdb6d8039b7c8a169a22f3e58 2500w" />
</Frame>

1. Configure permissions for `datafold_tmp_<username>`.

Grant read/write/create/delete permissions to the user for their `datafold_tmp_<username>` schema. This can be done by granting roles like **BigQuery Data Editor** or **BigQuery Data Owner** or any custom roles with the required permissions.

Go to Google Cloud console, navigate to BigQuery, select `datafold_tmp_<username>` dataset, and click **Create dataset** → **Manage Permissions**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9989c77e33d9c8d40101e5aac7c2a979" data-og-width="739" width="739" data-og-height="361" height="361" data-path="images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f0b1f01e2b49e73fcb542a1ed7a69aeb 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0a2ba425ab7469349354c9aa984b1804 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e81e037ad7933777de21dad0147e31f3 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=63f72fdf7be3976d4c84a81bb930018d 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9167ba1e691a3657ee37d853b4fddc9e 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions1-c085ec5f619915d10c8e1819aa31420c.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9b37b86665feec3ee743aa49de073855 2500w" />
</Frame>

Click **+ ADD PRINCIPAL**, specify the user and role, then click **SAVE**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a3e60b12eaa6d54d9e221013bed04a21" data-og-width="604" width="604" data-og-height="732" height="732" data-path="images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7f1050dc093e9657511d7bf62daf4016 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=32691682ea6ebf87393fb27461736e65 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=23d9328c76f4a7b8caf926d911509a0d 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dce6e5f68c8ad6fcafd51eaa4dbe1895 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4426be737dbe82574a823a6a0cc72025 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_config_schema_permissions2-2cea1df20480853fe7f9aacf1e786280.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=05fc2a428a4afa31225c9afc459f42ca 2500w" />
</Frame>

caution

Ensure that only the specified user (excluding admins) has read/write/create/delete permissions on `datafold_tmp_<username>`.

1. Configure temporary schema in Datafold.

As a user, navigate to `https://app.datafold.com/users/me`. If the user lacks credentials for BigQuery, click on **+ Add credentials**, select BigQuery datasource from the list, and click **Create credentials**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e2622cd1e1be8568cfc8c3c2de089d8f" data-og-width="528" width="528" data-og-height="308" height="308" data-path="images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=56a929eb8b7c869a94460bdb249d78d7 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bd1de29114cc4240425340791a1f2916 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9ee2c65f1dd8ad5256c977966112b2d3 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4524a4c45873f75f4f742b2332a05e3d 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6eaa79c59e13da3bc8a50dcb0c270c80 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema1-0ed07791aae93db489b72f56d9a8b956.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6711bc955c5a8ff7885aea5840121027 2500w" />
</Frame>

The user will be redirected to `accounts.google.com` and then returned to the previous page:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ec94dfc0f8a0cad000a4e5ed291d278d" data-og-width="945" width="945" data-og-height="568" height="568" data-path="images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f58954c9249c8d998ea97b2500fed64a 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b9dd1c7d4728b27d2f837ba0302e6000 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8b722f3609424923fa411ef497e72aae 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=89ec8306292fa155aab0924abc201877 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9dd6a09b7ace6eb77195913e500f0b96 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema2-dc4418e6faa3aaceb9ecccd773618fd4.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b2322e97a0d94120955d68b7feaecb90 2500w" />
</Frame>

Select BigQuery credentials from the list, input the **Temporary Schema** field in the format `<project>.<datafold_tmp_<username>>`, and click **Update**:

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8ec2d70ffeee17a7318a66784aca373a" data-og-width="526" width="526" data-og-height="365" height="365" data-path="images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5058d821083509dde08712f76a87bd90 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=419485442d5532209ff26f1fb8b2eaa7 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1d10d6ac876cd7f2c4b115fe4ca1c33d 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=01b731418e545edf5f9d67d2e7243feb 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a01890857e91623ce9a2e6beaff1c190 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bq_datafold_temp_schema3-19e078cdc1acee794bfb92a2abb907a4.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=be3ef9191263981497cad5e8ff623cfa 2500w" />
</Frame>

<Note>
  **INFO**

  Users can update BigQuery credentials only if they have the correct permissions for `<datafold_tmp_<username>`.
</Note>
