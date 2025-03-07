#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import datetime

import pandas as pd
import random

target = pd.read_csv(r"human_target.txt", sep="\t", header=None)
shuffled = pd.read_csv(r"human_shuffled.txt", sep="\t", header=None)

shuffled_set = set(shuffled[0]) - set(target[0])
sampled_peptides = random.sample(list(shuffled_set), 5000)

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y%m%d_%H%M%S")
filename = f"sampled_shuffled_{formatted_time}.txt"
with open(filename, "w") as f:
    for peptide in sampled_peptides:
        f.write(peptide + "\n")

print(f"Sampled peptides written to {filename}")
