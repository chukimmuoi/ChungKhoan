import matplotlib.pyplot as plt
import os
import pandas as pd


def get_percent_follow_year(path, in_folder, out_folder, compare_value):
    list_folder = [x[0] for x in os.walk(path)]

    for folder in list_folder[1:]:
        if folder == path + '/' + in_folder:
            files = os.listdir(folder)

            if len(files) > 0:
                for file in files:
                    file_name = file.replace('.csv', "")
                    full_file_path = folder + '/' + file
                    print(file_name)

                    df = pd.read_csv(full_file_path)
                    df_out = pd.DataFrame(columns=['Year', 'Status', 'Value'])
                    so_ky = 0
                    gia_tri_hien_tai = 0
                    gia_tri_tuong_lai = 0
                    for index, row in df.iterrows():
                        if index == 0:
                            so_ky = 1
                            gia_tri_hien_tai = row['close']

                            year_old = row['transDate'].split('-')[2]
                            close_old = row['close']
                            df_out = df_out.append(
                                {
                                    'Year': year_old,
                                    'Close': close_old,
                                    'Status': "START",
                                    'Value': 0
                                },
                                ignore_index=True)
                        else:
                            year_new = row['transDate'].split('-')[2]
                            if year_new != year_old:
                                so_ky += 1
                                gia_tri_tuong_lai = row['close']

                                percent = row['close'] - close_old
                                if percent < 0:
                                    status = "GIAM"
                                elif percent > 0:
                                    status = "TANG"
                                else:
                                    status = "KHONG DOI"
                                df_out = df_out.append(
                                    {
                                        'Year': year_new,
                                        'Close': row['close'],
                                        'Status': status,
                                        'Value': (percent/close_old) * 100
                                    },
                                    ignore_index=True)
                                close_old = row['close']

                            year_old = year_new

                    ty_suat_sinh_loi = ((gia_tri_tuong_lai / gia_tri_hien_tai)**(1/so_ky) - 1) * 100
                    if ty_suat_sinh_loi > compare_value:
                        print(file_name + " co ty suat sinh loi: " + str(ty_suat_sinh_loi))
                    df_out = df_out.append(
                        {
                            'Year': "2021",
                            'Close': "close",
                            'Status': "status",
                            'Value': ty_suat_sinh_loi
                        }, ignore_index=True)

                    df_out.to_csv(path + '/' + out_folder + '/' + file_name + ".csv", index=True)


get_percent_follow_year('../data', 'csv', 'percent/year', 15)