# imap을 통해 읽어들인다.
import imaplib
import email
from email.parser import Parser
import email.policy
#
# mhtml = Path(r"mhtml.mhtm").read_text(encoding="utf-8")
# e = Parser(policy=email.policy.default).parsestr(mhtml)

# 이메일 헤더에서 제목 가져오기 함수
def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode


# 네이버 imap 접속주소로 접속하기
imap = imaplib.IMAP4_SSL('imap.gmail.com')
id = 'qa.kim@day1company.co.kr'
pw = 'irzdtfdyvaqcxuvo'
imap.login(id, pw)

# 최근 3개의 이메일 가져오기
imap.select('INBOX')
stagus, messages = imap.uid('search', None,'(FROM "noreply@fastcampus.co.kr")')
messages = messages[0].split()
recent_email = messages[-1]
last_email = messages[-100:]

res, msg = imap.uid('fetch', recent_email, "(RFC822)")
raw = msg[0][1]
raw_readable = msg[0][1].decode('utf-8')


email_message = email.message_from_string(raw_readable)

if email_message.is_multipart():
    for part in email_message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True).decode()  # decode
            break
else:
    body = email_message.get_payload(decode=True).decode()



print(body)


# 3개의 이메일에서 정보 가져오기
# for mail in reversed(last_email):
#     result, data = imap.uid('fetch', mail, '(RFC822)')
#     raw_email = data[0][1]
#     email_message = email.message_from_bytes(raw_email, policy=policy.default)
#
#     print('=' * 70)
#     print('FROM', email_message['From'])
#     print('SENDER', email_message['Sender'])
#     print('TO', email_message['To'])
#     print('DATE', email_message['Date'])
#     # 제목 가져오기
#     subject, encode = find_encoding_info(email_message['Subject'])
#     print('SUBJECT : ', subject)
#     print('+' * 80)
#     raw_readable = raw_email.decode('utf-8')
#
#
#     # 본문 내용 출력하기
#     message = ''
#     email_message = email.message_from_string((raw_readable))
#     if email_message.is_multipart():
#         for part in email_message.get_payload():
#             cdispo = str(part.get('Content-Disposition'))
#             if part.get_content_type() == 'text/plain'and 'attachemnt' not in cdispo :
#                 bytes = part.get_payload(decode=True)
#                 encode = part.get_content_charset()
#                 message = message + str(bytes, encode)
#     print(message)
#     print('=' * 80)

# imap.close()
# imap.logout()