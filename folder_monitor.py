import os
import time

# Tentukan folder yang ingin dipantau
folder_path = "C:/Users/admin/Documents"
file_name = "example.txt"

def check_folder_status():
    """Memeriksa apakah folder dan file ada"""
    if os.path.exists(folder_path):
        print(f"[INFO] Folder '{folder_path}' ditemukan.")
        
        # Memeriksa apakah file tertentu ada di folder tersebut
        if os.path.isfile(os.path.join(folder_path, file_name)):
            print(f"[INFO] File '{file_name}' ditemukan di folder.")
        else:
            print(f"[WARNING] File '{file_name}' TIDAK ditemukan di folder.")
    else:
        print(f"[ERROR] Folder '{folder_path}' TIDAK ditemukan!")

# Memeriksa status folder dan file setiap 10 detik
if __name__ == "__main__":
    while True:
        check_folder_status()
        time.sleep(10)  # Cek setiap 10 detik
