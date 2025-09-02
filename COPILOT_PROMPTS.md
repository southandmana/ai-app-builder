# Copilot Prompt Templates — Project-wide Scans

Short, plain-language descriptions followed by ready-to-paste prompts. Each prompt is written so you can copy it straight into Copilot or another assistant. Use them when you want help exploring or changing the whole project.

---

### Overview — What the app looks like
What it does: Gives a simple map of the project's main parts and how they connect.
```text
Scan the project and produce a clear, high-level architecture map: main modules, where the app starts, major libraries it uses, and how data flows between parts. Follow the guide system in GUIDE.md.
```

### Find TODOs — What still needs work
What it does: Lists developer notes like TODO/FIXME with where they are and suggested next steps.
```text
Find all TODO and FIXME comments across the project, show the file and line number for each, explain the situation in plain language, and suggest next steps.
```

### Find likely bugs — Things that may break
What it does: Looks for common mistakes and explains them simply, with a suggested fix.
```text
Search the project for likely bugs and confusing code (e.g., missing checks, inconsistent use of data, duplicated logic). Explain each problem in plain language and suggest a small fix. Use all files.
```

### Security check — Safety issues to fix
What it does: Finds secrets, unsafe data handling, or risky network use and says how to fix them.
```text
Review the project for security issues: exposed secrets, unsafe evaluation of user input, insecure network calls, and risky dependencies. Point to the files and give clear remediation steps.
```

### Dependencies & licenses — What the project relies on
What it does: Lists packages the project uses, if any are out of date, and their license types.
```text
List project dependencies and their versions, flag outdated or vulnerable packages, and note license types and any possible license conflicts. Scan package manifest files across the project.
```

### Refactor suggestions — Make code easier to read
What it does: Suggests simple code cleanups to reduce repetition and improve clarity, with examples.
```text
Suggest targeted refactors to reduce repetition and make code easier to read. Show concrete code change examples for the top 3 opportunities, with file references.
```

### Generate tests — Add safety nets
What it does: Creates unit tests for functions or modules you specify, including edge cases.
```text
Generate unit tests for the functions in <path/to/file> (or 'all modules' for the whole project). Use the project's test framework and include important edge-case tests and simple mocks.
```

### Performance check — Spot slow parts
What it does: Finds parts of the project that may be slow and suggests improvements.
```text
Identify potential performance bottlenecks across the project (slow algorithms, heavy I/O, repetitive work) and suggest practical optimizations with example fixes.
```

### Find unused code — Clean up clutter
What it does: Looks for files or functions that don't seem to be used and suggests safe removals.
```text
Find potentially unused code, files, or exports across the project. Provide a safe removal plan and a shortlist of items to review manually.
```

### CI/CD & release readiness — How to ship safely
What it does: Reviews automation and testing setup and lists missing steps for safe releases.
```text
Review CI/CD configuration and release readiness. List missing checks, recommended pipeline steps, and tests that should run on pull requests. Scan common CI folders (e.g., .github/).
```

### Formatting & linting — Keep code tidy
What it does: Checks style and linting setup and suggests one-line fixes where possible.
```text
Run a repo-wide style and lint checklist: report missing config (e.g., prettier, eslint, black), common style issues, and provide a one-shot command to auto-fix fixable problems.
```

### PR & commit help — Write clearer change notes
What it does: Drafts short, clear PR descriptions and small commit messages based on workspace changes.
```text
Using changes in the workspace, draft a clear pull request description and a set of short, focused commit messages that explain intent and risk.
```

### Follow the project guide — Use the project's rules
What it does: Loads the project's guide (if present) and follows its rules when analyzing or changing code.
```text
Before answering, load the project's guide at /docs/guide.md (if present) and follow its coding conventions and review checklist while scanning the project.
```

### Search helpers — Copy-paste queries for Find tool
What it does: Gives ready-made search queries you can paste into VS Code's Find to locate APIs, database calls, configs, and tests.
```text
Generate a set of glob and regex search queries to locate API endpoints, database calls, config file reads, and tests across the project. Output queries you can paste into your editor.
```

---

