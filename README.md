# FLASK API LTE ARFCN -> BAND INFO (FREQUENCY & NAME)

## Example of requests :
Request with ARFCN supported : 

  `curl http://localhost:5000/convert/arfcn=2750`

Answer :
  `{ "arfcn": 2750, "band": "2600", "band_name": "B7" }`
___
Request with ARFCN not supported : 

  `curl http://localhost:5000/convert/arfcn=8000`

Answer :
    `{ "arfcn": 8000, "error": "Band not found" }`
___
Request with ARFCN not in URI : 

  `curl http://localhost:5000/convert/arfcn=` 

Answer : 
    `{ "error": "ARFCN argument required" }`

## TODO :
- NR EARFCN -> NR BAND