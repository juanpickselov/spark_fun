def write_the_data(sprksess, tfile_df):
    print('App Name:', sprksess.conf.get('spark.app.name'))
    print('Number of lines:', tfile_df.count)
    tfile_df.show(truncate=False)
    sprksess.sql("""CREATE EXTERNAL TABLE IF NOT EXISTS TOMG_TEST_THIS(NAME STRING, ITEM STRING)
    LOCATION 'C:/zData/hivedata/TOMG_TEST_TBL'
    """)


if __name__ == '__main__':
    write_the_data()
