import pandas as pd
import os
import json
from matplotlib import style

style.use("dark_background")

path = "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data"

htms = []


def getMCK():
    listFolder = [x[0] for x in os.walk(path)]

    for folder in listFolder[1:]:
        print("folder = " + folder)
        if folder == "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/htm":
            files = os.listdir(folder)
            htm = folder.split("/")[-1]
            if htm != 'htm':
                break
            htms.append(htm)

            if len(files) > 0:
                for file in files:
                    fileName = file.replace('.' + htm, "")
                    print("1 -----> fileName = " + fileName)
                    fullFilePath = folder + '/' + file
                    print("2 -----> fullFilePath = " + fullFilePath)
                    contentFile = open(fullFilePath, 'r', encoding='utf-8').read().replace("\n", "")
                    first = contentFile.split('drawChartForFirstTime(')
                    if len(first) >= 2:
                        jsonString = first[1].split(');});</script><input type="hidden" id="whichSymbolIsDraw"')
                        print(fileName + " === " + jsonString[0])

                        jsonLoad = json.loads(jsonString[0])
                        result = pd.DataFrame(jsonLoad)
                        result['transDate'] = pd.to_datetime(result['transDate'], unit='ms').dt.strftime('%d-%m-%Y')
                        result.to_csv("/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/vcs/" + fileName + ".csv", index=True)


getMCK()
