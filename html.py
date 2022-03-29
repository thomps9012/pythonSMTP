import os
import base64

import pandas as pd
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

body = """
            <bold>Dear {first_name} {last_name},</bold>
            <br />
            <br />
            I recently saw that {company} was looking for a {position}. As a burgeoning web developer who has created several full stack web applications, I believe I would be a great fit for this posting.
            <br/>
            <br/>
            Some relevant skills I have related to this posting are:
                <ol>
                <li>{skill1}</li>
                <li>{skill2}</li>
                <li>{skill3}</li>
                <li>{skill4}</li>
                <li>{skill5}</li>
                </ol>
            Attached is my resume with relevant work experience, and below are links to my online portfolio/blog, GitHub, and LinkedIn profiles.
            <br />
            <br />
            Thank you for your consideration to join your team at {company},
            <br />
            <br />
            Samuel Thompson
            <hr />
            <a target="_blank" href="https://sjtportfolio.herokuapp.com/"><p>Online Portfolio</p></a>
            <a target="_blank" href="https://www.linkedin.com/in/samuel-joseph-thompson/"><p>LinkedIn Profile</p></a>
            <a target="_blank" href="https://github.com/thomps9012"><p>GitHub Profile</p></a>
            <hr />
            216-970-1203
            <br />
            thompsonsamuel097@gmail.com
"""            

from_address='thompsonsamuel097@gmail.com'
filename = 'SamuelThompsonCV.pdf'

data = pd.read_csv('job_search.csv')

for d in data.values:
    # for row in reader:
    body = body.format(company=d[0], first_name=d[1], last_name=d[2], email=d[3], position=d[4], skill1=d[5], skill2=d[6], skill3=d[7], skill4=d[8], skill5=d[9])
    contact = d[3]
    message = Mail(
        from_email=from_address,
        to_emails=d[3],
        subject=f"Interest in {d[4]} Position",
        html_content=body,
    )
    with open(filename, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()
    
    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('SamuelThompsonCV.pdf'),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    message.attachment = attachedFile
    try:
       sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
       response = sg.send(message)
       print(response.status_code)
       print(response.body)
       print(response.headers)
    except Exception as e:
            print(e)
