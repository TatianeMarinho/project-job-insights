from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            salary = job.get("max_salary")
            # isdigit() verifica se contem apenas digitos
            if salary is not None and salary.strip() and salary.isdigit():
                salary_int = int(salary)
                max_salary = max(max_salary, salary_int)
        return max_salary

    def get_min_salary(self) -> int:
        # float("inf") retorna o maior valor float possivel
        min_salary = float("inf")
        for job in self.jobs_list:
            salary = job.get("min_salary")
            # isdigit() verifica se contem apenas digitos
            if salary is not None and salary.strip() and salary.isdigit():
                salary_int = int(salary)
                min_salary = min(min_salary, salary_int)
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
