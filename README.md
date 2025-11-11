[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2RrJif8H)
# HW04 — Event Log Deduplicator (Custom Set via Chaining)

**Story intro (new theme):**  
You manage a **system event log**. Each event has a unique **event id** string. You must **deduplicate** repeated event ids quickly and support **add**, **contains**, and **remove**.

**Today’s topic focus:** Build a **hash-set** with chaining (no values, just keys).

---

## Technical description
- **Goal:** Implement a small **set** using chaining.
- **Functions to write in `main.py`:**
  - `make_set(m)` → new table with `m` buckets.
  - `add(s, key)` → return `True` if added; `False` if already present.
  - `contains(s, key)` → `True/False`.
  - `remove(s, key)` → `True` if removed; `False` if not present.
  - `size(s)` → number of keys stored.
- **Inputs/Outputs:** Keys are strings (event ids). No values.
- **Constraints:** `2 ≤ m ≤ 101`. No external libs.
- **Expected complexity:** Average **O(1)** for operations at moderate load.

---

## ESL scaffold — The 8 Steps
**Minimal prompts (hw04):**  
- **Read:** We store unique ids.  
- **I/O:** Inputs: table and key; Outputs: booleans or counts.  
- **Students drive Steps 4–8.**

---

## Hints
- Reuse the same `hash_basic` style from HW01 or write a simple one.
- For `add`, scan the bucket; if found, return `False`; else append.
- For `remove`, find index in bucket; `pop` it; return `True`.

---

## How to run tests locally

```python -m pytest -q```


---

## FAQ
**Q1. Do we store values?** No, it is a set.  
**Q2. Duplicates?** `add` returns `False` and does not change size.  
**Q3. Complexity?** Aim for average **O(1)**.  
**Q4. Mutate inputs?** Do not modify the key string.  
**Q5. Bucket order?** Not graded.  
**Q6. Grading?** Pytest autograder.  
**Q7. Failures?** Read message; check bucket scanning and size updates.