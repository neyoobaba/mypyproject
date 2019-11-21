# from psycopg2 import pool
# import psycopg2
#
# # def connect():
# #     return  psycopg2.connect(user='postgres', password='qfalinc5', database='mylearning',
# #                               host='localhost')
#
# connection_pool = pool.SimpleConnectionPool(1, 10, database='"mylearning', user="postgres", password="qfalinc5", host="localhost")

def get_data:
    command = "[AOSTAT;ZA;ZB;ZC;ZD;ZE;ZF;ZG;ZH;ZI;ZJ;ZK;ZL;ZM;ZN;ZO;ZP;FS0;]"
    data = ProcessCommand(s, False, command, 2048, "STAT", "STAT", "STAT", verbose);
    startZD = GetTagString(data, "ZD")
    startZD = int(startZD, 16)
    starttime = time.time()
    lasttime = time.time()
    startZDtrans = 0
    who = options.host
    sample_interval = float(options.sample)
    while True:
        time.sleep(sample_interval)
        command = "[AOSTAT;ZA;ZB;ZC;ZD;ZE;ZF;ZG;ZH;ZI;ZJ;ZK;ZL;ZM;ZN;ZO;ZP;FS0;]"
        data = ProcessCommand(s, False, command, 2048, "STAT", "STAT", "STAT", verbose);
        endZD = GetTagString(data, "ZD")
        endZD = int(endZD, 16)
        ZD = endZD - startZD
        startZD  = endZD
        timeperiod = time.time() - lasttime
        elasped = time.time() - starttime
        lasttime = time.time()
        tps = ZD / elasped
        tps1=ZD/ timeperiod
        localtime =  time.strftime("%c" ,time.localtime())
        filename = "tpsfile" + ""

        #outfile = open('tpsfile.csv', options.mode);

        #data1 = "\r\n" + str(localtime) + "," + str(tps1) + "," + str(ZD)
        #outfile.write(data1);

        #outfile.close()
        print float(tps1)