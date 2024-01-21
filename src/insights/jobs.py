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

    def filter_by_multiple_criteria(self, list_jobs: List[Dict],
                                    filter_criteria: Dict) -> List[dict]:
        #  verifica se o filtro fornecido e um dicionario
        if not isinstance(filter_criteria, dict):
            #  se nao for levanta um erro
            raise TypeError('O filtro fornecido deve ser um dicionario')
        #  cria uma lista vazia para armazenar os trabalhos filtrados
        filtered_jobs = []
        #  iterar sobre os trabalhos na lista de trabalhos
        for job in list_jobs:
            #  verifica se o trabalho atende a todos os criterios de filtro
            match_all_criteria = all(
                #  p/cada chave, o valor e igual ao valor do criterio de filtro
                job.get(key) == value for key, value in filter_criteria
                .items())
            #  se o trabalho atender a todos os criterios de filtro
            if match_all_criteria:
                #  adiciona o trabalho a lista de trabalhos filtrados
                filtered_jobs.append(job)
        #  retorna a lista de trabalhos filtrados
        return filtered_jobs
