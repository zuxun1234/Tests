import os
import time
import psutil  # 需要安装 psutil 模块

def memory_stress_test(target_percentage=80, duration=2):
    """
    快速占用内存到目标百分比，并保持指定时间后释放。

    参数:
        target_percentage (float): 目标内存占用百分比（例如80）。
        duration (int): 保持目标内存占用的时间（秒）。
    """
    # 获取系统总内存
    total_memory = psutil.virtual_memory().total  # 总内存大小（字节）
    target_memory = int(total_memory * target_percentage / 100)  # 目标内存大小
    current_memory = 0

    print(f"开始内存压力测试，目标占用：{target_percentage}%")
    print(f"总内存：{total_memory / (1024 ** 3):.2f} GB")
    print(f"目标内存：{target_memory / (1024 ** 3):.2f} GB")

    data = []
    try:
        # 快速分配内存
        while current_memory < target_memory:
            chunk = bytearray(1024 * 1024 * 10)  # 每次分配10MB
            data.append(chunk)
            current_memory += len(chunk)
            if current_memory >= target_memory:
                break

        print(f"已达到目标内存占用：{current_memory / (1024 ** 3):.2f} GB")
        print(f"保持该内存占用 {duration} 秒...")
        time.sleep(duration)  # 保持目标内存占用
    except MemoryError:
        print("内存不足，测试结束。")
    finally:
        del data  # 释放内存
        print("测试完成，内存已释放。")

if __name__ == "__main__":
    memory_stress_test(target_percentage=80, duration=2)