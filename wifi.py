import os
if __name__=="__main__":
    with open("wifi.txt",'w') as f:
        for i in range(0,99999999):
            password = str(i).zfill(8)
            f.write(password + "\n")