class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                del bucket[i]
                return True
        return False

# Ejemplo de uso
ht = HashTable(10)
ht.insert("manzana", 1)
ht.insert("banana", 2)
ht.insert("cereza", 3)

print("Buscar 'manzana':", ht.search("manzana"))
print("Buscar 'banana':", ht.search("banana"))
print("Buscar 'cereza':", ht.search("cereza"))
print("Buscar 'durazno':", ht.search("durazno"))

ht.delete("banana")
print("Buscar 'banana' después de eliminar:", ht.search("banana"))
