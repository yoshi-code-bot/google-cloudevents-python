# Copyright 2020 Google LLC
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

import google.protobuf.json_format as json_format


def test_cloud_pubsub_v1_messagepublisheddata_binary():
    from google.events.cloud.pubsub_v1 import MessagePublishedData

    with open("tests/data/cloud_pubsub_v1_messagepublisheddata_binary.json") as f:
        raw_data = f.read()

    obj = MessagePublishedData.from_json(raw_data, ignore_unknown_fields=True)
    # Ensure the parsed object is not empty.
    assert obj != MessagePublishedData()


def test_cloud_pubsub_v1_messagepublisheddata_text():
    from google.events.cloud.pubsub_v1 import MessagePublishedData

    with open("tests/data/cloud_pubsub_v1_messagepublisheddata_text.json") as f:
        raw_data = f.read()
    obj = MessagePublishedData.from_json(raw_data, ignore_unknown_fields=True)
    # Ensure the parsed object is not empty.
    assert obj != MessagePublishedData()
