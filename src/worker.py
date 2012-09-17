import config
import custom_gearman as gearman


worker = gearman.GearmanWorker(config.GEARMAN_HOSTS)


def take_screenshot(gm_worker, gm_job):
    print gm_worker
    print gm_job.data
    return gm_job.data


if __name__ == '__main__':
    worker.register_task('screenshot', take_screenshot)
    worker.work()
