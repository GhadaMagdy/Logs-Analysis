
import psycopg2
from psycopg2 import Error

question1='What are the most popular three articles of all time?'
query1="select count(*) as views,slug from articles INNER JOIN log on (concat('/article/',articles.slug)=log.path) where log.status LIKE '%200%' group by articles.slug order by views DESC limit 3"
class LogsAnalysis:
    def __init__(self):
        try:
            self.db = psycopg2.connect(host="localhost",database="news", user="postgres", password="postgres")
            self.cursor = self.db.cursor()
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while connecting to PostgreSQL", error)
    def execute_query(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def solve(self,ques,query,str="views"):
        result=self.execute_query(query)
        print (ques)
        for i in range(len(result)):
            print ('"',result[i][0]," — ",result[i][1]," ",str,'\n')
    def exit(self):
        self.db.close()


if __name__ == '__main__':
    LogsAnalysis = LogsAnalysis()
    LogsAnalysis.solve(question1, query1)
    LogsAnalysis.exit()

