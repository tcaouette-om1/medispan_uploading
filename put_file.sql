--File used to select database, schema and files for medispan staging. these are executed in the staging_sno_sql.py file.
use database research
;
use schema medispan
;
create or replace stage medispan
  FILE_FORMAT = (
  TYPE = 'CSV' 
  FIELD_DELIMITER  = '|' 
  EMPTY_FIELD_AS_NULL  = TRUE
  )
;

PUT file:///Users/tobiascaouette/Documents/medispan/med-cond_0_0_mo_pdu-w-opt_1.0_d_20220302/MCM/USAENG/DB/* @medispan/mcm auto_compress=true;


PUT file:///Users/tobiascaouette/Documents/medispan/indication_0_0_mo_pdu-std_1.0_d_20220302/IND/USAENG/DB/* @medispan/ind auto_compress=true;


PUT file:///Users/tobiascaouette/Documents/medispan/med-file2_0_0_mo_pdu-delimt_complete_d_20220302/MEDFV2/USAENG/DB/DELIMIT/* @medispan/mdfv2 auto_compress=true;
