import email , imaplib, os

imap = imaplib.IMAP4_SSL('imap.gmail.com')
id = 'qa.kim@day1company.co.kr'
pw = 'irzdtfdyvaqcxuvo'
imap.login(id, pw)
imap.select("INBOX")
# 만약 특정 발신 메일만 선택하고 싶다면 'ALL' 대신에 '(FROM "xxxxx@naver.com")' 입력
status, messages = imap.uid('search', None, '(FROM "noreply@fastcampus.co.kr")')

messages = messages[0].split()
recent_email = messages[-1]
latest_email = messages[-10:]

res, msg = imap.uid('fetch', recent_email, "(RFC822)")

# 사람이 읽을 수 있는 없는 상태의 이메일
raw = msg[0][1]

# 사람이 읽을 수 있는 형태로 변환
raw_readable = msg[0][1].decode('utf-8')

import email

# raw_readable에서 원하는 부분만 파싱하기 위해 email 모듈을 이용해 변환
email_message = email.message_from_string(raw_readable)

from email.header import decode_header, make_header

# 보낸사람
fr = make_header(decode_header(email_message.get('From')))
print(fr)

# 메일 제목
subject = make_header(decode_header(email_message.get('Subject')))
print(subject)

# 메일 내용
if email_message.is_multipart():
    for part in email_message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
else:
    body = email_message.get_payload(decode=True)

body = body.decode('utf-8')
print(body)