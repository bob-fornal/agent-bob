# TypeScript-Specific Rules

## Strict Mode
- Always enable `"strict": true` in `tsconfig.json`. This activates:
  - `noImplicitAny`
  - `strictNullChecks`
  - `strictFunctionTypes`
  - `strictPropertyInitialization`
  - `strictBindCallApply`
- Also enable `"noUncheckedIndexedAccess": true` and `"noImplicitOverride": true` for additional safety.

## No Explicit `any`
- Never use the `any` type when it can be avoided.
- Use `unknown` for genuinely unknown types and narrow with type guards or `instanceof` checks.
- If a third-party library forces `any`, isolate it behind a typed wrapper.
- ESLint rule: `@typescript-eslint/no-explicit-any: "error"`

## Explicit Return Types
- All exported and public functions/methods **must** declare an explicit return type.
- Private/internal helpers are encouraged but not required to have explicit return types.

**Wrong:**
```ts
export function getUser(id: string) {
  return db.find(id);
}
```

**Correct:**
```ts
export function getUser(id: string): Promise<User | null> {
  return db.find(id);
}
```

## Naming Conventions

| Entity               | Convention          | Example                   |
|----------------------|---------------------|---------------------------|
| Variables & functions | `camelCase`        | `getUserById`             |
| Classes              | `PascalCase`        | `UserService`             |
| Interfaces           | `PascalCase`        | `RequestPayload`          |
| Type aliases         | `PascalCase`        | `ApiResponse`             |
| Enums                | `PascalCase`        | `HttpStatus`              |
| Enum members         | `UPPER_SNAKE_CASE`  | `NOT_FOUND`               |
| Top-level constants  | `UPPER_SNAKE_CASE`  | `MAX_RETRIES`             |
| Boolean variables    | Prefix `is/has/can` | `isValid`, `hasPermission`|
| Generic type params  | Single uppercase or descriptive PascalCase | `T`, `TResponse` |

## Interfaces vs. Type Aliases
- Prefer `interface` for object shapes that may be extended or implemented by a class.
- Use `type` for union types, intersection types, tuple types, and mapped types.

## Unused Variables & Imports
- No unused imports or variables are permitted.
- Prefix intentionally unused function parameters with `_` (e.g., `_event`, `_ctx`).
- ESLint rules:
  - `@typescript-eslint/no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]`

## `const` Over `let`
- Default to `const`. Only use `let` when a variable must be reassigned.
- Never use `var`.

## Non-Null Assertion Operator
- Avoid the `!` non-null assertion operator (`value!`).
- Prefer explicit null checks, optional chaining (`?.`), or nullish coalescing (`??`).

## Equality
- Always use strict equality `===` and `!==`. Never use `==` or `!=`.
- ESLint rule: `eqeqeq: ["error", "always"]`

## Enums
- Prefer `const enum` for compile-time-only enumerations to avoid runtime overhead.
- Prefer string-valued enums over numeric enums for debuggability.

## `as` Type Assertions
- Minimize `as` type assertions. If you must use one, add a comment explaining why the type system cannot infer it.
- Never use `as any` as a shortcut — fix the types instead.
