# Install and update Postman

To get the latest version of the Postman desktop app, visit the [Download Postman page](https://www.postman.com/downloads/) and select the option for your operating system. Postman is available as a native desktop app for Windows (Intel 64-bit or ARM 64-bit), macOS (Intel or Apple silicon), and Linux (Intel 64-bit or ARM 64-bit).

Postman is also available as a [web app](https://go.postman.co/home/). You can use the Postman web app to carry out many of your API development and testing tasks in your web browser. Keep in mind that some features aren't supported when using the [Postman web app](/docs/getting-started/installation/installation-and-updates/#web-limitations), so use the Postman desktop app for the full Postman experience.

## Install Postman on Windows

To install Postman on Windows, do the following:

1. [Download](https://www.postman.com/downloads/) the latest Postman version.
2. Select and run the .exe file to install Postman.

![Postman Desktop App Installation](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

1. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
2. Click **Add Members**. To be added, members need to be part of the organization.
3. Determine how restricted the Team access should be. All Organization Teams have two settings:
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
4. Populate the team with the members who are responsible for the team’s contents.
5. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
6. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
7. Click **Create**.

![Create a Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
5. Enter a name for the component file and select the OpenAPI specification format it'll be used in. You can't change the name or OpenAPI specification version of a component file later.
6. Click **Create**.

![Create a Component File](https://assets.postman.com/postman-docs/v11/component-library-create-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component file in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Edit a Component File](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your component file, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component in the left sidebar that you'd like to version and publish.
5. Click **Version & Publish** in the upper right corner.

![Version and Publish a Component File](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)

1. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
2. Click **Create Version & Publish**.

Once the component is published, your teammates can [reference the file's components](#reference-a-component-in-a-specification) in their specifications.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Click ![Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of a specification.
3. Click **Open Component Library**.
4. Search for a component file and select it in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Link icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Reference a Component in a Specification](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

As you edit your specification, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original team's shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

### Determine the structure of your teams and memberships

A team within an Organization represents physical members of a functional team, for example, developer or test team, and also contains the workspaces that the group of users wants to keep secure and access controlled.

By creating teams and memberships first, you can establish strategic collaborations and empower your teams to migrate their own work to their teams. For example, even if your QA team hasn't moved all their workspaces to a QA-designated team yet, other teams can still invite the QA team members to collaborate with their team.

Once you define the teams, you can start the process of improving collaboration and security by populating the teams with your workspaces.

To determine the team membership, do the following:

1. The [Organization Manager (or Super Admin)](/docs/administration/organization/roles/) creates a Team and assigns a Team Manager to it.
2. Determine how restricted the Team access should be. All Organization Teams have two settings:
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
3. Populate the team with the members who are responsible for the team’s contents.
4. If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
5. If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
6. Ensure the team is prepopulated with the appropriate roles.
7. Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two settings:
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team’s contents.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create**.

![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
5. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
6. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
7. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
8. Click **Create**.

![Create Organization Workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)

1. Select the team in the left sidebar.
2. Select the workspace in the left sidebar.
3. Select the workspace in the left sidebar.
4. Select the workspace in the left sidebar.
5. Select the workspace in the left sidebar.
6. Select the workspace in the left sidebar.
7. Select the workspace in the left sidebar.
8. Select the workspace in the left sidebar.
9. Select the workspace in the left sidebar.
10. Select the workspace in the left sidebar.
11. Select the workspace in the left sidebar.
12. Select the workspace in the left sidebar.
13. Select the workspace in the left sidebar.
14. Select the workspace in the left sidebar.
15. Select the workspace in the left sidebar.
16. Select the workspace in the left sidebar.
17. Select the workspace in the left sidebar.
18. Select the workspace in the left sidebar.
19. Select the workspace in the left sidebar.
20. Select the workspace in the left sidebar.
21. Select the workspace in the left sidebar.
22. Select the workspace in the left sidebar.
23. Select the workspace in the left sidebar.
24. Select the workspace in the left sidebar.
25. Select the workspace in the left sidebar.
26. Select the workspace in the left sidebar.
27. Select the workspace in the left sidebar.
28. Select the workspace in the left sidebar.
29. Select the workspace in the left sidebar.
30. Select the workspace in the left sidebar.
31. Select the workspace in the left sidebar.
32. Select the workspace in the left sidebar.
33. Select the workspace in the left sidebar.
34. Select the workspace in the left sidebar.
35. Select the workspace in the left sidebar.
36. Select the workspace in the left sidebar.
37. Select the workspace in the left sidebar.
38. Select the workspace in the left sidebar.
39. Select the workspace in the left sidebar.
40. Select the workspace in the left sidebar.
41. Select the workspace in the left sidebar.
42. Select the workspace in the left sidebar.
43. Select the workspace in the left sidebar.
44. Select the workspace in the left sidebar.
45. Select the workspace in the left sidebar.
46. Select the workspace in the left sidebar.
47. Select the workspace in the left sidebar.
48. Select the workspace in the left sidebar.
49. Select the workspace in the left sidebar.
50. Select the workspace in the left sidebar.
51. Select the workspace in the left sidebar.
52. Select the workspace in the left sidebar.
53. Select the workspace in the left sidebar.
54. Select the workspace in the left sidebar.
55. Select the workspace in the left sidebar.
56. Select the workspace in the left sidebar.
57. Select the workspace in the left sidebar.
58. Select the workspace in the left sidebar.
59. Select the workspace in the left sidebar.
60. Select the workspace in the left sidebar.
61. Select the workspace in the left sidebar.
62. Select the workspace in the left sidebar.
63. Select the workspace in the left sidebar.
64. Select the workspace in the left sidebar.
65. Select the workspace in the left sidebar.
66. Select the workspace in the left sidebar.
67. Select the workspace in the left sidebar.
68. Select the workspace in the left sidebar.
69. Select the workspace in the left sidebar.
70. Select the workspace in the left sidebar.
71. Select the workspace in the left sidebar.
72. Select the workspace in the left sidebar.
73. Select the workspace in the left sidebar.
74. Select the workspace in the left sidebar.
75. Select the workspace in the left sidebar.
76. Select the workspace in the left sidebar.
77. Select the workspace in the left sidebar.
78. Select the workspace in the left sidebar.
79. Select the workspace in the left sidebar.
80. Select the workspace in the left sidebar.
81. Select the workspace in the left sidebar.
82. Select the workspace in the left sidebar.
83. Select the workspace in the left sidebar.
84. Select the workspace in the left sidebar.
85. Select the workspace in the left sidebar.
86. Select the workspace in the left sidebar.
87. Select the workspace in the left sidebar.
88. Select the workspace in the left sidebar.
89. Select the workspace in the left sidebar.
90. Select the workspace in the left sidebar.
91. Select the workspace in the left sidebar.
92. Select the workspace in the left sidebar.
93. Select the workspace in the left sidebar.
94. Select the workspace in the left sidebar.
95. Select the workspace in the left sidebar.
96. Select the workspace in the left sidebar.
97. Select the workspace in the left sidebar.
98. Select the workspace in the left sidebar.
99. Select the workspace in the left sidebar.
100. Select the workspace in the left sidebar.
101. Select the workspace in the left sidebar.
102. Select the workspace in the left sidebar.
103. Select the workspace in the left sidebar.
104. Select the workspace in the left sidebar.
105. Select the workspace in the left sidebar.
106. Select the workspace in the left sidebar.
107. Select the workspace in the left sidebar.
108. Select the workspace in the left sidebar.
109. Select the workspace in the left sidebar.
110. Select the workspace in the left sidebar.
111. Select the workspace in the left sidebar.
112. Select the workspace in the left sidebar.
113. Select the workspace in the left sidebar.
114. Select the workspace in the left sidebar.
115. Select the workspace in the left sidebar.
116. Select the workspace in the left sidebar.
117. Select the workspace in the left sidebar.
118. Select the workspace in the left sidebar.
119. Select the workspace in the left sidebar.
120. Select the workspace in the left sidebar.
121. Select the workspace in the left sidebar.
122. Select the workspace in the left sidebar.
123. Select the workspace in the left sidebar.
124. Select the workspace in the left sidebar.
125. Select the workspace in the left sidebar.
126. Select the workspace in the left sidebar.
127. Select the workspace in the left sidebar.
128. Select the workspace in the left sidebar.
129. Select the workspace in the left sidebar.
130. Select the workspace in the left sidebar.
131. Select the workspace in the left sidebar.
132. Select the workspace in the left sidebar.
133. Select the workspace in the left sidebar.
134. Select the workspace in the left sidebar.
135. Select the workspace in the left sidebar.
136. Select the workspace in the left sidebar.
137. Select the workspace in the left sidebar.
138. Select the workspace in the left sidebar.
139. Select the workspace in the left sidebar.
140. Select the workspace in the left sidebar.
141. Select the workspace in the left sidebar.
142. Select the workspace in the left sidebar.
143. Select the workspace in the left sidebar.
144. Select the workspace in the left sidebar.
145. Select the workspace in the left sidebar.
146. Select the workspace in the left sidebar.
147. Select the workspace in the left sidebar.
148. Select the workspace in the left sidebar.
149. Select the workspace in the left sidebar.
150. Select the workspace in the left sidebar.
151. Select the workspace in the left sidebar.
152. Select the workspace in the left sidebar.
153. Select the workspace in the left sidebar.
154. Select the workspace in the left sidebar.
155. Select the workspace in the left sidebar.
156. Select the workspace in the left sidebar.
157. Select the workspace in the left sidebar.
158. Select the workspace in the left sidebar.
159. Select the workspace in the left sidebar.
160. Select the workspace in the left sidebar.
161. Select the workspace in the left sidebar.
162. Select the workspace in the left sidebar.
163. Select the workspace in the left sidebar.
164. Select the workspace in the left sidebar.
165. Select the workspace in the left sidebar.
166. Select the workspace in the left sidebar.
167. Select the workspace in the left sidebar.
168. Select the workspace in the left sidebar.
169. Select the workspace in the left sidebar.
170. Select the workspace in the left sidebar.
171. Select the workspace in the left sidebar.
172. Select the workspace in the left sidebar.
173. Select the workspace in the left sidebar.
174. Select the workspace in the left sidebar.
175. Select the workspace in the left sidebar.
176. Select the workspace in the left sidebar.
177. Select the workspace in the left sidebar.
178. Select the workspace in the left sidebar.
179. Select the workspace in the left sidebar.
180. Select the workspace in the left sidebar.
181. Select the workspace in the left sidebar.
182. Select the workspace in the left sidebar.
183. Select the workspace in the left sidebar.
184. Select the workspace in the left sidebar.
185. Select the workspace in the left sidebar.
186. Select the workspace in the left sidebar.
187. Select the workspace in the left sidebar.
188. Select the workspace in the left sidebar.
189. Select the workspace in the left sidebar.
190. Select the workspace in the left sidebar.
191. Select the workspace in the left sidebar.
192. Select the workspace in the left sidebar.
193. Select the workspace in the left sidebar.
194. Select the workspace in the left sidebar.
195. Select the workspace in the left sidebar.
196. Select the workspace in the left sidebar.
197. Select the workspace in the left sidebar.
198. Select the workspace in the left sidebar.
199. Select the workspace in the left sidebar.
200. Select the workspace in the left sidebar.
201. Select the workspace in the left sidebar.
202. Select the workspace in the left sidebar.
203. Select the workspace in the left sidebar.
204. Select the workspace in the left sidebar.
205. Select the workspace in the left sidebar.
206. Select the workspace in the left sidebar.
207. Select the workspace in the left sidebar.
208. Select the workspace in the left sidebar.
209. Select the workspace in the left sidebar.
210. Select the workspace in the left sidebar.
211. Select the workspace in the left sidebar.
212. Select the workspace in the left sidebar.
213. Select the workspace in the left sidebar.
214. Select the workspace in the left sidebar.
215. Select the workspace in the left sidebar.
216. Select the workspace in the left sidebar.
217. Select the workspace in the left sidebar.
218. Select the workspace in the left sidebar.
219. Select the workspace in the left sidebar.
220. Select the workspace in the left sidebar.
221. Select the workspace in the left sidebar.
222. Select the workspace in the left sidebar.
223. Select the workspace in the left sidebar.
224. Select the workspace in the left sidebar.
225. Select the workspace in the left sidebar.
226. Select the workspace in the left sidebar.
227. Select the workspace in the left sidebar.
228. Select the workspace in the left sidebar.
229. Select the workspace in the left sidebar.
230. Select the workspace in the left sidebar.
231. Select the workspace in the left sidebar.
232. Select the workspace in the left sidebar.
233. Select the workspace in the left sidebar.
234. Select the workspace in the left sidebar.
235. Select the workspace in the left sidebar.
236. Select the workspace in the left sidebar.
237. Select the workspace in the left sidebar.
238. Select the workspace in the left sidebar.
239. Select the workspace in the left sidebar.
240. Select the workspace in the left sidebar.
241. Select the workspace in the left sidebar.
242. Select the workspace in the left sidebar.
243. Select the workspace in the left sidebar.
244. Select the workspace in the left sidebar.
245. Select the workspace in the left sidebar.
246. Select the workspace in the left sidebar.
247. Select the workspace in the left sidebar.
248. Select the workspace in the left sidebar.
249. Select the workspace in the left sidebar.
250. Select the workspace in the left sidebar.
251. Select the workspace in the left sidebar.
252. Select the workspace in the left sidebar.
253. Select the workspace in the left sidebar.
254. Select the workspace in the left sidebar.
255. Select the workspace in the left sidebar.
256. Select the workspace in the left sidebar.
257. Select the workspace in the left sidebar.
258. Select the workspace in the left sidebar.
259. Select the workspace in the left sidebar.
260. Select the workspace in the left sidebar.
261. Select the workspace in the left sidebar.
262. Select the workspace in the left sidebar.
263. Select the workspace in the left sidebar.
264. Select the workspace in the left sidebar.
265. Select the workspace in the left sidebar.
266. Select the workspace in the left sidebar.
267. Select the workspace in the left sidebar.
268. Select the workspace in the left sidebar.
269. Select the workspace in the left sidebar.
270. Select the workspace in the left sidebar.
271. Select the workspace in the left sidebar.
272. Select the workspace in the left sidebar.
273. Select the workspace in the left sidebar.
274. Select the workspace in the left sidebar.
275. Select the workspace in the left sidebar.
276. Select the workspace in the left sidebar.
277. Select the workspace in the left sidebar.
278. Select the workspace in the left sidebar.
279. Select the workspace in the left sidebar.
280. Select the workspace in the left sidebar.
281. Select the workspace in the left sidebar.
282. Select the workspace in the left sidebar.
283. Select the workspace in the left sidebar.
284. Select the workspace in the left sidebar.
285. Select the workspace in the left sidebar.
286. Select the workspace in the left sidebar.
287. Select the workspace in the left sidebar.
288. Select the workspace in the left sidebar.
289. Select the workspace in the left sidebar.
290. Select the workspace in the left sidebar.
291. Select the workspace in the left sidebar.
292. Select the workspace in the left sidebar.
293. Select the workspace in the left sidebar.
294. Select the workspace in the left sidebar.
295. Select the workspace in the left sidebar.
296. Select the workspace in the left sidebar.
297. Select the workspace in the left sidebar.
298. Select the workspace in the left sidebar.
299. Select the workspace in the left sidebar.
300. Select the workspace in the left sidebar.
301. Select the workspace in the left sidebar.
302. Select the workspace in the left sidebar.
303. Select the workspace in the left sidebar.
304. Select the workspace in the left sidebar.
305. Select the workspace in the left sidebar.
306. Select the workspace in the left sidebar.
307. Select the workspace in the left sidebar.
308. Select the workspace in the left sidebar.
309. Select the workspace in the left sidebar.
310. Select the workspace in the left sidebar.
311. Select the workspace in the left sidebar.
312. Select the workspace in the left sidebar.
313. Select the workspace in the left sidebar.
314. Select the workspace in the left sidebar.
315. Select the workspace in the left sidebar.
316. Select the workspace in the left sidebar.
317. Select the workspace in the left sidebar.
318. Select the workspace in the left sidebar.
319. Select the workspace in the left sidebar.
320. Select the workspace in the left sidebar.
321. Select the workspace in the left sidebar.
322. Select the workspace in the left sidebar.
323. Select the workspace in the left sidebar.
324. Select the workspace in the left sidebar.
325. Select the workspace in the left sidebar.
326. Select the workspace in the left sidebar.
327. Select the workspace in the left sidebar.
328. Select the workspace in the left sidebar.
329. Select the workspace in the left sidebar.
330. Select the workspace in the left sidebar.
331. Select the workspace in the left sidebar.
332. Select the workspace in the left sidebar.
333. Select the workspace in the left sidebar.
334. Select the workspace in the left sidebar.
335. Select the workspace in the left sidebar.
336. Select the workspace in the left sidebar.
337. Select the workspace in the left sidebar.
338. Select the workspace in the left sidebar.
339. Select the workspace in the left sidebar.
340. Select the workspace in the left sidebar.
341. Select the workspace in the left sidebar.
342. Select the workspace in the left sidebar.
343. Select the workspace in the left sidebar.
344. Select the workspace in the left sidebar.
345. Select the workspace in the left sidebar.
346. Select the workspace in the left sidebar.
347. Select the workspace in the left sidebar.
348. Select the workspace in the left sidebar.
349. Select the workspace in the left sidebar.
350. Select the workspace in the left sidebar.
351. Select the workspace in the left sidebar.
352. Select the workspace in the left sidebar.
353. Select the workspace in the left sidebar.
354. Select the workspace in the left sidebar.
355. Select the workspace in the left sidebar.
356. Select the workspace in the left sidebar.
357. Select the workspace in the left sidebar.
358. Select the workspace in the left sidebar.
359. Select the workspace in the left sidebar.
360. Select the workspace in the left sidebar.
361. Select the workspace in the left sidebar.
362. Select the workspace in the left sidebar.
363. Select the workspace in the left sidebar.
364. Select the workspace in the left sidebar.
365. Select the workspace in the left sidebar.
366. Select the workspace in the left sidebar.
367. Select the workspace in the left sidebar.
368. Select the workspace in the left sidebar.
369. Select the workspace in the left sidebar.
370. Select the workspace in the left sidebar.
371. Select the workspace in the left sidebar.
372. Select the workspace in the left sidebar.
373. Select the workspace in the left sidebar.
374. Select the workspace in the left sidebar.
375. Select the workspace in the left sidebar.
376. Select the workspace in the left sidebar.
377. Select the workspace in the left sidebar.
378. Select the workspace in the left sidebar.
379. Select the workspace in the left sidebar.
380. Select the workspace in the left sidebar.
3