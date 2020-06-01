import pandas as pd
import os
import json
from matplotlib import style

style.use("dark_background")


def convert_htm_to_csv(path, in_folder, out_folder):
    list_folder = [x[0] for x in os.walk(path)]

    for folder in list_folder[1:]:
        if folder == path + '/' + in_folder:
            files = os.listdir(folder)

            if len(files) > 0:
                for file in files:
                    file_name = file.replace('.htm', "")
                    full_file_path = folder + '/' + file
                    print(file_name)

                    content_file = open(full_file_path, 'r', encoding='utf-8').read().replace("\n", "")
                    first = content_file.split('drawChartForFirstTime(')
                    if len(first) >= 2:
                        json_string = first[1].split(');});</script><input type="hidden" id="whichSymbolIsDraw"')

                        data = json.loads(json_string[0])
                        result = pd.DataFrame(data)
                        result['transDate'] = pd.to_datetime(result['transDate'], unit='ms').dt.strftime('%d-%m-%Y')
                        result.to_csv(path + '/' + out_folder + '/' + file_name + ".csv", index=True)


convert_htm_to_csv('../data', 'htm', 'csv')
