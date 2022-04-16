import subprocess
import sys
import os


def open_file(filename):
    try:
        os.startfile(filename)
    except:
        subprocess.Popen(['xdg-open', filename])


def resource_path(relative_path):
    """
    获取资源的绝对路径
    :param relative_path: 资源相对路径
    :return:
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
