EMPTY = object()
DELETED = object()

def make_set(m=8):
    """Create a new hash set with initial capacity m."""
    return {"table": [EMPTY]*m, "count": 0}

def _hash(key, m):
    return hash(key) % m

def _resize(s):
    """Resize the table when load factor exceeds 0.7"""
    old_table = s["table"]
    new_size = len(old_table) * 2
    s["table"] = [EMPTY] * new_size
    s["count"] = 0
    for entry in old_table:
        if entry is not EMPTY and entry is not DELETED:
            add(s, entry)

def add(s, key):
    table = s["table"]
    m = len(table)
    if s["count"] / m >= 0.7:
        _resize(s)
        table = s["table"]
        m = len(table)

    index = _hash(key, m)
    first_deleted = None

    for i in range(m):
        probe = (index + i) % m
        if table[probe] is EMPTY:
            if first_deleted is not None:
                table[first_deleted] = key
            else:
                table[probe] = key
            s["count"] += 1
            return True
        elif table[probe] is DELETED:
            if first_deleted is None:
                first_deleted = probe
        elif table[probe] == key:
            return False  # duplicate
    if first_deleted is not None:
        table[first_deleted] = key
        s["count"] += 1
        return True
    return False  # full (should rarely happen with resizing)

def contains(s, key):
    table = s["table"]
    m = len(table)
    index = _hash(key, m)
    for i in range(m):
        probe = (index + i) % m
        if table[probe] is EMPTY:
            return False
        elif table[probe] is DELETED:
            continue
        elif table[probe] == key:
            return True
    return False

def remove(s, key):
    table = s["table"]
    m = len(table)
    index = _hash(key, m)
    for i in range(m):
        probe = (index + i) % m
        if table[probe] is EMPTY:
            return False
        elif table[probe] is DELETED:
            continue
        elif table[probe] == key:
            table[probe] = DELETED
            s["count"] -= 1
            return True
    return False

def size(s):
    return s["count"]
