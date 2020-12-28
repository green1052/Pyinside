import protocol, json

URL = json.load(open('./link/link.json', 'r')) # ./link/link.json

def read(gall_id, article_no, page=1):
    body = {
        "app_id": protocol.app_id,
        "id": gall_id,
        "no": article_no,
        "re_page": page
    }

    res = protocol.get(URL["comment"]["read"], body)
    return res.json()

def write(gall_id, article_no, nickname, password, memo):
    body = {
        "id": gall_id,
        "no": article_no,
        "app_id": protocol.app_id,
        "mode": "com_write",
        "client_token": protocol.token,
        "comment_memo": memo,
        "comment_nick": nickname,
        "comment_pw": password
    }

    res = protocol.post(URL["comment"]["write"], body)
    return res.json()
