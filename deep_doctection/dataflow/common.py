# -*- coding: utf-8 -*-
# File: common.py

# Copyright 2021 Dr. Janis Meyer. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Some additional DataFlow classes for transforming and processing datapoints
"""
from typing import Any

from dataflow.dataflow import ProxyDataFlow  # type: ignore

__all__ = ["FlattenData"]


class FlattenData(ProxyDataFlow):  # type: ignore
    """
    Flatten an iterator within a datapoint. Will flatten the datapoint if it is a list or a tuple.

    **Example:**

       dp_1 = ['a','b']

       dp_2 = ['c','d']

       will stream 'a', 'b', 'c', 'd'.
    """

    def __iter__(self) -> Any:
        for dp in self.ds:
            if isinstance(dp, (list, tuple)):
                for dpp in dp:
                    yield [dpp] if isinstance(dp, list) else tuple(dpp)
