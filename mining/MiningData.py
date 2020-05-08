import pandas as pd
import os
import csv
import json
import time
from datetime import datetime

from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

style.use("dark_background")

import re
import urllib

path = "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data"

htms = []


def getMCK():
    listFolder = [x[0] for x in os.walk(path)]

    for folder in listFolder[1:]:
        files = os.listdir(folder)
        htm = folder.split("/")[-1]
        htms.append(htm)

        if len(files) > 0:
            for file in files:
                filename = file.replace('.' + htm, "")
                fullFilePath = folder + '/' + file
                print(fullFilePath)
                contentFile = open(fullFilePath, 'r', encoding='mac_roman').read()

                first = contentFile.split('drawChartForFirstTime(')
                if len(first) >= 2:
                    jsonString = first[1].split(');\n});\n</script>\n<input type="hidden" id="whichSymbolIsDraw"')
                    print(jsonString[0])

                    jsonLoad = json.loads(jsonString[0])
                    result = pd.DataFrame(jsonLoad)
                    result['date'] = pd.to_datetime(result['transDate'], unit='ms')
                    result.to_csv("/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/vsc/" + filename + ".csv", index=True)


getMCK()
