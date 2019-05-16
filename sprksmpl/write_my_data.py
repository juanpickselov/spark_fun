def write_the_data(sprksess, tfile_df):
    print('App Name:', sprksess.conf.get('spark.app.name'))
    print('Number of lines:', tfile_df.count)
    tfile_df.show(truncate=False)


if __name__ == '__main__':
    write_the_data()
