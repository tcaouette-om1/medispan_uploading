import os, shlex, subprocess
from subprocess import call
# need to build main controller main()
# this file is used to connect to snowsql client and run the files denoted by -f flag. these directories need to be updated for each new user.
# change location of the files before running. check the files for complete setup.
# files being passed - put_file.sql, medispan_create_tables.sql, medispan_copyinto.sql
# scripts being used - medispan_use_db_create_tables.py, medispan_copyinto.py
os.system('''snowsql -c my_conn -f /Users/tobiascaouette/Documents/put_file.sql  -f /Users/tobiascaouette/Documents/medispan_create_tables.sql -f /Users/tobiascaouette/Documents/medispan_copyinto.sql -f /Users/tobiascaouette/Documents/medispan_qc.sql''')

#os.system('''snowsql -c my_conn''')
    

    




