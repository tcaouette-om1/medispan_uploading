COPY INTO test_MF2SUM_20220509 from
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
