def make_the_table(sprksess):
    print('App Name:', sprksess.conf.get('spark.app.name'))

    sprksess.sql("""CREATE EXTERNAL TABLE IF NOT EXISTS ITEM_LISTING(NAME STRING, ITEM STRING)
    LOCATION 'C:/zData/hivedata/ITEM_LISTING'
    """)
    fill_the_table(sprksess)

def fill_the_table(sprksess):
    sprksess.sql("""INSERT INTO TABLE ITEM_LISTING VALUES 
    ('Spark: The Definitive Guide','book'),
    ('Effective Python','book'),
    ('bugfix cards','index cards')
    """)
