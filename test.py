from data.db_session import create_session, global_init
from data.marsian import User
from data.jobs import Jobs


if __name__ == "__main__":
    name = input().strip()
    global_init(name)
    sess = create_session()
    jobs = sess.query(Jobs).all()
    max_length = max([len(i.collaborators.split(',')) for i in jobs])
    leads = set()
    for job in jobs:
        if len(job.collaborators.split(",")) == max_length:
            leads.add(job.user)
    for lead in leads:
        print(f"{lead.name} {lead.surname}")
