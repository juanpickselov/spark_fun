def read_the_data(sprksess):
    txt_file_df = sprksess.read.text('the_data.txt')
    return txt_file_df


if __name__ == '__main__':
    read_the_data()
