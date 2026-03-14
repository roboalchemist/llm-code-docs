# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Promissory.md

# [Promissory](https://bryntum.com/docs/gantt/api/Core/helper/util/Promissory)

Encapsulates a Promise and provides `resolve()` and `reject()` methods.

For example:

```
 load() {
     this.loading = new Promissory();
     this.store.load();

     return this.loading.promise;
 }

 onStoreLoad(store, err) {
     if (err) {
         this.loading.resolve(this);
     }
     else {
         this.loading.reject(err);
     }
 }

```
