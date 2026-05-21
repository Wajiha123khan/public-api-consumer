# ANSWERS

## 1. How to run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 2. Stack choice

I chose Python because it is simple, readable, and excellent for working with APIs. The requests library makes HTTP requests easy to handle.
A worse choice would have been using a very heavy framework for such a small CLI project because it would add unnecessary complexity.

## 3. One real edge case

Edge case handled:
User enters an empty country name.
File:
main.py
Line:
The validation inside main() before API call.
Without this handling, the API request would be invalid and the user experience would be confusing.

## 4. AI usage

I used Claude for:
- understanding assessment requirements
- improving project structure
- generating initial README structure

One thing I changed:
I modified the generated error handling code to make messages more user-friendly and readable.

## 5. Honest gap
One thing missing is automated testing.
With another day, I would add unit tests and improve the UI formatting for better user experience.