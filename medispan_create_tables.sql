
list @medispan/mcm; 


create or replace table test_mf2ndcm_20220509
 (ndc_upc_hri varchar2(11) not null
 ,modifier_code varchar2(6) not null
 ,reserve varchar2(6) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;


create or replace table test_mf2sum_20220509
 (record_type varchar2(3) null
 ,reserve_1 varchar2(1) null
 ,sequence_number number(3,0) null
 ,reserve_2 varchar2(1) null
 ,comment_marker varchar2(1) null
 ,data_comment varchar2(87) null
 )
;

