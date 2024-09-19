# sentiment-analysis-api

## uvicorn main:app --reload to start the server

## curl -X POST http://127.0.0.1:8000/analyze_sentiment/ -H "Content-Type: application/json" -d '{"text": "I love programming"}'

## curl -X POST http://127.0.0.1:8000/analyze_batch_sentiment/ -H "Content-Type: application/json" -d '{"texts": ["I love programming", "I hate programming"]}'