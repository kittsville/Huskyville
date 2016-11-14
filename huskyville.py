import requests

url      = 'https://dal09-gateway.watsonplatform.net/instance/561/deepqa/v1/question'
username = 'YOUR_USERNAME_HERE'
password = 'YOUR_PASSWORD_HERE'

# YOUR ANSWER PROCESSING LOGIC HERE
def good_answer(answer):
    if 'back pain' in answer:
        return True
    else:
        return False

if username == 'YOUR_USERNAME_HERE' or password == 'YOUR_PASSWORD_HERE':
    print 'You need to enter a valid username/password for the Watson Q&A service'
    sys.exit(1)

headers = {
    'Content-Type'  : 'application/json'
}

print 'Loading questions from "questions.txt"'

with open('questions.txt', 'r') as questions_file:
    questions = [question.strip() for question in questions_file.readlines()]

print 'Loaded {0} questions\nSending to Watson API...'.format(len(questions))

failed       = 0
good_answers = 0
bad_answers  = 0

for question_id, question in enumerate(questions):
    question_data = {
        'question' : {
            'questionText' : question,
            'items'        : 1, # Number of answers to provide
            'evidenceRequest' : {
                'items'   : 1,
                'profile' : 'yes'
            }
        }
    }
    
    print 'Sending #{0} >>>'.format(str(question_id).zfill(3)), # To indicate submission
    
    response = requests.post(url, auth=(username, password), json=question_data, headers=headers)
    
    if response.status_code == 200:
        print 'Answered >>>',
        
        response_json = response.json()
        
        if response_json['question']['status'] != 'Complete':
            print 'Failed (No answer returned)'
            failed += 1
            continue
        
        answer_text = response_json['question']['answers'][0]['text']
        
        if good_answer(answer_text):
            print 'Good Answer'
            good_answers += 1
        else:
            print 'Bad Answer'
            bad_answers += 1
    else:
        print 'Failed (HTTP Code: {0})'.format(response.status_code) # To indicate bad response
        failed += 1
        continue


print 'Submitted: {0}\nGood Answers: {1}\nBad Answers: {2}\nFailed: {3}'.format(len(questions), good_answers, bad_answers, failed)
