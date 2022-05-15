import time
import os
import shutil

def main():
    deletedFoldersCount = 0
    deletedFilesCount = 0
    path = "/pathtodelete"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFoldersCount += 1
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFoldersCount += 1
    else:
        print("Path is not found")
        deletedFoldersCount += 1
    print("Total folders deleted: {deletedFoldersCount}")

main()