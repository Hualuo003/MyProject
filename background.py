# coding=utf-8
import web
import MySQLdb


urls = ("/AdminLogin", "AdminLogin", "/Homepage", "Homepage")
app = web.application(urls, globals())


class AdminLogin:
    def GET(self):
        #print("get")
        return web.seeother('./static/Login.html', True)

    def POST(self):
        # web.header("Access-Control-Allow-Origin", "*")
        #print("post")
        params = web.input()
        username = params['username']
        password = params['password']

        db = MySQLdb.connect("localhost", port=3306, user="root", passwd="123456", db="lab", charset='utf8')
        cursor = db.cursor()
        sql = '''select * from user '''

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            #print(results)
            flag = 0
            for row in results:
                x = row[0]
                y = row[1]
                if x == username and y == password:
                    flag = 1

            if flag == 1:
                return 1
            else:
                return 0
        except:
            print("ERROR")
            db.rollback()
        cursor.close()
        db.close()


class Homepage:
    def GET(self):
        return web.seeother('/static/HomePage.html', True)


if __name__ == '__main__':
    app.run()
