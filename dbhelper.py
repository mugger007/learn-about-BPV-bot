from sqlalchemy import *
from config import host, port, database, user, password

class DBHelper:

    def __init__(self):
        conn_str = f"postgresql://{user}:{password}@{host}/{database}"
        global engine
        engine = create_engine(conn_str)
        metadata = MetaData(bind = engine)
        global user_tb
        user_tb = Table('TABLE_NAME', metadata, autoload = True)

    def add_user(self, user_id):
        query = insert(user_tb).values(user_id = user_id)
        connection = engine.connect()
        ResultProxy = connection.execute(query)

    def add_user_education(self, user_education, user_id):
        query = update(user_tb).values(user_education = user_education).where(user_tb.c.user_id == user_id)
        connection = engine.connect()
        ResultProxy = connection.execute(query)

    def get_user_education(self, user_id):
        query = select(user_tb.c.user_education).where(user_tb.c.user_id == user_id)
        connection = engine.connect()
        result = connection.execute(query)
        return [r.user_education for r in result]

    #update completion status
    def update_column_status(self, column_values_dict, user_id):
        query = update(user_tb).values(column_values_dict).where(user_tb.c.user_id == user_id)
        connection = engine.connect()
        ResultProxy = connection.execute(query)
    #get completion status
    def get_column_status(self, columns, user_id):
        column_status = []
        for i in columns:
            query = select(column(i)).where(user_tb.c.user_id == user_id)
            connection = engine.connect()
            result = connection.execute(query)
            column_status.append([r[0] for r in result][0])
        return column_status

    #check if pre quiz is completed
    def check_pre_quiz(self, user_id):
        query = select(user_tb.c.pre_quiz_q5).where(user_tb.c.user_id == user_id)
        connection = engine.connect()
        result = connection.execute(query)
        return [r.pre_quiz_q5 for r in result][0]
    #update quiz
    def update_quiz(self, quiz_dict, user_id):
        query = update(user_tb).values(quiz_dict).where(user_tb.c.user_id == user_id)
        connection = engine.connect()
        ResultProxy = connection.execute(query)
    #update survey
    def update_survey(self, survey_dict, user_id):
        query = update(user_tb).values(survey_dict).where(user_tb.c.user_id == user_id)
        connection = engine.connect()
        ResultProxy = connection.execute(query)
