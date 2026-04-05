# ============================================================
#  WEEK 12 LAB — Q1: SCANNER INHERITANCE
#  COMP2152 — [Your Name Here]
# ============================================================

import socket
import urllib.request


class Scanner:
    """Parent class — shared by all scanner types."""

    def __init__(self, target):
        self.target = target
        self.results = []

    # TODO: Write display_results(self)
    #   Print "Results for {self.target}:"
    #   If self.results is empty: print "  (no results)"
    #   Otherwise: print each result with "  " indent
    def display_results(self):
        pass


class PortScanner(Scanner):
    def __init__(self, target, ports):
        super().__init__(target)
        self.ports = ports

    def scan(self):
        print(f"\nScanning ports on {self.target}...")
        for port in self.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((self.target, port))
            if result == 0:
                self.results.append(f"Port {port} is OPEN")
            else:
                self.results.append(f"Port {port} is CLOSED")
            s.close()



class HTTPScanner(Scanner):
    """Child class — scans HTTP paths for accessible pages."""

    # class HTTPScanner(Scanner):
    def __init__(self, target, paths):
        super().__init__(target)
        self.paths = paths

    def scan(self):
        print(f"\nChecking HTTP paths on {self.target}...")
        for path in self.paths:
            url = f"http://{self.target}/{path}"
            try:
                urllib.request.urlopen(url, timeout=2)
                self.results.append(f"/{path} exists (200 OK)")
            except:
                self.results.append(f"/{path} not found")



# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: SCANNER INHERITANCE")
    print("=" * 60)

    print("\n--- Port Scanner ---")
    ps = PortScanner("127.0.0.1", [22, 80, 443])
    print(f"  Scanning {ps.target} ports...")
    ps.scan()
    ps.display_results()

    print("\n--- HTTP Scanner ---")
    hs = HTTPScanner("127.0.0.1", ["/", "/admin", "/.git/config"])
    print(f"  Scanning {hs.target} paths...")
    hs.scan()
    hs.display_results()

    print("\n" + "=" * 60)