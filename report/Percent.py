import matplotlib.pyplot as plt
import os
import pandas as pd

path = "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data"


def getPercentFollowYear():
    listFolder = [x[0] for x in os.walk(path)]

    for folder in listFolder[1:]:
        print("folder = " + folder)
        if folder == "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/vcs":
            files = os.listdir(folder)
            htm = folder.split("/")[-1]
            if len(files) > 0:
                for file in files:
                    fileName = file.replace('.' + htm, "")
                    df = pd.read_csv("/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/vcs/" + file)
                    dfOut = pd.DataFrame(columns=['Year', 'Status', 'Value'])
                    for index, row in df.iterrows():
                        if index == 0:
                            yearOld = row['transDate'].split('-')[2]
                            closeOld = row['close']
                            dfOut = dfOut.append({'Year': yearOld, 'Close': closeOld, 'Status': "START", 'Value': 0}, ignore_index=True)
                        else:
                            yearNew = row['transDate'].split('-')[2]
                            if yearNew != yearOld:
                                percent = row['close'] - closeOld
                                if percent < 0:
                                    status = "GIAM"
                                elif percent > 0:
                                    status = "TANG"
                                else:
                                    status = "KHONG DOI"
                                dfOut = dfOut.append({'Year': yearNew, 'Close': row['close'], 'Status': status, 'Value': (percent/closeOld) * 100}, ignore_index=True)
                                closeOld = row['close']

                            yearOld = yearNew
                    dfOut.to_csv("/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/percent/year/" + fileName, index=True)


getPercentFollowYear()