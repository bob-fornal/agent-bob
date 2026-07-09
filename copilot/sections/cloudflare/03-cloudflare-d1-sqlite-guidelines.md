# Cloudflare D1 (SQLite) Guidelines

## D1 Query Mechanics in Workers
* **Prepared Statements:** Always use prepared statements via `env.DB.prepare(...).bind(...)` to prevent SQL injection. NEVER concatenate strings into SQL queries.
* **Execution Methods:** Choose the correct execution method based on the use case:
  * `.first()`: Retrieve a single row or single value.
  * `.all()`: Retrieve an array of all matching rows.
  * `.run()`: For execution queries (INSERT, UPDATE, DELETE) where results aren't returned.
  * `.batch()`: For executing multiple statements efficiently in a single network roundtrip.

## SQL Creation Scripts (DDL)
* **Dialect:** The target SQL dialect is SQLite (specifically the version used by D1).
* **Data Types:** Use SQLite standard types: `TEXT`, `INTEGER`, `REAL`, `BLOB`. (e.g., Booleans should be `INTEGER` 0 or 1, Dates should be `TEXT` ISO8601 strings or `INTEGER` unix timestamps).
* **Primary Keys:** Clearly define `PRIMARY KEY`. For auto-incrementing IDs, use `INTEGER PRIMARY KEY AUTOINCREMENT`. For UUIDs, specify as `TEXT PRIMARY KEY`.
* **Idempotency:** DDL scripts should be rerunnable without errors. Rely on `CREATE TABLE IF NOT EXISTS` and `DROP TABLE IF EXISTS`.
* **Default Values & Constraints:** Use `NOT NULL`, `UNIQUE`, and `DEFAULT` constraints appropriately to enforce schema integrity.
* **Foreign Keys:** While D1 conceptually supports underlying SQLite features, be mindful of complex foreign key cascades and test thoroughly, as D1's distributed nature has had specific considerations with strict referential integrity in the past. Use `FOREIGN KEY (column) REFERENCES table(column)`.
