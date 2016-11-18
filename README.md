# Huskyville

Python script for batch evaluation of Watson Q&A API. It reads in questions from `questions.txt` (one per line) and sends them to Watson. It then passes Watson's answer to the function `good_answer()`, where you can put your code to evaluate the answer.

Note this script only has placeholder code for evaluating the answer. You need to write that yourself for the CS4046 assessment.

## Requirements

- Python 2.7
- Python's Requests package (`pip install requests`)

## Installation

1. `pip install requests`
2. Make sure the URL points to your Watson instance
3. Put your username/password for the Watson instance into the `username`/`password` variables
4. Run script with `python huskyville.py`

## License

This script is licensed under MIT license
