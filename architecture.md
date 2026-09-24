# System Architecture

## Architecture Diagram

```text
                    USER
                      |
                      v
                +-------------+
                |   main.py   |
                | Main Menu   |
                +-------------+
                   /    |    \
                  /     |     \
                 v      v      v
        +----------+ +----------+ +----------+
        |profile.py| |tracker.py| |analysis.py|
        +----------+ +----------+ +----------+
             |           |             |
             v           v             v
        User Profile   Daily        Health
        & BMI          Records      Analysis
             \           |             /
              \          |            /
               \         v           /
                +-------------------+
                |    display.py     |
                | Results & Reports |
                +-------------------+
                         |
                         v
                  FINAL REPORT