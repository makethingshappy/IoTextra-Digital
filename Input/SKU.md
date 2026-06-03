# SKU — IoTextra Input

```
040101vvvscc
```

| Field | Description |
|---|---|
| `040101` | Product code — IoTextra Input |
| `vvv` | Version (e.g. 302 = version 3.02) |
| `s` | Signal type |
| `cc` | Communication |

**Signal type (s):**

| Value | Description |
|---|---|
| 0 | Unipolar |
| 1 | Bipolar |

**Communication (cc):**

| Value | Description |
|---|---|
| 10 | HOST-10 connector |
| 09 | HOST-12 connector |
| 11 | HOST-12 connector and two I²C connectors |
