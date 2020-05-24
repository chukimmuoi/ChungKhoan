import matplotlib.pyplot as plt
import os
import pandas as pd

path = "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data"


def getReport():
    listFolder = [x[0] for x in os.walk(path)]

    for folder in listFolder[2:]:
        files = os.listdir(folder)
        htm = folder.split("/")[-1]
        if len(files) > 0:
            for file in files:
                fileName = file.replace('.' + htm, "")
                df = pd.read_csv("/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/vcs/" + file)
                plot_df = df.set_index(['transDate'])
                plot_df['close'].plot()
                plt.xlabel('Thời gian')
                plt.ylabel('Giá chứng khoán')
                plt.title(fileName)
                plt.legend()
                plt.show()


#getReport()


def getPercentFollowYear():
    listFolder = [x[0] for x in os.walk(path)]

    for folder in listFolder[2:]:
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
                        dfOut = dfOut.append({'Year': yearOld, 'Status': "START", 'Value': 0}, ignore_index=True)
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
                            dfOut = dfOut.append({'Year': yearNew, 'Status': status, 'Value': (row['close']/closeOld - 1) * 100}, ignore_index=True)
                            closeOld = row['close']

                        yearOld = yearNew
                dfOut.to_csv("/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/percent/" + fileName, index=True)


getPercentFollowYear()

