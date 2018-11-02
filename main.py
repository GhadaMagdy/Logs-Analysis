
import psycopg2
from psycopg2 import Error

ques1='What are the most popular three articles of all time?'
query1="select slug, count(*) as views from articles INNER JOIN log on (concat('/article/',articles.slug)=log.path) where log.status LIKE '%200%' group by articles.slug order by views DESC limit 3"

ques2="Who are the most popular article authors of all time?"
query2="select authors.name , count(*) as views from articles INNER JOIN authors on (authors.id=articles.author) INNER JOIN log on (concat('/article/',articles.slug)=log.path) where log.status LIKE '%200%' group by authors.name order by views DESC;"

ques3="On which days did more than 1% of requests lead to errors?"
query3="select * from (select a.day,round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)as errp from(select date(time) as day, count(*) as hits from log group by day) as a inner join(select date(time) as day, count(*) as hits from log where status like '%404%' group by day) as b on a.day = b.day)as t where errp > 1.0;"
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
            print ('\t',result[i][0]," — ",result[i][1]," ",str,'\n')
    def exit(self):
        self.db.close()


if __name__ == '__main__':
    LogsAnalysis = LogsAnalysis()
    LogsAnalysis.solve(ques1, query1)
    LogsAnalysis.solve(ques2, query2)
    LogsAnalysis.solve(ques3, query3,' % error')
    LogsAnalysis.exit()

