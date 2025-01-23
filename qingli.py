import os
import shutil
import ctypes
import subprocess
from pathlib import Path

def is_admin():
    """
    检查是否以管理员权限运行
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clear_temp_files():
    """
    清理系统临时文件
    """
    print("清理系统临时文件...")
    temp_folders = [
        r"C:\Windows\Temp",
        r"C:\Users\{}\AppData\Local\Temp".format(os.getlogin()),
        r"C:\Users\{}\AppData\Local\Microsoft\Windows\INetCache".format(os.getlogin())
    ]
    for folder in temp_folders:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder, topdown=False):
                for name in files:
                    file_path = os.path.join(root, name)
                    try:
                        os.remove(file_path)
                        print(f"已删除文件：{file_path}")
                    except PermissionError:
                        print(f"删除文件时出错：{file_path}，错误：权限被拒绝。")
                    except OSError as e:
                        print(f"删除文件时出错：{file_path}，错误：{e}")
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    try:
                        if not os.path.islink(dir_path):  # 检查是否为符号链接
                            shutil.rmtree(dir_path)
                            print(f"已删除文件夹：{dir_path}")
                    except PermissionError:
                        print(f"删除文件夹时出错：{dir_path}，错误：权限被拒绝。")
                    except OSError as e:
                        print(f"删除文件夹时出错：{dir_path}，错误：{e}")

def empty_recycle_bin():
    """
    清空回收站
    """
    print("清空回收站...")
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)
        print("回收站已清空")
    except Exception as e:
        print(f"清空回收站时出错：{e}")

def clear_system_cache():
    """
    清理系统缓存
    """
    print("清理系统缓存...")
    try:
        subprocess.run("DISM.exe /Online /Cleanup-image /StartComponentCleanup", shell=True)
        print("系统缓存清理完成")
    except Exception as e:
        print(f"清理系统缓存时出错：{e}")

def main():
    if not is_admin():
        print("请以管理员权限运行此脚本！")
        return

    print("开始清理C盘...")
    clear_temp_files()
    empty_recycle_bin()
    clear_system_cache()
    print("清理完成！")

if __name__ == "__main__":
    main()