import datetime


sql = f'''
select * from test_mf2val_{datetime.date.today().strftime("%Y%m%d")}  limit 10;   
select * from test_mf2tcgpi_{datetime.date.today().strftime("%Y%m%d")} limit 10;   
select * from test_mf2sum_{datetime.date.today().strftime("%Y%m%d")} limit 10;  
select * from test_mf2sec_{datetime.date.today().strftime("%Y%m%d")} limit 10;  
select * from test_mf2prc_{datetime.date.today().strftime("%Y%m%d")} limit 10;  
select * from test_mf2ndc_{datetime.date.today().strftime("%Y%m%d")}  limit 10;  
select * from test_mf2name_{datetime.date.today().strftime("%Y%m%d")} limit 10; 
select * from test_mf2mod_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_mf2lab_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_MF2GPR_{datetime.date.today().strftime("%Y%m%d")}  limit 10;  
select * from test_mf2gppc_{datetime.date.today().strftime("%Y%m%d")} limit 10;  
select * from test_mf2err_{datetime.date.today().strftime("%Y%m%d")}  limit 10;  
select * from test_mf2dict_{datetime.date.today().strftime("%Y%m%d")} limit 10;  
select * from test_MF2RTDRG_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_mf2set_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_mf2ings_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_MF2idrg_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_MF2str_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_indgind_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_mf2drgnm_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_mcmname_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_mf2drg_{datetime.date.today().strftime("%Y%m%d")} limit 10;
select * from test_mf2desc_{datetime.date.today().strftime("%Y%m%d")} limit 10;  
select * from test_mf2ndcm_{datetime.date.today().strftime("%Y%m%d")}  limit 10;  

'''

sql_file = open("medispan_qc.sql", "w")
sql_file.write(sql)
sql_file.close()