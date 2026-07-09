# Cloudflare Worker API Guidelines

## Format & Syntax
* **ES Modules format:** Always use ES Modules syntax (`export default { fetch(request, env, ctx) { ... } }`) instead of the older Service Worker syntax (`addEventListener`).
* **Environment Variables & Bindings:** Access secrets and resources (like D1 bindings, KV namespaces) exclusively through the `env` object passed to the `fetch` handler.
* **Routing:** Use URL pattern matching with the `URL` API (`new URL(request.url).pathname`) and standard `switch` or `if/else` statements for routing. Do not use external router libraries.
* **CORS:** Ensure endpoints handling cross-origin requests implement robust CORS headers, including handling preflight `OPTIONS` requests.
* **Response Generation:** Always return standard web APIs `Response` objects (`new Response(...)`, `Response.json(...)`). Use proper status codes (e.g., 200 OK, 201 Created, 400 Bad Request, 404 Not Found, 500 Internal Server Error).
* **Error Handling:** Wrap execution in `try/catch` blocks. Never expose internal stack traces or sensitive database errors directly in the unauthenticated API responses. Log errors appropriately.
* **TypeScript:** Prefer generating TypeScript code (`index.ts`) for Workers to leverage strict typing for the `env` bindings (using `interface Env { DB: D1Database }`).

## Performance & Security
* Validate all incoming request payloads before processing.
* Avoid blocking the event loop; make sure all external calls via `fetch()` and database queries are properly `await`ed.
* Use `ctx.waitUntil()` for background tasks like logging or analytics that don't need to block the response to the user.
