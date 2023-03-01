import requests

resp = requests.post(
    "https://www.google.com/recaptcha/api/siteverify",
    data={
        "secret": "6Le-2MMkAAAAALofmcnS8hQgpf1zViHV1M7C2iVu",
        "response": "03AFY_a8UzPEmeEW1yKUUqnAUs5gYZTBdat-TIIuy_H4TxAz32hw8iInmoD99_Jlh7m11lb2SLjN2OziBf398N8ZPB6dHJ1r9sTH38viMm8c8hGmWKzmIabmfMJvoKPTeIITbGvt4xNvCa0OT9eKdDSKsYNxU_Ml6iA97Ufq6KWmPX0XCtgU5PBoj7rd_V9BiST-2zuFOtJE6GIqMEtbWCrLd4vreTcO-PMwHwezmc831RqMbfRkuYTU67nof7S1yrhGSyxneh-upeY2ufDdNWfl0LFB3iOvF1O5rQeNZAFUNT1QteRi8QT5CJUFsDDNkK7pp1BijGmVqUzezTZejy12bwYTG896TYfcWD3gAiMV2yMWMxjO5Gl_sgk_9VO9K0v2lndU8Mf4ewDfSWSJQVrpk7JhizR68Ba2UaMNSJLc7qSyrIikEKfWWBs9fF02LIFNWFC5IN0SQGJ4bD5eJ-RORcL-NvEjqN2BOmHFiMOv4lWxe2-56D3SZdTmBO3mpMepeSU-QaqCYxB8hezZIy-ekuUt6UgbL8meOwBpRJg5-4tel_B5ie-ARx1WCst0Xd6RvqZZTiWaiXrGEp1ZXojT6_HFuYu_JttQ"
    }
)

print(resp.json())