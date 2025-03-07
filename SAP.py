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

import os.path
import matplotlib.pyplot as plt
import pandas as pd

p = r"G:\Dropbox\Fengchao_papers\pepcentric\script\results\SAP\5e5eb194-c07b-4e7f-9751-f428a1d30c7e_sequences.csv"
table = pd.read_csv(p, sep=",")

plt.rcParams['font.sans-serif'] = 'Arial'

table["binned_count"] = table["dataset_count"].apply(lambda x: 31 if x > 30 else x)

ax = table["binned_count"].value_counts().sort_index().plot(kind="bar")
plt.ylabel("dataset count", fontsize=20)

labels = [item.get_text() for item in ax.get_xticklabels()]
if labels[-1] != "31+":
    labels[-1] = ">30"
ax.set_xticklabels(labels)

xx = table["binned_count"].value_counts().sort_index().cumsum()
xx[0] = 0
xx.sort_index().shift(-1, fill_value=0)[:-1].plot(secondary_y=True, color="tab:orange")
plt.ylabel("cumulative dataset count", fontsize=20)


plt.gcf().set_size_inches(15, 5)
plt.savefig(os.path.dirname(p) + "/dataset_count.pdf")


