# Copyright 2018-2021 Open Source Robotics Foundation, Inc.
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

"""Module for OnProcessExit class."""

from typing import Callable
from typing import cast
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union

from .on_process_event_base import OnProcessEventBase
from ..events.process import ProcessExited
from ..events.process import RunningProcessEvent
from ..launch_context import LaunchContext
from ..some_actions_type import SomeActionsType


if TYPE_CHECKING:
    from ..actions import ExecuteProcess  # noqa: F401


class OnProcessExit(OnProcessEventBase):
    """
    Convenience class for handling a process exited event.

    It may be configured to only handle the exiting of a specific action,
    or to handle all exited processes.
    """

    def __init__(
        self,
        *,
        target_action:
            Optional[Union[Callable[['ExecuteProcess'], bool], 'ExecuteProcess']] = None,
        on_exit:
            Union[
                SomeActionsType,
                Callable[[ProcessExited, LaunchContext], Optional[SomeActionsType]]
            ],
        **kwargs
    ) -> None:
        """Create an OnProcessExit event handler."""
        on_exit = cast(
            Union[
                RunningProcessEvent,
                Callable[[ProcessExited, LaunchContext], Optional[SomeActionsType]]],
            on_exit)
        super().__init__(
            process_matcher=target_action,
            on_event=on_exit,
            target_event_cls=ProcessExited,
            **kwargs,
        )
