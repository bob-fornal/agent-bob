# JSON Formatting Rules

## One Key/Value Per Line
- Every key/value pair in a JSON object **must** appear on its own line.
- No inline/compressed objects (except genuinely empty objects `{}`).

**Wrong:**
```json
{ "name": "my-app", "version": "1.0.0", "private": true }
```

**Correct:**
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "private": true
}
```

## Indentation
- Use **2 spaces** for indentation in all JSON files.
- Never use tabs in JSON files.

## Arrays
- When an array has more than one element, each element must appear on its own line.

**Wrong:**
```json
{
  "keywords": ["typescript", "linting", "eslint"]
}
```

**Correct:**
```json
{
  "keywords": [
    "eslint",
    "linting",
    "typescript"
  ]
}
```

- Single-element arrays may remain on one line: `"scripts": ["build"]`

## Trailing Commas
- JSON does **not** allow trailing commas. Never add a trailing comma after the last key/value pair or array element.

## Nesting
- Nested objects follow the same one-key/value-per-line rule.

**Wrong:**
```json
{
  "compilerOptions": { "strict": true, "target": "ES2022" }
}
```

**Correct:**
```json
{
  "compilerOptions": {
    "strict": true,
    "target": "ES2022"
  }
}
```

## Key Ordering (Recommended)
- In `package.json`, follow the conventional key order: `name`, `version`, `description`, `main`/`module`, `types`, `scripts`, `dependencies`, `devDependencies`, `peerDependencies`.
- In `tsconfig.json`, group `compilerOptions` keys by category: target/module settings first, then strictness flags, then paths/output.

## Tooling
- Use **Prettier** with `"printWidth": 80` to auto-format JSON files.
- Validate JSON syntax with `jsonlint` or via IDE schema validation (e.g., the `json.schemas` VS Code setting).
