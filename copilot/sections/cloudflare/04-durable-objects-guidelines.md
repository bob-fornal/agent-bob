# Durable Objects Guidelines

## State Management & JSON
* **JSON Serialization:** When storing complex objects or arrays in Durable Object storage (`ctx.storage.put`), you do not need to manually `JSON.stringify()` or `JSON.parse()`. Cloudflare's Durable Object storage natively leverages structured cloning, allowing you to directly store and retrieve native JavaScript objects (including JSON-like structures).
* **In-Memory References:** You can maintain references to JSON objects in the Durable Object's in-memory state (e.g., as class properties). However, ensure you synchronize critical state changes to persistent storage (`ctx.storage.put`) to avoid data loss if the Durable Object is evicted from memory or restarts.
* **Concurrency & Mutability:** When modifying in-memory JSON objects or retrieving them from storage, remember that returning an object from state might return a reference. If mutating these JSON objects, ensure you update the storage explicitly to persist the changes. Use `ctx.blockConcurrencyWhile()` if you need to ensure exclusive access to state during complex memory updates and storage syncs.
