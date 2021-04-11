# @Author: Абделлах Улахияне
# @Date:   2021-04-11 04:34:24
# @Last Modified by:   Абделлах Улахияне
# @Last Modified time: 2021-04-11 05:49:43
import sqlite3
class db(object):
    @staticmethod
    def add(table_name,data=dict()):
        sql = "INSERT INTO %s (`%s`) VALUES ('%s')"%(table_name,"`,`".join(list(data.keys())),"','".join(list(map(str,data.values()))))
        try:
            cnx__ = sqlite3.connect("chess.db")
            cur__ = cnx__.cursor()
            cur__.execute(sql)
        except sqlite3.Error as err:
            cnx__.rollback()
            return False
        else:
            cnx__.commit()
        finally:
            cur__.close()
            cnx__.close()
        return True
    
    @staticmethod
    def update(table_name,data=dict(),commands=dict())->bool:
        sql = "UPDATE %s SET "%(table_name)
        for x,y in data.items():
            sql+="`%s`='%s',"%(str(x),str(y))
        sql=sql.strip(',')
        if len(commands)>0:
            sql+=" where "
            for x,y in commands.items():
                sql+="`%s`='%s',"%(str(x),str(y))
            sql=sql.strip(',')
        try:
            cnx__ = sqlite3.connect("chess.db")
            cur__ = cnx__.cursor()
            cur__.execute(sql)
        except sqlite3.Error as err:
            cnx__.rollback()
            return False
        else:
            cnx__.commit()
        finally:
            cur__.close()
            cnx__.close()
        return True
    @staticmethod
    def delete(table_name,commands=dict())->bool:
        sql = "DELETE FROM %s "%(table_name)
        
        if len(commands)>0:
            sql+=" where "
            for x,y in commands.items():
                sql+="`%s`='%s' and "%(str(x),str(y))
            sql=sql.strip(' and ')
        print(sql)
        try:
            cnx__ = sqlite3.connect("chess.db")
            cur__ = cnx__.cursor()
            cur__.execute(sql)
        except sqlite3.Error as err:
            cnx__.rollback()
            return False
        else:
            cnx__.commit()
        finally:
            cur__.close()
            cnx__.close()
        return True

    @staticmethod
    def select(table_name,commands=dict()):
        sql = "SELECT * FROM %s "%(table_name) 
        if len(commands)>0:
            sql+=" where "
            for x,y in commands.items():
                sql+="`%s`='%s' and "%(str(x),str(y))
            sql=sql.strip(' and ')
        try:
            cnx__ = sqlite3.connect("chess.db")
            cur__ = cnx__.cursor()
            cur__.execute(sql)
        except sqlite3.Error as err:
            cnx__.rollback()
        else:
            return cur__.fetchall()
                
        finally:
            cur__.close()
            cnx__.close()

        