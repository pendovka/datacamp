from common.base import session
from common.queries import insight_query 

def main():
       session.execute(insight_query)
       session.commit()
       print("Insights view created")
