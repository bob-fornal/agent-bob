# Import Ordering Rules

## Alphabetization
- All import statements **must** be sorted alphabetically by module specifier (the string in quotes).
- Sorting is **case-insensitive**; uppercase and lowercase letters are treated equally.

**Wrong:**
```ts
import { z } from 'zod';
import { Router } from 'express';
import fs from 'fs';
```

**Correct:**
```ts
import fs from 'fs';
import { Router } from 'express';
import { z } from 'zod';
```

## Import Group Order
Separate import groups with a **single blank line** in this order:

1. Node.js built-in modules (e.g., `fs`, `path`, `crypto`)
2. External npm packages
3. Internal absolute path aliases (e.g., `@/utils`, `~/config`)
4. Relative imports (`../`, `./`)

**Example:**
```ts
import path from 'path';

import { Hono } from 'hono';
import { z } from 'zod';

import { config } from '@/config';

import { helper } from '../utils/helper';
import { localFn } from './local';
```

## Named Import Sorting
- Named imports within a single `import { ... }` statement must also be alphabetized.

**Wrong:**
```ts
import { useState, useEffect, useRef } from 'react';
```

**Correct:**
```ts
import { useEffect, useRef, useState } from 'react';
```

## Type-Only Imports
- Use `import type { ... }` for type-only imports to avoid runtime overhead.
- `import type` statements follow the same alphabetization rules within their group.
- Place `import type` from the same module directly after the corresponding value import.

**Example:**
```ts
import express from 'express';
import type { Request, Response } from 'express';
```

## Side-Effect Imports
- Side-effect imports (`import 'some-polyfill'`) go first, before all other groups, and are not alphabetized with regular imports.

## ESLint Rules That Enforce This
- `import/order` with `alphabetize: { order: "asc", caseInsensitive: true }` (eslint-plugin-import)
- `sort-imports` with `ignoreDeclarationSort: true, ignoreMemberSort: false`
- `@typescript-eslint/consistent-type-imports`
