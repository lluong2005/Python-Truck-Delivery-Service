class HashTable:
    def __init__(self, initial_capacity=20):
        self.buckets = []
        for i in range(initial_capacity):
            self.buckets.append([])

    def insert(self, key, value):
        # Inserts or updates a key-value pair in the hash map
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def lookup(self, key):
        # Looks up a value associated with the given key in the hash map
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        # Removes the key-value pair associated with the given key from the hash map
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key not found: {key}")
