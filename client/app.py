# Copyright 2015 gRPC authors.
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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import user_pb2
import user_pb2_grpc


def run():
    response = []
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = user_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(user_pb2.GetUsersRequest())
    print(response.users)


if __name__ == "__main__":
    run()
