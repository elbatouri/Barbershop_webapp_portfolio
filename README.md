## Project Background:

The Barbershop Project aimed to create a digital bridge between barbershops and clients. This comprehensive platform facilitates appointment scheduling, client reviews, and a seamless interface for both barbers and clients.
Team Members:
EL BATOURI Rabi : Responsive frontend , user authentication, Database and deployement management
Reda Mjibel : Frontend, and UI Design
Timeline : 3 weeks.
Our dynamic team consisted of skilled individuals taking on various roles. Timely planning and effective communication were the cornerstones of our success. The project unfolded in phases, with each team member contributing their expertise to meet deadlines and deliver a polished product.


# Flask Web App Tutorial

## Setup & Installation

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to https://boroda.elclubourirabi.tech/

## Navigating Code Horizons: The Technical Challenge:

During the development of the appointment dashboard in the barbershop project, a significant technical challenge emerged. The task at hand was to implement dynamic filters for appointments based on both barbers and dates. Given that the data was fetched from a MySQL database through PyMySQL, templated using Jinja2, and routed with Flask, the challenge was to make the dashboard refresh the data seamlessly every time a filter was applied.
The specific task was to create a filtering mechanism that would allow users to filter appointments by barber and date. The difficulty arose due to the need for real-time updates without relying on AJAX, which is a common approach for such scenarios.
To tackle this challenge, I took a proactive approach. Recognizing the complexity, I reached out to several peers and organized a collaborative whiteboarding session. Together, we brainstormed and devised a solution that involved manipulating the DOM directly without using AJAX. This approach ensured that the data in the dashboard would refresh dynamically based on the selected filters.
The result was a successful implementation of the filtering mechanism. The collaborative effort not only resolved the immediate technical challenge but also contributed to the knowledge-sharing within the team. The whiteboarding session, while initially aimed at addressing a specific problem, turned into a valuable learning experience for all involved, laying the groundwork for future projects.
