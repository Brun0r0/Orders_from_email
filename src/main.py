import email_reader
from dotenv import load_dotenv
import os


load_dotenv()

leitura = email_reader.FetchEmail(os.getenv("IMAP_SERVER"), os.getenv("IMAP_PORT"), os.getenv("EMAIL_USER"), os.getenv("KEY_CODE"))

emails = leitura.fetch_unread_messages()


for email in emails:
    arquivo = leitura.save_attachment(email)
    print(arquivo)

leitura.close_connection()