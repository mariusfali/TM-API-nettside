def get_live_token():
    with open("tokens.txt") as f:
        data = f.readlines()
        return str(data[0]).strip()

def get_core_token():
    with open("tokens.txt") as f:
        data = f.readlines()
        return str(data[1]).strip()

def get_oauth_token():
    with open("tokens.txt") as f:
        data = f.readlines()
        return str(data[2]).strip()
