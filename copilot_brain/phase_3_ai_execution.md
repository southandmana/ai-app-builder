

# Phase 3 – Copilot Builds Your App (For Everyone)

**Note:** For a full list and explanation of software development methods (like Agile or Scrum), see [`copilot_brain/methodologies_and_best_practices.md`](methodologies_and_best_practices.md).

---

## How This Step Works

**What Copilot will do automatically:**
- Copilot will generate your app’s code, tests, and setup files based on your planning documents.
- Copilot will handle all technical details unless you want to provide your own code or files.

**What you need to do:**
- If you have your own code or want to upload files, you can do so when asked.
- If not, just say “continue” and Copilot will do everything for you.

**Tip:** Copilot will always ask before overwriting anything you’ve provided.

---

## What You’ll Create in This Step
You’ll end up with these files (Copilot will save them in the right place):
- codebase/ (source code files)
- tests/ (unit, integration, and e2e tests)
- ci_cd_workflows.md
- acceptance_criteria.md (imported from Phase 2, extended with code-level checks)
- tech_stack.md (imported from Phase 2, may be refined)
- configs/ (environment and build configs)

This phase is about letting Copilot build your app for you. You don’t need to know any technical terms—just answer questions in your own words, or let Copilot do it all.

---

## Step 1 – Prepare Inputs
**Short description:** Collect everything needed before execution.
- Upload high-detail flow diagrams (per screen).
- Upload six deliverables per flow (user, data, state, API, error, security).
- Upload component architecture document.
- Upload acceptance criteria document.
- Upload tech stack decision document.
- Optionally: include configs/tests/scripts (from Phase 2 or starter folders) to improve alignment.

---

## Step 2 – Guided Execution by Copilot
**Short description:** Generate code step by step.
- Work on one component at a time.
- Track progress (e.g., “3/6 deliverables completed”).
- For each component:
  - Generate implementation code.
  - Verify against acceptance criteria.
  - Ensure compatibility with chosen tech stack.
- Stop after each deliverable to validate before moving on.

---

## Step 3 – Embed Best Practices
**Short description:** Ensure outputs follow standards from earlier assets.
- **From code.zip**
  - Respect environment configs (dev/staging/prod).
  - Align generated tests with e2e categories (calls, payments, matchmaking).
  - Ensure compatibility with `.devcontainer` and `.vscode` setups.

- **From github.zip**
  - Generate/update CI/CD workflows (lint, test, build, deploy).
  - Include security scans (secrets detection, static analysis).
  - Ensure workflows trigger on pull requests and merges.

- **From handbook.zip**
  - Apply contract-driven design (interfaces, events, error codes).
  - Include resilience rules (retries, recovery, backup paths).
  - Embed observability hooks (logs, metrics, dashboards, alerts).
  - Consider cost/performance tradeoffs (avoid inefficient patterns).

- **From more.zip**
  - Enforce code style (ESLint, Prettier, commit hooks).
  - If TypeScript is selected, use strict configs (`tsconfig.base.json`).
  - Maintain clean commit history (commitlint rules).

---

## Step 4 – Iteration Loop
**Short description:** Build, check, refine.
- If generated output fails acceptance criteria, refine until it passes.
- If flow diagrams are updated, regenerate only the affected deliverables.
- Always adapt outputs to the selected tech stack (never assume defaults).

---

## Step 5 – User Interaction Rules
**Short description:** Guide the user through execution.
- For each step, show a short description of what is happening.
- Ask: “Do you already have the required input?”
  - If **yes**, proceed.
  - If **no**, expand instructions for preparing the input.
- After each generated deliverable:
  - Confirm completion count (e.g., 2/6 done).
  - Remind user to test in CI/CD pipeline.

---

## Step 6 – Deliverables of Phase 3
**Short description:** End results of execution.
1. Generated codebase for frontend, backend, media/calling, and infra components.
2. Config-aware setup for dev/staging/prod.
3. Automated tests aligned with acceptance criteria.
4. GitHub workflows for CI/CD, security, and releases.
5. Observability hooks (metrics, logs, alerts).
6. Cost/performance guardrails embedded in design.

---

**Outcome:** By the end of Phase 3, you will have a working, testable codebase generated and refined with AI, ready to move into testing and iteration (Phase 4).

