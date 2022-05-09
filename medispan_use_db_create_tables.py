import datetime 

sql =f'''
list @medispan/mcm; 


create or replace table test_mf2ndcm_{datetime.date.today().strftime("%Y%m%d")}
 (ndc_upc_hri varchar2(11) not null
 ,modifier_code varchar2(6) not null
 ,reserve varchar2(6) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;


create or replace table test_mf2sum_{datetime.date.today().strftime("%Y%m%d")}
 (record_type varchar2(3) null
 ,reserve_1 varchar2(1) null
 ,sequence_number number(3,0) null
 ,reserve_2 varchar2(1) null
 ,comment_marker varchar2(1) null
 ,data_comment varchar2(87) null
 )
;

'''

sql_file = open("medispan_create_tables.sql", "w")
sql_file.write(sql)
sql_file.close()
