from screenshooter import config
import subprocess
import os


def save_path(filename, filepath='/tmp/'):
    filename = "%s.jpg" % filename
    savepath = os.path.join(filepath, filename)
    return savepath


def take_screenshot(url, savepath):
    data = subprocess.call([config.PHANTOM_BIN_PATH, 'shooter.js', url, savepath])
    return data
