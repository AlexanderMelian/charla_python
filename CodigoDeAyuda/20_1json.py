results=[
    {
        "final": True,
        "alternatives":[
            {
                "transcript": "Texto texto texto/// ",
                "confidence": 0.83
            }
        ]
    },
    {
        "final": True,
        "alternatives": [
            {
                "transcript": "Texto texto texto///",
                "confidence": 0.83
            }
        ]
    }
]

print(results[1]["alternatives"][0]["confidence"])#0.83