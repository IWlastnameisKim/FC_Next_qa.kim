import requests
import json

url = "https://kauth.kakao.com/oauth/token"



class Kakao():
    def __init__(self):
        self.app_key = "40a2e62b0f1bf00443d4199cc4617678"
        with open("kakao_token.json", "r") as fp :
            self.tokens = json.load(fp)
            self.refresh_token()

    def refresh_token(self):
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": self.app_key,
            "redirect_uri": "https://staging.fastcampus.co.kr",
            "refesh_token": self.tokens['refresh_koken']
        }

        response = requests.post(url, data=data)
        result = response.json()

        # 토큰을 파일로 저장하기
        if 'access_token' in result:
            self.tokens['access_token'] = result['access_token']

            if 'refresh_token' in result :
                self.tokens['refresh_token'] = result['refresh_token']
            else : pass
            with open("kakao_token.json", "w") as fp :
                json.dump((self.tokens, fp))

    def send_to_kakao(self, text):
        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        headers = {"Authorization": "Bearer " + self.tokens['access_token']}
        content = {
            "object_type": "text",
            "text": text,
            "link": {"mobile_web_url": "http://m.naver.com"}
        }

        data = {"template_object": json.dumps(content)}
        res = requests.post(url, headers=headers, data=data)

        ## 에러메시지 확인
        res.json()

def __init__(self) :
    self.kakao = Kakao()
    self.kakao.send_to_kakao(
        text="테스트"
    )