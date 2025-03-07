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

import pandas as pd

pepquery_wd = Path(r"G:\Dropbox\Fengchao_papers\pepcentric\script\results\entrapment_12cptac\pepquery\\")

pepquery_df = pd.DataFrame()
for f in pepquery_wd.rglob("*\\psm_rank.txt"):
    pepquery_df = pd.concat([pepquery_df, pd.read_csv(f, sep="\t")])

pepquery_df = pepquery_df.reset_index(drop=True)
pepquery_df = pepquery_df[pepquery_df["confident"] == "Yes"]

pepquery_df.to_csv(pepquery_wd.joinpath("entrapment_12_pepquery.csv"), index=False)

print("pepquery_sequence: ", pepquery_df["peptide"].nunique())

