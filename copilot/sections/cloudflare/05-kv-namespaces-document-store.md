# Key-Value (KV) Namespaces as a Document Store

## Simple Document Database Pattern
* **Document Storage:** KV Namespaces can be treated as a lightweight document database. Structure the key to represent the collection and document ID (e.g., `user:12345` or `config:app_settings`).
* **JSON Serialization:** Unlike Durable Objects, KV stores data as strings, ArrayBuffers, or Streams. When saving a document, you must serialize the JavaScript object to a JSON string using `JSON.stringify()`.
* **JSON Deserialization:** When fetching a document, specify the type as `"json"` to have Cloudflare automatically parse it (`await env.MY_KV.get('user:12345', { type: 'json' })`).
* **Eventual Consistency:** Be aware that KV data is eventually consistent across the global edge network. Writes may take up to 60 seconds to propagate to all edge locations. Avoid using KV for highly transactional data where strong consistency is immediately required (use D1 or Durable Objects instead).
* **No Metadata Usage:** Do not rely on KV metadata for this pattern due to strict size limits. Keep all required fields in the document value itself and design keys for lookup (e.g., `user:12345`, `user_by_email:alice@example.com`).
* **Query Pattern:** Use `list({ prefix: 'user:' })` for collection-style scans, and create explicit secondary index keys when you need alternate lookups.
