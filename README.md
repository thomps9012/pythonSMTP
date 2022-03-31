# Job Hunter Simple Mail Transfer Protocol (SMTP)

## Description
Ever wanted to apply for jobs, but can't seem to find the time, much less energy, to organize and track your applications and contacts with hiring managers. Using this SMTP, built with python and SendGrid, you'll be able to email hiring managers and recruiters with your resume, relevant skills, and links to online presences.

### Features
- Using Hyper Text Markup Language (HTML) customize the email as you'd like
- Up to 100 emails able to be sent daily (using SendGrid's Free tier)
- Automatically attach your resume and relevant skills in the email
- Encoded security using the base64 encoding systems

### Instructions
1. Fork the repository
2. Download and install the necessary dependencies using
```
pip install sendgrid
pip install pandas
```
3. Create a Comma Seperated Value (CSV) file with the following information:
    1. Company (company)
    2. First Name of Contact (first_name)
    3. Last Name of Contact (last_name)
    4. Email (email)
    5. Position Applying for (position)
    6. Relevant Skill 1 (skill1) 
    7. Relevant Skill 2 (skill2) 
    8. Relevant Skill 3 (skill3) 
    9. Relevant Skill 4 (skill4) 
    10. Relevant Skill 5 (skill5)
4. Upload your Resume in your preferred format
5. Create an environment variable on your local machine labelled SENDGRID_API_KEY
    - Prerequisites
        - GitBash or Command Prompt Knowledge
    1. GitBash Instructions
        - Open a GitBash shell then run the following commands
        ```
          $  export SENDGRID_API_KEY="your api key here"
        ```
        - Double check that the your environment variable was properly set
        ```
          $ echo $SENDGRID_API_KEY
        ```

    2. Windows User Interface Instructions
        - Open up the System Properties of your computer
        - Click on the 'Envrionment Variables' button
        - Click the 'New' button under user variables
        - Set the Variable name to SENDGRID_API_KEY
        - Set the Variable value to the actual api key

    3. Mac Instructions
        - Follow this great [Tutorial](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255)
6. Make any changes you deem necessary to the email template
    - unless you'd like to apply to jobs for me :)
7. Run the application using either of the two methods below!
    - Open html.py in VSCode and click the *** Run Python File Button *** in the upper right corner
    - Open a terminal and run the following command
        ``` python html.py ```

### Technical Specifications
- Python
- SendGrid
- GitBash or Command Prompt
- HTML
- PIP Installer

### License
MIT License

Copyright (c) [2022] [Job Hunter Simple Mail Transfer Protocol]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.