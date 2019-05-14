def make_the_table(sprksess):
    print('App Name:', sprksess.conf.get('spark.app.name'))

    sprksess.sql("""CREATE EXTERNAL TABLE IF NOT EXISTS ITEM_DATA(NAME STRING, ITEM STRING)
    LOCATION 'C:/zData/hivedata/ITEM_DATA'
    """)


if __name__ == '__main__':
    make_the_table()
