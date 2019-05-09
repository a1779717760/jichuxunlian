from pymysql import *

def create_table():
    conne = connect(host='localhost', user='root', passwd='root',database='python_test',charset='utf8')
    cs1 = conne.cursor()
    input = open('002.txt')
    for line in input:
        linelist = line.split(' ')
        #print('%s' %(linelist))
    for i in linelist:
        print('%s' %(i))
        cs1.execute("insert into jihuoma(ma) values ('%s');" %(i))
    conne.commit()
    cs1.close()
    conne.close()

if __name__ == '__main__':
    create_table()