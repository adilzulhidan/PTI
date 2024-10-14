class Memory:
    def __init__(self, size):
        self.size = size
        self.free = size
        self.allocated = {}

    def allocate(self, process_id, size):
        if size <= self.free:
            self.allocated[process_id] = size
            self.free -= size
            print(f"Memori {size} dialokasikan untuk proses {process_id}")
        else:
            print(f"Memori tidak cukup untuk proses {process_id}")

    def deallocate(self, process_id):
        if process_id in self.allocated:
            size = self.allocated.pop(process_id)
            self.free += size
            print(f"Memori {size} dibebaskan dari proses {process_id}")

# Contoh Penggunaan
memory = Memory(1024)  # 1024 MB memori
memory.allocate("P1", 200)
memory.allocate("P2", 500)
memory.deallocate("P1")
