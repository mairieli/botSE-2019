import subprocess
import csv
import iocsv

if __name__ == "__main__":
    pull_out = open('data.csv', 'w')
    w_pull_out = csv.writer(pull_out)

    db_user = os.environ['DB_USER']
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']
    db_pass = os.environ['DB_PASS']

    command = f"mysql -ss -u {db_user} -h {db_host} --port={db_port} -p{db_pass} -e 'use ghtorrent;"

    repos = iocsv.read_csv("projects.csv")
    for r in repos:

        sql = "select p.forked_from from projects p, users u where p.owner_id = u.id and p.name = \"{}\" and u.login = \"{}\";'".format(r['repo'], r['owner'])

        process = subprocess.Popen("{}{}".format(command, sql),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               stdin=subprocess.PIPE,
                               shell=True)

        stdout, _ = process.communicate()

        write = stdout.decode("utf-8")
        pull = [r['owner'], r['repo'], write.strip()]
     
        w_pull_out.writerow(pull)
        pull_out.flush()

    pull_out.close()
