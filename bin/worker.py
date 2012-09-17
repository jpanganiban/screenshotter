#!/usr/bin/env python

from screenshooter import config, utils
from screenshooter import custom_gearman as gearman


worker = gearman.GearmanWorker(config.GEARMAN_HOSTS)


def take_screenshot(gm_worker, gm_job):
    utils.take_screenshot(gm_job.data['url'], gm_job.unique)
    return gm_job.data


if __name__ == '__main__':
    worker.register_task('screenshot', take_screenshot)
    worker.work()
