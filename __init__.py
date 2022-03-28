import smtplib, ssl, csv

            
message = """
            Subject: Application for {position} at {company}


            Dear {first_name} {last_name},
                I am submitting my application for consideration regarding the {position} position with you at {company}.
            <br />
            The relevant skills I have related to this position are:
            <ul>
                <li>{skill1}</li>
                <li>{skill2}</li>
                <li>{skill3}</li>
                <li>{skill4}</li>
                <li>{skill5}</li>
            </ul>
                As a full stack web development bootcamp graduate and current software engineer and developer, I have experience creating web applications that solve unique business and user needs, and integrate / redevelop continuously based on user feedback. I would love to bring my multidisciplinary approach, unique life experiences, and a commitment to excellence by building software that solves problems across platforms through uncommon ideas and designs.
            <br />
            Attached is my resume with relevant work experience, and below are links to my online portfolio, GitHub, and LinkedIn profiles.
            <br />
            <br />
            Thank for you the opportunity to join your team at {company},
            Samuel Thompson
            <a target="_blank" href="https://www.sjtportfolio.herokuapp.com"><p>Online Portfolio</p></a>
            <a target="_blank" href="https://www.linkedin.com/in/samuel-joseph-thompson/"><p>LinkedIn Profile</p></a>
            <a target="_blank" href="https://github.com/thomps9012"><p>GitHub Profile</p></a>
           """

from_address="thomps9012@gmail.com"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("job_search.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for company, position, first_name, last_name, email, skill1, skill2, skill3, skill4, skill5 in reader:
            server.sendmail(
                from_address,
                email,
                message.format(company=company,position=position,first_name=first_name, last_name=last_name, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, skill5=skill5),
            )