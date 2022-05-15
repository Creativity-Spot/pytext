#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from accelerators.pytorch.lib.quantize import quantize_statically

from .new_task import _NewTask, NewTask
from .serialize import get_latest_checkpoint_path, load, save
from .task import create_task, Task_Deprecated, TaskBase


__all__ = [
    "_NewTask",
    "NewTask",
    "Task_Deprecated",
    "TaskBase",
    "save",
    "load",
    "create_task",
    "get_latest_checkpoint_path",
    "quantize_statically",
]
