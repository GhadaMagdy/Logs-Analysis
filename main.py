
import psycopg2

question1='What are the most popular three articles of all time?'
query1="select * from authors"
class LogsAnalysis:
    def __init__(self):
        try:
            self.db = psycopg2.connect("dbname=news")
            self.cursor = self.db.cursor()
        except Exception as e:
            print (e)
    def execute_query(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def solve(self,ques,query):
        result=self.execute_query(query)
        print (ques)
        print (result)
    def exit(self):
        self.db.close()


if __name__ == '__main__':
    LogsAnalysis = LogsAnalysis()
    LogsAnalysis.solve(question1, query1)
    LogsAnalysis.exit()

