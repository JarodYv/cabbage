import os
import re
import platform
import threading
from playsound import playsound
import uiautomator2 as u2
from file_utils import resource_path
import time


def connect_phone(device_name: str) -> u2.Device:
    """ 连接手机

    :param device_name:
    :return:
    """
    d = u2.connect(device_name)
    if not d.uiautomator.start():
        # 启动uiautomator服务
        print("start uiautomator")
        d.uiautomator.start()
        time.sleep(2)
    return d


def is_mac() -> bool:
    """ 判断当前操作系统是否是Mac

    :return:
    """
    system = platform.system()
    if system == "Windows":
        print("当前系统是Windows")
        return False
    else:
        print("当前系统是Mac")
        return True


def get_device_list() -> list[dict]:
    # root_path = os.getcwd()
    if is_mac():
        adb_path = resource_path(f"sources/mac_tools/adb")
    else:
        adb_path = resource_path(f"sources/win_tools/adb")
        # start_server = os.path.join(root_path, "sources", "win_tools", "adb.exe start-server")
        # cmd = os.path.join(root_path, "sources", "win_tools", "adb.exe devices -l")
    start_server = adb_path + " start-server"
    cmd = adb_path + " devices -l"
    os.popen(start_server)
    res = os.popen(cmd).read()
    print(f"adb 命令结果是:\n{res}")
    list_phone = [i for i in res.split("\n") if i]
    phone_infos = []
    for phone in list_phone[1:]:
        if phone:
            info = re.split(r"\s+", phone)
            print(info)
            device_id = info[0]
            device_info = {"device_id": device_id}
            for i in info[2:]:
                if ":" in i:
                    k = i.split(":")
                    device_info[k[0]] = k[1]
            phone_infos.append(device_info)
    print(f"得到的设备列表是:{phone_infos}")
    return phone_infos


def play_voice(content: str):
    """
    播放声音提醒
    """
    # root_path = os.getcwd()
    # video_path = os.path.join(root_path, "sources", "videos", f"{content}.mp3")
    video_path = resource_path(f"sources/videos/{content}.mp3")
    threading.Thread(target=playsound, args=(video_path,)).start()
