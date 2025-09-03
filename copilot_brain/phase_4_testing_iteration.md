# Phase 4 – Copilot Tests and Improves Your App (For Everyone)

**Note:** For a full list and explanation of software development methods (like Agile or Scrum), see [`copilot_brain/methodologies_and_best_practices.md`](methodologies_and_best_practices.md).

---

## How This Step Works

**What Copilot will do automatically:**
- Copilot will run tests, check for bugs, and summarize results for you.
- Copilot will handle all technical details unless you want to provide your own test cases or bug reports.

**What you need to do:**
- If you have your own tests or want to upload bug reports, you can do so when asked.
- If not, just say “continue” and Copilot will do everything for you.

**Tip:** Copilot will always ask before overwriting anything you’ve provided.

---

## What You’ll Create in This Step
You’ll end up with these files (Copilot will save them in the right place):
- test_results.md
- bug_report.md
- ci_cd_logs.md

This phase is about letting Copilot test your app and help you fix any issues. You don’t need to know any technical terms—just answer questions in your own words, or let Copilot do it all.

---

## Step 1 – Prepare Test Environment
**Short description:** Set up everything needed for testing.
- Ensure dev/staging environments are live (as defined in configs).
- Connect CI/CD pipeline (GitHub workflows) to run tests automatically.
- Verify observability stack (logs, metrics, dashboards) is active.

---

## Step 2 – Run Unit & Component Tests
**Short description:** Validate small pieces of the system.
- Run unit tests for UI components, services, and utilities.
- Run component tests to confirm modules interact correctly.
- Check that style/lint rules (ESLint, Prettier) pass.
- Acceptance criteria: each test passes without manual overrides.

---

## Step 3 – Run Integration & API Tests
**Short description:** Test services working together.
- Run integration tests for data flow between frontend and backend.
- Test APIs against contract definitions (interfaces, events, error codes).
- Ensure error/timeout paths behave as expected.
- Acceptance criteria: all core flows meet contract rules.

---

## Step 4 – Run End-to-End (E2E) Tests
**Short description:** Test complete user journeys.
- Use the e2e test scripts (calls, payments, matchmaking).
- Simulate real user flows across multiple devices/environments.
- Acceptance criteria: golden paths always succeed, failure paths recover gracefully.

---

## Step 5 – Load & Stress Testing
**Short description:** Check performance under pressure.
- Run load tests (e.g., thousands of calls/events).
- Run stress tests to simulate unexpected spikes or resource exhaustion.
- Monitor system response times, error rates, and recovery.
- Acceptance criteria: system stays within performance budgets (cost-aware).

---

## Step 6 – Security & Compliance Testing
**Short description:** Ensure safety and trust.
- Run static analysis (CodeQL) and secret scans.
- Perform penetration tests or vulnerability scans.
- Validate data handling complies with privacy and retention policies.
- Acceptance criteria: no critical vulnerabilities, policies enforced.

---

## Step 7 – Bug Triage & Fixing
**Short description:** Address issues found during tests.
- Collect bug reports from CI/CD and observability logs.
- Prioritize issues (critical, major, minor).
- Fix issues component by component.
- Acceptance criteria: all critical and major bugs resolved before release.

---

## Step 8 – Iteration Cycle
**Short description:** Repeat until stable.
- Rerun all tests after fixes.
- Ensure regression tests confirm old bugs do not return.
- Iterate until all acceptance criteria are consistently met.

---

## Step 9 – Edge Case and Regression Testing
**Short description:** Ensure robustness by testing edge cases and preventing regressions.
- Identify edge cases for each feature (e.g., invalid inputs, boundary values).
- Create regression tests to ensure previously fixed bugs do not reoccur.
- Use automated tools to run regression tests after every major change.
- Acceptance criteria: All edge cases pass, and no regressions are detected.
### Edge Case and Regression Testing (Expanded)
- Use tools like Selenium or Cypress for automated regression tests.
- Test boundary values, invalid inputs, and rare user behaviors.
- Example: For a login feature, test with empty fields, special characters, and long passwords.

---

## Step 10 – Advanced Scenarios
**Short description:** Test complex and rare scenarios.
- Simulate rare user behaviors (e.g., simultaneous actions, high-latency environments).
- Test under extreme conditions (e.g., low battery, poor network).
- Acceptance criteria: App remains functional and stable under all tested scenarios.
### Advanced Scenarios (Expanded)
- Simulate high-latency environments using tools like Network Link Conditioner.
- Test on low-spec devices to ensure performance remains acceptable.

---

## Step 11 – Deliverables of Phase 4
**Short description:** Outputs after iteration.
1. Fully tested codebase with all acceptance criteria met.
2. Passing test suite (unit, integration, e2e, load, security).
3. Stable staging environment ready for release.
4. Logs and reports documenting performance, resilience, and compliance.

---

## Progress Updates
After completing each step, display progress in the format:
"Step [X] of [Total Steps in this Phase] complete ✅ (next up: Step [X+1] – [Step Title])"

## Recall Summaries
Generate a summary file for each step in `/recall/phase4_stepY_summary.md`.

---

**Outcome:** By the end of Phase 4, the app will be stable, secure, and validated against all acceptance and performance criteria, ready for launch in Phase 5.

