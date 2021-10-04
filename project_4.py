import email
import imaplib
import os
import mimetypes
import pdfkit
from PyPDF2 import PdfFileMerger

#username & password of your gmail account
username='XXXXX@gmail.com'
password='*****'

def fetch_email(given_date):

    mail=imaplib.IMAP4_SSL("imap.gmail.com")
    # logging in
    mail.login(username,password)
    # selecting inbox
    mail.select("inbox")
    result,data=mail.uid('search',None,"ALL")
    inbox_items=data[0].split()
    for item in inbox_items:
        result2, email_data=mail.uid('fetch',item,'(RFC822)')
        raw_email=email_data[0][1].decode("utf-8")
        email_msg=email.message_from_string(raw_email)
        to_=email_msg['To']
        from_=email_msg['from']
        subject_=email_msg['subject']
        date_=email_msg['date']
        print(date_)
        # searching for particular mail using given date from input
        if given_date in date_:
            print("Mail is identified")
            counter=1
            save_path=os.path.join(os.getcwd(),"emails")
            date1=date_+".pdf" 
            if not os.path.exists(save_path):
                os.makedirs(save_path)
                #if email_msg.get_content_maintype() == 'multipart': 
            for part in email_msg.walk():
                print ("inside for loop")
                if part.get_content_maintype() == 'multipart':
                    print ("inside 1st if")
                    continue 
                """if part.get('Content-Disposition') is None:
                    print ("inside 2nd if")
                    continue"""
                print(part.get_content_type())
                filename=part.get_filename()
                print(filename)
                #downloading attachments of email in currect working directory
                if filename is not None: 
                   sv_path=os.path.join(save_path,filename)
                   if not os.path.isfile(sv_path): 
                      print (sv_path) 
                      fp = open(sv_path, 'wb') 
                      fp.write(part.get_payload(decode=True))
                      fp.close()
                      f1=open(os.path.join(save_path,from_+""+date1),'a')
                      f1.write("Attachment:"+filename+"\n")   
                      f1.close() 
                else:
                   flag=0
                   content_type=part.get_content_type()
                   """if 'plain' in content_type:
                      f1=open(os.path.join(save_path,date1),'a')
                      #print(part.get_payload())
                      f1.write(part.get_payload()) 
                      f1.close()
                      flag=1 """
                   #downloading email content(plain/html) as pdf   
                   if 'text' in content_type:
                        if flag==0 :
                         print("inside elif")
                         sample_file="sample.html"
                         with open(os.path.join(save_path,sample_file),'wb') as fp:
                            fp.write(part.get_payload(decode=True))
                         options = {'enable-local-file-access': None} 
                         pdfkit.from_file(os.path.join(save_path,sample_file),os.path.join(save_path,from_+""+date1),options=options)
                         os.remove('/Users/muthubharathi/mini_projects_python/emails/sample.html')
            mail.close()
            mail.logout()           
            print("the email is successfully fetched!!")
            return
    print("The details given are not matched!")
    mail.close()
    mail.logout()

given_date=input("Enter the the of the you want to fetch")
#given_subject=input("Enter some words in the subject")
#given_from=input("Enter the email address of the sender")
counter=0
fetch_email(given_date)


  













    








    
    

    
