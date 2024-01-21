import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding='utf-8') as file:
            jobs_reader = csv.DictReader(file)
            self.jobs_list = list(jobs_reader)
            return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        #   cria um conjunto vazio(que armazem valores unicos)
        unique_job_types = set()
        #   iterar sobre trabalho(dicionario) na lista de trabalhos
        for job in self.jobs_list:
            #   obtem o tipo de trabalho(get retorna None se nao existir)
            job_type = job.get('job_type')
            #   se existi um job_type mesmo tirando espaço em branco iniciofim
            if job_type and job_type.strip():
                #    adiciona o job_type ao conjunto
                unique_job_types.add(job['job_type'])
        #   converte o conjunto em uma lista e a retorna
        return list(unique_job_types)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
