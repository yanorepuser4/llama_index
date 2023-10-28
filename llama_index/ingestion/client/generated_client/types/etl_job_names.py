# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EtlJobNames(str, enum.Enum):
    """
    Enum for executable pipeline job names.
    """

    LOAD_DOCUMENTS_JOB = "load_documents_job"
    RUN_TRANSFORM_JOB = "run_transform_job"

    def visit(
        self,
        load_documents_job: typing.Callable[[], T_Result],
        run_transform_job: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EtlJobNames.LOAD_DOCUMENTS_JOB:
            return load_documents_job()
        if self is EtlJobNames.RUN_TRANSFORM_JOB:
            return run_transform_job()
        return None
