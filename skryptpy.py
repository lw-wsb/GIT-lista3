import subprocess
import json

def make_request(url):
    try:
        response = subprocess.check_output(['curl', '-s', url])
        return response.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return None

def check_response(response, required_keys):
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        return False

    for key in required_keys:
        if key not in data:
            return False
    return True

def run_tests():
    tests = [
        {
            'url': 'https://jsonplaceholder.typicode.com/posts/1',
            'required_keys': ['userId', 'id', 'title', 'body']
        },
        {
            'url': 'https://jsonplaceholder.typicode.com/users/1',
            'required_keys': ['id', 'name', 'username', 'email']
        },
        {
            'url': 'https://jsonplaceholder.typicode.com/todos/1',
            'required_keys': ['userId', 'id', 'title', 'completed']
        }
    ]

    for i, test in enumerate(tests):
        response = make_request(test['url'])
        if response is None:
            print(f'Test {i+1}: FAILED (No response)')
            continue

        if check_response(response, test['required_keys']):
            print(f'Test {i+1}: PASSED')
        else:
            print(f'Test {i+1}: FAILED')

if __name__ == '__main__':
    run_tests()
