from screenshooter import config
import subprocess
import os


def take_screenshot(url, filename, filepath='/tmp/'):
    filename = "%s.jpg" % filename
    savepath = os.path.join(filepath, filename)
    return subprocess.call([config.PHANTOM_BIN_PATH, 'shooter.js', url, savepath])
