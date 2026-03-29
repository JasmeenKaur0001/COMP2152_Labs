class Report:
    def __init__(self, team_name):
        self.team_name = team_name
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)

    def get_by_severity(self, severity):
        return [f for f in self.findings if f.severity == severity]

    def summary(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self.findings)}")

        high = len([f for f in self.findings if f.severity == "HIGH"])
        medium = len([f for f in self.findings if f.severity == "MEDIUM"])
        low = len([f for f in self.findings if f.severity == "LOW"])

        print(f"  HIGH:   {high}")
        print(f"  MEDIUM: {medium}")
        print(f"  LOW:    {low}")
        print("  ----------------------------------------")

        for f in self.findings:
            print(f)
