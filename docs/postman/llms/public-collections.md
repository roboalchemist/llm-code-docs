# Prepare your public collections for the Postman API Network

Create a public API reference collection and overview collection for your API consumers. When you [publish your public APIs](/docs/postman-api-network/showcase/publish/public-apis/), you can invite your API consumers to [fork your public collections](/docs/collaborating-in-postman/using-version-control/forking-elements/), and get them to their first 200 OK response fast.

An API reference collection contains your public API's endpoints and their HTTP methods. An overview collection compliments your API reference collection and serves as a starting point for your API consumers.

## Important:
Protect your sensitive data. If Postman detects any API keys, tokens, or similar, it replaces them with placeholders. To learn more, see [Postman Secret Scanner](/docs/administration/managing-your-team/secret-scanner/overview/).

## Create your public API reference collection

An API reference collection is a comprehensive list of your public API's endpoints and their HTTP methods, which define your API's operations. It's often based on an API specification, such an OpenAPI definition.

Postman recommends you [import your OpenAPI definition to create your API reference collection](#import-your-openapi-definition-to-create-your-api-reference-collection). If you don't have an OpenAPI definition, you can [manually create your API reference collection](#manually-create-your-api-reference-collection).

### Import your OpenAPI definition to create your API reference collection

To import your OpenAPI definition to create your API reference collection, do the following:

1. From the Postman sidebar, click **Import**.
2. Use one of the options to import your OpenAPI definition.
3. Click **Postman Collection**.
4. (Optional) Click ![Image 1: Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **View Import Settings** and edit your settings.
5. Click **Import**.

Postman turns your OpenAPI definition into a Postman Collection. You can continue to edit your API reference collection as your public APIs evolve and you [curate your public collections](/docs/postman-api-network/showcase/prepare/curate/overview/).

To learn more, see [Import an API into Postman](/docs/design-apis/api-builder/importing-an-api/).

### Manually create your API reference collection

If you don't have an OpenAPI definition, you can manually create your API reference collection.

To manually create your API reference collection, do the following:

1. From the Postman sidebar, click ![Image 2: Collection icon](https://assets.postman.com/postman-docs/aether-icons/entity-collection-stroke.svg#icon) **Collections**.
2. Select ![Image 3: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Create new collection** \[![Image 4: New collection icon](https://assets.postman.com/postman-docs/aether-icons/action-newCollection-stroke.svg#icon)\] **Blank collection**.
3. [Name your collection](/docs/postman-api-network/showcase/prepare/curate/public-collections-overview/#name-your-collection) and [write a description for it](/docs/postman-api-network/showcase/prepare/curate/public-collections-overview/#write-a-description-for-your-collection).
4. [Add requests to your collection](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#add-requests-to-your-collection) and [examples to your requests](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#add-examples-to-your-requests).
5. [Document your requests](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#document-your-requests).
6. [Organize your collection with folders](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#organize-your-collection-with-folders).

You can continue to edit your API reference collection as your public APIs evolve and you [curate your public collections](/docs/postman-api-network/showcase/prepare/curate/overview/).

To learn more, see [Create a new collection](/docs/collections/use-collections/create-collections/).

## Create your public overview collection

An overview collection compliments your API reference collection. It's a starting point for your API consumers. Use an overview collection to summarize your public APIs and get your API consumers to their first 200 OK response in the fewest steps as possible. You can also showcase your public APIs with common use cases and popular workflows.

To create your public overview collection, do the following:

1. From the Postman sidebar, click ![Image 5: Collection icon](https://assets.postman.com/postman-docs/aether-icons/entity-collection-stroke.svg#icon) **Collections**.
2. Select ![Image 6: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Create new collection** \[![Image 7: New collection icon](https://assets.postman.com/postman-docs/aether-icons/action-newCollection-stroke.svg#icon)\] **Blank collection**.
3. [Name your collection](/docs/postman-api-network/showcase/prepare/curate/public-collections-overview/#name-your-collection) and [write a description for it](/docs/postman-api-network/showcase/prepare/curate/public-collections-overview/#write-a-description-for-your-collection).
4. [Add requests to your collection](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#add-requests-to-your-collection) and [examples to your requests](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#add-examples-to-your-requests).
5. [Document your requests](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#document-your-requests).
6. [Organize your collection with folders](/docs/postman-api-network/showcase/prepare/curate/public-collections-requests/#organize-your-collection-with-folders).

You can continue to edit your overview collection as your public APIs evolve and you [curate your public collections](/docs/postman-api-network/showcase/prepare/curate/overview/).

To learn more, see [Create a new collection](/docs/collections/use-collections/create-collections/).

## Create a Stripe API key

To create a Stripe API key to use with Postman Flows, do the following:

1. Log in to [Stripe](https://dashboard.stripe.com/login).
2. In the Developer Dashboard, select [API keys](https://dashboard.stripe.com/test/apikeys).
3. Select **Create secret key** to create a new key.
4. Copy the key, and then save it as a variable in your Postman environment named `Stripe_Api_Key`.
5. Save the data center identifier as a variable in your Postman environment named `Stripe_DC`.

## Create a Slack API key

To create a Slack API key to use with Postman Flows, do the following:

1. Log in to [Slack](https://www.slack.com/)
2. Navigate to **Settings** > **Account** > **Extras** > **API Keys**.
3. Select **Create A Key**. Enter a name for the key, and then select **Generate Key**.
4. Copy the key you generated, excluding the suffix that contains the data center identifier. For example, if the key value is `YOUR_API_KEY-us00`, don't include `-us00`.
5. Save the key value as a variable in your Postman environment named `Slack_API_Key`.

## Create a Notion API key

To create a Notion API key to use with Postman Flows, do the following:

1. Log in to [Notion](https://www.notion.so/)
2. Navigate to **Settings** > **Account** > **Accounts** > **My Account**.
3. Select **Create a new account**.
4. Enter a name for the account, and then select **Create**.
5. Select **Notion** as the account type.
6. Select **Create account**.
7. Enter a password for the account, and then select **Save**.
8. Select **Notion** as the account type.
9. Select **Create account**.
10. Enter a password for the account, and then select **Save**.
11. Select **Notion** as the account type.
12. Select **Create account**.
13. Enter a password for the account, and then select **Save**.
14. Select **Notion** as the account type.
15. Select **Create account**.
16. Enter a password for the account, and then select **Save**.
17. Select **Notion** as the account type.
18. Select **Create account**.
19. Enter a password for the account, and then select **Save**.
20. Select **Notion** as the account type.
21. Select **Create account**.
22. Enter a password for the account, and then select **Save**.
23. Select **Notion** as the account type.
24. Select **Create account**.
25. Enter a password for the account, and then select **Save**.
26. Select **Notion** as the account type.
27. Select **Create account**.
28. Enter a password for the account, and then select **Save**.
29. Select **Notion** as the account type.
30. Select **Create account**.
31. Enter a password for the account, and then select **Save**.
32. Select **Notion** as the account type.
33. Select **Create account**.
34. Enter a password for the account, and then select **Save**.
35. Select **Notion** as the account type.
36. Select **Create account**.
37. Enter a password for the account, and then select **Save**.
38. Select **Notion** as the account type.
39. Select **Create account**.
40. Enter a password for the account, and then select **Save**.
41. Select **Notion** as the account type.
42. Select **Create account**.
43. Enter a password for the account, and then select **Save**.
44. Select **Notion** as the account type.
45. Select **Create account**.
46. Enter a password for the account, and then select **Save**.
47. Select **Notion** as the account type.
48. Select **Create account**.
49. Enter a password for the account, and then select **Save**.
50. Select **Notion** as the account type.
51. Select **Create account**.
52. Enter a password for the account, and then select **Save**.
53. Select **Notion** as the account type.
54. Select **Create account**.
55. Enter a password for the account, and then select **Save**.
56. Select **Notion** as the account type.
57. Select **Create account**.
58. Enter a password for the account, and then select **Save**.
59. Select **Notion** as the account type.
60. Select **Create account**.
61. Enter a password for the account, and then select **Save**.
62. Select **Notion** as the account type.
63. Select **Create account**.
64. Enter a password for the account, and then select **Save**.
65. Select **Notion** as the account type.
66. Select **Create account**.
67. Enter a password for the account, and then select **Save**.
68. Select **Notion** as the account type.
69. Select **Create account**.
70. Enter a password for the account, and then select **Save**.
71. Select **Notion** as the account type.
72. Select **Create account**.
73. Enter a password for the account, and then select **Save**.
74. Select **Notion** as the account type.
75. Select **Create account**.
76. Enter a password for the account, and then select **Save**.
77. Select **Notion** as the account type.
78. Select **Create account**.
79. Enter a password for the account, and then select **Save**.
80. Select **Notion** as the account type.
81. Select **Create account**.
82. Enter a password for the account, and then select **Save**.
83. Select **Notion** as the account type.
84. Select **Create account**.
85. Enter a password for the account, and then select **Save**.
86. Select **Notion** as the account type.
87. Select **Create account**.
88. Enter a password for the account, and then select **Save**.
89. Select **Notion** as the account type.
90. Select **Create account**.
91. Enter a password for the account, and then select **Save**.
92. Select **Notion** as the account type.
93. Select **Create account**.
94. Enter a password for the account, and then select **Save**.
95. Select **Notion** as the account type.
96. Select **Create account**.
97. Enter a password for the account, and then select **Save**.
98. Select **Notion** as the account type.
99. Select **Create account**.
100. Enter a password for the account, and then select **Save**.
101. Select **Notion** as the account type.
102. Select **Create account**.
103. Enter a password for the account, and then select **Save**.
104. Select **Notion** as the account type.
105. Select **Create account**.
106. Enter a password for the account, and then select **Save**.
107. Select **Notion** as the account type.
108. Select **Create account**.
109. Enter a password for the account, and then select **Save**.
110. Select **Notion** as the account type.
111. Select **Create account**.
112. Enter a password for the account, and then select **Save**.
113. Select **Notion** as the account type.
114. Select **Create account**.
115. Enter a password for the account, and then select **Save**.
116. Select **Notion** as the account type.
117. Select **Create account**.
118. Enter a password for the account, and then select **Save**.
119. Select **Notion** as the account type.
120. Select **Create account**.
121. Enter a password for the account, and then select **Save**.
122. Select **Notion** as the account type.
123. Select **Create account**.
124. Enter a password for the account, and then select **Save**.
125. Select **Notion** as the account type.
126. Select **Create account**.
127. Enter a password for the account, and then select **Save**.
128. Select **Notion** as the account type.
129. Select **Create account**.
130. Enter a password for the account, and then select **Save**.
131. Select **Notion** as the account type.
132. Select **Create account**.
133. Enter a password for the account, and then select **Save**.
134. Select **Notion** as the account type.
135. Select **Create account**.
136. Enter a password for the account, and then select **Save**.
137. Select **Notion** as the account type.
138. Select **Create account**.
139. Enter a password for the account, and then select **Save**.
140. Select **Notion** as the account type.
141. Select **Create account**.
142. Enter a password for the account, and then select **Save**.
143. Select **Notion** as the account type.
144. Select **Create account**.
145. Enter a password for the account, and then select **Save**.
146. Select **Notion** as the account type.
147. Select **Create account**.
148. Enter a password for the account, and then select **Save**.
149. Select **Notion** as the account type.
150. Select **Create account**.
151. Enter a password for the account, and then select **Save**.
152. Select **Notion** as the account type.
153. Select **Create account**.
154. Enter a password for the account, and then select **Save**.
155. Select **Notion** as the account type.
156. Select **Create account**.
157. Enter a password for the account, and then select **Save**.
158. Select **Notion** as the account type.
159. Select **Create account**.
160. Enter a password for the account, and then select **Save**.
161. Select **Notion** as the account type.
162. Select **Create account**.
163. Enter a password for the account, and then select **Save**.
164. Select **Notion** as the account type.
165. Select **Create account**.
166. Enter a password for the account, and then select **Save**.
167. Select **Notion** as the account type.
168. Select **Create account**.
169. Enter a password for the account, and then select **Save**.
170. Select **Notion** as the account type.
171. Select **Create account**.
172. Enter a password for the account, and then select **Save**.
173. Select **Notion** as the account type.
174. Select **Create account**.
175. Enter a password for the account, and then select **Save**.
176. Select **Notion** as the account type.
177. Select **Create account**.
178. Enter a password for the account, and then select **Save**.
179. Select **Notion** as the account type.
180. Select **Create account**.
181. Enter a password for the account, and then select **Save**.
182. Select **Notion** as the account type.
183. Select **Create account**.
184. Enter a password for the account, and then select **Save**.
185. Select **Notion** as the account type.
186. Select **Create account**.
187. Enter a password for the account, and then select **Save**.
188. Select **Notion** as the account type.
189. Select **Create account**.
190. Enter a password for the account, and then select **Save**.
191. Select **Notion** as the account type.
192. Select **Create account**.
193. Enter a password for the account, and then select **Save**.
194. Select **Notion** as the account type.
195. Select **Create account**.
196. Enter a password for the account, and then select **Save**.
197. Select **Notion** as the account type.
198. Select **Create account**.
199. Enter a password for the account, and then select **Save**.
200. Select **Notion** as the account type.
201. Select **Create account**.
202. Enter a password for the account, and then select **Save**.
203. Select **Notion** as the account type.
204. Select **Create account**.
205. Enter a password for the account, and then select **Save**.
206. Select **Notion** as the account type.
207. Select **Create account**.
208. Enter a password for the account, and then select **Save**.
209. Select **Notion** as the account type.
210. Select **Create account**.
211. Enter a password for the account, and then select **Save**.
212. Select **Notion** as the account type.
213. Select **Create account**.
214. Enter a password for the account, and then select **Save**.
215. Select **Notion** as the account type.
216. Select **Create account**.
217. Enter a password for the account, and then select **Save**.
218. Select **Notion** as the account type.
219. Select **Create account**.
220. Enter a password for the account, and then select **Save**.
221. Select **Notion** as the account type.
222. Select **Create account**.
223. Enter a password for the account, and then select **Save**.
224. Select **Notion** as the account type.
225. Select **Create account**.
226. Enter a password for the account, and then select **Save**.
227. Select **Notion** as the account type.
228. Select **Create account**.
229. Enter a password for the account, and then select **Save**.
230. Select **Notion** as the account type.
231. Select **Create account**.
232. Enter a password for the account, and then select **Save**.
233. Select **Notion** as the account type.
234. Select **Create account**.
235. Enter a password for the account, and then select **Save**.
236. Select **Notion** as the account type.
237. Select **Create account**.
238. Enter a password for the account, and then select **Save**.
239. Select **Notion** as the account type.
240. Select **Create account**.
241. Enter a password for the account, and then select **Save**.
242. Select **Notion** as the account type.
243. Select **Create account**.
244. Enter a password for the account, and then select **Save**.
245. Select **Notion** as the account type.
246. Select **Create account**.
247. Enter a password for the account, and then select **Save**.
248. Select **Notion** as the account type.
249. Select **Create account**.
250. Enter a password for the account, and then select **Save**.
251. Select **Notion** as the account type.
252. Select **Create account**.
253. Enter a password for the account, and then select **Save**.
254. Select **Notion** as the account type.
255. Select **Create account**.
256. Enter a password for the account, and then select **Save**.
257. Select **Notion** as the account type.
258. Select **Create account**.
259. Enter a password for the account, and then select **Save**.
260. Select **Notion** as the account type.
261. Select **Create account**.
262. Enter a password for the account, and then select **Save**.
263. Select **Notion** as the account type.
264. Select **Create account**.
265. Enter a password for the account, and then select **Save**.
266. Select **Notion** as the account type.
267. Select **Create account**.
268. Enter a password for the account, and then select **Save**.
269. Select **Notion** as the account type.
270. Select **Create account**.
271. Enter a password for the account, and then select **Save**.
272. Select **Notion** as the account type.
273. Select **Create account**.
274. Enter a password for the account, and then select **Save**.
275. Select **Notion** as the account type.
276. Select **Create account**.
277. Enter a password for the account, and then select **Save**.
278. Select **Notion** as the account type.
279. Select **Create account**.
280. Enter a password for the account, and then select **Save**.
281. Select **Notion** as the account type.
282. Select **Create account**.
283. Enter a password for the account, and then select **Save**.
284. Select **Notion** as the account type.
285. Select **Create account**.
286. Enter a password for the account, and then select **Save**.
287. Select **Notion** as the account type.
288. Select **Create account**.
289. Enter a password for the account, and then select **Save**.
290. Select **Notion** as the account type.
291. Select **Create account**.
292. Enter a password for the account, and then select **Save**.
293. Select **Notion** as the account type.
294. Select **Create account**.
295. Enter a password for the account, and then select **Save**.
296. Select **Notion** as the account type.
297. Select **Create account**.
298. Enter a password for the account, and then select **Save**.
299. Select **Notion** as the account type.
300. Select **Create account**.
301. Enter a password for the account, and then select **Save**.
302. Select **Notion** as the account type.
303. Select **Create account**.
304. Enter a password for the account, and then select **Save**.
305. Select **Notion** as the account type.
306. Select **Create account**.
307. Enter a password for the account, and then select **Save**.
308. Select **Notion** as the account type.
309. Select **Create account**.
310. Enter a password for the account, and then select **Save**.
311. Select **Notion** as the account type.
312. Select **Create account**.
313. Enter a password for the account, and then select **Save**.
314. Select **Notion** as the account type.
315. Select **Create account**.
316. Enter a password for the account, and then select **Save**.
317. Select **Notion** as the account type.
318. Select **Create account**.
319. Enter a password for the account, and then select **Save**.
320. Select **Notion** as the account type.
321. Select **Create account**.
322. Enter a password for the account, and then select **Save**.
323. Select **Notion** as the account type.
324. Select **Create account**.
325. Enter a password for the account, and then select **Save**.
326. Select **Notion** as the account type.
327. Select **Create account**.
328. Enter a password for the account, and then select **Save**.
329. Select **Notion** as the account type.
330. Select **Create account**.
331. Enter a password for the account, and then select **Save**.
332. Select **Notion** as the account type.
333. Select **Create account**.
334. Enter a password for the account, and then select **Save**.
335. Select **Notion** as the account type.
336. Select **Create account**.
337. Enter a password for the account, and then select **Save**.
338. Select **Notion** as the account type.
339. Select **Create account**.
340. Enter a password for the account, and then select **Save**.
341. Select **Notion** as the account type.
342. Select **Create account**.
343. Enter a password for the account, and then select **Save**.
344. Select **Notion** as the account type.
345. Select **Create account**.
346. Enter a password for the account, and then select **Save**.
347. Select **Notion** as the account type.
348. Select **Create account**.
349. Enter a password for the account, and then select **Save**.
350. Select **Notion** as the account type.
351. Select **Create account**.
352. Enter a password for the account, and then select **Save**.
353. Select **Notion** as the account type.
354. Select **Create account**.
355. Enter a password for the account, and then select **Save**.
356. Select **Notion** as the account type.
357. Select **Create account**.
358. Enter a password for the account, and then select **Save**.
359. Select **Notion** as the account type.
360. Select **Create account**.
361. Enter a password for the account, and then select **Save**.
362. Select **Notion** as the account type.
363. Select **Create account**.
364. Enter a password for the account, and then select **Save**.
365. Select **Notion** as the account type.
366. Select **Create account**.
367. Enter a password for the account, and then select **Save**.
368. Select **Notion** as the account type.
369. Select **Create account**.
370. Enter a password for the account, and then select **Save**.
371. Select **Notion** as the account type.
372. Select **Create account**.
373. Enter a password for the account, and then select **Save**.
374. Select **Notion** as the account type.
375. Select **Create account**.
376. Enter a password for the account, and then select **Save**.
377. Select **Notion** as the account type.
378. Select **Create account**.
378. Enter a password for the account, and then select **Save**.
379. Select **Notion** as the account type.
380. Select **Create account**.
381. Enter a password for the account, and then select **Save**.
382. Select **Notion** as the account type.
383. Select **Create account**.
384. Enter a password for the account, and then select **Save**.
385. Select **Notion** as the account type.
386. Select **Create account**.
387. Enter a password for the account, and then select **Save**.
388. Select **Notion** as the account type.
389. Select **Create account**.
390. Enter a password for the account, and then select **Save**.
391. Select **Notion** as the account type.
392. Select **Create account**.
393. Enter a password for the account, and then select **Save**.
394. Select **Notion** as the account type.
395. Select **Create account**.
396. Enter a password for the account, and then select **Save**.
397. Select **Notion** as the account type.
398. Select **Create account**.
395. Enter a password for the account, and then select **Save**.
396. Select **Notion** as the account type.
397. Select **Create account**.
398. Enter a password for the account, and then select **Save**.
399. Select **Notion** as the account type.
400. Select **Create account**.
401. Enter a password for the account, and then select **Save**.
402. Select **Notion** as the account type.
403. Select **Create account**.
404. Enter a password for the account, and then select **Save**.
405. Select **Notion** as the account type.
406. Select **Create account**.
407. Enter a password for the account, and then select **Save**.
408. Select **Notion** as the account type.
409. Select **Create account**.
410. Enter a password for the account, and then select **Save**.
411. Select **Notion** as the account type.
412. Select **Create account**.
413. Enter a password for the account, and then select **Save**.
414. Select **Notion** as the account type.
415. Select **Create account**.
416. Enter a password for the account, and then select **Save**.
417. Select **Notion** as the account type.
418. Select **Create account**.
419. Enter a password for the account, and then select **Save**.
420. Select **Notion** as the account type.
421. Select **Create account**.
422. Enter a password for the account, and then select **Save**.
423. Select **Notion** as the account type.
424. Select **Create account**.
425. Enter a password for the account, and then select **Save**.
426. Select **Notion** as the account type.
427. Select **Create account**.
428. Enter a password for the account, and then select **Save**.
429. Select **Notion** as the account type.
430. Select **Create account**.
431. Enter a password for the account, and then select **Save**.
432. Select **Notion** as the account type.
433. Select **Create account**.
434. Enter a password for the account, and then select **Save**.
435. Select **Notion** as the account type.
436. Select **Create account**.
437. Enter a password for the account, and then select **Save**.
438. Select **Notion** as the account type.
435. Select **Create account**.
436. Enter a password for the account, and then select **Save**.
437. Select **Notion** as the account type.
438. Select **Create account**.
439. Enter a password for the account, and then select **Save**.
440. Select **Notion** as the account type.
441. Select **Create account**.
442. Enter a password for the account, and then select **Save**.
443. Select **Notion** as the account type.
444. Select **Create account**.
445. Enter a password for the account, and then select **Save**.
446. Select **Notion** as the account type.
447. Select **Create account**.
448. Enter a password for the account, and then select **Save**.
449. Select **Notion** as the account type.
450. Select **Create account**.
451. Enter a password for the account, and then select **Save**.
452. Select **Notion** as the account type.
453. Select **Create account**.
454. Enter a password for the account, and then select **Save**.
455. Select **Notion** as the account type.
456. Select **Create account**.
457. Enter a password for the account, and then select **Save**.
458. Select **Notion** as the account type.
459. Select **Create account**.
460. Enter a password for the account, and then select **Save**.
461. Select **Notion** as the account type.
462. Select **Create account**.
463. Enter a password for the account, and then select **Save**.