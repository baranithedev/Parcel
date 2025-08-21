from shutil import get_terminal_size 
from platform import system 
from os import path 

termsize:int = get_terminal_size().columns // 2

class Essential:
    def format_size(self, size_bytes):
        for unit in ['B','KB','MB','GB','TB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024

    def file_details(self, filename, filesize):
        return f"""Filename: {filename}
Filesize: {self.format_size(filesize)}
"""

    def createparcelfolder(self, folder_name: str):
        if system().lower() == "linux":
            folder_path = path.join(path.expanduser("~"), folder_name)
            possible_path = ["/sdcard/", "/storage/emulated/0/"]
            for pp in possible_path:
                if path.exists(pp):
                    return "/storage/emulated/0/"+folder_name
            return folder_path
        else:
            return path.join(path.expanduser("~"), folder_name)
