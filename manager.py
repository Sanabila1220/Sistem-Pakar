class Agent:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.completed_tasks = []

    def can_do(self, task):
        return task in self.skills

    def perform(self, task):
        self.completed_tasks.append(task)
        return f"{self.name} menyelesaikan tugas: {task}"


class MultiAgentManager:
    def __init__(self):
        self.agents = [
            Agent("Agent A", ["mengumpulkan data", "menganalisis data"]),
            Agent("Agent B", ["menganalisis data", "membuat laporan"]),
            Agent("Agent C", ["membuat laporan", "memeriksa hasil"])
        ]

    def assign_task(self, task):
        for agent in self.agents:
            if agent.can_do(task):
                result = agent.perform(task)
                print(result)
                return

        print(f"Tidak ada agen yang mampu mengerjakan: {task}")

    def run(self):
        print("=== MULTI-AGENT SYSTEM ===")

        tasks = [
            "mengumpulkan data",
            "menganalisis data",
            "membuat laporan",
            "memeriksa hasil"
        ]

        for task in tasks:
            print(f"\nManager memberikan tugas: {task}")
            self.assign_task(task)

        print("\n=== RINGKASAN TUGAS ===")
        for agent in self.agents:
            print(f"{agent.name}: {len(agent.completed_tasks)} tugas selesai")


def run_multi_agent():
    manager = MultiAgentManager()
    manager.run()