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

from pathlib import Path
from matplotlib_venn import venn2

import pandas as pd

pepquery_wd = Path(r"G:\Dropbox\Fengchao_papers\pepcentric\script\results\KRAS\pepquery\\")
pepcentric_path = r"G:\Dropbox\Fengchao_papers\pepcentric\script\results\KRAS\pepcentric\job-a7be635a-d4a0-4322-b9f8-03a9d5e611b5.tsv"

pepquery_psm = pd.DataFrame()
for f in pepquery_wd.rglob("*psm_rank.txt"):
    pepquery_psm = pd.concat([pepquery_psm, pd.read_csv(f, sep="\t")])

pepquery_psm = pepquery_psm.reset_index(drop=True)
pepquery_psm = pepquery_psm[pepquery_psm["confident"] == "Yes"]

pepquery_psm['spectrum_title'] = pepquery_psm['spectrum_title'].str.replace(r":\d+:\d+", lambda m: "." + m.group(0).split(":")[1], regex=True)

pepcentric_psm = pd.read_csv(pepcentric_path, sep="\t")

pepcentric_psm = pepcentric_psm.reset_index(drop=True)
pepcentric_psm["spectrum"] = pepcentric_psm["run"] + "." + pepcentric_psm["scan"].astype(str)

set1 = set(pepquery_psm["spectrum_title"])
set2 = set(pepcentric_psm["spectrum"])

venn2([set1, set2], set_labels=('PepQuery', 'PepCentric'), set_colors=("#A67968", "#168C8C"), alpha=1)

# list the PSm that is unique to pepquery_psm and pepcentric_psm
unique_pepquery_psm = set1 - set2
unique_pepcentric_psm = set2 - set1

print("unique_pepquery_psm: ", unique_pepquery_psm)
print("unique_pepcentric_psm: ", unique_pepcentric_psm)
