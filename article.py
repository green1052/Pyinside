from urllib.parse import quote

import protocol
from url import URL


def read(gall_id, article_no):
    body = {
        "app_id": protocol.app_id,
        "id": gall_id,
        "no": article_no
    }

    res = protocol.get(URL["article"]["read"], body)
    return res.json()


# 작동 안함
def write(gall_id, subject, memo, name, password):
    tempMemo = memo
    tempMemo.replace(" ", "&nbsp;", len(tempMemo))
    tempMemo.replace("<", "&lt;", len(tempMemo))
    tempMemo.replace(">", "&gt;", len(tempMemo))
    tempMemo.replace("&", "&amp;", len(tempMemo))
    tempMemo.replace('"', "&quot;", len(tempMemo))
    tempMemo.replace("\n", "<br>", len(tempMemo))
    tempMemo.replace("\t", "&nbsp; &nbsp; &nbsp;", len(tempMemo))

    body = {
        "id": gall_id,
        "app_id": protocol.app_id,
        "mode": "write",
        "client_token": protocol.token,
        "subject": quote(subject),
        "memo_block[0]": quote(f"<div>{quote(tempMemo)}</div>"),
        "name": quote(name),
        "password": quote(password)
    }

    res = protocol.post(URL["article"]["write"], body)
    return res.json()


def search(gall_id, context, page=1):
    body = {
        "app_id": protocol.app_id,
        "id": gall_id,
        "page": page,
        "s_type": "memo",
        "serVal": context
    }

    res = protocol.get(URL["article"]["search"], body)
    return res.json()
