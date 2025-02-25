import mysql
import mysql.connector
import datetime


class delete_ssrf_data:

    def __init__(self):
        print(datetime.datetime.now())

    def amsdbconnection(self):
        # replica = 35.154.213.175
        # master = 35.154.36.218
        self.conn = mysql.connector.connect(host='35.154.213.175',
                                            database='appserver_core',
                                            user='qauser',
                                            password='qauser')
        self.cursor = self.conn.cursor()

    def commit_changes(self, query):
        pass

    def delete_assessment_test_users(self):
        self.amsdbconnection()
        tuser_results = "delete from test_results where testuser_id in (2359422,2359424,2359426,2359468,2359470);"
        self.cursor.execute(tuser_results)
        self.conn.commit()
        tuser_scores = 'delete from candidate_scores where testuser_id in ' \
                       '(select tu.id from test_users tu inner join tests t on t.id = tu.test_id ' \
                       'where test_id in(10564,15254)' \
                       ' and login_time is not null and t.tenant_id in (159,1786));'
        print(tuser_scores)

        self.cursor.execute(tuser_scores)
        self.conn.commit()
        tuser_login_infos = 'delete from test_user_login_infos where testuser_id in ' \
                            '(select tu.id from test_users tu inner join tests t on t.id = tu.test_id ' \
                            'where test_id in(10564,15254) ' \
                            'and login_time is not null and t.tenant_id in (159,1786));'
        print(tuser_login_infos)
        self.cursor.execute(tuser_login_infos)
        self.conn.commit()

        tuser_proctoring_infos = 'delete from test_user_proctor_details where testuser_id in ' \
                                 '(select tu.id from test_users tu inner join tests t on t.id = tu.test_id ' \
                                 'where test_id in(10564,15254) ' \
                                 'and login_time is not null and t.tenant_id in (159,1786));'
        print(tuser_proctoring_infos)
        self.cursor.execute(tuser_proctoring_infos)
        self.conn.commit()

        update_tuser_statuss = 'update test_users set login_time = NULL, log_out_time = NULL, status = 0, ' \
                               'client_system_info = NULL, time_spent = NULL, is_password_disabled = 0,config = NULL, ' \
                               'client_system_info = NULL, total_score = NULL, test_start_time = NULL, percentage = NULL ' \
                               'where test_id in(10564,15254) and ' \
                               'login_time is not null;'
        print(update_tuser_statuss)
        self.cursor.execute(update_tuser_statuss)
        self.conn.commit()
        self.conn.close()


del_data = delete_ssrf_data()
del_data.delete_assessment_test_users()
print(datetime.datetime.now())
