from screenshooter import config
import subprocess
import os


def save_path(filename, filepath='/tmp/'):
    filename = "%s.jpg" % filename
    savepath = os.path.join(filepath, filename)
    return savepath


def take_screenshot(url, filename, savepath):
    subprocess.call([config.PHANTOM_BIN_PATH, 'shooter.js', url, savepath])
    return {'url': url, 'filename': savepath}
