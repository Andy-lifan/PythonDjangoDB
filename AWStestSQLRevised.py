#!/usr/bin/env python3
import pymysql

def main():
    try:
        #create an instance of connection to acquire the right
        cnnx = pymysql.connect(user='*****', password='*****', host='dbtest-aws.cguv4ydrregf.us-east-2.rds.amazonaws.com',database='dbtest1')
        cursor = cnnx.cursor ()        
        #create a table
        sql = " create table if not exists tb_test (employeeid int (6), lastname varchar(50), firstname varchar(50));"
        cursor.execute (sql)        
        #insert data
        sql = "INSERT INTO tb_test (employeeid, lastname, firstname) VALUES (1,'Lau','Andy'), (10, 'Chen', 'Mike'), (110, 'Su','Peter');"
        cursor.execute (sql)        
        #query data
        sql = "SELECT * from tb_test;"
        cursor.execute (sql)                
        allRows = cursor.fetchall();
        if allRows:
            print('employeeid    lastname    firstname')
            for rec in allRows:
                print('{0:>8}    {1:>8}    {2:>8}'.format(rec[0], rec[1], rec[2]))
                #print('employeeid: {0}, last name: {1}, firstname: {2}'.format(rec[0], rec[1], rec[2]))
        else: print('No data records for query.')   
        #drop table tb_test
        sql = "drop table if exists tb_test;"
        cursor.execute (sql)     
        cursor.close()
        cnnx.close()
    except Exception as e:
        print(e)  

        
if __name__ == '__main__': main()