### Core scope (recommended)
What it does: A short, clear instruction that tells Copilot/assistant to use the whole project when answering.
```text
Scan the entire project workspace and consider every file under the project root (including .gitignored and hidden files) before answering.
```

Usage notes (plain language):
- Replace placeholders like `<path/to/file>` or `GUIDE.md` with the real file paths in your project.
- If you want to include files normally ignored by version control, add "including .gitignored and hidden files" to the prompt.
- To focus on specific file types, add a line such as: "Only consider files matching: **/*.py, **/package.json".

File: `COPILOT_PROMPTS.md`
Location: project root

If you'd like wording changes, a different filename, or an indexed table of contents, tell me and I'll update the file.

---

### Reorganize Project Structure — Clean and Logical
What it does: Proposes a new folder structure to organize files logically without breaking functionality.
```text
Scan the entire project workspace and propose a new, clean folder structure that organizes files logically. Ensure all necessary changes (e.g., imports, references) are updated to reflect the new structure without breaking functionality.
```

### Proposed Folder Structure
What it does: Provides a clean, logical organization for the project files.
```text
app_project/
│
├── copilot_brain/                  # Copilot’s knowledge base
│   ├── FOLDER_STRUCTURE.md
│   ├── instructions.md
│   ├── phase1_concept_strategy.md
│   ├── phase2_development_planning.md
│   ├── phase3_ai_execution.md
│   ├── phase4_testing_iteration.md
│   └── phase5_launch_growth.md
│
├── user_guide/                     # Human-facing guide
│   ├── how_to_use.md
│   ├── customization_guidance.md
│   ├── feedback_loop.md
│   ├── roles_and_workflows.md
│   └── welcome_and_faq.md
│
├── project_overview/               # Project-level meta files
│   ├── README.md
│   ├── MASTER_GOAL_PROGRESS.md
│   ├── Milestone_Goal_Progress_and_Instructions.md
│   └── UPDATE_PROGRESS_INSTRUCTIONS.md
│
├── phases/                         # All phases grouped together
│   ├── phase1_concept_strategy/
│   ├── phase2_development_planning/
│   │   ├── screen_flows/
│   │   │   └── [screen_name].mmd
│   │   ├── deliverables/
│   │   │   ├── user_flow.md
│   │   │   ├── data_flow.md
│   │   │   ├── state_flow.md
│   │   │   ├── api_service_flow.md
│   │   │   ├── error_exception_flow.md
│   │   │   └── security_privacy_flow.md
│   │   ├── system_architecture.md
│   │   ├── integration_view.md
│   │   ├── functional_architecture.md
│   │   ├── component_architecture.md
│   │   ├── acceptance_criteria.md
│   │   └── tech_stack.md
│   ├── phase3_ai_execution/
│   │   ├── codebase/
│   │   ├── tests/
│   │   ├── configs/
│   │   └── ci_cd_workflows.md
│   ├── phase4_testing_iteration/
│   │   ├── test_results.md
│   │   ├── bug_report.md
│   │   └── ci_cd_logs.md
│   └── phase5_launch_growth/
│       ├── appstore_metadata.md
│       ├── marketing_funnel.md
│       ├── monetization.md
│       ├── retention_systems.md
│       └── trust_safety.md
│
├── recall/                         # Memory layer (auto-generated summaries)
│   └── phaseX_stepY_summary.md
│
├── templates_examples/             # Templates and examples
│   ├── accessibility_guidance.md
│   ├── complex_app_appendix.md
│   ├── copilot_prompts.md
│   ├── feature_checklist.md
│   ├── localization_guidance.md
│   ├── roles_and_collaboration_guidance.md
│   ├── security_privacy_guidance.md
│   ├── troubleshooting_appendix.md
│   └── update_verification_checklist.md
│
├── tests/                          # General tests
│   ├── test_chat_interface.py
│   ├── test_chat_interface_unittest.py
│   └── __pycache__/
│
├── tools/                          # Utility scripts
│   ├── cli_interface.py
│   ├── update_progress.py
│   └── reset_project.py
│
└── .venv/                          # Virtual environment
```
