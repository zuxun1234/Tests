import psutil
import winreg
import os
import time

# 定义不需要的进程名称
UNWANTED_PROCESSES = [
    "example.exe",  # 替换为不需要的进程名称
    "another_example.exe"
]

# 定义不需要的启动项名称
UNWANTED_STARTUP_ITEMS = [
    "ExampleApp",  # 替换为不需要的启动项名称
    "AnotherApp"
]

# 日志文件路径
LOG_FILE = "cleanup_log.txt"

def log(message):
    """记录日志"""
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)

def kill_unwanted_processes():
    """关闭不必要的进程"""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in UNWANTED_PROCESSES:
                log(f"关闭进程: {proc.info['name']} (PID: {proc.info['pid']})")
                proc.terminate()
                proc.wait(timeout=5)  # 等待进程关闭
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
            log(f"无法关闭进程 {proc.info['name']} (PID: {proc.info['pid']}) - {e}")

def remove_unwanted_startup_items():
    """移除不必要的启动项"""
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ) as key:
            for i in range(winreg.QueryInfoKey(key)[1]):
                name, value, _ = winreg.EnumValue(key, i)
                if name in UNWANTED_STARTUP_ITEMS:
                    log(f"移除启动项: {name}")
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE) as key_write:
                        winreg.DeleteValue(key_write, name)
    except Exception as e:
        log(f"无法移除启动项 - {e}")

def main():
    log("开始清理不必要的进程和启动项...")
    kill_unwanted_processes()
    remove_unwanted_startup_items()
    log("清理完成。")

if __name__ == "__main__":
    main()