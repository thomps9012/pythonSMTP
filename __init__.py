import yagmail
import pandas as pd
from googleapiclient.errors import HttpError

message = """
            Dear {first_name} {last_name},
                
                I am submitting my application for consideration regarding the {position} position with you at {company}.

            The relevant skills I have related to this position are:

                - {skill1}
                - {skill2}
                - {skill3}
                - {skill4}
                - {skill5}
                
            As a full stack web development bootcamp graduate and current software engineer and developer, I have experience creating web applications that solve unique business and user needs, and integrate / redevelop continuously based on user feedback. I would love to bring my multidisciplinary approach, unique life experiences, and a commitment to excellence by building software that solves problems across platforms through uncommon ideas and designs.

            Attached is my resume with relevant work experience, and below are links to my online portfolio, GitHub, and LinkedIn profiles.

            Thank for you the opportunity to join your team at {company},

            Samuel Thompson
            
            <a target="_blank" href="https://www.sjtportfolio.herokuapp.com"><p>Online Portfolio</p></a>
            <a target="_blank" href="https://www.linkedin.com/in/samuel-joseph-thompson/"><p>LinkedIn Profile</p></a>
            <a target="_blank" href="https://github.com/thomps9012"><p>GitHub Profile</p></a>
"""            

from_address="thompsonsamuel097@gmail.com"
filename = 'SamuelThompsonCV.pdf'

yag = yagmail.SMTP('thompsonsamuel097@gmail.com', oauth2_file='~/oauth2_creds.json' )


data = pd.read_csv('job_search.csv')

for d in data.values:
    # for row in reader:
    body = message.format(company=d[0], first_name=d[1], last_name=d[2], email=d[3], position=d[4], skill1=d[5], skill2=d[6], skill3=d[7], skill4=d[8], skill5=d[9])
    contact = d[3]
    try:
        yag.send(to=contact,
        contents = body,
        subject=f"Application for {d[4]} at {d[0]}",
        attachments = filename
        )
        print('success')
    except HttpError as error:
            print(f'An error occurred: {error}')
