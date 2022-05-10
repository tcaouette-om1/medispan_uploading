import datetime 


sql = f'''
--MF2DICT
COPY INTO test_MF2DICT_{datetime.date.today().strftime("%Y%m%d")} FROM @medispan/mdfv2/MF2DICT.gz
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;

--MF2GPPC
COPY INTO test_MF2GPPC_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 generic_product_pack_code,
    cast(left(t.$2,6)||'.'||right(t.$2,3) as number) package_size,--updated 9(6)V9(3)
    t.$3 package_size_uom,
    cast(t.$4 as number) package_quantity,
    t.$5 unit_dose_unit_use_pkg_code,
    t.$6 package_description_code,
    t.$7 generic_product_identifier,
    t.$8 reserve,
    t.$9 transaction_code,
    t.$10 last_change_date
  from @medispan/mdfv2/MF2GPPC.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;

--MF2GPR
COPY INTO test_MF2GPR_{datetime.date.today().strftime("%Y%m%d")} FROM 
(
  select 
    t.$1 generic_product_pack_code,
    t.$2 gppc_price_code,
    t.$3 effective_date,
    cast(left(t.$4,5)||'.'||right(t.$4,6) as number) unit_price,
    t.$5 reserve,
    t.$6 transaction_code,
    t.$7 transaction_code
  from @medispan/mdfv2/MF2GPR.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE;

;

--AL: 
 /*NDC Modifier File*/   
 COPY INTO test_mf2ndcm_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 ndc_upc_hri,
    t.$2 modifier_code,
    t.$3 reserve,
    t.$4 transaction_code,
    to_date(t.$5,'YYYYMMDD') last_change_date
  from @medispan/mdfv2/MF2NDCM.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;   


/*NDC File*/
 COPY INTO test_MF2NDC_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 ndc_upc_hri,
    t.$2 drug_descriptor_id,--char
    t.$3 tee_code,
    t.$4 dea_class_code,
    t.$5 desi_code,
    t.$6 rx_otc_indicator_code,
    t.$7 generic_product_pack_code,
    t.$8 old_ndc_upc_hri,
    t.$9 new_ndc_upc_hri,
    t.$10 repackaged_code,
    t.$11 id_number_format_code,
    t.$12 third_party_restriction_code,
    t.$13 kdc,--char
    t.$14 kdc_flag,
    t.$15 medispan_labeler_id,
    t.$16 multi_source_code,
    t.$17 name_type_code,
    t.$18 item_status_flag,
    t.$19 innerpack_code,
    t.$20 clinic_pack_code,
    t.$21 reserve1,
    t.$22 ppg_indicator_code,
    t.$23 hfpg_indicatory_code,
    t.$24 dispensing_unit_code,
    t.$25 dollar_rank_code,
    t.$26 rx_rank_code,
    t.$27 storage_condition_code,
    t.$28 limited_distribution_code,
    to_date(t.$29,'YYYYMMDD') old_effective_date,
    to_date(t.$30,'YYYYMMDD') new_effective_date,
    t.$31 next_smaller_ndc_suffix,
    t.$32 next_larger_ndc_suffix,
    t.$33 reserve2,
    t.$34 transaction_code,
    to_date(t.$35,'YYYYMMDD') last_change_date
      from @medispan/mdfv2/MF2NDC.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE; 
;

/*MF2ERR Error Correct File
The Error Correct File is present only in an Incremental Update when an error correction has been made.
*/
 COPY INTO test_MF2ERR_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 KEY_IDENTIFIER,
    t.$2 UNIQUE_KEY,
    t.$3 DATA_ELEMENT_CODE,
    t.$4 DATA_ELEMENT_LENGTH,
    t.$5 RESERVE
  from @medispan/mdfv2/MF2ERR.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 

/*MF2LAB
Labeler File*/

COPY INTO test_MF2LAB_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 MEDISPAN_LABELER_ID,--char
    t.$2 MANUFACTURER_NAME,
    t.$3 MANUFACTURER_ABBR_NAME,
    t.$4 LABELER_TYPE_CODE,
    t.$5 RESERVE,
    t.$6 TRANSACTION_CODE,
    to_date(t.$7,'YYYYMMDD') LAST_CHANGE_DATE
    
  from @medispan/mdfv2/MF2LAB.txt.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 

/*MF2MOD Modifier File */

COPY INTO test_MF2MOD_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 MODIFIER_CODE,
    t.$2 MODIFIER_DESCRIPTION,
    t.$3 RESERVE,
    t.$4 TRANSACTION_CODE,
    to_date(t.$5,'YYYYMMDD') LAST_CHANGE_DATE
    
  from @medispan/mdfv2/MF2MOD.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 

--list @medispan/mdfv2
/*MF2NAME Drug Name File */

 COPY INTO test_MF2NAME_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 DRUG_DESCRIPTOR_ID,
    t.$2 DRUG_NAME,
    t.$3 ROUTE_OF_ADMINISTRATION,
    t.$4 DOSAGE_FORM,
    t.$5 STRENGTH,
    t.$6 STRENGTH_UNIT_OF_MEASURE,
    t.$7 BIOEQUIVALENCE_CODE,
    t.$8 CONTROLLED_SUBSTANCE_CODE,
    t.$9 EFFICACY_CODE,
    t.$10 LEGEND_INDICATOR_CODE,
    t.$11 MULTI_SOURCE_CODE,
    t.$12 BRAND_NAME_CODE,
    t.$13 NAME_SOURCE_CODE,
    t.$14 GENERIC_PRODUCT_IDENTIFIER,
    t.$15 KDC,
    t.$16 NEW_DRUG_DESCRIPTOR_IDENTIFIER,
    t.$17 SCREENABLE_FLAG,
    t.$18 KDC_FLAG,
    t.$19 LOCAL_SYSTEMIC_FLAG,
    t.$20 MAINTENANCE_DRUG_CODE,
    t.$21 FORM_TYPE_CODE,
    t.$22 INTERNAL_EXTERNAL_CODE,
    t.$23 SINGLE_COMBINATION_CODE,
    t.$24 REPRESENTATIVE_GPI_FLAG,
    t.$25 REPRESENTATIVE_KDC_FLAG,
    t.$26 RESERVE,
    t.$27 TRANSACTION_CODE,
    to_date(t.$28,'YYYYMMDD') LAST_CHANGE_DATE
      from @medispan/mdfv2/MF2NAME.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 

/*MF2PRC NDC Price File */ --need to validate prices

COPY INTO test_MF2PRC_{datetime.date.today().strftime("%Y%m%d")} FROM 
(
  select 
    t.$1 NDC_UPC_HRI,
    t.$2 PRICE_CODE,
    to_date(t.$3,'YYYYMMDD') PRICE_EFFECTIVE_DATE,
    cast(left(t.$4,5)||'.'||right(t.$4,6) as number) unit_price,--strange
    cast(left(t.$5,8)||'.'||right(t.$5,5) as number) EXTENDED_UNIT_PRICE,
    cast(left(t.$6,8)||'.'||right(t.$6,2) as number) PACKAGE_PRICE,--strange---
    t.$7 AWP_INDICATOR_CODE,
    t.$8 TRANSACTION_CODE,
    to_date(t.$9, 'YYYYMMDD') LAST_CHANGE_DATE
  from @medispan/mdfv2/MF2PRC.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;

/*MF2SEC Secondary Alternate ID File */
COPY INTO test_MF2SEC_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 EXTERNAL_DRUG_ID,
    t.$2 EXTERNAL_DRUG_ID_TYPE_CODE,
    t.$3 ALTERNATE_DRUG_ID,
    t.$4 ALTERNATE_DRUG_ID_FOMAT_CODE,
    t.$5 TRANSACTION_CODE,
    t.$6 RESERVE
  from @medispan/mdfv2/MF2SEC.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 


/*MF2SUM Summary File
* The length for records within the Summary File is not fixed, and may vary from row to row; however, it will not exceed the value noted in the table above. */
COPY INTO test_MF2SUM_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 RECORD_TYPE,
    t.$2 RESERVE_1,
    t.$3 SEQUENCE_NUMBER,
    t.$4 RESERVE_2,
    t.$5 COMMENT_MARKER,
    t.$6 DATA_COMMENT
  from @medispan/mdfv2/MF2SUM.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 


/*MF2TCGPI TC-GPI Name File*/

COPY INTO test_MF2TCGPI_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 TCGPI_ID,--TC-GPI Key
    t.$2 RECORD_TYPE,
    t.$3 TCGPI_NAME,
    t.$4 TC_LEVEL_CODE,
    t.$5 RESERVE,
    t.$6 TRANSACTION_CODE,
    to_date(t.$7, 'YYYYMMDD') LAST_CHANGE_DATE
  from @medispan/mdfv2/MF2TCGPI.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 

/*MF2VAL Validation/Translation File
 */
COPY INTO test_MF2VAL_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 FIELD_IDENTIFIER,
    t.$2 FIELD_VALUE,
    t.$3 LANGUAGE_CODE,
    t.$4 VALUE_DESCRIPTION,
    t.$5 VALUE_ABBREVIATION,
    t.$6 RESERVE
  from @medispan/mdfv2/MF2VAL.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
; 

--RTDRG
COPY INTO test_MF2RTDRG_{datetime.date.today().strftime("%Y%m%d")} from
( select 
 t.$1  concept_type
 ,t.$2 country_code 
 ,t.$3  concept_id
 ,t.$4  transaction_code
 ,t.$5  drug_name_id
 ,t.$6  route_id
 ,t.$7  status 
 ,t.$8  link_value 
 ,t.$9  link_date
 ,t.$10  reserve
 from @medispan/mdfv2/MF2RTDRG.gz t
 )
 ON_ERROR = 'ABORT_STATEMENT'

;


COPY INTO test_MF2DESC_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 concept_type,
    t.$2 country_code,
    t.$3 concept_id,
    t.$4 type_code,
    t.$5 transaction_code,
    t.$6 description,
    t.$7 reserve
  from @medispan/mdfv2/MF2DESC.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'

;
---MF2STR and MF2IDRG ADDED 6/10/2020 --

 
 --AL: 
 /*NDC Modifier File*/   
 COPY INTO test_mf2str_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 ingredient_identifier,
    t.$2 reserve_1,
    t.$3 transaction_cd,
    t.$4 ingredient_drug_id,
    t.$5 ingredient_strength_value,
    t.$6 ingredient_strength_uom_combined,
    t.$7 ingredient_strength_uom_individual,
    t.$8 volume_value, 
    t.$9 volume_uom,
    t.$10 reserve_2
      from @medispan/mdfv2/MF2STR.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;   
  --AL: 
 /*NDC Modifier File*/   
 COPY INTO test_MF2IDRG_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 ingredient_identifier,
    t.$2 transaction_cd,
    t.$3 cas_number,
    t.$4 knowledge_base_code_7,
    t.$5 reserve_1,
    t.$6 ingredient_drug_name,
    t.$7 generic_id,
    t.$8 reserve_2
      from @medispan/mdfv2/MF2IDRG.gz t
  )
ON_ERROR = 'ABORT_STATEMENT';
--PURGE = TRUE

---Added MF2SET and MF2INGS 6/10/2020

 
 --AL: 
 /*NDC Modifier File*/   
 COPY INTO test_mf2set_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 concept_type,
    t.$2 country_code,
    t.$3 concept_id, 
    t.$4 ingredient_set_id,
    t.$5 transaction_cd,
    t.$6 representative_set_indicator,
    t.$7 reserve
          from @medispan/mdfv2/MF2SET.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;   

 
  --AL: 
 /*NDC Modifier File*/   
 COPY INTO test_mf2ings_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 ingredient_set_id,
    t.$2 ingredient_identifier,
    t.$3 active_inactive_ingredient_flag,
    t.$4 transaction_cd,
    t.$5 reserve
      from @medispan/mdfv2/MF2INGS.gz t
  )
ON_ERROR = 'ABORT_STATEMENT';
--PURGE = TRUE

---Added MF2DRG 06/10/2020

 
 --AL: 
 /*NDC Modifier File*/   
 COPY INTO test_mf2drg_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 concept_type,
    t.$2 country_code,
    t.$3 concept_id, 
    t.$4 transaction_cd,
    t.$5 routed_drug_id,
    t.$6 dose_form_id,
    t.$7 strength,
    t.$8 strength_uom,
    t.$9 name_source,
    t.$10 device_flag,
    t.$11 staus,
    t.$12 link_value,
    t.$13 link_date,
    t.$14 routed_drug_form_id,
    t.$15 drug_dose_form_id,
    t.$16 strength_strength_uom_id,
    t.$17 reserve 
          from @medispan/mdfv2/MF2DRG.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;   

----added MF2DRGNM 06112020

 --AL: 
 /*NDC Modifier File*/   
 COPY INTO test_mf2drgnm_{datetime.date.today().strftime("%Y%m%d")} from
  (
  select 
    t.$1 concept_type,
    t.$2 country_code,
    t.$3 concept_id, 
    t.$4 transaction_cd,
    t.$5 name_type,
    t.$6 status,
    t.$7 link_value,
    t.$8 link_date,
    t.$9 reserve 
          from @medispan/mdfv2/MF2DRGNM.gz t
  )
ON_ERROR = 'ABORT_STATEMENT'
--PURGE = TRUE
;   

-----These are slightly different because the source files are delimited by length, so for these two, you have to handle them slightly differently



COPY INTO test_MCMNAME_STAGE from
  (
  select 
    t.$1 STAGE_COL
  from @medispan/mcm/MCMNAME.gz t
  )
ON_ERROR = 'ABORT_STATEMENT';

INSERT INTO test_MCMNAME_{datetime.date.today().strftime("%Y%m%d")} 
select 
    left(stage_col, 7) MEDICAL_CONDITION_CODE,
    substring(stage_col, 8, 2) COUNTRY_CODE,
    substring(stage_col, 10, 2) LANGUAGE_CODE,
    substring(stage_col, 12, 2) NAME_TYPE_CODE,
    trim(substring(stage_col, 14, 58)) MEDICAL_CONDITION_TYPE,
    trim(substring(stage_col, 72, 24)) RESERVE,
    substring(stage_col, 96, 1) TRANSACTION_CODE
from test_MCMNAME_STAGE;


--INDGIND



COPY INTO test_INDGIND_STAGE from
  (
  select 
    t.$1 STAGE_COL
  from @medispan/ind/INDGIND.gz t
  )
ON_ERROR = 'ABORT_STATEMENT';

INSERT INTO test_INDGIND_{datetime.date.today().strftime("%Y%m%d")} 

select
    left(stage_col, 14) GPI,
    trim(substring(stage_col, 15, 4)) RESERVE_1, 
    trim(substring(stage_col, 19, 7)) MED_COND_RESTRICTION_CODE,
    trim(substring(stage_col, 26, 7)) IND_MED_COND_CODE,
    trim(substring(stage_col, 33, 7)) MICROORG_CODE,
    trim(substring(stage_col, 40, 2)) ROLE_OF_THERAPY_CODE,
    trim(substring(stage_col, 42, 2)) OUTCOME_CODE,
    trim(substring(stage_col, 44, 2)) TREATMENT_RANK_CODE,
    trim(substring(stage_col, 46, 2)) ACCEPTABLE_LEVEL,
    trim(substring(stage_col, 48, 1)) PROXY_CODE,
    trim(substring(stage_col, 49, 1)) PROXY_ONLY,
    trim(substring(stage_col, 50, 25)) RESERVE_2,
    trim(substring(stage_col, 75, 1)) TRANSACTION_CODE
from test_INDGIND_STAGE;

'''


sql_file = open("medispan_copyinto.sql", "w")
sql_file.write(sql)
sql_file.close()