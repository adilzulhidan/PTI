import multiprocessing
import time
import os


def child_process():
    print(f"Proses anak {os.getpid()} sedang berjalan")
    time.sleep(5)
    print(f"Proses anak {os.getpid()} selesai")


def fork_process():
   
    process = multiprocessing.Process(target=child_process)
    process.start()  
    print(f"Proses induk {os.getpid()} menunggu proses anak {process.pid}")
    process.join()  
    print(f"Proses anak {process.pid} selesai")


if __name__ == "__main__":
    fork_process()
