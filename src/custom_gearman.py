import gearman
import json


class JSONEncoder(gearman.DataEncoder):
    """Json encoder to make things more convinient.
    **As specified by the docs."""

    @classmethod
    def encode(cls, encodable_object):
        return json.dumps(encodable_object)

    @classmethod
    def decode(cls, decodable_string):
        return json.loads(decodable_string)


class GearmanJob(gearman.job.GearmanJob):
    """Our custom Gearman Job class"""
    pass


class GearmanWorker(gearman.GearmanWorker):
    """Our custom Gearman Worker class"""

    data_encoder = JSONEncoder
    job_class = GearmanJob


class GearmanClient(gearman.GearmanClient):
    """Our custom Gearman Client class"""

    data_encoder = JSONEncoder
    job_class = GearmanJob
