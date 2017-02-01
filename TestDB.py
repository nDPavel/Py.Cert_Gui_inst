#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as db
#import sqlite3
dbCon = db.connect(r"./DB/Cert2.db3")
cur = dbCon.cursor()
sql = """select   u.Name,
                  us.Name,
                  cd.DateCre,
                  cd.DateExp,
                  cd.PodrName,
                  cd.UserName
                         from Unit as U,
                              UnitSubject as us,
                              CertDate as cd,
                              LinkCertORUnitSub as link
                                      WHERE 1=1
                                        and link.idPodr = us.id
                                        and link.IdCert = cd.id
                                        and U.id = us.idPodr
                                        and us.Name = 'Alapaevsk'
"""
try:
    cur.execute(sql)
    
except db.DatabaseError as err:
    print('Ошибка:',err)
else:
    print('запрос успешно выполнен')
    for Name,Name2, DateCre,DateExp,PodrName,UserName in cur:
        print(Name,Name2, DateCre,DateExp,PodrName,UserName)
        print("{0}|{1}|{2}|{3}|{4}|{5}".format(Name,Name2, DateCre,DateExp,PodrName,UserName)) 
    dbCon.commit()
    
dbCon.close()






















