import numpy as np

x=np.array(([1,133,111600],[1,111,104400],[1,129,97200],[1,117,79200],[1,130,126000],[1,154,108000],[1,149,147600],[1,90,104400],[1,118,169200],[1,131,75600],[1,141,133200],[1,119,133200],[1,115,176400],[1,102,180000],[1,129,133200],[1,144,147600],[1,153,122400],[1,96,158400],[1,104,165600],[1,156,104400],[1,119,136800],[1,125,115200],[1,130,115200],[1,123,151200],[1,128,97200],[1,97,122400],[1,124,208800],[1,138,93600],[1,137,115200],[1,129,118800],[1,97,129600],[1,133,100800],[1,145,147600],[1,149,126000],[1,122,108000],[1,120,194400],[1,128,176400],[1,117,172800]))

y=np.array(([1197576,1053648,1124172,987144,1283616,1295100,1407444,922416,1272012,1064856,1269960,1064760,1207488,1186284,1231464,1296708,13020648,1102704,
1184316,1326360,1162596,1195116,1134768,1269024,1118688,904776,1357644,1027308,1181976,1221636,1060452,1229028,1406196,1293936,1056384,1415316,1338060,
1457400]))

b=np.linalg.inv(x.transpose().dot(x)).dot(x.transpose()).dot(y)

print(b)

#actual coefficients:[41008.840 5931.850 3.136]
