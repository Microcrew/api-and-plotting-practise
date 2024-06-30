import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import requests
from pyscbwrapper import SCB

api_url = "https://api.scb.se/OV0104/v1/doris/sv/ssd/START/HA/HA0201/HA0201A/ImportExportSnabbAr"
call = {
  "query": [],
  "response": {
    "format": "json"
  }
}

response = requests.post(api_url, json=call)
jsonData = response.json()
print(jsonData)
quit()
imports = []
exports = []
balance = []
dates = []
for pair in (pair for pair in jsonData["data"] if pair["key"][0] == "ITOT"):
    imports.append(int(pair["values"][0]))
    dates.append(int(pair["key"][1]))

for pair in (pair for pair in jsonData["data"] if pair["key"][0] == "ETOT"):
    exports.append(int(pair["values"][0]))

for pair in (pair for pair in jsonData["data"] if pair["key"][0] == "HANDELSB"):
    balance.append(int(pair["values"][0]))

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=False)

ax1.plot(dates, imports, label = "Imports")
ax1.plot(dates, exports, label = "Exports")
ax2.plot(dates, balance, label = "Trade balance")
ax1.legend()
ax2.legend()
ax2.fill_between(dates, 0, balance, alpha=0.7)
plt.show()

"""
scb = SCB('sv', 'HA', 'HA0201', 'HA0201A')
print(scb.get_data())

"""