#!/usr/bin/python3
#coding:utf-8

import pymysql.cursors,settings

def execute(sql, params=None, db='', is_fetchone=True):
    #Connect to the database
    connection = pymysql.connect(host=settings.DB_HOST,
                                 port=settings.DB_PORT,
                                 user=settings.DB_USER,
                                 password=settings.DB_PASSWORD,
                                 db=db,
                                 autocommit=True,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            if is_fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
    finally:
        connection.close()