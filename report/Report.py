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


getReport()
