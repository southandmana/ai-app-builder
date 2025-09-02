# AI App Builder

## Overview
The AI App Builder is a CLI-based tool designed to guide users through the process of planning, building, testing, and launching an app. It leverages a structured workflow divided into five distinct phases:

1. **Concept & Strategy**: Define the app's purpose and strategy.
2. **Development Planning**: Plan the app's architecture, user flows, and technical stack.
3. **AI Execution**: Build the app using AI-driven tools.
4. **Testing & Iteration**: Test and refine the app to ensure quality.
5. **Launch & Growth**: Deploy the app and set up growth strategies.

## Features
- Step-by-step guidance through each phase of app development.
- Dynamic file generation for deliverables.
- Automated testing and CI/CD workflows.
- Support for app store submission and marketing setup.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/southandmana/ai-app-builder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-app-builder
   ```
3. Run the CLI:
   ```bash
   python cli_interface.py
   ```

## Requirements
- Python 3.7 or higher
- No external dependencies required (uses Python's standard library).

## Project Structure
- `phase1_concept_strategy/`: Files and deliverables for Phase 1.
- `phase2_development_planning/`: Files and deliverables for Phase 2.
- `phase3_ai_execution/`: Codebase and tests for Phase 3.
- `phase4_testing_iteration/`: Logs and reports for Phase 4.
- `phase5_launch_growth/`: Metadata and marketing materials for Phase 5.

## Resetting the Project

To reset the project and delete all generated files, run the following command:

```bash
python reset_project.py
```

You will be prompted to confirm the reset before any files are deleted.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
