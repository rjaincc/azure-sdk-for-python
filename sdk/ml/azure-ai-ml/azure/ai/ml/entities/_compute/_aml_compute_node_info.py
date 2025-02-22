# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import Dict

from azure.ai.ml._restclient.v2022_10_01_preview.models import AmlComputeNodeInformation
from azure.ai.ml._schema.compute.aml_compute_node_info import AmlComputeNodeInfoSchema
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY


class AmlComputeNodeInfo:
    def __init__(self):
        """Compute node information related to a AmlCompute Variables are only
        populated by the server, and will be ignored when sending a request."""

        self.node_id = None
        self.private_ip_address = None
        self.port = None
        self.node_state = None
        self.run_id = None

    @property
    def current_job_name(self) -> str:
        return self.run_id

    @current_job_name.setter
    def current_job_name(self, value: str) -> None:
        self.run_id = value

    @classmethod
    def _from_rest_object(cls, rest_obj: AmlComputeNodeInformation) -> "AmlComputeNodeInfo":
        result = cls()
        result.__dict__.update(rest_obj.as_dict())
        return result

    def _to_dict(self) -> Dict:
        # pylint: disable=no-member
        return AmlComputeNodeInfoSchema(context={BASE_PATH_CONTEXT_KEY: "./"}).dump(self)
