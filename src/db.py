import pymysql


def iud(qry,val):
    con=pymysql.connect(host='sql106.infinityfree.com',port=3306,user='if0_34811636',password='XDw48cSis4Kf',db='if0_34811636_XXX')
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=cmd.lastrowid
    con.commit()
    con.close()

    return id

def selectone(qry,val):
    con=pymysql.connect(host='sql106.infinityfree.com',port=3306,user='if0_34811636',password='XDw48cSis4Kf',db='if0_34811636_XXX',cursorclass=pymysql.cursors.DictCursor)
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchone()

    return res

def selectall(qry):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='the_butcher',cursorclass=pymysql.cursors.DictCursor)
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    return res
def selectall2(qry,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='the_butcher',cursorclass=pymysql.cursors.DictCursor)
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchall()
    return res