import multiprocessing
import time
import os

def cpu_intensive_task():
    """
    一个简单的CPU密集型任务，通过计算密集型操作占用CPU。
    """
    while True:
        # 使用一个简单的计算密集型操作
        _ = [x * x for x in range(1000000)]

def main(target_load=70, duration=2):
    """
    主函数，用于启动多个进程以将CPU占用率提升到目标值。

    参数:
        target_load (int): 目标CPU占用率（百分比）。
        duration (int): 持续时间（秒）。
    """
    # 获取系统CPU核心数
    num_cores = os.cpu_count()
    print(f"系统CPU核心数: {num_cores}")
    print(f"目标CPU占用率: {target_load}%")
    print(f"持续时间: {duration}秒")

    # 计算需要启动的进程数量
    num_processes = int((target_load / 100) * num_cores)
    print(f"启动进程数: {num_processes}")

    processes = []

    # 创建并启动进程
    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_intensive_task)
        processes.append(process)
        process.start()

    print("CPU占用率已提升到目标值，保持中...")
    time.sleep(duration)

    # 停止所有进程
    for process in processes:
        process.terminate()
        process.join()

    print("CPU占用测试完成，进程已停止。")

if __name__ == "__main__":
    main(target_load=70, duration=2)