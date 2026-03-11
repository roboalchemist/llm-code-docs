# Source: https://www.hammerdb.com/docs4.0/ch14s01.html

Title: 1. Generating Trace Files

URL Source: https://www.hammerdb.com/docs4.0/ch14s01.html

Markdown Content:
To begin converting Oracle trace file workloads with HammerDB the first step is to load an Oracle trace file under the File:Open menu option. Before doing this therefore an Oracle trace file must be generated using Oracle Event 10046. (There are numerous methods to generate Oracle trace files of which only event 10046, level 4 to capture bind variables is covered here). As an example the simplest method to start and stop the trace of a session interactively is as follows:

SQL> connect / as sysdba
Connected.
SQL> alter session set events '10046 trace name context forever, level 4'; 

Session altered.

SQL> select sysdate from dual;

SYSDATE
---------
10-APR-18

SQL> alter session set events '10046 trace name context off';

Session altered.

SQL> 

For more advanced use the creation of a logon trigger is recommended. This trigger can then be enabled or disabled to capture the trace information for a particular use. The example uses the user TPCC created for an Oracle HammerDB OLTP test.

create or replace trigger logon_trigger
after logon on database
begin
if (user = 'TPCC') then
execute immediate
'alter session set events ''10046 trace name context forever, level 4''';
end if;
end;
This will then create a tracefile automatically at logon.

SQL> connect tpcc/tpcc@RVDB1
Connected.
SQL> select sysdate from dual;

SYSDATE
---------
10-APR-18

The trigger must be created as SYS with SYSDBA privileges, if created by system the trigger will create successfully but fail on the user login. This event will produce a trace file in the diagnostic area specified for the database server. By default the file will be identifiable by ora_SPID.trc, however there are also methods that can be used to set the name of the trace file. Note that in a Shared Server environment (previously MTS) one users’ session may be distributed across numerous trace files as the user processes share multiple server processes. Therefore in this environment it is necessary to reassemble the trace file data before converting with the Oracle utility ‘trcsess’. A a raw trace file is shown below:

race file /home/oracle/app/oracle/diag/rdbms/rvdb1/RVDB1/trace/RVDB1_ora_13783.trc
Oracle Database 12c Enterprise Edition Release 12.1.0.2.0 - 64bit Production
With the Partitioning, OLAP, Advanced Analytics and Real Application Testing options
ORACLE_HOME = /home/oracle/app/oracle/product/12.1.0/dbhome_1
System name:Linux
Node name:raven
Release:4.1.12-61.1.23.el7uek.x86_64
Version:#2 SMP Tue Dec 20 16:59:23 PST 2016
Machine:x86_64
Instance name: RVDB1
Redo thread mounted by this instance: 1
Oracle process number: 72
Unix process pid: 13783, image: oracle@raven (TNS V1-V3)

*** 2018-04-10 14:35:39.821
*** SESSION ID:(4.48241) 2018-04-10 14:35:39.821
*** CLIENT ID:() 2018-04-10 14:35:39.821
*** SERVICE NAME:(SYS$USERS) 2018-04-10 14:35:39.821
*** MODULE NAME:(sqlplus@raven (TNS V1-V3)) 2018-04-10 14:35:39.821
*** CLIENT DRIVER:(SQL*PLUS) 2018-04-10 14:35:39.821
*** ACTION NAME:() 2018-04-10 14:35:39.821
 
CLOSE #140169830640712:c=0,e=6,dep=0,type=1,tim=530154237
=====================
PARSING IN CURSOR #140169830722080 len=24 dep=0 uid=0 oct=3 lid=0 tim=530194337 hv=2343063137 ad='97b9c9e8' sqlid='7h35uxf5uhmm1'
select sysdate from dual
END OF STMT
PARSE #140169830722080:c=3149,e=39623,p=0,cr=0,cu=0,mis=1,r=0,dep=0,og=1,plh=1388734953,tim=530194336
EXEC #140169830722080:c=0,e=21,p=0,cr=0,cu=0,mis=0,r=0,dep=0,og=1,plh=1388734953,tim=530194497
FETCH #140169830722080:c=0,e=16,p=0,cr=0,cu=0,mis=0,r=1,dep=0,og=1,plh=1388734953,tim=530194568
STAT #140169830722080 id=1 cnt=1 pid=0 pos=1 obj=0 op='FAST DUAL  (cr=0 pr=0 pw=0 time=0 us cost=2 size=0 card=1)'
FETCH #140169830722080:c=0,e=1,p=0,cr=0,cu=0,mis=0,r=0,dep=0,og=0,plh=1388734953,tim=530213687

*** 2018-04-10 14:36:07.973
CLOSE #140169830722080:c=539,e=34,dep=0,type=0,tim=558307025
=====================
PARSING IN CURSOR #140169830722080 len=55 dep=0 uid=0 oct=42 lid=0 tim=558307224 hv=2217940283 ad='0' sqlid='06nvwn223659v'
alter session set events '10046 trace name context off'
END OF STMT
PARSE #140169830722080:c=0,e=112,p=0,cr=0,cu=0,mis=0,r=0,dep=0,og=0,plh=0,tim=558307223
EXEC #140169830722080:c=0,e=214,p=0,cr=0,cu=0,mis=0,r=0,dep=0,og=0,plh=0,tim=558307510
For more information on the trace file format the document Note:39817.1 Subject “Interpreting Raw SQL_TRACE output “ available from My Oracle Support, however this knowledge is not essential as HammerDB can convert this raw format into a form that can be replayed.

**Figure 14.1.Doc 39817.1**

![Image 1: Doc 39817.1](https://www.hammerdb.com/docs4.0/resources/ch12-1.PNG)
