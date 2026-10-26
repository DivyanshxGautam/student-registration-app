import os
import sys
from bs4 import BeautifulSoup

def test_registration_form():
    html_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    if not os.path.exists(html_path):
        print(f"FAILED: {html_path} does not exist.")
        sys.exit(1)

    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # 1. Verify form container
    form = soup.find('form', id='studentForm')
    assert form is not None, "Form element with id='studentForm' is missing"

    # 2. Check for required input elements
    checks = {
        "Student Name Field": soup.find('input', {'id': 'studentName'}),
        "Roll Number Field": soup.find('input', {'id': 'rollNumber'}),
        "Email Field": soup.find('input', {'id': 'email', 'type': 'email'}),
        "Course Field": soup.find('select', {'id': 'course'}),
        "Submit Button": soup.find('button', {'id': 'submitBtn'})
    }

    failed = False
    for field_name, element in checks.items():
        if element:
            print(f"✓ PASS: {field_name} found")
        else:
            print(f"✗ FAIL: {field_name} missing")
            failed = True

    if failed:
        sys.exit(1)
    
    print("\nSUCCESS: All form elements verified successfully!")

if __name__ == '__main__':
    test_registration_form()