import matplotlib.pyplot as plt
import os
import pandas as pd

path = "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/percent/"
chot= ["VIC", "VCS", "MWG", "VNM", "PNJ", "MBB", "VCB",  "REE", "HPG", "FPT", "VJC", "VGC"]

def getReport():
    listFolder = [x[0] for x in os.walk(path)]

    for folder in listFolder[1:]:
        print("folder = " + folder)
        if folder == "/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/percent/year":
            files = os.listdir(folder)
            htm = folder.split("/")[-1]
            if len(files) > 0:
                for file in files:
                    fileName = file.replace('.csv', "")
                    print("----> fileName = " + fileName)
                    if fileName in chot:
                        df = pd.read_csv("/Users/chukimmuoi/PycharmProjects/ChungKhoan/data/percent/year/" + file)

                        plt.bar(df["Year"], df["Value"])
                        plt.xlabel('Thời gian')
                        plt.ylabel('Giá chứng khoán')
                        plt.title(fileName)
                        plt.show()


getReport()




