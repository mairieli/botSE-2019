from pydriller import RepositoryMining
import iocsv
import csv

repos = iocsv.read_csv_repos_fil("data_filtered.csv")

out = open('project_bot.csv', 'w')
w_out = csv.writer(out)

for commit in RepositoryMining(path_to_repo=repos, only_modifications_with_file_types= ['.yml']).traverse_commits():
    files = []
    for mod in commit.modifications:
        if mod.filename == "stale.yml":
            file = [commit.project_name, mod.change_type.name, commit.in_main_branch, commit.hash, commit.msg, commit.author.name, commit.committer.name, commit.merge, 
                commit.author_date.strftime("%Y-%m-%d %H:%M:%S"), mod.source_code, mod.diff, mod.added, mod.removed]

            files.append(file)
            break

    if files:        
        w_out.writerow(files)
        out.flush()
out.close()



