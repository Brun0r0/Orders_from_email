#Bibliotecas necessárias para importar os email por imap
from imaplib import IMAP4, IMAP4_SSL
import email
from email.header import decode_header
import os



class FetchEmail():

    connection = None
    error = None

    #To inicialize the fetch we have to connect
    def __init__(self, emailServer, emailPort, emailUser, emailKey):
        self.connection = IMAP4_SSL(emailServer, emailPort)
        self.connection.login(emailUser, emailKey)
        self.connection.select("INBOX")

    #Simple function to close connection
    def close_connection(self):
        self.connection.close()

    #We save de attachments on file -> /temp_pdfs
    def save_attachment(self, msg, download_folder= '../emailPDFOrder/temp_pdfs'):

        if not os.path.isdir(download_folder):
            os.makedirs(download_folder, exist_ok=True)

        att_path = 'No attachments'

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            att_path = os.path.join(download_folder, filename)

            if not os.path.isfile(att_path):
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

        return att_path
    
    #Realiza a busca por mensagens não lidas
    def fetch_unread_messages(self):
        status, messages = self.connection.search(None, "UNSEEN")

        emails = []
        if(status == 'OK'):
            for message in messages[0].split():
                try:
                    ret, data = self.connection.fetch(message, '(RFC822)')
                    text_email = data[0][1].decode('utf-8')
                except:
                    print('No new emails to read')
                    self.close_connection
                    exit()

                text_email = email.message_from_string(text_email)

                emails.append(text_email)

            return emails
        
        self.error = "Failed to retrieve emails"
        return emails

'''

#Realizar conexão por imap com as credenciais do .env
imap = IMAP4_SSL(os.getenv("IMAP_SERVER"), os.getenv("IMAP_PORT"), timeout=None)

imap.login(os.getenv("EMAIL_USER"), os.getenv("KEY_CODE"))

#Realizar a busca por emails não lidos
mailbox = "INBOX"
imap.select(mailbox)

while(1):
    status, message_ids = imap.search(None, "UNSEEN")

    if status == "OK":
        message_ids = message_ids[0].split()

        for message_id in message_ids:
            status, message_data = imap.fetch(message_id, "(RFC822)")
            if status == "OK":
                message = email.message_from_bytes(message_data[0][1])
                subject, encoding = decode_header(message["subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")

                print(f"New email: {subject}")

'''