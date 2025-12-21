import json
import requests

def get_request(url,auth):
    response = requests.get(url=url,auth=auth)
    return response.json()

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_reques(url,auth,headers,payload,in_json):
    patch_request = requests.patch(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return patch_request.json()
    return patch_request

def put_request(url,auth,headers,payload,in_json):
    put_request = requests.put(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return put_request.json()
    return put_request

def delete_request(url,auth,headers,in_json):
    delete_request = requests.delete(url=url,auth=auth,headers=headers)
    if in_json is True:
        return delete_request.json()
    return delete_request


