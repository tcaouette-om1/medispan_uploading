




create or replace table test_mf2ndcm_20220510
 (ndc_upc_hri varchar2(11) not null
 ,modifier_code varchar2(6) not null
 ,reserve varchar2(6) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;


create or replace table test_mf2sum_20220510
 (record_type varchar2(3) null
 ,reserve_1 varchar2(1) null
 ,sequence_number number(3,0) null
 ,reserve_2 varchar2(1) null
 ,comment_marker varchar2(1) null
 ,data_comment varchar2(87) null
 )
;
create or replace table test_mf2ndc_20220510
 (ndc_upc_hri varchar2(11) not null
 ,drug_descriptor_id varchar2(6) null
 ,tee_code varchar2(2) null
 ,dea_class_code varchar2(1) null
 ,desi_code varchar2(1) null
 ,rx_otc_indicator_code varchar2(1) null
 ,generic_product_pack_code varchar2(8) null
 ,old_ndc_upc_hri varchar2(11) null
 ,new_ndc_upc_hri varchar2(11) null
 ,repackaged_code varchar2(1) null
 ,id_number_format_code varchar2(1) null
 ,third_party_restriction_code varchar2(1) null
 ,kdc varchar2(10) null
 ,kdc_flag varchar2(1) null
 ,medispan_labeler_id varchar2(5) null
 ,multi_source_code varchar2(1) null
 ,name_type_code varchar2(1) null
 ,item_status_flag varchar2(1) null
 ,innerpack_code varchar2(1) null
 ,clinic_pack_code varchar2(1) null
 ,reserve1 varchar2(2) null
 ,ppg_indicator_code varchar2(1) null
 ,hfpg_indicatory_code varchar2(1) null
 ,dispensing_unit_code varchar2(1) null
 ,dollar_rank_code varchar2(1) null
 ,rx_rank_code varchar2(1) null
 ,storage_condition_code varchar2(1) null
 ,limited_distribution_code varchar2(2) null
 ,old_effective_date varchar2(10) null
 ,new_effective_date varchar2(10) null
 ,next_smaller_ndc_suffix varchar2(2) null
 ,next_larger_ndc_suffix varchar2(2) null
 ,reserve2 varchar2(13) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;

create or replace table test_mf2lab_20220510
 (medispan_labeler_id varchar2(5) not null
 ,manufacturer_name varchar2(30) null
 ,manufacturer_abbr_name varchar2(10) null
 ,labeler_type_code varchar2(1) null
 ,reserve varchar2(9) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;

create or replace table test_mf2tcgpi_20220510
 (tcgpi_id varchar2(14) not null
 ,record_type varchar2(1) not null
 ,tcgpi_name varchar2(60) null
 ,tc_level_code varchar2(2) null
 ,reserve varchar2(10) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;

create or replace table test_mf2dict_20220510
 (field_identifier varchar2(4) not null
 ,field_description varchar2(35) null
 ,field_type varchar2(1) null
 ,field_length number(3) null
 ,implied_decimal_flag varchar2(1) null
 ,decimal_places number(2) null
 ,field_validation_flag varchar2(1) null
 ,field_abbreviation_flag varchar2(1) null
 ,reserve varchar2(16) null
 )
;

create or replace table test_mf2val_20220510
 (field_identifier varchar2(4) null
 ,field_value varchar2(15) null
 ,language_code varchar2(2) null--char
 ,value_description varchar2(40) null
 ,value_abbreviation varchar2(15) null
 ,reserve varchar2(20) null
 )
;

create or replace table test_mf2sec_20220510
 (external_drug_id varchar2(20) not null
 ,external_drug_id_type_code varchar2(1) not null
 ,alternate_drug_id varchar2(20) not null
 ,alternate_drug_id_fomat_code varchar2(1) null
 ,transaction_code varchar2(1) null
 ,reserve varchar2(21) null
 )
;

create or replace table test_mf2prc_20220510
 (ndc_upc_hri varchar2(11) not null
 ,price_code varchar2(1) not null
 ,price_effective_date varchar2(10) not null
 ,unit_price number(11,6) null
 ,extended_unit_price number(13,5) null
 ,package_price number(10,2) null
 ,awp_indicator_code varchar2(1) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;

create or replace table test_mf2mod_20220510
 (modifier_code varchar2(6) not null
 ,modifier_description varchar2(25) null
 ,reserve varchar2(24) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;

create or replace table test_mf2err_20220510
 (key_identifier varchar2(1) not null
 ,unique_key varchar2(19) not null
 ,data_element_code varchar2(4) not null
 ,data_element_length number(3) default 3 null
 ,reserve varchar2(5) null
 )
;

create or replace table test_mf2gppc_20220510
 (generic_product_pack_code varchar2(8) not null
 ,package_size number null
 ,package_size_uom varchar2(2) null
 ,package_quantity number null
 ,unit_dose_unit_use_pkg_code varchar2(1) null
 ,package_description_code varchar2(2) null
 ,generic_product_identifier varchar2(14) null
 ,reserve varchar2(14) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;

create or replace table test_mf2name_20220510
 (drug_descriptor_id varchar2(6) not null--char
 ,drug_name varchar2(30) null
 ,route_of_administration varchar2(2) null
 ,dosage_form varchar2(4) null
 ,strength varchar2(15) null
 ,strength_unit_of_measure varchar2(10) null
 ,bioequivalence_code varchar2(1) null
 ,controlled_substance_code varchar2(1) null
 ,efficacy_code varchar2(1) null
 ,legend_indicator_code varchar2(1) null
 ,multi_source_code varchar2(1) null
 ,brand_name_code varchar2(1) null
 ,name_source_code varchar2(1) null
 ,generic_product_identifier varchar2(14) null
 ,kdc varchar2(10) null--char
 ,new_drug_descriptor_identifier varchar2(6) null--char
 ,screenable_flag varchar2(1) null
 ,kdc_flag varchar2(1) null
 ,local_systemic_flag varchar2(1) null
 ,maintenance_drug_code varchar2(1) null
 ,form_type_code varchar2(1) null
 ,internal_external_code varchar2(1) null
 ,single_combination_code varchar2(1) null
 ,representative_gpi_flag varchar2(1) null
 ,representative_kdc_flag varchar2(1) null
 ,reserve varchar2(6) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;

create or replace table test_mf2gpr_20220510
 (generic_product_pack_code varchar2(8) not null
 ,gppc_price_code varchar2(1) not null
 ,effective_date varchar2(10) not null
 ,unit_price number(11,6) null
 ,reserve varchar2(27) null
 ,transaction_code varchar2(1) null
 ,last_change_date varchar2(10) null
 )
;


create or replace table test_MF2RTDRG_20220510 
(concept_type integer
 ,country_code integer
 ,concept_id integer 
 ,transaction_code varchar(1)
 ,drug_name_id integer
 ,route_id integer
 ,status varchar(1)
 ,link_value integer
 ,link_date varchar(10)
 ,reserve varchar(28)
 )
;
create OR REPLACE table test_MF2DESC_20220510 
 (concept_type integer not null
 ,country_code integer not null
 ,concept_id integer not null
 ,type_code integer not null
 ,transaction_code varchar(1) null
 ,description varchar(250) null
 ,reserve varchar(67) null
 )
; 
create or replace table test_mf2str_20220510
 (ingredient_identifier varchar2(10) 
 ,reserve_1 varchar2(2) 
 ,transaction_cd varchar2(1) 
 ,ingredient_drug_id varchar2(10) 
 ,ingredient_strength_value varchar2(13) 
 ,ingredient_strength_uom_combined varchar2(11) 
 ,ingredient_strength_uom_individual varchar2(11) 
 ,volume_value varchar2(13) 
 ,volume_uom varchar2(11)
 ,reserve_2 varchar2(30) 
 )
 ;
 
 
 create or replace table test_mf2idrg_20220510
 (ingredient_drug_id varchar2(10)  
 ,transaction_cd varchar2(1) 
 ,cas_number varchar2(20)
 ,knowledge_base_code_7 varchar2(10)
 ,reserve_1 varchar2(20)
 ,ingredient_drug_name varchar2(60) 
 ,generic_id varchar2(10) 
 ,reserve_2 varchar2(30) 
 )
 ;
  
  create or replace table test_mf2set_20220510
 (concept_type varchar2(5) 
 ,counry_code integer
 ,concept_id varchar2(14) 
 ,ingredient_set_id varchar2(10) 
 ,transaction_cd varchar2(1) 
 ,representative_set_indicator varchar2(1) 
 ,reserve varchar2(25) 
 )
 ;
 create or replace table test_mf2ings_20220510
 (ingredient_set_id varchar2(10)  
 ,ingredient_identifier varchar2(10) 
 ,active_inactive_ingredient_flag varchar2(1)
 ,transaction_cd varchar2(1)
 ,reserve varchar2(20)
  
 )
 ;
create or replace table test_mf2drg_20220510
 (concept_type varchar2(5) 
 ,country_code integer
 ,concept_id integer 
 ,transaction_cd varchar2(1) 
 ,routed_drug_id varchar2(10)
 ,dose_form_id varchar2(5) 
 ,strength varchar2(15) 
 ,strength_uom varchar2(15)
 ,name_source varchar2(1)
 ,device_flag varchar2(1)
 ,staus varchar2(1)
 ,link_value varchar2(10)
 ,link_date varchar2(8)
 ,routed_drug_form_id varchar2(10)
 ,drug_dose_form_id varchar2(10)
 ,strength_strength_uom_id varchar2(10)
 ,reserve varchar2(30)
 
 )
 ;
 
 
create or replace table test_mf2drgnm_20220510
 (concept_type varchar2(5) 
 ,country_code integer
 ,concept_id integer 
 ,transaction_cd varchar2(1) 
 ,name_type varchar2(1)
 ,status varchar2(1) 
 ,link_value varchar2(10)
 ,link_date varchar2(8)
 ,reserve varchar2(30)
 
 )
 ;
 
  

 
 


CREATE OR REPLACE TABLE test_MCMNAME_20220510
 (
    MEDICAL_CONDITION_CODE VARCHAR(7), 
    COUNTRY_CODE VARCHAR(2), 
    LANGUAGE_CODE VARCHAR(2), 
    NAME_TYPE_CODE VARCHAR(2), 
    MEDICAL_CONDITION_NAME VARCHAR(58), 
    RESERVE VARCHAR(24), 
    TRANSACTION_CODE VARCHAR(1)
 );
 
 create or replace table test_indgind_20220510
 (GPI varchar2(25),
RESERVE_1 varchar2(4),
MED_COND_RESTRICTION_CODE varchar2(7),
IND_MED_COND_CODE varchar2(7),
MICROORG_CODE varchar2(7),
ROLE_OF_THERAPY_CODE varchar2(2),
OUTCOME_CODE varchar2(2),
TREATMENT_RANK_CODE varchar2(2),
ACCEPTANCE_LEVEL varchar2(2),
PROXY_CODE varchar2(1),
PROXY_ONLY varchar2(1),
RESERVE_2 varchar2(25),
TRANSACTION_CODE varchar2(1))
 
 ;

