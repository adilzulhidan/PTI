class FileSystem:
    def __init__(self) -> None:
        self.file = {}

    def create_file(self, filename, content):
        if filename in self.file:
            print(f"File {filename} sudah ada")
        else:
            self.file[filename] = content
            print(f"File {filename} dibuat")

    def read_file(self, filename):
        if filename in self.file:
            print(f"Isi dari {filename}: {self.file[filename]}")
        else:
            print(f"File {filename} tidak ada")


fs = FileSystem()
fs.create_file("file1.txt", "hello world!")
fs.read_file("file1.txt")
