# Code Style

## Semicolons
- Always use semicolons at the end of statements. Do not rely on ASI (Automatic Semicolon Insertion).

## Quotes
- Use **single quotes** for TypeScript string literals.
- Use **backticks** for template literals when embedding expressions or writing multi-line strings.
- Use **double quotes** in JSON files (required by the JSON specification).

## Trailing Commas
- Always include trailing commas in multi-line TypeScript constructs: arrays, objects, function parameters, generic type argument lists, and destructuring patterns.
- Prettier setting: `"trailingComma": "all"`

**Example:**
```ts
const config = {
  host: 'localhost',
  port: 3000,
  debug: true,
};

function create(
  name: string,
  options: Options,
  callback: Callback,
): void {}
```

## Line Length
- Maximum line length: **100 characters**.
- Exception: import paths and URL string literals should not be broken mid-string — allow these to exceed the limit.

## Blank Lines
- One blank line between top-level declarations (functions, classes, constants).
- No blank lines at the start or end of a block body.
- No more than two consecutive blank lines anywhere in a file.

## Braces & Blocks
- Always use braces `{}` for `if`, `else`, `for`, `while`, `do`, and `switch` bodies — even for single-line bodies.

**Wrong:**
```ts
if (isValid) doThing();
```

**Correct:**
```ts
if (isValid) {
  doThing();
}
```

## Arrow Functions
- Use arrow functions for callbacks and inline expressions.
- Always include parentheses around parameters, even for a single parameter.

**Wrong:**
```ts
const doubled = numbers.map(n => n * 2);
```

**Correct:**
```ts
const doubled = numbers.map((n) => n * 2);
```

## Template Literals
- Prefer template literals over string concatenation.

**Wrong:**
```ts
const msg = 'Hello, ' + name + '!';
```

**Correct:**
```ts
const msg = `Hello, ${name}!`;
```

## Object & Array Spread
- Prefer object spread (`{ ...a, ...b }`) over `Object.assign()`.
- Prefer array spread (`[...a, ...b]`) over `Array.prototype.concat()`.

## Optional Chaining & Nullish Coalescing
- Use optional chaining (`?.`) instead of nested `&&` null checks.
- Use nullish coalescing (`??`) instead of `||` when a falsy-but-defined value (e.g., `0`, `''`) is valid.

**Wrong:**
```ts
const name = user && user.profile && user.profile.name;
const display = name || 'Anonymous';
```

**Correct:**
```ts
const name = user?.profile?.name;
const display = name ?? 'Anonymous';
```

## Comments
- Use `//` for single-line comments and `/* */` for multi-line comments.
- Use `/** */` JSDoc-style comments for all exported functions, classes, and types.
- Do not leave commented-out dead code in committed files.
