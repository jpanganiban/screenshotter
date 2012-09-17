#!/usr/bin/env python

from screenshooter import config, utils
from screenshooter import custom_gearman as gearman


worker = gearman.GearmanWorker(config.GEARMAN_HOSTS)


def take_screenshot(gm_worker, gm_job):
    savepath = utils.save_path(gm_job.unique)
    print savepath
    data = utils.take_screenshot(gm_job.data['url'], savepath)
    print data
    return data

if __name__ == '__main__':
    worker.register_task('screenshot', take_screenshot)
    worker.work()
