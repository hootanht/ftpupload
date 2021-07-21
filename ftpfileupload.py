from ftplib import FTP, FTP_TLS
host = input('Enter host address : ')
session = FTP(host)
session.encoding='utf-8'
userName = input("Enter your username : ")
password = input("Enter your password : ")
session.login(userName,password)
fileName = input('Enter your filename to upload : ')
file = open(fileName,'rb')                 
session.storbinary('STOR '+ fileName, file)     
file.close()                                    
session.quit()
print('file upload Complete!')