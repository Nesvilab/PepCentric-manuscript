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

import re
from datetime import datetime

# log_path = r"G:\Dropbox\Fengchao_papers\pepcentric\script\results\KRAS\pepquery\run_pepquery.log"
log_path = r"G:\Dropbox\Fengchao_papers\pepcentric\script\results\entrapment_12cptac\pepquery\run_pepquery.log"

log_lines = open(log_path, "r").read().split("\n")

log_entry_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[INFO *\] (.+ - .+)")

steps = {
    'Peptide preparation and initial filtering': {
        "start": "Searching MS/MS dataset:",
        "end": "Step 1: target peptide sequence preparation and initial filtering done:"},
    'Candidate spectra retrieval': {
        "start": "Step 1: target peptide sequence preparation and initial filtering done:",
        "end": "[readSpectraFromMSMSlibrary:371] - Used CPUs:"},
    'PSM scoring': {
        "start": "[readSpectraFromMSMSlibrary:371] - Used CPUs:",
        "end": "Step 2: candidate spectra retrieval and PSM scoring done:"},
    'Competitive filtering based on reference sequences and statistical evaluation': {
        "start": "Step 2: candidate spectra retrieval and PSM scoring done:",
        "end": "Step 3-4: competitive filtering based on reference sequences and statistical evaluation done:"},
    'Competitive filtering based on unrestricted modification searching': {
        "start": "Step 3-4: competitive filtering based on reference sequences and statistical evaluation done:",
        "end": "End."}
}


def calculate_duration(start, end):
    fmt = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start, fmt)
    end_dt = datetime.strptime(end, fmt)
    return (end_dt - start_dt).total_seconds()


start = ""
end = ""

for line in log_lines:
    match = log_entry_pattern.search(line)
    if match:
        start = match.group(1)
        break

for line in reversed(log_lines):
    match = log_entry_pattern.search(line)
    if match:
        end = match.group(1)
        break

print(f"Start: {start}")
print(f"End: {end}")
print(f"Duration: {calculate_duration(start, end):.2f} s")

start_times = {}
durations = {step: 0 for step in steps}

for line in log_lines:
    match = log_entry_pattern.search(line)
    if match:
        timestamp, message = match.groups()
        for step, info in steps.items():
            if info["start"] in message:
                start_times[step] = timestamp
            elif info["end"] in message and step in start_times:
                duration = calculate_duration(start_times[step], timestamp)
                durations[step] += duration
                start_times.clear()

# Print results.
for step, total_duration in durations.items():
    print(f"{step}: {total_duration:.2f} s")
